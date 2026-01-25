# 本地预览模式说明

## 问题

Hexo 使用 `{% asset_img %}` 标签来引用图片，这种语法在普通的 Markdown 预览器（VS Code、Typora、Cursor 等）中无法正常显示图片。

## 解决方案

我们提供了一个预览模式切换工具，可以在 Hexo 语法和标准 Markdown 语法之间自动转换。

## 快速使用

### 方式1: 使用快捷脚本（推荐）

```bash
# 在博客根目录执行

# 1. 切换到预览模式（本地可见图片）
./preview.sh

# 2. 在 IDE 中预览 Markdown 文件，现在可以看到图片了！

# 3. 完成后恢复并部署
./deploy.sh
```

### 方式2: 手动使用工具

```bash
cd tools

# 转换为预览模式
python3 preview_mode.py preview ../source/_posts/使用-Cursor-编程的感想.md

# 恢复为部署模式
python3 preview_mode.py deploy ../source/_posts/使用-Cursor-编程的感想.md
```

## 工作原理

### 预览模式
将 Hexo 语法：
```
{% asset_img vibe-programming-flow.png "Vibe Programming 流程图" %}
```

转换为标准 Markdown 语法：
```markdown
![Vibe Programming 流程图](./使用-Cursor-编程的感想/vibe-programming-flow.png)
```

### 部署模式
从自动创建的 `.backup` 文件恢复原始的 Hexo 语法。

## 安全机制

- ✅ 首次运行 preview 时自动创建 `.backup` 备份文件
- ✅ deploy 时从备份恢复，确保不丢失 Hexo 语法
- ✅ 备份文件只创建一次，避免覆盖

## 注意事项

1. **预览模式下不要部署**
   - 预览模式使用的是标准 Markdown 语法
   - 需要先运行 `./deploy.sh` 或 `preview_mode.py deploy` 恢复

2. **备份文件**
   - `.backup` 文件会被 git 忽略（已加入 .gitignore）
   - 不要手动删除 `.backup` 文件
   - 如果不小心删除，重新从 git 获取原文件即可

3. **多个文章**
   - 当前脚本只处理 "使用-Cursor-编程的感想.md"
   - 如需处理其他文章，修改快捷脚本或直接使用工具命令

## 文件列表

```
blog/
├── preview.sh              # 快捷脚本：切换到预览模式
├── deploy.sh               # 快捷脚本：恢复并部署
└── tools/
    ├── preview_mode.py     # 预览模式切换工具
    └── PREVIEW_MODE_README.md  # 本文档
```

## 常见问题

### Q: 预览模式下部署会怎样？
A: Hexo 生成时会找不到图片路径，导致图片显示不正常。记得先运行 `./deploy.sh` 恢复。

### Q: 忘记运行 deploy 就提交了怎么办？
A: 从 git 恢复文件，或者手动将标准 Markdown 语法改回 Hexo 语法。

### Q: 可以同时预览多个文章吗？
A: 可以。修改脚本添加更多文章路径，或者对每个文章单独运行工具。

### Q: 我的 IDE 已经支持 Hexo 语法了
A: 那太好了！就不需要这个工具了。目前大多数 Markdown 预览器还不支持 Hexo 的自定义标签。

## 推荐工作流

```bash
# 1. 写作时：切换到预览模式
./preview.sh

# 2. 在 IDE 中编辑和预览
# （可以看到图片了）

# 3. 完成后：一键恢复并部署
./deploy.sh

# 4. 提交代码
git add .
git commit -m "更新文章"
git push
```

这样就可以愉快地在本地预览图片，又不影响 Hexo 的正常部署了！
