# Self-evolving multi-agent RL system

毕业设计项目：一个**自进化的多 Agent 强化学习系统**。系统由三部分咬合而成——

1. **多 Agent 采样**：一个 ReAct actor 在代码沙箱里执行工具动作；一个 **Observer** agent 以沙箱前后状态的确定性 diff 产出 `ObservationReport`（不是复读 actor 的自述）；一个 **Questioner** agent 用人设驱动多轮用户模拟。
2. **diff 驱动的奖励**：一个外部冻结的 LLM judge 把"任务是否完成"锚定在 Observer 的**真实状态 diff** 上，而不是 actor 的声称——以此抵抗 reward hacking。
3. **标准 GRPO 训练**：在 [verl](https://github.com/volcengine/verl) `0.8.0`（pip 安装，**不 fork**）上用原生 PPO/GRPO 目标训练，通过 verl 官方注入点接入自定义 rollout。

> **训练本身只是为了验证系统端到端跑通（rollout → reward → PPO 更新），不是研究贡献，也不追 SOTA。** 本仓库**不含任何持续学习（CL）机制**——没有回放 buffer、没有 CL loss、没有防遗忘评测；那部分留在原始 CL 研究仓库。

## 架构一览

```
                 configs/run/*.yaml  (OmegaConf: base.yaml → 实验 override)
                          │
                          ▼
       trainer/agent_rl_main.py ──► trainer/agent_rl_runner.py
                          │            (构建 verl RayPPOTrainer，标准 GRPO)
                          ▼
   verl 原生 fit() ──generate_sequences──► trainer/agent_rollout_manager.py
      (verl 已按 rollout.n 复制 query)         AgentSchedulerAgentLoopManager
                          │                        │  每行 = 一次沙箱 rollout
                          │                        ├─ rollout/  actor + 会话调度 + 沙箱
                          │                        ├─ agents/observer  沙箱 before/after diff
                          │                        └─ agents/reward+verifier  judge 打分
                          ▼                        ▼
                  PPO/GRPO 更新  ◄── rm_scores ── DataProto（含 observer_report）
```

- **rollout 注入点**：`actor_rollout_ref.rollout.agent.agent_loop_manager_class = trainer.agent_rollout_manager.AgentLoopManager`。verl 用它替换默认 rollout，`fit()` 零改动。
- **自定义 rollout 配置**：顶层 `agent_rl:` 段（只被 `agent_rollout_manager.py` 读，verl 忽略）。
- **奖励**：训练时 reward 在 rollout 内联算好（observer diff + verifier + 外部 judge → `t.reward`），写进 `rm_scores`，verl 直接读（`use_rm=False`）。judge 走 `trainer/model_reward.py::compute_score`，模型由 env 解析（`JUDGE_API_BASE`/`REWARD_API_BASE` + `MODEL`），不写死。

## 快速开始

```bash
# 1. 安装（含开发依赖，src-layout：src/ + agents/ 双根）
pip install -e ".[dev]"

# 2. 跑 CPU 单测（本机无 torch/verl/GPU 时：217 passed, 19 skipped）
#    单测用 AFS miniconda3 python 即可，无需 GPU 环境。
pytest

# 3. 4 卡 debug 冒烟（4 step，验证 rollout→reward→GRPO 更新能跑通，不产出有意义结果）
#    需要有 torch/verl 的训练 python（/opt/conda/bin/python3，脚本内已写死）。
#    长任务务必放 tmux/nohup，不要前台跑。
tmux new -d -s smoke 'bash scripts/train_4gpu.sh configs/run/agent_rl_4gpu.yaml'
tmux attach -t smoke

# 训练入口也可直接调用
/opt/conda/bin/python3 -m trainer.agent_rl_main --config configs/run/agent_rl_4gpu.yaml
```

- **基座模型**：configs 默认 Qwen3.6-27B（`configs/base.yaml`）；4 卡 debug config 用小模型 Qwen3.5-9B（经 env `MODEL_PATH` 指定）。
- **沙箱后端**：`local`（本机，debug 默认，无凭证）或 `e2b`（腾讯云，需凭证）。见 `doc/ops/sandbox/`。

## 仓库结构

```
.
├── README.md                # 本文件，项目入口
├── OVERVIEW.md              # 架构 / 设计深入（采样环、三 Agent 契约、reward 流）
├── CLAUDE.md                # AI 协作指南（开发命令 + 架构 + 规范）
├── pyproject.toml           # 项目元数据 / 依赖（src-layout）
├── src/                     # 库包（PYTHONPATH 含 src/）
│   ├── trainer/             #   训练入口 + verl runner + 自定义 rollout manager + reward + verl 稳定性 patch
│   ├── rollout/             #   采样侧：会话池 / 调度 / 采集 / 沙箱客户端 / simulated_session
│   ├── inference/           #   单步生成边界（VerlRolloutGenerateFn）
│   ├── rewardmodel_choose/  #   reward 模型选型 sweep（一次性分析）
│   ├── claw_eval_hermes/    #   ClawEval 评测（Hermes 路径）
│   └── claw_eval_vendor/    #   ClawEval 评测（vendor 路径）
├── agents/                  # 多 Agent 核心：observer / questioner / reward(judge) / verifier / personas / base
├── configs/                 # 配置（base.yaml + run/agent_rl_4gpu.yaml + verl defaults + sandbox）
├── scripts/                 # 训练 / 评测 / 沙箱 / 采集脚本（train_4gpu.sh 是 4 卡冒烟入口）
├── docker/                  # 沙箱镜像构建
├── doc/                     # 设计 / 运行文档
└── tests/                   # CPU 单测（+ torch/verl/GPU-gated skip）
```

## 分工

本项目由 @孙豪 独立完成：多 Agent 采样、沙箱环境、diff 驱动奖励、GRPO 训练链路、评测。
