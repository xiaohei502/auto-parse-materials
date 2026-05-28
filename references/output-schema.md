# 输出结构

当用户要求可复用、可导入其它工具、或需要稳定格式的解析结果时，使用这里的结构。

## Markdown 格式

```markdown
# 资料解析笔记：<标题>

## 资料信息与解析假设
- 类型：
- 来源：
- 语言：
- 范围：
- 不确定点：

## 摘要

## 章节大纲

## 时间线

## 关键观点

## 术语、人物、工具与日期

## 可继续追问的问题

## 行动项或学习任务

## 关键原文摘录
```

## JSON 格式

```json
{
  "type": "notes | subtitles | transcript | article | meeting | course | mixed",
  "source": "string",
  "language": "string",
  "assumptions": ["string"],
  "overview": "string",
  "chapters": [
    {
      "title": "string",
      "time_range": "string",
      "points": ["string"]
    }
  ],
  "timeline": [
    {
      "time": "string",
      "event": "string"
    }
  ],
  "key_points": ["string"],
  "entities": [
    {
      "name": "string",
      "kind": "person | organization | concept | date | tool | place | other",
      "note": "string"
    }
  ],
  "questions": ["string"],
  "action_items": [
    {
      "task": "string",
      "reason": "string",
      "priority": "low | medium | high"
    }
  ],
  "quotes": [
    {
      "time": "string",
      "text": "string"
    }
  ]
}
```

缺失内容保留为空数组或空字符串，不要为了填满字段而编造信息。

## 详细页 JSON 格式

```json
{
  "title": "string",
  "source": "string",
  "language": "string",
  "input_file": "string",
  "assumptions": ["string"],
  "full_summary": "string",
  "close_reading": {
    "optimized_transcript": "string",
    "polished_text": "string",
    "rewritten_article": "string"
  },
  "highlights": {
    "default": [
      {
        "time": "string",
        "text": "string",
        "reason": "string"
      }
    ],
    "emotional_peaks": [
      {
        "time": "string",
        "text": "string",
        "emotion_type": "string",
        "reason": "string"
      }
    ],
    "viral_clips": [
      {
        "time_range": "string",
        "hook": "string",
        "summary": "string",
        "scores": {
          "hook_strength": 0,
          "emotional_tension": 0,
          "twist_or_quote": 0,
          "reuse_potential": 0,
          "total": 0
        },
        "limits": "string"
      }
    ]
  },
  "subtitle_script": [
    {
      "time": "string",
      "text": "string"
    }
  ],
  "visual_summary": {
    "wechat_draft": "string",
    "screenshot_suggestions": [
      {
        "time": "string",
        "purpose": "string",
        "visual_note": "string"
      }
    ],
    "visual_limits": "string",
    "short_clip_ideas": [
      {
        "time_range": "string",
        "title": "string",
        "hook": "string",
        "platform": "string"
      }
    ]
  },
  "custom_summary": "string"
}
```
