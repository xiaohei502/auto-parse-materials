# Auto Parse Materials

一套本地化、半自动的资料解析工作台，用于把手动准备好的字幕、转写稿、网页复制文本和笔记整理成结构化 Markdown。

## 快速开始

中文导航入口：

- Markdown 版：`中文工作台.md`
- 可视化版：`中文可视化工作台.html`

最简单的方式是直接把材料粘贴给 Codex：

```text
使用 auto-parse-materials 解析下面资料，先问我想生成哪种产出。
```

然后粘贴字幕、转写稿、文章、网页正文、会议记录或课程材料。

如果资料很长、需要保存、需要保留原文记录或批量处理，再使用本地文件流程：

1. 把 `.srt`、`.vtt`、`.txt` 或 `.md` 放入 `inputs/`。
2. 运行预处理：

   ```bash
   python auto-parse-materials/scripts/parse_material.py auto-parse-materials/inputs/example.srt --output auto-parse-materials/outputs/example-preprocessed.md
   ```

3. 让 Codex 读取预处理结果，并选择模板：
   - 普通总结：`templates/bibigpt-style-note-prompt.md`
   - 详细页：`templates/detail-page-prompt.md`
   - 高光笔记：`templates/highlight-notes-prompt.md`
   - 原文细读：`templates/close-reading-prompt.md`
   - 公众号图文：`templates/wechat-article-prompt.md`
   - 课程学习笔记：`templates/个人常用-课程学习笔记提示词.md`
   - 自定义总结：`templates/custom-summary-prompt.md`

## 工作台结构

- `inputs/`：原始材料。
- `records/`：原文记录、转写稿、预处理稿。
- `outputs/`：预处理结果和最终笔记。
- `library/`：资源库、总结记录、分类索引。
- `artifacts/`：高光笔记、AI 对话、视觉化总结、改写文章、公众号图文。
- `collections/`：合集。
- `explore/`：订阅和热门资料清单。
- `templates/`：提示词模板。
- `manual/`：操作说明。
- `references/`：输出结构和工作台结构。

## 中文入口对照

- 入口：待处理资料 = `inputs/`
- 存档：原文记录 = `records/originals/`
- 存档：转写稿 = `records/transcripts/`
- 存档：预处理稿 = `records/preprocessed/`
- 出口：最终笔记 = `outputs/`
- 出口：二次产出 = `artifacts/`
- 知识库 = `library/`
- 合集 = `collections/`
- 探索 = `explore/`

## 边界

这不是对任何外部网站的复制，只是在本地模拟类似的资料处理能力。不自动抓取需要登录、验证码、付费权限或反爬绕过的内容。
