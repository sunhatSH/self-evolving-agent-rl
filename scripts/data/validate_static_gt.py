#!/usr/bin/env python3
"""验证新静态 GT 是否有意义:让 luna 当 agent 真跑 SWE/LH 任务,再用【新静态 GT】
对产出打 correctness(命中率),看 GT 能否区分好坏、每条验收点是否可判。

背景(2026-09-03):SWE/LH GT 重制为静态验收点(gen_static_gt.py),judge 按命中率判
(model_reward._render_static_gt + CORRECTNESS_RUBRIC)。本脚本做端到端验证:
  luna 起 e2b 沙箱 → 注入 files → hermes(luna) 跑任务 → before/after diff
  → 用真实 compute_score(注入 answer_key=新静态GT + observer diff)打 correctness
  → 汇总命中率分布 + 每条点命中情况,判 GT 是否有意义。

复用 probe_swe_completability 的沙箱/agent/diff 机器(upload_workspace/snapshot_ws/
diff_ws/_hermes_chat),打分换成走新 GT 的 compute_score(而非旧 rubric judge)。

用法(tmux 后台):
  tmux new -d -s valGT 'bash -c "cd ...; source .env; PYTHONPATH=src:. python3 scripts/data/validate_static_gt.py --limit 30"'
  --limit N 先抽样;满意再全量。需 TOKENHUB_API_KEY + e2b 凭证(tencent.env)。
输出: logs/validate_static_gt.jsonl(每任务一行) + 末尾汇总。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import httpx

ROOT = Path("/mnt/afs_toolcall/sunhao4/workspace/agentic_cl_research")
TASKSPECS = ROOT / "datasources" / "taskspecs_w3"
TRAIN_PARQUET = ROOT / "datasets" / "train_cl.parquet"
OUT = ROOT / "logs" / "validate_static_gt.jsonl"
ACTOR_MODEL = os.environ.get("VAL_ACTOR_MODEL", "gpt-5.6-luna")


def load_tasks(limit: int) -> list[dict]:
    """训练集命中的 SWE/LH:record_id + query + 有 static GT。"""
    import pyarrow.parquet as pq

    t = pq.read_table(TRAIN_PARQUET)
    seen = set()
    tasks = []
    for r in t.to_pylist():
        ei = r.get("extra_info") or {}
        rid = str(ei.get("record_id", "") or "")
        gid = str(ei.get("gen_task_id", "") or "")
        key = rid if rid.startswith(("SWE_", "LH_")) else gid
        if not key.startswith(("SWE_", "LH_")) or key in seen:
            continue
        ak = TASKSPECS / key / "answer_key.json"
        if not ak.is_file():
            continue
        try:
            akd = json.loads(ak.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if akd.get("type") != "static":
            continue
        seen.add(key)
        tasks.append({"id": key, "query": (ei.get("queries") or [""])[0], "answer_key": akd})
    if limit:
        tasks = tasks[:limit]
    return tasks


def run_one(task: dict, key: str, max_turns: int, slot_timeout: int) -> dict:
    """luna 跑一个任务 + 用新静态 GT 打 correctness。"""
    from rollout.sandbox_client import make_sandbox
    from scripts.data.probe_swe_completability import diff_ws, snapshot_ws, upload_workspace
    from trainer.model_reward import OpenAIJudgeClient, compute_score

    tid = task["id"]
    query = task["query"]
    ak = task["answer_key"]
    n_pts = len(ak.get("acceptance_points", []))
    result = {"id": tid, "n_points": n_pts}

    sb = None
    try:
        from scripts.collect.sandbox_grpo_collect import _hermes_chat, _write_hermes_config

        sb = make_sandbox("e2b", template="agentic-cl-sandbox", timeout=slot_timeout + 600)
        result["n_uploaded"] = upload_workspace(sb, tid)
        cfg = _write_hermes_config(sb, ACTOR_MODEL, "")
        if not cfg.ok:
            result["error"] = f"hermes config: {cfg.stderr[:150]}"
            return result

        before = snapshot_ws(sb)
        stdout, stderr, ok, _sid = _hermes_chat(sb, query, ACTOR_MODEL, max_turns, slot_timeout)
        result["agent_ok"] = bool(ok)
        after = snapshot_ws(sb)
        diff_text = diff_ws(before, after, sb)
        result["n_changed"] = len([p for p, v in after.items() if before.get(p) != v])

        # 用真实打分路径:注入 answer_key(新静态GT) + observer_report(diff) → compute_score
        judge = OpenAIJudgeClient(
            base_url=os.environ.get("REWARD_API_BASE", "https://tokenhub.sensetime.com/v1"),
            model=os.environ.get("REWARD_MODEL", "gpt-5.6-luna"),
            api_key=os.environ.get("TOKENHUB_API_KEY", ""),
        )
        scored = compute_score(
            "agentic_cl",
            (stdout or "")[-6000:],
            "",
            extra_info={
                "task": query,
                "answer_key": ak,
                "observer_report": diff_text[:8000],
            },
            judge=judge,
        )
        result["correctness"] = round(float(scored.get("correctness", 0.0)), 3)
        result["consistency"] = round(float(scored.get("consistency", 0.0)), 3)
        result["score"] = round(float(scored.get("score", 0.0)), 3)
        result["correctness_reason"] = (scored.get("correctness_reason") or "")[:300]
        result["judge_error"] = scored.get("judge_error", 0.0)
    except Exception as exc:  # noqa: BLE001
        result["error"] = f"{type(exc).__name__}: {str(exc)[:200]}"
    finally:
        if sb is not None:
            try:
                sb.kill()
            except Exception:  # noqa: BLE001
                pass
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=30)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--max-turns", type=int, default=30)
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args()

    key = os.environ.get("TOKENHUB_API_KEY", "")
    if not key:
        print("ERROR: 需要 TOKENHUB_API_KEY", file=sys.stderr)
        return 1

    tasks = load_tasks(args.limit)
    print(f"验证 {len(tasks)} 个任务(luna 跑 + 新静态GT打分), workers={args.workers}", flush=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)

    results = []
    with open(OUT, "w", encoding="utf-8") as fout, ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(run_one, t, key, args.max_turns, args.timeout): t["id"] for t in tasks}
        for i, fut in enumerate(as_completed(futs), 1):
            r = fut.result()
            results.append(r)
            fout.write(json.dumps(r, ensure_ascii=False) + "\n")
            fout.flush()
            print(f"  [{i}/{len(tasks)}] {r['id']} corr={r.get('correctness')} "
                  f"changed={r.get('n_changed')} err={r.get('error','')}", flush=True)

    # 汇总:GT 是否有意义
    scored = [r for r in results if r.get("correctness") is not None]
    errs = [r for r in results if r.get("error")]
    if scored:
        cs = [r["correctness"] for r in scored]
        import statistics
        print(f"\n=== 汇总 ({len(scored)} 打分成功, {len(errs)} error) ===")
        print(f"correctness: mean={statistics.mean(cs):.3f} min={min(cs):.3f} max={max(cs):.3f}")
        print(f"  ==0: {sum(1 for x in cs if x==0)}  0<x<1: {sum(1 for x in cs if 0<x<1)}  ==1: {sum(1 for x in cs if x==1)}")
        print(f"  区分度(0<corr<1 占比): {100*sum(1 for x in cs if 0<x<1)/len(cs):.0f}% "
              f"— 越高说明 GT 越能分辨部分完成(有意义);全 0 或全 1 = GT 失效")
    print(f"\n明细: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
