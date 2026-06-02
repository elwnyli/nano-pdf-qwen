<div align="center">

[![English](https://img.shields.io/badge/English-active-blue?style=for-the-badge)](README.md)
&nbsp;&nbsp;
[![中文](https://img.shields.io/badge/中文-切换-red?style=for-the-badge)](README.zh.md)

</div>

---

# nano-pdf-qwen

A PDF editor using natural language instructions — powered by **Qwen (Tongyi Qianwen)**.  
Inspired by [nano-pdf](https://github.com/gavrielc/Nano-PDF).

## vs nano-pdf

| | nano-pdf (original) | nano-pdf-qwen (this) |
|---|---|---|
| AI Model | Gemini 3 Pro Image | Qwen (Tongyi Qianwen) |
| Editing | AI visual editing | Text block positioning + PyMuPDF |
| Local mode | No | Yes (keyword matching, free & offline) |
| API Key | GEMINI_API_KEY | DASHSCOPE_API_KEY (optional) |
| System deps | tesseract + poppler | None |

## Install

```bash
git clone https://github.com/elwnyli/nano-pdf-qwen.git ~/.claude/skills/nano-pdf-qwen
pip install PyMuPDF dashscope
```

## Usage

```bash
# Local mode (free, no API key needed)
python qwen_pdf_edit.py document.pdf 1 "remove watermark"

# Qwen AI mode
export DASHSCOPE_API_KEY="your-key"
python qwen_pdf_edit.py document.pdf 1 "change subtitle to 2026 Annual Report"
```

## Get Qwen API Key

Visit [Alibaba Bailian](https://bailian.console.aliyun.com).

## Credits

Inspired by [nano-pdf](https://github.com/gavrielc/Nano-PDF) by [@gavrielc](https://github.com/gavrielc).

## License

MIT
