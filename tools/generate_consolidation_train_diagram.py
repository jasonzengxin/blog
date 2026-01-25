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
        self.width = 1700
        self.height = 1300
        self.create_canvas()
        
        # 标题
        self.draw_text_multiline(
            'Consolidation Train 工作流程',
            (self.width//2, 50),
            38,
            Color.BLACK,
            'center'
        )
        
        # 副标题
        self.draw_text_multiline(
            '双轨并行：持续需求 + 自动化测试修复',
            (self.width//2, 105),
            22,
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
        track_y1 = 230  # 主力开发轨道
        track_y2 = 480  # Consolidation 轨道
        track_start = 200
        track_end = 1550
        
        # 轨道 1: 主力开发 Session
        self.draw_text_box(
            '主力开发 Session (Terminal 1)\n专注创造',
            (30, track_y1 - 50, 190, track_y1 + 50),
            font_size=15,
            bg_color=Color.HUMAN,
            border_width=2
        )
        
        # 绘制轨道线
        self.draw.line(
            [(track_start, track_y1), (track_end, track_y1)],
            fill=Color.BLACK,
            width=5
        )
        
        # 轨道 2: Consolidation Train
        self.draw_text_box(
            'Consolidation Train\n自动化测试修复',
            (30, track_y2 - 50, 190, track_y2 + 50),
            font_size=15,
            bg_color=Color.AI,
            border_width=2
        )
        
        # 绘制轨道线
        self.draw.line(
            [(track_start, track_y2), (track_end, track_y2)],
            fill=Color.BLACK,
            width=5
        )
        
        # 绘制连接箭头 - 调整位置
        arrow_x = track_start + 100
        self.draw_curved_arrow(
            (arrow_x, track_y1 + 15),
            (arrow_x, track_y2 - 15),
            control_offset=(60, 0),
            color=Color.GRAY,
            width=2
        )
        self.draw.text(
            (arrow_x + 65, (track_y1 + track_y2) // 2 - 15),
            '需求登上\nTrain',
            font=self.get_font(15),
            fill=Color.GRAY
        )
    
    def _draw_timeline(self):
        """绘制时间线"""
        track_start = 200
        time_points = [
            (track_start + 100, 'T0\n提需求1'),
            (track_start + 450, 'T0+10min\n提需求2'),
            (track_start + 800, '到站\n测试通过'),
            (track_start + 1150, 'T0+15min\nTrain到站'),
        ]
        
        for x, label in time_points:
            # 垂直线
            self.draw.line(
                [(x, 165), (x, 565)],
                fill=Color.LIGHT_GRAY,
                width=2
            )
            # 时间标签
            self.draw_text_multiline(
                label,
                (x, 595),
                15,
                Color.GRAY,
                'center'
            )
    
    def _draw_train_process(self):
        """绘制 Train 运行过程"""
        track_y1 = 230
        track_y2 = 480
        track_start = 200
        
        # T0: 人提需求 1
        x1 = track_start + 100
        self.draw_circle((x1, track_y1), 25, '#FFE5B4', Color.BLACK, 3)
        self.draw_text_multiline('需求1', (x1, track_y1 - 10), 16, Color.BLACK, 'center')
        
        # T0+5min: Train 发车 - 第一个 Train
        x_train1 = track_start + 250
        
        # 绘制火车头
        train_box = (x_train1 - 90, track_y2 - 60, x_train1 + 90, track_y2 + 60)
        self.draw_rounded_rectangle(
            train_box,
            15,
            '#B4D7FF',
            Color.BLUE,
            4
        )
        self.draw_text_multiline(
            '🚂 Train\n需求1',
            (x_train1, track_y2 - 10),
            18,
            Color.BLACK,
            'center'
        )
        
        # Train 的任务列表 - 放在下方，不重叠
        task_y = track_y2 + 70
        self.draw_text_box(
            '编译\n↓\n测试\n↓\n修复',
            (x_train1 - 70, task_y, x_train1 + 70, task_y + 140),
            font_size=16,
            bg_color='#E8F5E9',
            border_color=Color.GREEN,
            border_width=2
        )
        
        # T0+10min: 人提需求 2（同时 Train 还在运行）
        x3 = track_start + 450
        self.draw_circle((x3, track_y1), 25, '#FFE5B4', Color.BLACK, 3)
        self.draw_text_multiline('需求2', (x3, track_y1 - 10), 16, Color.BLACK, 'center')
        
        # 显示 Train 正在运行
        x_mid = track_start + 550
        self.draw.line(
            [(x_train1 + 90, track_y2), (x_mid, track_y2)],
            fill=Color.BLUE,
            width=4
        )
        self.draw_text_multiline(
            '运行中...',
            ((x_train1 + x_mid) // 2, track_y2 - 50),
            16,
            Color.BLUE,
            'center'
        )
        
        # T0+15min: Train 到站
        x4 = track_start + 800
        self.draw_circle((x4, track_y2), 35, Color.SUCCESS, Color.DARK_GREEN, 5)
        self.draw_text_multiline('到站\n✓', (x4, track_y2 - 15), 20, Color.DARK_GREEN, 'center')
        
        # 下一班 Train 准备发车（需求2登车）
        self.draw_curved_arrow(
            (x3, track_y1 + 30),
            (x4 + 150, track_y2 - 50),
            control_offset=(80, 60),
            color=Color.GRAY,
            width=2
        )
        
        # 新的 Train
        x_train2 = track_start + 1150
        train_box2 = (x_train2 - 90, track_y2 - 50, x_train2 + 90, track_y2 + 50)
        self.draw_rounded_rectangle(
            train_box2,
            15,
            '#B4D7FF',
            Color.BLUE,
            3
        )
        self.draw_text_multiline(
            '🚂 下一班\n需求2',
            (x_train2, track_y2 - 8),
            16,
            Color.BLACK,
            'center'
        )
    
    def _draw_legend(self):
        """绘制图例"""
        legend_x = 100
        legend_y = 710
        
        legend_items = [
            ('主力开发（人）', Color.HUMAN),
            ('Consolidation Train（AI）', Color.AI),
            ('成功到站', Color.SUCCESS),
            ('运行过程', '#E8F5E9'),
        ]
        
        self.draw_legend(legend_items, (legend_x, legend_y), spacing=320)
    
    def _draw_notes(self):
        """绘制说明"""
        notes = [
            '💡 核心优势：',
            '  • 人可以持续提需求，无需等待',
            '  • AI 自动处理编译、测试、修复',
            '  • 需求按顺序处理，避免冲突',
            '  • 解放重复劳动，可以去喝咖啡 ☕️',
        ]
        
        y_start = 830
        for i, note in enumerate(notes):
            self.draw.text(
                (100, y_start + i * 35),
                note,
                font=self.get_font(18 if i == 0 else 16),
                fill=Color.BLACK if i == 0 else Color.DARK_GREEN
            )
        
        # 挑战说明
        challenges = [
            '⚠️  挑战：',
            '  • 需求冲突：通过顺序到站解决',
            '  • Token 成本：按需触发，调整间隔',
        ]
        
        y_start = 1060
        for i, challenge in enumerate(challenges):
            self.draw.text(
                (100, y_start + i * 35),
                challenge,
                font=self.get_font(18 if i == 0 else 16),
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
