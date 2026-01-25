#!/usr/bin/env python3
"""
图表生成命令行工具

快速调用各种图表生成脚本

使用方法:
    python3 generate.py vibe              # 生成 Vibe Programming 图表
    python3 generate.py template          # 运行模板示例
    python3 generate.py list              # 列出所有可用的生成器
"""

import sys
import os
import importlib.util


def load_module(module_name, file_path):
    """动态加载模块"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def generate_vibe():
    """生成 Vibe Programming 图表"""
    print("🎨 生成 Vibe Programming 图表...\n")
    module = load_module("generate_vibe", "generate_vibe_programming_diagrams.py")
    module.main()


def run_template():
    """运行模板示例"""
    print("🎨 运行模板示例...\n")
    module = load_module("template", "template_new_diagram.py")
    module.main()


def list_generators():
    """列出所有可用的生成器"""
    print("📋 可用的图表生成器:\n")
    print("1. vibe      - Vibe Programming 图表")
    print("   用法: python3 generate.py vibe")
    print()
    print("2. template  - 运行模板示例（生成4个示例图表）")
    print("   用法: python3 generate.py template")
    print()
    print("💡 提示:")
    print("   - 查看 README.md 了解更多详细用法")
    print("   - 复制 template_new_diagram.py 创建你自己的生成器")
    print("   - 所有图表默认保存到 source/_posts/ 目录")


def show_help():
    """显示帮助信息"""
    print("图表生成工具 - 命令行入口\n")
    print("用法: python3 generate.py [命令]\n")
    print("可用命令:")
    print("  vibe      生成 Vibe Programming 图表")
    print("  template  运行模板示例")
    print("  list      列出所有可用的生成器")
    print("  help      显示此帮助信息")
    print("\n示例:")
    print("  python3 generate.py vibe")
    print("  python3 generate.py template")
    print("\n更多信息请查看 README.md")


def main():
    """主函数"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    commands = {
        'vibe': generate_vibe,
        'template': run_template,
        'list': list_generators,
        'help': show_help,
        '-h': show_help,
        '--help': show_help,
    }
    
    if command in commands:
        commands[command]()
    else:
        print(f"❌ 未知命令: {command}")
        print(f"运行 'python3 generate.py help' 查看帮助")
        sys.exit(1)


if __name__ == "__main__":
    main()
