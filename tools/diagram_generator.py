"""
通用图表生成工具
用于生成博客文章中的各类图表，包括流程图、对比图、架构图等

依赖: Pillow (PIL)
使用示例: 
    from diagram_generator import DiagramGenerator
    
    dg = DiagramGenerator()
    dg.create_flow_diagram(steps, output_path)
"""

from PIL import Image, ImageDraw, ImageFont
import math
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass


@dataclass
class Color:
    """预定义的颜色方案"""
    # 基础色
    WHITE = '#FFFFFF'
    BLACK = '#000000'
    GRAY = '#808080'
    LIGHT_GRAY = '#D3D3D3'
    
    # 状态色
    SUCCESS = '#E4FFE4'
    WARNING = '#FFF8E4'
    ERROR = '#FFE4E4'
    INFO = '#E4F4FF'
    
    # 功能色
    HUMAN = '#FFE5B4'      # 人的活动 - 浅橙
    AI = '#B4D7FF'         # AI的活动 - 浅蓝
    CODE = '#D4E7D7'       # 代码状态 - 浅绿
    DECISION = '#FFD4D4'   # 决策点 - 浅红
    
    # 边框色
    RED = '#FF0000'
    ORANGE = '#FFA500'
    GREEN = '#008000'
    BLUE = '#0000FF'
    DARK_GREEN = '#006400'
    DARK_RED = '#8B0000'


class DiagramGenerator:
    """图表生成器基类"""
    
    def __init__(self, width: int = 1400, height: int = 1200, bg_color: str = Color.WHITE):
        """
        初始化图表生成器
        
        Args:
            width: 图片宽度
            height: 图片高度
            bg_color: 背景颜色
        """
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.img = None
        self.draw = None
        self._init_fonts()
    
    def _init_fonts(self):
        """初始化字体"""
        self.fonts = {}
        font_paths = [
            "/System/Library/Fonts/PingFang.ttc",
            "/System/Library/Fonts/STHeiti Medium.ttc",
            "/System/Library/Fonts/Hiragino Sans GB.ttc",
            "Arial Unicode.ttf",
        ]
        
        # 尝试加载字体
        for size in [12, 14, 16, 18, 20, 24, 28, 32, 36, 40]:
            for font_path in font_paths:
                try:
                    self.fonts[size] = ImageFont.truetype(font_path, size)
                    break
                except:
                    continue
            
            # 如果所有字体都失败，使用默认字体
            if size not in self.fonts:
                self.fonts[size] = ImageFont.load_default()
    
    def get_font(self, size: int) -> ImageFont:
        """获取指定大小的字体"""
        return self.fonts.get(size, self.fonts.get(18, ImageFont.load_default()))
    
    def create_canvas(self):
        """创建画布"""
        self.img = Image.new('RGB', (self.width, self.height), self.bg_color)
        self.draw = ImageDraw.Draw(self.img)
    
    def draw_rounded_rectangle(
        self, 
        xy: Tuple[int, int, int, int], 
        radius: int = 20, 
        fill: str = Color.WHITE, 
        outline: str = Color.BLACK, 
        width: int = 2
    ):
        """
        绘制圆角矩形
        
        Args:
            xy: (x1, y1, x2, y2) 矩形坐标
            radius: 圆角半径
            fill: 填充颜色
            outline: 边框颜色
            width: 边框宽度
        """
        x1, y1, x2, y2 = xy
        
        # 绘制四个圆角
        self.draw.ellipse([x1, y1, x1 + radius*2, y1 + radius*2], 
                         fill=fill, outline=outline, width=width)
        self.draw.ellipse([x2 - radius*2, y1, x2, y1 + radius*2], 
                         fill=fill, outline=outline, width=width)
        self.draw.ellipse([x1, y2 - radius*2, x1 + radius*2, y2], 
                         fill=fill, outline=outline, width=width)
        self.draw.ellipse([x2 - radius*2, y2 - radius*2, x2, y2], 
                         fill=fill, outline=outline, width=width)
        
        # 绘制矩形主体
        self.draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill, outline=None)
        self.draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill, outline=None)
        
        # 绘制边框
        self.draw.line([x1 + radius, y1, x2 - radius, y1], fill=outline, width=width)
        self.draw.line([x1 + radius, y2, x2 - radius, y2], fill=outline, width=width)
        self.draw.line([x1, y1 + radius, x1, y2 - radius], fill=outline, width=width)
        self.draw.line([x2, y1 + radius, x2, y2 - radius], fill=outline, width=width)
    
    def draw_arrow(
        self, 
        start: Tuple[int, int], 
        end: Tuple[int, int], 
        color: str = Color.BLACK, 
        width: int = 3,
        arrow_size: int = 15
    ):
        """
        绘制箭头
        
        Args:
            start: 起点 (x, y)
            end: 终点 (x, y)
            color: 颜色
            width: 线条宽度
            arrow_size: 箭头大小
        """
        x1, y1 = start
        x2, y2 = end
        
        # 绘制线条
        self.draw.line([x1, y1, x2, y2], fill=color, width=width)
        
        # 计算箭头
        angle = math.atan2(y2 - y1, x2 - x1)
        arrow_angle = math.pi / 6
        
        x3 = x2 - arrow_size * math.cos(angle - arrow_angle)
        y3 = y2 - arrow_size * math.sin(angle - arrow_angle)
        x4 = x2 - arrow_size * math.cos(angle + arrow_angle)
        y4 = y2 - arrow_size * math.sin(angle + arrow_angle)
        
        self.draw.polygon([(x2, y2), (x3, y3), (x4, y4)], fill=color)
    
    def draw_curved_arrow(
        self,
        start: Tuple[int, int],
        end: Tuple[int, int],
        control_offset: Tuple[int, int] = (50, 50),
        color: str = Color.BLACK,
        width: int = 2
    ):
        """
        绘制曲线箭头
        
        Args:
            start: 起点
            end: 终点
            control_offset: 控制点偏移
            color: 颜色
            width: 线条宽度
        """
        x1, y1 = start
        x2, y2 = end
        cx = (x1 + x2) / 2 + control_offset[0]
        cy = (y1 + y2) / 2 + control_offset[1]
        
        # 绘制贝塞尔曲线（简化版）
        points = []
        for t in range(0, 101, 5):
            t = t / 100
            x = (1-t)**2 * x1 + 2*(1-t)*t * cx + t**2 * x2
            y = (1-t)**2 * y1 + 2*(1-t)*t * cy + t**2 * y2
            points.append((x, y))
        
        for i in range(len(points) - 1):
            self.draw.line([points[i], points[i+1]], fill=color, width=width)
        
        # 绘制箭头
        angle = math.atan2(y2 - points[-2][1], x2 - points[-2][0])
        arrow_size = 12
        arrow_angle = math.pi / 6
        
        x3 = x2 - arrow_size * math.cos(angle - arrow_angle)
        y3 = y2 - arrow_size * math.sin(angle - arrow_angle)
        x4 = x2 - arrow_size * math.cos(angle + arrow_angle)
        y4 = y2 - arrow_size * math.sin(angle + arrow_angle)
        
        self.draw.polygon([(x2, y2), (x3, y3), (x4, y4)], fill=color)
    
    def draw_text_multiline(
        self, 
        text: str, 
        position: Tuple[int, int], 
        font_size: int = 18,
        fill: str = Color.BLACK, 
        align: str = 'center',
        line_spacing: int = 5
    ):
        """
        绘制多行文本
        
        Args:
            text: 文本内容（可以包含\\n）
            position: 位置 (x, y)
            font_size: 字体大小
            fill: 文本颜色
            align: 对齐方式 ('left', 'center', 'right')
            line_spacing: 行间距
        """
        lines = text.split('\n')
        x, y = position
        font = self.get_font(font_size)
        
        for line in lines:
            bbox = self.draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            if align == 'center':
                self.draw.text((x - text_width/2, y), line, font=font, fill=fill)
            elif align == 'right':
                self.draw.text((x - text_width, y), line, font=font, fill=fill)
            else:  # left
                self.draw.text((x, y), line, font=font, fill=fill)
            
            y += text_height + line_spacing
    
    def draw_text_box(
        self,
        text: str,
        xy: Tuple[int, int, int, int],
        font_size: int = 18,
        text_color: str = Color.BLACK,
        bg_color: str = Color.WHITE,
        border_color: str = Color.BLACK,
        border_width: int = 2,
        radius: int = 15
    ):
        """
        绘制带文本的框
        
        Args:
            text: 文本内容
            xy: (x1, y1, x2, y2) 框的坐标
            font_size: 字体大小
            text_color: 文本颜色
            bg_color: 背景颜色
            border_color: 边框颜色
            border_width: 边框宽度
            radius: 圆角半径
        """
        x1, y1, x2, y2 = xy
        
        # 绘制框
        self.draw_rounded_rectangle(xy, radius, bg_color, border_color, border_width)
        
        # 绘制文本
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        
        font = self.get_font(font_size)
        bbox = self.draw.textbbox((0, 0), text, font=font)
        text_height = bbox[3] - bbox[1]
        
        self.draw_text_multiline(
            text, 
            (center_x, center_y - text_height/2), 
            font_size, 
            text_color, 
            'center'
        )
    
    def draw_circle(
        self,
        center: Tuple[int, int],
        radius: int,
        fill: str = Color.WHITE,
        outline: str = Color.BLACK,
        width: int = 2
    ):
        """绘制圆形"""
        x, y = center
        self.draw.ellipse(
            [x - radius, y - radius, x + radius, y + radius],
            fill=fill,
            outline=outline,
            width=width
        )
    
    def draw_legend(
        self,
        items: List[Tuple[str, str]],
        position: Tuple[int, int],
        box_size: int = 40,
        font_size: int = 18,
        spacing: int = 250
    ):
        """
        绘制图例
        
        Args:
            items: [(label, color), ...] 图例项
            position: 起始位置 (x, y)
            box_size: 色块大小
            font_size: 字体大小
            spacing: 项之间的间距
        """
        x, y = position
        
        for i, (label, color) in enumerate(items):
            box_x = x + i * spacing
            
            # 绘制色块
            self.draw_rounded_rectangle(
                (box_x, y, box_x + box_size, y + box_size - 10),
                5,
                color,
                Color.BLACK,
                2
            )
            
            # 绘制标签
            font = self.get_font(font_size)
            self.draw.text((box_x + box_size + 10, y + 5), label, font=font, fill=Color.BLACK)
    
    def save(self, output_path: str, dpi: int = 300):
        """
        保存图片
        
        Args:
            output_path: 输出路径
            dpi: 分辨率
        """
        if self.img:
            self.img.save(output_path, dpi=(dpi, dpi))
            print(f"✓ 图表已保存到: {output_path}")
        else:
            print("错误: 没有可保存的图片，请先创建画布")


class FlowDiagramGenerator(DiagramGenerator):
    """流程图生成器"""
    
    def create_simple_flow(
        self,
        steps: List[Dict],
        output_path: str,
        title: str = "流程图"
    ):
        """
        创建简单的线性流程图
        
        Args:
            steps: 步骤列表，每个步骤是字典: {
                'text': '步骤文本',
                'color': '背景颜色',
                'note': '可选的注释'
            }
            output_path: 输出路径
            title: 标题
        """
        self.create_canvas()
        
        # 绘制标题
        title_font = self.get_font(36)
        bbox = self.draw.textbbox((0, 0), title, font=title_font)
        title_width = bbox[2] - bbox[0]
        self.draw.text((self.width//2 - title_width//2, 30), title, font=title_font, fill=Color.BLACK)
        
        # 计算步骤位置
        step_height = 80
        step_width = 600
        step_spacing = 60
        start_y = 120
        
        center_x = self.width // 2
        
        for i, step in enumerate(steps):
            y = start_y + i * (step_height + step_spacing)
            
            # 绘制步骤框
            box = (
                center_x - step_width//2, 
                y, 
                center_x + step_width//2, 
                y + step_height
            )
            
            color = step.get('color', Color.INFO)
            self.draw_text_box(
                step['text'],
                box,
                font_size=20,
                bg_color=color,
                border_color=Color.BLACK,
                border_width=3
            )
            
            # 绘制箭头（如果不是最后一步）
            if i < len(steps) - 1:
                self.draw_arrow(
                    (center_x, y + step_height),
                    (center_x, y + step_height + step_spacing),
                    Color.BLACK,
                    3
                )
            
            # 绘制注释（如果有）
            if 'note' in step:
                self.draw.text(
                    (center_x + step_width//2 + 20, y + 20),
                    step['note'],
                    font=self.get_font(14),
                    fill=Color.GRAY
                )
        
        self.save(output_path)


class ComparisonDiagramGenerator(DiagramGenerator):
    """对比图生成器"""
    
    def create_two_column_comparison(
        self,
        left_data: Dict,
        right_data: Dict,
        output_path: str,
        title: str = "对比图"
    ):
        """
        创建两列对比图
        
        Args:
            left_data: 左侧数据 {
                'title': '标题',
                'items': [('文本', y位置, '颜色'), ...],
                'features': ['特点1', '特点2', ...]
            }
            right_data: 右侧数据（格式同上）
            output_path: 输出路径
            title: 总标题
        """
        self.create_canvas()
        
        # 绘制分割线
        self.draw.line(
            [(self.width//2, 80), (self.width//2, self.height - 100)],
            fill=Color.GRAY,
            width=3
        )
        
        # 左侧
        self._draw_comparison_column(left_data, 0, self.width//2)
        
        # 右侧
        self._draw_comparison_column(right_data, self.width//2, self.width)
        
        # 底部说明
        if title:
            note_box = (100, self.height - 90, self.width - 100, self.height - 20)
            self.draw_rounded_rectangle(note_box, 15, '#FFFACD', Color.ORANGE, 2)
            bbox = self.draw.textbbox((0, 0), title, font=self.get_font(24))
            text_width = bbox[2] - bbox[0]
            self.draw.text(
                (self.width//2 - text_width//2, self.height - 70),
                title,
                font=self.get_font(24),
                fill=Color.BLACK
            )
        
        self.save(output_path)
    
    def _draw_comparison_column(self, data: Dict, start_x: int, end_x: int):
        """绘制对比图的一列"""
        center_x = (start_x + end_x) // 2
        
        # 标题
        title = data.get('title', '')
        bbox = self.draw.textbbox((0, 0), title, font=self.get_font(28))
        title_width = bbox[2] - bbox[0]
        self.draw.text((center_x - title_width//2, 30), title, font=self.get_font(28), fill=Color.BLACK)
        
        # 项目列表
        items = data.get('items', [])
        for text, y, color in items:
            box = (start_x + 50, y, end_x - 50, y + 80)
            self.draw_text_box(text, box, font_size=20, bg_color=color)
        
        # 特点
        features = data.get('features', [])
        if features:
            self.draw.text((center_x - 50, 920), '特点：', font=self.get_font(24), fill=Color.BLACK)
            for i, feature in enumerate(features):
                self.draw.text(
                    (start_x + 50, 970 + i*35),
                    feature,
                    font=self.get_font(18),
                    fill=Color.DARK_RED if '❌' in feature else Color.DARK_GREEN
                )


# 便捷函数
def create_simple_flow_diagram(steps: List[Dict], output_path: str, title: str = "流程图"):
    """快速创建简单流程图"""
    generator = FlowDiagramGenerator()
    generator.create_simple_flow(steps, output_path, title)


def create_comparison_diagram(left_data: Dict, right_data: Dict, output_path: str, title: str = ""):
    """快速创建对比图"""
    generator = ComparisonDiagramGenerator()
    generator.create_two_column_comparison(left_data, right_data, output_path, title)


if __name__ == "__main__":
    # 示例：创建简单流程图
    print("示例1: 创建简单流程图")
    steps = [
        {'text': '步骤1: 开始', 'color': Color.INFO},
        {'text': '步骤2: 处理数据', 'color': Color.HUMAN, 'note': '需要人工确认'},
        {'text': '步骤3: AI分析', 'color': Color.AI},
        {'text': '步骤4: 完成', 'color': Color.SUCCESS},
    ]
    create_simple_flow_diagram(steps, '/tmp/test_flow.png', '示例流程图')
    
    # 示例：创建对比图
    print("\n示例2: 创建对比图")
    left = {
        'title': '传统方式',
        'items': [
            ('步骤1', 150, Color.ERROR),
            ('步骤2', 280, Color.WARNING),
            ('步骤3', 410, Color.INFO),
        ],
        'features': ['❌ 慢', '❌ 复杂']
    }
    right = {
        'title': '新方式',
        'items': [
            ('快速迭代', 150, Color.SUCCESS),
            ('简单直接', 280, Color.SUCCESS),
        ],
        'features': ['✅ 快', '✅ 简单']
    }
    create_comparison_diagram(left, right, '/tmp/test_comparison.png', '方式对比')
    
    print("\n✅ 示例图表生成完成!")
