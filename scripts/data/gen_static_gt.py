#!/usr/bin/env python3
"""重制 SWE/LH 的 GT 为【静态验收点】(只需查看轨迹+diff,不需执行)。

背景(2026-09-03 用户决策,见 Bug_Fix F17/F18):旧 SWE/LH GT 是运行类判据
(LH=输入→期望输出测试用例、SWE=行为验收 rubric),text-only LLM judge 无法运行
只能读文本猜 → 系统性错判。重制为 judge 可【目测】的静态验收点,judge 逐条核对命中率。

数据流(in-place 重制,现有 answer_key 是源材料,故先跑本脚本再谈删除):
  读 taskspecs_w3/<id>/answer_key.json(旧 rubric/checks/title,含接口与行为材料)
  + 训练集 query(任务描述;LH 含 embedded source + 迁移规格)
  → 调 tokenhub 强模型(build_static_gt_prompt)生成 acceptance_points
  → 覆盖写回 answer_key.json: {"type":"static","title":..,"acceptance_points":[{point,checkable_from},..]}

判分端:agents.prompts._load_ground_truth 识别 type=="static" → 渲染验收清单;
model_reward.CORRECTNESS_RUBRIC 判"逐条命中率"。

用法(tmux 后台,项目规则):
  tmux new -d -s genGT 'PY=/opt/conda/bin/python3; PYTHONPATH=src:. $PY scripts/data/gen_static_gt.py'
  只跑训练集命中的 SWE/LH(默认);--all 跑 taskspecs_w3 下全部;--limit N 抽样试跑。
凭证: 需 TOKENHUB_API_KEY(source .env)。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import httpx

ROOT = Path("/mnt/afs_toolcall/sunhao4/workspace/agentic_cl_research")
TASKSPECS = ROOT / "datasources" / "taskspecs_w3"
TRAIN_PARQUET = ROOT / "datasets" / "train_cl.parquet"
API_BASE = os.environ.get("GT_GEN_API_BASE", "https://tokenhub.sensetime.com/v1")
MODEL = os.environ.get("GT_GEN_MODEL", "gpt-5.6-luna")
API_KEY = os.environ.get("TOKENHUB_API_KEY", "")


def _load_task_queries() -> dict[str, str]:
    """record_id/gen_task_id → 训练集 query(任务描述 + LH 的 embedded source)。"""
    import pyarrow.parquet as pq

    out: dict[str, str] = {}
    t = pq.read_table(TRAIN_PARQUET)
    for r in t.to_pylist():
        ei = r.get("extra_info") or {}
        rid = str(ei.get("record_id", "") or "")
        gid = str(ei.get("gen_task_id", "") or "")
        q = (ei.get("queries") or [""])[0] if ei.get("queries") else ""
        for k in (rid, gid):
            if k and k not in out:
                out[k] = q
    return out


def _old_material(ak: dict) -> str:
    """把旧 answer_key 的 rubric/checks/title 拼成源材料(供 LLM 转写成静态点)。"""
    parts: list[str] = []
    if ak.get("title"):
        parts.append(f"Title: {ak['title']}")
    rub = ak.get("rubric")
    if rub:
        if isinstance(rub, list):
            parts.append("Behavior requirements:\n" + "\n".join(f"- {x}" for x in rub))
        else:
            parts.append(f"Behavior requirements:\n{rub}")
    checks = ak.get("checks")
    if checks:
        parts.append("Original test cases (TRANSLATE to inspectable structure, do NOT keep as run-based):\n"
                     + json.dumps(checks, ensure_ascii=False)[:3000])
    return "\n\n".join(parts)


def _gen_one(rid: str, query: str, client: httpx.Client) -> dict | None:
    """为一个任务生成 static GT。返回 answer_key dict,失败返回 None。"""
    from agents.prompts import build_static_gt_prompt, parse_check_code  # noqa: F401

    ak_path = TASKSPECS / rid / "answer_key.json"
    if not (TASKSPECS / rid).is_dir():
        return None
    old = {}
    if ak_path.is_file():
        try:
            old = json.loads(ak_path.read_text(encoding="utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            old = {}
    material = _old_material(old)
    if not material and not query:
        return None

    messages = build_static_gt_prompt(task=query or old.get("title", ""), source_material=material)
    for attempt in range(3):
        try:
            resp = client.post(
                f"{API_BASE}/chat/completions",
                json={"model": MODEL, "messages": messages, "max_tokens": 2048, "temperature": 0.0},
                headers={"Authorization": f"Bearer {API_KEY}"},
                timeout=120.0,
            )
            resp.raise_for_status()
            content = resp.json()["choices"][0]["message"]["content"]
            obj = _parse_json(content)
            pts = obj.get("acceptance_points") if isinstance(obj, dict) else None
            if pts and isinstance(pts, list):
                return {
                    "type": "static",
                    "title": old.get("title", ""),
                    "acceptance_points": pts,
                }
        except Exception:  # noqa: BLE001
            time.sleep(1.5 * (attempt + 1))
    return None


def _parse_json(text: str) -> dict:
    import re

    if not text:
        return {}
    try:
        return json.loads(text)
    except (TypeError, ValueError):
        m = re.search(r"\{.*\}", text, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except (TypeError, ValueError):
                return {}
    return {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="跑 taskspecs 下全部 SWE/LH(默认只跑训练集命中的)")
    ap.add_argument("--limit", type=int, default=0, help="抽样试跑前 N 个")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    if not API_KEY:
        print("ERROR: 需要 TOKENHUB_API_KEY(source .env)", file=sys.stderr)
        return 1

    queries = _load_task_queries()
    if args.all:
        ids = [d.name for d in sorted(TASKSPECS.glob("SWE_*")) if d.is_dir()]
        ids += [d.name for d in sorted(TASKSPECS.glob("LH_*")) if d.is_dir()]
    else:
        ids = [k for k in queries if k.startswith(("SWE_", "LH_"))]
    ids = sorted(set(ids))
    if args.limit:
        ids = ids[: args.limit]
    print(f"待生成 {len(ids)} 个 static GT (all={args.all}, model={MODEL})", flush=True)

    ok = fail = 0
    lock_client = httpx.Client()

    def _work(rid: str) -> bool:
        gt = _gen_one(rid, queries.get(rid, ""), lock_client)
        if gt is None:
            return False
        (TASKSPECS / rid / "answer_key.json").write_text(
            json.dumps(gt, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return True

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for i, res in enumerate(ex.map(_work, ids), 1):
            if res:
                ok += 1
            else:
                fail += 1
            if i % 50 == 0:
                print(f"  进度 {i}/{len(ids)}  ok={ok} fail={fail}", flush=True)

    print(f"\n✅ static GT 生成完成: ok={ok} fail={fail} / {len(ids)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
