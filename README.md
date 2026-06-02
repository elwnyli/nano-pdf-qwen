<h1 align="center">nano-pdf-qwen</h1>

<p align="center">
  <a href="https://github.com/elwnyli/nano-pdf-qwen/stargazers"><img src="https://img.shields.io/github/stars/elwnyli/nano-pdf-qwen?style=flat-square&logo=github&color=blue" alt="GitHub stars"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white&style=flat-square" alt="Python"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/elwnyli/nano-pdf-qwen?style=flat-square" alt="License"></a>
</p>

<p align="center">
  <a href="/README.md"><strong>English</strong></a> / <a href="/README.zh.md"><strong>简体中文</strong></a>
</p>

<p align="center">
  Edit PDFs with natural language — powered by <strong>Qwen (Tongyi Qianwen)</strong>.<br>
  Inspired by <a href="https://github.com/gavrielc/Nano-PDF">nano-pdf</a>.
</p>

---

## Features

- ✅ **Natural Language Editing** — describe what you want, AI does the rest
- ✅ **Dual Mode** — Qwen AI for complex edits, local keyword matching for quick fixes
- ✅ **Zero System Dependencies** — no tesseract, no poppler; pure Python
- ✅ **Precise Text Operations** — PyMuPDF-powered block-level positioning
- ✅ **Optional AI** — works fully offline in local mode; add Qwen API key for AI mode
- ✅ **Format Preserving** — edits text while keeping the original PDF layout intact

## vs nano-pdf

| | nano-pdf (original) | nano-pdf-qwen |
|---|---|---|
| AI Model | Gemini 3 Pro Image | Qwen (Tongyi Qianwen) |
| Approach | AI visual editing | Text block positioning + PyMuPDF |
| Local mode | ❌ | ✅ keyword matching, free & offline |
| System deps | tesseract + poppler | **None** |
| API Key | `GEMINI_API_KEY` | `DASHSCOPE_API_KEY` (optional) |

## Quick Start

```bash
# Install as Claude Code skill
git clone https://github.com/elwnyli/nano-pdf-qwen.git ~/.claude/skills/nano-pdf-qwen
pip install PyMuPDF dashscope

# Local mode (free, no API key)
python ~/.claude/skills/nano-pdf-qwen/qwen_pdf_edit.py document.pdf 1 "remove watermark"

# Qwen AI mode
export DASHSCOPE_API_KEY="your-key"
python ~/.claude/skills/nano-pdf-qwen/qwen_pdf_edit.py document.pdf 1 "change subtitle to 2026 Annual Report"
```

## Get Qwen API Key

Visit [Alibaba Bailian](https://bailian.console.aliyun.com) → create API Key → `export DASHSCOPE_API_KEY="sk-xxx"`

## How It Works

1. PyMuPDF extracts all text blocks with precise coordinates
2. Qwen AI (or local keyword matching) identifies target text
3. PyMuPDF applies edits — redact, replace, or insert
4. Outputs `*_edited.pdf` with changes applied

## Credits

Inspired by [nano-pdf](https://github.com/gavrielc/Nano-PDF) by [@gavrielc](https://github.com/gavrielc).

## License

MIT
