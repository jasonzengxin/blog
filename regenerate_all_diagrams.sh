#!/bin/bash
# 重新生成所有博客图表

cd "$(dirname "$0")"

echo "🎨 开始重新生成所有图表..."
echo ""

# 生成 Vibe Programming 图表
echo "1️⃣  生成 Vibe Programming 流程图和对比图..."
python3 tools/generate_vibe_programming_diagrams.py

echo ""

# 生成 Consolidation Train 图表
echo "2️⃣  生成 Consolidation Train 流程图..."
python3 tools/generate_consolidation_train_diagram.py

echo ""
echo "✅ 所有图表生成完成！"
echo ""
echo "📁 图表位置："
ls -lh source/_posts/使用-Cursor-编程的感想/*.png
