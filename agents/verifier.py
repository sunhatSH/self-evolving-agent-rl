"""Execution-grounded correctness verifier (the "verifier-agent").

== Why this exists ==

The plain correctness judge (``trainer.model_reward``) grades correctness from the
agent's final TEXT only: no answer_key (removed 2026-09-01, the model-generated GT
was unreliable) and no tool-return values in the trajectory it reads. For data-
analysis tasks (read source CSV/XLSX -> produce a report) it therefore cannot verify
any number, so it invents deductions -- measured: ~84% of low correctness scores in
the cl2r_baseline run were hallucinated ("miscounts X", "INC-9030 doesn't exist")
against source data the judge never saw. correctness collapsed 0.35 -> 0.14 the day
answer_key was removed.

== What it is ==

The verifier is the SAME correctness judge, but handed TOOLS to investigate the LIVE
sandbox at scoring time (the sandbox is still alive in ``_score_all_slots``, before
``pool.destroy_all()``). It is a single LLM in a tool-use loop -- NOT two roles:

    task + trajectory + diff  --> judge LLM
    judge: "to grade this I must verify <these values>"  --> tool call
    harness runs it in the LIVE sandbox (read_file / list_dir / run_check)
    result --> judge  (repeat up to max_rounds)
    judge scores correctness from the REAL evidence it gathered

``run_check`` (execute Python in the sandbox) is the tool that turns a reader into a
verifier: the judge recomputes the expected answer from the real source data instead
of trusting the agent's claims.

== Design ==

Mirrors ``agents.observer.Observer`` deliberately: same package, same config-resolved
client, same tool-use loop skeleton, same "LLM/parse failure -> degrade, never crash
the session" contract. It reuses the observer's sandbox probes (``_read_file_probe`` /
``_list_dir_probe`` / ``_run_json_probe``) and the reward module's robust JSON parser
(``parse_judge_output``) so there is one implementation of each, not two.

On ANY failure (LLM error, truncation, parse failure, no sandbox, all rounds spent
with no verdict) it returns ``verified=False`` and the caller keeps the plain judge's
correctness -- the verifier is a strict IMPROVEMENT layer, it never regresses the
existing path or adds a crash surface.
"""

from __future__ import annotations

import json
from collections.abc import Sequence
from typing import Any

from agents.base import ChatClient, TruncatedOutputError
from agents.observer import (
    ReadOnlySandbox,
    _list_dir_probe,
    _read_file_probe,
    _run_json_probe,
    flatten_trajectory,
)
from agents.prompts import VERIFIER_TOOLS, build_verifier_prompt


def _read_file_probe_8k(path: str) -> str:
    """Like observer's read-file probe but 8 KB (verifier reads source data, not excerpts)."""
    return (
        "import json\n"
        f"PATH={json.dumps(path)}\n"
        "try:\n"
        "    with open(PATH) as f:\n"
        "        data=f.read(8192)\n"
        "    print(json.dumps({'path': PATH, 'content': data, 'truncated': len(data)>=8192}))\n"
        "except Exception as e:\n"
        "    print(json.dumps({'path': PATH, 'error': str(e)}))\n"
    )


def _execute_verifier_tool(tool_name: str, tool_args: dict, sandbox: ReadOnlySandbox | None) -> str:
    """Execute one verifier tool call against the LIVE sandbox; return a string result.

    Never raises: a failed tool returns a JSON error string the model can react to
    (mirrors ``_execute_observer_tool``). ``run_check`` runs arbitrary Python via the
    backend-agnostic ``run_code`` and returns stdout/stderr/ok.
    """
    if sandbox is None:
        return json.dumps({"error": "no sandbox available"})

    if tool_name == "read_file":
        path = tool_args.get("path", ".")
        result = _run_json_probe(sandbox, _read_file_probe_8k(path))
        return json.dumps(result, ensure_ascii=False) if result else json.dumps({"error": "read failed"})

    if tool_name == "list_dir":
        path = tool_args.get("path", ".")
        result = _run_json_probe(sandbox, _list_dir_probe(path))
        return json.dumps(result, ensure_ascii=False) if result else json.dumps({"error": "list failed"})

    if tool_name == "run_check":
        code = tool_args.get("code", "")
        if not code:
            return json.dumps({"error": "run_check requires 'code'"})
        try:
            res = sandbox.run_code(code)
        except Exception as e:  # noqa: BLE001 -- verification must never crash the session
            return json.dumps({"error": f"execution failed: {e}"})
        out = (getattr(res, "stdout", "") or "")[:8192]
        err = (getattr(res, "stderr", "") or "")[:2048]
        return json.dumps(
            {"stdout": out, "stderr": err, "ok": bool(getattr(res, "ok", False))},
            ensure_ascii=False,
        )

    return json.dumps({"error": f"unknown tool: {tool_name}"})


def _resolve_verifier_client() -> ChatClient:
    """Resolve the verifier LLM: reuse the frozen REWARD judge endpoint (agents.yaml).

    The verifier IS the correctness judge, so it shares the reward model / endpoint
    (config-first via ``resolve_judge``, then REWARD_* env fallback). Returns an
    ``OpenAIChatClient`` (which supports ``chat_with_tools``).
    """
    from agents.base import OpenAIChatClient

    try:
        from agents.config import resolve_judge

        ep = resolve_judge()
        return OpenAIChatClient(
            base_url=ep.base_url, model=ep.model, api_key=ep.api_key, temperature=ep.temperature
        )
    except RuntimeError:
        pass  # fall through to env-only path
    import os

    base = os.environ.get("REWARD_API_BASE")
    model = os.environ.get("REWARD_MODEL")
    if not base or not model:
        raise RuntimeError(
            "verifier not configured: set the reward judge in configs/agents.yaml or "
            "REWARD_API_BASE + REWARD_MODEL env."
        )
    return OpenAIChatClient(
        base_url=base, model=model, api_key=os.environ.get("REWARD_API_KEY", "sk-local"), temperature=0.0
    )


class Verifier:
    """Execution-grounded correctness judge with live-sandbox tool use.

    ``verify`` returns ``{correctness, correctness_reason, verified}``:
      - ``verified=True``  -> a grounded verdict; caller SHOULD use ``correctness``.
      - ``verified=False`` -> the verifier could not produce a grounded verdict
        (no sandbox / LLM error / truncation / parse failure / rounds exhausted);
        caller keeps the plain judge's correctness. ``correctness`` is 0.0 here and
        MUST NOT be used.
    """

    def __init__(
        self,
        client: ChatClient | None = None,
        *,
        max_tokens: int = 4096,
        max_tool_rounds: int = 4,
    ):
        self._client = client
        self._max_tokens = max_tokens
        self._max_tool_rounds = max_tool_rounds

    @property
    def client(self) -> ChatClient:
        if self._client is None:
            self._client = _resolve_verifier_client()
        return self._client

    def verify(
        self,
        *,
        task: str,
        trajectory: Sequence[dict[str, Any]] | str,
        sandbox: ReadOnlySandbox | None,
        state_diff: str = "",
    ) -> dict[str, Any]:
        """Grade correctness by investigating the live sandbox; degrade on any failure.

        Args:
            task: what the agent was asked (the seed query).
            trajectory: the agent's messages (or flattened text) -- its CLAIMS, to be
                verified, not trusted.
            sandbox: the LIVE sandbox the agent worked in (source data still present).
            state_diff: the observer's auto-collected before/after diff (starting hint).

        Returns ``{correctness: float, correctness_reason: str, verified: bool}``.
        """
        if sandbox is None:
            return {"correctness": 0.0, "correctness_reason": "no sandbox", "verified": False}
        traj_text = flatten_trajectory(trajectory)
        # Timing + call counters (perf audit: how much wall-time / how many LLM
        # round-trips + run_check executions each verification costs). Written into
        # the returned dict so _apply_verifier can log + persist them.
        import time as _time

        stats = {"n_llm_calls": 0, "n_tool_calls": 0, "n_run_check": 0}
        _t0 = _time.perf_counter()

        def _stamp(res: dict) -> dict:
            res["verify_secs"] = round(_time.perf_counter() - _t0, 3)
            res["n_llm_calls"] = stats["n_llm_calls"]
            res["n_tool_calls"] = stats["n_tool_calls"]
            res["n_run_check"] = stats["n_run_check"]
            return res

        try:
            return _stamp(
                self._tool_use_loop(
                    task=task, trajectory=traj_text, sandbox=sandbox, state_diff=state_diff, stats=stats
                )
            )
        except TruncatedOutputError as e:
            return _stamp({"correctness": 0.0, "correctness_reason": f"truncated: {e}", "verified": False})
        except Exception as e:  # noqa: BLE001 -- verification must never crash the session
            return _stamp({"correctness": 0.0, "correctness_reason": f"verifier error: {e}", "verified": False})

    def _tool_use_loop(
        self, *, task: str, trajectory: str, sandbox: ReadOnlySandbox | None, state_diff: str, stats: dict
    ) -> dict[str, Any]:
        """Run the judge with tool-use until it outputs the correctness JSON.

        A client without ``chat_with_tools`` degrades to a single-shot ungrounded
        call (still parsed, but ``verified`` only when a verdict is extracted).
        ``stats`` is mutated in place with LLM/tool/run_check call counts (perf audit).
        """
        from trainer.model_reward import parse_judge_output

        messages = build_verifier_prompt(task=task, trajectory=trajectory, state_diff=state_diff)
        client = self.client
        has_tools = hasattr(client, "chat_with_tools")

        def _finalize(content: str) -> dict[str, Any] | None:
            """Parse a correctness verdict; None when no verdict JSON was present."""
            verdict, parsed = parse_judge_output(content, dimensions=("correctness",))
            if not parsed:
                return None
            return {
                "correctness": float(verdict.get("correctness", 0.0)),
                "correctness_reason": str(verdict.get("correctness_reason", verdict.get("reason", ""))),
                "verified": True,
            }

        for _round in range(self._max_tool_rounds):
            stats["n_llm_calls"] += 1
            if has_tools:
                msg = client.chat_with_tools(messages, tools=VERIFIER_TOOLS, max_tokens=self._max_tokens)
            else:
                content = client.chat(messages, max_tokens=self._max_tokens)
                msg = {"role": "assistant", "content": content}
            messages.append(msg)

            tool_calls = msg.get("tool_calls") or []
            if not tool_calls:
                # No tool call -> this should be the final correctness JSON.
                result = _finalize(msg.get("content", "") or "")
                if result is not None:
                    return result
                # Not a verdict: nudge once for the JSON, then stop.
                break

            for tc in tool_calls:
                fn = tc.get("function", {})
                tool_name = fn.get("name", "")
                stats["n_tool_calls"] += 1
                if tool_name == "run_check":
                    stats["n_run_check"] += 1
                try:
                    tool_args = json.loads(fn.get("arguments", "{}"))
                except (json.JSONDecodeError, TypeError):
                    tool_args = {}
                tool_result = _execute_verifier_tool(tool_name, tool_args, sandbox)
                messages.append(
                    {"role": "tool", "tool_call_id": tc.get("id", ""), "content": tool_result}
                )

        # Rounds exhausted (or a non-verdict final): ask once for the JSON, no tools.
        messages.append(
            {
                "role": "user",
                "content": "Output the correctness JSON now based on the evidence gathered. "
                'ONLY: {"correctness": <0~1>, "correctness_reason": "<why, with evidence>"}.',
            }
        )
        stats["n_llm_calls"] += 1
        if has_tools:
            final_msg = client.chat_with_tools(messages, max_tokens=self._max_tokens)
            content = final_msg.get("content", "") or ""
        else:
            content = client.chat(messages, max_tokens=self._max_tokens)
        result = _finalize(content)
        if result is not None:
            return result
        return {"correctness": 0.0, "correctness_reason": "no verdict produced", "verified": False}
