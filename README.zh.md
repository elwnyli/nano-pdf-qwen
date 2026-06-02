<div align="center">

[![English](https://img.shields.io/badge/English-Switch-blue?style=for-the-badge)](README.md)
&nbsp;&nbsp;
[![中文](https://img.shields.io/badge/中文-当前-red?style=for-the-badge)](README.zh.md)

</div>

---

# nano-pdf-qwen

基于 [nano-pdf](https://github.com/gavrielc/Nano-PDF) 理念，使用**通义千问**的自然语言 PDF 编辑器。

## vs nano-pdf

| | nano-pdf（原版） | nano-pdf-qwen（本版） |
|---|---|---|
| AI 模型 | Gemini 3 Pro Image | 通义千问 (Qwen) |
| 编辑方式 | AI 视觉编辑 | 文本块定位 + PyMuPDF 精确操作 |
| 本地模式 | 不支持 | 支持（关键词匹配，免费离线） |
| API Key | GEMINI_API_KEY | DASHSCOPE_API_KEY（可选） |
| 系统依赖 | tesseract + poppler | 无 |

## 安装

```bash
git clone https://github.com/elwnyli/nano-pdf-qwen.git ~/.claude/skills/nano-pdf-qwen
pip install PyMuPDF dashscope
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

访问 [阿里云百炼](https://bailian.console.aliyun.com)。

## 致谢

本技能受 [nano-pdf](https://github.com/gavrielc/Nano-PDF)（作者 [@gavrielc](https://github.com/gavrielc)）启发。

## 许可证

MIT
