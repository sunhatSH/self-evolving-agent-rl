# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库性质

毕设项目：**自进化的多 Agent 强化学习系统**。仓库所有者：@孙豪。

系统 = **多 Agent 采样**（沙箱内 ReAct actor + diff 驱动的 Observer + 人设驱动的 Questioner）
+ **diff 驱动奖励**（外部冻结 LLM judge 把完成度锚定在 Observer 的真实状态 diff 上，抗 reward hacking）
+ **标准 GRPO 训练**（verl `0.8.0`，pip 安装不 fork，官方注入点接自定义 rollout）。

> **本仓库不含任何持续学习（CL）机制**：没有回放 buffer、没有 CL loss（L_replay/KL/U 形权重）、没有防遗忘评测、没有分桶。那部分留在原始 CL 研究仓库。**不要在这里描述或引入任何 CL 内容。** 训练只用于验证系统端到端跑通（rollout → reward → PPO 更新），不是研究贡献，不追 SOTA。

架构详见 [`OVERVIEW.md`](OVERVIEW.md)，入口见 [`README.md`](README.md)。

## 硬性规则（必读）

### 采集 / 长任务用 tmux/nohup

**采集数据、训练等长时间运行的任务，必须用 tmux 或 nohup 开后台，绝对不许前台运行。**
前台跑会随会话断开被杀，浪费几小时的计算和配额。

```bash
tmux new -d -s <name> 'bash scripts/<任务>.sh'   # 启动
tmux attach -t <name>                            # 查看
```

### 两个 Python

| 用途 | Python | 说明 |
|------|--------|------|
| **训练 / 全栈 smoke** | `/opt/conda/bin/python3` | 有 torch/verl，跑 `train_4gpu.sh` / `agent_rl_main`（脚本内已写死）。 |
| **CPU 单测** | AFS miniconda3 python | 无 torch/verl/GPU，跑 `pytest`（217 passed, 19 skipped）。 |

## 开发命令

```bash
# 安装（含开发依赖，src-layout：src/ + agents/ 双根）
pip install -e ".[dev]"

# CPU 单测（本机无 torch/verl/GPU：217 passed, 19 skipped，skip 全是 torch/verl/GPU-gated）
pytest
pytest tests/test_xxx.py::test_yyy -v          # 单个测试

# Lint / 格式化 / 类型
ruff check .              # ruff check --fix . 自动修复
black .                   # black --check . 仅检查
mypy src/trainer/

# 训练入口（直接调用；训练 python 必须是 /opt/conda/bin/python3）
/opt/conda/bin/python3 -m trainer.agent_rl_main --config configs/run/agent_rl_4gpu.yaml

# 4 卡 debug 冒烟（4 step，验证 rollout→reward→GRPO 更新能跑通，不产出结果）
# 长任务放 tmux，不要前台！
tmux new -d -s smoke 'bash scripts/train_4gpu.sh configs/run/agent_rl_4gpu.yaml'
```

> **凭证**：训练/沙箱凭证从 gitignored 的 env 文件 / 环境变量取（judge 走 `JUDGE_API_BASE`/`REWARD_API_BASE` + `MODEL`；沙箱腾讯云凭证从 `docker/sandbox/*.env`），从不在代码里硬编码。无沙箱凭证时用 `sandbox_backend: local`（4 卡 debug config 默认）。

## 代码架构

```
configs/run/agent_rl_4gpu.yaml  (OmegaConf: base.yaml → 实验 override)
        │
        ▼
trainer/agent_rl_main.py ──► trainer/agent_rl_runner.py   (构建 verl RayPPOTrainer，标准 GRPO)
        │
        ▼
verl 原生 fit() ──generate_sequences──► trainer/agent_rollout_manager.py
   (verl 已按 rollout.n 复制 query)        每行 = 1 次沙箱 rollout：
        │                                    rollout/(actor+调度+沙箱) + agents/observer(diff) + agents/reward+verifier(judge)
        ▼                                    │
   PPO/GRPO 更新  ◄────── rm_scores ────────┘  (reward 在 rollout 内联算好，写 rm_scores，verl 直接读)
```

关键接线（改这些前先看 `OVERVIEW.md` §4/§5）：

- **rollout 注入**：`actor_rollout_ref.rollout.agent.agent_loop_manager_class = trainer.agent_rollout_manager.AgentLoopManager`。verl 用它替换默认 rollout，`fit()` 零改动。
- **自定义 rollout 配置**：顶层 `agent_rl:` 段，只被 `agent_rollout_manager.py` 读，verl 忽略。
- **行数契约**：verl 拥有 ×n 复制和 GRPO 分组，`generate_sequences` 每个输入行只回**恰好 1 条**轨迹、按序、不自造 uid。
- **奖励**：reward 在 rollout 内联算好（observer diff + verifier + judge → `t.reward` → `rm_scores`），verl 直接读（`use_rm=False`），**从不调用 reward manager**（`base.yaml` 的 `naive` reward_manager 永不触发）。`observer_reward_manager.py` 是未接线的备选，保留作参考。
- **奖励抗 hacking**：judge 把完成度锚定在 Observer 的确定性 before/after diff（FS diff 带内容 + SYS diff），actor 自述只作交叉核对；空 diff 短路返回 0 分不调 judge。

模块与 verl 的解耦：`rollout/`、`inference/`、`agents/` 不 import verl；`agent_rollout_manager.py` 懒加载 verl，纯函数（`trajectories_to_dataproto` 等）用 fake 单测，故本机可 import 可测。

## 编码规范

- Python ≥ 3.10，ruff line-length=110，black line-length=110
- ruff 启用：E, F, W, I(isort), B(bugbear), UP(pyupgrade)；`E501` 忽略（由 black 管）
- 训练配置用 OmegaConf/yaml，实验 yaml 通过 `defaults: [../base]` 继承 `configs/base.yaml`（解析在 `trainer/agent_rl_main.py`）
- `bin/` 是独立数据管道工具（自有风格，ruff/black 已 `extend-exclude` 排除），不套项目规范、不当可 import 的库

## 目录结构

```
self-evolving-agent-rl/
├── CLAUDE.md                # 本文件，AI 协作指南
├── README.md                # 项目入口
├── OVERVIEW.md              # 架构 / 设计深入
├── pyproject.toml           # 元数据 / 依赖（src-layout：src/ + agents/ 双根；pythonpath=["src","."]）
├── src/
│   ├── trainer/             #   agent_rl_main / agent_rl_runner / agent_rollout_manager
│   │                        #   + model_reward(_omni) / observer_hook(_register) / verifier_hook
│   │                        #   + observer_reward_manager(备选,未接) / live_messages / mkdir_deliverable_hook
│   │                        #   + verl 稳定性 patch（dataproto/entropy/padding/empty_batch/image_drop/pause/sp_gather）
│   ├── rollout/             #   scheduler / session_pool / collect / sandbox_client / simulated_session
│   ├── inference/           #   单步生成边界（VerlRolloutGenerateFn / HTTP）
│   ├── rewardmodel_choose/  #   reward 模型选型 sweep（一次性分析）
│   ├── claw_eval_hermes/    #   ClawEval 评测（Hermes 路径）
│   └── claw_eval_vendor/    #   ClawEval 评测（vendor 路径）
├── agents/                  # 多 Agent 核心：observer / questioner / reward(judge) / verifier / personas / base / schema
├── configs/                 # base.yaml + run/agent_rl_4gpu.yaml + _generated_ppo_trainer.yaml(verl 默认) + sandbox_*.json
├── scripts/                 # train_4gpu.sh(4 卡冒烟) / _train_impl.sh / env/ / collect/ / sandbox/ / serve/ / eval_*.sh
├── docker/sandbox/          # 沙箱镜像构建
├── doc/                     # 设计 / 运行文档（沙箱与 Agent 部分仍适用；CL 相关的 source/ 与本项目无关）
└── tests/                   # CPU 单测（+ torch/verl/GPU-gated skip）
│
│ ─── 运行时产物（gitignored）───
├── ckpts/  logs/  wandb/    # checkpoint / 日志 / 追踪
```

### 模型存放约定

| 类别 | 位置 | 说明 |
|------|------|------|
| **基座模型** | 仓库外，绝对路径 | configs 默认 **Qwen3.5-9B**（`configs/base.yaml`），4 卡 debug 与 16 卡正式均用 9B。 |
| **训练 checkpoint** | `ckpts/<实验名>-step-<N>/` | trainer 写入（4 卡 debug 的 `save_freq` 大于总步数故不产）。 |

所有运行时产物在 `.gitignore`，不提交 git。

## 沙箱与文档

- **沙箱后端解耦**：`SandboxClient` Protocol = 接口契约，`register_backend`/`make_sandbox` = 按名选择的注册表。`local`（本机 debug）与 `e2b`（腾讯云，需凭证）为真实现，其余厂商留 stub。换/加厂商零改调用方。
- **接口怎么用 / 三 Agent 报告与声明怎么消费**：先读 [`doc/ops/sandbox/接口使用_Sandbox与三Agent.md`](doc/ops/sandbox/接口使用_Sandbox与三Agent.md)（Sandbox 后端 + `ObservationReport`/`actor_claims`/Questioner + claim→diff 取证设计）。
- 沙箱运行手册在 `doc/ops/sandbox/`（概念、冒烟、Dockerfile、调度）。

> `doc/source/` 下的 `CL_Design.md`/`BucketAlgorithm.md`/`usersim.md` 等以及 `skills/` 中带 CL 字样的条目是**原始 CL 研究仓库的遗留**，与本项目无关，不要据此改本仓库代码。

## 术语

| 术语 | 含义 |
|------|------|
| verl | 使用的 RL 训练框架（0.8.0，pip 装不 fork） |
| GRPO | 使用的 RL 算法 |
| actor | 被训练的策略（沙箱内 ReAct） |
| Observer | 产出确定性 before/after diff 的 agent（reward 的 ground truth） |
| Questioner | 人设驱动的模拟用户 agent（多轮 query） |
| judge | 外部冻结 LLM，按 Observer diff 给完成度打分 |
| `ObservationReport` | Observer 产出的客观状态报告（`agents/schema.py`），Questioner + reward judge 共两个消费方 |
| diff-driven | 奖励锚定在环境真实 diff 而非 actor 自述——抗 reward hacking 的核心 |

## 分工

本项目由 @孙豪 独立完成：多 Agent 采样、沙箱环境、diff 驱动奖励、GRPO 训练链路、评测。
