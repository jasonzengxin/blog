"""
使用通用图表生成器创建 Vibe Programming 相关的图表

这个脚本展示了如何使用 diagram_generator.py 来创建复杂的自定义图表
"""

from diagram_generator import DiagramGenerator, Color
import math


class VibeProgrammingDiagramGenerator(DiagramGenerator):
    """Vibe Programming 专用图表生成器"""
    
    def create_flow_diagram(self, output_path: str):
        """创建 Vibe Programming 流程图"""
        self.width = 1400
        self.height = 1200
        self.create_canvas()
        
        # 标题
        title = 'Vibe Programming 工作流程'
        self.draw_text_multiline(title, (self.width//2, 50), 36, Color.BLACK, 'center')
        
        # 1. 起点 - 人给出模糊提示词
        self.draw_text_box(
            '1. 人：给出模糊提示词\n"做一个用户管理页面"',
            (150, 120, 550, 220),
            font_size=18,
            bg_color=Color.HUMAN,
            border_width=3
        )
        
        # 箭头1
        self.draw_arrow((350, 220), (350, 300), Color.BLACK)
        self.draw.text((380, 250), 'context:\n语言、风格', 
                      font=self.get_font(14), fill=Color.GRAY)
        
        # 2. AI生成代码
        self.draw_text_box(
            '2. AI：直接生成实现\n• 组件结构\n• 数据模型\n• 交互逻辑',
            (120, 300, 580, 450),
            font_size=18,
            bg_color=Color.AI,
            border_width=3
        )
        
        # 箭头2
        self.draw_arrow((350, 450), (350, 530), Color.BLACK)
        
        # 3. 代码状态
        self.draw_text_box(
            '3. 可运行的代码',
            (150, 530, 550, 610),
            font_size=24,
            bg_color=Color.CODE,
            border_width=3
        )
        
        # 箭头3
        self.draw_arrow((350, 610), (350, 690), Color.BLACK)
        
        # 4. 决策点
        self.draw_text_box(
            '4. 人：测试和反馈',
            (100, 690, 600, 790),
            font_size=24,
            bg_color=Color.DECISION,
            border_width=3
        )
        
        # 分支1: 运行错误
        self.draw_text_box(
            '情况1: 运行错误\n"编译失败"、"依赖缺失"',
            (700, 120, 1300, 250),
            font_size=18,
            bg_color='#FFE4E4',
            border_color=Color.RED,
            border_width=3
        )
        self.draw_arrow((600, 710), (700, 185), Color.RED, width=2)
        self.draw_arrow((700, 210), (580, 360), Color.RED)
        self.draw.text((620, 280), '粘贴错误信息', 
                      font=self.get_font(14), fill=Color.RED)
        
        # 分支2: 功能不符
        self.draw_text_box(
            '情况2: 功能不符\n"需要action buttons"\n"添加表单验证"',
            (700, 300, 1300, 460),
            font_size=18,
            bg_color='#FFF8E4',
            border_color=Color.ORANGE,
            border_width=3
        )
        self.draw_arrow((600, 740), (700, 380), Color.ORANGE, width=2)
        self.draw_arrow((700, 400), (580, 390), Color.ORANGE)
        self.draw.text((620, 390), '提出改进要求', 
                      font=self.get_font(14), fill=Color.ORANGE)
        
        # 分支3: 满足预期
        self.draw_text_box(
            '情况3: 达到预期 ✓\n功能完成！',
            (700, 510, 1300, 630),
            font_size=20,
            bg_color='#E4FFE4',
            border_color=Color.GREEN,
            border_width=3,
            text_color=Color.DARK_GREEN
        )
        self.draw_arrow((600, 740), (700, 570), Color.GREEN, width=2)
        self.draw_arrow((1000, 630), (1000, 720), Color.GREEN, width=4)
        
        self.draw_text_box(
            '进入下一个 Feature',
            (700, 720, 1300, 800),
            font_size=24,
            bg_color='#C8FFC8',
            border_color=Color.DARK_GREEN,
            border_width=3,
            text_color=Color.DARK_GREEN
        )
        
        # 图例
        legend_items = [
            ('人的活动', Color.HUMAN),
            ('AI的活动', Color.AI),
            ('代码状态', Color.CODE),
            ('决策点', Color.DECISION),
        ]
        self.draw_legend(legend_items, (100, 880))
        
        # 核心理念
        self.draw_text_box(
            '💡 核心：快速迭代，边做边调整',
            (100, 1050, 700, 1120),
            font_size=24,
            bg_color='#FFFACD',
            border_color=Color.ORANGE
        )
        
        self.save(output_path)
    
    def create_comparison_diagram(self, output_path: str):
        """创建传统方式 vs Vibe Programming 对比图"""
        self.width = 1600
        self.height = 1200
        self.create_canvas()
        
        # 分割线
        self.draw.line(
            [(self.width//2, 80), (self.width//2, self.height - 100)],
            fill=Color.GRAY,
            width=3
        )
        
        # 左侧：传统方式
        self.draw_text_multiline('传统开发方式', (self.width//4, 50), 36, Color.BLACK, 'center')
        
        steps_traditional = [
            ('1. 需求文档', 150, '#FFD4D4'),
            ('2. 概要设计', 280, '#FFE4D4'),
            ('3. 详细设计', 410, '#FFF4D4'),
            ('4. 编码实现', 540, '#E4F4FF'),
            ('5. 测试', 670, '#E4FFE4'),
            ('6. 部署', 800, '#E4E4FF'),
        ]
        
        for i, (step, y, color) in enumerate(steps_traditional):
            self.draw_text_box(
                step,
                (50, y, self.width//2 - 100, y + 80),
                font_size=24,
                bg_color=color,
                border_width=3
            )
            
            # 箭头
            if i < len(steps_traditional) - 1:
                self.draw_arrow(
                    (self.width//4, y + 80),
                    (self.width//4, steps_traditional[i+1][1]),
                    Color.BLACK
                )
        
        # 左侧特点
        self.draw.text((self.width//4 - 50, 920), '特点：', 
                      font=self.get_font(24), fill=Color.BLACK)
        features_traditional = [
            '❌ 前期需要想清楚所有细节',
            '❌ 设计错误成本高',
            '❌ 周期长，反馈慢',
            '❌ 需要手写大量代码',
        ]
        for i, feature in enumerate(features_traditional):
            self.draw.text((50, 970 + i*35), feature, 
                          font=self.get_font(18), fill=Color.DARK_RED)
        
        # 右侧：Vibe Programming
        self.draw_text_multiline('Vibe Programming', (self.width*3//4, 50), 
                                36, Color.BLACK, 'center')
        
        # 绘制循环
        center_x = self.width * 3 // 4
        center_y = 450
        radius = 200
        
        # 外圈
        self.draw.ellipse(
            [center_x - radius - 30, center_y - radius - 30,
             center_x + radius + 30, center_y + radius + 30],
            outline=Color.BLUE,
            width=5
        )
        
        # 箭头指示循环
        self.draw_arrow(
            (center_x + radius + 20, center_y - 10),
            (center_x + radius + 20, center_y + 30),
            Color.BLUE,
            width=5
        )
        
        # 三个步骤
        steps_vibe = [
            ('模糊需求', 0, Color.HUMAN),
            ('AI生成', -120, Color.AI),
            ('测试反馈', -240, '#FFE4E4'),
        ]
        
        for step, angle_offset, color in steps_vibe:
            angle_rad = math.radians(angle_offset + 90)
            x = center_x + radius * math.cos(angle_rad)
            y = center_y - radius * math.sin(angle_rad)
            
            self.draw_text_box(
                step,
                (x - 90, y - 35, x + 90, y + 35),
                font_size=24,
                bg_color=color,
                border_width=3
            )
        
        # 中心文字
        self.draw_circle((center_x, center_y), 70, '#FFFACD', Color.ORANGE, width=3)
        self.draw_text_multiline('快速\n迭代', (center_x, center_y - 20), 
                                28, Color.BLACK, 'center')
        
        # 右侧特点
        self.draw.text((self.width*3//4 - 50, 720), '特点：', 
                      font=self.get_font(24), fill=Color.BLACK)
        features_vibe = [
            '✅ 可以边做边想',
            '✅ 试错成本极低',
            '✅ 即时反馈，快速调整',
            '✅ AI自动生成代码',
        ]
        for i, feature in enumerate(features_vibe):
            self.draw.text((self.width//2 + 50, 770 + i*35), feature,
                          font=self.get_font(18), fill=Color.DARK_GREEN)
        
        # 底部说明
        note_text = '核心区别：传统方式是"线性瀑布"，Vibe Programming是"快速迭代循环"'
        self.draw_text_box(
            note_text,
            (100, 1100, self.width - 100, 1170),
            font_size=24,
            bg_color='#FFFACD',
            border_color=Color.ORANGE
        )
        
        self.save(output_path)


def main():
    """主函数：生成 Vibe Programming 相关图表"""
    import os
    
    # 确定输出目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    blog_dir = os.path.dirname(script_dir)
    output_dir = os.path.join(blog_dir, 'source/_posts')
    
    # 创建生成器
    generator = VibeProgrammingDiagramGenerator()
    
    # 生成流程图
    print("正在生成 Vibe Programming 流程图...")
    flow_path = os.path.join(output_dir, 'vibe-programming-flow.png')
    generator.create_flow_diagram(flow_path)
    
    # 生成对比图
    print("正在生成 Vibe Programming 对比图...")
    comparison_path = os.path.join(output_dir, 'vibe-programming-comparison.png')
    generator.create_comparison_diagram(comparison_path)
    
    print("\n✅ 所有图表生成完成！")
    print(f"输出目录: {output_dir}")


if __name__ == "__main__":
    main()
