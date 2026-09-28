"""Sandbox-side hermes trajectory capture (方案3 P2).

This script runs INSIDE the sandbox (where hermes is pip-installed as an editable
package, so ``import run_agent`` works — pyproject py-modules lists run_agent).
It patches ``AIAgent.run_conversation`` to stash the STRUCTURED result (messages
with tool_calls, POST-compression = train/infer consistent) and ``delegate_tool.
_run_single_child`` to harvest each sub-agent (delegate_task) child trajectory
hermes spawns on its own. It reads {query, conversation_history} from a JSON input
file and writes {messages, children, ok, error} to an output file.

Contract (input file → stdout JSON, probe-style, so the actor reuses the same
read-back path as observer probes; no data crosses the dev process):
    python _hermes_capture.py <input.json>
    input.json  = {"query": str, "history": [msg...], "max_iterations": int}
    stdout      = a single line ``__CAPTURE__<json>`` where <json> =
                  {"messages": [...], "children": [{task_index,goal,messages}],
                   "ok": bool, "error": str}
    (the marker prefix lets the actor find the payload even if hermes prints noise.)

hermes model/base/key come from the sandbox's ~/.hermes/config.yaml (already written
by _write_hermes_config) + AGENT_MODEL_* env, so keys never leave the sandbox.

⚠️ Version note: the sandbox image pins HERMES_VERSION (e.g. v2026.6.5). The
AIAgent(...) kwargs and run_conversation signature below match the reference
source; if a pinned version differs, this script must be validated in-sandbox
(P2 smoke) and adjusted. It fails LOUD (writes error to output) rather than
silently producing a degraded trajectory.
"""

import json
import os
import sys
import threading

# ---- child (sub-agent) capture sink: run_token -> list[child cap] ----
_CHILD_SINK = {}
_CHILD_SINK_LOCK = threading.Lock()
_PATCHED = False


def _install_patches():
    """Wrap run_conversation (stash structured result) + _build_assistant_message
    (harvest reasoning_content per API response — the final result.messages
    history strips it) + _run_single_child (harvest delegated child traj). Idempotent."""
    global _PATCHED
    if _PATCHED:
        return
    import run_agent

    # ── reasoning_content capture ────────────────────────────────────────
    # DeepSeek/thinking models return reasoning_content in the API response,
    # but hermes' final result.messages strips it. We intercept the OpenAI SDK
    # `Completions.create` and accumulate reasoning per API call (streaming:
    # sum delta.reasoning_content across chunks; non-streaming: read directly).
    # Reasonings are collected in call order, then re-attached to assistant
    # messages in result.messages (same order) in _wrapped_run.
    #
    # GPT/Claude 系列还返回 reasoning_signature（验证思考完整性的签名），同样
    # 从 delta/model_extra 捕获并按序回挂到 assistant 消息。
    _REASONING_ORDER: list[str] = []   # one entry per assistant API response, in order
    _SIGNATURE_ORDER: list[str] = []   # reasoning_signature per API response
    _REASONING_LOCK = threading.Lock()

    def _extract_rc_from_message(msg_obj) -> str:
        """Read reasoning_content from a non-streaming ChatCompletion message."""
        rc = getattr(msg_obj, "reasoning_content", None)
        if rc is None and hasattr(msg_obj, "model_extra"):
            me = msg_obj.model_extra or {}
            rc = me.get("reasoning_content")
        return rc or ""

    def _extract_rs_from_message(msg_obj) -> str:
        """Read reasoning_signature from a non-streaming ChatCompletion message."""
        rs = getattr(msg_obj, "reasoning_signature", None)
        if rs is None and hasattr(msg_obj, "model_extra"):
            me = msg_obj.model_extra or {}
            rs = me.get("reasoning_signature")
        return rs or ""

    def _extract_rs_from_delta(delta) -> str:
        rs = getattr(delta, "reasoning_signature", None)
        if rs is None and hasattr(delta, "model_extra"):
            rs = (delta.model_extra or {}).get("reasoning_signature")
        return rs or ""

    try:
        from openai.resources.chat.completions import Completions

        _orig_create = Completions.create

        # Claude 系列（claude-4.6-opus 等，走原生 Anthropic 通道，id 不带 anthropic/ 前缀）
        # 默认不吐 reasoning_content，必须显式带 thinking 参数才产生思考。DeepSeek 默认吐、
        # 不需要；gpt 系列不认该参数。故仅对 claude 注入 thinking:{enabled,budget_tokens}，
        # 让 claude 采集也带思考（数据质量对齐 ds 且更高）。budget < max_tokens 以留出答案预算。
        #
        # 注意：thinking 是 Anthropic 原生参数，OpenAI SDK 的 create() 不接受顶层 kwarg
        # （会 TypeError: unexpected keyword argument 'thinking'），必须放 extra_body 透传。
        def _maybe_inject_thinking(k):
            model = str(k.get("model", "")).lower()
            if "claude" not in model:
                return
            eb = k.get("extra_body") or {}
            if "thinking" in eb or "reasoning_effort" in eb or "thinking" in k:
                return  # 调用方已显式指定，尊重之
            max_tok = k.get("max_tokens")
            budget = 4096
            if isinstance(max_tok, int) and max_tok > 0:
                budget = max(1024, min(budget, max_tok - 512))  # 留 ≥512 给答案
            elif not isinstance(max_tok, int) or max_tok <= budget:
                # thinking 要求 max_tokens > budget_tokens；未设或过小则抬高
                k["max_tokens"] = budget + 2048
            eb["thinking"] = {"type": "enabled", "budget_tokens": budget}
            k["extra_body"] = eb

        def _patched_create(self, *a, **k):
            _maybe_inject_thinking(k)
            resp = _orig_create(self, *a, **k)
            if k.get("stream"):
                acc: list[str] = []
                sig_acc: list[str] = []

                def _gen():
                    for chunk in resp:
                        try:
                            for ch in getattr(chunk, "choices", []) or []:
                                delta = getattr(ch, "delta", None)
                                if delta is None:
                                    continue
                                rc = getattr(delta, "reasoning_content", None)
                                if rc is None and hasattr(delta, "model_extra"):
                                    rc = (delta.model_extra or {}).get("reasoning_content")
                                if rc:
                                    acc.append(rc)
                                rs = _extract_rs_from_delta(delta)
                                if rs:
                                    sig_acc.append(rs)
                        except Exception:
                            pass
                        yield chunk
                    # record accumulated reasoning for this API call (may be "")
                    with _REASONING_LOCK:
                        _REASONING_ORDER.append("".join(acc))
                        _SIGNATURE_ORDER.append("".join(sig_acc))

                return _gen()
            else:
                # non-streaming: read reasoning + signature directly, record in order
                try:
                    msg0 = resp.choices[0].message
                    with _REASONING_LOCK:
                        _REASONING_ORDER.append(_extract_rc_from_message(msg0))
                        _SIGNATURE_ORDER.append(_extract_rs_from_message(msg0))
                except Exception:
                    pass
                return resp

        Completions.create = _patched_create
    except Exception:
        pass  # openai SDK layout changed → reasoning stays empty, not fatal

    _orig_run = run_agent.AIAgent.run_conversation

    def _wrapped_run(self, *a, **k):
        result = _orig_run(self, *a, **k)
        try:
            msgs = (result or {}).get("messages") if isinstance(result, dict) else None
            # Re-attach captured reasoning to assistant messages, in order.
            if msgs:
                with _REASONING_LOCK:
                    order = list(_REASONING_ORDER)
                    sig_order = list(_SIGNATURE_ORDER)
                    _REASONING_ORDER.clear()
                    _SIGNATURE_ORDER.clear()
                assistants = [m for m in msgs
                              if isinstance(m, dict) and m.get("role") == "assistant"]
                for m, rc in zip(assistants, order):
                    if rc and rc.strip() and not (m.get("reasoning_content") or "").strip():
                        m["reasoning_content"] = rc
                for m, rs in zip(assistants, sig_order):
                    if rs and rs.strip() and not (m.get("reasoning_signature") or "").strip():
                        m["reasoning_signature"] = rs
            self._cap = {
                "messages": msgs,
                "completed": (result or {}).get("completed") if isinstance(result, dict) else None,
                "partial": (result or {}).get("partial") if isinstance(result, dict) else None,
                "error": (result or {}).get("error") if isinstance(result, dict) else None,
                "api_calls": (result or {}).get("api_calls") if isinstance(result, dict) else None,
                "tools": getattr(self, "tools", None),
                "system_prompt": getattr(self, "_cached_system_prompt", None),
                "ephemeral_system_prompt": getattr(self, "ephemeral_system_prompt", None),
                "model": getattr(self, "model", None),
            }
        except Exception:
            self._cap = None
        return result

    run_agent.AIAgent.run_conversation = _wrapped_run

    # ── 工具名别名规范化 ────────────────────────────────────────────────────
    # 根因(2026-09-23 startup 训练): Qwen 基座凭预训练记忆调 bash/run/python 等
    # 通用 agent 工具名, 但 hermes 真名是 terminal/execute_code 等 → 模型调用 undefined
    # (日志 256 次 undefined, 主导 rollout 失败). 工具 schema 注入本身正常(已验证
    # enabled_toolsets=None 时 32 工具含 terminal/execute_code/read_file/...).
    # 修法: 在工具分发入口把高频误名映射回 hermes 真名, 让惯用名也能命中.
    # (别名仅覆盖有把握的同义映射; 长尾乱码名 execu/ter/pad 等交给失败案例自演化.)
    _TOOL_ALIASES = {
        # 执行 shell 命令 → terminal
        "bash": "terminal", "run": "terminal", "run_command": "terminal",
        "run_shell_command": "terminal", "shell": "terminal", "shell_command": "terminal",
        "run_in_shell": "terminal", "execute_bash": "terminal", "command": "terminal",
        # 跑代码 → execute_code
        "python": "execute_code", "run_python": "execute_code", "run_code": "execute_code",
        "execute": "execute_code", "exec": "execute_code", "code_execution": "execute_code",
        # 文件操作(hermes 真名已存在, 补常见变体)
        "create_file": "write_file", "update_file": "write_file", "rewrite_file": "write_file",
        "delete_file": "write_file", "remove_file": "write_file",
        "list_files": "search_files", "list_files_in_directory": "search_files",
        "ls": "search_files", "list_dir": "search_files",
        # 技能
        "skill_list": "skills_list",
    }
    try:
        _orig_invoke = run_agent.AIAgent._invoke_tool

        def _aliased_invoke(self, function_name, function_args, *a, **k):
            # ① tool_search 路由: 模型不确定工具名时调它, 返回全部可用工具的名字+用途,
            #    让模型据此改调正确工具. 覆盖 hermes 原生 tool_search 覆盖不到的 core 工具.
            if function_name == "tool_search":
                avail = [t.get("function", {}) for t in (getattr(self, "tools", None) or [])
                         if isinstance(t, dict)]
                lines = []
                for f in avail:
                    nm = f.get("name")
                    if not nm or nm == "tool_search":
                        continue
                    desc = (f.get("description") or "").strip().splitlines()
                    lines.append(f"- {nm}: {desc[0] if desc else ''}"[:160])
                q = ""
                if isinstance(function_args, dict):
                    q = str(function_args.get("query") or function_args.get("q") or "").strip()
                hint = f"(query: {q})\n" if q else ""
                return (
                    "可用工具清单(请从中选择正确的工具名再调用; 常见对应: "
                    "执行 shell 命令→terminal, 跑代码→execute_code, "
                    "读文件→read_file, 写文件→write_file, 搜文件→search_files):\n"
                    + hint + "\n".join(lines)
                )
            # ② 别名兜底: 模型直接调惯用名(bash/run/python...) → 映射回 hermes 真名.
            real = _TOOL_ALIASES.get(function_name)
            if real is not None:
                avail = {t.get("function", {}).get("name")
                         for t in (getattr(self, "tools", None) or [])
                         if isinstance(t, dict)}
                if not avail or real in avail:
                    function_name = real
            return _orig_invoke(self, function_name, function_args, *a, **k)

        run_agent.AIAgent._invoke_tool = _aliased_invoke
    except Exception:
        pass  # hermes 版本无 _invoke_tool → 跳过别名, 不致命

    # ── 注入 tool_search 工具到模型可见列表 ─────────────────────────────────
    # patch model_tools.get_tool_definitions: 在返回的工具 schema 末尾追加 tool_search,
    # 让模型看到"不确定工具名时可调 tool_search 查"这个入口(hermes 原生 tool_search
    # 只覆盖 MCP/plugin 工具, 不含 core; 这里自造一个覆盖全部工具的版本).
    _TOOL_SEARCH_SCHEMA = {
        "type": "function",
        "function": {
            "name": "tool_search",
            "description": (
                "查询当前可用的工具清单及用途。当你不确定某个操作该用哪个工具、"
                "或调用工具报 undefined 时, 先调用本工具查看正确的工具名, 再改调该工具。"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "想做的操作或意图, 如 'run shell command'"}
                },
                "required": [],
            },
        },
    }
    try:
        import model_tools as _mt

        _orig_get_defs = _mt.get_tool_definitions

        def _get_defs_with_search(*a, **k):
            defs = _orig_get_defs(*a, **k)
            try:
                names = {d.get("function", {}).get("name") for d in defs if isinstance(d, dict)}
                if "tool_search" not in names:
                    defs = list(defs) + [_TOOL_SEARCH_SCHEMA]
            except Exception:
                pass
            return defs

        _mt.get_tool_definitions = _get_defs_with_search
        # run_agent 模块级 re-export 也要覆盖(line 137 `from model_tools import get_tool_definitions`)
        if hasattr(run_agent, "get_tool_definitions"):
            run_agent.get_tool_definitions = _get_defs_with_search
    except Exception:
        pass  # 无 model_tools → 跳过注入, 别名兜底仍在


    try:
        from tools import delegate_tool

        _orig_child = delegate_tool._run_single_child

        def _wrapped_child(task_index, goal, child=None, parent_agent=None, **kw):
            ret = _orig_child(task_index, goal, child, parent_agent, **kw)
            try:
                token = getattr(parent_agent, "_run_token", None)
                cap = getattr(child, "_cap", None)
                if token is not None and cap is not None:
                    with _CHILD_SINK_LOCK:
                        sink = _CHILD_SINK.get(token)
                    if sink is not None:
                        sink.append({"task_index": task_index, "goal": goal, "cap": cap})
            except Exception:
                pass
            return ret

        delegate_tool._run_single_child = _wrapped_child
    except Exception:
        # delegate tool absent in this hermes build -> single-agent only, fine.
        pass

    _PATCHED = True


def _child_messages(children_caps):
    """Flatten harvested child caps -> [{task_index, goal, messages, system_prompt, base_system_prompt, tools}]."""
    out = []
    for c in children_caps or []:
        cap = c.get("cap") or {}
        # Child: ephemeral_system_prompt = delegated task + context (the "real" instruction).
        # _cached_system_prompt = hermes identity + tool enforcement (the "base").
        row = {
            "task_index": c.get("task_index"),
            "goal": c.get("goal"),
            "messages": cap.get("messages") or [],
            "system_prompt": cap.get("ephemeral_system_prompt"),
            "base_system_prompt": cap.get("system_prompt"),
            "tools": cap.get("tools"),
        }
        out.append(row)
    return out


def _resolve_runtime(name: str, model: str) -> dict:
    """Resolve endpoint via hermes' OWN oneshot resolver (the working path).

    Returns a dict with base_url/api_key/provider/api_mode (whatever the resolver
    provides). Falls back to reading providers.<name> from ~/.hermes/config.yaml,
    then to {} (caller then uses env). Never raises."""
    # 1. hermes' own resolver — identical to `hermes chat -q` oneshot.
    try:
        from hermes_cli.runtime_provider import resolve_runtime_provider

        rt = resolve_runtime_provider(requested=name, target_model=model or None)
        if isinstance(rt, dict) and rt.get("base_url"):
            return rt
    except Exception:
        pass
    # 2. plain config.yaml providers.<name> read.
    try:
        import yaml

        cfg = yaml.safe_load(open(os.path.expanduser("~/.hermes/config.yaml"), encoding="utf-8")) or {}
        prov = ((cfg.get("providers") or {}).get(name)) or {}
        if prov.get("base_url"):
            return {"base_url": str(prov["base_url"]), "api_key": str(prov.get("api_key") or ""),
                    "provider": name}
    except Exception:
        pass
    return {}


def main() -> None:
    in_path = sys.argv[1]
    result_out = {"messages": [], "children": [], "ok": False, "error": ""}
    try:
        spec = json.load(open(in_path, encoding="utf-8"))
        query = spec["query"]
        max_iter = int(spec.get("max_iterations", 30))
        session_id = spec.get("session_id") or None

        _install_patches()
        import inspect

        import run_agent

        # Resolve the endpoint the SAME way the working `hermes chat -q` (oneshot)
        # Model priority: ~/.hermes/config.yaml top-level `model` (written by
        # _write_hermes_config with the caller's --actor-model) FIRST, then the
        # sandbox-injected AGENT_MODEL_NAME. Reading env first silently ran every
        # request as runtime.env's model (openai/gpt-5.5) regardless of
        # --actor-model → thinking models never engaged, reasoning_content empty.
        model = ""
        try:
            import yaml as _yaml
            _cfg = _yaml.safe_load(
                open(os.path.expanduser("~/.hermes/config.yaml"), encoding="utf-8")) or {}
            model = str(_cfg.get("model") or "")
        except Exception:
            pass
        if not model:
            model = os.environ.get("AGENT_MODEL_NAME", "")
        runtime = _resolve_runtime("agent", model)
        base = runtime.get("base_url") or os.environ.get("AGENT_MODEL_BASE", "")
        key = runtime.get("api_key") or os.environ.get("AGENT_MODEL_KEY", "")

        # Version-robust: only pass kwargs the sandbox's hermes AIAgent accepts.
        want = {
            "base_url": base or None,
            "api_key": key or None,
            "provider": runtime.get("provider") or "agent",
            "api_mode": runtime.get("api_mode"),
            "model": model,
            "max_iterations": max_iter,
            "save_trajectories": False,
            "quiet_mode": True,
            "persist_session": True,
            "skip_memory": True,
            "skip_context_files": True,
        }
        if session_id:
            want["session_id"] = session_id
        try:
            sig_params = set(inspect.signature(run_agent.AIAgent.__init__).parameters)
        except (TypeError, ValueError):
            sig_params = set(want)  # fall back to trying all if introspection fails
        kwargs = {k: v for k, v in want.items() if k in sig_params and v is not None}
        agent = run_agent.AIAgent(**kwargs)
        run_token = f"capture/{os.getpid()}"
        agent._run_token = run_token
        with _CHILD_SINK_LOCK:
            _CHILD_SINK[run_token] = []

        # Session resume: pass session_id so hermes loads its own persistent state.
        # conversation_history is NOT passed — hermes manages its own context.
        res = agent.run_conversation(
            query, task_id=session_id or run_token
        )

        cap = getattr(agent, "_cap", None) or {}
        with _CHILD_SINK_LOCK:
            child_caps = _CHILD_SINK.pop(run_token, [])

        # Messages from result (hermes stores system prompt separately — messages
        # start with user, NOT system). system_prompt and tools are surfaced as
        # independent fields (matching nairong/荣磊's schema) so downstream can
        # reassemble the full system context at training time.
        msgs = cap.get("messages") or (res or {}).get("messages") or []
        # Rename hermes' "reasoning" to "reasoning_content" + parse tool_calls arguments.
        for _m in msgs:
            if _m.get("role") == "assistant" and "reasoning" in _m and "reasoning_content" not in _m:
                _m["reasoning_content"] = _m.pop("reasoning")
            for _tc in _m.get("tool_calls") or []:
                _args = _tc.get("function", {}).get("arguments")
                if isinstance(_args, str):
                    try:
                        _tc["function"]["arguments"] = json.loads(_args)
                    except (json.JSONDecodeError, TypeError):
                        pass
        result_out["messages"] = msgs
        result_out["system_prompt"] = cap.get("system_prompt") or ""
        result_out["ephemeral_system_prompt"] = cap.get("ephemeral_system_prompt") or ""
        result_out["tools"] = cap.get("tools") or []
        result_out["api_calls"] = cap.get("api_calls") or (res or {}).get("api_calls", 0)
        result_out["partial"] = cap.get("partial") or (res or {}).get("partial", False)
        result_out["children"] = _child_messages(child_caps)
        result_out["ok"] = bool((res or {}).get("completed", True)) and not (res or {}).get("error")
        result_out["error"] = str((res or {}).get("error") or "")
        # Surfacing session_id so the caller can pass it back for the next turn.
        # hermes may return it in the result dict OR as an agent attribute.
        _sid = (
            (res or {}).get("session_id")
            or getattr(agent, "session_id", None)
            or session_id
        )
        result_out["session_id"] = _sid
    except Exception as exc:  # fail loud into the output payload
        result_out["ok"] = False
        result_out["error"] = f"{type(exc).__name__}: {exc}"
    finally:
        # Marker prefix so the actor can extract the payload past any hermes noise.
        sys.stdout.write("__CAPTURE__" + json.dumps(result_out, ensure_ascii=False) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
