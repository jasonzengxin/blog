#!/usr/bin/env python3
"""
测试所有图表生成器

运行这个脚本来验证所有功能是否正常工作
"""

import os
import sys


def test_imports():
    """测试导入"""
    print("测试 1/5: 检查模块导入...")
    try:
        from diagram_generator import (
            DiagramGenerator, Color,
            create_simple_flow_diagram,
            create_comparison_diagram
        )
        from common_diagrams import (
            create_timeline,
            create_mindmap,
            create_quadrant_matrix
        )
        print("✅ 所有模块导入成功\n")
        return True
    except Exception as e:
        print(f"❌ 导入失败: {e}\n")
        return False


def test_basic_diagram():
    """测试基础图表生成"""
    print("测试 2/5: 生成基础图表...")
    try:
        from diagram_generator import DiagramGenerator, Color
        
        generator = DiagramGenerator(width=800, height=600)
        generator.create_canvas()
        generator.draw_text_multiline('测试图表', (400, 100), 32, align='center')
        generator.draw_text_box('测试框', (200, 200, 600, 300), bg_color=Color.INFO)
        generator.save('/tmp/test_basic.png')
        
        print("✅ 基础图表生成成功\n")
        return True
    except Exception as e:
        print(f"❌ 生成失败: {e}\n")
        return False


def test_flow_diagram():
    """测试流程图"""
    print("测试 3/5: 生成流程图...")
    try:
        from diagram_generator import create_simple_flow_diagram, Color
        
        steps = [
            {'text': '开始', 'color': Color.INFO},
            {'text': '处理', 'color': Color.HUMAN},
            {'text': '结束', 'color': Color.SUCCESS},
        ]
        create_simple_flow_diagram(steps, '/tmp/test_flow.png', '测试流程')
        
        print("✅ 流程图生成成功\n")
        return True
    except Exception as e:
        print(f"❌ 生成失败: {e}\n")
        return False


def test_timeline():
    """测试时间线"""
    print("测试 4/5: 生成时间线...")
    try:
        from common_diagrams import create_timeline, Color
        
        events = [
            {'date': '2020', 'title': '开始', 'color': Color.INFO},
            {'date': '2021', 'title': '进展', 'color': Color.SUCCESS},
        ]
        create_timeline(events, '/tmp/test_timeline.png', '测试时间线')
        
        print("✅ 时间线生成成功\n")
        return True
    except Exception as e:
        print(f"❌ 生成失败: {e}\n")
        return False


def test_mindmap():
    """测试思维导图"""
    print("测试 5/5: 生成思维导图...")
    try:
        from common_diagrams import create_mindmap
        
        branches = {
            '分支1': ['节点1', '节点2'],
            '分支2': ['节点3'],
        }
        create_mindmap('中心', branches, '/tmp/test_mindmap.png', '测试思维导图')
        
        print("✅ 思维导图生成成功\n")
        return True
    except Exception as e:
        print(f"❌ 生成失败: {e}\n")
        return False


def main():
    """运行所有测试"""
    print("=" * 60)
    print("图表生成工具 - 功能测试")
    print("=" * 60)
    print()
    
    tests = [
        test_imports,
        test_basic_diagram,
        test_flow_diagram,
        test_timeline,
        test_mindmap,
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("=" * 60)
    print("测试结果")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"通过: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 所有测试通过！工具已准备就绪。")
        print("\n💡 下一步:")
        print("   1. 运行 'python3 generate.py vibe' 生成实际图表")
        print("   2. 查看 README.md 了解详细用法")
        print("   3. 复制 template_new_diagram.py 创建自己的图表")
        return 0
    else:
        print(f"\n❌ {total - passed} 个测试失败")
        print("请检查错误信息并确保已安装 Pillow:")
        print("   pip3 install Pillow")
        return 1


if __name__ == "__main__":
    sys.exit(main())
