# 快速参考指南

## 命令速查

```bash
# 查看帮助
python3 generate.py help

# 列出所有生成器
python3 generate.py list

# 生成 Vibe Programming 图表
python3 generate.py vibe

# 运行模板示例
python3 generate.py template
```

## 代码速查

### 流程图

```python
from diagram_generator import create_simple_flow_diagram, Color

steps = [
    {'text': '步骤1', 'color': Color.INFO},
    {'text': '步骤2', 'color': Color.HUMAN, 'note': '可选注释'},
    {'text': '步骤3', 'color': Color.SUCCESS},
]
create_simple_flow_diagram(steps, 'flow.png', '流程图标题')
```

### 对比图

```python
from diagram_generator import create_comparison_diagram, Color

left = {
    'title': '方案A',
    'items': [('步骤1', 150, Color.ERROR), ('步骤2', 280, Color.WARNING)],
    'features': ['❌ 缺点1', '❌ 缺点2']
}
right = {
    'title': '方案B',
    'items': [('步骤1', 150, Color.SUCCESS)],
    'features': ['✅ 优点1', '✅ 优点2']
}
create_comparison_diagram(left, right, 'comparison.png', '对比说明')
```

### 时间线

```python
from common_diagrams import create_timeline, Color

events = [
    {'date': '2020-01', 'title': '标题', 'description': '描述', 'color': Color.INFO},
    {'date': '2020-06', 'title': '标题2', 'color': Color.SUCCESS},
]
create_timeline(events, 'timeline.png', '时间线标题', orientation='horizontal')
# orientation: 'horizontal' 或 'vertical'
```

### 思维导图

```python
from common_diagrams import create_mindmap

branches = {
    '分支1': ['子节点1', '子节点2'],
    '分支2': ['子节点3', '子节点4'],
    '分支3': ['子节点5'],
}
create_mindmap('中心节点', branches, 'mindmap.png', '思维导图标题')
```

### 四象限矩阵

```python
from common_diagrams import create_quadrant_matrix

quadrants = {
    'top_right': {'title': '象限1', 'items': ['项1', '项2'], 'color': '#FFE4E4'},
    'top_left': {'title': '象限2', 'items': ['项3'], 'color': '#E4FFE4'},
    'bottom_right': {'title': '象限3', 'items': ['项4'], 'color': '#FFF8E4'},
    'bottom_left': {'title': '象限4', 'items': ['项5'], 'color': '#F0F0F0'}
}
create_quadrant_matrix('X轴标签 →', '↑ Y轴标签', quadrants, 'matrix.png', '矩阵标题')
```

## 常用颜色

```python
from diagram_generator import Color

# 基础色
Color.WHITE, Color.BLACK, Color.GRAY

# 状态色
Color.SUCCESS   # 绿色 - 成功
Color.WARNING   # 黄色 - 警告
Color.ERROR     # 红色 - 错误
Color.INFO      # 蓝色 - 信息

# 功能色
Color.HUMAN     # 浅橙 - 人的活动
Color.AI        # 浅蓝 - AI的活动
Color.CODE      # 浅绿 - 代码状态
Color.DECISION  # 浅红 - 决策点

# 边框色
Color.RED, Color.ORANGE, Color.GREEN, Color.BLUE
Color.DARK_GREEN, Color.DARK_RED

# 自定义颜色（十六进制）
'#RRGGBB'  # 例如: '#FFE5B4'
```

## 自定义图表模板

```python
from diagram_generator import DiagramGenerator, Color

class MyDiagram(DiagramGenerator):
    def create(self, output_path):
        self.width = 1400
        self.height = 1000
        self.create_canvas()
        
        # 标题
        self.draw_text_multiline('标题', (self.width//2, 50), 36, align='center')
        
        # 文本框
        self.draw_text_box('内容', (100, 150, 500, 250), 
                          font_size=18, bg_color=Color.INFO)
        
        # 箭头
        self.draw_arrow((300, 250), (300, 350), Color.BLACK, width=3)
        
        # 圆形
        self.draw_circle((700, 200), 50, Color.SUCCESS, Color.BLACK)
        
        # 图例
        self.draw_legend([('标签1', Color.RED), ('标签2', Color.BLUE)], (100, 500))
        
        self.save(output_path)

# 使用
generator = MyDiagram()
generator.create('my_diagram.png')
```

## 常用方法速查

| 方法 | 用途 | 示例 |
|------|------|------|
| `draw_text_box()` | 带背景的文本框 | `draw_text_box('文本', (x1,y1,x2,y2))` |
| `draw_arrow()` | 箭头 | `draw_arrow((x1,y1), (x2,y2))` |
| `draw_circle()` | 圆形 | `draw_circle((x,y), radius)` |
| `draw_rounded_rectangle()` | 圆角矩形 | `draw_rounded_rectangle((x1,y1,x2,y2))` |
| `draw_text_multiline()` | 多行文本 | `draw_text_multiline('文本', (x,y))` |
| `draw_legend()` | 图例 | `draw_legend([('标签', 颜色)], (x,y))` |
| `draw_curved_arrow()` | 曲线箭头 | `draw_curved_arrow((x1,y1), (x2,y2))` |

## 技巧

### 1. 快速原型
```python
# 使用较小的 dpi 快速预览
self.save('preview.png', dpi=72)
```

### 2. 高分辨率输出
```python
# 用于印刷或展示
self.save('final.png', dpi=300)
```

### 3. 调整画布大小
```python
generator = DiagramGenerator(width=1600, height=1200)
```

### 4. 批量生成
```python
for i, data in enumerate(dataset):
    generator = MyDiagram()
    generator.create(f'diagram_{i}.png')
```

### 5. 文本换行
```python
text = '第一行\n第二行\n第三行'
self.draw_text_multiline(text, (x, y))
```

## 文件结构

```
tools/
├── __init__.py                              # 包初始化
├── diagram_generator.py                     # 核心库 ⭐
├── common_diagrams.py                       # 常用图表
├── generate.py                              # 命令行工具
├── generate_vibe_programming_diagrams.py    # Vibe 图表
├── template_new_diagram.py                  # 模板示例
├── README.md                                # 完整文档
└── QUICK_REFERENCE.md                       # 本文档
```

## 创建新项目

1. 复制模板:
```bash
cp template_new_diagram.py my_article_diagrams.py
```

2. 修改内容:
```python
# 在 my_article_diagrams.py 中
def my_diagram_1():
    # 你的代码...
    pass

def main():
    my_diagram_1()
    # ... 更多图表

if __name__ == "__main__":
    main()
```

3. 运行:
```bash
python3 my_article_diagrams.py
```

## 常见问题

**Q: 中文显示为方块?**  
A: 工具会自动加载系统中文字体，如果还有问题，检查字体路径。

**Q: 图表太大/太小?**  
A: 调整 `width` 和 `height` 参数，或元素坐标。

**Q: 需要更复杂的图形?**  
A: 使用 Pillow/PIL 的所有方法，`self.draw` 是 `ImageDraw` 对象。

**Q: 如何调试布局?**  
A: 先用低 dpi 快速预览，调整好后再用高 dpi 生成。

## 获取帮助

- 查看 `README.md` 获取详细文档
- 查看 `template_new_diagram.py` 获取完整示例
- 查看各个生成器的源代码了解实现细节
