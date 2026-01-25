"""
生成 Consolidation Train 流程图

展示双轨并行的开发模式：
- 主力开发 Session：人持续提需求
- Consolidation Train：定时自动测试和修复
"""

from diagram_generator import DiagramGenerator, Color
import math


class ConsolidationTrainDiagramGenerator(DiagramGenerator):
    """Consolidation Train 图表生成器"""
    
    def create_consolidation_train_diagram(self, output_path: str):
        """创建 Consolidation Train 工作流程图"""
        self.width = 1600
        self.height = 1200
        self.create_canvas()
        
        # 标题
        self.draw_text_multiline(
            'Consolidation Train 工作流程',
            (self.width//2, 40),
            36,
            Color.BLACK,
            'center'
        )
        
        # 副标题
        self.draw_text_multiline(
            '双轨并行：持续需求 + 自动化测试修复',
            (self.width//2, 90),
            20,
            Color.GRAY,
            'center'
        )
        
        # 绘制两条平行轨道
        self._draw_dual_tracks()
        
        # 绘制时间线
        self._draw_timeline()
        
        # 绘制 Train 运行过程
        self._draw_train_process()
        
        # 绘制图例
        self._draw_legend()
        
        # 添加说明
        self._draw_notes()
        
        self.save(output_path)
    
    def _draw_dual_tracks(self):
        """绘制双轨道"""
        track_y1 = 200  # 主力开发轨道
        track_y2 = 500  # Consolidation 轨道
        track_start = 150
        track_end = 1450
        
        # 轨道 1: 主力开发 Session
        self.draw_text_box(
            '主力开发 Session (Terminal 1)\n专注创造',
            (track_start - 120, track_y1 - 40, track_start, track_y1 + 40),
            font_size=14,
            bg_color=Color.HUMAN,
            border_width=2
        )
        
        # 绘制轨道线
        self.draw.line(
            [(track_start, track_y1), (track_end, track_y1)],
            fill=Color.BLACK,
            width=4
        )
        
        # 轨道 2: Consolidation Train
        self.draw_text_box(
            'Consolidation Train\n自动化测试修复',
            (track_start - 120, track_y2 - 40, track_start, track_y2 + 40),
            font_size=14,
            bg_color=Color.AI,
            border_width=2
        )
        
        # 绘制轨道线
        self.draw.line(
            [(track_start, track_y2), (track_end, track_y2)],
            fill=Color.BLACK,
            width=4
        )
        
        # 绘制连接箭头
        self.draw_curved_arrow(
            (track_start + 200, track_y1 + 10),
            (track_start + 200, track_y2 - 10),
            control_offset=(50, 0),
            color=Color.GRAY,
            width=2
        )
        self.draw.text(
            (track_start + 250, (track_y1 + track_y2) // 2 - 10),
            '需求登上\nTrain',
            font=self.get_font(14),
            fill=Color.GRAY
        )
    
    def _draw_timeline(self):
        """绘制时间线"""
        track_start = 150
        time_points = [
            (track_start + 200, 'T0\n提需求1'),
            (track_start + 500, 'T0+5min\nTrain发车'),
            (track_start + 800, 'T0+10min\n提需求2'),
            (track_start + 1100, 'T0+15min\nTrain到站'),
        ]
        
        for x, label in time_points:
            # 垂直线
            self.draw.line(
                [(x, 150), (x, 550)],
                fill=Color.LIGHT_GRAY,
                width=2
            )
            # 时间标签
            self.draw_text_multiline(
                label,
                (x, 580),
                14,
                Color.GRAY,
                'center'
            )
    
    def _draw_train_process(self):
        """绘制 Train 运行过程"""
        track_y1 = 200
        track_y2 = 500
        track_start = 150
        
        # T0: 人提需求 1
        x1 = track_start + 200
        self.draw_circle((x1, track_y1), 20, '#FFE5B4', Color.BLACK, 3)
        self.draw_text_multiline('需求1', (x1, track_y1 - 8), 14, Color.BLACK, 'center')
        
        # T0+5min: Train 发车
        x2 = track_start + 500
        
        # 绘制火车头
        train_box = (x2 - 80, track_y2 - 50, x2 + 80, track_y2 + 50)
        self.draw_rounded_rectangle(
            train_box,
            15,
            '#B4D7FF',
            Color.BLUE,
            3
        )
        self.draw_text_multiline(
            '🚂 Train\n需求1',
            (x2, track_y2 - 20),
            16,
            Color.BLACK,
            'center'
        )
        
        # Train 的任务列表
        self.draw_text_box(
            '编译\n↓\n测试\n↓\n修复',
            (x2 - 70, track_y2 + 60, x2 + 70, track_y2 + 180),
            font_size=14,
            bg_color='#E8F5E9',
            border_color=Color.GREEN,
            border_width=2
        )
        
        # T0+10min: 人提需求 2（同时 Train 还在运行）
        x3 = track_start + 800
        self.draw_circle((x3, track_y1), 20, '#FFE5B4', Color.BLACK, 3)
        self.draw_text_multiline('需求2', (x3, track_y1 - 8), 14, Color.BLACK, 'center')
        
        # 显示 Train 正在运行
        self.draw.line(
            [(x2 + 80, track_y2), (x3 - 100, track_y2)],
            fill=Color.BLUE,
            width=3
        )
        self.draw_text_multiline(
            '运行中...',
            ((x2 + x3) // 2, track_y2 - 40),
            14,
            Color.BLUE,
            'center'
        )
        
        # T0+15min: Train 到站
        x4 = track_start + 1100
        self.draw_circle((x4, track_y2), 30, Color.SUCCESS, Color.DARK_GREEN, 4)
        self.draw_text_multiline('到站\n✓', (x4, track_y2 - 12), 18, Color.DARK_GREEN, 'center')
        
        # 下一班 Train 准备发车（需求2登车）
        self.draw_curved_arrow(
            (x3, track_y1 + 25),
            (x4 + 100, track_y2 - 35),
            control_offset=(50, 50),
            color=Color.GRAY,
            width=2
        )
        
        # 新的 Train
        train_box2 = (x4 + 80, track_y2 - 40, x4 + 220, track_y2 + 40)
        self.draw_rounded_rectangle(
            train_box2,
            15,
            '#B4D7FF',
            Color.BLUE,
            2
        )
        self.draw_text_multiline(
            '🚂 下一班\n需求2',
            (x4 + 150, track_y2 - 10),
            14,
            Color.BLACK,
            'center'
        )
    
    def _draw_legend(self):
        """绘制图例"""
        legend_x = 100
        legend_y = 650
        
        legend_items = [
            ('主力开发（人）', Color.HUMAN),
            ('Consolidation Train（AI）', Color.AI),
            ('成功到站', Color.SUCCESS),
            ('运行过程', '#E8F5E9'),
        ]
        
        self.draw_legend(legend_items, (legend_x, legend_y), spacing=300)
    
    def _draw_notes(self):
        """绘制说明"""
        notes = [
            '💡 核心优势：',
            '  • 人可以持续提需求，无需等待',
            '  • AI 自动处理编译、测试、修复',
            '  • 需求按顺序处理，避免冲突',
            '  • 解放重复劳动，可以去喝咖啡 ☕️',
        ]
        
        y_start = 750
        for i, note in enumerate(notes):
            self.draw.text(
                (100, y_start + i * 30),
                note,
                font=self.get_font(16 if i == 0 else 14),
                fill=Color.BLACK if i == 0 else Color.DARK_GREEN
            )
        
        # 挑战说明
        challenges = [
            '⚠️  挑战：',
            '  • 需求冲突：通过顺序到站解决',
            '  • Token 成本：按需触发，调整间隔',
        ]
        
        y_start = 950
        for i, challenge in enumerate(challenges):
            self.draw.text(
                (100, y_start + i * 30),
                challenge,
                font=self.get_font(16 if i == 0 else 14),
                fill=Color.BLACK if i == 0 else Color.DARK_RED
            )


def main():
    """主函数：生成 Consolidation Train 图表"""
    import os
    
    # 确定输出目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    blog_dir = os.path.dirname(script_dir)
    output_dir = os.path.join(blog_dir, 'source/_posts/使用-Cursor-编程的感想')
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 创建生成器
    generator = ConsolidationTrainDiagramGenerator()
    
    # 生成流程图
    print("正在生成 Consolidation Train 流程图...")
    output_path = os.path.join(output_dir, 'consolidation-train-flow.png')
    generator.create_consolidation_train_diagram(output_path)
    
    print(f"\n✅ 图表生成完成！")
    print(f"输出路径: {output_path}")


if __name__ == "__main__":
    main()
