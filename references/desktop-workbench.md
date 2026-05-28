# 本地桌面工作台结构

这份结构用于在 Codex 本地工作区中模拟桌面端资料工作台。它只定义本地文件组织与生成物规范，不实现网站 UI。

## 快捷入口

- 新总结：在 `inputs/` 放入资料后，运行预处理脚本并生成详细页笔记。
- 全局搜索：使用系统文件搜索或 Codex 搜索 `library/`、`outputs/`、`artifacts/`。

## 知：资源库

总结记录基础分类：

- `library/summary-records/all/`：所有总结索引。
- `library/summary-records/highlighted/`：已高亮内容。
- `library/summary-records/inbox/`：待整理资料。
- `library/summary-records/favorites/`：已收藏资料。
- `library/summary-records/todos/`：待办事项。
- `library/summary-records/flash-capsules/`：闪念胶囊。
- `library/smart-categories/`：按主题、人物、项目、课程自动或手动分类。

## 行：产出物

- `artifacts/my-prompts/`：个人提示词。
- `artifacts/official-prompts/`：稳定通用提示词。
- `artifacts/prompt-market/`：可复用提示词清单。
- `artifacts/highlight-notes/`：高光笔记。
- `artifacts/ai-dialogues/`：基于材料的问答记录。
- `artifacts/image-generation/`：图片生成提示词与结果记录。
- `artifacts/visual-summaries/`：视觉化总结、截图分析、图文草稿。
- `artifacts/rewrites/`：AI 改写文章。
- `artifacts/wechat-articles/`：公众号图文草稿。

## 探索

- `explore/subscriptions/`：订阅源、作者、频道、课程清单。
- `explore/hot/`：热门资料和待解析链接清单。

## 合集

- `collections/`：按课程、主题、项目或资料系列建立合集索引。

## 详细页视图

每份重要资料建议生成一个详细页 Markdown，包含：

- 全文总结
- 原文细读
- 口播逐字稿
- AI 润色
- AI 改写
- 高光笔记
- 字幕脚本
- 视觉化总结
- 自定义总结
