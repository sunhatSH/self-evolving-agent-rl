#!/usr/bin/env python3
"""Closed-loop smoke for the execution-grounded Verifier (agents/verifier.py).

CLOSED LOOP = 发起(task + trajectory + live sandbox) -> 得到 correctness 分, 且分数正确无误.

Two known-truth fixtures share the SAME task and the SAME real source data in a
LocalSandbox; they differ only in what the agent CLAIMED:

  fixture A (agent WRONG):   claims the sum is 100  -> verifier recomputes 42 -> LOW
  fixture B (agent CORRECT): claims the sum is 42   -> verifier recomputes 42 -> HIGH

The verifier reads ``data.csv`` from the live sandbox and runs its own check code,
so the score is grounded in reality rather than guessed from the agent's text.

PASS criteria (the "score is correct" assertion):
  - A.correctness < 0.4  AND  B.correctness > 0.6  AND  A < B
  - at least one fixture actually executed code in the sandbox (run_check issued)

Run (needs the real tokenhub judge key; long -> use tmux per project rules):
    set -a; source .env; set +a          # loads TOKENHUB_API_KEY
    PYTHONPATH=src:. python scripts/verifier_smoke.py
"""

from __future__ import annotations

import sys

from agents.verifier import Verifier
from rollout.sandbox_client import LocalSandbox

# The known ground truth: values sum to 42.
_CSV = "value\n10\n12\n20\n"
_TASK = (
    "Read data.csv in the current working directory. Sum the 'value' column and "
    "report the total."
)


def _seed_sandbox() -> LocalSandbox:
    """Fresh LocalSandbox with data.csv written into its persistent workdir."""
    sb = LocalSandbox(timeout=30)
    # LocalSandbox runs each snippet in its persistent workdir (cwd), so writing
    # via run_code lands the file where read_file('./data.csv') will find it.
    code = "open('data.csv','w').write(%r)\nprint('seeded')" % _CSV
    res = sb.run_code(code)
    if not res.ok:
        raise RuntimeError(f"failed to seed sandbox: {res.stderr}")
    return sb


def _agent_traj(claimed_sum: int) -> str:
    return (
        "[user] Read data.csv and sum the 'value' column.\n"
        f"[assistant] I read data.csv and computed the total of the value column: {claimed_sum}."
    )


def _run_fixture(name: str, claimed_sum: int) -> dict:
    sb = _seed_sandbox()
    try:
        v = Verifier(max_tool_rounds=4)
        return v.verify(task=_TASK, trajectory=_agent_traj(claimed_sum), sandbox=sb)
    finally:
        sb.kill()


def main() -> int:
    print("=== Verifier closed-loop smoke (LocalSandbox + real judge) ===")
    print(f"task: {_TASK}")
    print(f"ground truth sum(value) = 42\n")

    a = _run_fixture("A_wrong", 100)
    print(f"[A agent claims 100]  verified={a.get('verified')} correctness={a.get('correctness')}")
    print(f"    reason: {a.get('correctness_reason')}")

    b = _run_fixture("B_correct", 42)
    print(f"[B agent claims 42 ]  verified={b.get('verified')} correctness={b.get('correctness')}")
    print(f"    reason: {b.get('correctness_reason')}")

    print("\n=== verdict ===")
    if not (a.get("verified") and b.get("verified")):
        print("FAIL: verifier did not produce a grounded verdict (check judge key / connectivity).")
        return 1
    ca, cb = float(a["correctness"]), float(b["correctness"])
    ok = ca < 0.4 and cb > 0.6 and ca < cb
    print(f"A.correctness={ca:.3f}  B.correctness={cb:.3f}  (want A<0.4, B>0.6, A<B)")
    if ok:
        print("PASS: closed loop verified — wrong answer scored low, correct answer scored high.")
        return 0
    print("FAIL: scores did not separate as expected.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
