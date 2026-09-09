"""VerifierHook：执行式 correctness 取证(模型出题 → 沙箱执行 → 证据回流 judge).

== 为什么(接 F17/F18)==

去 answer_key 后,correctness judge 只读 agent 自述文本、无源数据 → 对数据分析/事件
报告类任务系统性"编造真值"扣分(实测:judge 声称 label 真值 24/19/29,而它读到的
observer_report 里 `24` 出现 0 次)。ObserverDiffHook 给了 judge "agent 产出了什么"
(diff),但没给"正确答案是什么"。本 hook 补这一环:趁沙箱还活着,让模型看着
[任务+产出+源文件] 出一道可执行校验题,在沙箱里真跑,把"重算出的真值 vs agent 的值"
写进 reward_info,judge 据此判分 —— 不再脑补。

== 三段式,全在 run() 内(沙箱活着,hook.run 在 sandbox.close 之前)==

  ① 采集素材(确定性):ctx.instruction(任务)+ ObserverDiffHook 已写的 observer_report
     (产出文件含内容)+ sandbox.exec 列 ./ 与 ./inputs 下源文件清单(小 head)。
  ② 出题(1 次 LLM 调用,async httpx,非重循环):build_check_gen_prompt → 让 reward judge
     模型输出一段自包含 Python 校验脚本(读源数据 recompute 真值、比对 agent 产出)。
  ③ 执行(确定性):把脚本 write_file 进沙箱、python3 跑,取 stdout/stderr。
  ④ 写证据:state.reward_info["verifier_report"] = {check_code, stdout, ok, ...}。

judge 侧(compute_score,跨进程、沙箱已死):verifier_report 经现成通路
(reward_info → omni extra_info → compute_score)进 correctness rubric。

== 约束 ==

- 只在 VERIFIER_ENABLE truthy 时运行;否则整个 hook no-op(零影响、零成本)。
- best-effort:LLM / exec / 解析任一失败 → 写空/降级,绝不抛(取证不能崩会话)。
- 单次 LLM(出题)+ 单次沙箱执行,不做 tool-use 重循环(那会拖垮 rollout 吞吐)。
- hook 拿不到 agent 的 message 轨迹(在 gateway TrajectoryBuffer);出题基于产出+diff+任务,
  这对"产出对不对"够用(correctness 要的就是核对产出)。
- ⚠️ 本机无 e2b + 无 verl worker,端到端靠集群实测;逻辑靠单测(mock async sandbox + judge)。
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from typing import Any

try:
    from recipe_custom.agent.runners.hooks.base import AgentRunHook
except Exception:  # noqa: BLE001 -- recipe_custom absent off-cluster（单测/本机）

    class AgentRunHook(ABC):  # type: ignore[no-redef]
        """Fallback 基类（离集群无 recipe_custom 时可 import + 单测）。

        run 标 @abstractmethod,与真实基类一致——子类漏实现则实例化 TypeError,本机冒烟即抓
        (对齐 mkdir_deliverable_hook 的 2026-08-27 教训)。
        """

        run_on_agent_error = False

        async def prepare(self, sandbox: Any, ctx: Any, state: Any) -> None: ...

        @abstractmethod
        async def run(self, sandbox: Any, ctx: Any, state: Any) -> None: ...



def _verifier_enabled() -> bool:
    return os.environ.get("VERIFIER_ENABLE", "").strip().lower() in ("1", "true", "yes", "on")


# 源文件清单探针:列 ./ 与 ./inputs 下的文件 + 小 head(供出题参考,不 dump 全文)。
_SOURCE_LIST_PROBE = (
    "import os, json\n"
    "out = {}\n"
    "for base in ('.', './inputs'):\n"
    "    if not os.path.isdir(base):\n"
    "        continue\n"
    "    for root, dirs, files in os.walk(base):\n"
    "        dirs[:] = [d for d in dirs if d not in ('__pycache__', 'node_modules', '.git')]\n"
    "        for fn in files:\n"
    "            p = os.path.join(root, fn)\n"
    "            try:\n"
    "                sz = os.path.getsize(p)\n"
    "            except OSError:\n"
    "                continue\n"
    "            rec = {'size': sz}\n"
    "            if fn.lower().endswith(('.csv', '.txt', '.json', '.md', '.py', '.tsv')):\n"
    "                try:\n"
    "                    with open(p, errors='replace') as f:\n"
    "                        rec['head'] = f.read(500)\n"
    "                except Exception as e:\n"
    "                    rec['head_err'] = str(e)\n"
    "            out[p] = rec\n"
    "            if len(out) >= 100:\n"
    "                break\n"
    "print(json.dumps(out)[:20000])\n"
)


async def _exec_capture(sandbox: Any, command: str, timeout: int = 60) -> dict:
    """Run a shell command in the sandbox; return {stdout, stderr, ok}. Never raises."""
    try:
        res = await sandbox.exec(command, timeout=timeout)
        return {
            "stdout": (getattr(res, "stdout", "") or "")[:8192],
            "stderr": (getattr(res, "stderr", "") or "")[:2048],
            "ok": int(getattr(res, "exit_code", 1) or 0) == 0,
        }
    except Exception as e:  # noqa: BLE001 -- 取证绝不能崩会话
        return {"stdout": "", "stderr": f"{type(e).__name__}: {e}", "ok": False}


async def _gen_check_code(task: str, produced: str, source_files: str, timeout: int = 120) -> str:
    """ONE async LLM call: turn [task + produced + sources] into a Python check script.

    Uses the reward judge endpoint (resolve_judge). Returns "" on any failure.
    """
    try:
        from agents.config import resolve_judge
        from agents.prompts import build_check_gen_prompt, parse_check_code

        ep = resolve_judge()
        messages = build_check_gen_prompt(task=task, produced=produced, source_files=source_files)
        import httpx

        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.post(
                f"{ep.base_url.rstrip('/')}/chat/completions",
                json={
                    "model": ep.model,
                    "messages": messages,
                    "temperature": 0.0,
                    "max_tokens": int(os.environ.get("VERIFIER_GEN_MAX_TOKENS", "") or 2048),
                },
                headers={"Authorization": f"Bearer {ep.api_key}"},
            )
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        return parse_check_code(content or "")
    except Exception:  # noqa: BLE001 -- 出题失败 → 降级(无 verifier 证据),不崩会话
        return ""


class VerifierHook(AgentRunHook):
    """执行式验证 hook：模型出题 → 沙箱执行 → 证据写 reward_info["verifier_report"].

    与 ObserverDiffHook 并列注册(在其之后跑,好读它写的 observer_report)。
    VERIFIER_ENABLE 关时整个 run() no-op。run_on_agent_error=True:即便 agent 超时/OOM,
    也对"部分产出"做验证(与 ObserverDiffHook 一致的归因原则)。
    """

    run_on_agent_error = True

    async def prepare(self, sandbox: Any, ctx: Any, state: Any) -> None:  # noqa: ARG002
        # 无需 baseline:验证基于 agent 产出 + 源数据(源数据在 ./inputs,由 runner 注入)。
        return None

    async def run(self, sandbox: Any, ctx: Any, state: Any) -> None:
        if not _verifier_enabled():
            return
        print("[cl][verifier_hook] run start", flush=True)
        try:
            task = str(getattr(ctx, "instruction", "") or "")
            produced = str(state.reward_info.get("observer_report", "") or "")[:8000]

            # ① 源文件清单(确定性探针)
            import shlex

            probe_cmd = "python3 -c " + shlex.quote(_SOURCE_LIST_PROBE)
            src = await _exec_capture(sandbox, probe_cmd, timeout=60)
            source_files = src.get("stdout", "")

            # ② 出题(1 次 LLM)
            code = await _gen_check_code(task=task, produced=produced, source_files=source_files)
            if not code:
                # 降级:无可执行校验 → 留空 report,judge 回退纯文本判分。
                state.reward_info["verifier_report"] = {"status": "no_check_generated"}
                return

            # ③ 执行:脚本落盘再跑(避免超长 -c 的 shell 转义/长度问题)
            check_path = "/tmp/_cl_verifier_check.py"
            try:
                await sandbox.write_file(check_path, code)
            except Exception:  # noqa: BLE001 -- write 失败退回 -c
                check_path = None
            if check_path:
                run_res = await _exec_capture(sandbox, f"python3 {check_path}", timeout=120)
            else:
                run_res = await _exec_capture(
                    sandbox, "python3 -c " + shlex.quote(code), timeout=120
                )

            # ④ 写证据(judge 用)
            state.reward_info["verifier_report"] = {
                "status": "ok",
                "check_code": code[:4000],
                "check_stdout": run_res.get("stdout", ""),
                "check_stderr": run_res.get("stderr", "")[:1024],
                "check_ok": run_res.get("ok", False),
            }
        except Exception as e:  # noqa: BLE001 -- 取证绝不能崩会话
            state.reward_info["verifier_report"] = {"status": "error", "error": f"{type(e).__name__}: {e}"}


# ─────────────────────────────────────────────────────────────────────────────
# CLUSTER-TODO：
#  1. sandbox.write_file/exec 在 agentic-cl-sandbox 镜像可用(python3 + pandas/openpyxl)。
#  2. resolve_judge() 在 worker 进程能解析(TOKENHUB_API_KEY 已透传;VERIFIER_ENABLE 需加进
#     verl_runner.py 的 _passthrough)。
#  3. verifier_report 经 reward_info → omni extra_info → compute_score 读得到
#     (model_reward_omni 白名单已加 verifier_report;compute_score 已拼进 rubric)。
#  4. 出题 LLM 单次调用的延迟对 rollout 吞吐的影响(每条轨迹 +1 次判分级 LLM + 1 次 exec)。
# ─────────────────────────────────────────────────────────────────────────────
