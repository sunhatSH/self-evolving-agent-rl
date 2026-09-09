# 迁移规划:agentic_cl_research → self-evolving-agent-rl

**目标**:从 CL 研究仓库复制出一个「自进化多 Agent RL 系统」毕设项目,**完全不含持续学习(CL)代码**。
原仓库 `agentic_cl_research` 保持不动。本项目 = 多 Agent 采样 + 沙箱环境 + diff 驱动奖励 + 标准 GRPO 训练(验证系统生效)。

## 一、去 CL 边界(哪些删、哪些留、哪些改名)

### 删除(CL 专属)—— 已完成
- `src/replay_buffer/`(9 桶 buffer)
- `src/trainer/`: cl_loss / cl_main / cl_eval / cl_agent_dataset / cl_replay_hook_v1 /
  replay_batch / replay_forward / replay_metrics / replay_num_tokens_patch / domain_tagging
- `src/trainer/verl_runner.py`(CL 版 runner,依赖 cl_loss/replay_*)→ 被 `agent_rl_runner.py` 取代
- `src/trainer/verl_async_runner.py`(fully-async 掺回放行)
- `src/trainer/trajectory_adapter.py` / `trajectory_adapter_v1.py`(抽轨迹入 buffer,依赖 domain_tagging)
- 对应 CL 测试(test_bucket/eviction/priority/sampler/weighting/store/replay_*/cl_loss/warmup 等)

### 保留(系统通用,零 CL 依赖)
- `agents/`(observer / questioner / reward-judge / verifier / personas / base)—— **多 Agent 核心**
- `src/rollout/`(session_pool / scheduler / collect / sandbox_client / simulated_session)
- `src/inference/`(generate 边界)
- `src/trainer/` 通用件:model_reward* / observer_hook* / observer_reward_manager /
  verifier_hook / live_messages / mkdir_deliverable_hook / 各 verl 稳定性 patch
  (dataproto/entropy/padding/empty_batch/image_drop/pause/sp_gather)
- `docker/sandbox/`、`scripts/`(采集/沙箱/serve)、`skills/`

### 改名(去 CL 命名,不改逻辑)
- `src/trainer/cl_rollout_manager.py` → `agent_rollout_manager.py`
  - class `CLSchedulerAgentLoopManager` → `AgentSchedulerAgentLoopManager`
  - 它零 CL import,是「session scheduler + observer diff 注入」的 rollout 管理器
- 新增 `src/trainer/agent_rl_runner.py`(已写)+ `agent_rl_main.py`(已写)
- config 里 `trainer.cl_rollout_manager.AgentLoopManager` FQN → `trainer.agent_rollout_manager.AgentLoopManager`

## 二、config 去 CL
- `configs/base.yaml`:删 `cl:` 整段(9桶/quota/priority/replay/weighting);
  保留 model / data / actor_rollout_ref / reward / trainer / sandbox 段
- `configs/run/`:只保留 1 个可跑的 4 卡 config(16 query/batch),其余 CL 实验 config 删
- 新增 `configs/run/agent_rl_4gpu.yaml`(16 query/batch,total_training_steps=4,debug 用)

## 三、子 Agent 模块边界(互不重叠的文件所有权)

> 地基(删文件 / 改 base.yaml / 改名 rollout_manager)由主 Agent 先做完,再派子 Agent。

| 子Agent | 独占文件范围 | 任务 |
|---|---|---|
| A. pyproject/包 | pyproject.toml、src/trainer/__init__.py、tests/__init__.py | 改包名/描述、清理指向已删模块的引用、确保可 import |
| B. configs | configs/base.yaml、configs/run/agent_rl_4gpu.yaml、configs/cluster.yaml | 去 cl 段、写 4 卡 debug config、改 FQN |
| C. 训练脚本 | scripts/train_4gpu.sh、scripts/_train_impl.sh、scripts/env/* | 指向 agent_rl_main、去 CL env |
| D. 测试清理 | tests/(除已删) | 删/改指向已删模块的 test,跑通 CPU 单测 |
| E. 文档/README | README.md、OVERVIEW.md、CLAUDE.md、doc/ | 重写为系统项目叙事,去 CL |

## 四、验证关口
1. `python -c "import trainer.agent_rl_runner, trainer.agent_rl_main"` 不报错(CPU)
2. `pytest`(CPU 单测)全绿或仅 skip(verl/GPU)
3. GPU 空闲后:`bash scripts/train_4gpu.sh configs/run/agent_rl_4gpu.yaml`(4 step,验证能跑)

## 五、多 Agent 系统已知坑(4 卡 debug 会撞,来自原仓库 bug 总表)
C1 rollout×8 行数(per-row 每行1条) / C2 rm_scores 没写 / C3 verl 拒自定义键 /
C4 没请求 logprob→ppo_kl=0 / C7 observer hook FQN 传不到 actor / B4 KV 池 OOM(降并发) /
D1 副本少起1个 hang(--num-cpus=nproc) / E1 GatewayActor jemalloc / E3 e2b HTTP/2 GOAWAY /
E4 reward 恒0(judge key 没进 worker + thinking judge max_tokens 太小) / 截断防护 / F8 写盘路径
