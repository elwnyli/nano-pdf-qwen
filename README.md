# nano-pdf-qwen

[English](#english) | [中文](#chinese)

---

## English

A PDF editor using natural language instructions — powered by **Qwen (Tongyi Qianwen)**.  
Inspired by [nano-pdf](https://github.com/gavrielc/Nano-PDF).

### vs nano-pdf

| | nano-pdf (original) | nano-pdf-qwen (this) |
|---|---|---|
| AI Model | Gemini 3 Pro Image | Qwen (Tongyi Qianwen) |
| Editing | AI visual editing | Text block positioning + PyMuPDF |
| Local mode | No | Yes (keyword matching, free & offline) |
| API Key | GEMINI_API_KEY | DASHSCOPE_API_KEY (optional) |
| System deps | tesseract + poppler | None |

### Install

```bash
pip install PyMuPDF dashscope

# As a Claude Code skill
cp -r nano-pdf-qwen ~/.claude/skills/
```

### Usage

```bash
# Local mode (free, no API key needed)
python qwen_pdf_edit.py document.pdf 1 "remove watermark"

# Qwen AI mode
export DASHSCOPE_API_KEY="your-key"
python qwen_pdf_edit.py document.pdf 1 "change subtitle to 2026 Annual Report"
```

### Get Qwen API Key

Visit [Alibaba Bailian](https://bailian.console.aliyun.com) to create an API key.

### Credits

Inspired by [nano-pdf](https://github.com/gavrielc/Nano-PDF) by [@gavrielc](https://github.com/gavrielc).

### License

MIT

---

## 中文

基于 [nano-pdf](https://github.com/gavrielc/Nano-PDF) 理念，使用**通义千问**的自然语言 PDF 编辑器。

### vs nano-pdf

| | nano-pdf（原版） | nano-pdf-qwen（本版） |
|---|---|---|
| AI 模型 | Gemini 3 Pro Image | 通义千问 (Qwen) |
| 编辑方式 | AI 视觉编辑 | 文本块定位 + PyMuPDF 精确操作 |
| 本地模式 | 不支持 | 支持（关键词匹配，免费离线） |
| API Key | GEMINI_API_KEY | DASHSCOPE_API_KEY（可选） |
| 系统依赖 | tesseract + poppler | 无 |

### 安装

```bash
pip install PyMuPDF dashscope

# 安装为 Claude Code 技能
cp -r nano-pdf-qwen ~/.claude/skills/
```

### 使用

```bash
# 本地模式（免费，无需 API Key）
python qwen_pdf_edit.py 文档.pdf 1 "删除 水印"

# 千问 AI 模式
export DASHSCOPE_API_KEY="你的key"
python qwen_pdf_edit.py 文档.pdf 1 "把副标题改成 2026 年度报告"
```

### 获取千问 API Key

访问 [阿里云百炼](https://bailian.console.aliyun.com) 创建 API Key。

### 致谢

本技能受 [nano-pdf](https://github.com/gavrielc/Nano-PDF)（作者 [@gavrielc](https://github.com/gavrielc)）启发。

### 许可证

MIT
