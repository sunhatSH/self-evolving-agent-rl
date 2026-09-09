# OVERVIEW — 架构与设计深入

> 系统 = **多 Agent 采样 + 沙箱环境 + diff 驱动奖励 + 标准 GRPO 训练**。
> 训练只用来验证系统端到端跑通，不含任何持续学习机制。协作规范见 `CLAUDE.md`，入口见 `README.md`。

---

## 1. 采样环（sampling loop）

一次 rollout 里的角色分工：

- **Actor（ReAct）** — 在代码沙箱中一步步执行工具动作解任务。它就是被训练的策略（verl 原生 rollout LLM server，逐步 `llm_client.generate` 返回 token_ids + log_probs）。
- **Observer** — 任务开始时拍一次沙箱快照（baseline），结束时再拍一次，产出 **before/after 确定性 diff**。这是奖励的 ground truth，**不是**让模型复读 actor 的自述。
- **Questioner** — 人设驱动的模拟用户，读 Observer 的客观报告 + 人设 + 历史，写下一轮 query，或结束会话（多轮路径，单轮时为 no-op）。

数据流（单次 `generate_sequences`）：

```
verl fit() ──prompts(已×n)──► agent_rollout_manager.generate_sequences
   每个输入 ROW → 1 次单槽 rollout（verl 拥有 ×n 复制与 GRPO 分组，我们每行只回 1 条轨迹）
      每 step → llm_client.generate（token_ids + log_probs）
      Observer 对该行做 diff → meta['observer_report']
      _score_all_slots：observer diff + verifier + judge → t.reward
   list[Trajectory] ──trajectories_to_dataproto──► DataProto（含 rm_scores + observer_report）
```

**行数契约（关键）**：verl 在调用我们之前已按 `rollout.n` 把每条 query 复制 n 份（interleave），并按它自己的 `uid` 分组算 advantage。所以我们**每个输入行只回恰好 1 条轨迹、按序、绝不自造 uid**（否则 `DataProto.union` 会碰撞）。

## 2. 三 Agent 的契约

| Agent | 输入 | 产出 | 消费方 |
|-------|------|------|--------|
| Observer | actor 轨迹 + 沙箱 baseline/after | `ObservationReport`（`agents/schema.py`） | Questioner（写下轮 query）+ Reward judge（判完成度） |
| Questioner | `ObservationReport` + persona + 历史 | 下一轮 user query 或 `<end_session>` | 下一轮 rollout |
| Reward | `ObservationReport` + 任务 | 标量 reward | 写入 `rm_scores` |

**`ObservationReport` 两个通道**（`agents/schema.py`）：
- `state_diff` / `intermediate` / `final` — Observer 模型归纳出的**状态证据**（来自确定性 diff），judge 用它判"真实效果 = 完成度"。
- `actor_trajectory` — actor 动作文本，**pass-through**：由 observer 组件携带给 reward judge 判过程/安全，但**从不进 observer 模型的 prompt**（省 token）。

## 3. diff 驱动的抗 reward-hacking 设计

Observer 的证据是**代码算出来的**，不是模型读 actor 声称的。两条证据通道（`agents/observer.py`）：

- **FS diff** — 本轮创建/修改/删除的文件，**带内容**；xlsx/docx/pptx/pdf 等富格式会在沙箱内提取成文本，所以"slide 3 写了 X"/"单元格 B2 = 12345"可核对，不是不透明字节。
- **SYS diff** — 非文件系统效果：本轮装的包、开的端口、起的进程（SysOps 类任务）。

actor 的自述只作为 **claims** 交叉核对（填 `discrepancies`）。为什么 diff-driven 而非 claim-driven：actor 叙事会幻觉出不存在的文件/值，只有环境 diff 是 ground truth；claims 只报结果、漏中间产物。

**奖励的多层拦截**（`agents/reward.py`）：本轮若无任何效果（空 diff、`has_effect=False`）→ **短路返回 0 分、不调用 judge**（改了个寂寞的轮次白得完成度 0，同时省掉昂贵的 judge 往返）。

**verifier**（`agents/verifier.py`）：对 data-analysis 类任务（读 CSV/XLSX → 出报告），纯文本 judge 看不到工具返回值会瞎扣分。verifier 是同一个 correctness judge，但在打分时**手握工具去查活着的沙箱**（`_score_all_slots` 里沙箱尚未销毁），单 LLM 工具循环核实数字。

## 4. rollout 如何注入 verl（不 fork）

verl 0.8.0 有官方注入点（`ray_trainer.py`）：把
`actor_rollout_ref.rollout.agent.agent_loop_manager_class` 设成一个 FQN，verl 用它替换默认 `AgentLoopManager`，**不碰 `fit()`**。

- 我们的类：`trainer/agent_rollout_manager.py`（`AgentSchedulerAgentLoopManager`，导出别名 `AgentLoopManager`），只 override `generate_sequences`。
- verl 懒加载（在 `create`/装配时才 import verl），所以模块能在无 verl 的机器上 import；`trajectories_to_dataproto` 和 prompt 抽取是纯函数，用 fake 单测。
- 自定义 rollout 的运行参数（如 `sessions_per_step`）在顶层 `agent_rl:` 段，只被 `agent_rollout_manager.py` 读，verl 忽略。

## 5. reward 如何流动

**当前是 rollout 内联算好**：`generate_sequences` → `_score_all_slots(observer diff + verifier + judge)` → `t.reward` → `trajectories_to_dataproto` 写 `rm_scores`。verl 直接读 `rm_scores`（`use_rm=False`），因此**从不调用 reward manager**——`base.yaml` 里 `reward_manager` 是 `naive`（既然 `rm_scores` 已存在就永不触发）。

> `src/trainer/observer_reward_manager.py` 是**未接线的备选方案**（把 reward 走 verl RewardLoopWorker + ObserverRewardManager 的路径），保留作参考，当前不运行。若要启用需同时让 `generate_sequences` 停写 `rm_scores`，否则双重奖励。

judge 本体：`trainer/model_reward.py::JudgeClient`（OpenAI 兼容的冻结 judge），模型由 env 解析（`JUDGE_API_BASE`/`REWARD_API_BASE` + `MODEL`），不写死；截断防护抛 `TruncatedOutputError` 由各消费方分流。

## 6. 关键文件速查

| 要改 | 文件 |
|------|------|
| 训练入口 / CLI override | `src/trainer/agent_rl_main.py` |
| verl runner（构建 RayPPOTrainer、std 指标） | `src/trainer/agent_rl_runner.py` |
| 自定义 rollout（行数契约、DataProto 装配） | `src/trainer/agent_rollout_manager.py` |
| Observer diff / 快照探针 | `agents/observer.py` |
| Questioner 人设 / 多轮 / patience | `agents/questioner.py` |
| reward 打分 / 短路门控 | `agents/reward.py` + `src/trainer/model_reward.py` |
| verifier 工具循环 | `agents/verifier.py` |
| 共享数据结构（ObservationReport / Persona） | `agents/schema.py` |
| 会话调度 / 沙箱客户端 / 采集 | `src/rollout/` |
| 单步生成边界 | `src/inference/generate.py` |
| verl 稳定性 patch（dataproto/entropy/padding/empty_batch/pause/sp_gather 等） | `src/trainer/*_patch.py` |

## 7. 配置

- **继承**：`configs/run/agent_rl_4gpu.yaml` 用 `defaults: [../base]` 合并 `configs/base.yaml`（OmegaConf，解析在 `agent_rl_main.py`）。命令行 `key=value` / `--lr` 最高优先级。
- **4 卡 debug config**：小模型（Qwen3.5-9B via env `MODEL_PATH`）、local 沙箱、`total_training_steps=4`、16 query/step、console-only logger、`save_freq` 大于总步数故不产 checkpoint。
- 自定义 rollout 段在顶层 `agent_rl:`；verl 全量默认在 `configs/_generated_ppo_trainer.yaml`。

## 8. 测试

CPU 单测 `pytest`：**217 passed, 19 skipped**（skip = torch/verl/GPU-gated）。单测用 AFS miniconda3 python 即可，无需 GPU。全栈（真实 verl DataProto + LLM server + 沙箱）只能在多卡机上验证。
