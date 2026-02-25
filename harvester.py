import os
import re
import json
import httpx
import frontmatter  # 处理 Obsidian 的 YAML
from tqdm import tqdm
import asyncio
from datetime import datetime

# --- [小酷 CTO 核定配置] ---
CONFIG = {
    "API_URL": "http://101.43.29.236:8189/v1/chat/completions",
    "MODEL_NAME": "internlm3-8b-instruct",
    "VAULT_PATH": "/Users/kenny/Documents/My_Obsidian_Vault",  # 【请修改：你的本地 Obsidian 库路径】
    "SESSION_ID": "kenny_harvest_session_001",
    # 归档根目录（相对 VAULT_PATH）；小黑判决后笔记落盘位置
    "ARCHIVE_ROOT": "归档",
    # 归档子文件夹按何划分：suggested_type | agent（primary_view）
    "ARCHIVE_BY": "suggested_type",
    # 过去制作的模板目录（相对 VAULT_PATH），如 000_Cabinet_System/Templates/old templates
    "TEMPLATES_OLD": "000_Cabinet_System/Templates/old templates",
}

# --- [审计员小黑的 Prompt] ---
SYSTEM_PROMPT = """你是由小酷配置的审计员小黑。你的任务是分析笔记内容，并输出 JSON 格式。
要求包含：
1. category: 笔记类别
2. tags: 建议标签 (list)
3. summary: 50字简述
4. action: 处理建议 (keep/archive/delete)
"""


# --- [小黑 JSON 表头与归档] ---
# 小黑分析范围：普通笔记 + 周记（content_type / suggested_type 可为「周记」），
# 周记会落入归档子目录「周记」并带 tag 周记，便于 Obsidian 筛选。
# 表头字段与 Dataview 兼容，参见项目内 DATAVIEW_TEMPLATES.md 的查询示例。

CONTENT_TYPE_ZHOUJI = ("周记", "weekly_journal", "周记类")  # 识别为周记的 content_type / suggested_type 取值


def _safe_filename(s, max_len=80):
    """去掉非法字符，截断长度，避免重名用时间戳后缀在外部加。"""
    s = re.sub(r'[<>:"/\\|?*\n\r]', "_", str(s).strip())
    return s[:max_len] if s else "untitled"


def _build_frontmatter_from_xiaohei(xiaohei):
    """从小黑 JSON 生成 Obsidian 表头（YAML frontmatter）。适配小黑最新 schema。"""
    arch = xiaohei.get("archive_recommendation") or {}
    primary = xiaohei.get("primary_view_recommendation") or {}
    risk_list = xiaohei.get("risk_flags") or []
    temporal = xiaohei.get("temporal_scope") or {}
    structure = xiaohei.get("structure_signals") or {}

    tags = []
    ct = (xiaohei.get("content_type") or "").strip()
    st_arch = (arch.get("suggested_type") or "").strip()
    if ct:
        tags.append(ct)
    if any(z in ct or z in st_arch for z in CONTENT_TYPE_ZHOUJI) and "周记" not in tags:
        tags.append("周记")
    if primary.get("agent"):
        tags.append(primary["agent"])

    risk_summary = "none"
    if risk_list:
        rt = risk_list[0].get("risk_type") or ""
        if rt and rt.strip():
            risk_summary = rt
        elif risk_list[0].get("severity") and risk_list[0]["severity"] != "low":
            risk_summary = risk_list[0].get("severity", "unknown")

    fm = {
        "agent": xiaohei.get("agent", "小黑"),
        "analysis_mode": xiaohei.get("analysis_mode") or "",
        "source_type": xiaohei.get("source_type") or "",
        "content_type": xiaohei.get("content_type") or "",
        "core_topic": xiaohei.get("core_topic") or "",
        "confidence_level": xiaohei.get("confidence_level"),
        "confidence_explanation": xiaohei.get("confidence_explanation") or "",
        "structure_score": xiaohei.get("structure_score"),
        "information_density": xiaohei.get("information_density"),
        "suggested_type": arch.get("suggested_type") or "",
        "primary_agent": primary.get("agent") or "",
        "archive_note": arch.get("note") or "",
        "risk": risk_summary,
        "tags": tags if tags else ["归档"],
        "date": datetime.now().strftime("%Y-%m-%d"),
        "source": xiaohei.get("source", "") or "",
    }
    # 时间范围（有任一非空再写）
    if any(temporal.get(k) for k in ("start", "end", "cycle")):
        fm["temporal_scope"] = {
            "start": temporal.get("start") or "",
            "end": temporal.get("end") or "",
            "cycle": temporal.get("cycle") or "",
        }
    # 结构信号（便于筛选待办/复盘/时间跨度）
    if structure:
        fm["structure_signals"] = {
            "has_todo": bool(structure.get("has_todo")),
            "has_done": bool(structure.get("has_done")),
            "has_reflection": bool(structure.get("has_reflection")),
            "has_time_range": bool(structure.get("has_time_range")),
        }
    # 周记标识（小黑分析范围含笔记+周记，便于 Obsidian 筛选）
    is_zhouji = any(z in ct or z in st_arch for z in CONTENT_TYPE_ZHOUJI)
    if is_zhouji:
        fm["is_weekly_journal"] = True
    return fm


def _build_body_from_xiaohei(xiaohei, source_content=""):
    """从小黑 JSON + 可选原文生成正文。"""
    lines = []

    if xiaohei.get("extracted_facts"):
        lines.append("## 提取事实\n")
        for item in xiaohei["extracted_facts"]:
            lines.append(f"- {item}")
        lines.append("")

    if xiaohei.get("key_points"):
        lines.append("## 要点\n")
        for item in xiaohei["key_points"]:
            lines.append(f"- {item}")
        lines.append("")

    inf_list = [i for i in (xiaohei.get("inference") or []) if (i.get("content") or "").strip()]
    if inf_list:
        lines.append("## 推断\n")
        for inf in inf_list:
            c = inf.get("content", "").strip()
            conf = inf.get("confidence")
            lines.append(f"- {c}" + (f" (置信度: {conf})" if conf is not None and conf != "" else ""))
        lines.append("")

    if xiaohei.get("persona_signals"):
        lines.append("## 人格/信号\n")
        for ps in xiaohei["persona_signals"]:
            st = ps.get("signal_type", "")
            desc = ps.get("description", "")
            strength = ps.get("strength", "")
            lines.append(f"- **{st}**: {desc}" + (f" (强度: {strength})" if strength != "" else ""))
        lines.append("")

    if source_content.strip():
        lines.append("---\n## 原文\n\n")
        lines.append(source_content.strip()[:50000])  # 单篇限制约 5 万字

    return "\n".join(lines).strip()


def _get_archive_subdir(xiaohei):
    """按 CONFIG['ARCHIVE_BY'] 决定归档子文件夹名。笔记、周记等均由此路由。"""
    by = CONFIG.get("ARCHIVE_BY", "suggested_type")
    if by == "agent":
        primary = xiaohei.get("primary_view_recommendation") or {}
        name = primary.get("agent", "未分配")
    else:
        arch = xiaohei.get("archive_recommendation") or {}
        name = (arch.get("suggested_type") or "").strip()
        ct = (xiaohei.get("content_type") or "").strip()
        # 小黑判定为周记但 suggested_type 未填时，统一进「周记」子目录
        if not name and any(z in ct for z in CONTENT_TYPE_ZHOUJI):
            name = "周记"
        if not name:
            name = "other"
    return _safe_filename(name).strip("._ ") or "other"


def write_harvested_note(xiaohei, filename_base=None, source_content="", vault_path=None):
    """
    把小黑 JSON 写成一篇带表头的 Markdown，放入归档文件夹。
    xiaohei: 小黑输出的完整 JSON 字典
    filename_base: 文件名（不含 .md），若为空则用 core_topic + 日期
    source_content: 可选原文，会出现在正文「原文」段
    vault_path: 覆盖 CONFIG['VAULT_PATH']
    返回: 写入的绝对路径
    """
    vault = vault_path or CONFIG["VAULT_PATH"]
    root = os.path.join(vault, CONFIG["ARCHIVE_ROOT"])
    sub = _get_archive_subdir(xiaohei)
    dir_path = os.path.join(root, sub)
    os.makedirs(dir_path, exist_ok=True)

    if not filename_base:
        topic = _safe_filename(xiaohei.get("core_topic", "untitled"), max_len=50)
        filename_base = f"{topic}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    filename_base = _safe_filename(filename_base, max_len=120)
    md_path = os.path.join(dir_path, f"{filename_base}.md")

    fm = _build_frontmatter_from_xiaohei(xiaohei)
    body = _build_body_from_xiaohei(xiaohei, source_content)
    post = frontmatter.Post(body, **fm)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post))

    return os.path.abspath(md_path)


def harvest_from_json_file(json_path, source_content="", filename_base=None, vault_path=None):
    """
    从「小黑 JSON 文件」收割：加表头、写入归档文件夹。
    json_path: 小黑输出的 .json 文件路径
    source_content: 可选原文
    filename_base: 可选，否则用 core_topic + 时间
    返回: 写入的 .md 绝对路径
    """
    with open(json_path, "r", encoding="utf-8") as f:
        xiaohei = json.load(f)
    return write_harvested_note(xiaohei, filename_base=filename_base, source_content=source_content, vault_path=vault_path)


def harvest_batch(manifest, vault_path=None):
    """
    批量收割，适合 4GB 文件逐步处理。
    manifest: 列表，每项为 dict：
      - "json_path": 小黑 JSON 文件路径，或
      - "xiaohei": 直接传小黑 JSON 字典
      - "source_path": 可选，原文 .md/.txt 路径（会读入作为 source_content）
      - "source_content": 可选，直接传原文字符串
      - "filename_base": 可选
    返回: [(item, written_path), ...]，失败项 written_path 为 None 并记错误信息。
    """
    results = []
    for item in tqdm(manifest, desc="收割进度"):
        xiaohei = None
        source_content = ""
        filename_base = item.get("filename_base")

        if item.get("xiaohei"):
            xiaohei = item["xiaohei"]
        elif item.get("json_path"):
            try:
                with open(item["json_path"], "r", encoding="utf-8") as f:
                    xiaohei = json.load(f)
            except Exception as e:
                results.append((item, None))
                print(f"跳过 {item.get('json_path')}: {e}")
                continue
        else:
            results.append((item, None))
            print("跳过：缺少 json_path 或 xiaohei")
            continue

        if item.get("source_content"):
            source_content = item["source_content"]
        elif item.get("source_path"):
            try:
                with open(item["source_path"], "r", encoding="utf-8") as f:
                    source_content = f.read()
            except Exception as e:
                print(f"原文读取失败 {item.get('source_path')}: {e}")

        try:
            path = write_harvested_note(xiaohei, filename_base=filename_base, source_content=source_content, vault_path=vault_path)
            results.append((item, path))
        except Exception as e:
            results.append((item, None))
            print(f"写入失败: {e}")
    return results


async def audit_note(content):
    """直接撞击 3090 的 8189 接口"""
    payload = {
        "model": CONFIG["MODEL_NAME"],
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content[:2000]} # 截取前2000字，防止长文本爆显存
        ],
        "temperature": 0.3,
        "session_id": CONFIG["SESSION_ID"],
        "repetition_penalty": 1.005
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(CONFIG["API_URL"], json=payload, timeout=30.0)
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            return f"Error: {response.status_code}"
        except Exception as e:
            return f"Failed: {str(e)}"

async def main():
    # 扫描所有 Markdown 文件
    notes = [os.path.join(dp, f) for dp, dn, filenames in os.walk(CONFIG["VAULT_PATH"]) 
             for f in filenames if f.endswith('.md')]
    
    print(f"🚀 小酷报告：发现 {len(notes)} 份遗产文件，准备开始收割...")

    # 先拿 5 个文件做压力测试，别一下全上
    for note_path in tqdm(notes[:5]):
        with open(note_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            # 调用 3090 进行审计
            audit_result = await audit_note(post.content)
            
            # 在这里我们暂时只打印结果，不写回文件，确保安全
            print(f"\n文件: {os.path.basename(note_path)}")
            print(f"审计报告: {audit_result}")
            print("-" * 30)

def main_harvest():
    """命令行：小黑 JSON 收割（表头 + 归档文件夹）。"""
    import argparse
    p = argparse.ArgumentParser(description="小黑 JSON → 带表头 Markdown 写入归档")
    p.add_argument("json", nargs="?", help="小黑输出的 JSON 文件路径")
    p.add_argument("--manifest", "-m", help="批量清单 JSON：每项含 json_path / xiaohei、可选 source_path / source_content / filename_base")
    p.add_argument("--source", "-s", help="原文文件路径（与单 json 同用）")
    p.add_argument("--vault", "-v", default=None, help="覆盖 Obsidian 库路径")
    p.add_argument("--dry-run", action="store_true", help="只打印将要写入的路径，不写文件")
    args = p.parse_args()

    vault = args.vault or CONFIG["VAULT_PATH"]
    if args.manifest:
        with open(args.manifest, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        if args.dry_run:
            for i, item in enumerate(manifest):
                jp = item.get("json_path") or "(xiaohei inline)"
                x = item.get("xiaohei")
                if not x and jp != "(xiaohei inline)" and os.path.isfile(jp):
                    try:
                        with open(jp, "r", encoding="utf-8") as f:
                            x = json.load(f)
                    except Exception:
                        x = {}
                sub = _get_archive_subdir(x) if x else "?"
                print(f"  [{i+1}] {jp} -> {os.path.join(vault, CONFIG['ARCHIVE_ROOT'], sub)}/")
            return
        results = harvest_batch(manifest, vault_path=vault)
        for item, path in results:
            print(path or f"失败: {item}")
        return

    if not args.json:
        # 无参数时沿用原有「扫库 + 3090 审计」流程
        asyncio.run(main())
        return

    if args.dry_run:
        with open(args.json, "r", encoding="utf-8") as f:
            x = json.load(f)
        sub = _get_archive_subdir(x)
        print(f"将写入: {os.path.join(vault, CONFIG['ARCHIVE_ROOT'], sub)}/")
        return

    src = ""
    if args.source and os.path.isfile(args.source):
        with open(args.source, "r", encoding="utf-8") as f:
            src = f.read()
    path = harvest_from_json_file(args.json, source_content=src, vault_path=vault)
    print(f"已写入: {path}")


if __name__ == "__main__":
    main_harvest()