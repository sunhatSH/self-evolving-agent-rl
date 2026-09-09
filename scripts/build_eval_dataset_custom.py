#!/usr/bin/env python3
"""Build a new ClawEval-format eval dataset from sampled tasks.

Samples 30/bucket (communication 6, qa 23 — pool-limited) from
all_tasks_labeled.jsonl, EXCLUDING the 6400 train_cl D_ids. Generates
ClawEval-format task.yaml + grader.py per task, plus a manifest.

Three task types map to two grader strategies:
  - checks (numeric/text GT) → score_answer fuzzy match (officeqa_reward-style)
  - rubric (subjective/code) → LLM judge on rubric text

Output: harness/claw-eval-official/tasks_custom/<task_id>/{task.yaml, grader.py}
        + eval/claweval_manifest_custom.json
"""
from __future__ import annotations

import json
import os
import pickle
import shutil
import textwrap
from pathlib import Path

import pandas as pd
import yaml

REPO = Path("/mnt/afs_toolcall/sunhao4/workspace/agentic_cl_research")
HARNESS = REPO / "harness" / "claw-eval-official"
TASKS_OUT = HARNESS / "tasks_custom"
MANIFEST_OUT = REPO / "src" / "eval" / "claweval_manifest_custom.json"

BUCKET_ORDER = [
    "workflow", "ops", "qa", "finance", "office",
    "communication", "safety", "coding", "research",
]


def load_train_rids() -> set[str]:
    tc = pd.read_parquet(REPO / "datasets" / "train_cl.parquet")
    rids = set()
    for ei in tc["extra_info"]:
        rid = ei.get("record_id") or ei.get("gen_task_id") or ""
        if rid:
            rids.add(rid)
    return rids


def load_all_tasks() -> list[dict]:
    rows = []
    with open(REPO / "datasources" / "labeled" / "all_tasks_labeled.jsonl") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def sample(all_tasks: list[dict], train_rids: set[str]) -> dict[str, list[dict]]:
    import random
    random.seed(42)
    by_bucket: dict[str, list[dict]] = {}
    for r in all_tasks:
        if r["D_id"] in train_rids:
            continue
        by_bucket.setdefault(r["bucket"], []).append(r)
    sampled = {}
    for b in BUCKET_ORDER:
        pool = by_bucket.get(b, [])
        n = min(30, len(pool))
        sampled[b] = random.sample(pool, n)
    return sampled


def find_task_dir(task: dict) -> Path | None:
    did = task["D_id"]
    if did.startswith("SWE"):
        p = REPO / "datasources" / "taskspecs_w3" / did
        return p if p.exists() else None
    # D-series: generated_tasks_hermes/<domain>/<D_id>
    domain = did.split("_")[0]
    p = REPO / "datasources" / "generated_tasks_hermes" / domain / did
    return p if p.exists() else None


def load_answer_key(task_dir: Path) -> dict:
    ak = task_dir / "answer_key.json"
    if ak.exists():
        return json.loads(ak.read_text())
    return {}


def load_task_json(task_dir: Path) -> dict:
    tj = task_dir / "task.json"
    if tj.exists():
        return json.loads(tj.read_text())
    # SWE uses taskspec.yaml
    ts = task_dir / "taskspec.yaml"
    if ts.exists():
        return {"user_prompt": yaml.safe_load(ts.read_text()).get("seed_query", "")}
    return {}


def classify(ak: dict) -> str:
    if ak.get("checks"):
        return "checks"
    if ak.get("rubric"):
        return "rubric"
    return "none"


def gen_task_yaml(task: dict, tjson: dict, task_dir: Path, bucket: str) -> str:
    did = task["D_id"]
    prompt = task["user_prompt"]
    inputs_dir = task.get("inputs_dir") or ""
    # sandbox_files: list input files (relative to task dir)
    sandbox_files = []
    if inputs_dir and Path(inputs_dir).exists():
        for f in sorted(Path(inputs_dir).iterdir()):
            if f.is_file():
                sandbox_files.append(f"inputs/{f.name}")
    difficulty = str(task.get("difficulty", "medium"))
    ty = {
        "task_id": did,
        "task_name": did,
        "version": "1.0",
        "category": bucket,
        "difficulty": difficulty,
        "tags": ["general"],
        "prompt": {"text": prompt, "language": "zh" if "_zh" in did else "en"},
        "tools": [],
        "tool_endpoints": [],
        "environment": {"timeout_seconds": 900, "max_turns": 30},
        "sandbox_files": sandbox_files,
    }
    return yaml.safe_dump(ty, allow_unicode=True, sort_keys=False)


GRADER_CHECKS_TEMPLATE = '''\
"""Auto-generated grader for {task_id} (checks-type: numeric/text GT)."""
from __future__ import annotations
import json, re
from claw_eval.graders.base import AbstractGrader
from claw_eval.models.task import TaskDefinition
from claw_eval.models.trace import DimensionScores, ToolDispatch, TraceMessage


def _extract_numbers(text: str) -> list[float]:
    out = []
    for m in re.finditer(r"-?\\d+\\.?\\d*", text):
        try:
            out.append(float(m.group()))
        except ValueError:
            pass
    return out


def _fuzzy_num(gt, pred, tol=0.05) -> bool:
    try:
        g = float(gt)
    except (TypeError, ValueError):
        return str(gt) in pred
    nums = _extract_numbers(pred)
    return any(abs(n - g) <= abs(g) * tol + 1e-6 for n in nums)


def _fuzzy_str(gt, pred) -> bool:
    return str(gt).strip() in pred


class Grader(AbstractGrader):
    def grade(self, messages, dispatches, task, audit_data=None, judge=None, media_events=None, env_snapshot=None):
        scores = DimensionScores()
        scores.safety = 1.0
        scores.robustness = 1.0
        ak = json.loads({answer_key_json})
        checks = ak.get("checks", [])
        if not checks:
            scores.completion = 0.0
            scores.communication = 0.0
            return scores
        final = ""
        for m in messages:
            if m.message.role == "assistant":
                final += m.message.text + "\\n"
        hit = 0
        for c in checks:
            q = c.get("question", "")
            a = c.get("answer")
            if a is None:
                continue
            if isinstance(a, (int, float)):
                ok = _fuzzy_num(a, final)
            elif isinstance(a, dict):
                ok = any(_fuzzy_num(v, final) for v in a.values() if isinstance(v, (int, float)))
            else:
                ok = _fuzzy_str(a, final)
            if ok:
                hit += 1
        scores.completion = round(hit / len(checks), 2) if checks else 0.0
        scores.communication = scores.completion
        return scores
'''


GRADER_RUBRIC_TEMPLATE = '''\
"""Auto-generated grader for {task_id} (rubric-type: LLM judge)."""
from __future__ import annotations
import json
from claw_eval.graders.base import AbstractGrader
from claw_eval.models.trace import DimensionScores


class Grader(AbstractGrader):
    def grade(self, messages, dispatches, task, audit_data=None, judge=None, media_events=None, env_snapshot=None):
        scores = DimensionScores()
        scores.safety = 1.0
        scores.robustness = 1.0
        ak = json.loads({answer_key_json})
        rubric = ak.get("rubric", [])
        if not rubric or judge is None:
            scores.completion = 0.0
            scores.communication = 0.0
            return scores
        conv = self.format_conversation(messages)
        rubric_text = chr(10).join("- " + r for r in rubric)
        try:
            result = judge.evaluate(task.prompt.text, conv, "", rubric_text)
            scores.completion = result.score
            scores.communication = result.score
        except Exception:
            scores.completion = 0.0
            scores.communication = 0.0
        return scores
'''


def gen_grader(task_id: str, ak: dict, atype: str) -> str:
    ak_json = json.dumps(ak, ensure_ascii=False)
    # escape for embedding in Python source
    ak_escaped = ak_json.replace("\\", "\\\\").replace("'", "\\'")
    if atype == "checks":
        return GRADER_CHECKS_TEMPLATE.format(
            task_id=task_id, answer_key_json="'" + ak_escaped + "'"
        )
    return GRADER_RUBRIC_TEMPLATE.format(
        task_id=task_id, answer_key_json="'" + ak_escaped + "'"
    )


def main() -> None:
    train_rids = load_train_rids()
    all_tasks = load_all_tasks()
    sampled = sample(all_tasks, train_rids)

    if TASKS_OUT.exists():
        shutil.rmtree(TASKS_OUT)
    TASKS_OUT.mkdir(parents=True, exist_ok=True)

    manifest = []
    stats = {"checks": 0, "rubric": 0, "none": 0}
    for bucket in BUCKET_ORDER:
        for task in sampled[bucket]:
            did = task["D_id"]
            task_dir = find_task_dir(task)
            if task_dir is None:
                print(f"  SKIP {did}: task dir not found")
                continue
            ak = load_answer_key(task_dir)
            tjson = load_task_json(task_dir)
            atype = classify(ak)
            stats[atype] = stats.get(atype, 0) + 1

            out_dir = TASKS_OUT / did
            out_dir.mkdir(parents=True, exist_ok=True)

            # task.yaml
            (out_dir / "task.yaml").write_text(
                gen_task_yaml(task, tjson, task_dir, bucket)
            )
            # grader.py
            (out_dir / "grader.py").write_text(gen_grader(did, ak, atype))
            # inputs (copy if exists)
            inputs_src = task.get("inputs_dir") or ""
            if inputs_src and Path(inputs_src).exists():
                (out_dir / "inputs").mkdir(exist_ok=True)
                for f in Path(inputs_src).iterdir():
                    if f.is_file():
                        shutil.copy2(f, out_dir / "inputs" / f.name)

            manifest.append({
                "task_id": did,
                "bucket": bucket,
                "category": bucket,
                "modality": "text",
                "split": "General",
                "prompt": task["user_prompt"][:200],
                "grader_type": atype,
            })

    MANIFEST_OUT.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2)
    )

    print("=" * 60)
    print(f"生成完成: {len(manifest)} 任务")
    print(f"输出: {TASKS_OUT}")
    print(f"manifest: {MANIFEST_OUT}")
    print(f"grader 类型: {stats}")
    print("分桶:")
    from collections import Counter
    for b in BUCKET_ORDER:
        n = sum(1 for m in manifest if m["bucket"] == b)
        print(f"  {b}: {n}")


if __name__ == "__main__":
    main()
