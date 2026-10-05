"""Cross-step state: observer LLM summary + Questioner-driven new seed queries.

跨 step 多轮的核心: step t 训练完后, 存每组最优轨迹 + observer diff 报告;
step t+1 开始时, observer 用 LLM 产执行概括(防直接沿用轨迹致偏移),
Questioner 基于概括 + 沙箱状态 产新 query, 作为 step t+1 的 seed.

数据流(driver 进程, 不在 worker):
  step t 完成 → 从 TQ 取 extra_fields(含 observer_report) + rm_scores + responses
  → 每组选最优轨迹(max reward)
  → observer LLM 产执行概括(基于 observer_report + 轨迹文本)
  → Questioner 基于概括 + 沙箱状态(diff) 产新 query
  → 构造新 batch(raw_prompt=新 query, 其他字段沿用上轮)
  → step t+1 rollout

沙箱状态: 用 observer_report 的 diff 文本作为"沙箱当前状态"给 Questioner,
不恢复文件系统(太复杂, 且 Questioner 只需文本描述).
"""

from __future__ import annotations

import logging
import uuid
from typing import Any

import numpy as np

logger = logging.getLogger(__name__)

_MAX_TRAJ_CHARS = 4000  # cap trajectory text fed to observer LLM
_MAX_OBSERVER_REPORT_CHARS = 8000  # cap observer diff report fed to LLM

# 空/低产出组的判定: 最优轨迹 reward 低于此值视为"没有值得追问的产出"。
# 这些组不生成追问(催促型追问是 reward-hacking 温床: agent 反问澄清→27s 交差→
# 文本兜底 report→judge 给分), 但其任务仍存活——只跳过追问, 不杀任务。
_LOW_YIELD_REWARD = 0.1

# 新任务生成比例: 存活组里高分组的种子中, 生成【全新任务】vs【建设性追问】的比例。
# 新任务为主(用户指令: 让新任务产生概率增加, 而不是追问增加)。
_NEW_TASK_RATIO = 0.7


def _generate_new_task(
    *,
    questioner: Any = None,
    exemplar_query: str = "",
    observer_report: str = "",
    source_data: str = "",
) -> str | None:
    """生成一个【全新独立任务】(非追问), 风格对齐原始种子池的任务描述.

    以 Questioner 池的 LLM 扮演 persona, 参考 exemplar(该组上轮任务)的风格,
    产一个自包含的新任务描述: 有明确输入文件 + 明确产出物 + 明确要求,
    和沙箱已有 workspace 无依赖关系(actor 从零开始做).

    文件名约束(防 hack 关键): 只允许引用 source_files 清单里【真实存在】的
    文件——上一轮"新任务引用编造文件名 → agent 'file not found' 拒答 → 拿分"
    的退化链由此掐断。无 source_files 时不生成新任务(返回 None, 该名额退回追问)。
    """
    if questioner is None:
        try:
            from agents.questioner import Questioner
            questioner = Questioner()
        except Exception as exc:  # noqa: BLE001
            print(f"[cross-step] questioner unavailable for new task: {exc}", flush=True)
            return None

    # 从 source_data(沙箱 probe 采集的真实输入文件清单)提取文件名列表
    import re as _re

    file_names = sorted(set(_re.findall(r"[\w./-]+\.(?:csv|tsv|txt|json|md|yaml|yml|xml|xlsx|xlsm|docx|pptx|pdf|py)", source_data)))
    if not file_names:
        print("[cross-step] no real source files for new task (source_data empty), fallback", flush=True)
        return None
    files_block = "\n".join(f"- {f}" for f in file_names[:30])

    try:
        from agents.personas import PERSONAS
        import random as _random

        persona = _random.choice(PERSONAS)
    except Exception as exc:  # noqa: BLE001
        print(f"[cross-step] persona unavailable for new task: {exc}", flush=True)
        return None

    prompt = f"""You are {persona.name}, a {getattr(persona, 'profession', 'professional')}.
Design ONE completely NEW, self-contained task for an AI assistant. This is NOT a
follow-up to any previous work.

Reference example of the task style (do NOT copy it, create a DIFFERENT task):
---
{exemplar_query[:1200]}
---

The ONLY files that exist in the sandbox (you MUST reference input files EXCLUSIVELY
from this list — any other filename does not exist and the agent WILL fail):
{files_block}

Requirements for your new task:
- Inputs: reference ONLY files from the list above (any subset, use exact names).
- Output: explicitly require the agent to PRODUCE FILES as deliverables
  (e.g. "write the analysis to <name>.md" / "output a cleaned <name>.xlsx").
  A chat-only reply must NOT satisfy the task.
- A realistic request this persona would actually make (analysis, audit,
  transformation, tool-building, summary — vary the TYPE from the example).
- One paragraph, direct, no meta-commentary.
- Output ONLY the task text.

New task:"""
    messages = [
        {"role": "system", "content": f"You are a task designer writing in the voice of {persona.name}."},
        {"role": "user", "content": prompt},
    ]
    try:
        from agents.questioner import END_SESSION

        text = questioner.client.chat(messages, max_tokens=512)
        text = (text or "").strip()
        if not text or END_SESSION in text:
            return None
        # 生成后校验: 任务文本里引用的文件名必须 ⊆ 真实文件清单(防 LLM 违规编造)。
        # 输出物文件名(任务要求 agent 新建的)不在清单里是正常的——区分不动词:
        # 出现在 "write/output/produce/save to ..." 之后的文件名是输出物, 免检;
        # 其余被引用的文件名若不在真实清单 → 判编造, 拒绝该任务。
        cited = set(_re.findall(r"[\w./-]+\.(?:csv|tsv|txt|json|md|yaml|yml|xml|xlsx|xlsm|docx|pptx|pdf|py)", text))
        real = set(file_names)
        # 输出物: 动词短语后到句末的任意文件名(中文"写入/输出/生成/保存" + 英文动词)。
        # finditer 逐个匹配只抓动词后【第一个】文件名, 漏掉 "produce A plus B" 的 B;
        # 改为: 找动词短语后的【分句】, 该分句里所有文件名都算输出物。
        outputs: set[str] = set()
        for m in _re.finditer(
            r"(?:write|output|produce|save|export|create|deliver|写入|输出|生成|保存|导出)((?:(?![.。](?![a-z0-9])).)*)",
            text,
            _re.IGNORECASE,
        ):
            outputs.update(
                _re.findall(r"[\w./-]+\.(?:csv|tsv|txt|json|md|yaml|yml|xml|xlsx|xlsm|docx|pptx|pdf|py)", m.group(1))
            )
        fabricated = [f for f in cited if f not in real and f not in outputs]
        if fabricated:
            print(
                f"[cross-step] new task references non-existent files {fabricated[:3]}, rejected",
                flush=True,
            )
            return None
        return text
    except Exception as exc:  # noqa: BLE001
        print(f"[cross-step] new-task generation failed: {exc}", flush=True)
        return None


def _extract_best_per_group(
    batch_keys: list[str],
    partition_id: str,
    group_size: int,
) -> list[dict[str, Any]]:
    """从 TQ 取 batch 的 extra_fields + rm_scores + responses, 每组选最优轨迹.

    返回 [{uid, reward, trajectory_text, observer_report, raw_prompt, extra_info}, ...]
    每组一条(最优轨迹).
    """
    try:
        import transfer_queue as tq
    except ImportError:
        return []

    fields = ["uid", "rm_scores", "responses", "raw_prompt", "extra_fields"]
    try:
        data = tq.kv_batch_get(keys=batch_keys, partition_id=partition_id, select_fields=fields)
    except Exception as exc:  # noqa: BLE001
        print("[cross-step] kv_batch_get failed: %s", exc)
        return []

    uids = data.get("uid")
    if uids is None:
        return []
    uids = uids.tolist() if hasattr(uids, "tolist") else list(uids)

    rm = data.get("rm_scores")
    try:
        rm_padded = rm.to_padded_tensor(padding=0.0) if hasattr(rm, "to_padded_tensor") else rm
        scores = rm_padded.sum(dim=-1).float().tolist() if hasattr(rm_padded, "sum") else [0.0] * len(uids)
    except Exception:  # noqa: BLE001
        scores = [0.0] * len(uids)

    responses = data.get("responses")
    raw_prompts = data.get("raw_prompt")
    extra_fields = data.get("extra_fields")

    # 按 uid 前缀分组, 每组选 max reward
    groups: dict[str, list[int]] = {}
    for i, uid_full in enumerate(uids):
        uid = str(uid_full).rsplit("_", 2)[0] if isinstance(uid_full, str) and str(uid_full).count("_") >= 2 else str(uid_full)
        groups.setdefault(uid, []).append(i)

    best_per_group: list[dict[str, Any]] = []
    for uid, indices in groups.items():
        best_idx = max(indices, key=lambda i: scores[i] if i < len(scores) else 0.0)
        # 轨迹文本: responses 是 nested tensor, 取 best_idx 行的文本
        traj_text = ""
        try:
            if responses is not None and best_idx < len(responses):
                resp = responses[best_idx]
                if hasattr(resp, "tolist"):
                    traj_text = str(resp.tolist())[:_MAX_TRAJ_CHARS]
                else:
                    traj_text = str(resp)[:_MAX_TRAJ_CHARS]
        except Exception:  # noqa: BLE001
            pass

        # observer_report: 从 extra_fields.reward_extra_info 取
        observer_report = ""
        source_data = ""
        extra_info = {}
        workspace_snapshot = None
        try:
            if extra_fields is not None and best_idx < len(extra_fields):
                ef = extra_fields[best_idx]
                if hasattr(ef, "tolist"):
                    ef = ef.tolist()
                if isinstance(ef, dict):
                    reward_extra = ef.get("reward_extra_info", {})
                    observer_report = str(reward_extra.get("observer_report", ""))[:_MAX_OBSERVER_REPORT_CHARS]
                    # 源输入文件清单(沙箱里真实存在的输入): 新任务生成的文件名锚点,
                    # 防止 LLM 编造不存在的文件名 → agent "file not found" 拒答 hack。
                    source_data = str(reward_extra.get("source_data", ""))[:4000]
                    # 跨 step 状态继承: 取该组最优轨迹的 workspace 快照(tar+base64)
                    workspace_snapshot = reward_extra.get("_workspace_snapshot")
                    extra_info = ef
        except Exception:  # noqa: BLE001
            pass

        # raw_prompt: 上轮的 seed query
        raw_prompt = None
        try:
            if raw_prompts is not None and best_idx < len(raw_prompts):
                rp = raw_prompts[best_idx]
                raw_prompt = list(rp) if hasattr(rp, "__iter__") else None
        except Exception:  # noqa: BLE001
            pass

        best_per_group.append({
            "uid": uid,
            "reward": float(scores[best_idx]) if best_idx < len(scores) else 0.0,
            "trajectory_text": traj_text,
            "observer_report": observer_report,
            "source_data": source_data,
            "raw_prompt": raw_prompt,
            "extra_info": extra_info,
            "workspace_snapshot": workspace_snapshot,
        })

    return best_per_group


def _observer_llm_summary(
    trajectory_text: str,
    observer_report: str,
    client: Any = None,
) -> str:
    """用 observer LLM 产执行概括(防直接沿用轨迹致偏移).

    输入: 上轮最优轨迹文本 + observer diff 报告.
    输出: 一段概括文本(给 Questioner, 不直接给 actor).

    超时: client 自带 httpx timeout(120s)——不要用 signal.alarm, 它只在主线程
    有效, 在 ThreadPoolExecutor 的 worker 线程里会静默失效(或直接 ValueError)。
    """
    if not client:
        try:
            from agents.base import resolve_observer_client
            client = resolve_observer_client()
        except Exception as exc:  # noqa: BLE001
            print(f"[cross-step] observer client unavailable: {exc}", flush=True)
            return f"Execution summary unavailable (LLM not configured). Last-turn trajectory excerpt: {trajectory_text[:500]}"

    prompt = f"""Summarize the execution of the following agent trajectory in one paragraph: what the agent did, what it produced, and what remains unfinished.
Do not restate the trajectory verbatim — summarize. This summary will be used to generate the next turn's follow-up query.

=== Observer state-diff report (real environment changes) ===
{observer_report}

=== Agent trajectory (execution process) ===
{trajectory_text}
"""
    messages = [
        {"role": "system", "content": "You are an objective execution summarizer. Summarize the agent's execution in one paragraph."},
        {"role": "user", "content": prompt},
    ]
    try:
        return client.chat(messages, max_tokens=512)
    except Exception as exc:  # noqa: BLE001
        print(f"[cross-step] observer LLM summary failed: {exc}", flush=True)
        return f"Execution summary failed ({exc}). Last-turn trajectory excerpt: {trajectory_text[:500]}"

def _questioner_new_query(
    summary: str,
    observer_report: str,
    persona: Any = None,
    history: list[dict[str, Any]] | None = None,
    questioner: Any = None,
) -> str | None:
    """Questioner 基于执行概括 + 沙箱状态 产新 query.

    返回新 query 文本, 或 None(无法生成).
    超时: client 自带 httpx timeout(120s)——signal.alarm 在 worker 线程失效, 不用。
    """
    if questioner is None:
        try:
            from agents.questioner import Questioner
            questioner = Questioner()
        except Exception as exc:  # noqa: BLE001
            print(f"[cross-step] questioner unavailable: {exc}", flush=True)
            return None

    if persona is None:
        try:
            from agents.personas import PERSONAS
            persona = PERSONAS[0]  # 简化: 用第一个 persona
        except Exception as exc:  # noqa: BLE001
            print(f"[cross-step] persona unavailable: {exc}", flush=True)
            return None

    # 构造简化 ObservationReport 给 Questioner
    try:
        from agents.schema import ObservationReport
        report = ObservationReport(
            actor_trajectory=summary,
            state_diff=observer_report,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"[cross-step] ObservationReport construction failed: {exc}", flush=True)
        return None

    try:
        return questioner.next_query(persona, report, history or [])
    except Exception as exc:  # noqa: BLE001
        print(f"[cross-step] questioner.next_query failed: {exc}", flush=True)
        return None


def generate_cross_step_seeds(
    batch_keys: list[str],
    partition_id: str,
    group_size: int,
    *,
    survived_uids: list[str] | None = None,
    observer_client: Any = None,
    questioner: Any = None,
    max_seeds: int = 0,
    max_workers: int = 64,
) -> list[dict[str, Any]]:
    """跨 step: 从上轮 batch 产新 seed queries(新任务为主, 追问为辅).

    返回 [{new_query, raw_prompt_template, extra_info, seed_kind, ...}, ...]
    高产组(reward >= _LOW_YIELD_REWARD)分流:
      - round(_NEW_TASK_RATIO) 比例生成【全新独立任务】(persona 驱动, 不依赖上轮产出,
        不带 workspace 快照, actor 从零开始);
      - 其余生成【建设性追问】(基于最优轨迹概括 + 沙箱状态, 带快照继承).
    低产组直接跳过——催促空产出只会教 agent 反问澄清拿分(reward hacking).

    Args:
        survived_uids: 任务存活组 uids(select_groups 的 task_survived_uids).
            只对这些组产种子; None = 不过滤(全部组).
        max_seeds: 最多产多少个 seed(0 = 不限, 生成全部存活组).
        max_workers: 并发线程数(每组 1-2 次串行 HTTP). 129 组 64 并发 ~2min.
    """
    best_per_group = _extract_best_per_group(batch_keys, partition_id, group_size)
    if not best_per_group:
        print("[cross-step] no best trajectories extracted, cannot generate seeds", flush=True)
        return []

    # 只对任务存活组产种子(全死组淘汰, 不追问)
    if survived_uids is not None:
        survived_set = set(survived_uids)
        n_before = len(best_per_group)
        best_per_group = [b for b in best_per_group if b["uid"] in survived_set]
        print(
            f"[cross-step] survived filter: {n_before} groups -> {len(best_per_group)} "
            f"(survived_uids={len(survived_set)})",
            flush=True,
        )

    # 按 reward 降序; max_seeds>0 时只取前 max_seeds 组(限制 HTTP 调用数)
    best_per_group.sort(key=lambda b: -b["reward"])
    if max_seeds > 0:
        best_per_group = best_per_group[:max_seeds]

    # ── 种子分流: 低产组跳过追问(避免催促型追问→反问澄清→reward hacking) ──
    # 高产组(reward >= _LOW_YIELD_REWARD)按比例生成【新任务】或【建设性追问】;
    # 低产组直接跳过(不再追问"你为什么没产出"——那种追问只会教 agent 敷衍)。
    high_yield = [b for b in best_per_group if b["reward"] >= _LOW_YIELD_REWARD]
    low_yield = [b for b in best_per_group if b["reward"] < _LOW_YIELD_REWARD]
    print(
        f"[cross-step] yield split: {len(high_yield)} high-yield (seed) / "
        f"{len(low_yield)} low-yield (skip, no prodding)",
        flush=True,
    )

    # 新任务 vs 追问的名额分配(新任务为主)
    import random as _random

    n_new = round(len(high_yield) * _NEW_TASK_RATIO)
    is_new_task = [True] * n_new + [False] * (len(high_yield) - n_new)
    _random.shuffle(is_new_task)

    print(
        f"[cross-step] generating seeds: {n_new} new tasks + "
        f"{len(high_yield) - n_new} follow-ups from {len(high_yield)} groups",
        flush=True,
    )

    # 并发生成(默认 64)。线程安全: OpenAIChatClient 用无状态 httpx.post,
    # FailoverChatClient 的 rotation/默认端点切换在 RLock 内。
    from concurrent.futures import ThreadPoolExecutor

    def _make_seed(best: dict[str, Any], new_query: str, summary: str, *, is_new_task: bool) -> dict[str, Any]:
        # 新任务不带 workspace 快照(actor 从零开始, 不继承上轮产出);
        # 追问带快照(在已有产出上继续)。回退场景由 is_new_task 显式传入。
        snap = None if is_new_task else best.get("workspace_snapshot")
        return {
            "new_query": new_query,
            "raw_prompt_template": best["raw_prompt"],
            "extra_info": best["extra_info"],
            "uid": best["uid"],
            "reward": best["reward"],
            "summary": summary,
            "seed_kind": "new_task" if is_new_task else "followup",
            "workspace_snapshot": snap,
        }

    def _gen_one(best: dict[str, Any]) -> dict[str, Any] | None:
        if best.get("_is_new_task"):
            # 全新任务: 参考该组上轮任务的风格, 只引用真实存在的输入文件
            exemplar = ""
            try:
                rp = best.get("raw_prompt") or []
                exemplar = " ".join(
                    str(m.get("content", "")) for m in rp if isinstance(m, dict)
                )
            except Exception:  # noqa: BLE001
                exemplar = ""
            new_query = _generate_new_task(
                questioner=questioner,
                exemplar_query=exemplar,
                observer_report=best["observer_report"],
                source_data=best.get("source_data", ""),
            )
            if new_query is not None:
                return _make_seed(best, new_query, "", is_new_task=True)
            # 新任务失败(无真实文件清单/文件名校验不过/LLM失败)→ 回退建设性追问,
            # 不浪费该组名额
            print(f"[cross-step] new-task failed for uid={best['uid']}, fallback to followup", flush=True)

        # 建设性追问: 仅对有产出的组, observer 概括 + Questioner 深化/扩展
        summary = _observer_llm_summary(
            best["trajectory_text"],
            best["observer_report"],
            client=observer_client,
        )
        new_query = _questioner_new_query(
            summary,
            best["observer_report"],
            questioner=questioner,
        )
        if new_query is None:
            print(f"[cross-step] questioner returned None for uid={best['uid']}, skip", flush=True)
            return None
        return _make_seed(best, new_query, summary, is_new_task=False)

    for best, new_flag in zip(high_yield, is_new_task, strict=False):
        best["_is_new_task"] = new_flag

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        results = list(pool.map(_gen_one, high_yield))
    seeds = [r for r in results if r is not None]

    n_new_ok = sum(1 for s in seeds if s.get("seed_kind") == "new_task")
    print(
        f"[cross-step] generated {len(seeds)} seeds ({n_new_ok} new tasks + "
        f"{len(seeds) - n_new_ok} follow-ups) from {len(high_yield)} high-yield groups",
        flush=True,
    )
    return seeds


def build_cross_step_batch(
    seeds: list[dict[str, Any]],
    tokenizer: Any = None,
) -> dict[str, Any] | None:
    """把跨 step seeds 构造成 verl dataloader 等价的 batch_dict.

    返回 batch_dict(含 raw_prompt/uid/data_source/reward_model/extra_info/dummy_tensor),
    或 None(构造失败).
    """
    if not seeds:
        return None

    raw_prompts = []
    prompts = []
    uids = []
    data_sources = []
    reward_models = []
    extra_infos = []
    buckets = []
    interaction_kwargs_list = []
    tools_kwargs_list = []
    indices = []

    for seed in seeds:
        new_query = seed["new_query"]
        template = seed["raw_prompt_template"]

        # 用新 query 替换 template 的 user message
        if template and len(template) > 0:
            new_prompt = [{"role": "user", "content": new_query}]
        else:
            new_prompt = [{"role": "user", "content": new_query}]

        raw_prompts.append(new_prompt)
        prompts.append(new_prompt)  # prompt 与 raw_prompt 同 (dataloader 有此字段)
        uids.append(str(uuid.uuid4()))
        data_sources.append("agentic_cl")
        reward_models.append({
            "ground_truth": "",
            "style": "rule",
            "reward_fn": {"_function_name": "trainer.model_reward_omni.compute_score"},
        })

        ei = seed.get("extra_info", {})
        if isinstance(ei, dict):
            ei = dict(ei)
        else:
            ei = {}
        ei["cross_step"] = True
        ei["original_uid"] = seed.get("uid", "")
        # 跨 step 状态继承: 把上轮 workspace 快照放进 extra_info, observer_hook.prepare
        # 会在本轮新沙箱创建后 base64 解包恢复(actor 在上轮产出的文件上继续).
        snap = seed.get("workspace_snapshot")
        if snap:
            ei["_workspace_snapshot"] = snap
        extra_infos.append(ei)
        # dataloader 额外字段 (与 RLHFDataset.__getitem__ 对齐, concat 需字段一致)
        buckets.append(ei.get("bucket", "coding"))
        interaction_kwargs_list.append({})
        tools_kwargs_list.append({})
        indices.append(0)

    import torch

    batch_dict = {
        "raw_prompt": np.array(raw_prompts, dtype=object),
        "prompt": np.array(prompts, dtype=object),
        "uid": np.array(uids, dtype=object),
        "data_source": np.array(data_sources, dtype=object),
        "reward_model": np.array(reward_models, dtype=object),
        "extra_info": np.array(extra_infos, dtype=object),
        "bucket": np.array(buckets, dtype=object),
        "interaction_kwargs": np.array(interaction_kwargs_list, dtype=object),
        "tools_kwargs": np.array(tools_kwargs_list, dtype=object),
        "index": np.array(indices, dtype=object),
        "dummy_tensor": torch.zeros((len(seeds), 1), dtype=torch.uint8),  # [N,1] 对齐 RLHFDataset (每行 [1])
    }
    return batch_dict
