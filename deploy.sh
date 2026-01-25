#!/bin/bash
# 恢复部署模式并部署

cd "$(dirname "$0")"

echo "正在恢复部署模式..."
python3 tools/preview_mode.py deploy "source/_posts/使用-Cursor-编程的感想.md"

echo ""
echo "正在重新生成和部署..."
hexo clean && hexo generate && hexo deploy

echo ""
echo "✅ 部署完成！"
