# 图表生成工具

这个目录包含用于生成博客文章中各类图表的 Python 工具。

## 文件说明

- **`diagram_generator.py`**: 通用图表生成器核心库
- **`common_diagrams.py`**: 常用图表类型（时间线、思维导图、矩阵图等）
- **`generate.py`**: 命令行工具入口
- **`generate_vibe_programming_diagrams.py`**: Vibe Programming 文章专用图表生成脚本
- **`template_new_diagram.py`**: 新图表项目模板（包含多个示例）
- **`README.md`**: 本文档

## 依赖安装

```bash
# 确保已安装 Pillow
pip3 install Pillow
```

## 快速开始

### 方式1: 使用命令行工具（推荐）

```bash
cd tools

# 查看帮助
python3 generate.py help

# 列出所有可用的生成器
python3 generate.py list

# 生成 Vibe Programming 图表
python3 generate.py vibe

# 运行模板示例（生成4个示例图表）
python3 generate.py template
```

### 方式2: 直接运行脚本

```bash
cd tools

# 生成 Vibe Programming 图表
python3 generate_vibe_programming_diagrams.py

# 运行常用图表示例
python3 common_diagrams.py

# 运行模板示例
python3 template_new_diagram.py
```

生成的图表会保存在 `source/_posts/` 目录下。

### 2. 使用通用工具创建简单流程图

```python
from diagram_generator import create_simple_flow_diagram, Color

steps = [
    {'text': '步骤1: 开始', 'color': Color.INFO},
    {'text': '步骤2: 处理', 'color': Color.HUMAN},
    {'text': '步骤3: 完成', 'color': Color.SUCCESS},
]

create_simple_flow_diagram(steps, 'output/my_flow.png', '我的流程图')
```

### 3. 创建对比图

```python
from diagram_generator import create_comparison_diagram, Color

left = {
    'title': '传统方式',
    'items': [
        ('步骤1', 150, Color.ERROR),
        ('步骤2', 280, Color.WARNING),
    ],
    'features': ['❌ 慢', '❌ 复杂']
}

right = {
    'title': '新方式',
    'items': [
        ('快速', 150, Color.SUCCESS),
    ],
    'features': ['✅ 快', '✅ 简单']
}

create_comparison_diagram(left, right, 'output/comparison.png', '方式对比')
```

### 4. 创建时间线图

```python
from common_diagrams import create_timeline, Color

events = [
    {'date': '2020-01', 'title': '项目启动', 'description': '确定目标', 'color': Color.INFO},
    {'date': '2020-06', 'title': '第一版发布', 'description': '基础功能', 'color': Color.SUCCESS},
    {'date': '2021-01', 'title': '重大更新', 'description': '新特性', 'color': Color.WARNING},
]

create_timeline(events, 'timeline.png', '产品发展时间线', orientation='horizontal')
```

### 5. 创建思维导图

```python
from common_diagrams import create_mindmap

branches = {
    '技术栈': ['Python', 'JavaScript', 'Go'],
    '工具': ['Git', 'Docker', 'VS Code'],
    '方法论': ['敏捷开发', 'TDD', 'CI/CD'],
}

create_mindmap('全栈开发', branches, 'mindmap.png', '全栈开发技能树')
```

### 6. 创建四象限矩阵

```python
from common_diagrams import create_quadrant_matrix

quadrants = {
    'top_right': {
        'title': '重要且紧急',
        'items': ['紧急bug修复', '线上事故处理'],
        'color': '#FFE4E4'
    },
    'top_left': {
        'title': '重要不紧急',
        'items': ['技术规划', '能力提升'],
        'color': '#E4FFE4'
    },
    'bottom_right': {
        'title': '不重要但紧急',
        'items': ['临时需求', '会议'],
        'color': '#FFF8E4'
    },
    'bottom_left': {
        'title': '不重要不紧急',
        'items': ['琐事'],
        'color': '#F0F0F0'
    }
}

create_quadrant_matrix('紧急程度 →', '↑ 重要程度', quadrants, 'matrix.png', '时间管理矩阵')
```

## 高级用法

### 自定义图表生成器

继承 `DiagramGenerator` 类来创建自定义图表：

```python
from diagram_generator import DiagramGenerator, Color

class MyDiagramGenerator(DiagramGenerator):
    def create_my_diagram(self, output_path):
        # 创建画布
        self.create_canvas()
        
        # 绘制标题
        self.draw_text_multiline(
            '我的图表', 
            (self.width//2, 50), 
            font_size=36
        )
        
        # 绘制文本框
        self.draw_text_box(
            '这是一个文本框',
            (100, 150, 500, 250),
            bg_color=Color.INFO
        )
        
        # 绘制箭头
        self.draw_arrow((300, 250), (300, 350))
        
        # 保存
        self.save(output_path)

# 使用
generator = MyDiagramGenerator(width=800, height=600)
generator.create_my_diagram('my_diagram.png')
```

### 可用的绘图方法

#### 基础图形

```python
# 圆角矩形
self.draw_rounded_rectangle(
    xy=(x1, y1, x2, y2),
    radius=20,
    fill=Color.WHITE,
    outline=Color.BLACK,
    width=2
)

# 圆形
self.draw_circle(
    center=(x, y),
    radius=50,
    fill=Color.WHITE,
    outline=Color.BLACK
)

# 箭头
self.draw_arrow(
    start=(x1, y1),
    end=(x2, y2),
    color=Color.BLACK,
    width=3
)

# 曲线箭头
self.draw_curved_arrow(
    start=(x1, y1),
    end=(x2, y2),
    control_offset=(50, 50),
    color=Color.BLACK
)
```

#### 文本

```python
# 多行文本
self.draw_text_multiline(
    text='第一行\n第二行',
    position=(x, y),
    font_size=18,
    fill=Color.BLACK,
    align='center'  # 'left', 'center', 'right'
)

# 带背景的文本框
self.draw_text_box(
    text='文本内容',
    xy=(x1, y1, x2, y2),
    font_size=18,
    text_color=Color.BLACK,
    bg_color=Color.WHITE,
    border_color=Color.BLACK
)
```

#### 图例

```python
# 绘制图例
self.draw_legend(
    items=[
        ('标签1', Color.RED),
        ('标签2', Color.BLUE),
    ],
    position=(100, 900)
)
```

### 预定义颜色

`Color` 类提供了常用的颜色：

```python
# 基础色
Color.WHITE, Color.BLACK, Color.GRAY, Color.LIGHT_GRAY

# 状态色
Color.SUCCESS  # 成功 - 绿色
Color.WARNING  # 警告 - 黄色
Color.ERROR    # 错误 - 红色
Color.INFO     # 信息 - 蓝色

# 功能色
Color.HUMAN    # 人的活动 - 浅橙
Color.AI       # AI的活动 - 浅蓝
Color.CODE     # 代码状态 - 浅绿
Color.DECISION # 决策点 - 浅红

# 边框色
Color.RED, Color.ORANGE, Color.GREEN, Color.BLUE
Color.DARK_GREEN, Color.DARK_RED
```

## 示例项目结构

```
blog/
├── tools/
│   ├── diagram_generator.py          # 核心库
│   ├── generate_vibe_programming_diagrams.py  # 示例脚本
│   └── README.md                      # 本文档
├── source/
│   └── _posts/
│       ├── 使用-Cursor-编程的感想.md
│       ├── vibe-programming-flow.png
│       └── vibe-programming-comparison.png
└── ...
```

## 创建新的图表脚本

参考 `generate_vibe_programming_diagrams.py` 的模式：

1. 从 `diagram_generator.py` 导入需要的类
2. 继承 `DiagramGenerator` 或使用便捷函数
3. 创建你的自定义生成方法
4. 在 `main()` 函数中调用

示例模板：

```python
from diagram_generator import DiagramGenerator, Color
import os

class MyArticleDiagramGenerator(DiagramGenerator):
    def create_diagram_1(self, output_path):
        self.create_canvas()
        # ... 你的绘图代码 ...
        self.save(output_path)
    
    def create_diagram_2(self, output_path):
        self.create_canvas()
        # ... 你的绘图代码 ...
        self.save(output_path)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    blog_dir = os.path.dirname(script_dir)
    output_dir = os.path.join(blog_dir, 'source/_posts')
    
    generator = MyArticleDiagramGenerator()
    generator.create_diagram_1(os.path.join(output_dir, 'diagram1.png'))
    generator.create_diagram_2(os.path.join(output_dir, 'diagram2.png'))
    
    print("✅ 图表生成完成！")

if __name__ == "__main__":
    main()
```

## 技巧和最佳实践

### 1. 字体问题

工具会自动尝试加载 macOS 的中文字体（PingFang、STHeiti 等）。如果字体显示有问题，可以手动指定字体路径：

```python
self.fonts[size] = ImageFont.truetype("/path/to/your/font.ttf", size)
```

### 2. 调整画布大小

根据内容复杂度调整画布大小：

```python
generator = DiagramGenerator(width=1600, height=1400)
```

### 3. 保存高分辨率图片

```python
self.save(output_path, dpi=300)  # 默认是 300 dpi
```

### 4. 调试布局

在开发时，可以先用较小的 dpi 快速预览：

```python
self.save('debug.png', dpi=72)  # 快速生成
```

### 5. 颜色选择

- 使用预定义的 `Color` 类颜色，保持一致性
- 或使用十六进制颜色代码：`'#RRGGBB'`

### 6. 文本换行

使用 `\n` 在文本中换行：

```python
text = '第一行\n第二行\n第三行'
```

## 常见问题

### Q: 中文显示为方块？
A: 确保系统中有中文字体，工具会自动尝试加载。如果还有问题，手动指定字体路径。

### Q: 图片太大/太小？
A: 调整 `width` 和 `height` 参数，或调整元素的坐标和大小。

### Q: 想要更复杂的图形？
A: 参考 Pillow/PIL 的官方文档，`self.draw` 是 `ImageDraw` 对象，支持所有 PIL 的绘图方法。

### Q: 如何批量生成多个图表？
A: 在 `main()` 函数中创建循环，或创建多个生成方法。

## 贡献

如果你创建了有用的通用绘图方法，可以添加到 `DiagramGenerator` 类中，方便复用。

## 许可

这些工具是博客项目的一部分，供个人使用。
