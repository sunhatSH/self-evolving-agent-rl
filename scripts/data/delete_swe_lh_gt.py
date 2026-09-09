#!/usr/bin/env python3
"""删除 SWE + LH 任务的旧 GT（answer_key.json），保留目录与 files/inputs。

背景（2026-09-03 用户决策）：SWE/LH 的旧 GT 是运行类判据（LH checks = 输入→期望
输出测试用例、SWE = 行为验收 rubric），LLM judge 无法运行只能读文本猜 → 系统性错判
（见 Bug_Fix F17）。故删除这两类 GT，改由 gen_static_gt.py 重制成"只需查看轨迹+diff、
不需执行"的静态验收点。D 类 GT（别人给的）不动。

只删 taskspecs_w3/{SWE_*,LH_*}/answer_key.json，保留目录本身及 files/inputs（沙箱注入
仍需要）。删除清单写日志，便于回溯。

用法: python3 scripts/data/delete_swe_lh_gt.py [--dry-run]
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/mnt/afs_toolcall/sunhao4/workspace/agentic_cl_research")
TASKSPECS = ROOT / "datasources" / "taskspecs_w3"
LOG = ROOT / "logs" / "delete_swe_lh_gt.log"


def main() -> int:
    dry = "--dry-run" in sys.argv
    deleted: list[str] = []
    missing = 0
    for prefix in ("SWE_", "LH_"):
        for d in sorted(TASKSPECS.glob(f"{prefix}*")):
            if not d.is_dir():
                continue
            ak = d / "answer_key.json"
            if ak.is_file():
                if not dry:
                    ak.unlink()
                deleted.append(str(ak.relative_to(ROOT)))
            else:
                missing += 1

    LOG.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    header = f"[{ts}] {'DRY-RUN ' if dry else ''}deleted {len(deleted)} SWE/LH answer_key.json (missing={missing})"
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(header + "\n")
        for p in deleted[:20]:
            f.write(f"  {p}\n")
        if len(deleted) > 20:
            f.write(f"  ... (+{len(deleted) - 20} more)\n")

    print(header)
    print(f"样例: {deleted[:3]}")
    print(f"日志: {LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
