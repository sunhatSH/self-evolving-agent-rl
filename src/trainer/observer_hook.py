"""阶段 F：observer diff 取证 hook（反 reward-hacking）+ answer_key 注入.

见 plan swift-juggling-toast 阶段 F。旧自写 rollout 的核心反 reward-hacking 机制：
observer 以【沙箱 before/after diff（含文件内容）】为 ground truth，判断 agent 是否真的
产出了交付物，而非只看模型自述。迁到 verl 原生 agent_loop 后，这条链断了（reward 只喂
模型 response 文本）。本 hook 恢复它。

机制（AgentRunHook 契约，recipe_custom/agent/runners/hooks/base.py）：
  · prepare(sandbox, ctx, state)：agent 跑之前，对沙箱工作区做只读 snapshot（baseline）。
  · run(sandbox, ctx, state)：sandbox 关之前，做 post snapshot + diff，把确定性证据写进
    state.reward_info["observer_report"]；并按 record_id 读 taskspecs_w3/<rid>/answer_key.json
    写进 reward_info["answer_key"]。二者经 reward_info → tq → omni extra_info → judge。

复用 agents/observer.py 的探针常量(_SNAPSHOT_PROBE/_SYS_PROBE)与纯 python diff
(diff_snapshots/diff_system/build_deterministic_report)。唯一差异：recipe_custom hook 是
async + sandbox.exec，而 observer 原探针走同步 sandbox.run_code —— 这里用 async exec 跑
同一段探针脚本，取 stdout 后在 driver 侧 json.loads + diff（diff 是纯 python，无关同步异步）。

⚠️ 本机无 e2b 沙箱无法端到端验证；集群实测（见文末 CLUSTER-TODO）。b1 baseline 可不挂此 hook
（reward 先用 judge 文本打分）；作为 reward 质量增强，R 系列 / 需强 grounding 时挂。
"""

from __future__ import annotations

import json
import os
from typing import Any

from recipe_custom.agent.runners.hooks.base import AgentRunHook

# taskspecs 根（与 cl_agent_dataset 同源）：<record_id>/answer_key.json 是 judge ground truth。
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # src/trainer → repo
TASKSPECS_ROOT = os.environ.get("CL_TASKSPECS_ROOT", os.path.join(_REPO_ROOT, "datasources", "taskspecs_w3"))
# generated_tasks_hermes 根：<D<N>>/<gen_task_id>/answer_key.json 是训练集(unk_* record_id)的
# judge ground truth。与 cl_agent_dataset.GEN_TASKS_ROOT 同源，靠 extra_info.gen_task_id 定位。
GEN_TASKS_ROOT = os.environ.get("CL_GEN_TASKS_ROOT", os.path.join(_REPO_ROOT, "datasources", "generated_tasks_hermes"))
# 沙箱工作区（探针 os.walk 的根）。与 fs-seed 注入的 ./inputs 同一工作目录。
SANDBOX_WORKSPACE = os.environ.get("CL_SANDBOX_WORKSPACE", ".")


async def _run_json_probe_async(sandbox: Any, probe: str, timeout: int = 60) -> dict:
    """async 版 _run_json_probe：sandbox.exec 跑探针脚本，取 stdout → json。永不抛。"""
    try:
        cmd = "python3 -c " + _shquote(probe)
        res = await sandbox.exec(cmd, timeout=timeout)
        out = (getattr(res, "stdout", "") or "").strip()
        if len(out) > 1_000_000:
            out = out[:1_000_000]
        data = json.loads(out) if out else {}
        return data if isinstance(data, dict) else {}
    except Exception:  # noqa: BLE001 -- 取证绝不能崩会话
        return {}


def _shquote(s: str) -> str:
    import shlex

    return shlex.quote(s)


def _record_id_from_ctx(ctx: Any) -> str | None:
    """从 ctx.extra（=runner kwargs，含 dataset 透传字段）取 record_id。"""
    extra = getattr(ctx, "extra", {}) or {}
    ei = extra.get("extra_info") or {}
    if isinstance(ei, dict):
        rid = ei.get("record_id")
        if rid:
            return str(rid)
    # 回退：reward_model.ground_truth 里可能带 task_id
    rm = extra.get("reward_model") or {}
    if isinstance(rm, dict):
        gt = rm.get("ground_truth")
        if isinstance(gt, dict) and gt.get("task_id"):
            return str(gt["task_id"])
    return None


def _gen_task_id_from_ctx(ctx: Any) -> str | None:
    """从 ctx.extra.extra_info 取 gen_task_id（generated_tasks_hermes 定位用）。"""
    extra = getattr(ctx, "extra", {}) or {}
    ei = extra.get("extra_info") or {}
    if isinstance(ei, dict):
        tid = ei.get("gen_task_id")
        if tid:
            return str(tid)
    return None


def _load_answer_key(record_id: str | None, gen_task_id: str | None = None) -> dict | None:
    """加载 judge ground truth。优先 gen_task_id → generated_tasks_hermes/<D>/<tid>/answer_key.json
    （训练集 record_id 是 unk_* 与 taskspecs_w3 不通）；回退 record_id → taskspecs_w3/<rid>/。"""
    candidates = []
    if gen_task_id:
        d_prefix = gen_task_id.split("_", 1)[0]  # D10_k982304_zh → D10
        candidates.append(os.path.join(GEN_TASKS_ROOT, d_prefix, gen_task_id, "answer_key.json"))
    if record_id:
        candidates.append(os.path.join(TASKSPECS_ROOT, record_id, "answer_key.json"))
    for path in candidates:
        if os.path.isfile(path):
            try:
                with open(path, encoding="utf-8") as f:
                    return json.load(f)
            except Exception:  # noqa: BLE001
                continue
    return None


# 源输入文件读取探针：在 agent 跑之前(prepare)读 ./inputs（及工作区根）下的源数据文件。
# text 类(csv/tsv/txt/json/md/yaml/xml)读全文(单文件截 20KB);rich 二进制(xlsx/docx/pdf)
# 标记为 binary(内容抽取交给下方 run 时的 extract_binaries,避免 prepare 阶段重依赖)。
# 只读、零 LLM;判 judge 用的真值锚点。总输出封顶 ~60KB。
_SOURCE_DATA_PROBE = (
    "import os, json\n"
    "TEXT_EXT=('.csv','.tsv','.txt','.json','.md','.yaml','.yml','.xml','.log','.py')\n"
    "RICH_EXT=('.xlsx','.xlsm','.docx','.pptx','.pdf')\n"
    "BASES=['./inputs','.',os.path.expanduser('~')]\n"
    "out={}; total=0\n"
    "seen=set()\n"
    "for base in BASES:\n"
    "    if not os.path.isdir(base):\n"
    "        continue\n"
    "    for root,dirs,files in os.walk(base):\n"
    "        dirs[:]=[d for d in dirs if d not in ('__pycache__','node_modules','.git','node-compile-cache')]\n"
    "        for fn in sorted(files):\n"
    "            p=os.path.join(root,fn)\n"
    "            rp=os.path.relpath(p)\n"
    "            if rp in seen or total>60000:\n"
    "                continue\n"
    "            seen.add(rp)\n"
    "            low=fn.lower()\n"
    "            try:\n"
    "                if low.endswith(RICH_EXT):\n"
    "                    out[rp]={'binary':True,'ext':os.path.splitext(low)[1]}\n"
    "                elif low.endswith(TEXT_EXT):\n"
    "                    with open(p,errors='replace') as f:\n"
    "                        data=f.read(20000)\n"
    "                    out[rp]={'content':data,'truncated':len(data)>=20000}\n"
    "                    total+=len(data)\n"
    "            except Exception as e:\n"
    "                out[rp]={'error':str(e)}\n"
    "print(json.dumps(out)[:120000])\n"
)


# stdout 类输出探针：读 hermes 整个对话流（agent 中间推理 + 最终回答 + terminal 工具输出）。
# hermes 启动命令 `hermes -z '...' chat > /tmp/hermes.log 2>&1`（hermes.py:76），整个对话
# 流重定向到此文件。agent 跑完沙箱关闭前 observer 读它 → judge 能看到真实运行结果，
# 不再只靠文件 diff（stdout-only 任务如"运行并报告"此前判不准的根因）。
# 单文件截 30KB（hermes.log 含思考链，太长；取头尾各 ~15KB 保留最终交付物）。
_HERMES_LOG_PATH = "/tmp/hermes.log"


async def _read_hermes_log_async(sandbox: Any, timeout: int = 30) -> str:
    """读 /tmp/hermes.log 全文（截 30KB 头尾）。沙箱关闭前调用。永不抛。"""
    try:
        res = await sandbox.exec(
            f"python3 -c \"import sys; sys.stdout.write(open('{_HERMES_LOG_PATH}','r',errors='replace').read()[:30000])\"",
            timeout=timeout,
        )
        out = getattr(res, "stdout", "") or ""
        return out
    except Exception:  # noqa: BLE001 -- 取证绝不能崩会话
        return ""


def _format_hermes_log(text: str) -> str:
    """把 hermes.log 渲染成 judge 可读文本块。空 → ''。"""
    text = (text or "").strip()
    if not text:
        return ""
    return f"\n\n# Agent stdout (hermes.log — agent 的对话流 + terminal 工具输出)\n{text}"


def _format_source_data(src: dict | None) -> str:
    """把源文件探针 dict 渲染成 judge 可读文本块。空/无源文件 → ''。"""
    if not isinstance(src, dict) or not src:
        return ""
    parts: list[str] = []
    for path, rec in src.items():
        if not isinstance(rec, dict):
            continue
        if rec.get("content") is not None:
            trunc = " [truncated]" if rec.get("truncated") else ""
            parts.append(f"### {path}{trunc}\n{rec['content']}")
        elif rec.get("binary"):
            parts.append(f"### {path} (binary {rec.get('ext', '')}, content extracted into the diff if changed)")
        elif rec.get("error"):
            parts.append(f"### {path} (read error: {rec['error']})")
    return "\n\n".join(parts).strip()


class ObserverDiffHook(AgentRunHook):
    """沙箱 before/after diff 取证 + answer_key 注入，写进 state.reward_info。

    run_on_agent_error=True：即使 agent 失败/超时，也采 diff（可能有部分交付物），让 judge
    基于真实产出打分，而非因异常直接 0（避免"失败即静默 0"掩盖部分完成）。
    """

    run_on_agent_error = True

    async def prepare(self, sandbox: Any, ctx: Any, state: Any) -> None:
        # agent 跑之前采 baseline（fs-seed 已由 runner 在 write_agent_assets 阶段注入 ./inputs，
        # 所以 baseline 已含输入文件 → diff 只暴露 agent 新产出/修改，不把输入文件误判为交付物）。
        from agents.observer import _SNAPSHOT_PROBE, _SYS_PROBE

        state.reward_info["_observer_pre_fs"] = await _run_json_probe_async(sandbox, _SNAPSHOT_PROBE)
        state.reward_info["_observer_pre_sys"] = await _run_json_probe_async(sandbox, _SYS_PROBE)
        # 源输入文件内容（judge 反幻觉锚点）：agent 跑【之前】沙箱里的源数据是干净的,此刻
        # 读它们的真实内容(csv/txt/json 全文 + xlsx/docx/pdf 抽取)写进 reward_info。judge
        # 据此核对/重算真值,不再对着看不见的源数据编造"实际应为 X"(F17 根因)。确定性、零 LLM。
        state.reward_info["_observer_src"] = await _run_json_probe_async(sandbox, _SOURCE_DATA_PROBE)

    async def run(self, sandbox: Any, ctx: Any, state: Any) -> None:
        from agents.observer import (
            _SNAPSHOT_PROBE,
            _SYS_PROBE,
            _format_changes,
            _is_runtime_file,
            diff_snapshots,
            diff_system,
        )

        pre_fs = state.reward_info.pop("_observer_pre_fs", None)
        pre_sys = state.reward_info.pop("_observer_pre_sys", None)
        post_fs = await _run_json_probe_async(sandbox, _SNAPSHOT_PROBE)
        post_sys = await _run_json_probe_async(sandbox, _SYS_PROBE)

        # runtime/framework 文件过滤（复用 observer._is_runtime_file：具名 + *.log/*.pid），
        # 与 snapshot_workspace 一致，避免 envd.log/jupyter.log 等噪声进 diff。
        def _filter(snap: dict | None) -> dict:
            if not isinstance(snap, dict):
                return {}
            return {p: r for p, r in snap.items() if not _is_runtime_file(p)}

        diff = diff_snapshots(_filter(pre_fs), _filter(post_fs))
        sys_diff = diff_system(pre_sys, post_sys)

        # observer_report = 人类可读正文（_format_changes）：三段式 新增/改变/删除，每段
        # 含【完整文件内容】，改变的文件含 [BEFORE]/[AFTER] 前后对比。这才是给 judge 看的
        # ground truth 正文（不是 dataclass repr）。judge 靠它核对 actor 自述是否属实。
        report = _format_changes(diff, sys_diff)
        # OOM/超时归因（B 方案 2026-09-02）：agent 被沙箱 kill（OOM code 137 / 超时）时，
        # verl e2b runner 把错误写进 state.agent_error。把它作为【权威环境事件】前置进 diff，
        # 让 judge 明确知道"轨迹是被外部终止截断的"而非"模型主动烂尾"——judge 据此归因，
        # 但仍按"有无交付"正常判分（B：OOM 是 agent 策略缺陷如全量 load 撑爆内存，照样算负
        # 样本，只是 reason 会写明 OOM 原因，便于事后分析）。
        agent_error = getattr(state, "agent_error", None)
        if agent_error:
            code = "137" if "137" in str(agent_error) else ""
            oom_hint = "（sandbox OOM，进程被内存上限杀死）" if code == "137" else ""
            banner = (
                f"[AGENT TERMINATED] 该轨迹被沙箱强制终止，未正常结束：{agent_error}{oom_hint}\n"
                "→ 轨迹在中途被截断，缺失的最终产出是【终止导致】而非模型主动放弃。"
                "按有无实际交付物评分（下方 diff 为终止时的真实沙箱状态）。\n\n"
            )
            report = banner + report
        state.reward_info["observer_report"] = report
        state.reward_info["state_diff"] = diff
        if agent_error:
            # 单独留一份，供 dump / 下游按需读取（不影响现有 observer_report 通路）。
            state.reward_info["agent_error"] = str(agent_error)
        answer_key = _load_answer_key(_record_id_from_ctx(ctx), _gen_task_id_from_ctx(ctx))
        if answer_key is not None:
            state.reward_info["answer_key"] = answer_key
        # 交付物计数（judge/completion 参考）：agent 新增/修改的文件数。
        state.reward_info["deliverable_count"] = len(diff.get("added", [])) + len(diff.get("modified", []))
        # 源输入文件内容 → 文本块（prepare 采的干净源数据）。judge 反幻觉锚点：拼进
        # correctness rubric 让 judge 核对真值。缺/空则不写(judge 回退无源判)。
        src = state.reward_info.pop("_observer_src", None)
        src_text = _format_source_data(src)
        if src_text:
            state.reward_info["source_data"] = src_text
        # stdout 类输出（hermes.log）：agent 的对话流 + terminal 工具输出。stdout-only
        # 任务（"运行并报告"）此前判不准的根因是 observer 只看文件 diff、看不到运行结果。
        # 沙箱关闭前读 /tmp/hermes.log → judge 能看到真实 stdout。截 30KB。
        hermes_log = await _read_hermes_log_async(sandbox)
        hermes_text = _format_hermes_log(hermes_log)
        if hermes_text:
            state.reward_info["hermes_log"] = hermes_text
        print(
            f"[cl][observer_hook] diff added={len(diff.get('added', []))} "
            f"modified={len(diff.get('modified', []))} source_data_chars={len(src_text)} "
            f"hermes_log_chars={len(hermes_text)}",
            flush=True,
        )


# ─────────────────────────────────────────────────────────────────────────────
# CLUSTER-TODO（集群实测）：
#  1. sandbox.exec("python3 -c <probe>") 在 agentic-cl-sandbox 镜像里能跑（python3 存在、
#     探针依赖的 openpyxl/python-docx/pdfplumber 装了 → 二进制提取生效；缺库降级不崩）。
#  2. ctx.extra 是否确实带 extra_info（record_id）—— 依赖 session_worker 把 dataset 的
#     extra_info 透传进 runner_kwargs（worker.py:497 白名单含 extra_info）。若不带，改从
#     raw_prompt 或 reward_model.ground_truth 取 record_id。
#  3. observer_report/answer_key 经 reward_info → tq → omni._prepare_item 的 extra_info →
#     model_reward_omni.compute_score 是否读得到（见阶段 F reward 回流 CLUSTER-TODO）。
#  4. SANDBOX_WORKSPACE 与 hermes 实际工作目录一致（探针 os.walk 的根）。
# ─────────────────────────────────────────────────────────────────────────────
