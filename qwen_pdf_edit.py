#!/usr/bin/env python3
"""
Qwen PDF Editor — natural language PDF editing.
Dual mode: local keyword matching (free, no API needed) or Qwen AI (DashScope).
Uses PyMuPDF for precise text operations.

Install: pip install PyMuPDF dashscope
"""

import sys
import os
import json
import re
import fitz  # PyMuPDF

DASHSCOPE_KEY = os.environ.get("DASHSCOPE_API_KEY", "")


# ── text extraction ──────────────────────────────────────────────

def get_text_blocks(page):
    """Extract all text blocks with bounding boxes from a page."""
    blocks = page.get_text("blocks")
    result = []
    for i, b in enumerate(blocks):
        x0, y0, x1, y1, text, block_type, _ = b
        if text.strip():
            result.append({
                "id": i,
                "text": text.strip(),
                "x0": round(x0, 1), "y0": round(y0, 1),
                "x1": round(x1, 1), "y1": round(y1, 1),
            })
    return result


# ── Qwen AI analysis ─────────────────────────────────────────────

def ask_qwen(instruction, blocks_text):
    """Use Qwen LLM to map natural-language instruction to edit actions."""
    if not DASHSCOPE_KEY:
        return None

    prompt = f"""你是一个PDF编辑助手。

用户指令: {instruction}

页面上有以下文本块（含坐标）:
{blocks_text}

请返回JSON（仅JSON，无其他文字）:
{{"actions":[{{"action":"remove"|"replace","target":"匹配文本关键词","new_text":"替换文本"}}]}}"""

    try:
        from dashscope import Generation
        resp = Generation.call(
            model="qwen-plus",
            messages=[{"role": "user", "content": prompt}],
            result_format="message",
        )
        if resp.status_code == 200:
            text = resp.output.choices[0].message.content.strip()
            if text.startswith("```"):
                text = text.split("\n", 1)[1].rsplit("```", 1)[0]
            return json.loads(text)
        else:
            print(f"  Qwen API 返回错误: {resp.code} - {resp.message}")
    except Exception as e:
        print(f"  Qwen API 异常: {e}")
    return None


# ── local keyword matching ───────────────────────────────────────

def local_match(instruction):
    """Fallback: extract target text from instruction using keyword patterns."""
    actions = []
    del_markers = ["删除", "去掉", "移除", "去除", "remove", "delete", "抹掉"]
    for kw in del_markers:
        if kw in instruction.lower():
            _, _, after = instruction.lower().partition(kw)
            target = after.strip().strip("'\"「『』」\"'")
            if target:
                actions.append({"action": "remove", "target": target})
                return {"actions": actions}

    # Quoted strings
    for m in re.finditer(r"['\"「『](.+?)['\"」』]", instruction):
        actions.append({"action": "remove", "target": m.group(1)})

    # Replace patterns
    rep = re.match(r".+把.+['\"「『]?(.+?)['\"」』]?\s*(?:改成?|替换(?:成|为)?|改为)\s*['\"「『]?(.+?)['\"」』]?$", instruction)
    if rep:
        actions.append({"action": "replace", "target": rep.group(1), "new_text": rep.group(2)})

    return {"actions": actions} if actions else None


# ── apply edits ──────────────────────────────────────────────────

def apply_edits(doc, page_num, blocks, actions):
    """Execute edit actions on the target page."""
    page = doc[page_num]
    modified = 0

    for action in actions.get("actions", []):
        target = action["target"].lower()
        act = action["action"]

        for block in blocks:
            if target in block["text"].lower():
                rect = fitz.Rect(block["x0"], block["y0"], block["x1"], block["y1"])

                if act == "remove":
                    page.add_redact_annot(rect, fill=(1, 1, 1))
                    print(f"  删除: {block['text'][:60]}")
                    modified += 1

                elif act == "replace":
                    new_text = action.get("new_text", "")
                    page.add_redact_annot(rect, fill=(1, 1, 1))
                    page.apply_redactions()
                    tw = fitz.TextWriter(page.rect)
                    fontsize = abs(block["y1"] - block["y0"]) * 0.8
                    tw.append(
                        (block["x0"], block["y0"] + fontsize),
                        new_text,
                        font=fitz.Font("helv"),
                        fontsize=fontsize,
                    )
                    tw.write_text(page)
                    print(f"  替换: {block['text'][:40]} -> {new_text}")
                    modified += 1
                break

    if modified:
        page.apply_redactions()
    return modified


# ── main ─────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 4:
        print("Qwen PDF Editor — 自然语言编辑 PDF")
        print(f"用法: python {os.path.basename(sys.argv[0])} <PDF> <页码> <指令>")
        print(f"示例: python {os.path.basename(sys.argv[0])} doc.pdf 1 '删除 副标题'")
        print(f"\n模式: 设置 DASHSCOPE_API_KEY 启用千问 AI，否则自动使用本地匹配")
        sys.exit(1)

    pdf_path = sys.argv[1]
    page_num = int(sys.argv[2]) - 1
    instruction = " ".join(sys.argv[3:])

    if not os.path.exists(pdf_path):
        print(f"文件不存在: {pdf_path}")
        sys.exit(1)

    print(f"打开: {pdf_path}")
    doc = fitz.open(pdf_path)

    if page_num < 0 or page_num >= len(doc):
        print(f"页码无效: {page_num + 1} (共 {len(doc)} 页)")
        doc.close()
        sys.exit(1)

    # Step 1: extract text blocks
    blocks = get_text_blocks(doc[page_num])
    if not blocks:
        print("页面无文本块（可能是扫描件，千问 AI 模式可处理）")
        doc.close()
        sys.exit(1)

    print(f"提取 {len(blocks)} 个文本块")

    # Step 2: build text representation
    blocks_text = "\n".join(
        f'[{b["id"]}] "{b["text"]}" @({b["x0"]},{b["y0"]})'
        for b in blocks
    )

    # Step 3: get edit actions
    actions = None
    if DASHSCOPE_KEY:
        print("使用千问 AI 分析指令...")
        actions = ask_qwen(instruction, blocks_text)

    if actions is None:
        print("使用本地关键词匹配...")
        actions = local_match(instruction)

    if not actions or not actions.get("actions"):
        print("无法从指令中解析编辑操作")
        print("提示: 试试用引号括起要删除的文字，如 '删除 \"某文字\"'")
        doc.close()
        sys.exit(1)

    print(f"执行 {len(actions['actions'])} 个操作...")

    # Step 4: apply
    modified = apply_edits(doc, page_num, blocks, actions)

    # Step 5: save
    base, ext = os.path.splitext(pdf_path)
    out_path = f"{base}_edited{ext}"
    doc.save(out_path)
    doc.close()

    print(f"\n已保存: {out_path}")
    print(f"修改 {modified} 处")
    print("请打开文件检查效果")


if __name__ == "__main__":
    main()
