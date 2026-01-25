#!/bin/bash
# 快速切换到预览模式

cd "$(dirname "$0")"
python3 tools/preview_mode.py preview "source/_posts/使用-Cursor-编程的感想.md"

echo ""
echo "📖 现在可以在任何 Markdown 预览器中查看图片了"
echo "   （VS Code、Typora、Cursor 等）"
echo ""
echo "⚠️  完成预览后，记得运行 ./deploy.sh 恢复部署模式"
