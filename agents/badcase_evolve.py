"""Failure-case-driven self-evolution of evaluator prompts and infra.

失败案例驱动的评估器与基建自演化（对应论文第 4.6 节）。

功能：
  1. 收集失败案例 (IsFailed → collect_failure_case)
  2. 触发判断（每 10 步 or 累积 20 个）
  3. 大模型归因：综合任务意图 + 轨迹 + 环境证据，区分"模型问题"与"基建问题"
  4. 分流处理：
       模型问题 → 热更新提示词（judge/questioner/actor 增量修订）
       基建问题 → 动态扩展基建（工具注册表 + 沙箱依赖 + harness 配置）

设计原则：
  - 归因由 LLM 综合判断，而非规则程序（OOM 可能是基建不足，也可能是模型暴力搜索）
  - 提示词采用增量追加而非整体重写，保证可回滚
  - 基建扩展只记录扩展项到日志/配置，不直接修改运行时（由下游流程消费）
  - 所有 LLM 调用带超时与异常捕获，失败时静默跳过不阻塞训练主循环
  - 触发参数（10步/20例）为演示可运行性而设定，并非调优后的最优取值

接入方式（trainer 调用）：
  from agents.badcase_evolve import BadcaseEvolver
  evolver = BadcaseEvolver()              # 在 trainer __init__ 里构造
  evolver.collect(step, traj, diff, reward, reward_info)  # 每条轨迹调用
  if evolver.should_trigger(global_step):
      evolver.evolve()                    # 驱动归因 + 更新
"""

from __future__ import annotations

import json
import logging
import os
import signal
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

_EVOLVE_EVERY_STEPS = int(os.environ.get("BADCASE_EVOLVE_STEPS", "10"))
_EVOLVE_ON_N_CASES = int(os.environ.get("BADCASE_EVOLVE_N", "20"))
_LLM_TIMEOUT_S = int(os.environ.get("BADCASE_LLM_TIMEOUT", "60"))
_MAX_TRAJ_CHARS = 2000
_MAX_REPORT_CHARS = 3000


@dataclass
class FailureCase:
    """一个失败案例的完整取证记录。"""
    step: int
    uid: str                        # GRPO 组 uid
    trajectory_text: str            # 轨迹文本（截断）
    observer_report: str            # 观察者状态差分报告
    agent_error: str                # agent 执行报错（如有）
    state_diff: dict                # 状态差分（文件/系统变更）
    reward: float                   # 最终得分
    deliverable_count: int          # 产出物数量
    raw_prompt: str                 # 原始任务描述
    hermes_log: str                 # 工具调用日志片段


@dataclass
class AttributionResult:
    """LLM 归因结果。"""
    uid: str
    attribution: str                # "model" | "infra" | "unclear"
    reasoning: str                  # 归因理由（LLM 输出）
    prompt_patch: str               # 如是模型问题，建议的提示词增量修订
    infra_patch: str                # 如是基建问题，建议的基建扩展项


@dataclass
class EvolverState:
    """持久化到磁盘的演化状态（提示词补丁历史 + 基建扩展日志）。"""
    prompt_patches: list[dict] = field(default_factory=list)
    infra_patches: list[dict] = field(default_factory=list)
    evolve_count: int = 0


def _is_failed(
    reward: float,
    reward_info: dict[str, Any],
    reward_threshold: float = 0.1,
) -> bool:
    """判断一条轨迹是否为失败案例。

    判据：
      - reward 极低（< threshold，几乎没有有效产出）
      - 有 agent_error（执行崩溃/超时）
      - deliverable_count == 0 且 state_diff 为空（啥都没做）
      - observer_report 与 trajectory 矛盾（暂用 reward < 0.3 且 deliverable > 0 的异常组合）
    """
    if reward < reward_threshold:
        return True
    if reward_info.get("agent_error"):
        return True
    diff = reward_info.get("state_diff") or {}
    deliverable = reward_info.get("deliverable_count", 0)
    if not diff and deliverable == 0 and reward < 0.3:
        return True
    return False


class BadcaseEvolver:
    """训练过程中持续收集失败案例并周期性驱动自演化的控制器。

    生命周期：
      __init__ → (每步) collect() × 多次 → should_trigger() → evolve() → 重复

    线程安全：单 driver 进程，不需要锁。
    """

    def __init__(
        self,
        state_dir: str | Path | None = None,
        evolve_every_steps: int = _EVOLVE_EVERY_STEPS,
        evolve_on_n_cases: int = _EVOLVE_ON_N_CASES,
    ) -> None:
        self._buffer: list[FailureCase] = []
        self._last_evolve_step: int = 0
        self._evolve_every_steps = evolve_every_steps
        self._evolve_on_n_cases = evolve_on_n_cases

        # 持久化目录（存储 prompt_patches.json + infra_patches.json）
        self._state_dir = Path(state_dir or "logs/badcase_evolve")
        self._state_dir.mkdir(parents=True, exist_ok=True)
        self._state = self._load_state()
        self._meta_llm: Any = None   # 延迟初始化，避免 import 顺序问题

    # ── 公开 API ──────────────────────────────────────────────────────────

    def collect(
        self,
        step: int,
        uid: str,
        trajectory_text: str,
        observer_report: str,
        reward: float,
        reward_info: dict[str, Any],
        raw_prompt: str = "",
    ) -> None:
        """从 reward_info 里提取取证字段，判断是否失败，失败则加入缓冲。

        在 trainer 的 _step_once 里，对每条轨迹的 reward_info 调用一次。
        """
        if not _is_failed(reward, reward_info):
            return
        case = FailureCase(
            step=step,
            uid=uid,
            trajectory_text=trajectory_text[:_MAX_TRAJ_CHARS],
            observer_report=(observer_report or "")[:_MAX_REPORT_CHARS],
            agent_error=str(reward_info.get("agent_error") or ""),
            state_diff=reward_info.get("state_diff") or {},
            reward=reward,
            deliverable_count=int(reward_info.get("deliverable_count") or 0),
            raw_prompt=raw_prompt[:500],
            hermes_log=str(reward_info.get("hermes_log") or "")[:1000],
        )
        self._buffer.append(case)
        logger.debug("[badcase] step=%d uid=%s reward=%.3f collected (total=%d)",
                     step, uid, reward, len(self._buffer))

    def should_trigger(self, global_step: int) -> bool:
        """判断是否应触发本轮演化。

        触发条件（二择一）：
          - 自上次演化起已过 evolve_every_steps 步
          - 缓冲区已积累 evolve_on_n_cases 个失败案例
        """
        if not self._buffer:
            return False
        step_trigger = (global_step - self._last_evolve_step) >= self._evolve_every_steps
        count_trigger = len(self._buffer) >= self._evolve_on_n_cases
        return step_trigger or count_trigger

    def evolve(self, global_step: int = 0) -> None:
        """对当前缓冲区里的失败案例进行一次归因 + 演化。

        流程：
          1. 抽样（最多取 8 个代表性案例，避免 prompt 过长）
          2. 批量调用 meta-LLM 归因（模型问题 or 基建问题）
          3. 按归因分流：模型问题 → 追加 prompt patch，基建问题 → 追加 infra patch
          4. 持久化 patches，清空缓冲，更新 last_evolve_step
        """
        cases = self._buffer[:8]   # 每次最多处理 8 个，避免 prompt 过长
        logger.info("[badcase] step=%d trigger evolve: %d cases in buffer (processing %d)",
                    global_step, len(self._buffer), len(cases))

        attributions = self._attribute_cases(cases)
        n_model = n_infra = 0
        for attr in attributions:
            if attr.attribution == "model" and attr.prompt_patch.strip():
                self._state.prompt_patches.append({
                    "step": global_step,
                    "uid": attr.uid,
                    "patch": attr.prompt_patch,
                    "reasoning": attr.reasoning[:300],
                })
                n_model += 1
            elif attr.attribution == "infra" and attr.infra_patch.strip():
                self._state.infra_patches.append({
                    "step": global_step,
                    "uid": attr.uid,
                    "patch": attr.infra_patch,
                    "reasoning": attr.reasoning[:300],
                })
                n_infra += 1

        self._state.evolve_count += 1
        self._save_state()
        self._apply_prompt_patches()
        self._apply_infra_patches()

        logger.info("[badcase] evolve #%d done: model_issues=%d infra_issues=%d "
                    "(unclear=%d), patches saved to %s",
                    self._state.evolve_count, n_model, n_infra,
                    len(attributions) - n_model - n_infra, self._state_dir)

        self._buffer.clear()
        self._last_evolve_step = global_step

    # ── 提示词热更新 ──────────────────────────────────────────────────────

    def get_prompt_patches(self) -> list[dict]:
        """返回所有已积累的提示词增量修订，供 judge/questioner/actor 在每步初始化时消费。

        调用方应将这些 patches 追加到对应角色的系统提示词末尾（而非整体替换），
        保证可回滚且不引起提示词漂移。
        """
        return list(self._state.prompt_patches)

    def get_infra_patches(self) -> list[dict]:
        """返回所有已积累的基建扩展项，供 harness 注册器/沙箱配置在启动时消费。"""
        return list(self._state.infra_patches)

    # ── 内部：LLM 归因 ────────────────────────────────────────────────────

    def _get_meta_llm(self) -> Any | None:
        """延迟初始化用于归因的 meta-LLM 客户端（优先使用 observer 角色配置）。"""
        if self._meta_llm is not None:
            return self._meta_llm
        try:
            from agents.base import get_observer
            self._meta_llm = get_observer()
            return self._meta_llm
        except Exception as exc:  # noqa: BLE001
            logger.warning("[badcase] meta-LLM unavailable, attribution skipped: %s", exc)
            return None

    def _attribute_cases(self, cases: list[FailureCase]) -> list[AttributionResult]:
        """批量归因：对每个失败案例调用 LLM 判断根因。

        若 LLM 不可用，返回 "unclear" 占位结果（不阻塞训练）。
        """
        client = self._get_meta_llm()
        results = []
        for case in cases:
            if client is None:
                results.append(AttributionResult(
                    uid=case.uid, attribution="unclear",
                    reasoning="meta-LLM unavailable", prompt_patch="", infra_patch="",
                ))
                continue
            attr = self._attribute_one(client, case)
            results.append(attr)
        return results

    def _attribute_one(self, client: Any, case: FailureCase) -> AttributionResult:
        """对单个失败案例调用 LLM 归因，带超时保护。"""
        prompt = _build_attribution_prompt(case)
        messages = [
            {
                "role": "system",
                "content": (
                    "你是一个自进化强化学习系统的诊断专家。"
                    "你的任务是分析训练中出现的失败案例，判断根因是『模型问题』还是『基建问题』，"
                    "并给出针对性的修复建议。\n"
                    "注意：归因必须综合考虑任务意图、轨迹、环境证据，不能仅凭错误码判断。"
                    "例如 OOM 可能是基建内存不足，也可能是模型选了暴力全量搜索的低效方案。"
                ),
            },
            {"role": "user", "content": prompt},
        ]
        try:
            def _timeout(signum, frame):
                raise TimeoutError(f"attribution LLM timed out ({_LLM_TIMEOUT_S}s)")
            old = signal.signal(signal.SIGALRM, _timeout)
            signal.alarm(_LLM_TIMEOUT_S)
            try:
                raw = client.chat(messages, max_tokens=800)
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old)
            return _parse_attribution_response(case.uid, raw)
        except Exception as exc:  # noqa: BLE001
            logger.warning("[badcase] attribution failed for uid=%s: %s", case.uid, exc)
            return AttributionResult(
                uid=case.uid, attribution="unclear",
                reasoning=f"LLM call failed: {exc}", prompt_patch="", infra_patch="",
            )

    # ── 内部：patch 应用 ──────────────────────────────────────────────────

    def _apply_prompt_patches(self) -> None:
        """将本轮新增的提示词 patches 写入 prompt_patches.json。

        下游：judge/questioner/actor 在下一轮初始化时读取并追加到系统提示词末尾。
        具体消费逻辑见 agents/prompts.py（待实现）。
        """
        patch_file = self._state_dir / "prompt_patches.json"
        with open(patch_file, "w", encoding="utf-8") as f:
            json.dump(self._state.prompt_patches, f, ensure_ascii=False, indent=2)
        if self._state.prompt_patches:
            latest = self._state.prompt_patches[-1]
            logger.info("[badcase] prompt patch saved: step=%s uid=%s patch_preview=%.80s",
                        latest.get("step"), latest.get("uid"), latest.get("patch", ""))

    def _apply_infra_patches(self) -> None:
        """将本轮新增的基建扩展项写入 infra_patches.json。

        下游：harness 注册器在下次沙箱初始化时读取，按 patch 类型执行：
          - tool: 注册新工具到工具白名单
          - dep: 在沙箱镜像/环境中补装依赖
          - timeout: 调整对应工具的超时阈值
          - harness: 记录 harness 处理逻辑待修复项（人工复核后合入代码）
        下游消费逻辑见 src/trainer/harness_register.py（待实现）。
        """
        patch_file = self._state_dir / "infra_patches.json"
        with open(patch_file, "w", encoding="utf-8") as f:
            json.dump(self._state.infra_patches, f, ensure_ascii=False, indent=2)
        if self._state.infra_patches:
            latest = self._state.infra_patches[-1]
            logger.info("[badcase] infra patch saved: step=%s uid=%s patch_preview=%.80s",
                        latest.get("step"), latest.get("uid"), latest.get("patch", ""))

    # ── 内部：状态序列化 ──────────────────────────────────────────────────

    def _load_state(self) -> EvolverState:
        state_file = self._state_dir / "evolver_state.json"
        if not state_file.exists():
            return EvolverState()
        try:
            with open(state_file, encoding="utf-8") as f:
                d = json.load(f)
            return EvolverState(
                prompt_patches=d.get("prompt_patches", []),
                infra_patches=d.get("infra_patches", []),
                evolve_count=d.get("evolve_count", 0),
            )
        except Exception as exc:  # noqa: BLE001
            logger.warning("[badcase] failed to load state, starting fresh: %s", exc)
            return EvolverState()

    def _save_state(self) -> None:
        state_file = self._state_dir / "evolver_state.json"
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump({
                "prompt_patches": self._state.prompt_patches,
                "infra_patches": self._state.infra_patches,
                "evolve_count": self._state.evolve_count,
                "saved_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            }, f, ensure_ascii=False, indent=2)


# ── Prompt 构造 ────────────────────────────────────────────────────────────

def _build_attribution_prompt(case: FailureCase) -> str:
    diff_summary = (
        json.dumps(case.state_diff, ensure_ascii=False)[:500]
        if case.state_diff else "（空：无任何文件/系统状态变更）"
    )
    return f"""## 失败案例归因请求

**任务描述**
{case.raw_prompt or "（无）"}

**轨迹摘要**（截断至 {_MAX_TRAJ_CHARS} 字符）
{case.trajectory_text or "（无）"}

**观察者状态差分**（截断至 {_MAX_REPORT_CHARS} 字符）
{case.observer_report or "（无）"}

**状态差分详情**（变更摘要）
{diff_summary}

**执行报错**
{case.agent_error or "（无）"}

**工具调用日志片段**
{case.hermes_log or "（无）"}

**得分**：{case.reward:.3f}（交付物数量：{case.deliverable_count}）

---

请按如下 JSON 格式回复（只输出 JSON，不要加任何解释文字）：

```json
{{
  "attribution": "model" | "infra" | "unclear",
  "reasoning": "综合任务意图、轨迹、环境证据的归因理由（2-4句话）",
  "prompt_patch": "若为模型问题，此处写对 judge/questioner/actor 提示词的增量修订建议（1-3条具体规则）；若非模型问题则留空",
  "infra_patch": "若为基建问题，此处写基建扩展项（格式：type:tool/dep/timeout/harness + 具体内容）；若非基建问题则留空"
}}
```"""


def _parse_attribution_response(uid: str, raw: str) -> AttributionResult:
    """解析 LLM 的归因 JSON 输出，对格式容错。"""
    import re
    # 尝试从 ```json ... ``` 或裸 JSON 中提取
    m = re.search(r"```json\s*(.*?)\s*```", raw, re.DOTALL)
    text = m.group(1) if m else raw.strip()
    try:
        d = json.loads(text)
    except json.JSONDecodeError:
        # 容错：取第一个 { ... } 块
        m2 = re.search(r"\{.*\}", text, re.DOTALL)
        if m2:
            try:
                d = json.loads(m2.group(0))
            except json.JSONDecodeError:
                d = {}
        else:
            d = {}
    attribution = d.get("attribution", "unclear")
    if attribution not in ("model", "infra", "unclear"):
        attribution = "unclear"
    return AttributionResult(
        uid=uid,
        attribution=attribution,
        reasoning=str(d.get("reasoning", "")),
        prompt_patch=str(d.get("prompt_patch", "")),
        infra_patch=str(d.get("infra_patch", "")),
    )
