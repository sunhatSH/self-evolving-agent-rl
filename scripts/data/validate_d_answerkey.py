#!/usr/bin/env python3
"""一次性验证: D 类 answer_key 本身可不可解。

对 verif6 里的每个 D 类任务:
  1. 读 answer_key.json 的 checks (question/answer 对)
  2. 把输入文件 dump 成文本 (xlsx→CSV sheets, pdf→text, 其余原样)
  3. 让 luna 读文件内容 + 回答所有 check 问题 (输出 JSON {idx: answer})
  4. 拿 luna 的答案 vs GT answer 做容错比对 → correctness = 命中数/总数

目的: 看 answer_key 本身的质量。如果 luna 能答对,说明 GT 可解、问题清晰;
如果 luna 答错,要么 GT 错要么问题有歧义 → 这类 check 不可用作 correctness 判据。

用法:
  source scripts/load_training_env.sh  # 拿 TOKENHUB_API_KEY
  /opt/conda/bin/python3 scripts/data/validate_d_answerkey.py
  # 或指定 rollout 文件:
  ROLLOUT=rollouts/training/qwen35_9b_r0-25k_4gpu_verif6/rollout_status-1.jsonl \
    /opt/conda/bin/python3 scripts/data/validate_d_answerkey.py
"""
from __future__ import annotations

import io
import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / "src"))

ROLLOUT = os.environ.get(
    "ROLLOUT", "rollouts/training/qwen35_9b_r0-25k_4gpu_verif6/rollout_status-1.jsonl"
)
TASKSPECS = ROOT / "datasources" / "taskspecs_w3"
OUT_JSONL = ROOT / "logs" / "validate_d_answerkey.jsonl"
OUT_SUMMARY = ROOT / "logs" / "validate_d_answerkey_summary.txt"


# --- file dumping --------------------------------------------------------- #

def _dump_xlsx(path: Path) -> str:
    try:
        import pandas as pd
    except ImportError:
        return f"[binary .xlsx, pandas unavailable — skipped]"
    out = []
    try:
        xls = pd.ExcelFile(path)
        for sheet in xls.sheet_names:
            df = pd.read_excel(path, sheet_name=sheet, dtype=object)
            out.append(f"## {path.name} :: sheet {sheet} ({len(df)} rows)")
            out.append(df.to_csv(index=False))
    except Exception as e:
        return f"[xlsx read error: {e}]"
    return "\n".join(out)


def _dump_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return f"[binary .pdf, pypdf unavailable — skipped]"
    try:
        r = PdfReader(str(path))
        txt = "\n".join((p.extract_text() or "") for p in r.pages)
        return f"## {path.name} (pdf text)\n{txt}"
    except Exception as e:
        return f"[pdf read error: {e}]"


def _dump_sqlite(path: Path) -> str:
    try:
        import sqlite3
    except ImportError:
        return f"[sqlite, unavailable]"
    out = []
    try:
        con = sqlite3.connect(str(path))
        cur = con.cursor()
        tables = [r[0] for r in cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
        for t in tables:
            n = cur.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
            out.append(f"## {path.name} :: table {t} ({n} rows)")
            rows = cur.execute(f"SELECT * FROM {t} LIMIT 50").fetchall()
            cols = [d[0] for d in cur.description]
            out.append(",".join(cols))
            for r in rows:
                out.append(",".join(str(x) for x in r))
        con.close()
    except Exception as e:
        return f"[sqlite read error: {e}]"
    return "\n".join(out)


def dump_file(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".xlsx":
        return _dump_xlsx(path)
    if ext == ".pdf":
        return _dump_pdf(path)
    if ext == ".sqlite" or ext == ".db":
        return _dump_sqlite(path)
    try:
        txt = path.read_text(encoding="utf-8", errors="replace")
        if len(txt) > 20000:
            txt = txt[:20000] + f"\n...[truncated, {len(txt)} chars total]"
        return f"## {path.name}\n{txt}"
    except Exception as e:
        return f"[read error: {e}]"


def dump_task_files(tid: str) -> str:
    fdir = TASKSPECS / tid / "files"
    if not fdir.is_dir():
        return ""
    parts = []
    for f in sorted(fdir.iterdir()):
        parts.append(dump_file(f))
    return "\n\n".join(parts)


# --- answer comparison ---------------------------------------------------- #

def _norm_num(v):
    """Try to coerce to float for numeric compare."""
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def answers_match(luna_ans, gt_ans) -> bool:
    """Tolerant match: numbers within 1% (or 0.01 abs), strings stripped equal,
    lists/dicts compared element-wise with numeric tolerance."""
    # Direct string compare after strip
    ls = str(luna_ans).strip()
    gs = str(gt_ans).strip()
    if ls == gs:
        return True
    # Numeric compare
    ln, gn = _norm_num(ls), _norm_num(gs)
    if ln is not None and gn is not None:
        if abs(ln - gn) < 0.01 + 0.01 * max(1.0, abs(gn)):
            return True
    # List/dict: parse both as JSON if possible, compare structurally
    try:
        lj = json.loads(ls) if ls[0] in "[{" else None
    except Exception:
        lj = None
    try:
        gj = json.loads(gs) if gs[0] in "[{" else None
    except Exception:
        gj = None
    if lj is not None and gj is not None:
        if _struct_match(lj, gj):
            return True
    return False


def _struct_match(a, b) -> bool:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(float(a) - float(b)) < 0.01 + 0.01 * max(1.0, abs(float(b)))
    if isinstance(a, str) and isinstance(b, str):
        return a.strip() == b.strip()
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        return all(_struct_match(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        return all(_struct_match(a[k], b[k]) for k in a)
    return False


# --- luna call ----------------------------------------------------------- #

def _resolve_endpoint():
    """Resolve tokenhub luna endpoint (mirrors agents.config.resolve_judge)."""
    base = os.environ.get("REWARD_API_BASE") or "https://tokenhub.sensetime.com/v1"
    model = os.environ.get("REWARD_MODEL") or "gpt-5.6-luna"
    key = (
        os.environ.get("TOKENHUB_API_KEY")
        or os.environ.get("REWARD_API_KEY")
        or ""
    )
    return base, model, key


def ask_luna(prompt: str, timeout: float = 180.0) -> str:
    import httpx
    base, model, key = _resolve_endpoint()
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a precise data analyst. Read the provided file contents and answer every question exactly. Output ONLY a JSON object mapping question index (0-based) to the answer. Use numbers when the answer is numeric. For multi-value answers, use a JSON array or object. No prose, no markdown fences."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.0,
        "max_tokens": 8192,
        "reasoning_effort": os.environ.get("REWARD_JUDGE_EFFORT", "") or "high",
    }
    headers = {"Authorization": f"Bearer {key}"}
    resp = httpx.post(f"{base}/chat/completions", json=body, headers=headers, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


# --- main ---------------------------------------------------------------- #

def collect_d_tasks():
    tasks = []
    with open(ROLLOUT) as f:
        for line in f:
            d = json.loads(line)
            tid = d["task_id"]
            if tid.startswith("D"):
                tasks.append(tid)
    return sorted(set(tasks))


def build_prompt(tid, checks, file_dump):
    qlines = []
    for i, c in enumerate(checks):
        q = c.get("question", c.get("name", ""))
        qlines.append(f"Q{i}: {q}")
    prompt = (
        f"# Task {tid} input files\n\n{file_dump}\n\n"
        f"# Questions (answer ALL {len(checks)} from the files above)\n"
        + "\n".join(qlines)
        + "\n\nReturn ONLY JSON: {\"0\": <ans>, \"1\": <ans>, ...}"
    )
    return prompt


def run_one(tid):
    ak_path = TASKSPECS / tid / "answer_key.json"
    if not ak_path.is_file():
        return {"task_id": tid, "error": "no answer_key"}
    ak = json.loads(ak_path.read_text("utf-8"))
    checks = ak.get("checks") or []
    if not checks:
        return {"task_id": tid, "error": "no checks", "ak_type": ak.get("type")}

    file_dump = dump_task_files(tid)
    if not file_dump:
        return {"task_id": tid, "error": "no files", "n_checks": len(checks)}

    prompt = build_prompt(tid, checks, file_dump)
    try:
        raw = ask_luna(prompt)
    except Exception as e:
        return {"task_id": tid, "error": f"luna call failed: {e}", "n_checks": len(checks)}

    # parse luna JSON
    try:
        # strip markdown fences if any
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        luna_ans = json.loads(m.group(0)) if m else json.loads(raw)
    except Exception:
        return {"task_id": tid, "error": "luna output not JSON", "raw": raw[:500],
                "n_checks": len(checks)}

    # compare
    hits = 0
    per_check = []
    for i, c in enumerate(checks):
        gt = c.get("answer", c.get("value"))
        la = luna_ans.get(str(i))
        if la is None:
            la = luna_ans.get(i)
        ok = answers_match(la, gt) if la is not None else False
        if ok:
            hits += 1
        per_check.append({
            "q": str(c.get("question", c.get("name", "")))[:120],
            "gt": gt,
            "luna": la,
            "ok": ok,
        })
    return {
        "task_id": tid,
        "n_checks": len(checks),
        "hits": hits,
        "correctness": hits / len(checks) if checks else 0.0,
        "per_check": per_check,
        "luna_raw_head": raw[:300],
    }


def main():
    tasks = collect_d_tasks()
    print(f"[validate_d_answerkey] {len(tasks)} D-type tasks from {ROLLOUT}")
    results = []
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSONL, "w") as out:
        for i, tid in enumerate(tasks):
            t0 = time.time()
            r = run_one(tid)
            r["elapsed_s"] = round(time.time() - t0, 1)
            out.write(json.dumps(r, ensure_ascii=False) + "\n")
            out.flush()
            results.append(r)
            if "error" in r:
                print(f"  [{i+1}/{len(tasks)}] {tid}: ERROR {r['error']} ({r['elapsed_s']}s)")
            else:
                print(f"  [{i+1}/{len(tasks)}] {tid}: {r['hits']}/{r['n_checks']} "
                      f"corr={r['correctness']:.3f} ({r['elapsed_s']}s)")

    # summary
    ok = [r for r in results if "error" not in r]
    if ok:
        corrs = [r["correctness"] for r in ok]
        mean_c = sum(corrs) / len(corrs)
        n0 = sum(1 for c in corrs if c == 0.0)
        n1 = sum(1 for c in corrs if c >= 0.99)
        total_checks = sum(r["n_checks"] for r in ok)
        total_hits = sum(r["hits"] for r in ok)
        lines = [
            f"D-type tasks: {len(tasks)}",
            f"  scored (no error): {len(ok)}",
            f"  errors: {len(tasks) - len(ok)}",
            f"  per-task correctness: mean={mean_c:.3f}  ==0:{n0}/{len(ok)}  ==1:{n1}/{len(ok)}",
            f"  per-check (micro): {total_hits}/{total_checks} = {total_hits/total_checks:.3f}",
        ]
        s = "\n".join(lines)
    else:
        s = "no tasks scored (all errored)"
    OUT_SUMMARY.write_text(s)
    print("\n=== SUMMARY ===")
    print(s)
    print(f"\nfull results: {OUT_JSONL}")
    print(f"summary:      {OUT_SUMMARY}")


if __name__ == "__main__":
    main()
