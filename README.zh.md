<h1 align="center">nano-pdf-qwen</h1>

<p align="center">
  <a href="https://github.com/elwnyli/nano-pdf-qwen/stargazers"><img src="https://img.shields.io/badge/GitHub-Stars-blue?style=flat-square&logo=github" alt="GitHub stars"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white&style=flat-square" alt="Python"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License"></a>
</p>

<p align="center">
  <a href="/README.md"><strong>English</strong></a> / <a href="/README.zh.md"><strong>简体中文</strong></a>
</p>

<p align="center">
  用自然语言指令编辑 PDF — 基于<strong>通义千问 (Qwen)</strong>。<br>
  灵感来自 <a href="https://github.com/gavrielc/Nano-PDF">nano-pdf</a>。
</p>

---

## 功能亮点

- ✅ **自然语言编辑** — 说人话就能改 PDF，AI 自动理解指令
- ✅ **双模式** — 千问 AI 处理复杂指令，本地关键词匹配快速修改
- ✅ **零系统依赖** — 不需要 tesseract、poppler；纯 Python 即可运行
- ✅ **精确定位** — 基于 PyMuPDF 的文本块级别操作，不破坏排版
- ✅ **可选 AI** — 本地模式完全离线免费；设个千问 API Key 即启用 AI 模式
- ✅ **保留格式** — 修改文字内容，保持原 PDF 布局不变

## vs nano-pdf

| | nano-pdf（原版） | nano-pdf-qwen |
|---|---|---|
| AI 模型 | Gemini 3 Pro Image | 通义千问 (Qwen) |
| 编辑方式 | AI 视觉编辑 | 文本块定位 + PyMuPDF 精确操作 |
| 本地模式 | ❌ 不支持 | ✅ 关键词匹配，免费离线 |
| 系统依赖 | tesseract + poppler | **无** |
| API Key | `GEMINI_API_KEY` | `DASHSCOPE_API_KEY`（可选） |

## 快速开始

```bash
# 安装为 Claude Code 技能
git clone https://github.com/elwnyli/nano-pdf-qwen.git ~/.claude/skills/nano-pdf-qwen
pip install PyMuPDF dashscope

# 本地模式（免费，无需 API Key）
python ~/.claude/skills/nano-pdf-qwen/qwen_pdf_edit.py 文档.pdf 1 "删除 水印"

# 千问 AI 模式
export DASHSCOPE_API_KEY="你的key"
python ~/.claude/skills/nano-pdf-qwen/qwen_pdf_edit.py 文档.pdf 1 "把副标题改成 2026 年度报告"
```

## 获取千问 API Key

访问 [阿里云百炼](https://bailian.console.aliyun.com) → 创建 API Key → `export DASHSCOPE_API_KEY="sk-xxx"`

## 原理

1. PyMuPDF 提取页面所有文本块及精确坐标
2. 千问 AI（或本地关键词匹配）定位目标文本
3. PyMuPDF 执行删除/替换/插入操作
4. 输出 `*_edited.pdf`

## 致谢

灵感来源于 [nano-pdf](https://github.com/gavrielc/Nano-PDF)（作者 [@gavrielc](https://github.com/gavrielc)）。

## 许可证

MIT
