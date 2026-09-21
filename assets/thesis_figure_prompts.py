"""毕业论文配图提示词 — 10 张图(图2 sys_run.png 已有, 此处 fig1/3-11).

每条: {key, title(图名), prompt(英文, gpt-image 对英文更稳)}.
生成脚本 scripts/gen_thesis_figures.py 读此文件, 调 tokenhub gpt-image-2.5-flare
生成 PNG 存 assets/fig_<key>.png.

风格统一: flat vector diagram / academic figure, white background, minimal,
clean sans-serif labels, muted professional color palette. 三个 Agent 用固定色:
Actor=蓝, Observer=绿, Questioner=橙.
"""

_STYLE = (
    "Flat vector academic diagram, white background, clean minimal style, "
    "sans-serif labels, muted professional colors, no photorealism, no clutter, "
    "high contrast, publication quality for a master's thesis. "
    "Color convention: Actor agent = blue, Observer agent = green, "
    "Questioner agent = orange, sandbox = light gray, reward judge = purple."
)

FIGURES = [
    {
        "key": "fig2_dataflow_zh",
        "title": "图2 数据-训练完整流程(中文版)",
        "prompt": (
            "一张自进化强化学习系统的端到端流程图, 从左到右分阶段排列, 用大箭头连接. "
            "所有文字标签必须是简体中文, 字体清晰规整. "
            "阶段1「种子(输入)」: 超采样规模 S 从这里进入. 两个入口箭头: 左侧小箭头标注"
            "『仅第1步: S=2N(简单初始任务)』, 下方大曲线箭头标注『第2步起: S=R(上一步存活组)』. "
            "阶段2「采样(Rollout)」: S 个查询每个生成 8 条轨迹, 在沙箱里由蓝色 Actor 跑 ReAct, "
            "产生 S×8 条轨迹和沙箱状态. "
            "阶段3「观察(Observer)」: 绿色 Observer 计算确定性的前后状态差分(不用大模型). "
            "阶段4「奖励(Reward)」: 紫色冻结大模型裁判, 基于差分给每条轨迹打分(差分驱动, 抗奖励作弊). "
            "阶段5「淘汰(Eliminate)」: 丢弃最优奖励同时满足『后20%且低于0.5』的组, 剩下 R 组(至少保留80%). "
            "阶段6「选组(Select)」: 计算优势, 选梯度最强的 N 组(N×8)做 GRPO 更新 Actor 策略. "
            "底部一条大曲线反馈箭头, 标题『跨步自进化』, 从 R 组回流到阶段1: "
            "恢复沙箱文件状态(状态继承), Observer 写执行概括, Questioner 生成下一步种子. "
            "右下角增加一个青色方框『失败案例自演化』: 收集失败/异常轨迹 → 大模型归因(模型问题 or 基建问题) "
            "→ 分别热更新提示词 / 动态扩展基建. 每10步或20例触发一次, 用虚线箭头接回阶段1和奖励裁判. "
            "最右侧一个小监视器框『训练崩溃即停止: 奖励标准差→0, 优势方差→0, pg_loss出现NaN, ppo_kl爆炸』. "
            "阶段编号1-6, 中文标签, 每个 Agent 用不同颜色的框. " + _STYLE
        ),
    },
    {
        "key": "fig2_dataflow",
        "title": "图2 数据-训练完整流程(重绘)",
        "prompt": (
            "A large end-to-end flow diagram of a self-evolving reinforcement learning "
            "pipeline, laid out left-to-right in clear stages with big arrows. "
            "STAGE 1 SEED (INPUT): the oversample size S enters here. Show two labeled "
            "entry arrows into this stage: a small one from the left 'Step 1 only: S = 2N "
            "(simple initial tasks)' and a big curved one from the feedback loop below "
            "'Step 2+: S = R (surviving groups from previous step)'. Make it visually clear "
            "that S = 2N is ONLY the first step's cold start, and from step 2 onward S = R. "
            "STAGE 2 ROLLOUT: each of the S queries spawns 8 trajectories inside sandboxes "
            "(blue Actor running ReAct), producing S x 8 trajectories and sandbox states. "
            "STAGE 3 OBSERVE: a green Observer computes deterministic before/after state diff "
            "(no LLM). "
            "STAGE 4 REWARD: a purple frozen LLM Judge scores each trajectory grounded on the "
            "diff (diff-driven, anti reward-hacking). "
            "STAGE 5 ELIMINATE: drop groups whose best reward is BOTH bottom-20% AND below 0.3, "
            "leaving R groups (>=80% survive). "
            "STAGE 6 SELECT: compute advantage, pick the N gradient-strongest groups (N x 8) "
            "for GRPO update of the Actor policy. "
            "Then a big curved feedback arrow labeled 'CROSS-STEP SELF-EVOLUTION' loops from "
            "the R groups back into STAGE 1 as the next step's input: for each surviving group, "
            "restore its sandbox file state (state inheritance), the green Observer writes an "
            "LLM execution summary, and the orange Questioner generates the next-step seed "
            "query. Label the loop output clearly 'S = R (feeds back to STAGE 1)'. "
            "At the far right a small monitor box 'STOP when training collapses: reward std->0, "
            "advantage variance->0, pg_loss NaN, ppo_kl explodes'. "
            "Number the stages 1-6, use clean English labels, distinct colored boxes per agent. "
            + _STYLE
        ),
    },
    {
        "key": "fig1_architecture",
        "title": "图1 系统总体架构",
        "prompt": (
            "System architecture diagram of a self-evolving multi-agent reinforcement "
            "learning system. Center: a Sandbox (light gray rounded box) containing an "
            "Actor agent (blue, running a ReAct loop with tools). Around it: an Observer "
            "agent (green, produces deterministic before/after state diff) and a Questioner "
            "agent (orange, persona-driven, generates new tasks). A frozen Reward Judge "
            "(purple, external LLM) scores trajectories grounded on the Observer's diff. "
            "A GRPO Trainer box updates the Actor policy. Arrows show: Actor executes in "
            "sandbox, Observer captures diff, Judge scores, Trainer updates Actor, Questioner "
            "feeds new tasks back. ADD a Failure-Case Self-Evolution module (teal rounded box, "
            "bottom): it collects failed/anomalous trajectories, an LLM attributes each to "
            "either a MODEL issue (dashed arrow updates the Judge/Questioner/Actor prompts) "
            "or an INFRA issue (dashed arrow expands the Sandbox tools/deps). Label it "
            "'Failure-Case Self-Evolution (evolves evaluator & infra)'. Label each component "
            "clearly in English. " + _STYLE
        ),
    },
    {
        "key": "fig3_oversample_select",
        "title": "图3 超采样-淘汰-选组机制",
        "prompt": (
            "A clean funnel-style flow diagram with three stages of group selection in RL "
            "training. NO legend row, NO agent icons, NO role labels, NO color key at the "
            "bottom whatsoever — the diagram ends after the third stage box. "
            "Stage 1 OVERSAMPLE: a large dashed-border panel labelled 'S = 32 groups "
            "(each with 8 trajectories)' containing 32 small blue bars arranged in a grid. "
            "Stage 2 ELIMINATE: a medium panel labelled 'R = 30 groups' with a caption "
            "'drop groups where MAX reward is BOTH in bottom 20% AND < 0.5'. Show 2 bars "
            "grayed-out and crossed out. Stage 3 SELECT: a smaller bright-green panel "
            "labelled 'N = 16 groups' with caption 'pick N groups with highest |advantage| "
            "mean for GRPO training'. A small annotation to the right: "
            "'S shrinks each step: 32 → 30 → 27 → 26'. "
            "Left-to-right funnel with gray arrows between stages. White background. "
            "Flat academic style, no photorealism, no decorative elements, no footer, "
            "no legend strip. " + _STYLE
        ),
    },
    {
        "key": "fig14_badcase_evolve",
        "title": "图4.5 失败案例驱动的评估器与基建自演化",
        "prompt": (
            "A clean academic flowchart for a self-evolving RL training system's failure-case "
            "attribution and evolution loop. Top center: a teal rounded box labeled "
            "'Failure-Case Buffer' with a small counter icon (collects every 10 steps or 20 cases). "
            "An arrow labeled 'Periodic trigger' points down to a central teal diamond labeled "
            "'LLM Attribution' with subtitle '(integrates task intent + trajectory + env evidence)'. "
            "From the diamond, two branches split: "
            "Left branch (orange): label 'Model Issue' → orange box 'Incremental Prompt Patch' "
            "with three sub-bullets: '• Judge prompt', '• Questioner prompt', '• Actor prompt'. "
            "Right branch (green): label 'Infra Issue' → green box 'Skill Synthesis & Infra Expansion' "
            "with three sub-bullets: '• Summarize reusable skill', '• Register tool / add dep', "
            "'• Fix harness / sandbox'. "
            "Both orange and green boxes have a curved dashed return arrow back to the main training "
            "loop box at the bottom labeled 'Next Training Step (evolved evaluator & infra)'. "
            "A separate small box on the left labeled 'Training Loop' feeds failed trajectories "
            "(red dashed arrow) into the Failure-Case Buffer. "
            "All labels in Chinese. White background. Flat vector academic style, muted colors, "
            "no photorealism. " + _STYLE
        ),
    },
    {
        "key": "fig4_self_evolve_loop",
        "title": "图4 跨step自进化闭环",
        "prompt": (
            "A circular loop diagram of cross-step self-evolution in RL. Nodes arranged in a "
            "cycle: (1) Step t best trajectory + sandbox state, (2) Sandbox State Inheritance "
            "(restore workspace files to next sandbox), (3) Observer LLM Execution Summary "
            "(green, summarizes what was done, prevents drift), (4) Questioner generates new "
            "follow-up query (orange), (5) Step t+1 new seed -> rollout again. Big curved "
            "arrows forming a closed loop. Highlight text in center: 'Except the initial seed, "
            "all subsequent queries are system-generated = self-evolving'. English labels. "
            + _STYLE
        ),
    },
    {
        "key": "fig5_diff_reward",
        "title": "图5 差分驱动奖励(抗reward-hacking)",
        "prompt": (
            "A diagram contrasting two reward grounding sources. Left: Actor's self-report "
            "(blue, a speech bubble 'I finished the task!') marked with a small warning icon "
            "(unreliable, can be gamed). Right: Observer's deterministic before/after file "
            "system diff (green, showing files added/modified with real content). A purple "
            "Reward Judge in the middle anchors its score on the Observer diff (thick solid "
            "arrow from diff) while only cross-checking the actor self-report (thin dashed "
            "arrow). Label: 'diff-driven reward resists reward hacking'. English labels. "
            + _STYLE
        ),
    },
    {
        "key": "fig6_sandbox_inherit",
        "title": "图6 沙箱状态继承机制",
        "prompt": (
            "A pipeline diagram of sandbox workspace state inheritance across training steps. "
            "Step t sandbox (light gray) with workspace files -> 'tar + base64 snapshot' box "
            "-> flows through a Transfer Queue (TQ) data channel -> Step t+1 new sandbox "
            "(light gray) where 'base64 decode + untar' restores the files before the Actor "
            "resumes. Show a small file tree (result.txt, data/report.csv, state.json) being "
            "carried over intact. Emphasize: 'Actor continues on previous step's files = true "
            "state inheritance, not just text description'. English labels. " + _STYLE
        ),
    },
    {
        "key": "fig7_sequence",
        "title": "图7 三Agent时序图",
        "prompt": (
            "A UML-style sequence diagram with 4 vertical lifelines labeled: Actor (blue), "
            "Sandbox (gray), Observer (green), Reward Judge (purple). Time flows top to bottom. "
            "Messages: Observer.prepare (snapshot baseline) -> Actor runs ReAct loop in Sandbox "
            "-> Observer.run (snapshot post + compute diff) -> Reward Judge scores using diff. "
            "Then a cross-step section: Observer produces LLM execution summary -> Questioner "
            "(orange lifeline) generates next query. Clean horizontal arrows with labels, "
            "dashed return arrows. English labels. " + _STYLE
        ),
    },
    {
        "key": "fig8_react_loop",
        "title": "图8 沙箱内Actor ReAct循环",
        "prompt": (
            "A cyclic diagram of an Actor agent's ReAct loop running inside a sandbox via a "
            "hermes CLI. Three nodes in a triangle cycle: THINK (reason about the task) -> ACT "
            "(call a tool: shell/python/file-write) -> OBSERVE (read tool output), then back to "
            "THINK. Around the cycle a light-gray sandbox boundary. Show tool icons: terminal, "
            "python, file. A small exit condition: 'until task done or max turns'. Blue accent "
            "for the Actor. English labels. " + _STYLE
        ),
    },
    {
        "key": "fig9_training_curves",
        "title": "图9 训练指标曲线与终止判据",
        "prompt": (
            "A 2x2 grid of line charts (academic training metrics), x-axis = training step. "
            "Chart 1: reward mean (rising then plateau) and reward std (declining toward 0). "
            "Chart 2: advantage variance declining toward 0. Chart 3: pg_loss, mostly stable "
            "then a spike/NaN marker near the end. Chart 4: ppo_kl, stable then exploding "
            "upward. A vertical red dashed line across all charts marks the 'training collapse "
            "/ stop point' where std->0, variance->0, NaN appears, KL explodes. Title: "
            "'Termination criterion: stop when training collapses'. English axis labels, "
            "muted colors, grid lines. " + _STYLE
        ),
    },
    {
        "key": "fig10_S_shrink",
        "title": "图10 超生量S收缩曲线",
        "prompt": (
            "A single step-line / bar chart showing the oversample size S shrinking over "
            "training steps due to elimination. X-axis = step (0..20), Y-axis = number of "
            "surviving groups S. Line starts at 32 and decreases in small steps: 32, 30, 27, "
            "26, 25... staying above the training size N=16 (a horizontal orange reference "
            "line labeled 'N=16 trained groups'). Shaded area between S and N = 'oversample "
            "margin'. Annotation: 'elimination keeps >=80% each step, S shrinks slowly'. "
            "English labels, muted colors. " + _STYLE
        ),
    },
    {
        "key": "fig11_difficulty_evolve",
        "title": "图11 任务难度演化",
        "prompt": (
            "A diagram showing task difficulty evolving upward over training steps as the "
            "system self-evolves. X-axis = training step, Y-axis = task difficulty (easy -> "
            "hard). A rising curve. Below the curve, small example task labels at increasing "
            "difficulty: early 'create a file' (easy, green), middle 'clean a CSV and compute "
            "KPIs' (medium, orange), late 'audit a repo, run tests, produce a PDF report' "
            "(hard, red). Annotation: 'As the Actor grows stronger, the Questioner asks "
            "deeper follow-ups = self-evolving curriculum'. English labels. " + _STYLE
        ),
    },
]
