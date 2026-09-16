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
    """
    if not client:
        try:
            from agents.base import resolve_observer_client
            client = resolve_observer_client()
        except Exception as exc:  # noqa: BLE001
            print("[cross-step] observer client unavailable: %s", exc)
            return f"执行概括不可用(LLM 未配置)。上轮轨迹摘要: {trajectory_text[:500]}"

    prompt = f"""请概括以下 agent 轨迹的执行情况, 用一段话描述 agent 做了什么、产出了什么、还有什么没完成.
不要直接复述轨迹, 要概括. 这段概括将用于生成下一轮追问.

=== Observer 状态差分报告(环境真实变更) ===
{observer_report}

=== Agent 轨迹(执行过程) ===
{trajectory_text}
"""
    messages = [
        {"role": "system", "content": "你是一个客观的执行概括器. 用一段话概括 agent 的执行情况."},
        {"role": "user", "content": prompt},
    ]
    try:
        # 加超时: 防止 tokenhub 卡住 driver 进程(30s 超时)
        import signal

        def _timeout_handler(signum, frame):
            raise TimeoutError("observer LLM summary timed out (30s)")
        old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
        signal.alarm(30)
        try:
            result = client.chat(messages, max_tokens=512)
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)
        return result
    except Exception as exc:  # noqa: BLE001
        print("[cross-step] observer LLM summary failed: %s", exc)
        return f"执行概括失败({exc})。上轮轨迹摘要: {trajectory_text[:500]}"

def _questioner_new_query(
    summary: str,
    observer_report: str,
    persona: Any = None,
    history: list[dict[str, Any]] | None = None,
    questioner: Any = None,
) -> str | None:
    """Questioner 基于执行概括 + 沙箱状态 产新 query.

    返回新 query 文本, 或 None(无法生成).
    """
    if questioner is None:
        try:
            from agents.questioner import Questioner
            questioner = Questioner()
        except Exception as exc:  # noqa: BLE001
            print("[cross-step] questioner unavailable: %s", exc)
            return None

    if persona is None:
        try:
            from agents.personas import PERSONAS
            persona = PERSONAS[0]  # 简化: 用第一个 persona
        except Exception as exc:  # noqa: BLE001
            print("[cross-step] persona unavailable: %s", exc)
            return None

    # 构造简化 ObservationReport 给 Questioner
    try:
        from agents.schema import ObservationReport
        report = ObservationReport(
            actor_trajectory=summary,
            state_diff=observer_report,
        )
    except Exception as exc:  # noqa: BLE001
        print("[cross-step] ObservationReport construction failed: %s", exc)
        return None

    try:
        # 加超时: 防止 Questioner 的 tokenhub HTTP 卡住 driver(30s)
        import signal

        def _timeout_handler(signum, frame):
            raise TimeoutError("questioner.next_query timed out (30s)")
        old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
        signal.alarm(30)
        try:
            new_query = questioner.next_query(persona, report, history or [])
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)
        return new_query
    except Exception as exc:  # noqa: BLE001
        print("[cross-step] questioner.next_query failed: %s", exc)
        return None


def generate_cross_step_seeds(
    batch_keys: list[str],
    partition_id: str,
    group_size: int,
    *,
    observer_client: Any = None,
    questioner: Any = None,
    max_seeds: int = 4,
) -> list[dict[str, Any]]:
    """跨 step: 从上轮 batch 产新 seed queries.

    返回 [{new_query, raw_prompt_template, extra_info}, ...]
    每组一个新 query(基于该组最优轨迹的概括 + 沙箱状态).

    Args:
        max_seeds: 最多产多少个 seed(限制 tokenhub HTTP 调用数, 避免卡 driver).
            默认 4(= 4 组 × 2 次 HTTP = 8 次调用, ~30s).
    """
    best_per_group = _extract_best_per_group(batch_keys, partition_id, group_size)
    if not best_per_group:
        print("[cross-step] no best trajectories extracted, cannot generate seeds")
        return []

    # 按 reward 降序, 只取前 max_seeds 组(减少 HTTP 调用)
    best_per_group.sort(key=lambda b: -b["reward"])
    best_per_group = best_per_group[:max_seeds]
    print("[cross-step] generating seeds for top %d/%d groups", len(best_per_group), len(best_per_group))

    seeds: list[dict[str, Any]] = []
    history: list[dict[str, Any]] = []
    for best in best_per_group:
        # 1. observer LLM 产执行概括
        summary = _observer_llm_summary(
            best["trajectory_text"],
            best["observer_report"],
            client=observer_client,
        )

        # 2. Questioner 产新 query
        new_query = _questioner_new_query(
            summary,
            best["observer_report"],
            history=history,
            questioner=questioner,
        )

        if new_query is None:
            print("[cross-step] questioner returned None for uid=%s, skip", best["uid"])
            continue

        # 3. 构造 seed: 新 query + 上轮的 raw_prompt 模板 + workspace 快照(状态继承)
        seeds.append({
            "new_query": new_query,
            "raw_prompt_template": best["raw_prompt"],
            "extra_info": best["extra_info"],
            "uid": best["uid"],
            "reward": best["reward"],
            "summary": summary,
            "workspace_snapshot": best.get("workspace_snapshot"),
        })

        # history 累积(给下一个 Questioner 调用用)
        history.append({"role": "user", "content": new_query})

    print("[cross-step] generated %d seeds from %d groups", len(seeds), len(best_per_group))
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
