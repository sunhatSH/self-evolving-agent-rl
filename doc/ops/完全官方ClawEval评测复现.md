# 完全官方 ClawEval 评测复现（Hermes 训练模型 → 官方 harness）

> 2026-08-29 跑通。目标：用**完全官方的方式**（官方 agent harness + 官方沙箱/mock_services
> + 官方 grader + 官方 audit_data）评测我们训练的模型（Qwen3.5-9B），对比之前的"半对齐"成绩。

## 为什么做

之前评测链路（`src/claw_eval_vendor` + `claw_eval_hermes/grade.py`）是"半对齐"：
- 用了官方 per-task grader.py + 公式 + LLM judge 主观分
- 但 `audit_data=None`（safety/部分 completion 判定丢失）、`response_status` 恒 200（robustness 恒 1.0）
- judge 用 gpt-5.6-luna（官方 gemini/claude）

半对齐成绩见 `eval/results/HALF_ALIGNED_RESULTS.md`。

完全官方 = 用官方仓库 `/tmp/claw-eval-official`（`claw-eval/claw-eval`）的完整 harness，
让 agent 用官方沙箱工具 + mock_services 审计日志，grader 拿到完整 audit_data。

## 关键组件

| 组件 | 半对齐 | 完全官方 |
|---|---|---|
| agent 工具 | Hermes（腾讯沙箱） | 官方 mock_services（web_search/web_fetch/Bash 等） |
| audit_data | None | 官方 mock_services 审计日志 |
| grader | 官方 grader.py（半） | 官方 grader.py（完整 audit） |
| robustness | 恒 1.0（response_status 假 200） | 真实（tool dispatch 的 response_status） |
| safety | 恒 1.0（audit_data=None） | 真实（audit 检查） |
| judge / user_agent | gpt-5.6-luna | gpt-5.6-luna（tokenhub） |

## 复现步骤

### 1. 起 Qwen3.5-9B OpenAI-compatible serve（LightLLM）

Qwen3.5-9B 是 GDN 混合架构，vLLM 0.13.0 不支持（无 qwen3_next 模块），必须用 LightLLM
（`lightllm/models/qwen3_5/` 自带支持）。

```bash
# /tmp/llm_serve.sh
export PATH=/mnt/afs_toolcall/sunhao4/.local/bin:/opt/conda/bin:$PATH
export PYTHONPATH=<LightLLM>:/mnt/afs_toolcall/sunhao4/dependencies/verl:<repo>/src:<repo>
export VLLM_GDN_PREFILL_BACKEND=triton
export NCCL_CUMEM_ENABLE=0
export TEXT_MODEL_ONLY=1
python -m lightllm.server.api_server \
  --model_dir /mnt/afs_toolcall/sunhao4/models/Qwen3.5-9B \
  --tp 2 --dp 1 --mem_fraction 0.75 \
  --tokenizer_mode fast --tool_call_parser qwen3_coder --reasoning_parser qwen3 \
  --max_req_total_len 32768 --host 0.0.0.0 --port 8000
```

⚠️ 坑：
- hypercorn 装到 `~/.local/bin`（user site），PATH 要加 `~/.local/bin`
- `--max_req_total_len` 至少 32768（8192 会 APIError：multi-turn 任务 prompt 累积超 8k）
- 起 serve 用**普通用户 nohup**（sudo 的 PATH 环境会导致 hypercorn 找不到）

### 2. 写官方 config（模型→本地 serve，judge/user_agent→tokenhub）

```yaml
# /tmp/claw-eval-official/config_ours.yaml
model: { api_key: dummy, base_url: "http://127.0.0.1:8000/v1", model_id: Qwen3.5-9B, context_window: 8192 }
judge: { api_key: "${TOKENHUB_API_KEY}", base_url: "https://tokenhub.sensetime.com/v1", model_id: gpt-5.6-luna, enabled: true }
user_agent_model: { api_key: "${TOKENHUB_API_KEY}", base_url: "https://tokenhub.sensetime.com/v1", model_id: gpt-5.6-luna }
defaults: { trace_dir: traces, tasks_dir: tasks }
```

⚠️ multi-turn 任务必须配 `user_agent_model`（模拟用户），否则 AuthenticationError 30 次重试。

### 3. 跑 batch

```bash
cd /tmp/claw-eval-official
export TOKENHUB_API_KEY=...
export PYTHONPATH=src
python -m claw_eval.cli batch --config config_ours.yaml --sandbox-tools \
  --trials 3 --tag general --parallel 8 --trace-dir /tmp/claw_traces_full
```

- `--tag general` = 199 个纯文本任务（非 multimodal）
- `--sandbox-tools` = 本地沙箱（不 Docker），ServiceManager 自动起 mock_services
- 入口是 `python -m claw_eval.cli`（不是 `python -m claw_eval`，无 `__main__.py`）

### 4. 汇总

```bash
python score_summary.py /tmp/claw_traces_full
# 输出 AvgScore / AvgPass / AnyPass / AllPass
```

## 结果

完全官方成绩（`python score_summary.py /tmp/claw_traces_full`）：

| 指标 | 半对齐 | 完全官方 |
|---|---|---|
| AvgScore | 0.209 | **0.473** |
| AvgPass | 15/197 (7.6%) | **39/197 (19.8%)** |
| AnyPass | 21/197 | 67/197 |
| AllPass | 14/197 | 36/197 |

> 完全官方 AvgScore 翻倍（0.209→0.473）。原因：半对齐时 completion 只有 LLM 主观分
> （无 ground truth answer_key 规则 + audit_data），分数被系统性压低；完全官方对齐后
> completion 有 ground truth 规则（answer_key 比对）+ audit_data，分数更准确。
> robustness/safety 在完全官方下是真实的（半对齐恒 1.0 失真）。

⚠️ 剩余 ~25 个 research 类任务（T045 cve_research、C04 image_processing、C07 financial_valuation 等）
<3 trials：base 未训练模型在 research 任务上无限搜索，context 爆炸到 20-40 万 tokens，grader/judge
打分失败。这是模型能力问题（base 不会收敛），不是评测链路 bug。已训好的模型（baseline/kl）应
该会收敛。

## 关键发现

1. 官方 harness 的确定性规则（robustness/safety）依赖 mock_services 审计日志，半对齐时这些恒 1.0 失真。
2. Qwen3.5-9B serve 的 `max_req_total_len` 必须够大（multi-turn 任务 prompt 累积超 8k，32768 够用）。
3. 官方 grader 的 completion 是规则（ground truth）+ LLM 混合，base 未训练模型会澄清但完不成任务。
4. research 类任务（T04x/T05x）容易让 base 模型无限搜索，context 爆炸——训好的模型应该收敛。
