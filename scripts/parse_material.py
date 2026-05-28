#!/usr/bin/env python3
"""Preprocess local notes, SRT, VTT, and plain text into cleaner Markdown."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TIMESTAMP_RE = re.compile(
    r"(?P<start>\d{1,2}:\d{2}:\d{2}[,.]\d{1,3})\s*-->\s*"
    r"(?P<end>\d{1,2}:\d{2}:\d{2}[,.]\d{1,3})"
)
VTT_TIMESTAMP_RE = re.compile(
    r"(?P<start>\d{1,2}:\d{2}(?::\d{2})?\.\d{3})\s*-->\s*"
    r"(?P<end>\d{1,2}:\d{2}(?::\d{2})?\.\d{3})"
)
INLINE_TIMESTAMP_RE = re.compile(
    r"^\[?(?P<time>\d{1,2}:\d{2}(?::\d{2})?)\]?\s*[:：-]?\s*(?P<text>.+)$"
)
NOISE_LINE_RE = re.compile(
    r"^(subscribe|like and share|click here|广告|点赞|投币|收藏|关注|转发)$",
    re.IGNORECASE,
)
SENTENCE_END_RE = re.compile(r"[.!?。！？]$")


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "utf-16"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace")


def normalize_timestamp(value: str) -> str:
    return value.replace(",", ".")


def normalize_line(line: str) -> str:
    line = re.sub(r"<[^>]+>", "", line)
    line = line.replace("\ufeff", "")
    line = re.sub(r"\s+", " ", line)
    return line.strip()


def is_noise_line(line: str) -> bool:
    return not line or bool(NOISE_LINE_RE.match(line))


def parse_subtitles(text: str) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    current_start = ""
    current_end = ""
    current_lines: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.upper().startswith("WEBVTT") or line.isdigit():
            if current_lines:
                entries.append((current_start, current_end, " ".join(current_lines)))
                current_lines = []
            continue

        match = TIMESTAMP_RE.search(line) or VTT_TIMESTAMP_RE.search(line)
        if match:
            if current_lines:
                entries.append((current_start, current_end, " ".join(current_lines)))
                current_lines = []
            current_start = normalize_timestamp(match.group("start"))
            current_end = normalize_timestamp(match.group("end"))
            continue

        clean = normalize_line(line)
        if clean and not is_noise_line(clean):
            current_lines.append(clean)

    if current_lines:
        entries.append((current_start, current_end, " ".join(current_lines)))

    return entries


def looks_like_subtitle(text: str, suffix: str) -> bool:
    return suffix in {".srt", ".vtt"} or "-->" in text[:4000]


def parse_inline_timestamps(text: str) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    for raw_line in text.splitlines():
        line = normalize_line(raw_line)
        if is_noise_line(line):
            continue
        match = INLINE_TIMESTAMP_RE.match(line)
        if match:
            entries.append((match.group("time"), "", match.group("text").strip()))
        elif line:
            entries.append(("", "", line))
    return entries


def looks_like_inline_timestamped(text: str) -> bool:
    sample = [line.strip() for line in text.splitlines()[:80] if line.strip()]
    if not sample:
        return False
    matched = sum(1 for line in sample if INLINE_TIMESTAMP_RE.match(line))
    return matched >= max(3, len(sample) // 4)


def merge_entries(
    entries: list[tuple[str, str, str]],
    *,
    max_chars: int = 420,
) -> list[tuple[str, str, str]]:
    merged: list[tuple[str, str, str]] = []
    buffer_start = ""
    buffer_end = ""
    buffer_text: list[str] = []

    for start, end, text in entries:
        if not buffer_text:
            buffer_start = start
        buffer_end = end
        buffer_text.append(text)

        joined = " ".join(buffer_text)
        if len(joined) >= max_chars or SENTENCE_END_RE.search(joined):
            merged.append((buffer_start, buffer_end, joined))
            buffer_text = []

    if buffer_text:
        merged.append((buffer_start, buffer_end, " ".join(buffer_text)))

    return merged


def plain_text_to_markdown(text: str) -> str:
    lines = [normalize_line(line) for line in text.splitlines()]
    blocks: list[str] = []
    paragraph: list[str] = []

    for line in lines:
        if is_noise_line(line):
            if paragraph:
                blocks.append(" ".join(paragraph))
                paragraph = []
            continue
        paragraph.append(line)

    if paragraph:
        blocks.append(" ".join(paragraph))

    return "\n\n".join(blocks)


def source_type(path: Path, text: str) -> str:
    suffix = path.suffix.lower()
    if suffix in {".srt", ".vtt"} or looks_like_subtitle(text, suffix):
        return "subtitles"
    if looks_like_inline_timestamped(text):
        return "timestamped transcript"
    if suffix == ".md":
        return "markdown notes"
    return "plain text"


def front_matter(path: Path, kind: str) -> list[str]:
    return [
        "# Preprocessed Local Material",
        "",
        "## Source",
        f"- File: `{path.name}`",
        f"- Type: {kind}",
        "",
        "## Cleaned Content",
        "",
    ]


def timestamped_to_markdown(
    path: Path,
    text: str,
    entries: list[tuple[str, str, str]],
) -> str:
    lines = front_matter(path, source_type(path, text))
    for start, end, body in merge_entries(entries):
        label = f"{start} - {end}".strip(" -")
        if label:
            lines.append(f"- **{label}** {body}")
        else:
            lines.append(f"- {body}")
    return "\n".join(lines)


def text_to_markdown(path: Path, text: str) -> str:
    content = plain_text_to_markdown(text)
    return "\n".join(front_matter(path, source_type(path, text))) + content


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Preprocess local notes, SRT, VTT, and text into Markdown."
    )
    parser.add_argument("input_file", type=Path)
    parser.add_argument("--format", choices=["markdown"], default="markdown")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        help="Write Markdown to this file instead of stdout.",
    )
    args = parser.parse_args()

    if not args.input_file.exists():
        raise SystemExit(f"Input file not found: {args.input_file}")

    text = read_text(args.input_file)
    if looks_like_subtitle(text, args.input_file.suffix.lower()):
        output = timestamped_to_markdown(args.input_file, text, parse_subtitles(text))
    elif looks_like_inline_timestamped(text):
        output = timestamped_to_markdown(
            args.input_file, text, parse_inline_timestamps(text)
        )
    else:
        output = text_to_markdown(args.input_file, text)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.buffer.write(output.encode("utf-8"))
        if not output.endswith("\n"):
            sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
