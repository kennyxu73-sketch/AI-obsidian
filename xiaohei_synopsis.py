"""
小黑 Step 1：本地 3090 初步筛选 → 输出「文件缩影」
> 只输出：文字数量、约200字概要、文件类型（+ 可选 source_path）
> 深度 JSON 由云端 Step 2 完成
"""
import os
import re
import json
import asyncio
import httpx

# --- [与 harvester 共用 3090 配置] ---
CONFIG = {
    "API_URL": "http://101.43.29.236:8189/v1/chat/completions",
    "MODEL_NAME": "internlm3-8b-instruct",
    "SESSION_ID": "kenny_synopsis_001",
    "MAX_CONTENT_LEN": 8000,  # 送 3090 的原文最大长度，避免爆显存
}

SYNOPSIS_PROMPT = """你只做一件事：对下面这段内容做「初步筛选」，输出一个 JSON，且只输出这一个 JSON，不要任何其他文字。

JSON 必须且仅包含以下 4 个字段（字段名必须是英文）：
1. word_count: 整数字，表示这段内容的「文字数量」大致多少（中英文都算）。
2. summary_200: 字符串，用大约 200 字以内概括这段内容在讲什么、有什么关键信息。
3. file_type: 字符串，且只能是以下之一：note, weekly_journal, web_article, video_note, mindmap, canvas, other。
4. source_path: 字符串，若没有来源路径就填空字符串 ""。

要求：
- 只输出合法 JSON，不要 markdown 代码块包裹，不要解释。
- file_type 根据内容判断：周记/周总结用 weekly_journal；网页/文章用 web_article；思维导图结构用 mindmap；白板/画布用 canvas；视频相关用 video_note；普通笔记用 note；无法判断用 other。
"""


def _extract_json_from_response(text: str) -> dict:
    """从模型返回中抠出第一个合法 JSON 对象。"""
    text = text.strip()
    # 去掉可能的 markdown 代码块
    for marker in ("```json", "```"):
        if marker in text:
            parts = text.split(marker)
            for p in parts:
                p = p.strip()
                if p.startswith("{"):
                    try:
                        return json.loads(p)
                    except json.JSONDecodeError:
                        continue
    # 找第一个 { ... }
    start = text.find("{")
    if start == -1:
        raise ValueError("响应中未找到 JSON 对象")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[start : i + 1])
                except json.JSONDecodeError:
                    break
    raise ValueError("无法解析出合法 JSON")


async def build_synopsis(
    content: str,
    source_path: str = "",
    api_url: str = None,
    model: str = None,
) -> dict:
    """
    用本地 3090 对 content 做初步筛选，返回「文件缩影」字典。

    Args:
        content: 原始文本（过长会自动截断到 CONFIG.MAX_CONTENT_LEN）
        source_path: 可选，来源路径或 ID，会传入 prompt 供模型填入 source_path
        api_url: 可选，覆盖 3090 API 地址
        model: 可选，覆盖模型名

    Returns:
        缩影 dict，必含键：word_count, summary_200, file_type, source_path
    """
    url = api_url or CONFIG["API_URL"]
    model_name = model or CONFIG["MODEL_NAME"]
    max_len = CONFIG.get("MAX_CONTENT_LEN", 8000)
    text = (content or "")[:max_len]

    user_msg = f"来源路径（若无则忽略）：{source_path}\n\n待分析内容：\n{text}"

    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": SYNOPSIS_PROMPT},
            {"role": "user", "content": user_msg},
        ],
        "temperature": 0.2,
        "session_id": CONFIG.get("SESSION_ID", "kenny_synopsis_001"),
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=payload, timeout=60.0)
        if resp.status_code != 200:
            raise RuntimeError(f"3090 请求失败: {resp.status_code}")

        data = resp.json()
        raw = (
            data.get("choices", [{}])[0].get("message", {}).get("content", "")
        )

    synopsis = _extract_json_from_response(raw)

    # 强制四键、类型
    word_count = synopsis.get("word_count")
    if word_count is None or not isinstance(word_count, (int, float)):
        word_count = len(content or "")
    synopsis["word_count"] = int(word_count)

    synopsis["summary_200"] = (synopsis.get("summary_200") or "").strip() or "(无概要)"
    synopsis["file_type"] = (synopsis.get("file_type") or "other").strip()
    if source_path and not synopsis.get("source_path"):
        synopsis["source_path"] = source_path
    else:
        synopsis["source_path"] = (synopsis.get("source_path") or "").strip()

    allowed_types = ("note", "weekly_journal", "web_article", "video_note", "mindmap", "canvas", "other")
    if synopsis["file_type"] not in allowed_types:
        synopsis["file_type"] = "other"

    return synopsis


def build_synopsis_sync(content: str, source_path: str = "", **kwargs) -> dict:
    """同步封装，便于非 async 环境调用。"""
    return asyncio.run(build_synopsis(content, source_path=source_path, **kwargs))


# --- 命令行：单文件或 stdin ---
async def _main():
    import argparse
    p = argparse.ArgumentParser(description="小黑 Step1：本地 3090 生成文件缩影")
    p.add_argument("file", nargs="?", help="输入文件路径（不填则从 stdin 读）")
    p.add_argument("--out", "-o", help="缩影 JSON 写入路径（不填则只打印）")
    args = p.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
        source_path = args.file
    else:
        content = __import__("sys").stdin.read()
        source_path = ""

    synopsis = await build_synopsis(content, source_path=source_path)
    out_json = json.dumps(synopsis, ensure_ascii=False, indent=2)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out_json)
        print(f"已写入: {args.out}")
    else:
        print(out_json)


if __name__ == "__main__":
    asyncio.run(_main())
