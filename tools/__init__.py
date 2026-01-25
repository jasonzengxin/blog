"""
博客图表生成工具包

提供多种类型的图表生成功能，包括：
- 流程图
- 对比图
- 时间线
- 思维导图
- 矩阵图
等等

使用示例:
    from tools import create_simple_flow_diagram, Color
    
    steps = [
        {'text': '步骤1', 'color': Color.INFO},
        {'text': '步骤2', 'color': Color.SUCCESS},
    ]
    create_simple_flow_diagram(steps, 'output.png', '我的流程')
"""

from .diagram_generator import (
    DiagramGenerator,
    FlowDiagramGenerator,
    ComparisonDiagramGenerator,
    Color,
    create_simple_flow_diagram,
    create_comparison_diagram,
)

from .common_diagrams import (
    TimelineDiagramGenerator,
    MindMapDiagramGenerator,
    MatrixDiagramGenerator,
    create_timeline,
    create_mindmap,
    create_quadrant_matrix,
)

__version__ = '1.0.0'
__all__ = [
    # 基础类
    'DiagramGenerator',
    'FlowDiagramGenerator',
    'ComparisonDiagramGenerator',
    'TimelineDiagramGenerator',
    'MindMapDiagramGenerator',
    'MatrixDiagramGenerator',
    
    # 颜色
    'Color',
    
    # 便捷函数
    'create_simple_flow_diagram',
    'create_comparison_diagram',
    'create_timeline',
    'create_mindmap',
    'create_quadrant_matrix',
]
