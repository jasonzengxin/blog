#!/usr/bin/env python3
"""
本地预览模式切换工具

在 Hexo 语法和标准 Markdown 语法之间切换图片引用
- preview: 转换为标准 Markdown 语法（本地预览）
- deploy: 转换为 Hexo asset_img 语法（部署）
"""

import sys
import os
import re


def convert_to_preview_mode(md_file):
    """转换为本地预览模式（标准 Markdown 语法）"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 将 {% asset_img filename "title" %} 转换为 ![title](./filename)
    pattern = r'{%\s*asset_img\s+([^\s]+)\s+"([^"]+)"\s*%}'
    replacement = r'![\2](./<post-folder>/\1)'
    
    # 获取文章文件夹名
    post_name = os.path.basename(md_file).replace('.md', '')
    replacement = replacement.replace('<post-folder>', post_name)
    
    converted = re.sub(pattern, replacement, content)
    
    # 备份原文件
    backup_file = md_file + '.backup'
    if not os.path.exists(backup_file):
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ 已创建备份: {backup_file}")
    
    # 写入转换后的内容
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(converted)
    
    print(f"✓ 已转换为预览模式: {md_file}")
    print(f"  现在可以在 Markdown 预览器中看到图片了")


def convert_to_deploy_mode(md_file):
    """转换为部署模式（Hexo 语法）"""
    backup_file = md_file + '.backup'
    
    if not os.path.exists(backup_file):
        print(f"✗ 未找到备份文件: {backup_file}")
        print(f"  无法恢复，或文件已经是部署模式")
        return
    
    # 从备份恢复
    with open(backup_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ 已恢复为部署模式: {md_file}")
    print(f"  使用 Hexo 语法，可以正常部署了")


def show_usage():
    """显示使用说明"""
    print("""
本地预览模式切换工具

用法:
    python3 preview_mode.py <preview|deploy> <markdown文件>

示例:
    # 转换为预览模式（本地可见图片）
    python3 preview_mode.py preview source/_posts/使用-Cursor-编程的感想.md
    
    # 恢复为部署模式（Hexo 语法）
    python3 preview_mode.py deploy source/_posts/使用-Cursor-编程的感想.md

说明:
    - preview: 将 {% asset_img %} 转换为 ![](./文件夹/图片)
    - deploy: 从备份恢复 Hexo 语法
    - 首次运行 preview 会自动创建 .backup 备份文件
""")


def main():
    if len(sys.argv) != 3:
        show_usage()
        sys.exit(1)
    
    mode = sys.argv[1].lower()
    md_file = sys.argv[2]
    
    if not os.path.exists(md_file):
        print(f"✗ 文件不存在: {md_file}")
        sys.exit(1)
    
    if mode == 'preview':
        convert_to_preview_mode(md_file)
    elif mode == 'deploy':
        convert_to_deploy_mode(md_file)
    else:
        print(f"✗ 未知模式: {mode}")
        show_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
