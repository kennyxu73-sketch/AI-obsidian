"""
Harvester V2 调度器 · 两阶段协议 (2P-Protocol) 自动化文档处理流

架构说明见 ARCHITECTURE_HARVESTER_V2.md

- Watchdog: 监控 000_Inbox 下 .md 文件
- Step 1: 本地哨兵 (xiaohei_synopsis + 增强：privacy_level / task_count / core_entities)
- Step 2: 智能分流（高智商→Dify，极简→本地 Frontmatter）
- 落盘: 按 core_entities 路径 + Obsidian YAML Frontmatter
- 3090 宕机时自动降级为纯文本移动，不阻塞
- 日志: logs/cabinet.log
"""
from __future__ import annotations

import os
import re
import json
import asyncio
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List, Tuple

import httpx
import frontmatter

# 本地哨兵
from xiaohei_synopsis import build_synopsis

# --- [小酷 CTO 核定配置] ---
CONFIG = {
    "INBOX_PATH": os.path.expanduser("~/Documents/Obsidian/000_Inbox"),
    "VAULT_PATH": os.path.expanduser("~/Documents/Obsidian"),
    "ARCHIVE_ROOT": "归档",
    "FALLBACK_DIR": "_fallback",  # 3090 不可用时移动到此（相对 INBOX 或 VAULT/归档）
    "LOG_PATH": "logs/cabinet.log",
    # Dify：高智商分支调用
    "DIFY_API_URL": os.environ.get("DIFY_API_URL", ""),
    "DIFY_API_KEY": os.environ.get("DIFY_API_KEY", ""),
    "DIFY_TIMEOUT": 120,
    # 敏感词：命中则 privacy_level = High
    "SENSITIVE_KEYWORDS": ["身份证号", "手机号", "密码", "银行卡", "敏感"],
    # 关键词 → 存储子目录（core_entities）
    "CORE_ENTITY_KEYWORDS": {
        "小康": ["民政", "百联", "慧享福", "养老", "慰康"],
        "小镜": ["回忆录", "叙事", "访谈", "憶镜", "数字永生"],
    },
    # 高智商分支触发词
    "HIGH_INTEL_KEYWORDS": ["战略", "协议"],
}

# --- 日志 ---
def _setup_logging() -> logging.Logger:
    log_path = CONFIG.get("LOG_PATH", "logs/cabinet.log")
    log_file = Path(log_path)
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("cabinet.v2")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler(log_path, encoding="utf-8")
        fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        logger.addHandler(fh)
    return logger

LOG = _setup_logging()


# --- 增强型缩影 ---
def _count_tasks(content: str) -> int:
    """统计未勾选待办 [ ] 数量（Markdown 格式 - [ ] 或 * [ ]）。"""
    if not content:
        return 0
    return len(re.findall(r"[-*]?\s*\[\s\]", content))


def _detect_privacy_level(content: str) -> str:
    """根据敏感词判定 privacy_level。"""
    if not content:
        return "Normal"
    keywords = CONFIG.get("SENSITIVE_KEYWORDS", [])
    for kw in keywords:
        if kw in content:
            return "High"
    return "Normal"


def _detect_core_entities(content: str) -> List[str]:
    """根据关键词匹配 core_entities（Agent 列表）。"""
    if not content:
        return []
    mapping = CONFIG.get("CORE_ENTITY_KEYWORDS", {})
    found = []
    for agent, kws in mapping.items():
        for kw in kws:
            if kw in content:
                found.append(agent)
                break
    return list(dict.fromkeys(found))  # 去序保序


def enhance_synopsis(content: str, base_synopsis: Dict[str, Any]) -> Dict[str, Any]:
    """在基础缩影上增加 privacy_level、task_count、core_entities。"""
    out = dict(base_synopsis)
    out["privacy_level"] = _detect_privacy_level(content)
    out["task_count"] = _count_tasks(content)
    out["core_entities"] = _detect_core_entities(content)
    return out


# --- 智能分流 ---
def _should_high_intel(content: str, synopsis: Dict[str, Any]) -> bool:
    """是否走高智商分支：weekly_journal 或 命中「战略/协议」。"""
    if (synopsis.get("file_type") or "").strip() == "weekly_journal":
        return True
    for kw in CONFIG.get("HIGH_INTEL_KEYWORDS", []):
        if kw in (content or ""):
            return True
    return False


def _should_minimal_local(synopsis: Dict[str, Any]) -> bool:
    """是否走极简模式：word_count < 300 且 privacy_level == High。"""
    wc = synopsis.get("word_count") or 0
    try:
        wc = int(wc)
    except (TypeError, ValueError):
        wc = 0
    return wc < 300 and (synopsis.get("privacy_level") == "High")


# --- 落盘路径（按 core_entities）---
def _storage_subdir(synopsis: Dict[str, Any]) -> str:
    """根据 core_entities 决定归档子目录。"""
    entities = synopsis.get("core_entities") or []
    if entities:
        return entities[0]  # 取首个命中
    return "Inbox"


def _safe_filename(s: str, max_len: int = 80) -> str:
    s = re.sub(r'[<>:"/\\|?*\n\r]', "_", str(s).strip())
    return s[:max_len] if s else "untitled"


# --- Frontmatter：从缩影生成（极简/默认分支）---
def build_frontmatter_from_synopsis(synopsis: Dict[str, Any]) -> Dict[str, Any]:
    """从增强型缩影生成 Obsidian 标准 YAML 表头。"""
    return {
        "source": "harvester_v2",
        "word_count": synopsis.get("word_count", 0),
        "summary_200": synopsis.get("summary_200", ""),
        "file_type": synopsis.get("file_type", ""),
        "source_path": synopsis.get("source_path", ""),
        "privacy_level": synopsis.get("privacy_level", "Normal"),
        "task_count": synopsis.get("task_count", 0),
        "core_entities": synopsis.get("core_entities", []),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "tags": ["归档", synopsis.get("file_type", "note")],
    }


def write_note_with_frontmatter(
    dest_dir: Path,
    body: str,
    frontmatter_dict: Dict[str, Any],
    filename_base: Optional[str] = None,
) -> Path:
    """将正文 + Frontmatter 写入目标目录，返回写入路径。"""
    dest_dir.mkdir(parents=True, exist_ok=True)
    if not filename_base:
        filename_base = f"note_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    filename_base = _safe_filename(filename_base, 120)
    path = dest_dir / f"{filename_base}.md"
    post = frontmatter.Post(body, **frontmatter_dict)
    path.write_text(frontmatter.dumps(post), encoding="utf-8")
    return path


# --- 3090 降级：纯文本移动 ---
def fallback_move_no_llm(src_path: Path, vault_path: Path, archive_root: str, fallback_dir: str) -> Path:
    """3090 不可用时，将文件移动到归档/fallback，不写 Frontmatter。"""
    root = vault_path / archive_root / fallback_dir
    root.mkdir(parents=True, exist_ok=True)
    dest = root / src_path.name
    if dest.resolve() == src_path.resolve():
        return dest
    body = src_path.read_text(encoding="utf-8")
    dest.write_text(body, encoding="utf-8")
    try:
        src_path.unlink()
    except OSError:
        pass
    return dest


# --- Dify 调用（高智商分支）---
async def call_dify_workflow(synopsis: Dict[str, Any], full_text: str) -> Optional[Dict[str, Any]]:
    """调用 Dify 工作流，传入缩影+全文，期望返回完整小黑 JSON。"""
    url = (CONFIG.get("DIFY_API_URL") or "").strip()
    key = (CONFIG.get("DIFY_API_KEY") or "").strip()
    if not url or not key:
        LOG.warning("Dify 未配置 DIFY_API_URL / DIFY_API_KEY，高智商分支跳过云端")
        return None
    payload = {
        "inputs": {
            "synopsis": json.dumps(synopsis, ensure_ascii=False),
            "raw_content": full_text[:8000],
        },
        "response_mode": "blocking",
        "user": "harvester_v2",
    }
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                url,
                json=payload,
                headers=headers,
                timeout=CONFIG.get("DIFY_TIMEOUT", 120),
            )
            if resp.status_code != 200:
                LOG.warning("Dify 请求失败: status=%s body=%s", resp.status_code, resp.text[:200])
                return None
            data = resp.json()
            # Dify 返回结构可能是 data.outputs 或 data.data.outputs
            outputs = (data.get("data") or data).get("outputs") or data.get("outputs") or {}
            # 假设工作流输出变量名为 result 或 xiaohei_json
            raw = outputs.get("result") or outputs.get("xiaohei_json") or outputs.get("text") or ""
            if isinstance(raw, dict):
                return raw
            if isinstance(raw, str) and raw.strip():
                return json.loads(raw)
    except Exception as e:
        LOG.exception("Dify 调用异常: %s", e)
    return None


# --- 从完整小黑 JSON 落盘（复用 harvester）---
def harvest_with_full_xiaohei(xiaohei: Dict[str, Any], source_content: str, vault_path: Path, archive_root: str) -> Optional[Path]:
    """有完整小黑 JSON 时，复用 harvester 逻辑落盘。"""
    try:
        from harvester import write_harvested_note
        written = write_harvested_note(
            xiaohei,
            source_content=source_content,
            vault_path=str(vault_path),
        )
        return Path(written)
    except Exception as e:
        LOG.exception("harvester.write_harvested_note 失败: %s", e)
        return None


# --- 单文件处理流水线 ---
async def process_one_file(file_path: Path) -> Tuple[str, Optional[Path]]:
    """
    处理单文件：Step1 哨兵 → Step2 分流 → 落盘。
    返回 (status, written_path)，status 为 "ok" | "fallback" | "error"。
    """
    vault = Path(CONFIG["VAULT_PATH"])
    inbox = Path(CONFIG["INBOX_PATH"])
    archive_root = CONFIG["ARCHIVE_ROOT"]
    fallback_dir = CONFIG["FALLBACK_DIR"]

    if not file_path.is_file() or file_path.suffix.lower() != ".md":
        return "skip", None

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        LOG.exception("读取文件失败 %s: %s", file_path, e)
        return "error", None

    # Step 1: 本地哨兵（3090）
    try:
        base_synopsis = await build_synopsis(
            content,
            source_path=str(file_path),
        )
    except Exception as e:
        LOG.warning("3090 不可用或超时，进入纯文本移动模式: %s", e)
        dest = fallback_move_no_llm(file_path, vault, archive_root, fallback_dir)
        LOG.info("已移动至 fallback: %s -> %s", file_path, dest)
        return "fallback", dest

    synopsis = enhance_synopsis(content, base_synopsis)
    subdir = _storage_subdir(synopsis)
    dest_dir = vault / archive_root / subdir

    # Step 2: 智能分流
    if _should_high_intel(content, synopsis):
        xiaohei = await call_dify_workflow(synopsis, content)
        if xiaohei:
            written = harvest_with_full_xiaohei(xiaohei, content, vault, archive_root)
            if written:
                LOG.info("高智商分支落盘: %s -> %s", file_path.name, written)
                try:
                    file_path.unlink()
                except OSError:
                    pass
                return "ok", written
        # Dify 未返回或未配置，退化为本地 Frontmatter
        fm = build_frontmatter_from_synopsis(synopsis)
        base_name = file_path.stem
        written = write_note_with_frontmatter(dest_dir, content, fm, filename_base=base_name)
        try:
            file_path.unlink()
        except OSError:
            pass
        LOG.info("高智商分支降级为本地 FM: %s -> %s", file_path.name, written)
        return "ok", written

    if _should_minimal_local(synopsis):
        fm = build_frontmatter_from_synopsis(synopsis)
        base_name = file_path.stem
        written = write_note_with_frontmatter(dest_dir, content, fm, filename_base=base_name)
        try:
            file_path.unlink()
        except OSError:
            pass
        LOG.info("极简分支落盘: %s -> %s", file_path.name, written)
        return "ok", written

    # 默认：本地缩影 Frontmatter
    fm = build_frontmatter_from_synopsis(synopsis)
    base_name = file_path.stem
    written = write_note_with_frontmatter(dest_dir, content, fm, filename_base=base_name)
    try:
        file_path.unlink()
    except OSError:
        pass
    LOG.info("默认分支落盘: %s -> %s", file_path.name, written)
    return "ok", written


# --- Watchdog + 异步队列 ---
def _enqueue_path(queue: asyncio.Queue, path: str) -> None:
    try:
        queue.put_nowait(path)
    except asyncio.QueueFull:
        LOG.warning("队列已满，丢弃路径: %s", path)


async def worker(queue: asyncio.Queue) -> None:
    """从队列取路径并处理。"""
    while True:
        try:
            path = await queue.get()
            if path is None:
                break
            p = Path(path)
            if not p.exists():
                queue.task_done()
                continue
            status, written = await process_one_file(p)
            LOG.info("处理完成 %s -> status=%s written=%s", path, status, written)
            queue.task_done()
        except asyncio.CancelledError:
            break
        except Exception as e:
            LOG.exception("worker 异常: %s", e)
            queue.task_done()


def run_scheduler() -> None:
    """同步入口：启动 Watchdog + 异步处理循环。"""
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        raise ImportError("请安装 watchdog: pip install watchdog")

    inbox = Path(CONFIG["INBOX_PATH"])
    inbox.mkdir(parents=True, exist_ok=True)
    queue: asyncio.Queue = asyncio.Queue(maxsize=500)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    def enqueue_safe(path: str) -> None:
        loop.call_soon_threadsafe(lambda: _enqueue_path(queue, path))

    class Handler(FileSystemEventHandler):
        def on_created(self, event):
            if event.is_directory:
                return
            if event.src_path.endswith(".md"):
                enqueue_safe(event.src_path)

        def on_modified(self, event):
            if event.is_directory:
                return
            if event.src_path.endswith(".md"):
                enqueue_safe(event.src_path)

    async def run_worker_forever():
        await worker(queue)

    t = loop.create_task(run_worker_forever())
    observer = Observer()
    observer.schedule(Handler(), str(inbox), recursive=True)
    observer.start()
    LOG.info("Harvester V2 调度器已启动，监控目录: %s", inbox)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.call_soon_threadsafe(lambda: queue.put_nowait(None))
        t.cancel()
        observer.stop()
        observer.join()
        loop.run_until_complete(asyncio.gather(t, return_exceptions=True))
        loop.close()
    LOG.info("调度器已停止")


if __name__ == "__main__":
    run_scheduler()
