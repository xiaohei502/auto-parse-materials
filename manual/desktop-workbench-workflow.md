# 本地桌面工作台使用流程

## 新总结

1. 把资料放入 `inputs/`。
2. 运行预处理：

   ```bash
   python auto-parse-materials/scripts/parse_material.py auto-parse-materials/inputs/example.srt --output auto-parse-materials/outputs/example-preprocessed.md
   ```

3. 按需求选择模板：
   - 普通笔记：`templates/bibigpt-style-note-prompt.md`
   - 详细页：`templates/detail-page-prompt.md`
   - 高光笔记：`templates/highlight-notes-prompt.md`
   - 原文细读：`templates/close-reading-prompt.md`
   - 公众号图文：`templates/wechat-article-prompt.md`
   - 自定义总结：`templates/custom-summary-prompt.md`

## 全局搜索

在 Codex 中搜索以下目录：

- `outputs/`
- `library/`
- `artifacts/`
- `collections/`

搜索关键词建议：

- 资料标题
- 人名、工具、概念
- `TODO`
- `高光`
- `爆款片段`
- `不确定点`

## 资源库整理

新资料默认先进入：

```text
library/summary-records/inbox/
```

整理后按状态复制或移动索引到：

- `all/`
- `highlighted/`
- `favorites/`
- `todos/`
- `flash-capsules/`

## 产出物整理

按用途保存到：

- `artifacts/highlight-notes/`
- `artifacts/ai-dialogues/`
- `artifacts/visual-summaries/`
- `artifacts/rewrites/`
- `artifacts/wechat-articles/`

## 视觉化总结的本地替代

v1 不让 AI 直接观看完整视频。可用手动方式替代：

1. 用户手动截取关键画面。
2. 把截图放在资料同名文件夹中。
3. 让 Codex 根据截图和字幕一起分析。
4. 在图文草稿里标注配图位置和截图说明。

没有截图时，Codex 只能给“建议截图点”，不能声称已经分析画面。
