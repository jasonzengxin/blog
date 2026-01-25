"""
新图表生成脚本模板

复制这个文件并重命名，然后修改成你需要的图表
例如: cp template_new_diagram.py generate_my_article_diagrams.py
"""

from diagram_generator import (
    DiagramGenerator, 
    FlowDiagramGenerator,
    ComparisonDiagramGenerator,
    Color,
    create_simple_flow_diagram,
    create_comparison_diagram
)
import os


def example_1_simple_flow():
    """示例1: 使用便捷函数创建简单流程图"""
    steps = [
        {
            'text': '步骤1: 需求分析', 
            'color': Color.HUMAN,
            'note': '可选注释'
        },
        {
            'text': '步骤2: 设计方案', 
            'color': Color.AI
        },
        {
            'text': '步骤3: 编码实现', 
            'color': Color.CODE
        },
        {
            'text': '步骤4: 测试验证', 
            'color': Color.DECISION
        },
        {
            'text': '步骤5: 上线部署', 
            'color': Color.SUCCESS
        },
    ]
    
    output_path = get_output_path('example_simple_flow.png')
    create_simple_flow_diagram(steps, output_path, '开发流程')
    print(f"✓ 示例1完成: {output_path}")


def example_2_comparison():
    """示例2: 使用便捷函数创建对比图"""
    left_data = {
        'title': '方案A',
        'items': [
            ('需求分析', 150, '#FFD4D4'),
            ('技术选型', 280, '#FFE4D4'),
            ('开发实现', 410, '#FFF4D4'),
            ('测试上线', 540, '#E4FFE4'),
        ],
        'features': [
            '❌ 周期长',
            '❌ 成本高',
            '❌ 风险大',
        ]
    }
    
    right_data = {
        'title': '方案B',
        'items': [
            ('快速原型', 150, Color.SUCCESS),
            ('迭代优化', 280, Color.SUCCESS),
            ('持续交付', 410, Color.SUCCESS),
        ],
        'features': [
            '✅ 周期短',
            '✅ 成本低',
            '✅ 风险小',
        ]
    }
    
    output_path = get_output_path('example_comparison.png')
    create_comparison_diagram(
        left_data, 
        right_data, 
        output_path, 
        '方案对比：传统开发 vs 敏捷开发'
    )
    print(f"✓ 示例2完成: {output_path}")


def example_3_custom():
    """示例3: 自定义复杂图表"""
    
    class CustomDiagramGenerator(DiagramGenerator):
        def create_custom_diagram(self, output_path):
            # 创建画布
            self.create_canvas()
            
            # 绘制标题
            self.draw_text_multiline(
                '自定义图表示例',
                (self.width // 2, 50),
                font_size=36,
                fill=Color.BLACK,
                align='center'
            )
            
            # 绘制多个框和箭头
            boxes = [
                {'text': '输入', 'pos': (200, 200, 500, 300), 'color': Color.HUMAN},
                {'text': '处理', 'pos': (600, 200, 900, 300), 'color': Color.AI},
                {'text': '输出', 'pos': (1000, 200, 1300, 300), 'color': Color.SUCCESS},
            ]
            
            for i, box in enumerate(boxes):
                self.draw_text_box(
                    box['text'],
                    box['pos'],
                    font_size=24,
                    bg_color=box['color'],
                    border_width=3
                )
                
                # 绘制箭头连接（除了最后一个）
                if i < len(boxes) - 1:
                    x1 = box['pos'][2]
                    y1 = (box['pos'][1] + box['pos'][3]) // 2
                    x2 = boxes[i + 1]['pos'][0]
                    y2 = y1
                    self.draw_arrow((x1, y1), (x2, y2), Color.BLACK, width=3)
            
            # 添加说明框
            self.draw_text_box(
                '这是一个自定义的复杂图表示例\n你可以任意组合各种元素',
                (200, 400, 1300, 500),
                font_size=20,
                bg_color='#FFFACD',
                border_color=Color.ORANGE
            )
            
            # 添加图例
            self.draw_legend(
                [
                    ('人工操作', Color.HUMAN),
                    ('自动处理', Color.AI),
                    ('最终结果', Color.SUCCESS),
                ],
                (200, 600)
            )
            
            # 绘制圆形和曲线箭头（高级示例）
            self.draw_circle((self.width // 2, 800), 80, '#FFE5B4', Color.ORANGE, 3)
            self.draw_text_multiline(
                '核心\n概念',
                (self.width // 2, 785),
                font_size=24,
                align='center'
            )
            
            # 保存
            self.save(output_path)
    
    # 使用自定义生成器
    generator = CustomDiagramGenerator(width=1500, height=1000)
    output_path = get_output_path('example_custom.png')
    generator.create_custom_diagram(output_path)
    print(f"✓ 示例3完成: {output_path}")


def example_4_architecture():
    """示例4: 架构图示例"""
    
    class ArchitectureDiagramGenerator(DiagramGenerator):
        def create_architecture(self, output_path):
            self.width = 1400
            self.height = 1000
            self.create_canvas()
            
            # 标题
            self.draw_text_multiline(
                '系统架构图',
                (self.width // 2, 40),
                font_size=36,
                align='center'
            )
            
            # 三层架构
            layers = [
                {
                    'name': '前端层',
                    'y': 150,
                    'color': '#E3F2FD',
                    'components': ['Web界面', '移动端', 'API接口']
                },
                {
                    'name': '应用层',
                    'y': 400,
                    'color': '#FFF3E0',
                    'components': ['业务逻辑', '数据处理', '任务调度']
                },
                {
                    'name': '数据层',
                    'y': 650,
                    'color': '#E8F5E9',
                    'components': ['数据库', '缓存', '文件存储']
                },
            ]
            
            for layer in layers:
                # 绘制层标签
                self.draw_text_box(
                    layer['name'],
                    (50, layer['y'], 250, layer['y'] + 80),
                    font_size=24,
                    bg_color=layer['color'],
                    border_width=3
                )
                
                # 绘制组件
                comp_width = 280
                start_x = 350
                for i, comp in enumerate(layer['components']):
                    x = start_x + i * (comp_width + 40)
                    self.draw_text_box(
                        comp,
                        (x, layer['y'] + 10, x + comp_width, layer['y'] + 60),
                        font_size=18,
                        bg_color=Color.WHITE,
                        border_color=Color.GRAY
                    )
            
            # 绘制层之间的连接
            for i in range(len(layers) - 1):
                y1 = layers[i]['y'] + 80
                y2 = layers[i + 1]['y']
                self.draw_arrow(
                    (self.width // 2, y1),
                    (self.width // 2, y2),
                    Color.GRAY,
                    width=2
                )
            
            self.save(output_path)
    
    generator = ArchitectureDiagramGenerator()
    output_path = get_output_path('example_architecture.png')
    generator.create_architecture(output_path)
    print(f"✓ 示例4完成: {output_path}")


def get_output_path(filename):
    """获取输出路径"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    blog_dir = os.path.dirname(script_dir)
    output_dir = os.path.join(blog_dir, 'source/_posts')
    return os.path.join(output_dir, filename)


def main():
    """主函数：运行所有示例"""
    print("=" * 60)
    print("图表生成示例")
    print("=" * 60)
    
    # 运行示例（可以注释掉不需要的）
    example_1_simple_flow()
    example_2_comparison()
    example_3_custom()
    example_4_architecture()
    
    print("\n" + "=" * 60)
    print("✅ 所有示例完成！")
    print("=" * 60)
    print("\n提示：")
    print("1. 查看生成的图片在 source/_posts/ 目录下")
    print("2. 修改这个模板来创建你自己的图表")
    print("3. 参考 README.md 了解更多用法")


if __name__ == "__main__":
    main()
