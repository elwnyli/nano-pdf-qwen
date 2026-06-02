# nano-pdf-qwen

基于 [nano-pdf](https://github.com/gavrielc/Nano-PDF) 理念的千问版 PDF 编辑器 — 用自然语言指令编辑 PDF。

## 与原版的区别

| | nano-pdf (原版) | nano-pdf-qwen (本版) |
|---|---|---|
| AI 模型 | Gemini 3 Pro Image | 通义千问 (Qwen) |
| 图像编辑 | AI 视觉编辑 | 文本块定位 + PyMuPDF 精确操作 |
| 本地模式 | 无 | 支持（关键词匹配，免费离线） |
| API Key | GEMINI_API_KEY | DASHSCOPE_API_KEY（可选） |
| 系统依赖 | tesseract + poppler | 无 |

## 安装

```bash
# 安装依赖
pip install PyMuPDF dashscope

# 安装技能
cp -r nano-pdf-qwen ~/.claude/skills/
```

## 使用

```bash
# 本地模式（免费，无需 API Key）
python qwen_pdf_edit.py 文档.pdf 1 "删除 水印"

# 千问 AI 模式
export DASHSCOPE_API_KEY="你的key"
python qwen_pdf_edit.py 文档.pdf 1 "把副标题改成 2026 年度报告"
```

## 获取千问 API Key

访问 [阿里云百炼](https://bailian.console.aliyun.com) 创建 API Key。

## 致谢

本技能受 [nano-pdf](https://github.com/gavrielc/Nano-PDF) (by [@gavrielc](https://github.com/gavrielc)) 启发，将 AI 模型替换为通义千问，并增加了本地关键词匹配模式。

## License

MIT
