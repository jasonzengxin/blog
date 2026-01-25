# Blog of Zeng Xin

基于 [Hexo](https://hexo.io/) 框架和 [Archer](https://github.com/fi3ework/hexo-theme-archer) 主题的个人博客。

## 🚀 快速开始

### 安装依赖

```bash
npm install
```

### 本地预览

```bash
npm run server
```

然后访问 http://localhost:4000 查看博客。

---

## ✍️ 写文章

### 创建新文章

```bash
npx hexo new "文章标题"
```

这会在 `source/_posts/` 目录下创建：
- `文章标题.md` - 文章内容
- `文章标题/` - 文章资源文件夹（用于存放图片等）

### 文章格式

文章使用 Markdown 格式，开头需要包含 Front-matter：

```yaml
---
title: 文章标题
date: 2024-01-01 12:00:00
tags:
  - 标签1
  - 标签2
categories:
  - 分类名
---

正文内容从这里开始...
```

### 添加图片

由于开启了 `post_asset_folder`，图片放在与文章同名的文件夹中：

```
source/_posts/
├── My-Article.md
└── My-Article/
    └── image.jpg
```

在文章中引用图片：

```markdown
![图片描述](image.jpg)
```

---

## 📝 修改文章

直接编辑 `source/_posts/` 目录下对应的 `.md` 文件即可。

### 查看现有文章

```bash
ls source/_posts/
```

当前文章列表：
- `Clean-Code.md` - Clean Code 读书笔记
- `NQueens-Problem.md` - N皇后问题

---

## 🚢 发布流程

### 一键发布（推荐）

```bash
npm run clean && npm run build && npm run deploy
```

### 分步操作

```bash
# 1. 清理旧文件
npm run clean

# 2. 生成静态文件
npm run build

# 3. 部署到 GitHub Pages
npm run deploy
```

部署目标：https://jasonzengxin.github.io

---

## 🛠 常用命令

| 命令 | 说明 |
|------|------|
| `npm run server` | 启动本地服务器预览 |
| `npm run build` | 生成静态文件到 `public/` |
| `npm run clean` | 清理缓存和生成的文件 |
| `npm run deploy` | 部署到 GitHub Pages |
| `npx hexo new "标题"` | 创建新文章 |
| `npx hexo new page "页面名"` | 创建新页面 |
| `npx hexo new draft "标题"` | 创建草稿 |
| `npx hexo publish "草稿标题"` | 发布草稿 |

---

## 📁 项目结构

```
blog/
├── _config.yml          # Hexo 主配置
├── package.json         # 项目依赖
├── source/
│   ├── _posts/          # 📝 文章目录
│   ├── about/           # 关于页面
│   └── CNAME            # 自定义域名
├── themes/
│   └── archer/          # 主题目录
├── public/              # 生成的静态文件
└── scaffolds/           # 模板
    ├── post.md          # 文章模板
    ├── page.md          # 页面模板
    └── draft.md         # 草稿模板
```

---

## 💡 工作流程速查

### 写新文章并发布

```bash
# 1. 创建文章
npx hexo new "我的新文章"

# 2. 编辑文章
# 打开 source/_posts/我的新文章.md 进行编辑

# 3. 本地预览
npm run server

# 4. 发布
npm run clean && npm run build && npm run deploy
```

### 修改已有文章并发布

```bash
# 1. 编辑 source/_posts/ 下的对应文章

# 2. 本地预览确认修改
npm run server

# 3. 发布
npm run clean && npm run build && npm run deploy
```

---

## 🔗 相关链接

- [Hexo 文档](https://hexo.io/docs/)
- [Archer 主题](https://github.com/fi3ework/hexo-theme-archer)
- [Markdown 语法指南](https://www.markdownguide.org/)

