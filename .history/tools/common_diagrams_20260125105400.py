"""
常用图表生成器集合

提供一些开箱即用的常见图表类型
"""

from diagram_generator import DiagramGenerator, Color
from typing import List, Dict, Tuple
import math


class TimelineDiagramGenerator(DiagramGenerator):
    """时间线图表生成器"""
    
    def create_timeline(
        self,
        events: List[Dict],
        output_path: str,
        title: str = "时间线",
        orientation: str = "horizontal"
    ):
        """
        创建时间线图表
        
        Args:
            events: 事件列表，每个事件: {
                'date': '日期',
                'title': '标题',
                'description': '描述（可选）',
                'color': '颜色（可选）'
            }
            output_path: 输出路径
            title: 标题
            orientation: 方向 ('horizontal' 或 'vertical')
        """
        if orientation == "horizontal":
            self.width = 1600
            self.height = 800
        else:
            self.width = 1000
            self.height = max(1200, len(events) * 200 + 200)
        
        self.create_canvas()
        
        # 标题
        self.draw_text_multiline(title, (self.width//2, 40), 36, Color.BLACK, 'center')
        
        if orientation == "horizontal":
            self._draw_horizontal_timeline(events)
        else:
            self._draw_vertical_timeline(events)
        
        self.save(output_path)
    
    def _draw_horizontal_timeline(self, events: List[Dict]):
        """绘制横向时间线"""
        line_y = 400
        margin = 150
        spacing = (self.width - 2 * margin) / (len(events) - 1) if len(events) > 1 else 0
        
        # 绘制主线
        self.draw.line(
            [(margin, line_y), (self.width - margin, line_y)],
            fill=Color.BLACK,
            width=4
        )
        
        # 绘制事件点
        for i, event in enumerate(events):
            x = margin + i * spacing if len(events) > 1 else self.width // 2
            color = event.get('color', Color.INFO)
            
            # 事件点
            self.draw_circle((x, line_y), 15, color, Color.BLACK, 3)
            
            # 日期（线下方）
            self.draw_text_multiline(
                event['date'],
                (x, line_y + 40),
                16,
                Color.BLACK,
                'center'
            )
            
            # 标题和描述（线上方）
            y_offset = 100 if i % 2 == 0 else 200
            self.draw_text_box(
                f"{event['title']}\n{event.get('description', '')}",
                (x - 120, line_y - y_offset - 60, x + 120, line_y - y_offset),
                font_size=14,
                bg_color=color,
                border_color=Color.BLACK
            )
            
            # 连接线
            self.draw.line(
                [(x, line_y - 15), (x, line_y - y_offset)],
                fill=Color.GRAY,
                width=2
            )
    
    def _draw_vertical_timeline(self, events: List[Dict]):
        """绘制纵向时间线"""
        line_x = 200
        start_y = 120
        spacing = 180
        
        # 绘制主线
        end_y = start_y + (len(events) - 1) * spacing
        self.draw.line(
            [(line_x, start_y), (line_x, end_y)],
            fill=Color.BLACK,
            width=4
        )
        
        # 绘制事件点
        for i, event in enumerate(events):
            y = start_y + i * spacing
            color = event.get('color', Color.INFO)
            
            # 事件点
            self.draw_circle((line_x, y), 15, color, Color.BLACK, 3)
            
            # 日期（左侧）
            self.draw_text_multiline(
                event['date'],
                (line_x - 80, y - 10),
                16,
                Color.BLACK,
                'right'
            )
            
            # 标题和描述（右侧）
            self.draw_text_box(
                f"{event['title']}\n{event.get('description', '')}",
                (line_x + 40, y - 50, line_x + 700, y + 50),
                font_size=16,
                bg_color=color,
                border_color=Color.BLACK
            )


class MindMapDiagramGenerator(DiagramGenerator):
    """思维导图生成器"""
    
    def create_mindmap(
        self,
        root: str,
        branches: Dict[str, List[str]],
        output_path: str,
        title: str = ""
    ):
        """
        创建简单的思维导图
        
        Args:
            root: 中心节点文本
            branches: 分支字典，{分支名: [子节点列表]}
            output_path: 输出路径
            title: 标题（可选）
        """
        self.width = 1600
        self.height = 1200
        self.create_canvas()
        
        # 标题
        if title:
            self.draw_text_multiline(title, (self.width//2, 30), 32, Color.BLACK, 'center')
        
        # 中心节点
        center_x, center_y = self.width // 2, self.height // 2
        self.draw_text_box(
            root,
            (center_x - 120, center_y - 60, center_x + 120, center_y + 60),
            font_size=24,
            bg_color='#FFE5B4',
            border_color=Color.BLACK,
            border_width=4
        )
        
        # 分支
        branch_list = list(branches.items())
        num_branches = len(branch_list)
        
        colors = [Color.INFO, Color.SUCCESS, Color.WARNING, '#E8F5E9', '#FFF3E0', '#F3E5F5']
        
        for i, (branch_name, sub_nodes) in enumerate(branch_list):
            angle = 2 * math.pi * i / num_branches
            
            # 主分支位置
            branch_distance = 350
            branch_x = center_x + int(branch_distance * math.cos(angle))
            branch_y = center_y + int(branch_distance * math.sin(angle))
            
            color = colors[i % len(colors)]
            
            # 绘制主分支
            self.draw_text_box(
                branch_name,
                (branch_x - 100, branch_y - 40, branch_x + 100, branch_y + 40),
                font_size=18,
                bg_color=color,
                border_color=Color.BLACK,
                border_width=3
            )
            
            # 连接到中心
            self.draw_curved_arrow(
                (center_x, center_y),
                (branch_x, branch_y),
                control_offset=(
                    int(50 * math.cos(angle)),
                    int(50 * math.sin(angle))
                ),
                color=Color.GRAY,
                width=3
            )
            
            # 绘制子节点
            for j, sub_node in enumerate(sub_nodes):
                sub_angle = angle + (j - len(sub_nodes)/2) * 0.3
                sub_distance = 180
                sub_x = branch_x + int(sub_distance * math.cos(sub_angle))
                sub_y = branch_y + int(sub_distance * math.sin(sub_angle))
                
                self.draw_text_box(
                    sub_node,
                    (sub_x - 70, sub_y - 25, sub_x + 70, sub_y + 25),
                    font_size=14,
                    bg_color=Color.WHITE,
                    border_color=Color.GRAY,
                    border_width=2
                )
                
                # 连接到主分支
                self.draw.line(
                    [(branch_x, branch_y), (sub_x, sub_y)],
                    fill=Color.GRAY,
                    width=2
                )
        
        self.save(output_path)


class MatrixDiagramGenerator(DiagramGenerator):
    """矩阵图生成器（如四象限图）"""
    
    def create_quadrant_matrix(
        self,
        x_label: str,
        y_label: str,
        quadrants: Dict[str, Dict],
        output_path: str,
        title: str = "四象限矩阵"
    ):
        """
        创建四象限矩阵图
        
        Args:
            x_label: X轴标签
            y_label: Y轴标签
            quadrants: 四个象限的数据，如:
                {
                    'top_right': {'title': '标题', 'items': ['项1', '项2'], 'color': '颜色'},
                    'top_left': {...},
                    'bottom_right': {...},
                    'bottom_left': {...}
                }
            output_path: 输出路径
            title: 标题
        """
        self.width = 1400
        self.height = 1400
        self.create_canvas()
        
        # 标题
        self.draw_text_multiline(title, (self.width//2, 40), 36, Color.BLACK, 'center')
        
        # 坐标轴
        center_x, center_y = self.width // 2, self.height // 2 + 50
        axis_length = 500
        
        # X轴
        self.draw_arrow(
            (center_x - axis_length, center_y),
            (center_x + axis_length, center_y),
            Color.BLACK,
            width=3
        )
        self.draw.text(
            (center_x + axis_length + 10, center_y - 20),
            x_label,
            font=self.get_font(20),
            fill=Color.BLACK
        )
        
        # Y轴
        self.draw_arrow(
            (center_x, center_y + axis_length),
            (center_x, center_y - axis_length),
            Color.BLACK,
            width=3
        )
        self.draw.text(
            (center_x + 10, center_y - axis_length - 30),
            y_label,
            font=self.get_font(20),
            fill=Color.BLACK
        )
        
        # 四个象限
        quadrant_positions = {
            'top_right': (center_x + 50, center_y - axis_length + 50, 
                         center_x + axis_length - 50, center_y - 50),
            'top_left': (center_x - axis_length + 50, center_y - axis_length + 50,
                        center_x - 50, center_y - 50),
            'bottom_right': (center_x + 50, center_y + 50,
                           center_x + axis_length - 50, center_y + axis_length - 50),
            'bottom_left': (center_x - axis_length + 50, center_y + 50,
                          center_x - 50, center_y + axis_length - 50)
        }
        
        for position, coords in quadrant_positions.items():
            if position in quadrants:
                data = quadrants[position]
                color = data.get('color', Color.INFO)
                
                # 绘制象限背景
                self.draw_rounded_rectangle(
                    coords,
                    radius=15,
                    fill=color,
                    outline=Color.GRAY,
                    width=2
                )
                
                # 象限标题
                center_box_x = (coords[0] + coords[2]) // 2
                self.draw_text_multiline(
                    data['title'],
                    (center_box_x, coords[1] + 30),
                    24,
                    Color.BLACK,
                    'center'
                )
                
                # 象限内容
                items = data.get('items', [])
                for i, item in enumerate(items):
                    self.draw_text_multiline(
                        f"• {item}",
                        (coords[0] + 30, coords[1] + 80 + i * 40),
                        16,
                        Color.BLACK,
                        'left'
                    )
        
        self.save(output_path)


# 便捷函数
def create_timeline(events: List[Dict], output_path: str, title: str = "时间线", orientation: str = "horizontal"):
    """快速创建时间线"""
    generator = TimelineDiagramGenerator()
    generator.create_timeline(events, output_path, title, orientation)


def create_mindmap(root: str, branches: Dict[str, List[str]], output_path: str, title: str = ""):
    """快速创建思维导图"""
    generator = MindMapDiagramGenerator()
    generator.create_mindmap(root, branches, output_path, title)


def create_quadrant_matrix(x_label: str, y_label: str, quadrants: Dict, output_path: str, title: str = "四象限矩阵"):
    """快速创建四象限矩阵"""
    generator = MatrixDiagramGenerator()
    generator.create_quadrant_matrix(x_label, y_label, quadrants, output_path, title)


if __name__ == "__main__":
    """示例用法"""
    import os
    
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'source/_posts')
    
    # 示例1: 时间线
    print("生成时间线示例...")
    events = [
        {'date': '2020-01', 'title': '项目启动', 'description': '确定目标', 'color': Color.INFO},
        {'date': '2020-06', 'title': '第一版发布', 'description': '基础功能', 'color': Color.SUCCESS},
        {'date': '2021-01', 'title': '重大更新', 'description': '新特性', 'color': Color.WARNING},
        {'date': '2021-12', 'title': '稳定版本', 'description': '性能优化', 'color': Color.SUCCESS},
    ]
    create_timeline(events, os.path.join(output_dir, 'example_timeline.png'), '产品发展时间线')
    
    # 示例2: 思维导图
    print("生成思维导图示例...")
    branches = {
        '技术栈': ['Python', 'JavaScript', 'Go'],
        '工具': ['Git', 'Docker', 'VS Code'],
        '方法论': ['敏捷开发', 'TDD', 'CI/CD'],
        '能力': ['前端', '后端', 'DevOps'],
    }
    create_mindmap('全栈开发', branches, os.path.join(output_dir, 'example_mindmap.png'), '全栈开发技能树')
    
    # 示例3: 四象限矩阵
    print("生成四象限矩阵示例...")
    quadrants = {
        'top_right': {
            'title': '重要且紧急',
            'items': ['紧急bug修复', '线上事故处理'],
            'color': '#FFE4E4'
        },
        'top_left': {
            'title': '重要不紧急',
            'items': ['技术规划', '能力提升', '代码重构'],
            'color': '#E4FFE4'
        },
        'bottom_right': {
            'title': '不重要但紧急',
            'items': ['临时需求', '会议'],
            'color': '#FFF8E4'
        },
        'bottom_left': {
            'title': '不重要不紧急',
            'items': ['琐事', '无效社交'],
            'color': '#F0F0F0'
        }
    }
    create_quadrant_matrix(
        '紧急程度 →',
        '↑ 重要程度',
        quadrants,
        os.path.join(output_dir, 'example_matrix.png'),
        '时间管理矩阵'
    )
    
    print("\n✅ 所有示例生成完成！")
