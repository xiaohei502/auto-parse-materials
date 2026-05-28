# 本地化 BibiGPT 式解析流程

## 适用范围

这套流程用于半自动解析本地资料。它复刻的是“音视频/字幕资料 -> 摘要笔记”的使用方式，不复制任何网站品牌、界面或专有服务。

v1 支持两种入口：

- 直接粘贴资料给 Codex。
- 把本地文件放入 `inputs/` 后运行预处理脚本。

支持的文件类型：

- `.srt`
- `.vtt`
- `.txt`
- `.md`

## 方式一：直接粘贴资料

这是日常使用的推荐方式。

你可以直接对 Codex 说：

```text
使用 auto-parse-materials 解析下面资料，先问我想生成哪种产出。
```

然后粘贴字幕、转写稿、文章、网页正文、会议记录或课程材料。

Codex 会先识别资料类型，然后询问你要生成：

- 普通总结
- 详细页
- 高光笔记
- 原文细读
- 公众号图文
- 自定义总结

如果你已经知道目标，可以直接说：

```text
这是字幕，直接生成详细页 + 高光笔记。
```

这种方式不需要先把资料保存到 `inputs/`。如果你希望保留原文和转写稿，可以直接说：

```text
请保存原文记录和转写稿，再生成详细页。
```

这时 Codex 应把原始粘贴内容保存到 `records/originals/`，把转写稿或字幕稿保存到 `records/transcripts/`，再生成最终笔记。

## 方式二：本地文件流程

1. 手动获取材料。
   - 视频网站：优先下载官方字幕，或复制平台提供的文字稿。
   - 音频/视频文件：先用本机转写工具生成 `.srt`、`.vtt` 或 `.txt`。
   - 网页文章：手动复制正文到 `.txt` 或 `.md`。

2. 把文件放入：

   ```text
   auto-parse-materials/inputs/
   ```

3. 运行预处理脚本：

   ```bash
   python auto-parse-materials/scripts/parse_material.py auto-parse-materials/inputs/example.srt --output auto-parse-materials/outputs/example-preprocessed.md
   ```

4. 让 Codex 读取预处理结果，并套用：

   ```text
   auto-parse-materials/templates/bibigpt-style-note-prompt.md
   ```

5. 把最终笔记保存到：

   ```text
   auto-parse-materials/outputs/
   ```

## 存档规则

长期使用时，不要只保存最终总结。建议保留四层记录：

- `records/originals/`：原文记录，保存用户粘贴的原始文本、网页正文、会议记录或未清洗资料。
- `records/transcripts/`：转写稿、字幕稿、逐字稿和口播稿。
- `records/preprocessed/`：预处理后的清洗稿。
- `outputs/`：最终总结、详细页、高光笔记等。

推荐命名：

```text
YYYY-MM-DD-topic-original.md
YYYY-MM-DD-topic-transcript.md
YYYY-MM-DD-topic-preprocessed.md
YYYY-MM-DD-topic-note.md
```

## 手动转写建议

可接受的手动方式包括：

- 使用视频平台自带字幕下载或复制功能。
- 使用本地语音识别工具生成转写稿。
- 使用浏览器插件导出合法可访问的字幕。
- 手动复制网页正文、课程讲义或会议记录。

不建议在 v1 中自动化的内容：

- 自动抓取需要登录的视频或课程。
- 绕过验证码、付费墙、反爬或地区限制。
- 批量下载平台内容。
- 自动发送或上传生成结果到第三方服务。

## 结果命名

推荐命名方式：

```text
YYYY-MM-DD-topic-preprocessed.md
YYYY-MM-DD-topic-note.md
```

预处理文件用于保留清洗结果，最终笔记用于长期阅读和检索。
