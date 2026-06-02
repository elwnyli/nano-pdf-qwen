---
name: qwen-pdf
description: 使用通义千问(Qwen) AI 编辑 PDF，支持自然语言指令增删改文字。双模式：本地关键词匹配（免费离线）或千问 AI 理解（需 DASHSCOPE_API_KEY）。基于 PyMuPDF 精确定位和修改。当用户需要编辑 PDF 内容、删除/修改/替换 PDF 文字时自动触发。
---

# Qwen PDF Editor

用自然语言指令编辑 PDF，支持千问 AI 理解 + PyMuPDF 精确操作。

## 快速开始

```bash
# 安装依赖
pip install PyMuPDF dashscope

# 本地模式（免费，无需 API Key）
python qwen_pdf_edit.py 文档.pdf 1 "删除 临时水印"

# 千问 AI 模式（需设置环境变量）
export DASHSCOPE_API_KEY="你的key"
python qwen_pdf_edit.py 文档.pdf 1 "把副标题改成 Q3 总结报告"
```

## 两种模式

| 模式 | 条件 | 能力 |
|------|------|------|
| 本地匹配 | 默认，无需配置 | 精确关键词定位，删除/替换文字 |
| 千问 AI | 设置 `DASHSCOPE_API_KEY` | 理解复杂自然语言指令，上下文分析 |

## 原理

1. PyMuPDF 提取页面所有文本块及其精确坐标
2. 千问 AI 分析指令，定位目标文本块（或本地关键词匹配）
3. PyMuPDF 精确执行删除/替换，保持排版不变
4. 输出 `原文件名_edited.pdf`

## 获取千问 API Key

1. 访问 [阿里云百炼](https://bailian.console.aliyun.com)
2. 开通模型服务，创建 API Key
3. `export DASHSCOPE_API_KEY="你的key"`
