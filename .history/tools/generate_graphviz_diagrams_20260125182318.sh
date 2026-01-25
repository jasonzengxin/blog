#!/bin/bash
# 使用 Graphviz 生成所有流程图

cd "$(dirname "$0")"

OUTPUT_DIR="../source/_posts/使用-Cursor-编程的感想"
DPI=150

echo "🎨 使用 Graphviz 生成流程图..."
echo ""

# 1. Vibe Programming 流程图
echo "1️⃣  生成 Vibe Programming 流程图..."
dot -Tpng -Gdpi=$DPI graphviz_vibe_programming_flow.dot \
    -o "$OUTPUT_DIR/vibe-programming-flow-graphviz.png"
echo "   ✓ vibe-programming-flow-graphviz.png"

# 2. Vibe Programming 对比图
echo "2️⃣  生成 Vibe Programming 对比图..."
dot -Tpng -Gdpi=$DPI graphviz_vibe_programming_comparison.dot \
    -o "$OUTPUT_DIR/vibe-programming-comparison-graphviz.png"
echo "   ✓ vibe-programming-comparison-graphviz.png"

# 3. Consolidation Train 流程图
echo "3️⃣  生成 Consolidation Train 流程图..."
dot -Tpng -Gdpi=$DPI graphviz_consolidation_train.dot \
    -o "$OUTPUT_DIR/consolidation-train-flow-graphviz.png"
echo "   ✓ consolidation-train-flow-graphviz.png"

echo ""
echo "✅ 所有 Graphviz 图表生成完成！"
echo ""
echo "📊 文件大小："
ls -lh "$OUTPUT_DIR"/*graphviz.png | awk '{print "   " $9 ": " $5}'

echo ""
echo "💡 提示："
echo "   - 修改 .dot 文件后运行此脚本重新生成"
echo "   - DPI=$DPI 可调整图片分辨率"
echo "   - 生成 SVG: dot -Tsvg xxx.dot -o xxx.svg"
