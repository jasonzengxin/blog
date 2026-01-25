# 新手入门指南

欢迎使用图表生成工具！这个指南会带你快速上手。

## 🚀 5分钟快速入门

### 步骤1: 验证环境

```bash
cd tools
python3 test_all.py
```

如果看到 "🎉 所有测试通过！"，说明环境已就绪。

### 步骤2: 生成第一个图表

```bash
python3 generate.py vibe
```

这会在 `source/_posts/` 目录下生成两张 Vibe Programming 相关的图表。

### 步骤3: 查看结果

打开 `source/_posts/` 目录，你会看到：
- `vibe-programming-flow.png` - 流程图
- `vibe-programming-comparison.png` - 对比图

### 步骤4: 尝试创建自己的图表

创建一个新文件 `my_first_diagram.py`:

```python
from diagram_generator import create_simple_flow_diagram, Color

steps = [
    {'text': '需求分析', 'color': Color.HUMAN},
    {'text': 'AI生成代码', 'color': Color.AI},
    {'text': '测试验证', 'color': Color.CODE},
    {'text': '部署上线', 'color': Color.SUCCESS},
]

create_simple_flow_diagram(steps, '../source/_posts/my_flow.png', '我的第一个流程图')
print("✅ 完成！")
```

运行它：

```bash
python3 my_first_diagram.py
```

## 📚 接下来学什么？

### 初学者路径

1. **查看示例** (10分钟)
   ```bash
   python3 template_new_diagram.py
   ```
   这会生成4个不同类型的图表示例。

2. **阅读快速参考** (15分钟)
   打开 `QUICK_REFERENCE.md`，浏览常用的代码片段。

3. **修改模板** (30分钟)
   - 复制 `template_new_diagram.py` 为 `my_diagrams.py`
   - 修改其中的示例，尝试不同的颜色和文字
   - 运行并查看效果

### 进阶用户路径

1. **学习核心 API** (1小时)
   阅读 `README.md` 中的 "高级用法" 部分。

2. **创建自定义生成器** (2小时)
   参考 `generate_vibe_programming_diagrams.py`，创建你自己的图表生成器。

3. **探索常用图表** (1小时)
   研究 `common_diagrams.py` 中的：
   - 时间线生成器
   - 思维导图生成器
   - 矩阵图生成器

## 🎯 常见场景示例

### 场景1: 我要画一个技术栈的思维导图

```python
from common_diagrams import create_mindmap

tech_stack = {
    '前端': ['React', 'Vue', 'TypeScript'],
    '后端': ['Python', 'Go', 'Node.js'],
    '数据库': ['PostgreSQL', 'Redis', 'MongoDB'],
    '工具': ['Git', 'Docker', 'K8s'],
}

create_mindmap('全栈技术', tech_stack, 'tech_stack.png', '我的技术栈')
```

### 场景2: 我要画一个项目时间线

```python
from common_diagrams import create_timeline, Color

milestones = [
    {
        'date': '2024-01',
        'title': '项目启动',
        'description': '确定目标和范围',
        'color': Color.INFO
    },
    {
        'date': '2024-03',
        'title': 'MVP完成',
        'description': '核心功能上线',
        'color': Color.SUCCESS
    },
    {
        'date': '2024-06',
        'title': '正式发布',
        'description': '1.0版本发布',
        'color': Color.SUCCESS
    },
]

create_timeline(milestones, 'project_timeline.png', '项目里程碑')
```

### 场景3: 我要对比两种方案

```python
from diagram_generator import create_comparison_diagram, Color

solution_a = {
    'title': '自建系统',
    'items': [
        ('开发周期：6个月', 150, Color.ERROR),
        ('维护成本：高', 280, Color.ERROR),
        ('灵活性：高', 410, Color.SUCCESS),
    ],
    'features': [
        '❌ 开发时间长',
        '❌ 维护成本高',
        '✅ 完全可控',
    ]
}

solution_b = {
    'title': '使用SaaS',
    'items': [
        ('开发周期：1周', 150, Color.SUCCESS),
        ('维护成本：低', 280, Color.SUCCESS),
        ('灵活性：中', 410, Color.WARNING),
    ],
    'features': [
        '✅ 快速上线',
        '✅ 维护简单',
        '⚠️ 功能受限',
    ]
}

create_comparison_diagram(
    solution_a,
    solution_b,
    'solution_comparison.png',
    '技术方案对比'
)
```

## 💡 实用技巧

### 技巧1: 快速预览
在开发时使用低 dpi 快速查看效果：

```python
generator.save('preview.png', dpi=72)  # 快速预览
generator.save('final.png', dpi=300)   # 最终版本
```

### 技巧2: 批量生成
如果需要生成多个相似的图表：

```python
from diagram_generator import create_simple_flow_diagram, Color

processes = {
    'frontend': ['设计', '开发', '测试', '部署'],
    'backend': ['API设计', '开发', '测试', '部署'],
    'database': ['建模', '迁移', '优化', '备份'],
}

for name, steps in processes.items():
    step_list = [{'text': s, 'color': Color.INFO} for s in steps]
    create_simple_flow_diagram(
        step_list,
        f'{name}_flow.png',
        f'{name.upper()} 流程'
    )
```

### 技巧3: 使用一致的配色
定义自己的配色方案：

```python
from diagram_generator import Color

MY_COLORS = {
    'phase1': '#E3F2FD',
    'phase2': '#FFF3E0',
    'phase3': '#E8F5E9',
    'important': '#FFE4E4',
}

# 在图表中使用
step = {'text': '重要步骤', 'color': MY_COLORS['important']}
```

## ❓ 常见问题

### Q: 图表文字太小/太大？
A: 调整 `font_size` 参数：
```python
self.draw_text_box('文本', (x1,y1,x2,y2), font_size=24)  # 增大字体
```

### Q: 图表太挤？
A: 增加画布大小：
```python
generator = DiagramGenerator(width=1600, height=1400)  # 更大的画布
```

### Q: 中文显示为方块？
A: 工具会自动加载系统中文字体。如果还有问题，检查系统是否有中文字体。

### Q: 想要不同的布局？
A: 查看 `template_new_diagram.py` 中的 `example_4_architecture()`，了解如何自定义布局。

## 🎓 学习资源

### 必读
- `QUICK_REFERENCE.md` - 代码速查表
- `README.md` - 完整文档

### 示例代码
- `template_new_diagram.py` - 4个完整示例
- `generate_vibe_programming_diagrams.py` - 实际项目案例
- `common_diagrams.py` - 高级图表类型

### 命令行工具
```bash
python3 generate.py help     # 查看帮助
python3 generate.py list     # 列出所有生成器
```

## 🚦 下一步

选择你的路径：

**路径A: 快速使用者**
→ 使用 `template_new_diagram.py` 修改示例
→ 生成需要的图表
→ 在博客中使用

**路径B: 深入学习者**
→ 阅读完整的 `README.md`
→ 学习核心 API
→ 创建自定义生成器

**路径C: 贡献者**
→ 研究源码
→ 添加新功能
→ 完善文档

## 📞 获取帮助

遇到问题？

1. 查看 `QUICK_REFERENCE.md` 找常见代码
2. 阅读 `README.md` 了解详细 API
3. 运行 `python3 test_all.py` 检查环境
4. 查看示例代码学习用法

---

**开始创建你的第一个图表吧！** 🎨

记住：最好的学习方式就是动手实践。复制一个示例，修改它，运行它，看看会发生什么！
