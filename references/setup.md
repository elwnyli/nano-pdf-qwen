# Qwen PDF Editor - 安装与配置

## 安装

```bash
# 1. 复制技能到 Claude Code 技能目录
cp -r qwen-pdf ~/.claude/skills/

# 2. 安装 Python 依赖
pip install PyMuPDF dashscope
```

## 千问 AI 模式配置

```bash
# 获取 Key: https://bailian.console.aliyun.com
export DASHSCOPE_API_KEY="你的key"
```

不设置 key 也能用，自动降级为本地关键词匹配。

## 验证

```bash
python qwen_pdf_edit.py
# 应输出帮助信息
```
