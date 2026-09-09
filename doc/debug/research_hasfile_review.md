# Research 有文件任务审查清单（1202 条）

来源：`datasets/_archive/train_v1_backup.parquet`（旧 13440）中 bucket=research、`has_inputs=True` 的任务。

这些任务 query 引用输入文件（csv/xlsx 等），沙箱需注入 files/。

## 统计

- 总数：1202
- 难度：{2: 2, 3: 18, 4: 84, 5: 82, 6: 512, 7: 465, 8: 39}
- 域：{'D1': 32, 'D10': 83, 'D11': 51, 'D12': 92, 'D13': 103, 'D3': 46, 'D4': 119, 'D5': 106, 'D6': 103, 'D7': 133, 'D8': 144, 'D9': 190}

## 任务清单

### 1. D4_g981210_zh (domain=D4, difficulty=2)

```
这两个文件你分析一下，给我一份综合报告。主要检查：1) 每个文章的关键词覆盖率（对照support.csv里的关键词列表）；2) 可读性评分（Flesch Reading Ease）是否符合要求（低于30的标记）；3) 是否缺少必填字段（date, description, image_url）；4) 标题是否重复（完全相同的标题）；5) 文章正文是否过长（超过2000字符的标记）；6) 是否含有禁止短语。另外，如果文章正文与描述内容明显不一致（比如描述里提到关键词但正文没有），也要标出来。报告汇总所有发现，并给出每个类别（tech, sports, politics）的总结。交叉对比两个文件中的数据。输出一个findings.md。
```

### 2. D5_g981603_zh (domain=D5, difficulty=2)

```
我们准备做一次小型工程审计，重点看代码风险、配置问题、测试失败和依赖风险。请基于 inputs/audit_records.xlsx、inputs/project_logs.txt、inputs/dependencies.json 以及 inputs/project/ 下面的代码文件，整理一份合并报告，明确哪些地方需要马上修，哪些是验证时要盯住的点。最后输出一个简洁的汇总文件，方便我直接发给团队。
```

### 3. D10_g981496_zh (domain=D10, difficulty=3)

```
请基于 inputs/customer_market_ops_master.xlsx、inputs/competitor_notes.txt 和 inputs/campaign_rules.json 出一份 decision_brief.md。我要看这次客户与市场运营的综合决策，重点放在评论/工单主题、客户流失风险、活动ROI、竞争对手动态，最后给出一页内的排名建议。
```

### 4. D11_k985432_en (domain=D11, difficulty=3)

```
Using the file rohitrox__healthcare-provider-fraud-detection-analysis__Train_Outpatientdata-1542865627584.csv, build a finance-analytics review focused mainly on temporal trend behavior in the claims data. I need a concise but rigorous analysis of how outpatient claim activity changes over time, especially by ClaimStartDt and ClaimEndDt, and how those changes interact with reimbursement, deductible amounts, procedure-code presence, diagnosis-code richness, and physician involvement. Please split the work into separate independent tracks so different analysts can work in parallel: one track on monthly/period-over-period volume and spend trends, one on claim-duration and timing patterns, one on coding intensity and missingness over time, one on provider-level trend concentration and outliers, and one on physician/beneficiary behavior shifts across time windows. The final output should be suitable for a finance analytics readout.
```

### 5. D12_g981149_zh (domain=D12, difficulty=3)

```
请基于这三份输入文件：interview_scorecards.xlsx、performance_calibration.xlsx、skills_onboarding_bundle.xlsx，输出一份 findings.md 的综合分析简报。我要的是 People/Training & Enablement 的交叉分析，不是逐行明细。请把四个视角合并成一页式结论：面试评分卡质量与推荐分布、绩效校准与原始绩效的一致性、技能矩阵缺口、以及入职模块的逾期/未完成情况。特别注意把跨来源对账结果写清楚：校准表与员工绩效表的匹配率、未匹配数量、最主要的不一致类型；以及面试评分卡里同一 candidate-stage-panelist 的重复记录。正文里请给出少量被点名的异常 ID 和前 3 个问题模块/技能，但不要展开成逐行清单。
```

### 6. D12_k983659_zh (domain=D12, difficulty=3)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的人力资源分析，重点围绕“排名与集中度”（Top-N、占比、帕累托/80-20、头部集中）。我想知道：哪些人群、岗位、部门、旅行频率、加班状态、薪资层级和工龄段最集中地贡献了离职风险或员工规模；哪些少数群体占据了大部分离职人数；以及离职员工与全员在这些维度上的集中度差异。请把结果拆成 4-6 个彼此独立的分析轨道，适合并行推进，最后给出一份简洁的分析总结（analysis_summary.json）。请尽量用真实列名：Attrition、Department、JobRole、BusinessTravel、OverTime、MonthlyIncome、JobLevel、TotalWorkingYears、YearsAtCompany、Age、MaritalStatus、Gender、DistanceFromHome、NumCompaniesWorked、JobSatisfaction、EnvironmentSatisfaction、WorkLifeBalance、StockOptionLevel、EducationField、TrainingTimesLastYear 等。
```

### 7. D12_k983679_zh (domain=D12, difficulty=3)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向 HR 的离职驱动分析，重点围绕“数值变量之间的相关性与驱动因素”展开：先找出离职率相关的关键数值字段，再看这些字段彼此之间的联动关系（尤其是 Age、MonthlyIncome、TotalWorkingYears、YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager、DistanceFromHome、PercentSalaryHike、JobLevel、StockOptionLevel、JobSatisfaction、EnvironmentSatisfaction、RelationshipSatisfaction、JobInvolvement、TrainingTimesLastYear 等），并按 Attrition 分组比较差异；同时请识别最强正/负相关的数值对、离职人群与未离职人群的差异、以及可能存在的“共线性/重叠信息”。输出应足够实务化，适合给 HRBP 和用工策略负责人做汇报：需要明确哪些指标最值得优先监控、哪些变量可能只是同一条职业发展轴上的不同侧面、以及哪些结论可以直接用于后续人事策略讨论。请把分析拆成若干彼此独立的子任务，方便不同分析员并行完成。
```

### 8. D13_g981497_en (domain=D13, difficulty=3)

```
I need a compact experiment readout for exp_checkout_17 using the files in inputs/. Please combine the assignment, event, revenue, and seed-context files into one short report. - Summarize funnel counts and purchase conversion by variant.
- Call out data-quality issues like duplicate events, future-dated events, and conflicting assignments.
- Include a simple revenue-per-purchaser view for control vs treatment.
- Keep the deliverable concise and decision-oriented.
```

### 9. D13_k985383_zh (domain=D13, difficulty=3)

```
请基于文件 aimlveera__counterfeit-product-detection-dataset__counterfeit_products.csv 做一份面向产品分析的多部分深度分析，重点围绕“时间/趋势”维度展开。这个数据里有 listing_date、views、purchases、wishlist_adds、seller_reviews、seller_rating、shipping_time_days、domain_age_days 等字段，我想看：1）不同上架日期阶段的可疑/假货风险是否有变化，2）按月的销量、收藏、浏览、转化率走势，3）不同类别和品牌在时间上的风险与表现差异，4）卖家口碑和履约表现是否随时间变化并影响假货概率，5）高风险信号（如 unusual_payment_patterns、ip_location_mismatch、bulk_orders）是否在近日期更集中，6）找出近期表现异常上升或下降的子群。请把结果拆成 4-6 个彼此独立、适合并行处理的分析轨道，并输出一份结构化结论，尽量给出可执行建议。
```

### 10. D4_k982946_en (domain=D4, difficulty=3)

```
Using sanjidh090__resultpf__bd_eng_news_daily.csv, analyze this newsroom/content dataset for editorial performance and publication mix. I mainly want a distribution-and-thresholds view: how stories are spread across publishers and dates, what share of coverage sits above/below meaningful article-length and title-length cutoffs, and how those threshold cohorts differ by publisher and publication timing. Please treat the file as fixed and use the real columns: title, text, publish_date, urls, news_collection_time, and publisher. I need this broken into independent workstreams so different analysts can work in parallel, and I want a concise JSON summary of the findings with threshold counts, quantile buckets, and mix shares.
```

### 11. D5_g980881_en (domain=D5, difficulty=3)

```
You are given three spreadsheet-style inputs: audit findings, test logs, and config audit rows. Identify the most important cross-linked issues by reconciling repeated patterns across the files, separating real seeds from synthetic rows, and summarizing the highest-confidence findings.

Deliverables:
1) A concise ranked list of the top issues with rationale.
2) A short table or bullet summary mapping each issue to the supporting rows/sheets.
3) A final recommendation section explaining what should be fixed first and why.

Keep the response grounded in the provided inputs and avoid guessing beyond the data.
```

### 12. D5_g981660_zh (domain=D5, difficulty=3)

```
请帮我把这套小项目做一次合并审计，输入是 inputs/code_audit_dataset.xlsx 和 inputs/test_logs.txt，我要一份单独的汇总报告，能同时覆盖模块A的静态代码问题、模块B的安全风险、测试日志里的失败分布，再加上生产配置和依赖的基础检查，最后给出一个统一的修复和验证计划。
```

### 13. D5_g981804_zh (domain=D5, difficulty=3)

```
请基于 codebase_audit.xlsx、test_run.log、dependency_config_audit.xlsx 做一次合并审计，输出一份 findings.md。我要的是一份可以直接给研发和测试一起看的分析简报，不是零散备注。
- 第一部分看代码基线，梳理被明确命中的高风险写法和可维护性问题。
- 第二部分看测试日志，归纳失败/跳过的集中模式，并把和代码问题对应起来。
- 第三部分看依赖与配置，检查生产配置里是否存在明显风险项。
- 最后把三份材料交叉对照，给出一版统一的修复优先级和验证建议。
```

### 14. D5_g982545_zh (domain=D5, difficulty=3)

```
请基于 inputs/codebase_audit.xlsx、inputs/test_results.xlsx、inputs/dependency_config.xlsx、inputs/issue_index.xlsx、inputs/reference_notes.xlsx 做一次合并审计，并输出一个紧凑的汇总报告文件。我需要你把静态代码审查、配置与依赖风险、测试失败分诊、以及与这两条真实问题记录相关的回归风险放在同一份结论里，并明确哪些问题是命中我们规定的可检出项、哪些测试用例失败、以及建议的修复优先级。报告尽量保持表格化，方便我直接转给研发和测试。
```

### 15. D5_g983381_en (domain=D5, difficulty=3)

```
I need one consolidated findings report for a release gate review. Please use the three input files — codebase_audit.xlsx, test_and_runtime_logs.xlsx, and policy_memo.pdf — and give me a single findings.md that ties together the code risks, the test failures, the config issues, and the dependency concerns. I want the main issues grouped clearly, with any conflicts or overlaps between the sources called out, and a practical fix-and-validation plan at the end.
```

### 16. D6_g981940_en (domain=D6, difficulty=3)

```
Review contracts.xlsx, policy_report.pdf, and operations_log.csv, then give me one short decision brief on whether we should proceed with the renewable procurement rollout. I want the file to rank the options, call out the key numbers behind the recommendation, and note any data issues that affect the decision.
```

### 17. D6_k982859_zh (domain=D6, difficulty=3)

```
请基于文件 chicago__chicago-contracts__contracts.csv 做一份面向合同/档案记录的综合数据质量审计，重点围绕缺失值、空字符串/问号占位、重复记录、数值范围异常以及分类字段不一致这几类问题。请直接使用现有字段（例如 Purchase Order Description、Purchase Order (Contract) Number、Revision Number、Specification Number、Contract Type、Start Date、End Date、Approval Date、Department、Vendor Name、Vendor ID、City、State、Zip、Award Amount、Procurement Type、Contract PDF），不要修改原始值。希望你把结果整理成一个可交付的 analysis_summary.json，并且按以下几个独立分析轨道分工：1）字段级缺失/占位符分布；2）合同主键/业务键重复与版本冲突；3）日期字段范围与逻辑一致性；4）Award Amount 的异常值、负值与极端值；5）分类字段标准化一致性（Department、State、Procurement Type 等）；6）可疑记录抽样定位（例如同一合同号多版本、同一供应商多地址/多ID）。请先给我结论，再给出需要优先清洗的数据问题清单和建议的规则。最后，请把每个分析轨道的关键发现单独列出来，便于我分配给不同子任务去复核。
```

### 18. D8_g980939_zh (domain=D8, difficulty=3)

```
请基于 kb_audit_articles.xlsx 和 kb_evidence_events.xlsx 做一次知识库审计与补洞分析，输出一份汇总报告文件。重点看文章陈旧度、缺口、补丁/支付/合规相关内容的风险，以及 StripeGlobal 事件证据和社区临时方案，再把需要优先修补的结论合并到同一份结果里。
```

### 19. D9_k982826_zh (domain=D9, difficulty=3)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的多部分深度分析，重点围绕“排名与集中度”展开：找出哪些攻击类别、协议/服务特征、以及关键流量指标最集中，前几名是否占据了大部分样本或数值总量，并用 Pareto/Top-N 的思路判断数据是否高度偏斜。请结合真实列名（例如 label、Protocol Type、Rate、Srate、Drate、flow_duration、Header_Length、HTTP、HTTPS、DNS、TCP、UDP、ICMP、Tot size、Weight 等）完成分析，并给出可直接用于汇报的结论。请把任务拆成多个相互独立的分析轨道：一条做标签频率与累计占比排名；一条做协议/服务命中集中度；一条做高值流量指标的Top-N贡献；一条做按标签分组的均值/中位数对比；一条做异常/极端值与集中度的关联；如有必要再补充一条做相关性与冗余特征观察。最终输出应便于我判断：哪些少数类别或特征贡献了大部分风险信号，以及哪些字段最值得优先监控。
```

### 20. D9_k984520_zh (domain=D9, difficulty=3)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全分析的综合审查，重点围绕“排名与集中度”来判断训练集里的流量/攻击是否高度集中在少数协议、服务、标志和特征组合上。请帮我分成 5 个互相独立的分析轨道并最终汇总成 analysis_summary.json：1）按 class、protocol_type、service、flag 做 Top-N 排名，计算各自占比和头部集中度；2）比较 normal 与 anomaly 在 src_bytes、dst_bytes、count、srv_count 等关键数值特征上的头部差异，并识别最集中的类别；3）分析 class 与高频协议/服务/标志之间的交叉集中度，找出最主要的攻击/正常流量组合；4）检查极端值与稀有值在数据中的集中程度（例如为 0、为 1、或显著高值的记录占比）；5）对关键连续特征之间的相关性做简洁审计，看看是否存在明显的同向集中趋势。请输出简明结论，务必给出 Top-N、份额、累计份额（Pareto）以及最值得关注的集中模式。请不要做建模，只做确定性统计分析，并说明哪些结果最能支持安全运营中的优先排查对象。
```

### 21. D10_g981106_en (domain=D10, difficulty=4)

```
Hi, we need a quick synthesis of our customer operations data. We have feedback from users, campaign performance, churn indicators, competitor tracking, and CRM updates. Please analyze these sources and produce a findings.md report that tells me: the most common complaint theme, the campaigns with the best ROI, the riskiest customers, the top competitor events, and any anomalies in CRM or campaign data. Keep it compact and focused on true business impact.
```

### 22. D10_g981317_en (domain=D10, difficulty=4)

```
Review customer_market_ops_main.xlsx, customers_notes.csv, feedback_clips.csv, and competitor_tracking.json. I need one compact decision brief that ranks the follow-up priority and the best GTM move for this quarter. Focus on the top three at-risk customers, the top complaint theme, the best ROI campaign, and the most important competitor signal, then synthesize it into one recommendation file.
```

### 23. D10_g981586_en (domain=D10, difficulty=4)

```
I need a compact findings brief from the customer and market ops files because we’re preparing the monthly operating review. Please review customer feedback, churn risk, campaign performance, competitor gaps, and CRM update coverage, then write findings.md. Make sure the most important complaints, the riskiest customers, the best campaigns, and the biggest competitor gaps are all summarized clearly, with any data mismatches called out.
```

### 24. D10_k982244_zh (domain=D10, difficulty=4)

```
请基于文件 radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv 做一次面向客户分析的多部分深度分析，重点放在“相关性与驱动因素”上：先看数值字段之间哪些一起升降、哪些关联最强，再把这些关系和流失结果 Exited 结合起来解释。请重点使用这些列：CreditScore、Age、Tenure、Balance、NumOfProducts、HasCrCard、IsActiveMember、EstimatedSalary、Complain、Satisfaction Score、Point Earned，以及 Exited；同时可结合 Geography、Gender、Card Type 做补充分层。我要的是可直接交付给业务团队的结论，不要泛泛而谈。请把分析拆成 4-6 个相互独立的轨道并行推进，最后给我一个简洁的分析摘要，说明：1）数值变量之间的主要正负相关；2）与 Exited 关联最强的数值驱动因素；3）不同地理/性别/卡等级下这些相关性是否有明显变化；4）是否存在值得进一步验证的高风险组合。
```

### 25. D10_k982373_en (domain=D10, difficulty=4)

```
Using radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv, build a customer analytics review focused mainly on temporal / trend analysis over the available sequence field RowNumber as a proxy for record order. I want a compact but rigorous analysis of churn behavior over the dataset’s progression, including whether Exited/Complain rates change from early to late records, how key customer mix variables shift over the record sequence (Age, Balance, NumOfProducts, IsActiveMember, Satisfaction Score, Point Earned), and whether churn-related patterns differ by Geography, Gender, and Card Type across early vs late segments. Please split the work into independent tracks so a small sub-agent team could handle them in parallel, and deliver the results in analysis_summary.json with clear period-over-period comparisons and short, decision-oriented takeaways.
```

### 26. D10_k982610_zh (domain=D10, difficulty=4)

```
请基于文件 radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv 做一份面向客户运营的分析，重点围绕“分布与阈值分层（高/低于业务阈值的数量、分位数组、以及各层占比）”来展开。请充分使用这些真实字段：CreditScore、Age、Tenure、Balance、NumOfProducts、HasCrCard、IsActiveMember、EstimatedSalary、Exited、Complain、Satisfaction Score、Card Type、Point Earned，以及 Geography、Gender。我要你把分析拆成几个彼此独立的子任务，方便不同分析员并行执行。请输出一份简洁的分析汇总（analysis_summary.json）思路，核心要回答：客户规模在关键阈值上的分布是什么、不同阈值区间里的流失/投诉/活跃情况如何、以及不同地理/性别/卡类型在这些阈值层中的占比差异是否明显。不要做建模、不要画图，只做可复现的描述性统计和分层统计。
```

### 27. D10_k982715_zh (domain=D10, difficulty=4)

```
请基于文件 radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv 做一份面向客户分析的分层流失诊断，重点围绕“分布与阈值分群（高于/低于业务阈值、分位数组、占比结构）”来展开。请先核对并汇总关键字段的分布，再按可解释的业务阈值拆分客群，看看不同阈值下流失率、客群占比、以及关键画像是否发生明显变化。数据里可直接用的字段包括：RowNumber、CustomerId、Surname、CreditScore、Geography、Gender、Age、Tenure、Balance、NumOfProducts、HasCrCard、IsActiveMember、EstimatedSalary、Exited、Complain、Satisfaction Score、Card Type、Point Earned。请输出一份可交付的分析摘要，最好能支持管理层快速判断：哪些阈值分群最值得优先关注、哪些人群组合的流失占比最高、以及这些分群在余额、年龄、活跃度、产品数、抱怨等方面的结构差异。请把工作拆成多个可并行的分析轨道，彼此尽量独立，以便不同分析同学同时推进。
```

### 28. D10_k983598_en (domain=D10, difficulty=4)

```
Using blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv, build me a customer-churn analysis focused mainly on temporal / trend patterns over the available sequence variable(s). I want a compact executive readout that tracks how churn and customer value change over tenure buckets, compares month-to-month vs one-year vs two-year contracts over time, and shows whether service/payment behavior shifts in ways that look like an early-warning signal. Please use the real columns in the file, especially tenure, MonthlyCharges, TotalCharges, Contract, PaymentMethod, InternetService, SeniorCitizen, Partner, Dependents, PaperlessBilling, and Churn. Break the work into a few independent tracks so different analysts can work in parallel, and end with a concise JSON summary of the main findings plus a short list of prioritized retention actions.
```

### 29. D11_k982498_zh (domain=D11, difficulty=4)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向风控/信贷产品的分层分析，重点围绕“阈值分层 + 分布分桶 + 结构占比”来判断哪些借款人特征与违约风险更相关。请直接读取数据中的真实字段（credit.policy, purpose, int.rate, installment, log.annual.inc, dti, fico, days.with.cr.line, revol.bal, revol.util, inq.last.6mths, delinq.2yrs, pub.rec, not.fully.paid），不要假设任何不存在的变量。我要你把分析拆成几个可以并行推进的部分：先按 not.fully.paid、credit.policy 和 fico / int.rate / dti / revol.util / inq.last.6mths 等核心字段做阈值 cohort 对比；再按 fico、int.rate、dti、revol.util 做分位数分桶，看各桶的样本量和坏账占比；同时看 purpose 结构在不同风险分层里的 mix share；最后补充少量相关性和异常值/极值分布，用来支持风控策略建议。输出时请围绕“哪些阈值附近的 cohort 风险明显抬升、哪些分桶样本集中、哪些目的用途在高风险桶占比更高”来组织结论。请给出可执行的分析思路、必要的统计口径，并确保所有结论都只来自这份 CSV 的真实数据。
```

### 30. D11_k982965_en (domain=D11, difficulty=4)

```
Using yasserh__loan-default-dataset__Loan_Default.csv, I need a finance-style correlation and driver analysis on the loan portfolio: identify which numeric fields move together, round correlations sensibly, and call out the strongest associations with default-related and pricing/risk variables. Please split the work into 5 independent tracks so it can be done in parallel: (1) numeric data quality and missingness for the key drivers, (2) pairwise correlations among the numeric fields, especially loan_amount, rate_of_interest, Interest_rate_spread, Upfront_charges, term, property_value, income, Credit_Score, LTV, dtir1, and Status, (3) correlations and rate comparisons by Year and Region for the main risk variables, (4) segment-level driver analysis across loan_type, loan_purpose, Gender, and loan_limit, and (5) a concise interpretation of the strongest positive/negative associations that are relevant for underwriting and default risk. Please produce a compact analysis summary with the main correlation findings and the most important driver patterns.
```

### 31. D11_k983078_zh (domain=D11, difficulty=4)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向信贷风控与产品经营的综合分析，重点围绕“排名与集中度”展开：先识别哪些贷款用途、信用表现和风险特征最集中；再看高风险是否被少数分组（如 purpose、fico 分段、credit.policy）主导；并补充变量之间的联动关系、违约/未结清标签 not.fully.paid 的集中分布，以及高频群体的画像。请把结果整理成一份可直接给管理层看的分析结论，最好包含 top-N 排名、占比、累计集中度（如前几类覆盖了多少比例）、以及能支撑业务决策的关键发现。数据字段包括 credit.policy、purpose、int.rate、installment、log.annual.inc、dti、fico、days.with.cr.line、revol.bal、revol.util、inq.last.6mths、delinq.2yrs、pub.rec、not.fully.paid 等。
```

### 32. D11_k983281_en (domain=D11, difficulty=4)

```
Using yasserh__loan-default-dataset__Loan_Default.csv, build a finance analytics memo focused mainly on ranking and concentration. I need a multi-part readout that identifies the top drivers of loan default and portfolio exposure, quantifies how concentrated defaults and loan amounts are across key segments, and highlights any Pareto-style patterns in this file. Please use the real columns in the dataset, especially Status, loan_type, loan_purpose, loan_limit, Gender, age, credit_type, occupancy_type, Secured_by, year, loan_amount, property_value, income, Credit_Score, LTV, rate_of_interest, Interest_rate_spread, Upfront_charges, term, and dtir1. Break the work into separate tracks so different analysts could handle them independently, and return a concise analysis_summary.json.
```

### 33. D11_k983472_zh (domain=D11, difficulty=4)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向信贷风控与投放的复杂分析报告，重点围绕“时间/序列趋势”展开。请把样本按放款或审批序列中可用的时间代理字段 days.with.cr.line、以及与风险变化相关的申请特征组合起来，分析：不同借款目的（purpose）在风险指标上的序列差异；信用质量相关指标（fico、int.rate）与负债压力指标（dti、revol.util）是否随连续区间呈现趋势变化；以及 credit.policy 和 not.fully.paid 在不同序列分层中的变化。请结合真实字段做出可执行结论，最后给出适合业务汇报的要点、异常点和建议。数据字段包括 credit.policy、purpose、int.rate、installment、log.annual.inc、dti、fico、days.with.cr.line、revol.bal、revol.util、inq.last.6mths、delinq.2yrs、pub.rec、not.fully.paid。
```

### 34. D11_k984190_en (domain=D11, difficulty=4)

```
Analyze the loan_data.csv file for finance analytics, focusing mainly on correlation and driver analysis: identify which numeric fields move together, report rounded pairwise correlations, and surface the strongest associations with credit quality and repayment risk. Break the work into 5 independent tracks: (1) numeric correlation map and top positive/negative associations, (2) borrower risk drivers tied to not.fully.paid, (3) lending policy and pricing relationships around credit.policy, int.rate, fico, and installment, (4) credit utilization / revolving balance / inquiry behavior relationships, and (5) purpose-based comparisons to see whether loan purpose shifts the key numeric drivers.
```

### 35. D11_k984430_zh (domain=D11, difficulty=4)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向信贷风控/业务运营的分层阈值分析，重点围绕“分布与阈值客群”（例如高/低利率、高/低 FICO、高/低负债率、高/低查询次数、是否有逾期/公开记录等）来判断不同客群的规模、违约倾向与结构差异。请把分析拆成几个可并行的部分：1）先做核心变量的分布与关键业务阈值切分；2）再做按 purpose 的客群结构和阈值占比；3）然后看 not.fully.paid 在各阈值分组中的差异；4）再比较 credit.policy 的通过/未通过客群在关键指标上的分布；5）最后给出若干可落地的 cohort 结论，例如高 dti/低 fico/高 inq.last.6mths 组合是否显著集中在更高违约率区间。请务必只基于真实数据输出，不要臆造任何值。
```

### 36. D11_k985081_en (domain=D11, difficulty=4)

```
Using the file upadorprofzs__credit-risk__original.csv, build a finance-analytics review focused mainly on distribution and threshold cohorts. I want a practical readout of the portfolio using the real columns clientid, income, age, loan, and default. Please split the work into independent tracks so it can be done in parallel: one track for how many customers sit above/below key business thresholds for income, age, and loan; one track for quantile-bucket cohort mix and default rates; one track for comparing default vs non-default distribution summaries; one track for segmenting the book into combined income/loan threshold bands and summarizing mix; and one track for spotting concentration in extreme values and whether default is overrepresented there. Keep it deterministic and based only on this dataset.
```

### 37. D12_g981659_zh (domain=D12, difficulty=4)

```
我需要你把这三份文件里的人员、培训和能力信息整合成一份管理层可直接看的简报，重点看面试/复核结果、培训完成情况、技能缺口和需要优先处理的异常点。请输出一份精简但完整的汇总报告，给我能直接拿去开会的结论、关键比例、Top 项和少量需要点名处理的记录。
```

### 38. D12_k982672_zh (domain=D12, difficulty=4)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向HR管理层的离职风险与人员结构分析，重点围绕“排名与集中度”展开：比如哪些部门/岗位/年龄段/婚姻状态/加班状态在员工规模上占据前几位，Top-N 群体是否贡献了大部分样本，是否存在明显的帕累托集中现象；同时结合 Attrition、MonthlyIncome、TotalWorkingYears、OverTime 等字段，找出离职更集中在哪些高频人群中，并给出可直接用于汇报的关键结论。请拆成多个独立分析轨道，确保不同轨道可以并行推进，最后输出一个简洁的 analysis_summary.json。
```

### 39. D12_k983509_zh (domain=D12, difficulty=4)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一次面向人力资源的异常与离群值分析，重点不是做建模，而是用明确、可复现的数值规则找出数据中的异常点、极端值和罕见类别，并判断这些异常在不同员工群体中的分布差异。请把结论整理成 analysis_summary.json，要求尽量业务化、可执行。

我希望你至少拆成 4-6 个彼此独立的分析轨道：
1) 数值字段异常值：用 IQR、分位数阈值或显式业务阈值识别 Age、MonthlyIncome、DistanceFromHome、TotalWorkingYears、YearsAtCompany、YearsSinceLastPromotion、YearsWithCurrManager 等字段的极端值，并统计占比。
2) 罕见类别与组合异常：找出 BusinessTravel、Department、EducationField、JobRole、MaritalStatus、OverTime 中的低频类别，以及与 Attrition 同时出现时是否更集中。
3) 薪酬/职级不一致检查：检查 JobLevel、MonthlyIncome、JobRole、TotalWorkingYears、Age 之间是否存在明显不匹配的记录，例如同职级下薪酬异常高/低。
4) 任职与晋升异常：用 YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager 检查“长期未晋升但薪酬仍异常高/低”或“刚入职但记录很极端”的员工。
5) 出勤/加班异常：分析 OverTime、JobSatisfaction、EnvironmentSatisfaction、WorkLifeBalance 与 attrition 的关系，重点关注异常压力群体是否离职更集中。
6) 输出一份简洁的风险画像：把最值得 HR 复核的异常员工特征总结成可操作规则，而不是泛泛描述。

请只使用真实字段，不要编造任何值；所有统计必须是确定性的、可复现的。
```

### 40. D12_k983807_zh (domain=D12, difficulty=4)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的 HR 分析，重点围绕“分布与阈值分层”来展开：先按关键业务阈值把员工切成不同 cohort（例如年龄、月收入、总工龄、通勤距离、培训次数、加班与否等），再看这些 cohort 的人数占比、离职占比、以及不同人群的结构差异。请重点回答：哪些阈值分层下离职压力最集中，哪些高风险 cohort 的规模和占比最大，哪些变量在分层后呈现明显的 mix share 失衡。需要把结果整理成可直接给领导看的 analysis_summary.json，并且输出可行动的结论建议。请至少从 4-6 个彼此独立的分析轨道展开：1）按年龄/工龄/司龄阈值分层的离职分布；2）按月收入分位数和职级分层的 cohort mix；3）按通勤距离与加班状态的风险分布；4）按满意度/环境满意度阈值分层的离职差异；5）按培训次数和绩效/加薪阈值的组合分布；6）按部门/岗位/婚姻状态的结构占比与离职对比。请务必使用原始真实列名：Age, Attrition, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, EmployeeCount, EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, Over18, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StandardHours, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager。不要做建模、不要预测，只做确定性的分组统计、计数、占比、分位数、均值/中位数和交叉表分析。需要给出可复核的具体数值。
```

### 41. D13_k982992_zh (domain=D13, difficulty=4)

```
请基于文件 PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv 做一轮产品分析，重点放在数据质量审计上，同时顺带给我能直接用于汇报的结论。请围绕这些字段展开：uniq_id、crawl_timestamp、product_url、product_name、product_category_tree、pid、retail_price、discounted_price、image、is_FK_Advantage_product、description、product_rating、overall_rating、brand、product_specifications。我要你把分析拆成 4-6 条彼此独立的轨道并行做，最后汇总成一份 analysis_summary.json。核心请检查：缺失值、'?' / 空字符串 / 空白字符串、重复记录、价格范围异常（如负值、discounted_price 高于 retail_price、极端折扣）、类别字段不一致（product_category_tree 的层级结构、brand 与规格字段是否冲突）、以及文本字段的脏数据模式。请按产品分析视角给出可落地的清洗优先级和风险点，必要时补充少量描述性统计帮助判断问题是否集中在某些品牌或类目上。
```

### 42. D13_k983128_en (domain=D13, difficulty=4)

```
Using akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv, analyze this Taobao maternal-and-infant trade history with a focus on distribution and threshold cohorts. I need a business-style readout of how the order-level mix behaves across user, category, product property, and time dimensions, especially counts above/below practical thresholds, quantile buckets, and share-of-total views. Please break it into independent workstreams so different analysts can work in parallel: 1) purchase-size threshold cohorts for buy_mount and how concentrated orders are at 1 vs 2+ units; 2) user activity distribution and cohorting by order counts/quantiles; 3) category and cat1 mix shares with thresholded concentration analysis; 4) property-string complexity distribution and whether richer property lists correlate with larger baskets or later days; 5) day-based distribution and time-sliced threshold cohorts; 6) a concise exception scan for the most extreme users/auctions/categories. Deliver a compact summary JSON plus the exact counts, shares, and threshold cutoffs used.
```

### 43. D13_k983718_en (domain=D13, difficulty=4)

```
Using PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv, build a product analytics memo focused mainly on segment comparison across categorical groups. I want you to compare rates/means across categories and identify the biggest gaps between segments using the real columns `product_category_tree`, `brand`, `is_FK_Advantage_product`, `retail_price`, `discounted_price`, `product_rating`, `overall_rating`, `description`, `product_name`, and `crawl_timestamp`. Please split the work into independent tracks so different analysts can work in parallel: (1) category-level price and discount comparisons, (2) brand-level segment gaps and concentration, (3) FK Advantage vs non-Advantage comparisons, (4) rating availability and rating differences by segment, and (5) sanity checks for missingness and data coverage. Summarize the most important segment gaps, not just averages, and call out any notable top/bottom groups in each comparison.
```

### 44. D13_k984100_en (domain=D13, difficulty=4)

```
Using akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv, build a product-analytics readout focused on ranking and concentration. I need a concise but rigorous analysis of what the long tail looks like in this Taobao maternal-and-infant trade history: identify the top users, auctions, categories, and day-level spikes; quantify how much of total purchasing is concentrated in the top groups; and check whether concentration differs by category or time. Use the actual columns user_id, auction_id, cat_id, cat1, property, buy_mount, and day. Please structure the work so a small team can run independent tracks in parallel and then merge the findings into a single analysis_summary.json.
```

### 45. D13_k984133_zh (domain=D13, difficulty=4)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份面向产品分析的完整数据质量审计，并顺带给出能帮助后续经营分析的基础画像。重点请围绕数据质量问题展开：检查 user_id、auction_id、cat_id、cat1、property、buy_mount、day 这些字段是否存在缺失、空字符串、问号占位、重复记录、数值范围异常，以及 cat_id 与 cat1 的组合是否一致、buy_mount 和 day 是否存在明显异常值。请把结果拆成 4-6 个互相独立的分析轨道，便于并行处理：1）整体缺失/异常值扫描；2）重复与主键一致性检查；3）类别与属性字段一致性检查；4）数值字段范围与离群检查；5）按用户和日期的交易行为分布；6）按商品类目做基础质量对比。最终请输出一份可直接给产品/数据团队看的结论摘要，并把关键发现整理到 analysis_summary.json。请只基于真实数据，不要补充任何不存在的值。另请给出每个检查项的可复现 pandas 计算方式，方便我后续复查。
```

### 46. D13_k984160_zh (domain=D13, difficulty=4)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份产品分析，重点围绕“异常与离群识别”展开，尽量用明确的数值规则来定位可疑交易/商品/用户行为。请先整体扫描 user_id、auction_id、cat_id、cat1、property、buy_mount、day 这些字段，找出：1）buy_mount 的极端值和异常大额购买；2）day 的时间分布里是否存在异常集中或异常稀疏的日期；3）property 中低频特征、超长特征串、以及与 cat1/cat_id 组合后极少出现的稀有组合；4）用户层面的异常行为，比如单用户交易次数、单用户覆盖的 auction_id / cat_id 数过高或过低；5）商品层面的异常，比如被极少数用户重复购买、或同一 auction_id 出现明显异常的 buy_mount；6）把上述规则汇总成一个可执行的异常清单，并说明每条规则筛出的样本数量与代表性例子。请按这些分析轨道拆分，最后输出一份适合产品团队讨论的 summary。
```

### 47. D13_k984487_en (domain=D13, difficulty=4)

```
Using the file akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv and the columns user_id, auction_id, cat_id, cat1, property, buy_mount, and day, build a product-analytics readout focused mainly on temporal trend analysis over day. I need a compact but rigorous summary of how transaction volume and buy_mount change over time, including period-over-period shifts, early-vs-late comparison, and whether the activity mix differs by category over time. Please structure it so a small team could split the work into independent tracks and return a single analysis_summary.json with the key findings, trend inflection points, and any notable category or user-behavior changes.
```

### 48. D13_k985248_en (domain=D13, difficulty=4)

```
Using the file PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv, build a product-analytics readout focused mainly on ranking and concentration. I need a compact but rigorous summary of where value and assortment are concentrated across the catalog using the real columns product_name, product_category_tree, retail_price, discounted_price, brand, product_rating, overall_rating, is_FK_Advantage_product, and description. Break it into 5 independent tracks: (1) top brands and how much of the catalog/revenue proxy they represent, (2) top categories by product count and discounted_price concentration, (3) Pareto analysis of whether a small set of brands/categories holds most of the discounted price mass, (4) top-N products by discounted_price and retail_price plus the share they contribute, and (5) how concentration differs for rated vs unrated products and for FK Advantage vs non-advantage products. I want the output written as if for an internal product review, with exact counts, shares, and top lists from this dataset only.
```

### 49. D3_k982517_zh (domain=D3, difficulty=4)

```
请基于文件 ajinilpatel__energy-consumption-prediction__Energy_consumption_dataset.csv 做一版面向业务汇报的能源消耗分析，重点放在“相关性与驱动因素”上：先找出数值字段之间哪些变量最同步、哪些与 EnergyConsumption 的关联最强，并把相关系数统一四舍五入到 2 位小数；再结合 Hour、Month、DayOfWeek、Holiday、HVACUsage、LightingUsage 这些业务字段，解释不同场景下能耗为什么变化。希望你把分析拆成若干独立部分，方便并行推进，最后输出一份可直接给管理层看的结论摘要，附上关键证据和需要重点关注的高关联变量。
```

### 50. D4_g980205_en (domain=D4, difficulty=4)

```
You are auditing a compact newsroom QA bundle.
Use the provided input files to verify counts, summarize QC status, and identify any issues.
Keep the response concise and grounded only in the inputs.
```

### 51. D4_g980726_zh (domain=D4, difficulty=4)

```
请基于 inputs/content_research_sources.xlsx 和 inputs/briefing.pdf 产出一个 findings.md，给我一版中文分析简报。重点是把 4 条分析线合并成一份可直接交付的摘要：数据概览、关键实体覆盖、异常与不合规、以及跨来源对照结论。
- 需要覆盖 reviews / evidence / rules 三个工作表里的信息
- 重点标出正文重复、空分类、过短摘要这几类异常
- 最终简报里保留必要的英文原文片段，但主体用中文写
- 写成单个 findings.md 文件，结构清楚，方便我直接转发
```

### 52. D4_g981000_en (domain=D4, difficulty=4)

```
You are reviewing a small news-archive dataset for editorial anomalies. Use the provided inputs to produce a concise QA brief that identifies the key issues, summarizes dataset composition, and recommends next steps.
```

### 53. D4_g981559_en (domain=D4, difficulty=4)

```
You are a multi-agent system for content creation and transformation. Analyze the provided articles, keywords, and validation rules. Your tasks: (1) Compute Flesch Reading Ease for each article. (2) Identify duplicate or overlapping content between articles using Jaccard similarity. (3) Verify that all keywords appear in the articles and that validation rules pass. Deliverables: a summary report, a list of flagged articles, and a corrected keyword list if needed.
```

### 54. D4_k982328_en (domain=D4, difficulty=4)

```
Using the file bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv, do a content/editorial analytics pass focused mainly on correlation and driver analysis: identify which article features move together, what the strongest associations are, and whether those relationships differ by section/topic and over time. Use the actual columns title, pubDate, guid, link, and description only. I need this broken into a small team of independent workstreams so we can parallelize it: first quantify the dataset structure and time coverage; second build article-level features from the text and URL structure that can act as numeric drivers; third compute rounded correlations and top positive/negative associations among those numeric features; fourth test whether the patterns differ by broad BBC section patterns inferred from guid/link paths; fifth summarize any temporal shifts in the numeric relationships across months; and sixth produce a concise editorial readout of the biggest driver relationships and notable outliers. Keep the work grounded in the fixed dataset and report only deterministic findings.
```

### 55. D4_k982840_zh (domain=D4, difficulty=4)

```
请基于文件 bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv 做一份面向内容/编辑分析的深度拆解，重点围绕“排名与集中度”来判断 BBC 这批文章的内容结构：哪些标题模式、发布时间、频道/栏目、以及描述文本特征最集中、最能贡献头部流量/头部频次。请你按业务上可落地的方式，把分析拆成多个彼此独立的轨道，优先回答：1）头部主题/栏目是否高度集中；2）TOP-N 文章、栏目、年份/月/星期、以及标题关键词的频次集中度（含前 10/前 20 占比、帕累托特征）；3）不同栏目在时间上的集中程度；4）标题和描述里的关键词是否被少数词主导；5）文章链接域名/路径类型是否存在明显头部集中；6）缺失值与数据质量是否会影响集中度判断。最后给我一个可直接用于汇报的 summary.json，里面要包含关键排名、集中度比例、以及每个分析轨道的结论要点。请仅使用表内真实字段：title、pubDate、guid、link、description，不要编造任何数值。
```

### 56. D4_k983050_en (domain=D4, difficulty=4)

```
Using sanjidh090__resultpf__bd_eng_news_daily.csv, do a content/editorial analytics review focused mainly on ranking and concentration patterns. Use the real columns title, text, publish_date, urls, news_collection_time, and publisher to answer: which publishers dominate volume, how concentrated the output is among the top entities, whether a small set of dates or collection times account for a large share of items, and whether article length shows a Pareto-style skew. I want a practical summary I can use to brief the editorial team, not a generic EDA. Please break it into independent tracks so different people could work on them in parallel.
```

### 57. D4_k983155_en (domain=D4, difficulty=4)

```
Using the file glushko__seth-godins-blogs-dataset__seth-data.csv, please do a content/editorial analysis focused on ranking and concentration. I need to know which blog topics/titles dominate the archive, how concentrated the output is among the most frequent titles and publication periods, and whether the most common items also account for a disproportionate share of total posts. Use the columns id, title, stars, publication-date, url, content_plain, and referral-url as needed. Please break the work into a few independent tracks so they can be handled in parallel, and return a concise analysis summary plus any key top-N concentration findings.
```

### 58. D4_k983226_zh (domain=D4, difficulty=4)

```
请基于文件 kimjihoo__coronavirusdataset__SeoulFloating.csv 做一份面向内容/编辑运营的分布与阈值分层分析，重点看 fp_num 的高低分层、是否超过业务阈值、以及不同人群/时间/区域的占比结构。数据字段包括 date、hour、birth_year、sex、province、city、fp_num。请重点围绕“分布 & threshold cohorts（高于/低于业务阈值的人群数、分位数分层、mix share）”来分析，不要只做均值总结。希望输出能支持编辑策略讨论，例如：哪些小时/日期/城区更容易落入高流量分层，哪些性别和年龄段的高阈值占比更高，以及不同阈值下的结构变化。请把分析拆成可并行的 4-6 个独立子任务，并最终整理成 analysis_summary.json。
```

### 59. D4_k983351_zh (domain=D4, difficulty=4)

```
请基于文件 balabaskar__bitcoin-news-articles-text-corpora__bitcoin_articles.csv 做一版面向内容/编辑分析的深度诊断，重点看“排名与集中度”：哪些主题、来源、作者、国家/语言、发布时间段最集中，头部内容是否吞噬大部分曝光/分数，以及这种集中是否在不同切片里一致。请你把分析拆成若干可并行的部分，最后给我一份适合汇报给编辑/内容运营团队的结论，最好能指出前10/前20占比、Top-N 贡献、Pareto 现象、以及异常集中的来源或作者。请务必只用数据本身，不要臆测。
```

### 60. D4_k983444_zh (domain=D4, difficulty=4)

```
请基于文件 thebumpkin__10400-classic-hits-10-genres-1923-to-2023__ClassicHit.csv 做一份面向内容/编辑团队的深度分析，重点围绕时间趋势和阶段变化来判断“经典热歌”在不同年代的内容形态是否发生了系统性迁移。请你把分析拆成可并行推进的几块：先看 Year 维度上的长期趋势与拐点，再看各 Genre 在不同年代的增长/衰退和代表性年代，再比较音频特征（Duration、Danceability、Energy、Loudness、Acousticness、Valence、Tempo 等）随时间的变化轨迹，最后结合 Popularity 与 Genre/年份判断哪些类型更像是“老歌长期稳定回流”而哪些是“近年爆发型”。请输出一个适合给编辑团队决策的结论摘要，并附带可复核的关键统计结果。数据里已有真实列：Track、Artist、Year、Duration、Time_Signature、Danceability、Energy、Key、Loudness、Mode、Speechiness、Acousticness、Instrumentalness、Liveness、Valence、Tempo、Popularity、Genre。请注意所有判断都要基于这份固定数据，不要编造任何值。
```

### 61. D4_k983489_en (domain=D4, difficulty=4)

```
Using the file bhadramohit__social-media-usage-datasetapplications__social_media_usage.csv and the columns User_ID, App, Daily_Minutes_Spent, Posts_Per_Day, Likes_Per_Day, and Follows_Per_Day, run a content/editorial analytics review focused mainly on data quality. I need a practical audit that tells me whether this dataset is trustworthy enough for editorial reporting. Please check for missing values, blank strings, literal '?' placeholders, duplicate records, range violations in the numeric fields, and inconsistent App categories. Then, as supporting context, summarize how usage and engagement differ by app so I can judge whether any data issues could distort content insights. I want this broken into independent workstreams so different people could work in parallel, and I only need a concise JSON summary file in the end.
```

### 62. D4_k983649_en (domain=D4, difficulty=4)

```
Using the file thebumpkin__300-world-music-tracks-with-spotify-data__WorldHits.csv, do a content/editorial analytics pass focused mainly on anomaly and outlier detection with explicit numeric rules. I need you to identify and summarize tracks that look editorially unusual or potentially data-quality suspicious using thresholds, IQR-style rules, rare categories, and extreme values across the real columns Track, Artist, Album, Year, Duration, Time_Signature, Danceability, Energy, Key, Loudness, Mode, Speechiness, Acousticness, Instrumentalness, Liveness, Valence, Tempo, and Popularity. Please split the work into independent tracks so different analysts could work in parallel: one track on extreme audio-feature outliers, one on rare structural metadata values, one on year/duration/popularity anomalies, one on artist/album concentration and repeated-entity oddities, and one on combined multi-criterion anomaly flags. I want a compact analysis_summary.json with the key findings, counts, and the exact songs/artists that trigger the rules.
```

### 63. D5_g980313_en (domain=D5, difficulty=4)

```
You are auditing a synthetic codebase and test corpus assembled from several bug-fix patterns. Review the provided inputs and produce a concise security-and-quality audit. Focus on identifying the highest-risk issues, the affected modules, and the evidence present in the logs and configuration files.
```

### 64. D5_g980569_en (domain=D5, difficulty=4)

```
You are given two input files under inputs/: a CSV inventory of code snippets and a JSON file with seed task metadata.
Your goal is to analyze the inventory and produce a concise quality report.

Deliverables:
1. Summarize the inventory by module and by issue_tag.
2. Identify the most frequent module and the most frequent non-OK issue_tag.
3. Mention any notable patterns you observe in the seed tasks and the code inventory.

Tool target: use the files in inputs/ only. Do not modify the inputs.
Subanalysis hint: compute aggregate counts first, then derive the top categories and a short narrative.
```

### 65. D5_g981209_zh (domain=D5, difficulty=4)

```
请审计这个小项目的代码、测试日志和配置文件，整理成一份综合报告。输入文件是 inputs/code_audit.xlsx、inputs/test_logs.xlsx、inputs/config_audit.xlsx 和 inputs/project_brief.docx。
- 分别做代码静态审查、测试失败归因、配置/依赖风险审查，再把结果合并成统一结论。
- 只关注文档里列出的明确问题类型；把命中的模块、文件、测试运行和配置项都汇总清楚。
- 最后给出修复优先级和一个简短的验证计划，说明先改什么、怎么复测。
- 输出一个简洁的综合报告文件即可，不要拆成很多份。
```

### 66. D5_g981297_en (domain=D5, difficulty=4)

```
Hi, I've attached two files: project_data.xlsx and codebase_audit_logs.json. Need a full audit: static code review of module A, security review of module B, test failure triage, and dependency/config check. Please give me a single report summarizing all findings.
```

### 67. D5_g982377_zh (domain=D5, difficulty=4)

```
你好，我们需要对一个包含两个模块（app_a 和 app_b）的Python项目进行复合审计。项目代码、测试日志和配置文件分别存放在以下三个文件中（均在 inputs/ 目录下）：

1. codebase_modules.xlsx：模块A和B的代码行（每行一条记录），包含真实代码片段及一些已知的常见安全漏洞模式。
2. test_results.xlsx：最近一次测试运行的结果，包含通过/失败/错误状态。
3. config_files.xlsx：不同环境（production, development, staging）的配置键值对。

请你协调一个团队并行执行以下四项子分析，并最终输出一份决策建议（decision_brief.md），汇总每个子分析的关键发现，并给出修复优先级建议。四项子分析分别是：
- 子分析A：对模块A进行静态代码审查，检测危险API调用（具体模式见评估标准）。
- 子分析B：对模块B进行安全/风险审查，查找硬编码密码和弱哈希使用。
- 子分析C：对测试日志进行失败分类统计（总测试数、失败数、通过数）。
- 子分析D：对配置文件进行审计，识别生产环境中的错误配置（DEBUG=True、短密钥、通配符主机等）。

请确保每个子分析都输出精确的数值，并在最终决策文件中引用这些数值。团队可以使用Python和命令行工具（grep等）处理文件。文件已放在 inputs/ 下，请开始。
```

### 68. D5_g982925_en (domain=D5, difficulty=4)

```
I need a single compact audit report for the codebase and the attached logs because we need to decide what to fix before the next release. Please review inputs/code_audit.xlsx, inputs/logs.xlsx, inputs/tests.xlsx, inputs/dependencies.xlsx, and inputs/real_seed_embeddings.json, then produce one summary file with the code risks, log/test failures, dependency/config issues, and a short unified fix-and-validation plan.
```

### 69. D5_g982970_zh (domain=D5, difficulty=4)

```
我需要你把 codebase_audit.xlsx 和 test_logs.pdf 里的内容一起做一次代码库审计，最后给我一份紧凑的汇总报告：一部分看模块 A 的兼容性/弃用问题，一部分看模块 B 的安全风险，一部分梳理测试日志里的失败/跳过，再做一部分配置检查，最后把能落地的修复和验证建议合并成一个结论。
```

### 70. D5_g983370_en (domain=D5, difficulty=4)

```
You are given a small codebase audit workbook, a test log workbook, and a brief PDF summary. Analyze the artifacts and produce a concise audit report.
```

### 71. D5_g983699_zh (domain=D5, difficulty=4)

```
请检查 inputs/codebase_audit.xlsx、inputs/dependency_audit.xlsx 和 inputs/test_run.log，输出一份合并后的代码库审计报告，覆盖模块静态审查、风险/安全审查、测试失败归因、以及依赖/配置审计。我只要一个最终汇总文件，格式按你认为最适合交付的来。
```

### 72. D6_g981036_zh (domain=D6, difficulty=4)

```
你好，我是法务部的李明。我们正在进行一项合同收购尽职调查，涉及一批法律文档。我已经把三个输入文件放在 inputs 目录下了：
1. contracts_clauses.xlsx：从各合同中提取的条款列表，包含条款文本、类别、标签等。
2. qa_accuracy.xlsx：之前 NLP 模型在电影脚本上的 QA 准确率测试数据，用于评估模型可靠性。
3. legislation_update.xlsx：新颁布的立法文本，包含禁止性条款关键词。 我需要你帮我生成一个决策文件 recommendation.json，内容是对所有合同（按文件名区分）进行风险排序，并给出前三名需要优先审阅的合同及其理由。风险计算需要综合以下四个独立分析的结果：
- 分析A：每个合同中“控制权变更”条款（class_id=17）的数量。
- 分析B：每个合同中“禁止转让”条款（class_id=18）的数量。
- 分析C：QA 准确率平均值（用于调整模型的可信度）。
- 分析D：每个合同是否包含与立法中禁止性模式匹配的条款（不区分大小写），作为合规冲突标志。 。注意数据中可能存在重复行、标签类别不匹配、QA 答案标记错误等异常，请在计算时正确识别并报告。最终请在 recommendation.json 中输出：
- 按风险总分从高到低排序的所有合同列表（包括每个合同的风险分解值）。
- 最高风险的三个合同的文件名及简要说明。
- 检测到的异常数量：重复行、标签不匹配、QA 不一致项。 先谢谢了。
```

### 73. D6_g981287_en (domain=D6, difficulty=4)

```
You are given two input files: one with contract clauses and one with QA examples.
Analyze them and produce a concise cross-file report that compares the two datasets.
Focus on label distributions, seed-vs-synthetic composition, and any notable field patterns.
Keep the report factual and grounded in the inputs.
```

### 74. D6_g981376_en (domain=D6, difficulty=4)

```
I have three documents in the inputs folder: two contracts (Verizon and RaeSystems) and one movie script excerpts PDF. I need you to extract all change-of-control clauses from the contracts, analyze their ambiguity, and identify any cross-references to movie titles or characters from the movie file. For the movie scripts, compute a defamation risk score based on negative language. Then produce a brief decision brief (decision_brief.md) that synthesizes these analyses into a ranked recommendation of which document requires most urgent legal review. Cite the supporting numbers.
```

### 75. D6_g981415_en (domain=D6, difficulty=4)

```
You are given two documents: 'non_policy_docs.docx' (a movie script summary) and 'policy_docs.docx' (three legislative bills). Your task is to:
1) Determine which documents are policy-related (all bills in policy_docs.docx).
2) Extract the title of each policy document.
3) Determine the total number of policy documents.
4) For the non-policy document, provide the answer to the question it contains.
5) Summarize the type of the non-policy document.
Deliver your results in a structured format as specified below.
```

### 76. D6_g981507_en (domain=D6, difficulty=4)

```
Analyze the provided contract clauses and movie QA pairs. For contract clauses: identify all clauses that belong to class_id '17' (Change Of Control) and list their file names. Also compute the total number of clauses in the file. For movie QA: answer each question based on the plot given, output the answer for each question.
```

### 77. D6_g981853_zh (domain=D6, difficulty=4)

```
这批合同抽取和质检结果要尽快汇总给法务和运营看，我需要你把三份输入文件里的关键信息合成一份简洁报告。请重点看 contract_review_packets.xlsx、processing_log.txt 和 policy_index.json，最后只交一份汇总文件。我要知道合同条款里 Change Of Control 相关内容的整体情况、覆盖和质量问题、以及日志里暴露出来的处理异常，并把需要我优先关注的点一起整理出来。
```

### 78. D6_k982975_en (domain=D6, difficulty=4)

```
Using chicago__chicago-contracts__contracts.csv, I need a contract-records analysis focused mainly on temporal trends and change over time. Please build a compact but thorough review of how contract activity, dollars, and timing evolve across the dataset using the date fields (especially Approval Date, Start Date, and End Date), and relate those trends to contract type, department, and procurement type where useful. I’d like this split into several independent workstreams so different people can work in parallel: one on yearly/period-over-period contract counts and award amounts; one on approval-vs-start/end timing and delays; one on contract type mix over time; one on department-level trend shifts; one on procurement type changes over time; and one on data quality patterns in the date fields. Summarize the findings in a single analysis_summary.json with concise, decision-useful takeaways.
```

### 79. D6_k983294_zh (domain=D6, difficulty=4)

```
请基于文件 pradumn203__payment-date-prediction-for-invoices-dataset__dataset.csv 做一份面向“单据/合同与记录分析”的数据诊断，重点围绕“相关性与驱动因素分析”：找出哪些数值字段彼此同向变化、哪些字段关联最强、以及这些关系是否在不同业务/币种/付款条款下有差异。请结合真实列名（如 buisness_year、doc_id、posting_id、area_business、total_open_amount、baseline_create_date、invoice_id、isOpen、due_in_date、document_create_date、document_create_date.1）来完成。需要输出一份可直接给业务团队看的简洁结论，并附上可复核的统计结果。分析中请特别注意日期类数值字段的相关性、金额字段与单据标识字段的关系、以及缺失值对相关性的潜在影响。请把工作拆成 4-6 个彼此独立的分析轨道，方便并行处理。
```

### 80. D6_k985116_en (domain=D6, difficulty=4)

```
Using jsherman256__sjpd-incidents-arrests-charges__Incidents_All.csv, analyze this incidents dataset for document / contract & records analytics with a focus on distribution and threshold cohorts. I need a practical, decision-oriented readout on how incident records are distributed across dates, times, locations, and incident descriptions, especially how many records fall above/below business thresholds and how the mix changes across buckets. Please break it into independent workstreams so they can be handled in parallel: (1) overall record completeness and field quality, (2) date and time distribution with threshold cohorts and quantile buckets, (3) incident-description mix and concentration, (4) beat and block-address concentration / long-tail analysis, and (5) cross-tabs of cohort segments versus description or beat to spot skew. Use the real columns INCIDENT NO, RPT DATE, RPT TIME, INCIDENT DESCRIPTION, BLOCK ADDRESS, and BEAT; keep all calculations deterministic and grounded in the file.
```

### 81. D7_g981245_zh (domain=D7, difficulty=4)

```
这次我要把 2024-05-14 这起线上事故做成一份最终决策简报，重点是判断后续应该优先推进哪条修复和沟通路径。请你结合 inputs/incident_events.xlsx、inputs/incident_timeline.xlsx、inputs/owner_comms.xlsx，先把影响范围、时间线、负责人和对外沟通状况理清，再给出一个按优先级排序的处置建议。我需要的是一份简短但结论明确的文件，能直接拿去给值班经理和相关团队看。
```

### 82. D7_g983335_en (domain=D7, difficulty=4)

```
You are auditing a small incident dataset and a set of seed texts. Produce a concise analysis that cross-checks the inputs and summarizes the operational pattern. Use the provided files in OUT_DIR/inputs/.
```

### 83. D7_k982230_zh (domain=D7, difficulty=4)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维/日志与事件分析的复杂排查分析，重点围绕“相关性与驱动因素分析”：哪些数值字段会一起变化、哪些关联最强、不同协议/流量类型下这些关系是否一致，以及异常记录是否呈现出与正常记录不同的数值模式。请直接使用现有列（Date first seen, Duration, Proto, Src IP Addr, Src Pt, Dst IP Addr, Dst Pt, Packets, Bytes, Flows, Flags, Tos, class, attackType, attackID, attackDescription），不要改动数据。最终请输出一个可交付给运维/安全团队的 analysis_summary.json，里面要包含：1）全局数值字段相关性矩阵的要点；2）最强的正/负相关对；3）按 class 分组的相关性差异；4）按 Proto 分组的关键相关性；5）正常/可疑/未知三类在包数、字节数、持续时间上的分布对比；6）能够解释这些相关性的可能驱动因素（例如连接持续时间、包数、字节数、端口特征）。如果有需要，请额外检查攻击类型/描述字段是否全为空或只有占位符，以判断这些字段对驱动分析是否有实际贡献。
```

### 84. D7_k982276_en (domain=D7, difficulty=4)

```
Using kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv, do a segmented incident-analytics review of the external-week1 server logs with a focus on how suspicious vs normal traffic differs across categorical groups. I want a concise but rigorous comparison of rates and average values by segment, plus the biggest gaps between segments. Please break the work into independent tracks so different analysts can run them in parallel: compare class distribution by Proto, by Src IP Addr bucket, and by Dst IP Addr bucket; compare mean Duration / Packets / Bytes by class across key segments; identify which source and destination segments have the largest suspicious-rate gaps; and summarize any notable differences in Flags and attackType/attackID patterns. Use only the fixed data in the file and report results in a compact JSON summary.
```

### 85. D7_k982476_zh (domain=D7, difficulty=4)

```
请基于数据文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维/日志与事件分析的排查简报，重点围绕“排名与集中度”：先找出最常见的流量/连接模式、最集中的来源与目的端，再看这些高频组是否贡献了大部分流量/字节/包数，并判断是否存在明显的 Pareto 集中现象。请结合真实列名（如 Date first seen、Duration、Proto、Src IP Addr、Src Pt、Dst IP Addr、Dst Pt、Packets、Bytes、Flows、Flags、Tos、class、attackType、attackID、attackDescription）输出可执行的分析结论。需要拆成多个独立分析轨道，方便不同子任务并行：1）总体流量与标签分布概览；2）按 Src IP Addr / Dst IP Addr 的 Top-N 集中度；3）按 Proto / Flags / Dst Pt 的 Top-N 排名与占比；4）按 class、attackType 的集中度与异常占比；5）按 Bytes、Packets、Duration 的头部贡献与 Pareto；6）可选的时间维度高峰段排名（Date first seen 按日期或小时聚合）。请输出适合运维值班查看的结论，注明哪些群组占了大部分流量，以及是否需要优先关注少数高频源、目的端或端口。
```

### 86. D7_k983042_zh (domain=D7, difficulty=4)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维 / 日志与事件分析的多部分排查分析，重点围绕“数值字段之间的相关性与驱动因素”展开：先把数据里可量化的字段（例如 Duration、Src Pt、Dst Pt、Packets、Tos、以及从 Bytes 清洗成数值后的字节数）之间的两两相关性、分组相关性和高关联对找出来，并结合 class / attackType / attackDescription 看看哪些数值模式更像 normal、suspicious、unknown；再按 Proto、Flags、Src IP Addr、Dst IP Addr 做分组，比较均值、中位数和高频组合，识别最可能的业务流量和异常流量驱动项。请把结果组织成 4-6 个彼此独立的分析轨道，适合多个子任务并行推进。最后输出一份可直接交付的 analysis_summary.json，里面要有核心相关系数、Top 关联对、按类别的关键差异、以及几个可复核的定量结论。请确保所有数字都来自这份数据文件本身，不要做任何假设。
```

### 87. D8_g980700_en (domain=D8, difficulty=4)

```
You are given a synthetic knowledge-base audit dataset. Analyze the files in inputs/ and prepare a remediation summary focused on stale records, duplicate/ambiguous entries, and coverage gaps.
```

### 88. D8_g980760_en (domain=D8, difficulty=4)

```
You are auditing a mixed KB dataset with real seed rows and synthetic rows. Produce a concise analysis of the dataset, focusing on record composition, status/category patterns, and staleness.
```

### 89. D8_g980970_en (domain=D8, difficulty=4)

```
We have three files from our knowledge base audit project. The first is a list of all KB articles with their last update dates, content, and status. The second is a log of user queries over the last few months. The third is an external audit report that flags some known issues. I need you to produce a single Excel report that summarizes the audit findings. Specifically, I need to know:
- Which active articles are stale (not updated in over 6 months)?
- Which articles have incorrect content (their answer doesn't match the question)?
- Are there any duplicate article titles?
- Which user queries are not covered by any existing article?
- What are the most critical issues in the external audit?
Please compile all into a compact report with a summary sheet and supporting details. The final deliverable should be one Excel file named kb_audit_report.xlsx.
```

### 90. D8_k982112_en (domain=D8, difficulty=4)

```
Using `inputs/tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv`, analyze the support-ticket knowledge base across `subject`, `body`, `answer`, `type`, `queue`, `priority`, `language`, and `tag_1` through `tag_8`. I need a ranking-and-concentration view: identify the dominant queues, languages, priorities, ticket types, and tags; quantify how much of the workload is held by the top groups; surface Pareto-style concentration patterns; and flag where metadata sparsity or missing subjects could distort routing or knowledge-base decisions. Keep the work split into independent tracks so separate analysts could run them, and produce the final results as `analysis_summary.json`.
```

### 91. D8_k982254_zh (domain=D8, difficulty=4)

```
请基于文件 suraj520__customer-support-ticket-dataset__customer_support_tickets.csv 做一份面向知识库/工单运营的综合分析，重点围绕时间维度和趋势变化来展开：我想知道不同时间段里工单量、响应速度、处理时长、满意度、以及问题类型结构有没有明显变化。请直接用数据里的真实字段（Ticket ID、Date of Purchase、Ticket Status、Ticket Type、Ticket Subject、Ticket Priority、Ticket Channel、First Response Time、Time to Resolution、Customer Satisfaction Rating、Product Purchased、Customer Age、Customer Gender 等）做分析，不要编造业务假设。最好能帮我识别出按月/按年份的变化、不同优先级与渠道在时间上的表现差异、以及哪些类别在后期更容易积压或评价更差。输出希望适合我直接给团队开会用，分成几个独立分析块，最后给一个精炼结论。
```

### 92. D8_k982679_zh (domain=D8, difficulty=4)

```
请基于文件 `tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv` 做一份面向知识/客服工单分析的深度拆解，重点围绕“排名与集中度”来判断资源是否被少数主题、队列、优先级和语言占用。请结合 `subject`, `body`, `answer`, `type`, `queue`, `priority`, `language`, `tag_1` 到 `tag_8` 这些列，输出能直接给管理层看的结论：哪些类别最集中、前几名累计占比有多高、是否存在明显的 80/20 现象，以及高频主题是否伴随更高优先级或特定语言分布。请把分析拆成 4-6 个彼此独立的 track，便于并行推进：例如按队列/类型做 Top-N 集中度、按语言做占比与集中度、按优先级做分布、按标签做频次排行与缺失情况、按主题文本特征做高频主题聚类式归纳（只用统计，不做建模）。最后给我一个可复核的 summary JSON 结构，里面要能直接看到每个 track 的核心排名、Top3/Top5 占比、以及你认为值得关注的异常点。
```

### 93. D8_k982973_en (domain=D8, difficulty=4)

```
Using the file tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv, please run a support-ticket analytics deep dive focused mainly on ranking and concentration. I need to know which ticket types, queues, priorities, languages, and tags dominate the workload, how concentrated the volume is in the top groups, and whether the mix changes by language or queue. Please break this into a few independent workstreams so different people could work in parallel, and keep the output practical for a support operations review using the columns subject, body, answer, type, queue, priority, language, and tag_1 through tag_8.
```

### 94. D9_g981009_zh (domain=D9, difficulty=4)

```
我们要把这批漏洞和整改线索做成一份可给管理层看的汇总，重点看当前风险、超期情况和最紧急的前10项。请综合处理 cve_catalog.xlsx、asset_register.xlsx、findings_triage.xlsx，输出一份精简但完整的结果文件，里面要有按严重度和状态的总量、SLA超期统计、按风险分排序的TOP10明细、以及需要优先盯住的资产ID。我只需要一个整合好的交付物，便于直接发给风险委员会。
```

### 95. D9_g981026_zh (domain=D9, difficulty=4)

```
请基于 inputs/ 下的 vulnerability_inventory.xlsx、remediation_tracker.xlsx、sla_controls.xlsx 做一份 findings.md。我需要你把三份来源串起来，输出一份简洁的三四段分析 brief，重点说清楚总体严重度分布、TOP-10 紧急项、SLA 逾期情况、以及三份来源之间的冲突/重复/口径差异。另外单独列出少量最需要优先盯住的资产 ID。
```

### 96. D9_k982203_en (domain=D9, difficulty=4)

```
Using `inputs/sampadab17__network-intrusion-detection__Test_data.csv`, analyze concentration and ranking patterns in this network-intrusion test set. Focus on which `service`, `protocol_type`, `flag`, and service/flag combinations dominate the 1,500 records, how much of the traffic volume and error behavior is concentrated in the top groups, and whether a small number of services account for most suspicious signals such as zero-payload connections, failed logins, high `serror_rate`, and high `rerror_rate`. Keep the work grounded in the actual columns such as `duration`, `protocol_type`, `service`, `flag`, `src_bytes`, `dst_bytes`, `num_failed_logins`, `logged_in`, `count`, `srv_count`, `serror_rate`, `rerror_rate`, `same_srv_rate`, `diff_srv_rate`, and the `dst_host_*` rate/count fields. Return compact ranked findings and Pareto-style concentration metrics suitable for a security analyst triage brief.
```

### 97. D9_k982208_en (domain=D9, difficulty=4)

```
Analyze the CSV file subhajournal__iotintrusion__IoT_Intrusion.csv as a security analytics data-quality audit, with the main focus on missing values (including literal '?' and blanks), duplicates, range violations, and inconsistent categorical encodings. Use the actual columns in the file, including flow_duration, Header_Length, Protocol Type, Duration, Rate, Srate, Drate, the TCP/UDP/HTTP/HTTPS/DNS/etc. flags, the traffic summary fields like Tot sum, Min, Max, AVG, Std, Tot size, IAT, Number, Magnitue, Radius, Covariance, Variance, Weight, and label. I need a compact but thorough audit that tells me where the dataset is clean, where it is suspicious, and whether any labels or protocol/service indicator fields look inconsistent. Organize the work so multiple analysts can work independently on different tracks, and keep the output suitable for a single analysis_summary.json deliverable.
```

### 98. D9_k982216_en (domain=D9, difficulty=4)

```
Using `inputs/sampadab17__network-intrusion-detection__Train_data.csv`, run a security-analytics correlation and driver analysis on the 1,500 network connection records. Focus on which numeric fields move together, which numeric and categorical fields are most associated with `class` being `anomaly` vs `normal`, and where redundant or highly collinear indicators appear. Please analyze the real columns in the file, including connection attributes like `duration`, `protocol_type`, `service`, `flag`, byte counts, login/content fields, traffic-window metrics such as `count`, `srv_count`, rates such as `serror_rate`, `rerror_rate`, `same_srv_rate`, `diff_srv_rate`, destination-host metrics like `dst_host_count`, `dst_host_srv_count`, `dst_host_same_srv_rate`, `dst_host_serror_rate`, and the target column `class`. Keep this practical for intrusion-detection triage: identify top correlation pairs, likely drivers of anomaly labels, categorical hotspots, redundant features, and any data-quality quirks that affect interpretation.
```

### 99. D9_k982238_en (domain=D9, difficulty=4)

```
Analyze the security-analytics dataset in subhajournal__iotintrusion__IoT_Intrusion.csv. I need a concise but rigorous ranking-and-concentration review of the attack traffic: identify which labels dominate the dataset, how concentrated the distribution is across attack types, which protocols/flags/ports are most associated with the highest-volume labels, and whether a small subset of categories accounts for most of the traffic. Please use the real columns in the file, especially label, Protocol Type, flow_duration, Duration, Rate, Srate, Drate, fin_flag_number, syn_flag_number, rst_flag_number, psh_flag_number, ack_flag_number, HTTP, HTTPS, DNS, Telnet, SMTP, SSH, IRC, TCP, UDP, DHCP, ARP, ICMP, IPv, LLC, Tot sum, Tot size, Number, Magnitue, Radius, Covariance, Variance, and Weight. Break the work into independent tracks so different analysts could work in parallel: label concentration, protocol concentration, flag concentration, port/service concentration, and high-volume feature profiles by label. I need the final output as a compact analysis summary JSON.
```

### 100. D9_k982398_zh (domain=D9, difficulty=4)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一版安全分析，重点放在“数值字段之间的相关性与驱动因素”上：请找出哪些数值特征彼此最同步变化、哪些特征对攻击/异常迹象最有解释力，并把相关性结果按两位小数汇总。请结合真实列名（例如 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_serror_rate、dst_host_rerror_rate 等）做分析，不要只给整体结论。希望最终输出一份可交付的 analysis_summary.json。请拆成 4-6 个彼此独立的分析轨道：一条做全量数值相关性矩阵与最高/最低相关对，一条做与核心拥塞/错误率变量的驱动因素排序，一条比较不同协议/flag 下关键相关结构的差异，一条关注高频计数类字段（count、srv_count、dst_host_count 等）的联动，一条排查最极端样本的共同特征，必要时再补一条做缺失值与字段覆盖检查。请给出每条轨道的关键发现、可复核的统计结果，以及适合安全运营解释的结论。
```

### 101. D9_k982546_zh (domain=D9, difficulty=4)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全分析的多部分数据解读，重点围绕“排名与集中度”来做：哪些协议/服务/标志类型最集中、正常与异常流量各自主要由哪些类别贡献、以及头部类别是否占据了绝大部分样本。我需要你把结果拆成 4-6 条彼此独立的分析线，方便我分给不同子任务并行跑。请结合真实列名分析：protocol_type、service、flag、class、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、dst_host_count、dst_host_srv_count 等，输出一个适合汇报的简洁结论摘要，并尽量给出 Top-N、份额、累计占比、Pareto/集中度指标和正常/异常对比。不要做建模，只做确定性统计分析。
```

### 102. D9_k983038_zh (domain=D9, difficulty=4)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份偏安全运营视角的复杂分析，重点围绕“按流量序列/记录顺序观察异常与正常行为的变化趋势”展开。数据里没有显式日期，请把行顺序当作观测序列，按时间窗口（例如前后 20%、前中后 3 段、滚动窗口）比较异常率、关键连接特征和服务分布是否发生阶段性变化，并判断哪些类别或特征最能解释这种变化。请同时结合 class、protocol_type、service、flag、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_serror_rate、dst_host_rerror_rate 等字段，输出可给安全负责人直接看的结论：1）异常是否随序列阶段上升/下降；2）哪一段最“危险”；3）哪些协议/服务/标志在不同阶段变化最明显；4）是否存在典型的扫描/爆破/拒绝服务式信号。请把分析拆成若干独立子任务并可并行执行，最后汇总成一份简洁的分析摘要与可复核的统计结果。
```

### 103. D9_k983135_zh (domain=D9, difficulty=4)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的分布与阈值分层分析报告，重点围绕“业务阈值以上/以下的样本数量、分位桶分布、以及不同攻击标签的流量构成占比”。我需要你先把数据当作真实入侵检测日志来处理，直接使用现有字段，不要假设任何额外列。请重点围绕这些字段展开：flow_duration、Header_Length、Protocol Type、Duration、Rate、Srate、Drate、ack_count、syn_count、fin_count、urg_count、rst_count，以及标签列 label；同时也要结合协议/服务指示列（HTTP、HTTPS、DNS、Telnet、SMTP、SSH、IRC、TCP、UDP、DHCP、ARP、ICMP、IPv、LLC）做阈值穿透和混合占比分析。

请把分析拆成 4-6 个相互独立的分析轨道：
1) 关键流量指标的阈值 cohort 划分（例如高/低速率、高/低时长、高/低头部长度），并比较各 cohort 的样本量与标签构成；
2) 按分位数分桶看 rate / Srate / Drate / flow_duration 的分布，找出每个桶里的主要攻击类型和占比；
3) 识别在业务阈值之上占比最高的攻击标签，以及它们在协议列上的 mix share；
4) 对 flag/count 类字段做极值与阈值穿透统计，观察不同攻击类别在 SYN/ACK/RST/FIN 行为上的分布差异；
5) 统计协议/服务指示列的命中率、共现模式和标签偏好，尤其关注 TCP/UDP/ICMP/DNS/HTTP/HTTPS 的组合；
6) 输出一个简洁的结论摘要，说明哪些阈值最能区分 DoS、DDoS、Mirai、Spoofing 等大类。

请注意：这是固定真实数据，所有数字必须严格从数据中计算，不允许编造。最终请输出适合内部汇报的 analysis_summary.json 结构化结果，重点是可复核的计数、占比、分位桶和阈值 cohort 结论。
```

### 104. D9_k983217_en (domain=D9, difficulty=4)

```
Use sampadab17__network-intrusion-detection__Test_data.csv to run a security-analytics deep dive focused mainly on correlation and driver analysis: identify which numeric fields move together, report the strongest rounded correlations, and explain which traffic/session features appear to be the main drivers of abnormal network behavior. Decompose this into independent workstreams so they can be analyzed in parallel: (1) overall numeric correlation structure and strongest pairwise associations, (2) how volume/session counters relate to attack-indicative rates, (3) protocol/service/flag context for the most correlated patterns, (4) correlation differences between logged-in vs non-logged-in traffic, and (5) a compact operational summary of the most influential variables and any surprising negatives or near-constants. Keep everything grounded in the real columns in the file and use only deterministic pandas-based analysis.
```

### 105. D10_g981654_en (domain=D10, difficulty=5)

```
You are given a customer reviews and account metrics dataset. Produce a concise bilingual-style business brief in Chinese that summarizes sentiment, topic clusters, high-risk accounts, and recommended actions for customer and marketing operations.
```

### 106. D10_k983525_en (domain=D10, difficulty=5)

```
Using radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv, please do a customer-analytics deep dive focused mainly on correlation and driver analysis. I need a practical readout of which numeric fields move together and which variables are most associated with Exited. Break it into independent workstreams so multiple analysts can work in parallel: (1) data quality and basic profiling of the numeric vs categorical fields, (2) rounded correlation analysis across all numeric columns with emphasis on the strongest positive/negative associations, (3) churn-driver analysis for Exited using correlations plus segmented comparisons by key fields like Geography, Gender, and Card Type, (4) product/engagement patterns using NumOfProducts, HasCrCard, IsActiveMember, Tenure, and Point Earned, and (5) customer value context using CreditScore, Balance, and EstimatedSalary to understand whether higher-value customers behave differently. Please summarize the main associations, call out the top correlated pairs, and identify the strongest numeric drivers of churn from this dataset.
```

### 107. D10_k983723_en (domain=D10, difficulty=5)

```
Using the file radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv, build a customer-churn analysis focused mainly on distribution and threshold cohorts. I need a practical readout of how the portfolio is split across key business cutoffs and quantile buckets, especially for Age, CreditScore, Balance, EstimatedSalary, NumOfProducts, Tenure, Satisfaction Score, Point Earned, and the churn-related flags Exited and Complain. Please treat this as a real customer analytics task and make it actionable: quantify how many customers sit above/below important thresholds, how churn mix changes across cohorts, and where the biggest concentration sits by geography, gender, card type, and activity status. Use the real columns in the file, and keep the analysis grounded in counts, shares, and simple summary stats rather than modeling. I want a concise output file called analysis_summary.json.
```

### 108. D10_k983772_en (domain=D10, difficulty=5)

```
Using blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv, build a customer analytics readout focused mainly on distribution and threshold cohorts. I want this broken into a few independent workstreams so different analysts can work in parallel: quantify how churn and service usage vary across tenure bands, MonthlyCharges quantiles, and TotalCharges thresholds; compare mix shares across contract and payment method segments; identify where the churn concentration sits above/below key business cutoffs; and summarize which customer groups have the highest/lowest exposure to churn-risk cohorts. Please keep it grounded in the real columns in the file (customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn) and use only deterministic pandas analysis.
```

### 109. D10_k984436_en (domain=D10, difficulty=5)

```
Please analyze the file karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv using the columns rating, review_content, likes, publish_time, device_model, game_name, and sentiment. I need a customer-analytics readout focused mainly on ranking and concentration: identify the top games and devices by review volume, quantify how much of total review volume is concentrated in the top groups (top-3, top-5, top-10 where relevant), and check whether high-engagement reviews (by likes) are similarly concentrated. Please also compare these concentration patterns across sentiment and rating segments so I can see whether positivity or negativity is more centralized in a few games. Keep the work modular so different people can handle separate parts of the analysis, and return the final result as analysis_summary.json.
```

### 110. D11_g981441_en (domain=D11, difficulty=5)

```
I need you to review the three source files in inputs/ and put together one concise findings brief on finance close and spend variance: compare budget vs actuals, summarize invoice and policy exceptions, and reconcile anything material across the sources. Please focus on the biggest variances by cost center and category, the main exception counts, and a short top-material-items table so I can see what needs follow-up.
```

### 111. D11_k982875_en (domain=D11, difficulty=5)

```
Using yasserh__loan-default-dataset__Loan_Default.csv, build a finance analytics brief focused mainly on ranking and concentration. I need a clear view of where the loan book is concentrated across the real columns in this file, especially the biggest buckets by count and by monetary exposure. Break the work into independent tracks so different analysts could work in parallel: identify the top segments by loan count, the top segments by total loan_amount, concentration among risk outcomes (Status), concentration by Region, and whether the biggest exposures are also the highest-default segments. Use the actual columns such as loan_type, loan_purpose, Gender, age, Region, loan_amount, property_value, income, Credit_Score, LTV, and Status. Summarize the Pareto-style concentration (e.g., top 3 / top 5 shares) and any notable ranking mismatches between volume and risk.
```

### 112. D11_k984580_en (domain=D11, difficulty=5)

```
Using inputs/itssuru__loan-data__loan_data.csv, run a finance-focused anomaly review of the loan book. I need a structured readout built mainly around explicit numeric outlier rules, not modeling: identify extreme values in int.rate, installment, dti, fico, days.with.cr.line, revol.bal, revol.util, and inq.last.6mths; flag rare purpose categories; check whether anomalous loans cluster in not.fully.paid or low credit.policy; and summarize any concentrated high-risk pockets by simple threshold / IQR / rarity rules. Please split the work into independent tracks so different analysts could handle them in parallel, and return a concise summary JSON with the key counts, rates, and cross-tabs.
```

### 113. D12_g981693_en (domain=D12, difficulty=5)

```
You are given a small HR analytics workbook and a JSON file of seed records.
Use the provided inputs to perform a compact analysis and produce a concise report.

Deliverables:
1) Summarize the employee data, including overall headcount, department distribution, and skill/interview trends.
2) Identify any notable patterns in performance and promotion data.
3) Briefly note how the embedded seed records appear to span different task families (e.g., resume/job matching, tabular profiling).

Tool target: the files in the inputs/ directory, especially hr_analytics_workbook.xlsx and seed_records.json.

Sub-analyses hint: inspect each sheet separately, then aggregate by department, track, and skill; compare counts and averages.
```

### 114. D12_k982945_en (domain=D12, difficulty=5)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, please run a compact HR attrition concentration analysis focused on ranking and Pareto-style concentration. I need this broken into a few independent workstreams so different analysts could work in parallel. Please: (1) rank the highest-attrition groups by Attrition, JobRole, Department, MaritalStatus, and BusinessTravel; (2) quantify how concentrated attrition is in the top groups within each of those dimensions using shares of total attrition; (3) check whether overtime and distance-from-home also show concentrated attrition patterns among the top bins; (4) compare the top contributors to attrition versus their prevalence in the workforce; and (5) identify whether a small set of segments accounts for a disproportionate share of leavers. Use the real columns in the dataset, and keep the output concise and decision-oriented.
```

### 115. D12_k983169_en (domain=D12, difficulty=5)

```
Using pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, please build a people-analytics brief focused mainly on ranking and concentration patterns in the workforce. I want a practical readout of where headcount, pay, tenure, and attrition are most concentrated, especially the top groups driving the largest shares of employees or attrition. Please use the real columns in the file, including Attrition, Department, JobRole, BusinessTravel, MaritalStatus, OverTime, Age, MonthlyIncome, TotalWorkingYears, YearsAtCompany, YearsInCurrentRole, StockOptionLevel, TrainingTimesLastYear, JobSatisfaction, EnvironmentSatisfaction, and any other fields you need. Break the work into independent tracks so they can be done in parallel: (1) rank the biggest concentration pockets of headcount by department/job role/business travel, (2) identify the top attrition drivers and how much of total attrition they account for, (3) measure pay concentration and whether the top income groups hold a disproportionate share of payroll, (4) compare tenure concentration across the longest-tenured groups versus the rest, and (5) check whether overtime or marital status are concentrated among leavers versus the whole population. Summarize the findings with a concise, decision-ready output.
```

### 116. D12_k983238_en (domain=D12, difficulty=5)

```
Using the file patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a people-analytics readout focused mainly on correlation and driver analysis for attrition. I need you to identify which numeric fields move together, surface the strongest rounded correlations, and translate those patterns into practical HR signals. Please break the work into a few independent tracks so it can be handled in parallel: (1) overall data profiling and attrition split, (2) correlation structure among the numeric HR fields, (3) driver comparisons for attrition vs. no attrition on key pay, tenure, and workload variables, (4) role/department and overtime patterns tied to attrition, and (5) a short prioritization of the most actionable risk indicators. Keep it grounded in the actual columns in this dataset, especially Age, MonthlyIncome, TotalWorkingYears, JobLevel, DistanceFromHome, OverTime, JobSatisfaction, WorkLifeBalance, YearsAtCompany, and YearsInCurrentRole.
```

### 117. D12_k983910_en (domain=D12, difficulty=5)

```
Using the file patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a people-analytics attrition brief focused mainly on correlation and driver analysis. I need you to identify which numeric fields move together, surface the strongest rounded correlations, and translate those patterns into likely attrition drivers using the real columns in this dataset (for example Age, MonthlyIncome, TotalWorkingYears, JobLevel, StockOptionLevel, PercentSalaryHike, TrainingTimesLastYear, DistanceFromHome, YearsAtCompany, YearsSinceLastPromotion, YearsWithCurrManager, JobSatisfaction, EnvironmentSatisfaction, RelationshipSatisfaction, WorkLifeBalance, JobInvolvement, JobRole, Department, BusinessTravel, OverTime, and Attrition). Please structure it as a compact analyst-ready memo with a few independent workstreams so different sub-agents could work in parallel: one on the numeric correlation map, one on attrition-linked numeric differences, one on categorical attrition concentration, one on a focused subpopulation comparison, and one on a short prioritization of likely drivers. Keep it grounded in this fixed dataset only and use rounded correlations where relevant.
```

### 118. D12_k984096_en (domain=D12, difficulty=5)

```
Using the file patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv, build an HR analytics readout focused mainly on segment comparison across categorical groups and where the biggest gaps are. I want 4-6 independent analysis tracks so separate people can work them in parallel. Please compare Attrition rates and key numeric averages across categories like Department, JobRole, MaritalStatus, BusinessTravel, OverTime, Gender, and EducationField; identify the largest segment gaps; and summarize which groups look most exposed. Also check whether the attrition pattern changes when combining a few categorical dimensions (for example OverTime by Department or MaritalStatus by BusinessTravel). Keep it practical and decision-oriented.
```

### 119. D12_k984135_en (domain=D12, difficulty=5)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build me a people-analytics attrition concentration review focused mainly on ranking and Pareto-style concentration. I need a practical readout of where attrition is concentrated and which employee segments account for the largest share of attrition pressure. Please use the real columns in the dataset, especially Attrition, Department, JobRole, BusinessTravel, OverTime, MaritalStatus, Gender, JobLevel, EducationField, Age, MonthlyIncome, TotalWorkingYears, and DistanceFromHome. Break the work into separate tracks that can be analyzed independently: 1) overall attrition concentration and top-N segments by count/share, 2) concentration by Department and JobRole, 3) concentration by Travel/OverTime/MaritalStatus, 4) concentration by Age and JobLevel bands, 5) income and tenure concentration among leavers, and 6) a concise Pareto summary showing how much of total attrition is covered by the top groups. I want a JSON-ready summary with the key ranked findings and a few deterministic checks.
```

### 120. D12_k984737_zh (domain=D12, difficulty=5)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向 HR 负责人的员工流失分析，重点围绕“排名与集中度”来展开：先找出流失人数最多的前 N 个群体，并计算这些头部群体对总流失的贡献占比，再看是否存在明显的 80/20 集中现象；同时结合 Age、Department、JobRole、MaritalStatus、BusinessTravel、OverTime、JobLevel、YearsAtCompany、MonthlyIncome 等字段，从不同维度拆解流失集中在哪些人群、岗位和工作特征上。请输出可执行的分析结论，而不是泛泛描述。希望你把任务拆成 4-6 个彼此独立的分析轨道，方便并行处理：例如按岗位/部门/婚姻状态/出差与加班/工龄层级的流失排名与集中度、头部群体贡献率、以及相关关键字段的交叉排序。最后请给出一份可汇总成 analysis_summary.json 的结构化结果。文件中的列名请严格使用原始字段名。
```

### 121. D13_g982406_en (domain=D13, difficulty=5)

```
You are given multiple CSV inputs from a synthetic analytics/debugging scenario.
Your job is to audit the datasets, identify data-quality issues, and compute the key summary metrics needed to resolve the discrepancies. Focus on assignments, event timing, reference-table composition, and noise-log anomalies.
```

### 122. D13_k983938_zh (domain=D13, difficulty=5)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份面向产品分析的深度诊断，重点围绕相关性与驱动因素分析：哪些数值字段彼此一起变化、买家下单数量 buy_mount 与时间 day/类目 cat_id/cat1 是否存在稳定关联、以及可疑的高频组合。数据列包括 user_id、auction_id、cat_id、cat1、property、buy_mount、day。请按真实业务口径输出结论：先给总体描述，再给关键相关系数（保留 2 位小数）、高关联字段/组合、以及分组后的差异解读。注意这是固定真实数据，不允许改值或补值。
```

### 123. D13_k983986_zh (domain=D13, difficulty=5)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份面向产品分析的多维数据审计，重点先查数据质量，再看交易行为特征。请围绕这些真实字段 user_id、auction_id、cat_id、cat1、property、buy_mount、day 展开，重点输出：1）缺失值/空字符串/问号占比；2）主键与业务键重复情况（尤其是 user_id、auction_id 组合）；3）数值字段范围是否合理（buy_mount、day、各类 id）；4）cat_id 与 cat1 的一致性和异常映射；5）property 字段的空值、异常分隔符、格式不规范情况；6）在数据质量问题之外，补充一些基础分布和关联性指标，帮助判断这批交易数据是否能直接用于后续转化、复购或商品分析。请把每个分析点拆成独立的小结论，最后给我一份可落地的数据质量审计摘要。
```

### 124. D13_k984036_en (domain=D13, difficulty=5)

```
Using PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv, build a product-analytics readout focused mainly on correlation and driver analysis. I want you to quantify which numeric fields move together, round correlations to 2 decimals, and call out the strongest positive/negative associations in a way that would help a marketplace team understand pricing and rating relationships. Split the work into 4-6 independent tracks so it can be handled in parallel: pricing relationships, rating/price relationships, discount dynamics, category-level differences, brand-level patterns, and data quality checks on missing/placeholder fields. Please use the real columns in the file, especially retail_price, discounted_price, product_rating, overall_rating, brand, product_category_tree, is_FK_Advantage_product, and the text fields only for lightweight grouping or cleanup where needed.
```

### 125. D13_k984472_en (domain=D13, difficulty=5)

```
Using the file akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv and its real columns (user_id, auction_id, cat_id, cat1, property, buy_mount, day), build a product-analytics readout focused mainly on distribution & threshold cohorts. I need you to break the analysis into a few independent workstreams so different people can work in parallel. Specifically: quantify how buy_mount is distributed across business thresholds; build quantile buckets for order size and compare mix shares; identify concentration by heavy-buying users and heavy-selling auctions; compare category/cat1 behavior across low vs high purchase cohorts; and summarize any date-based threshold shifts in buying intensity. Please return a concise analysis_summary.json with the main findings, clear threshold definitions, and the key cohort comparisons.
```

### 126. D13_k985191_en (domain=D13, difficulty=5)

```
Using PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv, build a product-analytics memo focused mainly on correlation and driver analysis across the numeric fields in this catalog. I want you to find which price-related and rating-related fields move together, highlight the strongest positive and negative associations after rounding correlations, and call out any obvious data-quality issues that could distort interpretation. Break the work into a few independent tracks so it can be parallelized: one track on numeric correlation patterns (retail_price, discounted_price, and any rating fields that can be coerced), one track on price-discount structure, one track on brand/category segmentation for the strongest associations, one track on missingness and unusable values in the relevant columns, and one track on a short executive summary of the key drivers and caveats. Keep the output concise but decision-oriented, as if I need to understand what drives price and rating behavior in this marketplace.
```

### 127. D13_k985541_en (domain=D13, difficulty=5)

```
Using utsavdey1410__food-nutrition-dataset__FOOD-DATA-GROUP5.csv, run a product-analytics style driver analysis on the nutrition fields: focus on which numeric attributes move together, which pairs have the strongest positive and negative correlations, and what that implies for positioning foods with different nutrition profiles. Keep it practical for a busy stakeholder: summarize the key correlation patterns, call out any surprising associations, and quantify the strongest relationships using rounded correlations. Also sanity-check the dataset by looking at missingness and a few high-level descriptive slices of the core fields.
```

### 128. D13_k985752_en (domain=D13, difficulty=5)

```
Using the file naushads__flipkart-reviews__flipkart_reviews_dataset.csv, analyze Flipkart product-review performance with an emphasis on ranking and concentration. I need a practical readout of which products dominate review volume and engagement, how concentrated the marketplace is among the top products, and whether the highest-volume products also have stronger review sentiment signals. Please use the real columns product_id, product_title, rating, summary, review, location, date, upvotes, and downvotes. Break this into independent workstreams so different analysts could work in parallel, and return a concise summary I can use for product analytics prioritization.
```

### 129. D1_g1051_zh (domain=D1, difficulty=5)

```
根据输入目录中的日历事件和行动项数据，生成一份面向管理层的紧凑结构化汇总，以及一份面向协调员的简短说明，重点覆盖关键风险、冲突与下一步建议。
```

### 130. D1_g980682_zh (domain=D1, difficulty=5)

```
请根据 inputs/office_collaboration_bundle.xlsx 帮我整理一份深蓝版本发布准备碰头会的分析简报，重点围绕 2026-04-29 这一天，给周川雯、孔璐琪、金诚婷和葛成然安排一个大约一小时的会议窗口。
- 先把四个人当天能同时空出的时间段找出来，并说明最合适的候选窗口。
- 再把相关行动项的推进情况做个状态汇总，顺手看一下有没有需要优先盯的阻塞项、重复项或异常记录。
- 结合状态同步和源材料，把能确认的一致信息写清楚；如果发现前后不一致，也请单独列出来。
- 最后输出一份 findings.md，内容要简洁但能直接拿去给会前协调人看。
```

### 131. D1_g981327_en (domain=D1, difficulty=5)

```
You are given synthetic data files in the 'inputs' folder. Your task is to analyze the data and provide answers for the following deliverables:
1. Calendar Analysis: Identify any anomalies (weekend meetings, overlapping meetings).
2. Action Item Analysis: Count items with missing assignee, items completed after due date, and items completed before creation.
3. Dialogue Summary: Extract the summary from the dialogue '13819578' and the emotion from the nostalgic dialogue.
4. Personality Extraction: List the personality statements and the candidate utterances.
5. Chinese Email: Identify the sender, receiver, and action requested.
Provide your answers in a structured JSON.
```

### 132. D1_k983924_en (domain=D1, difficulty=5)

```
Using ziya07__smart-logistics-supply-chain-dataset__smart_logistics_dataset.csv, run a multi-part operations and collaboration analytics review focused mainly on correlation and driver analysis. I need a concise but decision-ready readout on which numeric fields move together, what the strongest rounded correlations are, and which operational factors look most linked to logistics delay. Please use the real columns in the file: Timestamp, Asset_ID, Latitude, Longitude, Inventory_Level, Shipment_Status, Temperature, Humidity, Traffic_Status, Waiting_Time, User_Transaction_Amount, User_Purchase_Frequency, Logistics_Delay_Reason, Asset_Utilization, Demand_Forecast, and Logistics_Delay. Break the work into independent tracks so it could be handled by a small sub-agent team: 1) overall numeric correlation map and top positive/negative associations, 2) delay-driver comparisons by Logistics_Delay and delay reason, 3) shipment-status and traffic-status operational patterns, 4) inventory/demand/transaction relationship checks, and 5) a short exception scan for missing delay reasons or unusual combinations. I only need factual findings from the dataset, with rounded correlations and small summary counts/means/medians where helpful.
```

### 133. D3_g982706_en (domain=D3, difficulty=5)

```
Review inputs/multisource_panel.xlsx and produce findings.md with a clean synthesis of the wine, adult, and iris sections. I need the main KPI story plus the anomalies that matter, and I want the cross-source comparisons called out clearly.
```

### 134. D3_k982286_en (domain=D3, difficulty=5)

```
Using the file mohamedebrahim88__greater-cairo-real-estate-prices-dataset__Apartments Prices Dataset.csv, run a BI-style driver analysis on apartment pricing. Focus mainly on correlation and what moves together: quantify the strongest relationships between numeric fields, identify how price varies with size/rooms/bathrooms/floor level/year built, and summarize the top associations in a way a business user can act on. Use the real columns price, area_sqm, rooms, bathrooms, floor_level, year_built, seller_type, view, price_per_sqm, payment_method, and finishing_type. I need a compact but rigorous output that can support pricing strategy and sales prioritization.
```

### 135. D3_k982937_en (domain=D3, difficulty=5)

```
Analyze the file ajinilpatel__energy-consumption-prediction__Energy_consumption_dataset.csv for a BI-style driver analysis of EnergyConsumption. Focus primarily on correlation and numeric drivers: quantify which numeric fields move together, round correlations to 2 decimals, and identify the strongest positive/negative associations with EnergyConsumption. I also need supporting breakdowns by time and operating conditions using the real columns Month, Hour, DayOfWeek, Holiday, Temperature, Humidity, SquareFootage, Occupancy, HVACUsage, LightingUsage, RenewableEnergy, and EnergyConsumption. Please structure it as a concise business analysis with clear findings, using the fixed dataset only.
```

### 136. D3_k982944_en (domain=D3, difficulty=5)

```
Using imakash3011__online-shoppers-purchasing-intention-dataset__online_shoppers_intention.csv, I need a BI-style analysis focused mainly on correlation and driver analysis: which numeric fields move together, the strongest rounded correlations, and the most important associations with Revenue. Please structure it as 4-6 independent tracks so different people can work in parallel: one track on numeric correlation structure, one on the strongest Revenue-related numeric drivers, one on visit-duration/page-activity relationships, one on traffic/engagement behavior by visitor type or Weekend, and one on quick sanity checks for the key categorical fields. I need concise, decision-ready findings, not a model. Please return the analysis in a single analysis_summary.json.
```

### 137. D4_g980972_en (domain=D4, difficulty=5)

```
You are given a multilingual content bank with seed records and synthetic rows. Your job is to validate the dataset, detect the embedded anomalies, and compute a compact quality summary. Preserve the task intent around news-label/highlights/summary content and the existing language/size constraints.
```

### 138. D4_k981910_en (domain=D4, difficulty=5)

```
Using the file bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv and its real columns (title, pubDate, guid, link, description), build a content/editorial analytics readout focused mainly on distribution and threshold cohorts. I need a business-style analysis that compares article volume across thresholds and quantile buckets, then breaks that mix down by content type and time. Please decompose it into a few independent workstreams so different analysts can run in parallel: first, overall volume and the share of articles above/below key thresholds for publication frequency; second, quantile bucket analysis for article lengths and description lengths; third, mix-share analysis by domain patterns in guid/link and by article topic cues in titles; fourth, time-based cohort analysis by day/month; and fifth, any notable concentration or skew in the tails. Keep it grounded in the actual dataset only and summarize the findings in a concise JSON deliverable.
```

### 139. D4_k982732_en (domain=D4, difficulty=5)

```
Using kuberiitb__indian-news-articles__historic_articles.csv, I need a content/editorial analytics pass focused mainly on anomaly and outlier detection with explicit numeric rules. Please inspect the real columns source, category, link, author, published_at, header, subheader, and content, and break the work into a few independent tracks so it can be split across sub-agents. I want a compact analysis summary that highlights unusual articles, rare categories/sources/authors, extreme text-length cases, and any date or metadata anomalies. Please use deterministic threshold-based methods only (e.g., IQR, fixed percentile cutoffs, rare-category rules, top/bottom extremes, missing-value counts) and make sure the final output is suitable for editorial review.
```

### 140. D4_k982882_en (domain=D4, difficulty=5)

```
Using sanjidh090__resultpf__bd_eng_news_daily.csv, please do a content/editorial analytics pass focused mainly on ranking and concentration. I want to know which publishers, publication dates, and headline/text themes dominate the dataset, how concentrated the output is in the top groups, and whether there are any clear Pareto-style patterns. Please use the available columns title, text, publish_date, urls, news_collection_time, and publisher (plus the index column if needed only for counting). I need a concise analysis that separates the work into a few independent tracks and ends with a JSON summary of the key findings.
```

### 141. D4_k983183_en (domain=D4, difficulty=5)

```
Using sentinel3734__neurologica-blog-posts__neurologica_articles.csv, analyze the content/editorial performance of these Neurologica posts with an emphasis on ranking and concentration: identify which titles, authors, categories, and publication periods account for the largest share of articles, where the top groups create a Pareto-style concentration, and whether a small number of entities dominate the corpus. Please base everything on the real columns publication_date, title, author, categories, text, and url, and produce an analysis summary that a busy editor could use to understand what the archive is concentrated in and what deserves priority review.
```

### 142. D4_k983217_en (domain=D4, difficulty=5)

```
Using bhadramohit__social-media-usage-datasetapplications__social_media_usage.csv, build an editorial analytics readout focused mainly on correlation and driver analysis. I need you to find which engagement/activity fields move together overall and by app, identify the strongest positive and negative pairwise relationships among Daily_Minutes_Spent, Posts_Per_Day, Likes_Per_Day, and Follows_Per_Day, and summarize whether the patterns differ across Instagram, Facebook, Twitter, LinkedIn, Snapchat, and Pinterest. Please also check for simple concentration signals such as which apps dominate the highest-activity users and whether any single metric looks like the main driver of the others. Keep it practical for a content/editorial team: quantify the rounded correlations, highlight the top associations, and call out any notable app-level differences.
```

### 143. D4_k983288_en (domain=D4, difficulty=5)

```
Using `chanemo__weibo-hot-searchlabeled__weibo-hot-search-labeled.csv` (columns: `日期`, `热搜词条`, `链接`, `标签（时政、科技、科普、娱乐、体育、社会讨论/话题、时事、经济）`), do a content/editorial analytics review focused mainly on ranking and concentration. I need to understand which labels and topics dominate the hot-search list, how concentrated the coverage is in the top groups, whether the distribution follows a Pareto-like pattern, and whether there are obvious differences by time. Please split the work into independent tracks so different people could handle them in parallel: 1) overall label ranking and share concentration, 2) Pareto/top-N concentration by label, 3) daily trend of the top labels, 4) top recurring hot-search phrases and how much of the dataset they occupy, 5) concentration of hot searches around the most repeated labels/topics, and 6) any missing/quality issues that could affect ranking analysis. I need a concise JSON summary with the key metrics and ranked lists.
```

### 144. D4_k983388_en (domain=D4, difficulty=5)

```
Using the file bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv and its columns title, pubDate, guid, link, and description, I need a content/editorial analytics readout focused mainly on temporal trend analysis. Please break it into 4–6 independent workstreams so different analysts can work in parallel: first, map publishing volume over time and compare period-over-period changes; second, look for weekday/weekend or intra-week seasonality in posting patterns; third, identify the fastest-growing and fastest-declining content areas over time using the URL/text signals available in guid/link/title; fourth, check whether article length in title/description is changing over time and whether that relates to publishing cadence; fifth, surface any notable date clusters or outlier spikes that may correspond to editorial events or unusual activity. Deliver the result as analysis_summary.json with concise findings and a few operational recommendations.
```

### 145. D4_k984039_en (domain=D4, difficulty=5)

```
Using the file `inputs/glushko__seth-godins-blogs-dataset__seth-data.csv`, build a content/editorial analytics readout focused mainly on temporal trend analysis. I want you to treat `publication-date` as the timeline and answer: how posting volume, average `stars`, and the mix of topics/titles change over time. Please split the work into 4-6 independent tracks so it could be handled by a small sub-agent team: one track for publication cadence and growth/decline over years and months, one for engagement (`stars`) trends over time, one for identifying the most active periods and weakest periods, one for title/content characteristics changing over time, and one for any notable missing-data or data-quality checks tied to the date field. Use the actual columns in the dataset (`id`, `url`, `title`, `content_plain`, `content_html`, `stars`, `publication-date`, `referral-url`) and produce a concise analysis summary JSON.
```

### 146. D4_k984271_en (domain=D4, difficulty=5)

```
Using the file bhadramohit__social-media-usage-datasetapplications__social_media_usage.csv, I need a content/editorial analytics readout on how usage and engagement differ by platform. Please compare the apps on Daily_Minutes_Spent, Posts_Per_Day, Likes_Per_Day, and Follows_Per_Day, with emphasis on segment gaps between platforms and where the biggest mean/rate differences show up. Break this into a few independent workstreams so different people could handle them in parallel: platform-level averages and rank order, strongest cross-app gaps in engagement behavior, posting intensity versus audience response, outlier-heavy or unusually active platforms, and any pairwise contrasts that would help an editorial team decide where to prioritize content formats. Keep it grounded in the actual data and return concise, decision-oriented findings.
```

### 147. D4_k984368_en (domain=D4, difficulty=5)

```
Using abdallahwagih__books-dataset__data.csv, run a content/editorial analytics review focused mainly on temporal trend analysis. I need a compact decision-ready summary that looks at how the catalog changes over time using published_year, and ties those trends to average_rating, ratings_count, num_pages, and the major categories/authors. Please break it into 4–6 independent workstreams so they can be handled in parallel: year-over-year catalog growth, rating trend shifts by publication year, engagement/rating intensity trends, category mix over time, author concentration in recent years, and any data-quality checks that affect the time analysis. Keep the output business-friendly and grounded in the actual columns in the file.
```

### 148. D4_k984813_en (domain=D4, difficulty=5)

```
Using emirhanai__social-media-usage-and-emotional-well-being__train.csv, run a correlation-and-driver analysis for content/editorial planning: identify which engagement metrics move together most strongly, whether daily usage relates to reactions/messages/emotion outcomes, and where the strongest positive/negative associations are by platform, gender, and age. Please split the work into independent tracks for numeric correlation mapping, top pairwise associations, platform-level comparison, emotion-conditioned patterns, demographic splits, and basic data quality checks on the relevant fields.
```

### 149. D5_g472_zh (domain=D5, difficulty=5)

```
我这里有一组小型代码库和审计资料，麻烦你帮我做一次并行可拆分的联合审计，最后输出 3 份紧凑报告文件：
1) 一份 JSON 总结静态代码审查与安全风险；
2) 一份 CSV 归纳测试失败和服务日志的关键结论；
3) 一份 Markdown 简报，给出统一的修复优先级和验证计划。

请直接基于 ['auth.py', 'billing.py', 'payments.py', 'config_prod.yml', 'config_staging.yml', 'config_dev.yml', 'requirements.txt', 'constraints.txt', 'pytest.log', 'service.log', 'audit.db'] 这些输入文件分析，不要凭空补内容。代码审查里，我只关心这些可机器识别的闭合集合：在源码中逐个统计是否出现 eval(、exec(、pickle.loads、yaml.load(、subprocess.call(、shell=True、sha1(、md5( 这些字面模式；其中 yaml.load 只要不是显式 SafeLoader / safe_load 就算命中，subprocess 只要出现 shell=True 就算命中，密码相关只统计 sha1/md5 这类哈希；配置审计只看生产配置是否存在 debug=true、secret_key 长度小于 16、以及是否把 localhost 放进了生产允许列表。依赖审计只看 requirements.txt 里固定版本依赖的数量，以及有没有明显的高风险组合；测试审计要按 pytest.log 中 FAILED 行数统计失败用例；服务日志审计只统计 ERROR 和 WARN 行数，并把 2024-06-01 这个当天日志当作唯一时间窗口。最后请把这些分开分析的结果合并成一个统一的修复优先级建议，明确哪些问题先修、哪些需要补测、哪些属于配置加固。
```

### 150. D5_g578_en (domain=D5, difficulty=5)

```
We need a quick but trustworthy audit before we decide whether this small service can go into a release candidate. Please review the code and test artifacts in inputs/app.py, inputs/worker.py, inputs/util.py, inputs/prod.ini, inputs/staging.ini, inputs/dev.ini, inputs/audit_manifest.xlsx, inputs/tests.log, and inputs/audit.db. I want one concise decision brief that tells me whether we should block the release, what the biggest risks are, and what we should fix first.

Please use the same rules throughout: for security, count only these exact tokens anywhere in the code files as issues: eval(, exec(, pickle.loads, yaml.load(, shell=True, md5(, sha1(. For config, only count debug=True in prod.ini and a secret_key shorter than 16 characters in prod.ini. For the test log, count only lines marked FAILED, and separate failures that mention one of the security tokens above from the rest. For the dependency audit, use the rows in audit.db as the source of truth. I need a ranked recommendation, with the supporting numbers called out clearly.
```

### 151. D5_g980668_en (domain=D5, difficulty=5)

```
I need a compact audit report for the files in inputs/audit_bundle.xlsx, inputs/app_logs.txt, and inputs/project_meta.json.
- Review the codebase for the security patterns I care about and summarize what shows up.
- Check the config rows for production debug flags and too-short secret keys.
- Triage the test log failures and summarize the failing tests and their count.
- Confirm the embedded real seed items are present and mention any obvious coverage gaps.
- Put everything into one short report with a clear fix-and-validation plan.
```

### 152. D5_g982864_en (domain=D5, difficulty=5)

```
Analyze the supplied audit inputs and produce a concise remediation summary. Use the code audit matrix, test logs, config notes, and triage table to identify the highest-risk open issues and the operational signals that confirm them.
```

### 153. D6_g314_en (domain=D6, difficulty=5)

```
I need you to work through the files in OUT_DIR/inputs/ – contracts_registry.xlsx, policy_handbook.json, billing_incidents.csv, and document_processing_log.txt – and put together 2-3 compact reports that reconcile the contract, policy, and incident data with any clues from the log. Just summarize the key facts and flag any anomalies you find.
```

### 154. D6_g980999_zh (domain=D6, difficulty=5)

```
需要准备一份关于并购合规的分析报告，涉及三个数据文件：
- contracts.xlsx（合同条款提取）
- qna.xlsx（文档问答数据）
- legislation.xlsx（加州立法文本）

请完成以下分析并汇总到一个Excel报告文件中（analysis_report.xlsx）：
1. 统计合同中的条款类型分布，重点标出Change Of Control和Most Favored Nation条款。
2. 查找立法文件中与合同条款相关的通知/变更控制要求。
3. 将问答数据中关于"change of control"或"most favored nation"的问题及其答案关联到对应合同。
4. 检测数据中的异常（重复行、矛盾标记、标题与摘要不匹配等）。
报告中需包含各部分的汇总表格。异常项也一并列出。
```

### 155. D6_g981991_zh (domain=D6, difficulty=5)

```
我需要你分析一下我们公司的合同、政策文件和事件日志。输入文件在inputs目录下：合同表contracts.xlsx，政策文件policy.pdf，事件日志events.json。请帮我整理一份分析简报findings.md。具体来说：从政策PDF里找出超支阈值和生效日期；检查合同中有没有金额异常（负数或超过阈值的）；看看事件日志里有没有包含特定关键词（比如Juggernaut、ghost、supernatural）的严重事件；最后把这些来源的信息综合起来，看看是否有需要特别关注的地方。简报里要列出关键发现和数字。
```

### 156. D6_k983624_en (domain=D6, difficulty=5)

```
Using ghassenkhaled__invoices-data__newest_invoices_data.csv, I need a compact but rigorous contract/invoice records analysis focused on ranking and concentration. Please break it into independent workstreams so different analysts can work in parallel: identify the top clients, services, countries, and invoice statuses by invoice count and by total value; measure how concentrated revenue and invoice volume are in the top groups (top-3, top-5, top-10, and Pareto-style shares); compare whether a small number of clients or services drive most of the billed amount; and flag any notable patterns in overdue vs paid balances and due dates that affect concentration risk. Use the real columns in the file: id_invoice, issuedDate, country, service, total, discount, tax, invoiceStatus, balance, dueDate, client. Deliver the results as analysis_summary.json with clear rankings, share-of-total metrics, and concise insights.
```

### 157. D6_k983770_zh (domain=D6, difficulty=5)

```
请基于文件 pradumn203__payment-date-prediction-for-invoices-dataset__dataset.csv 做一份面向文档/合同与记录管理场景的深度分析，重点放在“数值字段之间的相关性与驱动因素”上：我想知道 total_open_amount、buisness_year、doc_id、posting_id、area_business、baseline_create_date、due_in_date 这些数值列彼此之间有哪些稳定联动关系，哪些是最强的正/负相关，相关性是否会被业务代码 business_code、币种 invoice_currency、付款条款 cust_payment_terms、客户 cust_number 等分类维度放大或削弱。请按下面思路拆成几个并行小组分别做：1）整体数值字段相关矩阵与最强相关对；2）按 business_code / invoice_currency 分组后的相关性对比；3）按 cust_payment_terms 识别最常见且相关性最强的条款；4）围绕 total_open_amount 找出与金额最相关的字段及客户/条款；5）检查缺失值、异常值和日期字段转换后是否影响相关性；6）输出可直接给业务方的“驱动因素优先级”摘要。请注意这是固定真实数据，不要假设或补值，只能基于现有字段做确定性统计。最后请把结果整理成可交付的 JSON 摘要。
```

### 158. D6_k984359_en (domain=D6, difficulty=5)

```
Using ramjasmaurya__nasa-patents__NASA_Patents.csv, please do a records analytics review focused on ranking and concentration. I need a compact but decision-useful assessment of how NASA patent records are distributed across Center, Status, and patent-title patterns, with emphasis on top-N groups, share of total held by the leaders, and whether a small number of entities dominate the dataset. Use the real columns Center, Status, Case Number, Application SN, Title, and Patent Expiration Date. Break the work into independent tracks covering: (1) Center-level concentration and Pareto share, (2) Status mix and dominance, (3) expiration-date clustering / concentration among records with usable dates, (4) title-pattern concentration using the most frequent title keywords or exact titles, and (5) a concise exceptions section for missing or blank fields that could affect ranking analysis. Please return findings in analysis_summary.json and make sure the rankings are based only on the provided file.
```

### 159. D7_g324_en (domain=D7, difficulty=5)

```
Use the files in inputs/ (incident_logs.xlsx, config_services.json, incident_tickets.xlsx, postmortem_notes.md) to investigate the outage of the Serverless Workflow Orchestrator. Produce two compact reports: incident_summary.json with aggregate metrics and timeline_report.md with key events in chronological order.
```

### 160. D7_k982365_en (domain=D7, difficulty=5)

```
Using speedwall10__iot-device-network-logs__Preprocessed_data.csv, analyze the IoT network logs for incident-ops reporting with a primary focus on distribution and threshold cohorts. I need a compact but realistic analysis that breaks the dataset into business-relevant buckets and compares mixes across normality states. Please look at frame.len, ip.len, tcp.len, tcp.srcport, tcp.dstport, Value, and ip.proto, and use the 1500-row file as-is. I want a summary that answers: how many records fall above/below key thresholds, how the data distributes across quantile buckets, how the mix of normality classes changes across those buckets, and whether any obvious port/protocol cohort patterns stand out. Please organize the work so different sub-analysts can handle each track independently and return a single analysis_summary.json.
```

### 161. D7_k984373_en (domain=D7, difficulty=5)

```
Using esathyaprakash__electrical-fault-detection-and-classification__detect_dataset.csv and its real columns (Output (S), Ia, Ib, Ic, Va, Vb, Vc, plus the two unnamed blank columns), build an incident-style analysis for IT ops / logs & incident analytics that focuses mainly on ranking and concentration: identify which signal states or conditions account for most of the records, how concentrated the dataset is in the top groups, and whether a small number of signal patterns dominate. I want this split into a few independent workstreams so different people can work in parallel: frequency concentration by Output (S), top absolute-signal spikes by current/voltage features, missing/blank column validation, relationship between extreme current patterns and Output (S), and a concise Pareto-style summary of where the mass of the dataset sits. Keep it practical and operational, like something that would inform incident triage priorities.
```

### 162. D8_g981483_en (domain=D8, difficulty=5)

```
You are supporting an incident-response review. Use the provided input files to assemble a short evidence-based briefing.
Focus on the two vendor incidents and the related KB pages.
Keep the output concise, but make sure every claim is backed by the supplied data.
```

### 163. D8_g981571_en (domain=D8, difficulty=5)

```
Analyze the provided IT support knowledge-base inputs and logs. Focus on duplicate/anomalous articles, review status, and scenario-to-article mapping.
```

### 164. D8_g981787_en (domain=D8, difficulty=5)

```
You are given a set of knowledge base articles (see inputs/). Perform an audit covering the following aspects:
1. Staleness: Identify articles not updated in the last 90 days (staleness threshold: 2025-03-21 minus 90 days).
2. Gaps: Determine which of the required topics (see required_topics.txt) are not adequately covered by any article (based on tags).
3. Duplicates: Find duplicate articles (same title) and flag them.
4. Incident coverage: Check whether each incident in the given list (see incidents below) is mentioned in at least one article (case-insensitive search in content).
Deliverables: Provide a summary report and a JSON file with the audit results.
Be thorough and list article IDs where applicable.
```

### 165. D8_g981869_en (domain=D8, difficulty=5)

```
We need a clean KB audit pack so I can see where our knowledge base is getting stale, where the content gaps are, and where our tracking data needs cleanup. Please review kb_issues.xlsx, kb_articles.xlsx, and kb_coverage.xlsx, then give me one concise report file that pulls the findings together in a way leadership can use. I want the main problem counts, the most important patterns, and a short section on anything that looks off in the source data.
```

### 166. D8_k982553_en (domain=D8, difficulty=5)

```
Use the file tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv and analyze the support-ticket mix with a strong focus on ranking and concentration: identify which ticket types, queues, priorities, languages, and tags dominate the workload, how much of total volume is captured by the top groups, and whether a Pareto-style concentration is visible. I need a compact analysis that a support ops lead could use to decide where to staff first. Please also break out any notable differences between ticket types and queues so we can tell whether the concentration is being driven by a small number of recurring issues or by broad demand across the dataset.
```

### 167. D8_k983113_en (domain=D8, difficulty=5)

```
Using the CSV file `inputs/tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv`, run a support-ticket analysis focused mainly on ranking and concentration: identify the biggest queues, priorities, languages, and issue tags by volume, then quantify how concentrated the workload is in the top groups (top-1/top-3/top-5 shares and Pareto-style concentration). Please also check whether the concentration pattern differs by ticket type and version. Use the real columns `subject`, `body`, `answer`, `type`, `queue`, `priority`, `language`, `version`, and `tag_1` through `tag_8`. I need this broken into separate workstreams so multiple analysts could work independently, and I want a concise JSON summary of the findings.
```

### 168. D8_k983533_en (domain=D8, difficulty=5)

```
Please analyze aniketg11__supportticketsclassification__all_tickets.csv for support-ticket concentration patterns and ranking. I need a compact exec summary that answers: which ticket types/categories/sub-categories/business services dominate the workload, how concentrated the volume is in the top groups, and whether urgency/impact are also concentrated in the same segments. Please use the real columns title, body, ticket_type, category, sub_category1, sub_category2, business_service, urgency, and impact. Break the work into separate tracks so they can be run independently: rank the top values and their shares for each taxonomy field; compute Pareto-style concentration for the top 3/5/10 groups; compare concentration across urgency and impact; look at the intersection of the most common ticket_type with its associated categories/sub-categories/business services; and identify any unusually skewed segments that account for a disproportionate amount of tickets. Keep it focused on ranking and concentration, and return a concise analysis_summary.json.
```

### 169. D8_k983645_zh (domain=D8, difficulty=5)

```
请分析我提供的支持工单数据集（文件：albertobircoci__support-ticket-priority-dataset-50k__Support_tickets.csv）。该数据集包含1500条工单记录，字段包括行业(industry)、公司规模(company_size)、客户层级(customer_tier)、区域(region)、产品领域(product_area)、停机时间(downtime_min)、受影响客户数(customers_affected)、优先级(priority)等。我需要你从排名与集中度的角度进行深入分析，重点关注**帕累托分布**（即少数关键组占据大部分总量）和**Top-N占比**。请分解为4-6个独立的子分析，每个子分析用不同的维度（如行业、产品领域、公司等）来衡量集中程度。最终输出一份综合摘要文件（analysis_summary.json），包含各子分析的关键发现。
```

### 170. D8_k983904_en (domain=D8, difficulty=5)

```
Using noopurbhatt__retail-ai-intelligence-knowledge-base__retail_ai_knowledge_base_100k.csv, please analyze this knowledge/support-ticket style dataset for ranking and concentration patterns. I need a compact executive readout focused on which categories, topics, regions, customer segments, source types, and AI use cases dominate the knowledge base, plus where the long tail starts. Please use the columns knowledge_id, category, topic, retail_problem, retail_insight, ai_use_case, customer_segment, merchandising_strategy, source_type, region, and tags. Break the work into independent tracks so they can be done in parallel: (1) top-N concentration by category and topic, (2) Pareto/share-of-total analysis for the most frequent groups, (3) region and source_type concentration, (4) customer_segment and ai_use_case ranking, and (5) a quick cross-tab of the most common category-topic combinations to identify repeated patterns. Keep the output practical for a knowledge ops / support-ticket analytics audience.
```

### 171. D8_k983932_en (domain=D8, difficulty=5)

```
Using abbas829__telecom-customer-churn-feature-engineering-dataset__telecom_customer_churn_feature_engineering.csv, I need a compact support-ticket and churn diagnostic focused mainly on ranking and concentration. Please analyze which customer groups generate the most support pressure and where the churn risk is most concentrated. Break it into separate tracks so different people can work independently: (1) top cities by support_tickets and their share of all tickets, (2) top customer_feedback themes by ticket volume and churn concentration, (3) contract_type concentration of churn and tickets, (4) whether the top income or bill segments account for a disproportionate share of tickets/churn, and (5) a Pareto-style view of how much of all support_tickets is generated by the top 20% of customers. Tie the findings together into a short executive summary that highlights the biggest concentration risks and the customer segments most overrepresented in support volume and churn. Use the real columns in the file: customer_id, signup_date, age, gender, city, education_level, employment_status, monthly_income, monthly_bill, internet_usage_gb, call_minutes, contract_type, support_tickets, customer_feedback, churn.
```

### 172. D8_k984058_en (domain=D8, difficulty=5)

```
Using samyakrajbayar__python-questions-faq-dataset__python_faq_dataset.csv, analyze the support-ticket / knowledge-base patterns in this dataset with an emphasis on ranking and concentration. I need a concise executive summary of which questions, topics, tags, sources, and difficulty levels dominate the corpus, how concentrated the volume is in the top groups, and whether shorter or longer posts tend to score differently. Please break the work into independent tracks so different people can work in parallel, and give me a compact JSON-ready summary with the key top-N lists, shares of total, and a Pareto-style readout.
```

### 173. D8_k984155_en (domain=D8, difficulty=5)

```
Using aniketg11__supportticketsclassification__all_tickets.csv, I need a compact but rigorous support-ticket analytics readout focused mainly on correlation and driver analysis across the numeric fields. Please break it into a few independent workstreams so different people could tackle them in parallel: first, quantify how the ticket classification fields move together with rounded correlations and identify the strongest positive/negative pairwise associations; second, check which drivers are most associated with operational severity signals like urgency and impact; third, compare averages and distributions of the numeric categories by ticket_type; fourth, look for any obvious redundancy or near-duplication among category, sub_category1, sub_category2, and business_service; and fifth, summarize any high-level patterns in text length proxies from title/body if they are useful as supporting context. I do not need charts, just a concise analysis summary with the main numeric findings, anomalies, and any practical interpretation for support-ticket triage and taxonomy quality.
```

### 174. D8_k985038_en (domain=D8, difficulty=5)

```
Using the file noopurbhatt__retail-ai-intelligence-knowledge-base__retail_ai_knowledge_base_100k.csv, do a support-ticket style knowledge-base analysis for me. Focus mainly on ranking and concentration: identify which categories, topics, regions, customer segments, source types, and AI use cases account for the most volume, how much of the dataset is concentrated in the top groups, and whether a small set of themes dominates the knowledge base. I also want a quick read on the most common retail problems and merchandising strategies so I can see where support and content effort is concentrated. Please keep it practical and summarize the findings in a way I can paste into an internal analysis note.
```

### 175. D8_k985101_en (domain=D8, difficulty=5)

```
Using the file noopurbhatt__retail-ai-intelligence-knowledge-base__retail_ai_knowledge_base_100k.csv, build a support-ticket style knowledge analytics summary focused on ranking and concentration. I need to know which categories, topics, AI use cases, customer segments, regions, and source types dominate the knowledge base, how concentrated the workload is in the top groups, and whether a small set of themes explains most of the content. Please also surface the most common retail problems and the most frequent tag patterns so I can prioritize our support taxonomy cleanup. Use the existing columns only: knowledge_id, category, topic, retail_problem, retail_insight, ai_use_case, customer_segment, merchandising_strategy, source_type, region, tags.
```

### 176. D8_k985110_en (domain=D8, difficulty=5)

```
Analyze the CSV file `thedevastator__sciq-a-dataset-for-science-question-answering__train.csv` using the columns `question`, `distractor3`, `distractor1`, `distractor2`, `correct_answer`, and `support`. I need a support-ticket style knowledge analysis that treats each row as an issue-answer record and focuses mainly on temporal/trend-style analysis over sequence position in the file (since there is no date field): look for how answer/support text characteristics change from the start of the file to the end, whether question/support length trends drift by quartile, and whether the distribution of correct answers and distractors shifts over the record order. Break this into multiple independent workstreams so different analysts can work in parallel, and return a concise summary plus any notable shifts or anomalies.
```

### 177. D9_g981580_zh (domain=D9, difficulty=5)

```
请基于 inputs/vulnerability_inventory.xlsx、inputs/sla_exceptions.csv、inputs/control_effectiveness.json 做一版安全漏洞整改 triage 结论，输出 decision_brief.md。我要看各严重度总量、SLA 逾期情况、TOP 10 紧急项，以及需要我优先点名的资产。
```

### 178. D9_k982986_zh (domain=D9, difficulty=5)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一次安全分析，重点放在“数值字段之间的相关性与驱动因素”上：先找出最强的正/负相关数值特征对，识别哪些指标成组一起变化，再看它们与连接行为/攻击迹象（如 count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate、dst_host_* 这些字段）之间的关系。请把分析拆成 4-6 条彼此独立的分析线索，便于不同子分析并行推进：1）全量数值特征相关矩阵与最强相关对；2）与核心连接/错误率字段的驱动关系；3）按 protocol_type / service / flag 分组后看相关结构是否变化；4）识别高关联特征簇和可能的冗余字段；5）找出最能区分“正常访问模式 vs 异常访问模式”的关键数值指标组合。输出时请给出可执行的结论、关键相关系数（保留两位小数）以及需要重点关注的字段对。请直接基于该 CSV 的真实数据分析，不要假设任何未给出的值。
```

### 179. D9_k983687_en (domain=D9, difficulty=5)

```
Analyze `subhajournal__iotintrusion__IoT_Intrusion.csv` for security-operations triage with a heavy focus on ranking and concentration. I need a concise but defensible readout of which attack labels dominate the dataset, how concentrated traffic volume is across the top groups, and whether a small number of patterns account for most of the observed activity. Please structure this as 4–6 independent workstreams so different analysts could handle them in parallel: (1) label-frequency ranking and Pareto concentration, (2) top-N by key traffic volume metrics such as `flow_duration`, `Duration`, `Rate`, and `Header_Length` aggregated by `label`, (3) concentration of protocol/flag indicators by label using columns like `TCP`, `UDP`, `HTTP`, `HTTPS`, `fin_flag_number`, `syn_flag_number`, `ack_flag_number`, (4) comparison of benign vs attack classes on the same ranking metrics, and (5) a compact anomaly-style summary of which labels dominate by packet/header-derived metrics versus simple row counts. I only need the final analysis packaged for decision-making, plus a small JSON summary file.
```

### 180. D9_k984015_en (domain=D9, difficulty=5)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, run a security-analytics review focused on correlation and driver analysis across the numeric fields. I need you to identify which metrics move together most strongly, round correlations to 2 decimals, and surface the top positive and negative associations that could explain intrusion patterns. Break the work into independent tracks covering: overall numeric correlation structure, highly related feature pairs, correlations between traffic-volume features and alarm/rate features, correlations involving host-based features, and a quick sanity check on the most common protocol/service/flag categories so we can contextualize the numeric drivers. Keep it grounded in the real columns in the file, and summarize findings in a compact analysis_summary.json.
```

### 181. D9_k984268_en (domain=D9, difficulty=5)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, do a security-analytics review focused on ranking and concentration. I need you to identify which protocol/service/flag combinations are carrying the bulk of traffic, how concentrated the attack classes are, and whether a small number of entities account for most of the suspicious volume. Use the real columns in the file, especially protocol_type, service, flag, class, src_bytes, dst_bytes, count, srv_count, serror_rate, rerror_rate, same_srv_rate, diff_srv_rate, dst_host_count, dst_host_srv_count, and related host-rate features. Please split the work into independent tracks so I can hand them to different analysts: one track for class concentration and Pareto shares, one for top protocol/service/flag rankings, one for byte-volume concentration, one for high-risk anomaly concentration using failure/error-rate features, and one for host-level concentration patterns. I need a concise JSON-ready summary with the biggest contributors, their shares of total, and a few deterministic checks I can verify.
```

### 182. D9_k984449_en (domain=D9, difficulty=5)

```
Using the file subhajournal__iotintrusion__IoT_Intrusion.csv, do a security-analytics review focused mainly on correlation and driver analysis. I need you to identify which numeric fields move together, surface the strongest rounded correlations, and explain which features appear most associated with label-separated behavior. Please work only from the real columns in the dataset, including flow_duration, Header_Length, Protocol Type, Duration, Rate, Srate, Drate, the TCP flag/count features, the protocol indicator columns, and the remaining numeric traffic-stat columns. Split the work into a few independent tracks so it can be handled in parallel, and return the findings in a compact analysis summary.
```

### 183. D9_k984542_en (domain=D9, difficulty=5)

```
Using subhajournal__iotintrusion__IoT_Intrusion.csv, build a security analytics brief focused mainly on distribution and threshold cohorts. I need to know how the traffic breaks down across business-relevant cutoffs for fields like Rate, Srate, Drate, flow_duration, Duration, and the flag/count columns, plus how the class mix shifts across those cohorts. Please segment the data into practical buckets, quantify above/below-threshold counts and shares, compare label composition across buckets, and call out any standout concentration patterns. Use the actual columns in the file, including label and the protocol/port indicators, and keep the output concise but decision-ready.
```

### 184. D9_k984680_en (domain=D9, difficulty=5)

```
Using subhajournal__iotintrusion__IoT_Intrusion.csv, run a security-focused correlation and driver analysis on the numeric features and label. I want to know which measurements move together, which features are most strongly associated with the attack labels, and whether any protocol/flag counters or traffic statistics appear to be the main drivers of the different intrusion families. Please keep it grounded in the real columns in the file, use rounded correlations and top associations, and summarize the findings in a way I can hand to a security analyst.
```

### 185. D9_k985060_zh (domain=D9, difficulty=5)

```
请基于文件 ujjwalchowdhury__walmartcleaned__walmart_cleaned.csv 做一份偏“安全分析”视角的分布与阈值分层分析，我主要想快速判断哪些门店/部门/时间段/环境条件更容易落入高风险销售异常区间。重点不是建模，而是做可落地的统计分层：请围绕 Weekly_Sales 的高低阈值、分位数桶、以及在不同业务条件下的占比变化来分析。数据里可用字段包括 Store、Date、IsHoliday、Dept、Weekly_Sales、Temperature、Fuel_Price、MarkDown1-5、CPI、Unemployment、Type、Size。请输出一个 analysis_summary.json，并按下面 4-6 个相互独立的分析轨道组织：1）按全样本分位数/业务阈值切分 Weekly_Sales 的分布与占比；2）按 Store 和 Type 统计高销售/低销售门店的混合占比；3）按 IsHoliday、Dept 分层看高风险阈值命中率；4）结合 Markdown 是否存在、以及 Markdown 强度分桶看销售分布变化；5）按 Temperature、Fuel_Price、CPI、Unemployment 的区间或分位数桶观察 Weekly_Sales 的阈值穿越情况；6）如有必要，再补一个日期维度（按年份或月份）的分层对比，说明异常销售是否集中在某些时间段。请全部基于真实数据计算，不要做任何预测或建模。
```

### 186. D9_k985065_en (domain=D9, difficulty=5)

```
Using the file ahmednour__website-phishing-data-set__Website Phishing.csv, do a security-analytics review focused mainly on correlation and driver analysis: identify which numeric fields move together, round correlations to 2 decimals, and highlight the strongest associations with Result. I need this broken into a few independent workstreams so different analysts can work in parallel: one track on feature-to-feature correlations across SFH, popUpWidnow, SSLfinal_State, Request_URL, URL_of_Anchor, web_traffic, URL_Length, age_of_domain, and having_IP_Address; one track on the strongest positive and negative relationships with Result; one track on how the class outcomes differ across key categorical signal levels; one track on any concentration or imbalance patterns in the predictors; and one track on basic data-quality checks such as missing values and duplicate rows. Please return a concise analysis summary suitable for a security analytics stakeholder.
```

### 187. D10_g1020_en (domain=D10, difficulty=6)

```
I need you to run a customer and market operations review using the files in ./inputs/: customers.xlsx, support_tickets.xlsx, customer_churn_snapshot.csv, campaign_performance.xlsx, and competitor_tracking.xlsx. Please produce a markdown executive summary, a JSON findings file, and a CSV table of ranked metrics covering the top complaint themes, churn risk scores, campaign ROI, competitor leader, support ticket totals and theme share, and any invalid row counts.
```

### 188. D10_g1263_en (domain=D10, difficulty=6)

```
Using the files in inputs/ – customers.csv, feedback.csv, crm_updates.csv, competitor_daily.xlsx, campaigns.xlsx, support_event_log.jsonl, ops_data.sqlite, and definitions.md – produce compact synthesis reports: a JSON summary for the leaderboard metrics and a CSV for CRM update and support log counts. Add a brief MD note if any assumptions need stating. Keep it concise.
```

### 189. D10_g980879_zh (domain=D10, difficulty=6)

```
请基于 inputs/crm_accounts.xlsx、inputs/campaign_metrics.xlsx、inputs/feedback_and_competitor.xlsx 写一份 findings.md，做成客户与市场运营的综合分析简报。我要看到跟进账号、活动回报、投诉主题、流失风险和竞品动态五块内容，并把跨文件之间不一致的地方单独说明。
```

### 190. D10_g981192_zh (domain=D10, difficulty=6)

```
请基于 inputs/customer_market_ops_source.xlsx 和 inputs/source_manifest.json 整理一份面向管理层的市场与客户运营分析简报，输出为 findings.md。
- 需要同时看评论、客户、活动和竞品四类材料，做出交叉结论，并单独写出各来源之间哪里一致、哪里有冲突。
- 请把最主要的反馈主题、最高风险客户、最佳ROI活动、以及竞品最新态势都讲清楚。
- 发现重复评论或数据异常时也要说明它们对结论有什么影响。
- 结论尽量简洁，但要有可执行建议。
```

### 191. D10_g981227_en (domain=D10, difficulty=6)

```
I need a compact findings brief for customer and market operations using the files `customer_market_ops_master.xlsx`, `campaign_spend_support.csv`, and `crm_notes.json`. Please synthesize the review themes, account-risk signals, campaign ROI, and competitor watch into one markdown brief.
- Summarize the main findings by source and call out any cross-source conflicts or mismatches.
- Include a ranked top-3 table for the riskiest customer accounts, the best ROI campaigns, and the top complaint themes.
- Flag any duplicate or missing records that affect the numbers.
- Keep it compact and decision-oriented.
```

### 192. D10_g981340_en (domain=D10, difficulty=6)

```
You are an analytics lead. Use the provided customer, campaign, feedback, and competitor inputs to produce a concise executive review.
You should inspect data quality, identify the highest-risk customers, summarize campaign performance, and interpret feedback themes.
Keep the output grounded in the data and do not invent numbers.
```

### 193. D10_g981457_zh (domain=D10, difficulty=6)

```
我需要你基于这四个输入文件做一份简短的决策文件：customer_health_ops.xlsx、support_tickets.csv、campaign_performance.json、competitor_tracker.txt。请把客户健康、工单主题、活动ROI和竞品动态合在一起，输出一个能直接给销售/市场/客户成功负责人看的单文件结论。我要你先按客户ID和活动ID去重，再分别算客户风险分、工单主题占比、活动ROI、以及竞品来源的净影响；其中客户风险分请使用 0.5*churn_prob + 0.3*(overdue_days/60) + 0.2*(ticket_count_90d/10)，活动ROI请使用 (revenue - spend) / spend，spend=0 的活动要排除。工单主题只认固定标签集合：pricing、integration、performance、bug、ux、support，其他都不要算作主题。最后请给我一个单独的决策文件，里面要有：建议优先跟进的客户 Top-3、最值得继续投放的活动 Top-3、最需要处理的主题、以及竞品里净影响最强的来源，并且用表格把分数和排序写清楚。请顺手把你发现的重复记录、空值或无法解析的竞品行也在文件里简要说明一下，但不要展开成流水账。
```

### 194. D10_g981941_zh (domain=D10, difficulty=6)

```
请基于 inputs/customer_market_ops_dataset.xlsx 和其中的真实种子记录，做一版客户与市场运营决策简报，输出为 decision_brief.md。我需要一页内能直接发给管理层的结论，重点看客户风险、活动 ROI、投诉主题和竞品态势，再给出你建议优先推进的动作。
```

### 195. D10_g981954_zh (domain=D10, difficulty=6)

```
我这边有三份材料：inputs/customer_market_ops_sources.xlsx、inputs/market_supporting_sources.xlsx 和 inputs/ops_memo.pdf。麻烦你把它们做成一份中文的分析简报，重点看客户反馈聚类、流失风险、活动ROI、竞品动态和CRM更新，最后给我一个简洁但能直接拿去开会的 findings.md。
```

### 196. D10_g981967_zh (domain=D10, difficulty=6)

```
请基于 customer_market_ops_master.xlsx、reference_mapping.json 和 ops_event_log.txt 做一版简洁的客户与市场运营汇总，把反馈主题、账户流失风险、活动ROI、竞品动态和日志里的异常一起整理成一个最终报告，并顺手把需要更新到CRM的重点对象也列成简表。
```

### 197. D10_g990_zh (domain=D10, difficulty=6)

```
我们最近在整理客户反馈、流失风险、活动效果和竞品动态，需要出一份综合简报，定位问题并给出行动建议。请基于以下五个输入文件做跨来源分析，重点指出数据矛盾、异常和可执行结论：

- inputs/customer_feedback.xlsx
- inputs/customer_health.xlsx
- inputs/campaign_performance.csv
- inputs/competitor_tracking.xlsx
- inputs/crm_snapshot.xlsx（用于核对，不单独输出全量）

希望输出一份简短的 Markdown 主文档加一个小证据表，至少从反馈主题、流失风险、活动 ROI、竞品威胁/CRM 对齐四条线索切入，最后合并。注意遵循内部标准操作文档中的统一口径（比如反馈主题分类、去重规则、指标定义、分析时间段等），我不过多重复细节。结论摘要、证据表、异常说明和行动建议都要有。
```

### 198. D10_k982301_en (domain=D10, difficulty=6)

```
Using radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv, run a customer-analytics review focused mainly on ranking and concentration: identify which customer segments and product/behavior groups account for the largest shares of churn, complaints, and customer value. I need a practical readout that highlights top-N concentration, Pareto-style shares, and the biggest drivers by geography, card type, gender, age band, product count, and activity status. Please break it into independent workstreams so different analysts can work in parallel, then summarize the main concentration patterns and any clear high-impact customer groups.
```

### 199. D10_k982853_en (domain=D10, difficulty=6)

```
Analyze the customer analytics file radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv using the real columns in the dataset, with the main focus on correlation and driver analysis: identify which numeric fields move together, round correlations, and surface the strongest associations with churn and complaints. I want a compact but rigorous analysis that also checks whether churn appears to be tied to age, balance, products, activity, tenure, credit score, estimated salary, satisfaction score, point earned, and complain behavior, while also comparing the main patterns by geography, gender, and card type where relevant. Please break it into a few independent workstreams so multiple analysts could work in parallel and then combine the findings into one concise summary.
```

### 200. D10_k982896_zh (domain=D10, difficulty=6)

```
请基于文件 blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv 做一份围绕“排名与集中度（Top-N、头部份额、Pareto）”的客户分析，重点找出：哪些客户群体、服务组合、付费方式和合同类型最集中地贡献了流失与收入；以及流失是否高度集中在少数细分群体中。请你把分析拆成可并行推进的 4-6 个独立方向，并给出一份适合业务汇报的结论框架。分析时请直接使用真实字段：Churn、MonthlyCharges、TotalCharges、Contract、PaymentMethod、InternetService、SeniorCitizen、tenure、PaperlessBilling、OnlineSecurity、TechSupport、StreamingTV、StreamingMovies、PhoneService、MultipleLines、Partner、Dependents、gender。不要编造任何数据；所有结论都必须可由数据直接复现。请特别关注：1）流失人数 Top-N 及其累计占比；2）收入贡献 Top-N 及其累计占比；3）头部客户群是否符合 80/20 现象；4）高风险群体的集中度；5）关键服务组合的排名；6）不同合同/支付方式下的流失集中情况。
```

### 201. D10_k983033_en (domain=D10, difficulty=6)

```
Analyze the file radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv for customer analytics with an emphasis on anomaly and outlier detection using explicit numeric rules. I want a compact, decision-ready summary that identifies unusual customers and unusual segments in the data using fixed thresholds, IQR-based rules, rare categories, and extreme values. Please structure the work as 5 independent tracks so they can be split across sub-agents: (1) numeric outliers in CreditScore, Age, Tenure, Balance, EstimatedSalary, and Point Earned using explicit threshold rules and IQR; (2) rare or unusual categorical patterns across Geography, Gender, and Card Type, including underrepresented combinations and whether they are overrepresented among churned customers; (3) anomaly association checks linking Complain, Exited, IsActiveMember, NumOfProducts, and HasCrCard; (4) customer-level extremity ranking that highlights the most extreme records across multiple fields; (5) segment-level anomaly profiling by Geography and Card Type, comparing churn, complaints, and extreme numeric behavior. Use only the real values in the dataset, and keep the output practical for a customer analytics team.
```

### 202. D10_k983167_zh (domain=D10, difficulty=6)

```
请基于文件 karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv（列：rating、review_content、likes、publish_time、device_model、game_name、sentiment）做一次面向客户分析的多维数据质量审计，并顺带给出最关键的业务可用性结论。请重点围绕数据质量问题展开：检查缺失值、空字符串、'?'、重复记录、异常取值/范围违规、类别字段不一致（如设备型号、游戏名、情感标签等），同时结合评分、点赞数、发布时间做基础一致性校验。这个任务请拆成 4-6 个彼此独立的分析方向，方便并行处理；最终输出一份 analysis_summary.json，里面要能直接支持后续清洗规则制定、异常来源排查和客户分析口径统一。
```

### 203. D10_k983276_zh (domain=D10, difficulty=6)

```
请基于文件 radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv 做一份面向客户分析的多阶段研究，重点围绕“时间/序列维度”的趋势分析展开。这个数据没有显式日期字段，所以请把 RowNumber 视为记录进入样本的序列顺序，按它分成前后等分或分位段，分析客户流失、投诉、活跃度、余额/信用/收入以及会员属性在序列上的变化趋势，并判断这些变化是否与流失率的上升/下降同步。请把结论组织成可给业务团队直接使用的摘要，并注明哪些结论是基于分段趋势、哪些是基于组间对比。

请至少拆成 4-6 个彼此独立的分析轨道：
1）按 RowNumber 序列分段的流失率趋势与环比/前后段变化；
2）投诉（Complain）与流失、活跃会员（IsActiveMember）的联动趋势；
3）不同 Geography、Gender、Card Type 在序列分段中的流失/投诉变化；
4）信用分、余额、估计薪资、Point Earned 等连续变量在序列上的变化及其与流失的关系；
5）产品数、持卡、满意度分数在序列上的结构变化；
6）如果能发现“异常拐点”或某一段显著抬升/下滑，请单独指出并量化。

请输出一份结构清晰、可执行的分析结果，最后附上关键指标表述和建议优先关注的客户群。
```

### 204. D10_k983386_en (domain=D10, difficulty=6)

```
Using karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv with the columns rating, review_content, likes, publish_time, device_model, game_name, and sentiment, I need a customer-analytics readout centered on ranking and concentration. Please build a practical analysis that shows where attention is concentrated: which games dominate review volume, likes, and sentiment; how much of total activity the top titles and top devices capture; whether high-like reviews are disproportionately concentrated in a few games or devices; and whether the most prominent titles differ from the most positively or negatively perceived ones. I need this split into independent workstreams so different analysts can work in parallel, and I want the output summarized in analysis_summary.json.
```

### 205. D10_k983599_en (domain=D10, difficulty=6)

```
Use karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv and build a customer analytics readout focused mainly on segment comparison across categorical groups. I need a concise but decision-oriented analysis of how review sentiment, ratings, and engagement differ by game_name, device_model, and publish_time segments, with emphasis on the biggest gaps between segments. Please split the work into 4-6 independent tracks so different analysts could work in parallel, and make sure the final output is fit for a management summary. Also include a small set of reproducible checks on the underlying data so I can verify the key segment claims.
```

### 206. D10_k983605_en (domain=D10, difficulty=6)

```
Using karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv, analyze customer sentiment and review behavior over time for mobile games. Focus mainly on temporal trends from publish_time: identify overall rating/sentiment changes by year and month, period-over-period shifts, and whether review engagement (likes) changes over time. Please also break out the analysis by game_name and device_model where useful so we can tell whether certain titles or devices have sharper trend changes or unusually positive/negative review patterns. I need this structured as a customer analytics readout with a few independent workstreams that can be handled in parallel, and I want the final output saved as analysis_summary.json.
```

### 207. D10_k983626_en (domain=D10, difficulty=6)

```
Using karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv, I need a customer-analytics readout focused mainly on temporal trends. Please analyze how review volume, ratings, likes, and sentiment change over time using publish_time, and connect those shifts to game_name and device_model where useful. I want a concise executive summary plus a few supporting slices that help explain whether certain games or devices are driving changes in satisfaction. If there are obvious period-over-period changes or spikes, call them out and quantify them. Please structure the work so different analysts could handle separate pieces in parallel, but make sure the final output is one cohesive memo.
```

### 208. D10_k983775_zh (domain=D10, difficulty=6)

```
请基于文件 blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv 做一份面向客户分析的异常/离群点审计，重点围绕显式数值规则来找出可疑记录：例如 tenure 的极低/极高值、MonthlyCharges 的极端值、TotalCharges 的异常空值或非数值、以及按类别字段定义的稀有组合。请先把数据按可执行规则拆成 4-6 个相互独立的分析轨道，分别覆盖：1）数值型异常阈值与分位数/IQR 离群；2）TotalCharges 的类型清洗、缺失/空白/非数值检查与极端值；3）稀有类别与罕见组合（如 PaymentMethod、Contract、InternetService 等）识别；4）异常客户画像与 Churn 关系；5）可能的数据录入异常或不一致规则（如 PhoneService 与 MultipleLines、InternetService 与增值服务逻辑冲突）。最后输出一份可供业务讨论的 analysis_summary.json，明确列出每类异常的数量、占比、Top 可疑规则以及最值得人工复核的客户分组。请基于真实列名：customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn。不要编造任何值，只用数据本身做统计。
```

### 209. D10_k983780_en (domain=D10, difficulty=6)

```
Using radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv, build a customer-analytics review focused mainly on temporal / trend analysis over any sequence-style fields available in the data (for example, compare change patterns across tenure bands and other ordered segments, and quantify period-over-period style differences where possible). I need a practical analysis that ties churn behavior to customer profile, product usage, and engagement, and I want it split into independent workstreams so different analysts can work in parallel. Please produce a concise analysis summary plus a few deterministic validation checks on the raw data using the real columns: RowNumber, CustomerId, Surname, CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Exited, Complain, Satisfaction Score, Card Type, and Point Earned.
```

### 210. D10_k983793_zh (domain=D10, difficulty=6)

```
请基于文件 blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv 里的真实客户流失数据做一份面向客户分析的阈值分布报告，重点围绕“分布与阈值 cohort（高/低阈值人数、分位数分桶、占比结构）”展开。请直接读取并使用这些真实字段：customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn。我要你把分析拆成几个彼此独立的部分，分别回答：1）客户基本规模与流失基线；2）tenure、MonthlyCharges、TotalCharges 的阈值 cohort 与分位数分桶分布；3）不同 Contract、InternetService、PaymentMethod 的结构占比与高风险阈值人群占比；4）Churn 在不同阈值 cohort 中的差异；5）关键字段的缺失/异常处理检查（尤其是 TotalCharges）；6）输出一个可直接给业务看的总结，突出哪些阈值下的人群规模最大、流失最集中、以及各类客户结构占比差异。请只基于数据本身，不要编造任何数字。
```

### 211. D10_k983850_zh (domain=D10, difficulty=6)

```
请基于文件 blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv 做一份客户流失分析，重点围绕“时间/序列趋势”来展开：把 tenure 视为客户生命周期序列，分析不同生命周期阶段的流失率变化、流失前后的费用结构变化，以及关键服务/合约/支付方式在生命周期中的趋势差异。请你把结果整理成一份可直接给业务团队看的分析摘要，并输出 analysis_summary.json。字段里要重点用到 customerID、tenure、MonthlyCharges、TotalCharges、Churn，以及 Contract、InternetService、PaymentMethod、TechSupport、OnlineSecurity、PaperlessBilling、SeniorCitizen、Partner、Dependents 等。希望输出不仅有总体结论，还要拆成几个相互独立的分析模块，便于分给不同子任务并行完成。每个模块都要给出明确的业务问题、关键发现、以及能支持决策的数值结果。
```

### 212. D10_k983976_zh (domain=D10, difficulty=6)

```
我需要你对这份客户流失数据集进行时间趋势分析。数据文件是 'blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv'，包含客户ID、性别、是否老年人、配偶、家属、在网月数(tenure)、电话服务、多线路、互联网服务、在线安全、在线备份、设备保护、技术支持、流媒体电视、流媒体电影、合同类型、电子账单、支付方式、月费、总费用、是否流失(Churn)等字段。主要分析角度是随时间的变化趋势（比如按在网月数分组的流失率变化、不同合同类型/支付方式下的流失率趋势等）。请设计一个复杂的多部分分析任务，分解为4-6个独立的分析方向，每个方向可以独立执行。最终输出一个分析摘要JSON文件。
```

### 213. D10_k984016_zh (domain=D10, difficulty=6)

```
请基于文件 karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv 做一份面向客户分析的多维诊断，重点围绕“排名与集中度”展开：先看哪些游戏、哪些评分、哪些设备型号、哪些时间段贡献了最多评论量，以及这些头部群体对总量的占比是否高度集中。请结合真实字段 rating、review_content、likes、publish_time、device_model、game_name、sentiment 做分析，不要改动任何原始值。希望你把结果拆成多个相互独立的分析轨道，适合并行执行，并最终汇总成 analysis_summary.json。请重点回答：1）评论量排名前列的游戏和它们的集中度；2）点赞数在游戏之间的集中度及头部贡献；3）评分分布的头部集中情况；4）不同设备型号的评论集中度；5）按发布时间拆分后的头部时段集中度；6）情感标签与头部游戏/头部评分的关系。请给出可直接复核的定量结论。
```

### 214. D10_k984140_en (domain=D10, difficulty=6)

```
Using radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv, run a customer-analytics data-quality audit first and then summarize what it means for churn analysis. I need you to inspect missing values and blank/'?' entries, duplicated records and duplicated CustomerId values, impossible or suspicious values in numeric fields like CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Exited, Complain, Satisfaction Score, and Point Earned, plus category consistency for Geography, Gender, and Card Type. After that, compare churn rates across valid customer segments and flag any data-quality issues that could bias those segment comparisons. Please organize the work so multiple independent threads can run in parallel and end with a concise analysis_summary.json.
```

### 215. D10_k984387_zh (domain=D10, difficulty=6)

```
请基于文件 blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv 做一份面向客户分析的深度诊断，重点围绕“排名与集中度”展开：找出流失客户与全量客户在关键维度上的Top-N构成、头部集中度、以及是否存在明显的帕累托现象。请重点分析这些真实字段：Churn、Contract、PaymentMethod、InternetService、tenure、MonthlyCharges、TotalCharges、SeniorCitizen、Partner、Dependents、PaperlessBilling、PhoneService、MultipleLines、OnlineSecurity、TechSupport、StreamingTV、StreamingMovies。我要的不是泛泛描述，而是能直接支持运营动作的结论：哪些头部类别贡献了最多流失、哪些组合群体占据了流失的大头、以及流失是否集中在少数高风险细分上。请把分析拆成多个彼此独立的轨道，方便并行推进，最后输出一份可执行的摘要文件 analysis_summary.json。
```

### 216. D10_k984470_zh (domain=D10, difficulty=6)

```
请基于文件 radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv 做一份面向客户分析的多部分分析，重点放在“相关性与驱动因素分析”：请围绕数值字段之间哪些变量一起变化、哪些变量与流失更相关、以及主要关联的强弱（相关系数保留两位小数）来展开。请结合真实列名（如 CreditScore、Age、Tenure、Balance、NumOfProducts、HasCrCard、IsActiveMember、EstimatedSalary、Exited、Complain、Satisfaction Score、Point Earned 等），不要改动数据。希望你把工作拆成几个相互独立的分析轨道，最后汇总成一份适合业务阅读的结论稿，最好能明确指出最值得优先关注的驱动因子，以及在不同客户分层下这些关系是否一致。
```

### 217. D10_k984473_en (domain=D10, difficulty=6)

```
Using radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv, build a customer analytics deep-dive centered on temporal / trend analysis. Treat RowNumber as the sequence index and analyze how churn, complaints, satisfaction, and customer value signals evolve across the sequence. I need a concise executive summary plus an analysis_summary.json output that covers the main drivers and any period-over-period shifts. Break this into independent tracks so they can be worked on in parallel: 1) churn trend over RowNumber buckets and change over time, 2) complaint and satisfaction trend over RowNumber buckets, 3) product / card / activity mix changes over the sequence, 4) geography and gender churn trend comparisons, and 5) age, balance, and credit score trend associations with churn over the sequence.
```

### 218. D10_k984547_en (domain=D10, difficulty=6)

```
Use the file karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv and analyze this TapTap customer review data with a focus on correlation & driver analysis. I need a concise but rigorous customer-analytics readout on which numeric fields move together and what the strongest associations are, using the actual columns rating, likes, sentiment, publish_time, device_model, game_name, and review_content only as context where needed. Break the work into 4-6 independent tracks so different analysts can work in parallel: quantify the relationship between rating, sentiment, and likes; identify the strongest positive and negative correlations among numeric fields; segment correlation patterns by game_name; compare likes/rating/sentiment behavior across review volumes or time slices; and flag any notable concentration or outlier patterns that may explain the strongest associations. Please return the findings in analysis_summary.json.
```

### 219. D10_k984597_zh (domain=D10, difficulty=6)

```
请基于文件 blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv 做一份面向客户分析的多维数据分析，重点围绕“排名与集中度”来展开：找出流失客户与留存客户在不同维度上的Top-N贡献、前几类客户/产品/支付方式是否集中贡献了大部分流失、以及这些集中群体的画像差异。请把分析拆成 4-6 个彼此独立的分析轨道，便于并行推进；每个轨道都要能输出可直接用于管理层讨论的结论。分析中请明确使用真实列名，例如 Churn、Contract、InternetService、PaymentMethod、tenure、MonthlyCharges、TotalCharges、SeniorCitizen、PaperlessBilling、Partner、Dependents、OnlineSecurity、TechSupport 等。最终请汇总成 analysis_summary.json，并给出基于排名、占比、累计占比/帕累托的结论。
```

### 220. D10_k984774_zh (domain=D10, difficulty=6)

```
请帮我基于文件 ruchi798__student-feedback-survey-responses__student_feedback.csv 做一份面向客户分析场景的深度分析，重点看“反馈随学生序号/记录顺序变化的趋势”，把学生反馈当作一组客户体验评分来解读。数据里有这些字段：Unnamed: 0、Student ID，以及 7 个评分题目：Well versed with the subject、Explains concepts in an understandable way、Use of presentations、Degree of difficulty of assignments、Solves doubts willingly、Structuring of the course、Provides support for students going above and beyond、Course recommendation based on relevance。请按记录顺序（用 Unnamed: 0 作为序列索引）分析评分是否存在前后期变化、哪些维度在后半段明显改善或恶化、各评分项与课程推荐意愿的相关性是否在不同阶段发生变化，并输出一个可供业务汇报使用的结论摘要。希望你把任务拆成 4-6 个彼此独立的分析轨道，适合分给多个子分析 agent 并行处理。最终请给我一份 analysis_summary.json。
```

### 221. D10_k984903_zh (domain=D10, difficulty=6)

```
请基于文件 blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv 做一份面向客户分析的数据质量审计，重点先查清这份 Telco Customer Churn 数据是否能直接用于后续流失分析。请围绕以下核心问题展开：1）缺失值、空字符串、'?'、空白字符等异常值在 customerID、gender、SeniorCitizen、Partner、Dependents、tenure、PhoneService、MultipleLines、InternetService、OnlineSecurity、OnlineBackup、DeviceProtection、TechSupport、StreamingTV、StreamingMovies、Contract、PaperlessBilling、PaymentMethod、MonthlyCharges、TotalCharges、Churn 中分别有多少；2）是否存在重复 customerID 或重复整行记录；3）数值字段 SeniorCitizen、tenure、MonthlyCharges、TotalCharges 是否有范围异常或类型异常；4）类别字段是否存在不在预期集合内的脏值，特别是诸如 No internet service、No phone service、Yes/No 组合是否与上游字段一致；5）TotalCharges 的可转换性与空值分布是否会影响建模样本量；6）在完成清洗前，先给我一个能指导后续客户流失分析的质量结论和优先修复清单。请把结果整理成一个可直接交给团队执行的审计输出。
```

### 222. D10_k984946_en (domain=D10, difficulty=6)

```
Using meetnagadia__hotel-reviews__Datafiniti_Hotel_Reviews_Jun19.csv, please run a customer analytics deep-dive focused mainly on correlation and driver analysis across the numeric review fields. I want a practical readout of which variables move together, where the strongest associations are, and whether sentiment-like review patterns differ by geography, brand, or time. Please keep it grounded in the real columns available in this file, especially reviews.rating, latitude, longitude, and any date fields that can be safely parsed. Break the work into a few independent tracks so it can be handled in parallel: (1) data quality and usable sample sizing for the correlation work, (2) numeric correlation scan and top pairwise associations, (3) rating drivers by geography and city-level context, (4) time-based shifts in ratings and review volume, and (5) hotel-level concentration / outlier patterns where unusually high or low average ratings may signal distinct customer experiences. Use only deterministic calculations and summarize the results in a compact analysis_summary.json.
```

### 223. D10_k985019_en (domain=D10, difficulty=6)

```
Use the dataset in `alfathterry__telco-customer-churn-11-1-3__telco.csv` to build a customer analytics readout focused mainly on temporal / trend analysis. I need a compact but rigorous investigation of how customer status and value evolve across the sequence fields we do have, especially `Tenure in Months` and `Quarter`, and how churn-related outcomes differ over time. Please break it into 4-6 independent workstreams so a small sub-agent team can work in parallel. At minimum, cover: churn/retention trends by tenure band and quarter; how key revenue and usage metrics change across tenure; whether referrals and contract type alter churn timing; and any time-ordered differences in satisfaction and churn reasons. Use the real columns in the file, including `Customer Status`, `Churn Label`, `Churn Score`, `Satisfaction Score`, `Total Revenue`, `Monthly Charge`, `Tenure in Months`, `Quarter`, `Number of Referrals`, `Contract`, `Internet Type`, and `Churn Reason`. Deliver the output as a concise JSON summary with the main findings and any notable period-over-period changes.
```

### 224. D10_r1_en (domain=D10, difficulty=6)

```
I have a customer dataset 'adult_census_income.csv' with 1500 rows and columns: age, workclass, fnlwgt, education, education.num, marital.status, occupation, relationship, race, sex, capital.gain, capital.loss, hours.per.week, native.country, income. I need a comprehensive analysis to understand income drivers and customer segments. Please break this into independent sub-analyses: (1) income distribution by demographics, (2) work patterns and capital effects, (3) missing data assessment, (4) correlations and top categories, (5) education and occupation insights, (6) marital status and relationship effects. Provide a summary JSON with key findings from each track.
```

### 225. D11_g981637_en (domain=D11, difficulty=6)

```
I need a finance and business ops analysis using the files in inputs/:
  budget_variance.xlsx    (budget vs actual by cost center and category)
  expense_exceptions.xlsx (expense issues with types and amounts)
  event_memo.pdf          (market commentary that may explain variances)

Please do the following in a single findings.md:
- Compute total budget, actual, and variance; report material variances (abs >= $10k or >=15% of budget).
- Count exception types, identify duplicate exceptions, and flag any exception >= $10k.
- List the top 3 exceptions by amount.
- Compare variance signs with memo sentiment for TSLA, OFIX, IBIO; note any conflicts.
- Keep tables compact (under 40 rows). No per-transaction dumps.
```

### 226. D11_g982211_zh (domain=D11, difficulty=6)

```
这次月度关账我需要一份简洁但完整的分析稿，帮助我把预算波动和费用异常一起看清楚，避免我们在管理层例会上被追问。请基于 inputs/budget_spend_review.xlsx 和 inputs/exceptions_audit.xlsx 整理成一份 findings.md，重点写出两份材料之间能互相印证或互相冲突的地方。
```

### 227. D11_g983646_en (domain=D11, difficulty=6)

```
You are reviewing a finance close package with three source files: a spend variance ledger, an invoice/expense exceptions register, and a long finance close memo. Analyze the inputs and produce a concise but evidence-backed close review.
```

### 228. D11_k982605_zh (domain=D11, difficulty=6)

```
请基于文件 yasserh__loan-default-dataset__Loan_Default.csv 做一份面向信贷审批和风险管理的分群对比分析，重点围绕不同细分群体之间的指标均值/比例差异、以及“最大差距”在哪里。请直接使用现有字段（例如 year、loan_limit、Gender、approv_in_adv、loan_type、loan_purpose、Credit_Worthiness、open_credit、business_or_commercial、loan_amount、rate_of_interest、Interest_rate_spread、Upfront_charges、term、Neg_ammortization、interest_only、lump_sum_payment、property_value、construction_type、occupancy_type、Secured_by、total_units、income、credit_type、Credit_Score、co-applicant_credit_type、age、submission_of_application、LTV、Region、Security_Type、Status、dtir1），不要编造任何值。请按 4-6 条彼此独立的分析线并行展开：一条做按分类变量分组的违约率/样本量对比，一条做利率与 LTV 等连续指标在群体间的均值对比，一条找出不同分组下风险差异最大的类别组合，一条检查缺失值是否在不同群体中集中，一条看年龄段/性别/地区的交叉差异，必要时再补充一条对“审批前置/贷款类型/用途”相关分群的对比。最后请输出可直接用于汇报的结论摘要，指出最值得关注的 3-5 个细分群体差距，以及这些差距可能对应的业务含义。
```

### 229. D11_k982944_zh (domain=D11, difficulty=6)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向信贷风控/贷款组合的相关性与驱动因素分析，重点看哪些数值字段彼此一起变化、哪些变量与坏账/是否未按时结清最相关。请把结果分成几个彼此独立的分析轨道并分别给出结论：1）全量数值字段的相关矩阵与强相关对（按绝对相关系数排序，保留两位小数）；2）围绕 not.fully.paid 的驱动因素分析，找出与其正负相关最强的数值变量，并结合 credit.policy、fico、int.rate、inq.last.6mths、revol.util 等解释风险画像；3）按 purpose 分组比较核心数值指标（如 int.rate、installment、dti、fico、revol.bal、revol.util）与 not.fully.paid 的差异，识别最风险的用途类别；4）检查信用行为相关变量之间的联动（如 fico、int.rate、installment、dti、days.with.cr.line、revol.bal、revol.util、inq.last.6mths），确认是否存在明显的“高负债/高循环利用/高查询次数”组合；5）做分层对比：credit.policy=0 vs 1、not.fully.paid=0 vs 1 的均值/中位数差异，找出最能区分样本的指标；6）输出一个可供业务汇报的简洁结论清单，说明哪些变量是高相关、哪些是主要风险驱动、哪些业务用途更需要关注。请严格基于真实数据，不要编造任何数值。
```

### 230. D11_k982954_zh (domain=D11, difficulty=6)

```
请基于文件 itssuru__loan-data__loan_data.csv（字段包括 credit.policy、purpose、int.rate、installment、log.annual.inc、dti、fico、days.with.cr.line、revol.bal、revol.util、inq.last.6mths、delinq.2yrs、pub.rec、not.fully.paid），帮我做一份面向信贷风控的多部分分析，重点围绕“序列/趋势变化”展开。虽然数据里没有显式日期字段，但请把 int.rate、fico、inq.last.6mths、delinq.2yrs、days.with.cr.line、revol.util 等视为可排序的序列维度，分析不同区间、分位段或递进层级上的坏账率、违约风险、负债压力和信用表现的变化趋势。我要你把结果拆成 4-6 个彼此独立的分析轨道，方便分给不同子代理并行完成。请输出可直接用于管理层汇报的结论结构，并在每个轨道里都尽量回答：趋势是否单调、拐点在哪里、哪些分组风险显著更高、以及这些风险变化在不同 purpose 下是否一致。最后请给我一个结构化的 summary JSON，便于后续自动入库。
```

### 231. D11_k983190_en (domain=D11, difficulty=6)

```
Analyze the loan_data.csv file for a finance analytics review focused mainly on ranking and concentration. I need you to quantify where the portfolio is concentrated by loan purpose, risk status, and a few key borrower/risk attributes. Please break it into independent workstreams so multiple analysts could work in parallel: (1) portfolio concentration by purpose using counts and share of total, including top-N and Pareto-style share of the top categories; (2) concentration of delinquency/default risk using not.fully.paid and credit.policy across purpose and fico bands; (3) concentration of exposure by high-balance / high-installment loans, including which segments hold the largest share of total revol.bal and installment dollars; (4) identify the most concentrated borrower-risk profiles using combinations like purpose + credit.policy + not.fully.paid; (5) assess how concentrated the loan book is across fico deciles or score bands; and (6) provide a concise summary of the most dominant groups and their shares so I can brief leadership. Use the real columns in the file, keep the analysis deterministic, and return the results in analysis_summary.json.
```

### 232. D11_k983268_zh (domain=D11, difficulty=6)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向信贷风控和资产定价的分布与阈值分层分析，重点围绕“业务阈值上下的客户数量、分位数组、以及各客群结构占比”来展开。请直接使用这些真实字段：credit.policy、purpose、int.rate、installment、log.annual.inc、dti、fico、days.with.cr.line、revol.bal、revol.util、inq.last.6mths、delinq.2yrs、pub.rec、not.fully.paid。我要你把结果整理成可交付给管理层的结论，尤其要回答：1）在常见风控阈值下，样本如何分层；2）不同 purpose 的组合结构在高风险/低风险人群中的占比如何；3）核心连续变量的分位数切分后，各桶的坏账率和样本占比分别是多少；4）哪些阈值附近存在明显的客户集中或风险跳变；5）这些阈值分层在 credit.policy、fico、int.rate、dti、inq.last.6mths 等维度上有什么差异。请按多个独立分析轨道并行完成，最终输出一份适合汇总成 analysis_summary.json 的结论草稿。
```

### 233. D11_k983359_en (domain=D11, difficulty=6)

```
Using yasserh__loan-default-dataset__Loan_Default.csv, build a finance analytics memo focused mainly on distribution and threshold cohorts. I want a compact but thorough readout of how the loan book is distributed across key business cutoffs and bucketed segments, with mix shares and default incidence by cohort. Please break this into independent workstreams so different analysts can work in parallel: (1) loan amount distribution by quantile buckets and how default status differs across those buckets, (2) LTV threshold analysis using business cutoffs such as above/below 80% and 90% plus quantile buckets, (3) income and debt-ratio style segmentation using income and dtir1 thresholds/buckets, (4) credit quality segmentation using Credit_Score cohorts and business threshold levels, (5) product/structure mix shares across loan_type, loan_purpose, loan_limit, and occupancy_type, and (6) a quick missing-data and data-quality check focused on fields needed for these cohort analyses. Please keep the output decision-oriented and suitable for a finance stakeholder.
```

### 234. D11_k984393_en (domain=D11, difficulty=6)

```
Using yasserh__loan-default-dataset__Loan_Default.csv, run a finance-focused driver and correlation analysis on the real loan dataset. Please center the work on which numeric fields move together and which variables are most associated with loan default/status, using rounded correlations and top associations. I also want you to split the work into independent tracks so multiple analysts can work in parallel: one track on numeric correlation structure among loan_amount, rate_of_interest, Interest_rate_spread, Upfront_charges, term, property_value, income, Credit_Score, LTV, and dtir1; one track on how Status differs across key loan and borrower segments; one track on missingness patterns in the numeric fields that affect the correlation readout; one track on the strongest pairwise relationships by absolute correlation; and one track on a concise business interpretation of the strongest drivers by group. Keep it strictly data-driven from the file, and make sure any reported correlations are rounded to 2 decimals.
```

### 235. D11_k984442_zh (domain=D11, difficulty=6)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向金融风控/信贷分析的深度排查，重点围绕“数值变量之间的相关性与驱动因素”展开：先把 credit.policy、int.rate、installment、log.annual.inc、dti、fico、days.with.cr.line、revol.bal、revol.util、inq.last.6mths、delinq.2yrs、pub.rec、not.fully.paid 这些字段之间的整体相关结构梳理清楚，找出最强的正/负相关组合，并进一步比较不同 purpose 下关键变量的差异、已违约与未违约人群的特征差别、以及信用评分 fico 与其他指标的联动关系。请输出一份适合给业务负责人看的结论摘要，并把可复核的统计结果整理成 analysis_summary.json。整个分析建议拆成 4-6 条互相独立的子任务并行完成，避免互相依赖。注意不要做建模预测，只做描述性统计、分组对比和相关性分析。
```

### 236. D11_k984576_en (domain=D11, difficulty=6)

```
Using the file itssuru__loan-data__loan_data.csv, build a finance analytics memo focused on ranking and concentration in the loan portfolio. I need you to identify which loan purposes dominate the book, how concentrated risk is in the top groups, and whether the highest-risk segments are disproportionately represented among defaults. Please break the work into 4-6 independent tracks so different analysts can work in parallel: (1) portfolio mix and Pareto concentration by purpose, (2) default concentration and non-performing exposure by purpose, (3) loan-size and balance concentration among the largest-value loans, (4) credit quality/risk concentration using fico, int.rate, and dti buckets, (5) whether concentration differs between credit.policy-approved vs not-approved loans, and (6) any operational red flags from inq.last.6mths, delinq.2yrs, and pub.rec among the top-risk segments. Keep it grounded strictly in the actual columns in the dataset and summarize only with deterministic counts, shares, and ranked aggregates.
```

### 237. D11_k984671_en (domain=D11, difficulty=6)

```
Using yasserh__loan-default-dataset__Loan_Default.csv, build a finance analytics review focused mainly on anomaly and outlier detection using explicit numeric rules. I want you to scan the real columns in the file — especially loan_amount, rate_of_interest, Interest_rate_spread, Upfront_charges, term, property_value, income, Credit_Score, LTV, dtir1, and Status — and identify suspicious records, rare categorical combinations, and extreme values. Please structure it as a compact analyst handoff with independent workstreams for: numeric threshold/IQR anomaly rules, category rarity and unusual combinations, missingness patterns tied to anomalous rows, default-status enrichment of flagged loans, and a brief risk segmentation by year/region/security type. Keep it practical for a lending/risk team and make the anomaly logic explicit and reproducible.
```

### 238. D11_k985034_en (domain=D11, difficulty=6)

```
Using the file `stefanoleone992__european-funds-dataset-from-morningstar__Morningstar - European Mutual Funds.csv`, analyze how European mutual funds differ across categorical segments, with the main focus on segment comparison across groups: compare means/rates by category, equity_style, equity_size, dividend_frequency, and analyst_rating, and quantify the biggest gaps between segments for key metrics like risk_rating, performance_rating, ongoing_cost, fund_size, sustainability_score, and trailing returns. Please also flag any segments with unusually high missingness in important fields, and summarize the most concentrated segment patterns in holdings and exposures where relevant.
```

### 239. D11_k985494_en (domain=D11, difficulty=6)

```
Using mhassansaboor__intel-stock-data-1980-2024__data.csv and the real columns Date, Open, High, Low, Close, Volume, Dividends, and Stock Splits, build a finance analytics memo focused mainly on distribution and threshold cohorts. I want you to break the work into independent tracks so it can be handled in parallel: (1) count how often Intel’s Close falls into business-relevant price bands and quantile buckets, (2) measure the mix share of days above/below key Close and Volume thresholds, (3) compare threshold cohorts across time periods and by calendar month, (4) summarize the tail behavior of daily returns and where the biggest moves sit relative to the threshold buckets, and (5) check whether corporate action days (Dividends or Stock Splits) cluster in any particular Close/Volume cohorts. Keep it strictly data-driven from the file; no forecasting, no charts, and no invented values.
```

### 240. D12_g383_en (domain=D12, difficulty=6)

```
I need you to use the files in inputs/ to put together three compact summary files for HR leadership: interview_and_calibration_summary.json, skills_and_onboarding_summary.csv, and reconciliation_overview.md. The goal is to synthesize interview scorecards, performance calibration, skills matrix, and onboarding gaps into a cross‑source summary. Keep everything aggregate – rates, counts, top discrepancies, and a few example IDs – no row‑by‑row tables.
```

### 241. D12_g52_zh (domain=D12, difficulty=6)

```
我需要你基于 `inputs/talent_pool.csv`、`inputs/onboarding.xlsx` 和 `inputs/calibration.xlsx` 做一份人力与培训启用（People, Training & Enablement）跨源分析简报。这是一项需要并行推进的综合性研究任务，请分别独立分析候选人转化链路、入职培训缺口、绩效校准与技能矩阵、以及跨源一致性问题，最后合并成一份统一简报。

输出只要 1–2 个紧凑的汇总交付物，不要逐行候选人→员工映射表或超过 100 行的明细。推荐交付为 `findings.md`（中文简报）和 `evidence_summary.csv`（小型证据表）。简报中必须明确写出跨源 reconcile / conflict 的结论，并单独列出异常或冲突样本的少量 ID 清单。

请在简报中包含以下分析结论（顺序你可以自行调整，但每项都必须在最终交付物中能被定位到）：

- 去重后的候选人总数、发 offer 数、最终入职数。
- 最终入职候选人在 onboarding 文件中能找到对应记录的匹配率，以及未匹配的数量。
- onboarding 文件中的“孤儿”记录数量（即未在 talent_pool 中关联到任何入职候选人的记录），并列出前 5 个 candidate_id。
- 去重后候选人的平均 interview_score。
- 未完成 onboarding 的前 3 类缺口原因及其数量。
- calibration 文件的有效记录数、无效记录数，以及有效记录中 calibrated_rating >= 4 的数量。
- 有效 calibration 记录中平均 leadership skill 最低的 role 及其均值。
- 最终入职但在 onboarding 文件中完全找不到记录的候选人数，并列出前 5 个 candidate_id。

所有比例请注明计算口径，所有平均值请注明四舍五入规则。使用自然中文表达结论，必要时附上很小的证据表或汇总表，但不要展开到逐行明细。
```

### 242. D12_g981013_zh (domain=D12, difficulty=6)

```
请基于 people_master_and_calibration_inputs.xlsx、interview_scorecards.xlsx、onboarding_skills_matrix.xlsx 输出一份决策简报，给我一个清晰的优先级排序：在“招聘评分校准、绩效校准、技能矩阵补强、入职补漏”四个动作里，哪个最该先做，哪个可以后置。简报里要同时给出各自的关键汇总数字、跨文件对账结果、以及你认为最值得关注的少数异常 ID。文件只要一份，内容要短，但结论必须有数据支撑。
```

### 243. D12_g981025_zh (domain=D12, difficulty=6)

```
请基于 inputs/people_training_enablement_master.xlsx、inputs/calibration_event_log.jsonl 和 inputs/performance_calibration_summary.xlsx 做一份决策简报，判断本季度应优先推进哪条改进主线：面试评分标准化、技能矩阵补齐、还是入职与绩效校准联动。我只需要一个简洁的决策文件，里面要有排名、关键依据数字、以及你建议先做什么。
```

### 244. D12_g981239_zh (domain=D12, difficulty=6)

```
我需要你把这三份文件——candidate_interview_scorecards.xlsx、performance_calibration_skills.xlsx、onboarding_gaps.xlsx——合成一份简短的决策简报，帮我判断下一轮培训资源优先投给哪一类人群。重点看候选人到入职员工的衔接、绩效校准、技能缺口和上岗训练完成情况，把最关键的对比结论、排名和少量需要我盯住的异常点写清楚就行。
```

### 245. D12_g981399_zh (domain=D12, difficulty=6)

```
请基于 candidate_interview_matrix.xlsx、performance_calibration.csv 和 onboarding_skills_matrix.csv 做一次人力与培训数据的交叉校准判断，重点看候选人面试到校准、入职技能覆盖、以及真实样本记录的完整性。我要一份简明的决策稿，把最重要的匹配率、缺口数量、Top 问题和最终建议放在同一个文件里，方便我直接拿去给用人经理和 HRBP 讨论。
```

### 246. D12_g981565_zh (domain=D12, difficulty=6)

```
请基于 people_training_enablement_sources.xlsx 和同目录里的两个补充文件，做一份面向 People/Training & Enablement 的综合分析简报，重点看招聘评估、绩效校准、技能矩阵和入职覆盖四块内容的交叉结论。
- 需要输出一份精简但完整的 findings.md，按主题分成 3-4 个互相独立的分析部分。
- 每个部分都要给出聚合结果：比例、数量、Top-N 失配原因或重点名单，不要展开成逐行明细。
- 要明确写出跨来源对账/冲突点，比如哪些员工在不同表里缺失、哪些评估与技能缺口不一致、哪些校准管理者问题更集中。
- 额外标出少量需要关注的员工或管理者 ID，但总量保持紧凑。
```

### 247. D12_g981777_en (domain=D12, difficulty=6)

```
You are given several input files containing resume/job-match examples, census-style records, and job-description annotation records. Your task is to analyze the inputs and produce a concise data-quality and labeling audit. Focus on identifying patterns, counts, and simple consistency checks.
```

### 248. D12_g982146_en (domain=D12, difficulty=6)

```
Review inputs/interview_scorecards.xlsx, inputs/calibration_skills_matrix.xlsx, and inputs/onboarding_gaps.xlsx, then produce one compact decision brief that ranks the main people-and-enablement risks and the best action to take. Keep it short, cite the key numbers, and include a concise reconciliation of the interview, calibration, skills, and onboarding findings.
```

### 249. D12_g982227_en (domain=D12, difficulty=6)

```
You are reviewing HR recruiting and talent data for a retail services organization. Using the provided files in inputs/, analyze the interview scorecards, performance calibration, skills/onboarding matrix, ATS roster, and seed notes. Focus on data quality, duplicates, mismatched identifiers, and hiring/performance patterns.

Deliverables:
1) Compute the key aggregate findings and data-quality issues.
2) Provide a concise reconciliation summary across candidate_id and employee_id.
3) Recommend the highest-priority cleanup steps and any notable exceptions.

Tool target: produce a structured analysis of the supplied files, not a narrative only.

Sub-analyses hint: check missing values, duplicate records, hire recommendation rates, average interview scores by department, calibration distribution, onboarding completion gaps, and identifier overlaps between datasets.
```

### 250. D12_g982274_zh (domain=D12, difficulty=6)

```
我需要你帮我分析一份人力资源多源数据，数据文件是 inputs/people_training_data.xlsx，里面有5个sheet：Seeds（原始种子数据）、Interview_Scorecards（面试评分卡）、Performance_Calibration（绩效校准）、Skills_Matrix（技能矩阵）、Onboarding_Gaps（入职缺口）。请你综合这些数据，生成一份分析简报 findings.md，重点包括以下方面的汇总：

1. **面试评分卡分析**：统计面试官的评分模式，找出异常（如给全5分的面试官、候选人所有维度评分完全相同的情况、个别候选人的总体分与维度均值明显不符）。请给出关键计数和比率。
2. **绩效校准分析**：比较初始评分和校准后评分，找出差异过大的员工（例如差≥3分），并且检查是否有经理的校准评分异常统一。提供汇总。
3. **技能矩阵分析**：计算每个技能的平均缺口（Gap = Required - Proficiency），列出缺口最大的前几个技能。同时检查数据是否有不合理之处（如Required为0、Proficiency超出1-5范围）。
4. **入职缺口分析**：按模块统计完成率，识别哪些员工有多个模块未完成（尤其是全部未完成的情况）。定义逾期逻辑（状态为Overdue或未完成且日期为空）。
5. **跨源对账**：将面试评分卡中的候选人ID与绩效校准中的员工ID进行匹配，统计匹配率。对于匹配的员工，比较面试总体评分与绩效校准评分，找出差异最大的前几个案例。

最终简报要包含每个部分的聚合摘要（计数、比率、Top-N），不要输出原始数据表。公式和具体阈值你们那边有标准定义，我不细说了。请输出一个 findings.md 文件。
```

### 251. D12_k982610_zh (domain=D12, difficulty=6)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv（已加载为 df）做一份面向管理层的人力流失分析，重点围绕“分布与阈值 cohort”来展开：先把员工按关键业务阈值切成高低两档/多档，再看各 cohort 的人数、流失率、占比、以及与核心人群特征的组合分布。请重点使用这些真实列：Attrition、Age、MonthlyIncome、TotalWorkingYears、DistanceFromHome、OverTime、JobLevel、JobSatisfaction、EnvironmentSatisfaction、RelationshipSatisfaction、WorkLifeBalance、NumCompaniesWorked、BusinessTravel、Department、MaritalStatus、Gender、EducationField、StockOptionLevel、YearsAtCompany、YearsSinceLastPromotion。你需要输出一份可直接给 HRBP/业务负责人看的结论摘要，说明哪些阈值人群更高风险、哪些人群构成占比更大、以及高风险 cohort 的典型画像。请把分析拆成多个彼此独立的 track，方便并行执行；主线要围绕阈值分层、分位数组和 mix share。
```

### 252. D12_k982626_zh (domain=D12, difficulty=6)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份员工流失的分群对比分析，重点围绕“不同类别分组之间的差异有多大、哪些组的流失率/均值差距最大”展开。请直接读取 df 后，重点比较 Attrition 在多个分类变量上的分布差异，并结合数值变量看各组均值/中位数的差别。请至少覆盖 BusinessTravel、Department、EducationField、JobRole、MaritalStatus、OverTime、Gender 等分组，识别流失率最高/最低的组、组间最大差距、以及这些高差异组在 Age、MonthlyIncome、TotalWorkingYears、JobSatisfaction、EnvironmentSatisfaction、StockOptionLevel、DistanceFromHome 等指标上的典型特征。输出需要适合给 HR 负责人看的结论摘要，且要能拆成多个彼此独立的分析轨道并行完成。
```

### 253. D12_k982778_zh (domain=D12, difficulty=6)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向人力资源团队的员工流失分析，重点围绕“分布与阈值分层”（例如按业务阈值统计高风险/低风险人群、按分位数分桶、看不同群体的构成占比）。请直接使用现有字段做分析，不要改动任何数据。希望你把结论拆成几个彼此独立的分析轨道，便于我分给不同同事并行处理。至少覆盖：1）流失与非流失在关键阈值上的人数与占比；2）年龄、月收入、总工龄、通勤距离等变量的分位数分桶分布；3）OverTime、BusinessTravel、JobLevel、MaritalStatus、Department 等类别变量的构成与流失混合；4）按阈值组合构建若干员工风险画像（例如高通勤+加班、低收入+低工龄等）的规模与流失率；5）找出最值得优先关注的 cohort，并输出可执行的摘要。请确保所有统计都可复现、可核验，并给出清晰的表格化结果或 JSON 风格汇总。
```

### 254. D12_k982885_zh (domain=D12, difficulty=6)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向HR的分群对比分析，重点看不同员工细分群体之间的离职率、均值差异和最大差距。我想知道：1）哪些分类维度（如 Department、JobRole、BusinessTravel、MaritalStatus、OverTime、Gender、EducationField）在离职率上差异最大；2）这些分群与 Age、MonthlyIncome、TotalWorkingYears、JobSatisfaction、EnvironmentSatisfaction、StockOptionLevel 等指标的均值/中位数有何系统性差异；3）在关键群体里，离职员工和未离职员工之间最明显的数值差异是什么；4）是否存在明显的高风险组合（例如某些部门+岗位+加班状态的离职率特别高）；5）输出可以直接给管理层看的结论摘要，最好用可复现的分组统计支撑。请把分析拆成互相独立的几个子任务，方便并行执行。
```

### 255. D12_k982923_en (domain=D12, difficulty=6)

```
Using pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a people-analytics attrition readout focused mainly on correlation and driver analysis: identify which numeric HR fields move together, round correlations to 2 decimals, and surface the strongest associations with Attrition. I need this broken into independent workstreams so different analysts can work in parallel: (1) numeric correlation matrix and top pairwise associations, (2) Attrition vs. pay/tenure/workload relationships, (3) department and job-role differences in the strongest numeric drivers, (4) overtime/travel/years-at-company interaction patterns, and (5) data-quality / coverage checks on the numeric fields used in the analysis. Please summarize the findings in a compact JSON-ready format and call out any surprising or high-signal relationships.
```

### 256. D12_k983081_en (domain=D12, difficulty=6)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a concise HR attrition analysis focused mainly on segment comparisons across categorical groups. I need the clearest gaps in attrition-related metrics by segment, especially where one category materially differs from another. Please use the real columns in the dataset, including Attrition, BusinessTravel, Department, EducationField, Gender, JobRole, MaritalStatus, OverTime, JobInvolvement, JobSatisfaction, EnvironmentSatisfaction, RelationshipSatisfaction, JobLevel, StockOptionLevel, MonthlyIncome, TotalWorkingYears, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, and YearsWithCurrManager. I want a practical readout for HR leadership: identify the biggest segment gaps, the highest-risk groups, and the strongest contrasts between categories. Decompose the work into multiple independent tracks so different analysts can work in parallel, and produce a single analysis_summary.json with the key findings.
```

### 257. D12_k983178_zh (domain=D12, difficulty=6)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向人力资源管理层的员工流失分析，重点围绕“时间/序列趋势”展开：请把 Age、MonthlyIncome、TotalWorkingYears、YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager、TrainingTimesLastYear、OverTime、Attrition、BusinessTravel、Department、JobRole、JobLevel、MaritalStatus、Gender、EducationField、EnvironmentSatisfaction、JobSatisfaction、RelationshipSatisfaction、WorkLifeBalance、StockOptionLevel 等字段结合起来，分析员工在工作年限推进过程中的流失变化、晋升停滞、任职年限积累、培训频次变化、加班与流失关系的周期性特征，以及不同部门/岗位/婚姻状态/性别的趋势差异；请输出可直接给管理层汇报的结论摘要、关键指标的时间序列或分段趋势、以及需要优先干预的人群画像。数据里没有真实日期时，请用 TotalWorkingYears、YearsAtCompany、YearsSinceLastPromotion 等作为序列维度来做“生命周期/阶段”趋势分析。请把结果整理成一个 analysis_summary.json。顺带请回答下面这些可验证的问题，用于核对你的分析结论。
```

### 258. D12_k983291_en (domain=D12, difficulty=6)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build an HR attrition segmentation analysis focused on comparing groups and finding the biggest gaps between segments. I need a concise but rigorous readout that helps me answer: which categorical employee groups have the highest attrition, where the biggest attrition gaps are, and how attrition differs across key business segments. Please use the real columns in this dataset, especially Attrition, BusinessTravel, Department, EducationField, Gender, JobRole, MaritalStatus, OverTime, and WorkLifeBalance, and tie the findings back to practical workforce actions. I want the analysis broken into independent workstreams so different analysts can handle them in parallel, and the final output should be suitable for a short management summary plus a supporting JSON artifact.
```

### 259. D12_k983421_en (domain=D12, difficulty=6)

```
Using pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a people-analytics deep dive on attrition concentration and workforce risk. I need you to identify where attrition is most concentrated and which groups account for the largest share of total leavers, using the real columns in the file (especially Attrition, BusinessTravel, Department, JobRole, MaritalStatus, Gender, OverTime, JobLevel, YearsAtCompany, TotalWorkingYears, DistanceFromHome, MonthlyIncome, and Age). Please break it into separate tracks so different analysts can work in parallel: 1) concentration and Pareto analysis of attrition by department/job role/business travel, 2) top-risk employee profiles and how much of all attrition they explain, 3) seniority/tenure segmentation with share-of-attrition concentration, 4) cross-tab checks for overtime and marital status concentration, and 5) a compact set of executive-ready takeaways that quantify the dominant groups and the cumulative share held by the top segments. Keep it strictly descriptive and deterministic, and focus on ranking, top-N shares, and cumulative concentration.
```

### 260. D12_k983535_en (domain=D12, difficulty=6)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a people-analytics attrition review focused mainly on temporal / trend analysis over sequence fields, especially YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager, and TotalWorkingYears. I need one coherent analysis that explains how attrition risk and engagement patterns change over tenure and career progression, while also checking whether those trends differ by department, job role, overtime, and business travel. Please split the work into independent tracks so a small team could handle them in parallel, and make the output suitable for an executive summary plus supporting detail. Use the real columns in the dataset; do not invent any new fields.
```

### 261. D12_k983569_en (domain=D12, difficulty=6)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build me an HR attrition analysis focused mainly on distribution and threshold cohorts. I want to understand how employee mix and attrition change across business thresholds and quantile buckets, not just simple averages. Please use the real columns in the file, especially Attrition, Age, MonthlyIncome, TotalWorkingYears, DistanceFromHome, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, OverTime, JobLevel, JobRole, Department, MaritalStatus, BusinessTravel, Gender, EnvironmentSatisfaction, JobSatisfaction, and WorkLifeBalance. I need a concise summary that identifies which cohorts are over- or under-represented, where attrition concentrates above/below thresholds, and how the composition differs across segments. Organize the work so it could be split across multiple analysts and then combined into one synthesis.
```

### 262. D12_k983802_en (domain=D12, difficulty=6)

```
Using the file patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a people-analytics attrition review focused mainly on segment comparison across categorical groups. I want you to compare attrition rates, average pay, tenure, and satisfaction across the key categories in the dataset, then identify the biggest gaps between segments and any combinations that look especially high-risk. Please use the real columns such as Attrition, BusinessTravel, Department, EducationField, Gender, JobRole, MaritalStatus, OverTime, EnvironmentSatisfaction, JobSatisfaction, RelationshipSatisfaction, JobInvolvement, JobLevel, and StockOptionLevel. Decompose the work into several independent tracks so different analysts can work in parallel, and end with a concise summary of the most important segment differences and likely retention risk areas.
```

### 263. D12_k983871_en (domain=D12, difficulty=6)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, I need a compact HR attrition analysis focused mainly on temporal / trend-style patterns even though the dataset is not timestamped. Treat the ordered employee records as a sequence and analyze whether attrition risk, work-life factors, tenure, pay, travel, and role mix change across the dataset order. Please split the work into 4-6 independent tracks so different analysts could work in parallel: (1) attrition rate trend across sequential record blocks, (2) tenure/pay trends by attrition status over the sequence, (3) overtime and travel pattern shifts over the sequence, (4) department/job-role composition changes over the sequence, and (5) identify the most pronounced differences between early vs late records on key HR metrics. Use only the real columns in the file, especially Attrition, OverTime, BusinessTravel, Department, JobRole, MonthlyIncome, TotalWorkingYears, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager, WorkLifeBalance, JobSatisfaction, and related fields.
```

### 264. D12_k983925_en (domain=D12, difficulty=6)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a concise HR analytics readout focused mainly on ranking and concentration: identify the highest-contributing groups behind attrition and compensation, quantify top-N shares and Pareto-style concentration, and translate that into practical retention priorities. Please use the real columns in the dataset, especially Attrition, JobRole, Department, BusinessTravel, OverTime, MaritalStatus, Gender, JobLevel, MonthlyIncome, Age, DistanceFromHome, NumCompaniesWorked, TotalWorkingYears, JobSatisfaction, and WorkLifeBalance. I want this split into a few independent workstreams so different analysts could work in parallel, and I need the output packaged as analysis_summary.json with clear rankings, concentration metrics, and short business implications.
```

### 265. D12_k983927_en (domain=D12, difficulty=6)

```
Using pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a people-analytics review focused mainly on temporal / trend patterns in employee tenure and progression. I need one integrated analysis that explains how attrition risk changes across tenure bands and career stages, and how movement through years-at-company, years-in-current-role, years-since-last-promotion, and years-with-current-manager relates to attrition. Please organize the work into separate tracks so different analysts can work independently: (1) attrition trend by tenure band using TotalWorkingYears and YearsAtCompany, (2) period-over-period changes in attrition across years-since-last-promotion and years-in-current-role, (3) progression vs stagnation comparison using YearsWithCurrManager and YearsAtCompany, (4) department/job-role differences in tenure-related attrition trends, (5) overtime and business-travel interactions with tenure trend, and (6) a compact executive summary with the strongest drivers and the most unusual segments. Use the real columns in the file, keep everything deterministic, and produce a concise analysis summary.json with the key findings, segment rankings, and any notable trend inflection points.
```

### 266. D12_k983991_zh (domain=D12, difficulty=6)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向人力资源分析的分组对比研究，重点围绕“不同人群分组之间的差异有多大、差异主要出现在哪些群体”来展开。请结合真实字段做多维度切分，尤其比较不同类别组的流失率、平均薪资、平均工龄、满意度等指标，并找出最大的分组差距。具体希望你把分析拆成若干相互独立的轨道，便于并行处理：例如按部门、按出差频率、按婚姻状态、按性别、按是否加班、按岗位层级/职位角色等分别比较。请输出适合管理层阅读的结论，指出最值得关注的高风险细分群体，以及哪些分组差距最明显。最终交付为 analysis_summary.json。
```

### 267. D12_k984001_en (domain=D12, difficulty=6)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, run a people analytics review focused mainly on correlation and driver analysis. I want a compact but rigorous readout of which numeric HR fields move together, which variables have the strongest rounded correlations with attrition, and how those relationships differ across key employee segments. Please structure the work so it can be split across 4–6 independent tracks: overall numeric correlation structure, top attrition drivers among numeric fields, compensation/workload relationships, tenure/promotion relationships, and segment cuts by department or overtime where helpful. Use the real columns in the file (for example Age, DailyRate, DistanceFromHome, MonthlyIncome, MonthlyRate, NumCompaniesWorked, PercentSalaryHike, TotalWorkingYears, TrainingTimesLastYear, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager, WorkLifeBalance, and Attrition). Return a concise analysis summary with the strongest rounded associations and the most important patterns for HR action.
```

### 268. D12_k984155_en (domain=D12, difficulty=6)

```
Using the dataset in pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, please run a HR analytics deep-dive focused mainly on correlation and driver analysis across the numeric fields. I need you to identify which continuous/numeric variables move together most strongly, report rounded correlations, and summarize the strongest positive and negative associations in a way a people-analytics team could use. Please also break the work into a few independent tracks so different analysts can work in parallel: one track for the overall numeric correlation structure, one for attrition-related numeric drivers, one for pay/tenure relationships, one for job satisfaction and engagement patterns, and one for any surprising outliers or concentration patterns in employee profiles. Keep the output concise and business-facing, with a final JSON summary.
```

### 269. D12_k984162_en (domain=D12, difficulty=6)

```
Using the file patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a compact HR analytics readout focused mainly on correlation and driver analysis. I want to know which numeric fields move together, the strongest rounded correlations, and which people/role/work-pattern factors look most associated with attrition in this dataset. Please break it into independent workstreams so they can be handled in parallel: one track for numeric correlation structure, one for attrition-linked numeric drivers, one for attrition by key categorical factors, one for role/tenure patterns, and one for data-quality/sanity checks on fields that could distort correlations. Keep the output practical and decision-oriented, not academic.
```

### 270. D12_k984201_zh (domain=D12, difficulty=6)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的人力资源分析，重点围绕“不同员工分群之间的差异”来找出离职风险和管理机会。请务必直接使用数据里的真实字段（例如 Attrition、Department、JobRole、MaritalStatus、Gender、BusinessTravel、OverTime、WorkLifeBalance、JobSatisfaction、EnvironmentSatisfaction、RelationshipSatisfaction、JobLevel、StockOptionLevel、Age、MonthlyIncome、TotalWorkingYears、DistanceFromHome、YearsAtCompany、YearsInCurrentRole 等），不要做预测模型。希望输出能帮助我回答：哪些分类群体的离职率差异最大、哪些群体在薪酬/工龄/满意度上表现明显不同、以及这些差异在不同业务场景下意味着什么。请把分析拆成 4-6 个相互独立的轨道，方便不同小组并行完成，并最终汇总成一个简洁的 analysis_summary.json。
```

### 271. D12_k984296_en (domain=D12, difficulty=6)

```
Using the file `patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv`, please build a people-analytics memo focused mainly on ranking and concentration patterns in this workforce. I need you to identify the biggest contributors to attrition and the most concentrated employee groups by headcount and compensation, using the real columns in the dataset (for example: `Attrition`, `BusinessTravel`, `Department`, `JobRole`, `MaritalStatus`, `OverTime`, `MonthlyIncome`, `JobLevel`, `Age`, `DistanceFromHome`, `YearsAtCompany`, `YearsSinceLastPromotion`, `StockOptionLevel`, `JobSatisfaction`, `EnvironmentSatisfaction`, `RelationshipSatisfaction`, `WorkLifeBalance`, etc.). Please structure the work as a set of independent tracks so different analysts can work in parallel: (1) rank the top attrition-driving segments and quantify their share of all leavers; (2) measure headcount concentration across job roles, departments, and travel patterns; (3) analyze compensation concentration using `MonthlyIncome` and `JobLevel` (top earners, share of total payroll, and Pareto-style concentration); (4) compare attrition concentration among overtime and marital-status groups; and (5) sanity-check whether the highest-concentration groups also align with low satisfaction or long commute indicators. I only need the final memo summary and supporting counts, not modeling or charts.
```

### 272. D12_k984443_zh (domain=D12, difficulty=6)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向人力资源管理的综合分析，重点围绕“排名与集中度”展开：先找出离职人数/离职率最高的细分群体、岗位、部门、出差类型、婚姻状态等 top-N 组合，再看这些 top 群体是否贡献了离职总量中的大部分（例如前 20% 群体是否占到 80% 左右），并结合收入、工龄、加班、工作满意度等变量判断离职风险是否高度集中在少数人群中。请把结果拆成 4-6 个彼此独立的分析轨道，方便并行处理；每条轨道都要给出可核验的结论、关键排名、以及集中度/占比指标。字段请直接使用数据中的真实列名，例如 Attrition、Department、JobRole、BusinessTravel、MaritalStatus、OverTime、Age、MonthlyIncome、TotalWorkingYears、JobSatisfaction、EnvironmentSatisfaction、NumCompaniesWorked、DistanceFromHome、StockOptionLevel 等。
```

### 273. D12_k984681_en (domain=D12, difficulty=6)

```
Using pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a people-analytics attrition brief focused on ranking and concentration. I need a clear read on where attrition and workforce value are most concentrated, which groups account for the largest shares, and whether a small set of roles, departments, travel patterns, overtime status, and tenure bands drive a Pareto-like pattern. Use the real columns in the file, including Attrition, Department, JobRole, BusinessTravel, OverTime, Age, MonthlyIncome, TotalWorkingYears, YearsAtCompany, YearsInCurrentRole, StockOptionLevel, JobLevel, and DistanceFromHome. Break the work into independent tracks so it can be split across sub-agents: (1) attrition concentration by department and job role, (2) share-of-total analysis for top categories and Pareto-style cumulative share, (3) concentration of high-income employees and whether a few roles/levels hold most payroll, (4) attrition ranking by travel/overtime/tenure bands, and (5) key cross-tabs that explain where attrition is disproportionately concentrated. Deliver the result as a concise analysis summary JSON.
```

### 274. D12_k984715_zh (domain=D12, difficulty=6)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向 HR 的综合分析，重点围绕“相关性与驱动因素分析”：先找出所有数值字段之间哪些最相关（请输出四舍五入到 2 位的小数的相关系数），再识别离职 Attrition 的关键数值驱动因素，并结合岗位、加班、婚姻状态等分类字段做交叉验证。请把结果拆成几个彼此独立的分析轨道，分别覆盖：1）整体数值相关矩阵与最强正/负相关对；2）离职与非离职员工在核心数值指标上的差异；3）离职率在不同加班/婚姻状态/部门/岗位上的差异；4）与离职最相关的连续变量排序；5）高风险人群画像（例如按工作年限、年龄、收入分位分组）；6）输出可直接交给管理层的结论摘要。请注意该数据集固定不变，不要推断不存在的字段，也不要做建模或可视化，只输出可复核的统计结果。
```

### 275. D12_k984754_zh (domain=D12, difficulty=6)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的人力资源分析，重点围绕“不同员工群体之间的离职差异”展开。请按可并行的 4-6 个分析轨道拆解：1）按部门、岗位、婚姻状态、性别、是否加班（Attrition/OverTime）等分类，比较离职率、平均收入、平均工龄等核心指标，找出差异最大的群组；2）分析通勤距离、出差频率（BusinessTravel）和离职的关系，输出各组离职率及最大差距；3）比较不同 JobLevel、教育程度、教育领域（EducationField）之间的收入和离职差异，识别最脆弱人群；4）分析工作满意度、环境满意度、关系满意度、工作投入等评分在离职与未离职员工之间的差异，并比较各组均值；5）检查绩效薪资涨幅（PercentSalaryHike）、股票期权（StockOptionLevel）、培训次数（TrainingTimesLastYear）与离职的分组差异；6）补充一个综合结论，指出最值得优先干预的员工细分群体，并说明依据。请输出一份可直接给 HR 管理层的分析摘要。
```

### 276. D12_k984923_zh (domain=D12, difficulty=6)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的员工数据异常审计，重点围绕“显式数值规则的异常/离群检测”展开。请直接用现有字段分析，不要补造任何值。我要你把结果拆成几个可并行的小分析：先用明确阈值、IQR、极端值和稀有类别找出异常员工，再看这些异常是否在离职、部门、职位、是否加班、出差频率等维度上集中；同时给出几类最值得关注的异常规则（例如年龄、距离、工龄、月收入、总工龄、换工作次数、晋升间隔等的极端值），并说明这些异常人群在 Attrition 上的差异。最后请输出一份可直接给我看的结构化结论，文件名按 analysis_summary.json 组织即可。
```

### 277. D12_k984963_en (domain=D12, difficulty=6)

```
Using pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build an HR attrition review centered on temporal / trend analysis using the sequence-style tenure fields (especially YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager, and TotalWorkingYears). I need a practical, decision-ready summary that shows where attrition risk appears to rise or fall across tenure bands and promotion/manager timelines, and how those patterns differ by key segments like Department, JobRole, OverTime, and BusinessTravel. Please organize the work so the analysis can be done in parallel, then return a concise JSON summary with the main trend findings, the most important segment differences, and a short list of actionable retention implications.
```

### 278. D12_k984992_en (domain=D12, difficulty=6)

```
Using patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a segment-comparison HR attrition analysis focused mainly on which employee groups have the biggest gaps in attrition and related workforce characteristics. I need a practical readout comparing rates/means across categorical segments, especially Attrition by BusinessTravel, Department, JobRole, MaritalStatus, Gender, OverTime, and EducationField, plus any key interactions where the gaps look largest. Please split the work into independent tracks so different analysts can work in parallel, and summarize the strongest differences, not just overall averages.
```

### 279. D12_k985152_en (domain=D12, difficulty=6)

```
Using the file jpmiller__employee-attrition-for-healthcare__watson_healthcare_modified.csv, build an HR analytics readout centered on attrition trends over the employee sequence and tenure-related progression. I want a multi-part analysis that is practical for workforce planning: first, examine how attrition changes across the employee sequence and whether the rate is shifting over time; second, compare attrition trends by shift and overtime status; third, identify which job roles and departments show the sharpest changes in attrition across tenure bands or employee order; fourth, quantify whether pay, job level, and total working years are associated with attrition changes over the sequence; fifth, summarize the most recent versus earliest segments of the workforce to highlight drift in risk factors; and sixth, pull together any notable interactions between satisfaction/involvement measures and attrition trend movement. Keep it grounded in the real columns in the dataset, and make the output suitable for an HR leader who needs concise, evidence-based takeaways.
```

### 280. D12_k985348_en (domain=D12, difficulty=6)

```
Using arashnic__hr-analytics-job-change-of-data-scientists__aug_train.csv, analyze likely job-change risk in this HR analytics dataset with a strong temporal/sequence lens even though the only sequence field is `last_new_job`. I want a practical readout of how job-change target rates vary across recency buckets in `last_new_job`, whether those patterns differ by `experience`, `education_level`, `company_size`, and `enrolled_university`, and how they compare against other signals like `city_development_index`, `training_hours`, and `relevent_experience`. Please structure the work so I can hand off independent pieces and then combine them into a concise summary and a few actionable insights for people analytics.
```

### 281. D13_g280_en (domain=D13, difficulty=6)

```
I need you to analyze the four files in inputs/ (events.xlsx, users.xlsx, daily_metrics.xlsx, support_tickets.xlsx) for the experiment exp_search_checkout_v2. Produce a brief decision report in recommendation.md that includes: data quality checks (duplicates, future dates, conflicting variants), 14-day purchase conversion rates for control and treatment with lift, funnel step counts from signup to purchase with drop-off rates, and identify the cohort_date with the highest 7-day purchase conversion rate. Then recommend one of: ship treatment, hold treatment and fix data, or roll back treatment, backed by the numeric findings.
```

### 282. D13_g336_en (domain=D13, difficulty=6)

```
We're analyzing a checkout funnel experiment from the input files: users.csv, sessions.xlsx, events.xlsx, assignments.xlsx, and touchpoints.csv. I need a few compact aggregate reports (CSV/JSON/MD) that synthesize across these files.

- Count of users with conflicting experiment assignments (more than one distinct variant in assignments.xlsx per user).
- Data quality on events.xlsx: exact duplicate rows, future-dated rows (after 2024-06-30), and rows where variant conflicts with the canonical assignment from assignments.xlsx.
- After cleaning events (removing duplicates, future dates, and variant conflicts), compute per-variant purchase conversion rate and the B minus A delta, then produce funnel step counts and step-to-step transition rates for view_pricing → start_checkout → add_payment → purchase.
- Revenue per assigned user for each variant from purchase events after the same cleaning.
- Data quality on touchpoints.csv: duplicate rows and future-dated touchpoints.
```

### 283. D13_g490_en (domain=D13, difficulty=6)

```
I need a compact but rigorous product analytics readout for the checkout_v4 experiment using inputs/users.csv, inputs/experiment_assignments.csv, inputs/events.xlsx, and inputs/customer_surveys.csv.

Please produce three deliverables only: a CSV for the experiment readout, a JSON for data-quality reconciliation, and a Markdown memo that ties the numbers together. I want the readout to be based on a single canonical user table built from the assignment file after deduping exact duplicate assignment rows, then resolving conflicting assignment rows by keeping the earliest assigned_at for each user_id; if two rows for the same user_id have the exact same assigned_at but different variants, keep the lexicographically smaller variant string. Any assignment row with assigned_at after 2025-01-01T00:00 should be treated as invalid and excluded from the canonical assignment table entirely. For event data, keep exact duplicate event_id rows only once, exclude any event with event_ts after 2025-01-01T00:00, and exclude events that occur strictly before the user’s canonical assigned_at. Join events to the canonical assignment table on user_id only after those filters. For survey data, dedupe exact duplicate rows first.

For the experiment readout, I want the closed universe to be users with a valid canonical assignment to either control or treatment. Please report the assigned-user counts by variant, the number of users with at least one purchase_complete event after assignment, the conversion rate for each variant, the absolute lift in conversion rate in percentage points, and the relative lift versus control. Use the formula lift_pp = treatment_cvr - control_cvr and relative_lift = (treatment_cvr / control_cvr) - 1. Round rates and lifts to 4 decimal places. Also include the median time in minutes from canonical assignment to the first purchase_complete event for purchasers only, measured in whole minutes by floor of the time difference; if a user has multiple purchase_complete events after assignment, use the earliest one.

For the funnel, use the same canonical assignment universe and count users who reach each step at least once after assignment in this exact order: landing_view, signup_start, signup_complete, checkout_view, payment_submit, purchase_complete. A user is counted at a step only if they have that event type on or after assigned_at and on or before 2024-12-31T23:59. Report step counts by variant, plus step-to-step conversion percentages within variant. Use the same round-to-4-decimals convention. Step-to-step conversion is count(step_k)/count(step_k-1). For the first step, report step reach rate = count(landing_view)/assigned users in that variant. I do not want any retention analysis.

For data quality, I want a compact reconciliation summary with counts of: raw assignment rows, exact duplicate assignment rows removed, conflicting assignment users, invalid future-dated assignment rows removed, raw event rows, exact duplicate event rows removed, future-dated events removed, pre-assignment events removed, raw survey rows, exact duplicate survey rows removed. Also report the number of unique users appearing in the final canonical assignment table and the number of users with at least one event retained after all event filters. Finally, list the user_id values of the 5 users with the highest total retained revenue_usd from purchase_complete events after assignment, breaking ties by higher retained purchase_complete event count, then lexicographically smaller user_id. If there are fewer than 5 such users, list all of them. Use JSON for that reconciliation object.

In the Markdown memo, I want a short executive summary plus a table that compares control and treatment on assigned users, purchase conversions, conversion rate, and lift, and a second table for the funnel step counts and step-to-step conversion percentages for both variants. Please keep everything compact and explicitly state the filter logic you used.
```

### 284. D13_g622_zh (domain=D13, difficulty=6)

```
我这边要做一次 checkout 改版 A/B 的简版读数，麻烦你直接基于下面 4 个文件出一份紧凑的分析产物：inputs/experiment_assignments.xlsx、inputs/events.xlsx、inputs/orders.csv、inputs/segment_expectations.csv。我关心的是最终纳入实验的样本规模、漏斗各步人数与步间流失、control/treatment 的支付转化率和 uplift，以及几条明显的数据质量问题。实验口径我先说清楚：只看 2024-06-30 23:59:59 之前的数据；分配表里 2024-06-01 00:00:00 之后的 assignment 先当作未来记录排除；同一个 user_id + experiment_id 如果出现多个 variant，就把这个用户整组剔除；assignment 去重时保留 assigned_at 最新的一条。事件口径也请严格一点：events 里完全相同的重复行按 (user_id, event_name, event_ts, session_id, order_id, amount, country) 去重，保留第一条；漏斗顺序固定为 product_view → add_to_cart → checkout_start → payment_success；漏斗人数按用户算，一个用户在某一步只要在其最终保留的 assigned_at 之后至少发生过一次该事件就算进入该步。转化率定义为 payment_success 用户数 / 该组纳入用户数；uplift 请同时给绝对提升和相对提升，绝对提升 = treatment 转化率 - control 转化率，相对提升 = 绝对提升 / control 转化率。orders 里按 order_id 去重，保留最后一条，输出 gross GMV、refunds、net GMV；payment_success 里缺失 order_id 的事件也请单独报出来；另外把未来日期的 assignment、未来日期的 event、完全重复事件行、以及冲突分配用户数都列成数据质量摘要。最后我想要 2 到 3 个紧凑文件：一个 JSON 主摘要、一个 CSV 漏斗/实验汇总表、一个 MD 的简短发现说明。内容不要铺太散，重点是我能快速拿给业务看。
```

### 285. D13_g981385_en (domain=D13, difficulty=6)

```
You are analyzing a signup checkout A/B test with user profiles, assignments, and event logs. Some rows contain deliberate anomalies. Use the provided files to clean the data and compute the experiment results.
```

### 286. D13_g981519_en (domain=D13, difficulty=6)

```
Analyze the provided experiment inputs and determine whether the checkout variant appears better than control after cleaning obvious data issues. You should inspect the event log, assignment map, catalog, and memo, then produce a concise analytical summary.
```

### 287. D13_g981527_en (domain=D13, difficulty=6)

```
You are given a large synthetic experiment event log, a compact funnel summary, and a short reference brief.
Analyze the data quality and experiment outcomes, then produce a concise operational report.

Focus on: assignment integrity, funnel progression, suspicious records, and treatment-vs-control comparison.
Keep the analysis grounded in the provided files only.
```

### 288. D13_g981701_en (domain=D13, difficulty=6)

```
You are given a dataset of user events from an A/B testing platform. The data includes user demographics, experiment assignments, and a funnel of events (page_view -> add_to_cart -> checkout -> purchase) with timestamps. Some users have conflicting assignments (both variants) for the same experiment. Your task is to analyze the effect of experiment variants on the conversion funnel. Provide a clear summary of the results, including any statistically significant differences, and identify any potential data quality issues (e.g., conflicts).
```

### 289. D13_g982020_en (domain=D13, difficulty=6)

```
You are given experiment assignment and event logs from a product onboarding A/B test. Some records are noisy or anomalous: duplicated assignment rows, conflicting user assignments, duplicate events, and future-dated events. Clean and analyze the data, then summarize the experiment.
```

### 290. D13_g982437_en (domain=D13, difficulty=6)

```
You are a data quality analyst. A team has collected user assignment data and event logs for an A/B test on a website funnel (step1 → step2 → step3 → step4 → purchase). The data may contain conflicts, duplicates, and future-dated records. Please analyze the provided data and produce a report identifying all data quality issues, their impact on the analysis, and suggested fixes.
```

### 291. D13_k982972_zh (domain=D13, difficulty=6)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份面向产品分析的深度解读，重点放在相关性与驱动因素分析：先看数值字段 buy_mount、day、cat_id、cat1、user_id、auction_id 之间哪些更相关（请给出四舍五入到 2 位的小数相关系数），再结合分组统计找出影响购买次数的主要模式。请拆成 4-6 个彼此独立的分析轨道并分别产出结论：1）整体数据质量与字段分布；2）buy_mount 的集中度、极值和高购买记录特征；3）day 的时间分布及其与 buy_mount 的关系；4）cat_id / cat1 的品类驱动与头部关联；5）user_id / auction_id 的重复出现与活跃度驱动；6）基于数值字段相关矩阵和若干分组指标，输出最值得关注的 top associations。最后把所有结论整理成一个可直接给业务同事看的简短 summary。
```

### 292. D13_k983039_zh (domain=D13, difficulty=6)

```
请基于文件 yasserh__amazon-product-reviews-dataset__7817_1.csv 做一份面向产品分析的分群对比分析，重点围绕不同类别/品牌/价格段/推荐与评分之间的差异来找出“谁更好、差多少、差异最大在哪里”。我需要你把结果拆成可并行推进的几个分析轨道，并最终输出一份简洁的 analysis_summary.json。请务必只使用数据里真实存在的列：brand、categories、prices、reviews.rating、reviews.doRecommend、reviews.numHelpful、reviews.text、reviews.title、reviews.date、dateAdded、dateUpdated、name、manufacturer 等。核心要回答：1）哪些品牌、品类、价格段的平均评分更高；2）哪些分组的推荐率差异最大；3）哪些组更容易获得高帮助票数；4）评论内容长度或标题长度是否在不同分组间有系统差异；5）能否找出表现最好的与最差的细分群体，并量化它们的差距。请按业务分析口径写结论，尽量给出可落地的分群洞察和优先级建议。
```

### 293. D13_k983056_en (domain=D13, difficulty=6)

```
Using akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv, build a product-analytics readout focused mainly on correlation and driver analysis across the real columns user_id, auction_id, cat_id, cat1, property, buy_mount, and day. I need a concise but decision-oriented summary that shows which numeric fields move together, where the strongest rounded correlations are, and what obvious high-signal associations exist. Please split the work into 4-6 independent tracks so separate analysts can work in parallel: one track for data quality and cardinality checks, one for overall correlation structure among numeric fields, one for transaction intensity drivers by cat1/cat_id/day, one for user-level purchase behavior concentration, and one for property-string complexity/associations. Keep it grounded in the actual dataset and return a compact analysis_summary.json suitable for product stakeholders.
```

### 294. D13_k983224_en (domain=D13, difficulty=6)

```
Use the file akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv and analyze the product behavior data in df with columns user_id, auction_id, cat_id, cat1, property, buy_mount, and day. I need a compact but rigorous product analytics readout focused mainly on correlation and driver analysis: which numeric fields move together, which rounded correlations stand out, and what associations look most important for understanding buying activity. Please break it into 4-6 independent workstreams so different agents can work in parallel, and keep the findings practical for a busy stakeholder.
```

### 295. D13_k983260_en (domain=D13, difficulty=6)

```
Using akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv with the real columns user_id, auction_id, cat_id, cat1, property, buy_mount, and day, I need a product-analytics readout focused mainly on ranking and concentration. Please analyze which users, categories, and day-level cohorts account for most of the buying activity, quantify Pareto-style concentration (top-N shares, cumulative shares, and how steep the long tail is), and summarize the most extreme repeat-behavior patterns. I also want the output to be usable for prioritizing merchandising and retention work, so include the most important top contributors by frequency and by buy_mount value, plus any simple distribution checks that help explain whether activity is concentrated in a small set of buyers, auctions, or categories. Break this into independent workstreams so different analysts could handle user concentration, category concentration, auction concentration, time concentration, and property-string complexity separately. Deliver the results as analysis_summary.json.
```

### 296. D13_k983574_en (domain=D13, difficulty=6)

```
Using PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv, I need a product-analytics readout focused mainly on correlation and driver analysis. Please break it into 5 independent tracks so a small team can work in parallel: (1) data quality and field readiness for numeric analysis, especially retail_price, discounted_price, product_rating, and overall_rating; (2) price and discount relationships, including which numeric fields move together most strongly and whether higher-priced items also have larger discounts; (3) rating/price drivers by brand and product category tree, looking for segments where correlation patterns differ; (4) category-level price ladders and discount depth patterns, using the product_category_tree and brand fields to identify where the strongest associations sit; and (5) a concise executive summary of the top positive and negative correlations, plus the most notable product segments driving them. Use the fixed dataset as-is, round correlations to 2 decimals, and keep outputs compact enough for a decision memo.
```

### 297. D13_k983677_en (domain=D13, difficulty=6)

```
Using the file akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv with the columns user_id, auction_id, cat_id, cat1, property, buy_mount, and day, I need a product-analytics review focused mainly on anomaly and outlier detection using explicit numeric rules. Please identify unusual buying behavior with deterministic thresholds, rare categories, and extreme values, then summarize what looks most suspicious or operationally important. Break the work into independent tracks so different people can handle them in parallel: one track on extreme buy_mount outliers, one on rare category/category1 patterns, one on temporal spikes by day, one on repeated-auction or repeated-user anomalies, and one on property-pattern irregularities. I only need a concise analysis summary JSON plus any supporting counts/tables that help explain the anomalies.
```

### 298. D13_k983729_en (domain=D13, difficulty=6)

```
Using inputs/yasserh__amazon-product-reviews-dataset__7817_1.csv, I need a product-analytics readout focused on ranking and concentration. Please find where review volume and rating contribution are concentrated across products, brands, and categories in this dataset, and quantify the Pareto-style skew (top-N share, cumulative share, and any long-tail effects). Use the real columns in the file, especially id, brand, categories, name, reviews.rating, reviews.numHelpful, reviews.doRecommend, reviews.username, and dateAdded/dateUpdated. I want this broken into separate workstreams so they can be done in parallel: identify the most-reviewed products and their share of all reviews; identify the most common brands and how concentrated review volume is by brand; identify the most common category groupings and their concentration; compare high-rating vs low-rating products for concentration differences; and surface any products/brands that dominate helpfulness or recommendation activity. Please summarize the ranking patterns, top groups, cumulative shares, and whether the distribution looks heavily skewed or relatively balanced.
```

### 299. D13_k983777_en (domain=D13, difficulty=6)

```
Using yasserh__amazon-product-reviews-dataset__7817_1.csv, do a product-analytics deep dive focused mainly on correlation and driver analysis. I need you to identify which numeric fields move together, round correlations to 2 decimals, and call out the strongest associations that are actually actionable. Split the work into independent tracks so it can be done in parallel: 1) data quality and coverage of numeric/review fields, 2) correlation structure among the numeric fields and missingness patterns, 3) review sentiment/engagement drivers around reviews.rating, reviews.numHelpful, and reviews.doRecommend, 4) category/product-level differences in rating and helpfulness, and 5) brand/manufacturer-level concentration and whether any brands are associated with systematically higher or lower ratings. Please make sure the analysis is grounded only in the real columns in this file: id, asins, brand, categories, colors, dateAdded, dateUpdated, dimension, ean, keys, manufacturer, manufacturerNumber, name, prices, reviews.date, reviews.doRecommend, reviews.numHelpful, reviews.rating, reviews.sourceURLs, reviews.text, reviews.title, reviews.userCity, reviews.userProvince, reviews.username, sizes, upc, weight. I want a concise summary plus the exact correlation findings and top associations.
```

### 300. D13_k983906_en (domain=D13, difficulty=6)

```
Using yasserh__amazon-product-reviews-dataset__7817_1.csv, please run a product analytics review focused mainly on temporal trend analysis. I need a compact but decision-ready summary that tracks how review volume, average star rating, recommendation rate, and helpfulness change over time using the date fields (especially reviews.date, dateAdded, and dateUpdated). Please break it into 4-6 independent workstreams so they can be analyzed in parallel: (1) review volume and rating trends by year and month, (2) period-over-period changes in rating and recommendation behavior, (3) brand/product comparisons across time, (4) helpfulness trends over time, and (5) any notable data-quality issues in the date fields that could affect the trend analysis. Use the real columns in the file, and keep the output concise but actionable for product stakeholders.
```

### 301. D13_k983966_en (domain=D13, difficulty=6)

```
Using the file yasserh__amazon-product-reviews-dataset__7817_1.csv, run a product analytics deep-dive focused mainly on correlation and driver analysis: figure out which numeric fields move together, which relationships are strongest once rounded to 2 decimals, and what simple product/review factors seem associated with higher review ratings and helpfulness. Please break it into independent workstreams so a team can split it up: one track for numeric correlation mapping across reviews.rating, reviews.numHelpful, ean, sizes, upc; one track for rating drivers by brand/manufacturer/category; one track for helpfulness drivers by review text/title/recommendation signals; one track for completeness/data-quality checks that could bias correlations; and one track for identifying the most review-rich products and whether they differ in rating/helpfulness patterns. Keep the output concise but decision-useful, with rounded correlations and top associations highlighted.
```

### 302. D13_k984003_zh (domain=D13, difficulty=6)

```
请基于文件 PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv 做一版产品分析，重点围绕“分布与阈值分层”来帮我判断价格带、折扣带、评分带、品牌集中度和类目结构是否健康。请直接用数据里的真实字段分析：retail_price、discounted_price、product_rating、overall_rating、brand、product_category_tree、is_FK_Advantage_product、description、product_specifications。我要的是能给业务汇报用的结论，不是探索性随便看一眼。请至少拆成 5 个彼此独立的分析轨道：先把价格按业务阈值分层，比较各层商品数和价格中位数；再把折扣率做分位数/阈值分箱，看不同折扣带的商品占比、均价和品牌分布；再检查评分字段在不同价格层和折扣层的缺失/占比；再做类目树的头部集中度与长尾占比；最后结合 is_FK_Advantage_product 看它在高价/高折扣商品中的渗透率。输出时请明确告诉我哪些阈值是用真实分位数或固定业务阈值切出来的，并给出每个分层的数量与 mix share。若字段有缺失或 'No rating available'，请按分析口径显式处理并说明。尽量给出可以直接放进管理层摘要的结论。
```

### 303. D13_k984121_zh (domain=D13, difficulty=6)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份面向产品分析的复杂拆解，重点围绕“排名与集中度”来展开：看哪些 user_id、auction_id、cat_id、cat1、property 在交易量上最集中，Top-N 的份额有多高，是否存在明显的 80/20 现象，以及不同维度之间的集中度差异。请把分析拆成 4-6 个彼此独立、适合并行推进的子任务，并最终输出一份可直接给业务方看的结论型 analysis_summary.json。请结合真实字段 user_id、auction_id、cat_id、cat1、property、buy_mount、day，给出可解释的排行、占比、累计贡献和头部集中情况；如果需要，也请顺带看一下按 day 的交易是否也呈现头部日期集中。
```

### 304. D13_k984325_en (domain=D13, difficulty=6)

```
Using the file akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv and its real columns user_id, auction_id, cat_id, cat1, property, buy_mount, and day, build a product analytics readout focused mainly on distribution and threshold cohorts. I need a practical summary of how order volume and basket size are distributed across users, auctions, categories, and dates; how many users/items fall above or below business thresholds; how those threshold cohorts differ by category mix and timing; and where the biggest concentration/long-tail effects are. Please split the work so separate analyses can be run independently and then merged into one concise analysis_summary.json.
```

### 305. D13_k984527_en (domain=D13, difficulty=6)

```
Using the file yasserh__amazon-product-reviews-dataset__7817_1.csv, build a product analytics readout focused on ranking and concentration. I need a compact but rigorous analysis of where review volume and rating signals are concentrated across brands and products, using the available columns like brand, name, reviews.rating, reviews.numHelpful, reviews.doRecommend, reviews.username, categories, and prices. Please decompose it into 4-6 independent workstreams so different analysts could work in parallel: (1) brand and product top-N concentration by review count and share of total, (2) Pareto-style coverage of reviews across brands/products, (3) rating quality among the highest-volume brands/products versus the rest, (4) helpfulness and recommendation concentration among top-ranked items, and (5) any category-level concentration if categories can be parsed cleanly from the strings. I want the output to identify the dominant brands/products, quantify how much of the total review activity they capture, and flag any big mismatches between popularity and quality.
```

### 306. D13_k984556_zh (domain=D13, difficulty=6)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份产品分析，重点围绕“分布与阈值分层”来拆解：先看 buy_mount 的分布、异常大额/小额阈值、按阈值划分后的用户与交易占比，再结合 day 做时间维度上的分层对比；同时用 user_id、auction_id、cat_id、cat1、property 这些字段做必要的交叉分析，看看不同阈值层的商品类目结构、属性复杂度以及复购/重复交易迹象。请把结果整理成可直接给业务汇报的分析结论，并重点回答：1）当前数据中 buy_mount 的主流分布区间和极端值情况是什么；2）若按业务阈值分层（如 >1、>2、>=3 等），各层交易数/用户数/GMV 占比如何；3）不同日区间或时间段中，高阈值交易是否更集中；4）高低阈值交易在 cat1/cat_id 与 property 复杂度上的 mix 有何差异；5）是否存在少数用户或少数 auction_id 贡献了明显的高阈值交易集中度。请按多分析轨道并行推进，最后给我一份简洁、可复核的 summary。
```

### 307. D13_k984604_en (domain=D13, difficulty=6)

```
Using akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv, analyze the trade history with a focus on ranking and concentration. I need a concise product analytics readout that tells me which categories, users, days, and product-property combinations account for most of the activity. Please break it into independent workstreams so different people can handle them in parallel: 1) top-N concentration by category and cat1, 2) user-level concentration and Pareto share, 3) temporal concentration by day/month, 4) product-property sparsity and top repeated property patterns, 5) basket-style repeat behavior using buy_mount, and 6) cross-segment concentration comparisons between high-volume and long-tail groups. Use the actual columns user_id, auction_id, cat_id, cat1, property, buy_mount, and day, and keep the output business-friendly for a product analytics team.
```

### 308. D13_k984632_en (domain=D13, difficulty=6)

```
Using yasserh__amazon-product-reviews-dataset__7817_1.csv, I need a product-analytics readout focused mainly on ranking and concentration. Please analyze which products, brands, and categories dominate review volume and review impact, and show where a small number of items account for a large share of activity. Break it into independent workstreams so a small sub-team can work in parallel: 1) top products by review count and their share of all reviews, 2) top brands/categories by review count and concentration/Pareto share, 3) review-score concentration by product and brand using reviews.rating, 4) helpfulness concentration using reviews.numHelpful and doRecommend, 5) overlap between top-reviewed products and highest-rated products, and 6) data quality checks for missingness in key ranking fields like brand, name, categories, reviews.rating, reviews.numHelpful, and reviews.doRecommend. Please summarize the practical implications for merchandising and prioritization.
```

### 309. D13_k984727_zh (domain=D13, difficulty=6)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份产品分析，重点围绕“异常与离群识别”展开，尽量用明确的数值规则来找问题：比如 IQR 规则、极端值、稀有类目、异常高频用户、异常购买量等。数据里有 user_id、auction_id、cat_id、cat1、property、buy_mount、day，day 是交易日期，buy_mount 是购买数量。我要你把结果拆成几条互相独立的分析线，方便不同同学并行推进，并输出一份适合汇报的分析结论。请至少覆盖：1）buy_mount 的极端值和分布异常；2）按 user_id 的高频/高额异常行为；3）按 auction_id、cat_id、cat1 的稀有类目与集中异常；4）按 day 的时间异常峰值；5）property 字段中异常稀有属性组合；6）跨字段交叉异常（例如极端 buy_mount 是否集中在某些类目或用户）。最后请给出可以直接落地的异常筛查规则建议和需要进一步人工复核的样本方向。
```

### 310. D13_k984787_en (domain=D13, difficulty=6)

```
Using the file akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv, analyze the product purchase history with a focus on distribution and threshold cohorts. I need a practical product-analytics readout built around counts above/below business thresholds, quantile buckets, and mix shares. Please use the real columns user_id, auction_id, cat_id, cat1, property, buy_mount, and day only. I want a concise analysis that tells me: how concentrated purchase quantities are, what share of orders/users fall into small vs large baskets, how much volume comes from the top quantiles, whether the monthly mix shifts over time, and which categories dominate the heavy-basket cohort. Please structure it so multiple analysts could work in parallel and then merge their findings into a single analysis_summary.json.
```

### 311. D13_k984871_zh (domain=D13, difficulty=6)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一版产品分析，重点围绕“分布与阈值分层”来写：我想知道用户在购买记录里的活跃度分布、按业务阈值切分后的高低价值人群占比、不同分位桶的结构差异，以及这些阈值分层在 category / cat1 / 购买金额（buy_mount） / 时间（day）上的混合特征。请直接给我可落地的结论框架，不要泛泛而谈。字段里我关心 user_id、auction_id、cat_id、cat1、property、buy_mount、day，尤其要结合计数阈值、分位数分桶和 mix share 做分析。最好把分析拆成多个互相独立的 track，便于并行处理，最后汇总成 analysis_summary.json。
```

### 312. D13_k984925_en (domain=D13, difficulty=6)

```
Using akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv, I need a product-analytics readout focused mainly on correlation and driver analysis. Please examine how the numeric fields move together, identify the strongest rounded correlations, and interpret what seems to be driving purchase volume. Split the work into independent tracks so different people can work in parallel: (1) data sanity and coverage for user_id, auction_id, cat_id, cat1, buy_mount, and day; (2) correlation analysis across the numeric fields with rounded coefficients and strongest pairs; (3) purchase-volume drivers by category and category-1 using buy_mount; (4) day/time pattern checks for whether buy_mount changes over time; (5) concentration analysis for repeat users and repeated auctions; and (6) a short synthesis of the top associations and any notable anomalies.
```

### 313. D13_k984976_en (domain=D13, difficulty=6)

```
Using akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv, analyze this maternal-and-infant shopping history with a focus on distribution & threshold cohorts. I need a concise product-analytics readout that quantifies how behavior changes around clear business thresholds: order-size buckets for buy_mount, day-based cohorts, category concentration and mix shares, and a few user-level thresholds. Please break it into independent workstreams so different agents can work in parallel: one on overall distribution/threshold framing, one on category and auction mix concentration, one on user repeat-purchase thresholds, one on time-window cohorts, and one on property-string complexity as a proxy for assortment richness. Keep the output compact and decision-oriented, and return a single analysis_summary.json.
```

### 314. D13_k984988_zh (domain=D13, difficulty=6)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份产品分析。重点围绕“数值字段之间的相关性与驱动因素”展开：先把 day、buy_mount 这类数值字段之间的关联理清楚，再补充按用户、类目、商品特征的细分对比。请给我一份可直接交付的分析结论，最好能说明哪些字段一起变化、相关性最强的组合、以及可能的业务含义。顺手也帮我确认几个基础事实，比如记录规模、时间跨度、字段缺失情况、重复交易/多次购买情况等。
```

### 315. D13_k985003_zh (domain=D13, difficulty=6)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份面向产品分析的紧凑但完整的分析报告，重点围绕“排名与集中度”展开：比如按 user_id、cat_id、cat1、day 的Top-N频次/购买量排名、头部用户/品类/日期的份额、以及是否存在明显的帕累托集中。请把结论拆成可并行推进的 4-6 个独立分析轨道，并尽量输出能直接给业务看的摘要。数据字段只有 user_id、auction_id、cat_id、cat1、property、buy_mount、day；请结合这些真实列做分析，不要编造口径。最终请输出一个 analysis_summary.json 风格的结果，能概括头部贡献、集中度、以及关键异常或机会点。
```

### 316. D13_k985010_en (domain=D13, difficulty=6)

```
Using yasserh__amazon-product-reviews-dataset__7817_1.csv, run a product-analytics review focused mainly on ranking and concentration. I need you to break the work into 5 independent tracks: (1) rank products by review volume and quantify how concentrated review activity is in the top products, (2) rank brands by review volume and measure Pareto-style share held by the top brands, (3) rank products by average review rating only among products with meaningful volume so we can spot highly rated high-visibility items, (4) rank products by helpfulness engagement and identify whether a small set of products captures most helpful votes, and (5) analyze whether recommendation and rating concentration differ between the highest-volume products and the rest. Please use the real columns in the file, especially name, brand, reviews.rating, reviews.numHelpful, reviews.doRecommend, and id/asins where needed. I want a concise analysis summary plus supporting deterministic checks that verify the top-N ranks, shares of total, and any simple concentration metrics you compute.
```

### 317. D13_k985251_en (domain=D13, difficulty=6)

```
Using PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv, I need a product-analytics readout focused mainly on segment comparison across categorical groups. Please break it into 4-6 independent tracks so different analysts can work in parallel: (1) compare pricing and discount behavior across product categories from product_category_tree, (2) compare brand-level and category-level rating patterns using product_rating / overall_rating, (3) identify the biggest price gaps between segments using retail_price vs discounted_price, (4) examine how missingness and 'No rating available' are distributed by category/brand, and (5) summarize category concentration and top segments by count. Use the real columns in the file, keep all results deterministic, and return a concise analysis_summary.json with the biggest gaps, leading segments, and any notable anomalies.
```

### 318. D13_k985276_en (domain=D13, difficulty=6)

```
Using akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv, I need a product-analytics readout focused mainly on ranking and concentration. Please analyze the trade history across user_id, auction_id, cat_id, cat1, property, buy_mount, and day, and tell me where activity is most concentrated. I want a compact executive summary plus the supporting metrics behind it: top-N users/items/categories, share of total volume captured by the top groups, Pareto-style concentration, and any obvious skew by day or category. Please structure the work so separate analysts can tackle independent tracks and then merge into one analysis_summary.json.
```

### 319. D13_k985339_zh (domain=D13, difficulty=6)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份面向产品分析的深度分析，重点围绕“排名与集中度”来展开：看哪些商品/类目/属性标签最集中，头部用户是否贡献了大部分购买量，以及是否存在明显的 80/20 现象。请结合列 user_id、auction_id、cat_id、cat1、property、buy_mount、day，输出一份可落地的分析结论，最好能解释头部贡献、长尾分布和关键类目/属性的集中风险，并给出我后续可以继续追问的数据切片方向。
```

### 320. D13_k985499_zh (domain=D13, difficulty=6)

```
请基于文件 nisargpatel__automobiles__Automobile.csv 做一份面向产品分析的多部分数据分析，重点围绕“相关性与驱动因素分析”：哪些数值字段彼此一起变化、关键特征之间的相关强弱、以及价格/油耗/动力等指标的主要关联驱动。请直接使用数据中的真实列：symboling、normalized_losses、wheel_base、length、width、height、curb_weight、engine_size、bore、stroke、compression_ratio、horsepower、peak_rpm、city_mpg、highway_mpg、price 等，并结合 make、fuel_type、aspiration、body_style、drive_wheels、engine_type、number_of_cylinders、fuel_system 做分组补充。请拆成 4-6 个彼此独立的分析轨道：1）核心数值指标的相关矩阵与Top关联对；2）price 的驱动因素排序；3）油耗与动力相关链路；4）不同车身/驱动/发动机类型下的差异；5）高相关变量的冗余与共线性提示；6）必要时补充缺失值/样本分布对相关性的影响。输出一份可执行的分析结论摘要，适合产品团队快速判断哪些变量最值得作为定价或性能解释因子。
```

### 321. D13_k985534_en (domain=D13, difficulty=6)

```
Using the file salmanabdu__tokopedia-product-reviews-2025__tokopedia_product_reviews_2025.csv, help me do a product-analytics deep dive focused mainly on correlation and driver analysis across the numeric fields review_id, product_price, product_id, rating, sold_count, and shop_id. I want a practical readout of which numeric variables move together, which associations are strongest after rounding correlations to 2 decimals, and whether review sentiment, rating, product price, sold count, product category, and product variant reveal any meaningful patterns. Please structure it as a compact analysis I can hand to stakeholders, with clear takeaways, a few robust sanity checks, and no invented values. Treat it like a real analyst task: identify the strongest positive and negative correlations, compare metrics by sentiment label, inspect ratings by category/variant, and surface any concentration in reviews by product or shop. Use the real column names exactly as in the dataset.
```

### 322. D13_k985598_en (domain=D13, difficulty=6)

```
Using iamsouravbanerjee__cars-dataset__cars.csv, build a product-analytics readout focused on ranking and concentration. I need to know which car brands, models, countries, and credit card types dominate the dataset, how concentrated the top groups are versus the long tail, and whether concentration changes when we slice by country, year of manufacture, and car color. Please also surface any notable Pareto-style patterns, like the share held by the top 3/5/10 categories and the most common brand-model combinations.
```

### 323. D13_k985697_en (domain=D13, difficulty=6)

```
Using mfaaris__spotify-app-reviews-2022__reviews.csv with the real columns Time_submitted, Review, Rating, Total_thumbsup, and Reply, build a product-analytics readout focused mainly on distribution and threshold cohorts. I need to know how review volume, sentiment proxy (Rating), and engagement (Total_thumbsup) break across business thresholds, especially counts above/below key cutoffs, quantile buckets, and mix shares. Please structure the work so different analysts can tackle separate tracks independently, then synthesize the results into a concise analysis_summary.json with actionable takeaways for Spotify’s app review backlog and response prioritization.
```

### 324. D13_k985704_en (domain=D13, difficulty=6)

```
Using the file sudarshan24byte__online-food-dataset__onlinefoods.csv, do a product-analytics readout focused mainly on distribution and threshold cohorts. I want you to split the work into a few independent tracks and then summarize the findings in analysis_summary.json. Please look at how customer mix changes above vs below practical business thresholds across Age, Family size, Monthly Income, Educational Qualifications, and geography, and connect that to Output and Feedback. Include quantile-bucket views, threshold counts, and share-of-total mix where useful. Also check for any data-quality oddities in the columns, especially the extra Unnamed: 12 field, and use the real column names exactly as they appear in the file.
```

### 325. D13_k985821_en (domain=D13, difficulty=6)

```
Use the file anvitkumar__shopping-dataset__Combined_dataset.csv to do a product-analytics deep dive focused mainly on correlation and driver analysis. I want you to identify which numeric fields move together, call out the strongest rounded correlations, and explain what seems to drive pricing, discounts, and popularity. Please break the work into independent tracks so different analysts could work in parallel: one track on numeric relationships across rating, ratings_count, initial_price, discount, and final_price; one track on price/discount patterns by category; one track on rating and review-count drivers; one track on missingness and data quality for the analytical fields; and one track on a compact summary of the most extreme products/outliers that may be influencing correlations. Keep it practical and grounded in the actual columns present in the dataset (product_id, title, rating, ratings_count, initial_price, discount, final_price, currency, category, seller_name, and the text/metadata fields where relevant).
```

### 326. D1_g1221_zh (domain=D1, difficulty=6)

```
我需要你综合多个输入文件，围绕2026-05-06的Partner Review（联合评审会）做跨来源核对：识别会议安排、参会人、相关待办以及任何冲突或异常，并给出结论。
```

### 327. D1_g1250_en (domain=D1, difficulty=6)

```
I need you to analyze the five input files in the inputs/ folder: calendar_A.csv, calendar_B.xlsx, action_items.csv, status_notes.xlsx, and meeting_requests.xlsx. Please produce two deliverables: a compact research/synthesis brief in markdown (findings.md) and a small evidence table (evidence.csv or evidence.md). The brief must reconcile the sources, explain any conflicts or anomalies, and include a short cross-source reconciliation section that explicitly notes at least one calendar conflict/duplicate issue and one notes/action‑item caveat. The table should support the synthesis with aggregated evidence.

Here are the specific results I need, all based on cross‑source reconciliation and deduplication where applicable – please treat each as a discrete analysis point:

- For the calendar files: after deduplicating rows by the pair (event_id, employee_id) across both calendar_A.csv and calendar_B.xlsx, report the number of rows remaining, the number of exact duplicate rows removed (identical in all fields), and the number of conflicting duplicate keys (same event_id+employee_id but differing event details).  
- Identify the earliest common free 30‑minute slot on 2026‑06‑03 for Lucas Thomas (E04) and Sophia Brown (E05).  
- Identify the earliest common free 90‑minute slot on 2026‑06‑03 for Noah Patel (E02), Mike Liu (E07), and Emma Taylor (E06).  

- For the action items: after deduplicating by action ID, compute the overdue open‑action‑item rate. “Overdue” means due_date < 2026‑06‑01 and status is not exactly “Done”. Also report how many open action items in the Skyline Delivery project (P01) have a priority of “High” or “Critical” (after dedup). Then report which owner has the most open action items in that same project (P01) and how many that owner has.

- For the status notes: in the date window 2026‑05‑20 through 2026‑05‑31 inclusive, report which project has the highest count of negative notes (presumably notes with a negative sentiment or flag), and how many that project has. Separately, report how many negative notes Skyline Delivery (P01) has in that same window.

The output must be a synthesis, not a raw dump – use explicit cross‑source reconciliation wherever sources disagree. Keep both deliverables aggregate‑focused and compact.
```

### 328. D1_g1318_zh (domain=D1, difficulty=6)

```
你好，我是项目负责人张明。我们团队最近在准备季度复盘，需要你帮忙整合一下从多个渠道收集到的信息，出一份状态汇总报告。

我们有以下几份数据：
- 团队成员名单：inputs/team.json
- 行动项清单：inputs/action_items.xlsx
- 邮件记录：inputs/emails.json（里面包含团队成员对行动项的状态更新）
- 日历事件：inputs/calendar_events.xlsx（记录了各种会议）

我需要你完成以下分析（你可以自己想办法分解工作，但最终产出一份 findings.md 以及一个简洁的证据表格(evidence_table.md)）：
1. 日历分析：统计每个团队成员的参会情况，包括总参会次数、总共花了多少小时开会，以及是否存在同一时间段两个会议冲突（按每人每天算）。只统计有参会人员的会议（空会议不计入）。
2. 行动项分析：总行动项数、逾期（指截止日期在今天之前且状态不是"已完成"或"已关闭"的）的数量、整体完成率（已完成或已关闭的占比），以及每个成员被分配了多少行动项。
3. 邮件状态核对：从邮件正文中提取出提到的行动项（像"AI-001"这样的编号），然后根据内容推断出状态（比如"已完成""进行中""阻塞"等）。再对照行动项清单里的实际状态，看看是否一致。注意：如果邮件说"阻塞"，而行动项状态是"进行中"，也算一致（阻塞是进行中的一种特殊情况）。
4. 交叉验证：找出那些在行动项清单里有分配任务，但从未出现在任何会议参会名单上的成员（忽略非团队成员的分配）。也要找出那些有参加会议但是没有任何行动项的成员。
5. 汇总每个人一张小卡片，包括：姓名、分配的行动项数量、参加的会议次数、发送的邮件数量。

请使用以下规则：
- 今天日期设定为 2025-03-20。
- 行动项截止日期以 CSV 中的 "due_date" 列为准。
- 邮件状态推断使用关键词：包含“已完成”或“done”视为“已完成”；“阻塞”或"blocked"视为“阻塞”；“进行中”或"progress"视为“进行中”；“已关闭”或"close"视为“已关闭”；“未开始”或“待办”视为“未开始”；否则为“未知”。
- 行动项实际状态以 CSV 中的 "status" 列（中文）为准。
- 会议时长由 start_time 和 end_time 计算，小时为单位。
- 冲突是指同一个人同一天内两个会议的时间段有重叠（一个会议的结束时间晚于另一个的开始时间）。
- 空会议（attendees 字段为空的）不计入任何参会统计，但总会议数里依然包含它。

输出文件：findings.md 包含上述分析的主要发现（文本描述），evidence_table.md 包含一个表格，列出每个团队成员的上述汇总数据（姓名、行动项数、会议次数、邮件数、是否逾期任务、是否有会议冲突）。另外，在 findings.md 里也列出前三名参会最多的成员。

请不要改原始数据，直接读取即可。输出要放在工作目录下。
```

### 329. D1_g1446_en (domain=D1, difficulty=6)

```
I need a Q1 2026 program health synthesis from three input files in ./inputs/:
 - calendar_log.xlsx (calendar events with attendees, location, status, actual attendance)
 - action_items.json (action items with assignee, due date, status, linked event)
 - team_rollups.json (team status reports with claimed metrics)

Please produce three JSON deliverables:
1) risk_assessment.json – with per-team composite risk score using the formula: risk = 0.4*action_overdue_rate + 0.3*conflict_frequency + 0.3*low_attendance_flag. Action_overdue_rate = fraction of action items per team past due (due before Apr 1) and not completed. Conflict_frequency = average scheduling conflict count per person in that team (events overlapping for same attendee), divided by 5, capped at 1. Low_attendance_flag = 1 if average actual/invited attendance <0.7, else 0. Round risk to two decimals; flag teams with risk >0.6 as high-risk.
2) discrepancy_report.json – list any team where claimed completion rate (extracted from report text as a percentage number) differs from actual completion rate by >=10 percentage points.
3) recommendations.json – top 3 actionable recommendations (strings) based on findings.

All fields: conform to standard Q1 2026 boundaries (Jan 1 to Mar 31, inclusive). Scheduling conflicts: two events share at least one attendee and their time intervals overlap (start<end of other). Actual attendance rate per event = actual_attendees / length of attendees list. Team membership for each person is given by: Alice:Engineering, Bob:Marketing, ..., Tina:Support (according to the mapping in the data generation seed). If a team has no action items, treat overdue_rate=0. Deliverables must be compact JSON arrays/objects, not exceeding a few dozen lines.
```

### 330. D1_g980647_en (domain=D1, difficulty=6)

```
You are given three input workbooks containing synthetic team records, calendar events, and action items. Analyze them jointly and produce a concise operational review. Keep the answer grounded in the files and compute any requested counts exactly.
```

### 331. D1_g980718_zh (domain=D1, difficulty=6)

```
收件箱里有一封 Partner Corp 陈总监发来的会议邮件，我需要你把这次协作安排整理成一个简洁的综合报告。
请基于 inputs/meeting_briefing.xlsx、inputs/action_items_status.xlsx 和 inputs/schedule_constraints.docx 处理下面这些点：
- 确认邮件里的会议时长、地点偏好和目标对象；
- 查清孙博、吕安的联系方式，并核对他们在 2026-05-20 的日程是否能拼出 1.5 小时的共同空档；
- 同时把相关行动项的状态做一个简短汇总，重点看当天到期的未完成事项；
- 输出一个可直接转发给团队的紧凑报告，里面要有最终安排、备选时段和异常说明。
- 报告里请把联系人、日程判断、行动项汇总和需要特别注意的冲突点都写清楚。
```

### 332. D1_g980758_zh (domain=D1, difficulty=6)

```
请审阅 inputs/meetings.xlsx、inputs/actions.xlsx 和 inputs/status_brief.docx，写一份 findings.md。 需要把会议日程、行动项状态和文档口径合并成一份简短分析，并明确说明跨文件的口径冲突、重复项和排期冲突。 结果里要分别列出 4 个独立分析方向的结论，再给一段综合建议。
```

### 333. D1_g981186_en (domain=D1, difficulty=6)

```
We have two datasets: conversations.json (employee check-in logs) and calendar_data.xlsx (meetings with action items). I need a concise analysis brief that covers:
- Meeting conflict patterns (overlapping meetings per participant)
- Action item completion rates (per participant and overall total)
- Employee sentiment trends from conversations
- Any discrepancies between the two datasets (e.g. participants with high conflicts showing negative sentiment)
- Anomalies in the data (duplicate IDs, missing fields, negative duration)

Synthesize everything into findings.md with clear cross-references. Provide the meeting date range, average durations, and a summary table of anomalies. Keep it factual and compact.
```

### 334. D1_g981868_zh (domain=D1, difficulty=6)

```
请把这三份文件里和 2026-04-27 这次需求评审相关的信息整理成一份汇总报告：inputs/calendar_events.xlsx、inputs/action_items.xlsx、inputs/status_rollups.xlsx。
- 先确认这场评审会的安排是否和其他日程冲突，并把冲突点说清楚。
- 再梳理相关行动项的推进情况，重点看哪些还没完成、哪些已经过期。
- 最后汇总状态周报里和这次协调有关的整体信号，顺手标出重复记录这类异常。
- 报告里请给出一个简洁的结论区和一个可直接发给项目组的待办摘要。
```

### 335. D1_k981729_zh (domain=D1, difficulty=6)

```
请基于文件 vladtasca__fomc-meeting-statements-and-minutes__communications.csv（列包括 Date、Release Date、Type、Text）做一份面向办公室/运营与协作分析的多维度研究，重点放在时间趋势和周期变化上。我要你把这 464 条沟通记录按发布时间、正式日期、文档类型和文本长度来拆解，判断不同类型文件的发布节奏、季节性/阶段性变化、发布延迟是否有变化，以及文本内容复杂度是否随时间演变。请同时关注：1）按年、季度、月的发布量趋势；2）Minutes 和 Statement 两类文档的时序对比与增速变化；3）发布日期与正式日期之间的滞后分布及其时间演化；4）按文本长度分组后的时间结构变化；5）在不同年份里 Type 结构是否发生迁移；6）识别最密集的发布月份/季度，并说明是否存在明显的周期峰值。请输出可直接给管理层看的结论和一份结构化摘要，方便我快速判断沟通节奏和协作负荷的变化。
```

### 336. D1_k982171_en (domain=D1, difficulty=6)

```
Using programmer3__construction-project-management-dataset__construction_dataset.csv, analyze how task execution differs across segments in our office/operations planning workflow. I need a segment-comparison report centered on categorical differences, especially where the biggest gaps are between groups. Please compare the dataset by Risk_Level and also by any relevant categorical splits you can derive from existing fields, then tie those segments back to operational burden and coordination friction using Task_Duration_Days, Labor_Required, Equipment_Units, Material_Cost_USD, Start_Constraint, Resource_Constraint_Score, Site_Constraint_Score, and Dependency_Count. I want the analysis to identify which segments are most expensive, slowest, most resource-intensive, and most constrained, and to call out the largest between-group gaps in means/rates. Please produce a concise analysis summary in analysis_summary.json with clear segment comparisons and the key takeaways for operations planning.
```

### 337. D1_k982910_en (domain=D1, difficulty=6)

```
Using the file bushraqurban__global-urbanization-and-climate-metrics__global_urbanization_climate_metrics.csv, build an operations-and-collaboration style analysis focused mainly on ranking and concentration: I want to know which countries and years dominate the dataset, how concentrated the top contributors are for population, GDP, urbanization, internet use, energy use, and CO2 emissions, and whether the same small set of countries keeps appearing at the top across different metrics. Please separate the work into independent tracks so different analysts can work in parallel: 1) top-country concentration by record count and by key metrics, 2) top-year concentration and temporal dominance, 3) Pareto/share-of-total analysis for GDP, population, CO2, and energy, 4) overlap of top-10 lists across metrics, 5) missing-data concentration among the most important countries/years, and 6) a compact executive summary of the most concentrated metric(s) and the most dominant country/year groups. Use the real columns in the file only (country, country_code, year, total_pop, gdp, urban_pop_perc, internet_use_pop, energy_kg_oil_eq_cap, co2_emiss_excl_lulucf, and the other available fields as needed).
```

### 338. D1_k983028_en (domain=D1, difficulty=6)

```
Using the file bushraqurban__global-urbanization-and-climate-metrics__global_urbanization_climate_metrics.csv, analyze how the numeric operational and sustainability metrics move together across countries and years. I need a correlation and driver analysis focused on office / operations & collaboration analytics: identify the strongest pairwise associations among the numeric fields, compare which infrastructure/adoption variables are most connected to urbanization and GDP, and surface any data-quality patterns that could affect interpretation. Please break it into multiple independent workstreams so different analysts could work in parallel, and keep the output concise and decision-oriented.
```

### 339. D1_k983449_zh (domain=D1, difficulty=6)

```
请基于数据文件 nehaprabhavalkar__av-healthcare-analytics-ii__train_data.csv 做一份面向办公室/运营与协作分析的多维诊断，重点围绕“排名与集中度”来展开：先找出 Stay、Hospital_code、Department、Ward_Type、Hospital_region_code、Hospital_type_code、Type of Admission、Severity of Illness、Age 等维度中的头部组别及其占比，再评估是否存在明显的帕累托集中现象（例如 Top-N 占比、累计占比、HHI/集中度的替代性度量），并结合 Admission_Deposit、Visitors with Patient、Available Extra Rooms in Hospital、Bed Grade、City_Code_Patient、City_Code_Hospital 等字段，判断高占比组是否也对应更高的资源使用、不同患者来源或更高严重程度。请把分析拆成 4-6 个彼此独立的分析轨道，分别覆盖：1）住院时长分布与集中度；2）医院/科室/病区的头部集中；3）入院类型与病情严重程度的集中；4）不同年龄与地区来源的集中；5）高集中组与资源指标的关联；6）必要时补充一个交叉维度的 Pareto 检查。最终输出一份可供管理层快速阅读的结构化摘要。
```

### 340. D1_k983709_en (domain=D1, difficulty=6)

```
Using grandmaster07__final-dataset__final_dataset.csv, analyze the office / operations & collaboration analytics implications of air quality across the observed dates. Focus the main story on distribution and threshold cohorts: how often observations fall above/below business thresholds, how the dataset splits into quantile buckets, and what the mix shares look like across pollutants and AQI. I need a practical decision memo, not a generic EDA.

Please decompose the work into 5 independent tracks so they can be handled in parallel: (1) AQI threshold cohort sizing and mix shares, (2) pollutant threshold exceedance profiling, (3) quantile-bucket segmentation of AQI and key pollutants, (4) seasonal/monthly distribution shifts in threshold cohorts, and (5) holiday-vs-non-holiday differences in cohort composition. Use the real columns Date, Month, Year, Holidays_Count, Days, PM2.5, PM10, NO2, SO2, CO, Ozone, and AQI exactly as given in the file. The final output should be a compact summary suitable for operations planning.
```

### 341. D1_k984275_en (domain=D1, difficulty=6)

```
Use the file ucimachinelearning__home-energy-management-dataset__HEMS_dataset.csv to produce an office / operations & collaboration analytics brief focused mainly on ranking and concentration patterns in usage. I need you to identify which houses, hours, weekdays, and operating modes account for the biggest shares of demand, cost, and grid impact, and quantify how concentrated the workload is (top-N shares, Pareto-style concentration, and whether a small set of records drives most of the totals). Please use the real columns in the dataset, especially house_id, timestamp, day_of_week, hour_of_day, minute_of_hour, is_weekend, total_demand_kW, instantaneous_cost_INR, grid_import_kW, grid_export_kW, net_grid_power_kW, pv_generation_kW, battery_soc_kWh, ev_charging_on, washing_machine_on, dishwasher_on, water_heater_on, hvac_power_kW, solar_irradiance_Wm2, and grid_co2_intensity_g_per_kWh. Decompose the work into 4-6 independent tracks so separate agents could handle them: (1) concentration by house and top contributors, (2) concentration by time of day / weekday, (3) Pareto of costs vs demand vs grid import, (4) operating-mode comparisons for EV/HVAC/appliances, and (5) PV/battery offset and grid-impact concentration.
```

### 342. D1_k984603_en (domain=D1, difficulty=6)

```
Using the file `thedevastator__county-cancer-death-rates__incd.csv`, analyze the county cancer incidence data with an operations/collaboration analytics lens, focusing mainly on correlation and driver analysis across the numeric fields. I want you to identify which measures move together most strongly, how the recent 5-year trend relates to current incidence and uncertainty bounds, whether counties with higher average annual counts also tend to have different incidence levels or trends, and whether the missing/placeholder entries are concentrated in any pattern that could distort the analysis. Please break this into a few independent workstreams so they can be handled in parallel, and then summarize the most important rounded correlations and top associations in a concise output file.
```

### 343. D3_g1178_en (domain=D3, difficulty=6)

```
请处理 inputs/ 下四个文件：customers_adult_like.xlsx、iris_extended.csv、transactions_q1.xlsx、sensor_kpis_daily.csv。清洗数据、检测异常，然后整合成一份研究简报（findings.md）和一张证据表（evidence_table.csv 或 markdown 表格）。几个要点：

- 客户数据：清洗后统计总行数、高收入率、前三职业。
- 鸢尾花数据：清洗后统计各物种花瓣长度均值，列出被剔除的异常行ID。
- 交易数据：清洗后统计总收入前两区域，列出因规则被剔除的订单ID。
- 传感器数据：清洗后按站点统计日均输出量，找出清洗后峰值温度对应的日期和数值。
- 在简报中注明清洗/异常对结果的影响，并做跨源冲突或异常说明。

证据表只放汇总指标，不要逐行罗列。
```

### 344. D3_g1274_zh (domain=D3, difficulty=6)

```
请帮我基于四个来源的数据完成一份中文分析简报，重点包括：

- 识别数据中的异常点
- 概括关键 KPI 表现
- 做跨来源对照，指出各来源之间的冲突与一致性

直接给出分析结果即可。
```

### 345. D3_g980513_zh (domain=D3, difficulty=6)

```
请基于这三份输入表做一版跨来源的数据清洗与指标分析，最后输出一份简洁的 findings.md，重点把异常、口径差异和关键 KPI 结论说清楚。

- 需要同时看 customer_profiles.xlsx、cellar_wine_metrics.xlsx、abalone_shell_metrics.xlsx 三个文件，先各自清洗，再合并成统一结论。
- 每个来源都要单独说明检测到的异常类型、清洗后保留下来的样本范围，以及 1-2 个最重要的 KPI。
- 需要做一次跨来源对照，指出三份数据里哪些结论方向一致、哪些不一致，给出可能原因。
- findings.md 里最好有一个小结表，方便我直接拿去给团队汇报。
- 重点是结果要清楚、可追溯，不要只给一段笼统描述。
```

### 346. D3_g980881_en (domain=D3, difficulty=6)

```
I need you to review employment_kpi_master.xlsx, system_events.log, and dataset_notes.txt, clean up the bad rows, check the obvious anomalies, and put together one short findings brief in Markdown that compares the employment data, the daily KPI table, and the event log. I want the main patterns, the flagged issues, and any cross-source connections you find.
```

### 347. D3_g980922_zh (domain=D3, difficulty=6)

```
请基于 inputs 里的 operational_metrics.xlsx 和 policy_notes.docx 做一份综合分析简报，重点把清洗、异常核查和 KPI 汇总串起来，并说明不同来源之间是否能对上。
- 先分别看员工、酒液、门店三张表的质量问题和核心指标。
- 再把 DOCX 里的政策数字和表格里的汇总结果做交叉核对，指出是否一致。
- 最后输出一份 findings.md，要求结构清楚，结论先行，附上关键数字和冲突说明。
```

### 348. D3_g980936_zh (domain=D3, difficulty=6)

```
请基于 inputs/sales_ops.xlsx、inputs/quality_logs.xlsx 和 inputs/benchmark_entities.xlsx 做一份决策简报，重点判断本期最值得优先处理的业务问题，并给出排序后的建议。我需要你同时把销售异常、质量日志异常、以及 benchmark 结果合并起来看，最后输出一份简短但完整的中文决策文件。
```

### 349. D3_g981022_en (domain=D3, difficulty=6)

```
You are auditing three synthetic operational datasets (adult-like records, iris-like measurements, and wine-like batches). Analyze the inputs, reconcile anomalies, and summarize the highest-priority findings.
```

### 350. D3_g981213_zh (domain=D3, difficulty=6)

```
请把 iris_panel.xlsx、adult_income_panel.xlsx、abalone_metrics_panel.xlsx 这三份表整理成一份决策简报，直接告诉我哪些面板最值得优先修复，并把你发现的关键异常和KPI一起写进去。我要的是一份能给管理层看的短报告，不要原始明细。
```

### 351. D3_k981708_zh (domain=D3, difficulty=6)

```
请基于文件 `karkavelrajaj__amazon-sales-dataset__amazon.csv` 做一份面向业务决策的电商商品分析，重点围绕“时间序列/趋势”来展开。数据里没有显式日期字段，所以请先把它当作一份固定快照数据，结合 `rating_count`、`rating`、`discount_percentage`、`discounted_price`、`actual_price`、`category`、`product_name`、`product_id`、`review_id`、`user_id`、`user_name` 等字段，做可复现的趋势类分析：例如按分组构造序列后的变化、不同价格/折扣区间的变化率、类别层面的相对变化、头部与长尾商品的“阶段性”表现对比等。请输出一份可供管理层阅读的简洁结论，重点回答：1）哪些类别/价格带/折扣带表现更强，2）评分与评价量之间是否存在明显联动，3）头部商品与长尾商品在业务指标上有何差异，4）哪些现象可被视作“趋势上的异常点”或需要进一步监控。请把分析拆成多个彼此独立的子任务，适合并行协作完成。文件字段均为原始真实值，不要改写任何数据。
```

### 352. D3_k981717_en (domain=D3, difficulty=6)

```
Using saidaminsaidaxmadov__chocolate-sales__Chocolate Sales (2).csv, I need a BI-style anomaly review focused mainly on explicit outlier detection. Please analyze Sales Person, Country, Product, Date, Amount, and Boxes Shipped, and decompose it into separate workstreams so different analysts could work in parallel. I want you to identify unusual transactions using clear numeric rules (for example IQR-based outliers, extreme values, rare categories, and threshold-based spikes), then summarize where the anomalies cluster by country, product, salesperson, and date. Please also compare whether high-Amount anomalies and high-Boxes-Shipped anomalies overlap or come from different segments, and call out the most extreme records and the rarest category combinations.
```

### 353. D3_k982118_en (domain=D3, difficulty=6)

```
Using the file imakash3011__online-shoppers-purchasing-intention-dataset__online_shoppers_intention.csv, build a BI-style analysis focused mainly on correlation and driver analysis for Revenue and related engagement metrics. I need a compact executive summary plus evidence on which numeric fields move together, the strongest positive/negative rounded correlations, and which visitor/session attributes appear most associated with purchase intent. Please split the work into 4-6 independent tracks so multiple analysts could work in parallel: one track on numeric correlation structure, one on Revenue driver ranking, one on segment comparisons by VisitorType/Weekend/Month, one on page-activity intensity vs purchase intent, and one on data quality/coverage of the key fields. Use the real columns exactly as named (e.g. Administrative, Administrative_Duration, Informational, Informational_Duration, ProductRelated, ProductRelated_Duration, BounceRates, ExitRates, PageValues, SpecialDay, Month, OperatingSystems, Browser, Region, TrafficType, VisitorType, Weekend, Revenue).
```

### 354. D3_k982385_zh (domain=D3, difficulty=6)

```
请基于数据文件 syedanwarafridi__vehicle-sales-data__car_prices.csv 做一份面向业务决策的二手车拍卖/销售分析，重点围绕“排名与集中度”展开：一方面找出销量和成交额最高的品牌、车型、州别、卖家及车身类型；另一方面评估这些头部群体是否高度集中（例如前 N 名占比、累计占比、帕累托 80/20 特征）。请结合 year、make、model、body、state、seller、sellingprice、mmr、condition、odometer、transmission、saledate 等字段，输出可直接给管理层看的结论，并指出哪些头部类别最值得优先关注。分析要覆盖 4-6 个相互独立的方向，便于分工协作。
```

### 355. D3_k982424_en (domain=D3, difficulty=6)

```
Using the file nilesh2042__nba-player-stats-2026__nba_player_stats_2026.csv, run a BI-style anomaly review on the NBA player stats and summarize the most suspicious outliers. Build the work around explicit numeric rules, not subjective judgments: identify players who are extreme on minutes/usage/production efficiency, players with unusually poor shooting or ball security, and any rare-category patterns by team or role. Please make this a structured analysis that can be split across multiple assistants, and include a concise output I can share with leadership. Focus on the columns PLAYER, TEAM, GP, MIN, FGM/FGA/FG_PCT, FG3M/FG3A/FG3_PCT, FTM/FTA/FT_PCT, REB, AST, STL, BLK, TOV, PTS, EFF, AST_TOV, and STL_TOV. I want the result to emphasize anomaly and outlier detection using explicit thresholds (for example: top/bottom percentile style cutoffs, IQR-based fences, and rare category counts), plus a short list of the players and teams that deserve a manual audit.
```

### 356. D3_k982601_en (domain=D3, difficulty=6)

```
Using manishabhatt22__marketing-campaign-performance-dataset__marketing_campaign_dataset.csv, run a correlation and driver analysis on the campaign performance data. I need a BI-style readout focused on which numeric fields move together and which variables seem to drive ROI and Conversion_Rate. Please use the real columns in the file, especially Conversion_Rate, Acquisition_Cost, ROI, Clicks, Impressions, and Engagement_Score, and break the work into a few independent tracks so different analysts could work in parallel. I want a concise evidence-based summary with rounded correlations, the strongest positive/negative associations, and a few segment cuts by Campaign_Type, Channel_Used, Customer_Segment, and Location to see where the strongest drivers show up.
```

### 357. D3_k982791_en (domain=D3, difficulty=6)

```
Analyze shashankshukla123123__marketing-campaign__marketing_campaign.csv as a marketing BI dataset, with the main focus on ranking and concentration. I need a compact decision-ready readout that tells me which customer segments and behaviors account for most of the revenue-driving activity. Please break it into independent workstreams so different people can work in parallel: 1) rank customers by total spend and quantify how concentrated spend is in the top 10%, top 20%, and top 5% of customers; 2) rank product categories and purchase channels by total spend / purchase volume and measure what share of total each top group holds; 3) rank customer segments by education, marital status, and age bands to identify the highest-value groups and their share of total spending; 4) quantify campaign response concentration by looking at which historical acceptors and recency bands contribute most of the Response=1 population; 5) identify outlier concentration in high-income or high-frequency shoppers versus the rest, using deterministic thresholds and top-group shares. Use the actual columns in the file, and keep the output practical for a BI audience.
```

### 358. D3_k982846_en (domain=D3, difficulty=6)

```
Using the file arunavakrchakraborty__australia-weather-data__Weather Training Data.csv, run a correlation and driver analysis on the weather features. I want a compact BI-style readout that focuses on which numeric fields move together, the strongest positive and negative rounded correlations, and what seems to drive RainTomorrow. Please break it into independent workstreams so multiple analysts could work in parallel: one for global numeric correlations, one for rainfall/rain-tomorrow drivers, one for temperature and humidity relationships, one for pressure and cloud interactions, and one for location-level differences in the strongest associations. Use the real columns in the file (MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, WindGustSpeed, WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Cloud9am, Cloud3pm, Temp9am, Temp3pm, RainToday, RainTomorrow, Location) and keep the output business-friendly with rounded correlation values and short ranked lists.
```

### 359. D3_k983085_en (domain=D3, difficulty=6)

```
Using maazshaikh05__global-web-traffic__global_web_traffic_dataset.csv, analyze the traffic mix with a heavy focus on ranking and concentration. I want a BI-style readout that tells me which countries, traffic sources, device types, browsers, and pages account for the most visits, how concentrated the traffic is among the top groups (top 3 / top 5 / top 10 shares and Pareto-style concentration), and whether the biggest traffic segments also over-index on conversions, bounces, or session depth. Please use the real columns in the file: visit_id, date, country, traffic_source, device_type, browser, page, session_duration_sec, pages_viewed, bounce, conversion. Break this into a few independent workstreams so different analysts could handle them in parallel, and return a concise analysis_summary.json.
```

### 360. D3_k983103_zh (domain=D3, difficulty=6)

```
请基于文件 roopacalistus__superstore__SampleSuperstore.csv 做一份面向业务的异常与离群点分析，重点围绕“明确数值规则下的异常识别”。数据里有 Ship Mode、Segment、Country、City、State、Postal Code、Region、Category、Sub-Category、Sales、Quantity、Discount、Profit 等字段，请你直接用这些真实列做分析，不要假设不存在的值。我要的是一份可落地给运营/BI团队的结论：先按统一规则找出异常订单，再拆解这些异常主要集中在哪些地区、品类、细分品类和客户分层，并判断这些异常是否更多来自高折扣、低利润、极端销售额或稀有类别。请把结果整理成 analysis_summary.json，内容至少包括异常定义、异常规模、Top 异常聚集维度、以及需要优先排查的业务信号。请按下面 4-6 个相互独立的分析轨道推进：1) 基于 Sales、Profit、Discount、Quantity 的明确阈值/IQR 异常订单识别；2) 按 Region/State/City 的异常聚集与偏离常规情况；3) 按 Category/Sub-Category 的稀有类别与极端值分析；4) 按 Segment/Ship Mode 的异常分布与结构差异；5) 异常与利润率/折扣率的关系验证；6) 输出可执行的排查优先级建议。
```

### 361. D3_k983126_en (domain=D3, difficulty=6)

```
Analyze the house_prices.csv dataset and build a correlation/driver analysis focused on which numeric fields move together and what the strongest rounded associations are. Please treat this like a BI investigation: first clean the obvious numeric-like fields, then quantify relationships between price, area, and inventory attributes, and finally summarize the most actionable drivers by property type and geography. Use the real columns in the file (Price (in rupees), Carpet Area, Super Area, Plot Area, Dimensions, Bathroom, Balcony, Car Parking, location, Status, Transaction, Furnishing, facing, Society). I want the work split into independent tracks so a small sub-team could run them in parallel, and I need a concise output I can hand to stakeholders.
```

### 362. D3_k983133_en (domain=D3, difficulty=6)

```
Using mashlyn__online-retail-ii-uci__online_retail_II.csv, do a BI-style driver analysis focused mainly on correlations and which numeric fields move together. Please treat this as a real retail transactions review using the actual columns Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, and Country. I want a compact but rigorous readout that covers: where Quantity and Price move together or against each other, how line value behaves, whether missing Customer ID rows look different from identified customers, which countries and stock codes most strongly associate with higher priced or higher quantity lines, and any notable patterns by time bucket. Please split the work so different people could handle the pieces independently, then return one concise summary file.
```

### 363. D3_k983469_en (domain=D3, difficulty=6)

```
Analyze the pipeline accidents dataset in usdot__pipeline-accidents__database.csv with a primary focus on correlation and driver analysis: identify which numeric fields move together, round correlations to 2 decimals, and surface the strongest associations. Please split the work into 4-6 independent tracks so it can be handled by separate analysts: (1) numeric-data quality and missingness among accident, release, injury, and cost fields; (2) correlation structure among the key numeric measures (releases, recovery, net loss, evacuations, injuries, costs); (3) which causes, pipeline types, or liquid types are associated with the largest releases or costs; (4) year-over-year shifts in the numeric drivers and how the correlations change over time; and (5) a short executive summary of the top associations and operational interpretations. Use only the real values in the file and keep all reported figures exact or rounded to 2 decimals where appropriate.
```

### 364. D3_k983694_zh (domain=D3, difficulty=6)

```
请基于数据文件 usdot__pipeline-accidents__database.csv 做一份面向管理层的事故集中度分析，重点围绕“排名与集中度（Top-N、总量占比、Pareto）”展开。请不要只做描述性统计，要把结论拆成可并行推进的 4-6 条分析线，并最终输出一份可直接用于汇报的 analysis_summary.json。重点关注以下方面：1）按事故发生频次和总损失分别找出最严重的 Top-N 事故原因类别/子类别，并计算它们占总体的份额；2）按州、运营商、管道类型/液体类型分别做集中度分析，识别是否存在少数主体贡献了大部分事故或损失；3）对死亡/伤害、火灾/爆炸、人员疏散等高风险结果做 Top-N 排名与集中度，看看是否高度集中在少数原因或少数州；4）把“事故次数集中度”和“损失金额集中度”进行对比，找出哪些维度是频次集中、哪些维度是损失集中；5）如果同一维度在不同指标上的排名差异很大，请标注出来，说明管理上应优先盯住哪里。请尽量用 80/20 或 Pareto 的方式说明：比如前 10% 的组别是否贡献了 50% 以上的事故/损失。所有结论都必须严格基于数据文件中的真实值。
```

### 365. D3_k983827_en (domain=D3, difficulty=6)

```
Using syedanwarafridi__vehicle-sales-data__car_prices.csv, I need a BI-style concentration analysis on vehicle sales: identify the top makes, models, states, and sellers by sales count and sellingprice contribution, quantify how much of total volume and total revenue they capture, and check whether pricing concentration differs from volume concentration. Please also break this into a few independent workstreams so we can review the ranking logic separately, and keep the analysis grounded in the actual columns year, make, model, trim, body, transmission, state, condition, odometer, seller, mmr, sellingprice, and saledate.
```

### 366. D3_k984048_zh (domain=D3, difficulty=6)

```
请基于文件 roopacalistus__superstore__SampleSuperstore.csv 做一份面向业务的异常与离群点分析，重点围绕“显式数值规则识别异常”来展开：例如按 Sales、Profit、Discount、Quantity 的极端值、IQR 离群点、负利润异常单、异常高折扣单、以及稀有类别/组合（Ship Mode、Segment、Region、Category、Sub-Category、State、City、Postal Code）的异常集中情况。请把分析拆成可并行的几条线：先做全局异常画像，再按 Region/State/Category/Sub-Category 分层看异常，再识别最极端的订单和最稀有的类别组合，再看异常是否集中在某些客户细分或运输方式上，最后给出可执行的业务解读与筛查规则。输出要能支持 BI 汇报，结论要尽量量化，明确说明阈值、命中条数、占比和代表性样本。
```

### 367. D3_k984471_en (domain=D3, difficulty=6)

```
Using the file janiobachmann__bank-marketing-dataset__bank.csv, I need a compact BI-style analysis focused on ranking and concentration in campaign performance. Please investigate which customer groups and contact patterns contribute most to deposit outcomes, with attention to top-N segments, share of total, and Pareto-style concentration. Break it into 4–6 independent tracks so different analysts can work in parallel: (1) top customer profiles by deposit rate and volume, (2) concentration of successful deposits across jobs/marital/education segments, (3) contact-channel and month rankings for deposit outcomes, (4) balance/duration/campaign behavior among the highest-contributing groups, and (5) any notable concentration from prior outcome and previous-contact history. Deliver a concise JSON summary that highlights the dominant segments, their share of total successes, and the most important ranking takeaways.
```

### 368. D4_g1104_en (domain=D4, difficulty=6)

```
I need a concise analysis brief from the four files in inputs/: articles.csv, edits.xlsx, translations.csv, and keywords.csv. Please produce two deliverables:

1. findings.md — a summary covering several independent threads: article counts by topic, body word count, duplicate title groups, edit records (including conflicts), translation coverage, keyword matches in titles, source distribution spread, and duplicate translation pairs. Also note any cross‑source conflicts or anomalies you find (e.g., duplicate titles across files, repeated edits, empty translations).
2. evidence.json — a small machine‑readable file with the key metrics for each of those threads.

Stick to objective numbers only, no subjective commentary. Treat these four files as the complete data set.
```

### 369. D4_g1176_zh (domain=D4, difficulty=6)

```
我需要你基于 `inputs/` 下的 5 个文件（`documents.csv`、`requirements.csv`、`document_metrics.csv`、`reviews.sqlite`、`brief.md`）帮我生成一份紧凑的跨文件核查报告。输出三个汇总文件：`summary.json`、`issues.csv` 和 `coverage.md`。对每份文稿做几项独立统计，再合并汇总——包括状态分布、空正文、超长标题、高链接数、重复文稿、规则覆盖情况以及审阅记录的关键指标。最终按违规严重度输出一个最多 5 条的问题清单。
```

### 370. D4_g1205_en (domain=D4, difficulty=6)

```
I need you to analyze the files in inputs/: articles.xlsx, reviews.xlsx, keyword_lexicon.csv, and feedback.xlsx. Produce a Markdown analysis brief (findings.md) and a compact evidence table (evidence_table.csv or .md) that covers key stats, data quality issues (like duplicates, missing titles, orphan reviews), keyword coverage by track, and feedback metrics. Also reconcile any cross‑source conflicts or anomalies you find.
```

### 371. D4_g1362_en (domain=D4, difficulty=6)

```
I need a clean decision brief from content_items.csv, revisions.xlsx, localization_segments.xlsx, document_ref_map.csv, and reference_catalog.json. Rank the three publishers and tell me which one to prioritize for the next content sprint using this score: 0.45*publish_rate + 0.25*revision_intensity + 0.20*reference_coverage - 0.10*localization_risk. Use the published window 2025-02-04 through 2025-03-08 UTC inclusive, count only rows with status='published', treat duplicate doc_id/title/body rows as one document, and ignore revisions or localization segments that point to missing doc_id values. Localization risk is the share of segments with qa_flag=1 or target_chars<0, reference coverage is docs with at least 2 unique refs from the closed set {guideline, policy, kb, help}, and revision intensity is total revisions divided by published docs. Deliver one brief markdown file with the ranked recommendation and the supporting numbers, plus a compact JSON with the headline aggregates.
```

### 372. D4_g4_zh (domain=D4, difficulty=6)

```
我们正在做内容审核与本地化质量评估，需要你基于以下文件帮我完成一份汇总报告：

- inputs/source_articles.csv
- inputs/target_keywords.xlsx
- inputs/localization_checks.json
- inputs/editorial_guidelines.md

请输出三个结果文件：
1. 一个 JSON 汇总文件，包含所有关键指标（如重复文章数、摘要问题统计、关键词覆盖率等）；
2. 一个 CSV 明细表，列出触发了任何规则的文章；
3. 一个 Markdown 说明，简要描述你采用的计算口径。

具体需要统计的内容包括：检查正文和摘要是否有完全相同的文章对、摘要长度是否合理（太长或太短或缺省）、按主题统计关键词缺失情况以及对应的平均摘要词数、汇总所有触发规则的文章总数、找出关键词缺失最多的主题，同时还要根据 localization_checks.json 统计缺失摘要和超出字数上限的检查条目。请按常规方法进行处理，不需要逐一列出公式。
```

### 373. D4_g971_en (domain=D4, difficulty=6)

```
I need an analysis brief based on four files: articles.xlsx, reviews.tsv, citations.jsonl, and audit_log.txt. The goal is to assess data quality and consistency across these sources. Please cover four separate areas: article inventory and duplication, review log metrics, citation integrity, and audit log anomalies. Then synthesize the findings into a single brief (findings.md) with a reconciliation section and a short conclusion. Also provide a supporting evidence table (evidence_table.csv) with only the rows needed to back up the brief. Use objective, computable metrics where possible—no subjective judgments. The specific rules for dates, duplicates, and blank values are handled in your standard process.
```

### 374. D4_g980281_en (domain=D4, difficulty=6)

```
Review inputs/news_main.xlsx, inputs/glossary.csv, and inputs/rules.json and produce one concise findings brief in Markdown. I need four parallel lines of analysis: track coverage, duplicate/near-duplicate handling, length/compliance checks, and entity coverage against the glossary. Reconcile anything that differs across the files, call out the checked anomalies, and keep the report to a single deliverable named findings.md.
```

### 375. D4_g980454_zh (domain=D4, difficulty=6)

```
我需要你结合 inputs/news_report.xlsx 和 inputs/translation_audit.xlsx 做一份决策简报，判断这批内容里哪些新闻素材更适合优先进入多语言发布流程，并顺手把翻译请求和审计日志里的异常情况一起核对清楚，最后给我一个按优先级排序的结论文件。
```

### 376. D4_g980784_en (domain=D4, difficulty=6)

```
I need a single findings brief that compares the four source files in this folder and pulls the main facts together for an editorial handoff. Please check the workbook against the index, metadata, and notes, then write a concise markdown brief that separates the main threads, calls out any overlaps or contradictions across sources, and highlights the data quality issues that matter for publication planning.
```

### 377. D4_g980964_zh (domain=D4, difficulty=6)

```
我这边要把一批内容素材整理成一份可交付的分析简报，方便给编辑、翻译和审核一起看。请同时参考 inputs/master_docs.xlsx、inputs/localization_map.xlsx、inputs/review_notes.csv 和 inputs/big_event_log.txt，最后输出一份 findings.md，按来源分开说明，再把四份材料之间能互相印证或冲突的地方单独列出来。
```

### 378. D4_g981541_zh (domain=D4, difficulty=6)

```
需要你把这三份材料整理成一份简短的研究简报，重点看新闻文章、评论和案件清单之间能对上的地方，以及哪里有口径不一致。最后只要一份 findings.md，内容要把每条分析线的结果和跨来源的对照结论写清楚，便于我直接拿去汇报。
```

### 379. D4_g981588_zh (domain=D4, difficulty=6)

```
我们要尽快把这批内容资料整理成一份可给业务和编辑一起看的分析 brief，重点是把来源里的关键信息串起来，顺手把明显的重复、链接、缺字段和长度问题说清楚。请基于 inputs/content_dataset.xlsx 和 inputs/review_memo.pdf，输出一份 findings.md。
```

### 380. D4_g981742_zh (domain=D4, difficulty=6)

```
我要把这三份资料整理成一页可交付的分析简报，给内容团队做后续分发前的核对：articles.xlsx、issues.xlsx、keywords.json。请重点从不同来源里找出可直接汇报的结论，并把重复、缺失和关键词覆盖这些需要协调的问题单独说明，最后输出一份 findings.md。
```

### 381. D4_g984_zh (domain=D4, difficulty=6)

```
分析 inputs/ 下的三个文件—— documents.xlsx（含文章正文和摘要）、required_entities.xlsx（每篇文档应含的实体及类型）和 config.json（配置参数）—— 按我们的标准方法完成以下分析并输出四个文件到输出目录：

- report1_metrics.csv：每篇文档的 word_count、char_count(仅字母)、sentence_count、avg_words_per_sentence、ARI、summary_word_count 以及摘要字数是否在 10–25 词范围内。
- report2_duplicates.csv：摘要间近似重复对（满足 config.json 中 duplicate_similarity_threshold），含 doc_id1、doc_id2 和 similarity，按相似度降序。
- report3_entity_coverage.csv：每篇文档的所需实体数、在正文中发现数、在摘要中发现数，以及 coverage_rate_doc（found_in_doc / num_required）。
- synthesis_report.json：汇总 total_docs、avg_ARI、summary_len_issues、total_duplicate_pairs、avg_entity_coverage、zero_coverage_docs（列表）、top5_ARI（doc_id 及 ARI）、top5_duplicates（doc1、doc2 及 similarity）、total_char_count、total_sentence_count。

全部用自动化方式处理，结果精确可复现。
```

### 382. D4_k982101_zh (domain=D4, difficulty=6)

```
请基于文件 `chanemo__weibo-hot-searchlabeled__weibo-hot-search-labeled.csv` 做一版给内容/编辑团队看的热点标签分析，重点围绕“不同标签之间的表现差异”和“哪些细分标签最不一样”展开。请直接用现成字段：`日期`、`热搜词条`、`链接`、`标签（时政、科技、科普、娱乐、体育、社会讨论/话题、时事、经济）`。我想要一份能支持选题分发和栏目策略调整的分析，不要泛泛描述，务必给出可落地的分组对比结果、差异最大的标签对、以及能反映内容结构的细分结论。请把结果整理成一个 `analysis_summary.json` 风格的输出，核心围绕以下几条独立分析线并行推进：1）按标签的量级和占比对比；2）按日期维度看各标签出现频次的均值/波动差异；3）按热搜词条长度或内容特征比较不同标签的词条风格差异；4）找出标签之间差距最大的指标（例如占比、日均热度、重复/独立词条比例等）；5）识别最能代表每个标签的高频词条或最典型词条；6）如果有明显的异常日期或集中爆发现象，也请单独指出并解释它和标签结构的关系。
```

### 383. D4_k982143_zh (domain=D4, difficulty=6)

```
请基于文件 sentinel3734__neurologica-blog-posts__neurologica_articles.csv 做一份面向内容/编辑分析的分群对比报告，重点看不同类别之间的表现差异，找出“哪些分组明显更高/更低、差距最大在哪里”。请直接使用字段 publication_date、title、author、categories、text、url，不要改动原始数据。我要你把分析拆成几条彼此独立的线并并行跑：先看 categories 的内容分布和文章量，再看按类别分组的文本长度与发布时间节奏，再看作者层面的发文量/覆盖类别差异，再看标题与正文长度在不同类别中的差别，最后把最极端的高低组和最大 gap 归纳出来。输出面向忙碌编辑团队，结论要尽量落到“哪个类别/作者更高、差多少、是不是集中在少数组”。
```

### 384. D4_k982293_zh (domain=D4, difficulty=6)

```
请基于文件 kimjihoo__coronavirusdataset__SeoulFloating.csv 做一份面向内容/编辑运营的分析简报，重点看“哪些人口与时间变量会和浮动人口 fp_num 一起变化”，也就是相关性与驱动因素分析。请把分析拆成几个彼此独立的轨道：1）整体数据概览与字段质量检查；2）按 birth_year、sex、hour、date 的浮动人口差异与峰谷；3）各数值字段之间的相关性、分组后均值/中位数差异，以及最强正/负关联；4）按 province/city 的区域分布与高低值城市；5）找出在不同年龄段、性别、时段下 fp_num 最容易同时抬升或回落的组合；6）输出给编辑团队可直接使用的结论：哪些因素最像“驱动项”，哪些更像背景噪声。请注意只使用真实数据，不要臆造任何数值，所有结论尽量给出 rounded correlations（保留 2 位小数）和可复核的分组统计。最后请生成一个简洁的 analysis_summary.json 结构化结果，便于后续写稿。
```

### 385. D4_k982384_en (domain=D4, difficulty=6)

```
Using bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv, analyze the BBC news article inventory for editorial/content patterns with a focus on correlation and driver analysis. I want a practical breakdown of what tends to move together in the dataset: publication timing, article text length proxies, domain/section mix from the links, and any strong associations between numeric measures. Please decompose this into independent workstreams so different analysts could work in parallel, and keep the final output tight and decision-oriented: identify the biggest correlation drivers, any section/topic clusters that behave differently, and a few sanity-check stats I can use to trust the findings.
```

### 386. D4_k982393_zh (domain=D4, difficulty=6)

```
请基于文件 chanemo__weibo-hot-searchlabeled__weibo-hot-search-labeled.csv 做一份面向内容/编辑分析的定量诊断，重点看“分布与阈值分层”：比如各标签在不同日期区间的热搜词条数量、超过/低于业务阈值后的占比、按分位数切桶后的结构变化、以及头部/尾部词条对整体量的贡献。请直接使用表里的真实字段：日期、热搜词条、链接、标签（时政、科技、科普、娱乐、体育、社会讨论/话题、时事、经济）。我想要你把结果整理成一个可复用的 analysis_summary.json，包含可执行结论和关键口径。请至少拆成 4-6 个彼此独立的分析轨道，分别回答：1）总量分布与阈值 cohort；2）按标签的结构和头尾占比；3）按日期的日粒度波动与高低日分层；4）按热搜词条出现频次的长尾/头部贡献；5）按标签在不同频次桶中的 mix 变化；6）如有必要补充异常日期或极端词条的定位。不要做预测或可视化，只做确定性统计。
```

### 387. D4_k982402_en (domain=D4, difficulty=6)

```
Using sanjidh090__resultpf__bd_eng_news_daily.csv and its real columns (title, text, publish_date, urls, news_collection_time, publisher), run a content/editorial analytics review focused mainly on segment comparison across categorical groups. I need a practical breakdown of which publishers differ most in article volume, article length, publication timing, and title patterns, plus any clear gaps between segments. Please structure it so a small team could split the work into independent tracks and then combine the findings into one concise summary with supporting counts, means/medians, and top/bottom group comparisons.
```

### 388. D4_k982506_en (domain=D4, difficulty=6)

```
Using sanjidh090__resultpf__bd_eng_news_daily.csv, do a content/editorial analytics deep-dive focused mainly on temporal trend analysis across publish_date. I need you to segment the newsroom output by publisher and over time, identify periods of acceleration/decline in volume, compare publisher-level trend patterns, and flag any timing-related data quality issues. Please use the real columns title, text, publish_date, urls, news_collection_time, and publisher, and keep the work grounded in what is actually in the file.
```

### 389. D4_k982546_en (domain=D4, difficulty=6)

```
Using sanjidh090__resultpf__bd_eng_news_daily.csv, build an editorial/content analytics brief focused mainly on ranking and concentration. I need you to identify which publishers and topics dominate the dataset, how concentrated the coverage is among the top groups, and whether that concentration differs across publication timing. Work from the real columns only: title, text, publish_date, urls, news_collection_time, publisher, and the Unnamed: 0 index. Please structure it as a multi-part analysis that could be split across a small team, then summarize the findings in analysis_summary.json. Keep the analysis grounded in the actual data, with top-N rankings, share-of-total calculations, and Pareto-style concentration measures.
```

### 390. D4_k982556_en (domain=D4, difficulty=6)

```
Using kuberiitb__indian-news-articles__historic_articles.csv, run a content/editorial analytics review focused mainly on segment comparison across categorical groups: compare engagement proxies and content characteristics across source, category, and publication timing segments, and identify the biggest gaps between segments. I need a practical readout of where the dataset differs most by group so we can spot editorial patterns and outliers. Please use the real columns source, category, link, author, published_at, header, subheader, and content; break the work into independent tracks so different analysts can work in parallel, and summarize the most material differences with clear group-level rates/means and gap comparisons.
```

### 391. D4_k982658_en (domain=D4, difficulty=6)

```
Using sanjidh090__resultpf__bd_eng_news_daily.csv, I need a content/editorial analytics readout focused mainly on ranking and concentration. Please analyze the articles using the real columns title, text, publish_date, urls, news_collection_time, and publisher. I want a practical report that tells me where the volume is concentrated, who dominates the corpus, whether a small set of items accounts for most of the text volume, and how publishing intensity changes over time. Please break it into a few independent tracks so different people could work on them in parallel, and keep the output concise but decision-ready.
```

### 392. D4_k982736_en (domain=D4, difficulty=6)

```
Using the file bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv with the columns title, pubDate, guid, link, and description, run a content/editorial analytics review focused mainly on distribution and threshold cohorts. I need this broken into a few independent workstreams so different people could work in parallel: quantify how article volume is distributed over time and across sections, build threshold-based cohorts using article metadata and text length, compare mix shares for the major news domains, and check whether the article-length distribution differs by section and by publication timing. Please surface the key counts, shares, and quantile bucket splits in a compact analysis summary rather than a large table.
```

### 393. D4_k982791_zh (domain=D4, difficulty=6)

```
请基于文件 sentinel3734__neurologica-blog-posts__neurologica_articles.csv 做一份面向内容/编辑分析的综合报告，重点围绕“排名与集中度”展开：先找出最常出现的作者、分类、标题关键词和发布时间段，评估头部作者/头部分类/头部月份对全部文章的占比与帕累托集中度；再比较不同作者、分类和时间段的内容长度、标题长度与文本长度差异；同时识别是否存在明显的重复标题、极端长文和缺失值问题。请把结果整理成可交付的 summary，并明确说明哪些头部群体贡献了大部分内容，哪些维度高度集中，哪些维度比较分散。文件中可用字段有 publication_date、title、author、categories、text、url。
```

### 394. D4_k982952_en (domain=D4, difficulty=6)

```
Using `bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv`, I need a content/editorial analytics readout focused on ranking and concentration. Please analyze the BBC article corpus using the available columns (`title`, `pubDate`, `guid`, `link`, `description`) and answer these questions in a way I can hand to editors. I want a clear top-N and Pareto-style view of where attention is concentrated, plus a few supporting cuts that help explain whether the concentration is driven by a small number of time periods, topics, or recurring article patterns. Please keep the work split into independent tracks so different analysts can work in parallel, and summarize the results in `analysis_summary.json`.
```

### 395. D4_k982993_zh (domain=D4, difficulty=6)

```
请基于文件 chanemo__weibo-hot-searchlabeled__weibo-hot-search-labeled.csv（字段：日期、热搜词条、链接、标签（时政、科技、科普、娱乐、体育、社会讨论/话题、时事、经济））做一份偏内容/编辑分析的专题报告，重点放在“相关性与驱动因素”上：先看不同标签在时间上的同步/分化，再看哪些标签组合和哪些时间窗口会一起升降，找出热搜内容标签之间最强的正负相关，并识别可能的内容驱动信号。请把分析拆成可并行的几条线：1）整体标签分布与集中度；2）按日期汇总后的标签相关矩阵与Top关联；3）高频热词/词条的标签联动；4）按月份或周度的趋势共振；5）异常高密度日期或标签簇；6）对“社会讨论/话题”“时事”“娱乐”“经济”等核心标签做驱动对比。最后输出一份适合编辑会讨论的简明结论和可执行建议。
```

### 396. D4_k983028_en (domain=D4, difficulty=6)

```
Using kuberiitb__indian-news-articles__historic_articles.csv, I need a compact editorial analytics readout focused on correlation and driver analysis. Please treat this as a newsroom/content performance audit on the real columns source, category, link, author, published_at, header, subheader, and content. I want you to identify which measurable text/date features move together, where the strongest associations are, and what seems to drive article length and publication patterns. Please split the work into 4-6 independent tracks so separate analysts can work in parallel: one track on text-length relationships, one on publication timing patterns, one on source/category concentration and co-movement, one on missing-data and data-quality drivers, and one on headline/subheader/content linkage. Keep it grounded in deterministic pandas-style counts, means, medians, and rounded correlations only.
```

### 397. D4_k983032_en (domain=D4, difficulty=6)

```
Using the file bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv, I need an editorial/content analytics readout focused mainly on segment comparison across categorical groups. Please treat title, pubDate, guid, link, and description as the available fields. Break the work into a few independent tracks so they can be done in parallel: compare publishing volume and average story length by year/month and by source/domain; identify the biggest gaps between categories such as sports vs news and any other obvious content segments you can derive from the URLs; look for differences in article timing and day-of-week patterns across those segments; surface the most frequent topics/keywords by segment; and flag any outlier or unusually long/short items that may explain the differences. I want a concise analysis summary with the most important segment-level gaps and a few concrete examples.
```

### 398. D4_k983128_en (domain=D4, difficulty=6)

```
Using bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv with the columns title, pubDate, guid, link, and description, please do a content/editorial analytics pass focused mainly on distribution and threshold cohorts. I want to understand how article volume is distributed over time and across article types, where the concentration sits versus business thresholds, and how mix shifts across quantile buckets. Please break it into separate workstreams so different analysts can run them independently: time-based volume/cohort analysis, threshold-bucket analysis on article length proxies, content-type mix analysis from titles/descriptions, source/path segmentation from links, and outlier/exception review for unusually short or long descriptions. Summarize the findings in analysis_summary.json.
```

### 399. D4_k983206_zh (domain=D4, difficulty=6)

```
请基于文件 thebumpkin__10400-classic-hits-10-genres-1923-to-2023__ClassicHit.csv 做一份面向内容/编辑分析的深度复盘，重点围绕时间趋势与阶段变化来展开。我要你把这份 1500 首经典歌曲的数据拆成几个彼此独立的分析轨道：先看 1923–2023 年之间不同年代的收录量、年均热门度（Popularity）和增长/回落节奏；再看各流派（Genre）在不同时期的占比迁移，以及哪些流派更早/更晚进入样本；再看歌曲时长、舞曲性（Danceability）、能量（Energy）、速度（Tempo）、情绪（Valence）这些内容特征是否随时间发生结构性变化；再找出近十年与早期年代在音频特征和热门度上的差异；最后补充几个适合编辑选题的“异常/极值”观察，比如最长/最短、最安静/最响、最热门/最冷门的歌曲各出现在哪些年份和流派里。请直接给出可执行的分析结论草稿，并确保所有结论都能追溯到 dataframe 里的真实值。不要画图，重点输出可核验的统计结果。
```

### 400. D4_k983245_en (domain=D4, difficulty=6)

```
Using wardabilal__spotify-global-music-dataset-20092025__track_data_final.csv, build a content/editorial analytics readout focused mainly on correlation and driver analysis across the track, artist, and album fields. I want to know which numeric signals move together, which relationships are strongest after rounding correlations to 2 decimals, and what editorial levers look most associated with track popularity. Please split the work into 5 independent tracks: 1) data quality and coverage checks on the numeric/editorial fields, 2) pairwise correlation analysis among track_popularity, track_duration_ms, artist_popularity, artist_followers, track_number, and album_total_tracks, 3) driver-style slicing of popularity by explicit vs non-explicit and album_type, 4) artist-scale effects using followers/popularity buckets, and 5) a short editorial implications summary that prioritizes the strongest positive and negative associations.
```

### 401. D4_k983343_en (domain=D4, difficulty=6)

```
Use the file thebumpkin__300-world-music-tracks-with-spotify-data__WorldHits.csv and build an editorial-analytics readout focused on correlation and driver analysis across the numeric fields in this dataset. I want you to identify which audio features move together, which features are most associated with Popularity, and whether those relationships differ by broad track characteristics like year and mode. Please keep it practical for content planning: summarize the strongest rounded correlations, call out the top positive and negative associations with Popularity, and segment the analysis into a few independent tracks so different analysts can work in parallel. Also include a small set of deterministic validation checks tied to the actual data values.
```

### 402. D4_k983345_en (domain=D4, difficulty=6)

```
Using the dataset in inputs/thedevastator__youtube-trending-videos-dataset__youtube.csv, I need a content/editorial analytics readout centered on distribution and threshold cohorts. Please analyze how videos split above vs below key performance cutoffs, how those cohorts differ by country, category, and time frame, and how the mix changes across quantile buckets of views and engagement. Use the real columns in the file, especially publish_country, category_id, time_frame, views, likes, dislikes, comment_count, comments_disabled, ratings_disabled, and video_error_or_removed. I’m mainly interested in counts, cohort shares, and simple mix comparisons that help editorial teams decide what to prioritize. Decompose the work into independent tracks so they can be handled in parallel, and summarize the findings in a compact JSON deliverable.
```

### 403. D4_k983354_en (domain=D4, difficulty=6)

```
Using the file bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv, build a content/editorial analytics summary focused mainly on segment comparison across categorical groups. I need you to compare how the article mix differs by segment using the available columns title, pubDate, guid, link, and description. Please break the work into a few independent tracks so they can be done in parallel: compare content volume by year and by month, compare article mix by high-level topic/category inferred from the title/description, identify the biggest gaps between segments in average article length and posting cadence, compare how often different segments mention recurring entities/themes in the text, and flag any unusual concentration of articles in particular categories over time. The output should be a concise analysis summary JSON with the biggest cross-segment differences, not a full table dump.
```

### 404. D4_k983374_en (domain=D4, difficulty=6)

```
Using sentinel3734__neurologica-blog-posts__neurologica_articles.csv, build a content/editorial analytics review focused mainly on temporal trend analysis. I want a compact summary of publishing cadence and topic mix over time, with period-over-period comparisons, spikes/dips, and any notable shifts in authorship or category coverage. Please use the publication_date, title, author, categories, text, and url columns. Break the work into independent tracks so it can be handled in parallel, and produce a concise analysis_summary.json.
```

### 405. D4_k983472_en (domain=D4, difficulty=6)

```
Using the file roman6335__13000-itunes-podcasts-april-2018__poddf.csv and its columns Name, Rating_Volume, Rating, Genre, and Description, run a content/editorial analytics review focused mainly on temporal or trend-style analysis over the dataset’s sequence patterns. I want a practical readout that helps us understand how audience reception changes across the catalog over the listing order, including where ratings and rating volume appear to rise or fall, which genres are most stable versus most volatile, and whether newer/earlier entries in the sequence differ meaningfully in quality or engagement. Please break this into several independent workstreams so different analysts can work in parallel, then summarize the findings in one compact JSON deliverable.
```

### 406. D4_k983493_zh (domain=D4, difficulty=6)

```
请基于文件 eliasdabbas__search-engine-results-flights-tickets-keywords__flights_tickets_serp2019-10-01.csv 做一份面向内容/编辑分析的多维诊断，重点围绕时间/序列字段的趋势变化来判断搜索结果生态是否稳定、是否有阶段性波动，以及不同查询词的结果质量表现是否随时间变化。请直接使用现有字段 searchTerms、rank、title、snippet、displayLink、link、queryTime、totalResults、searchTime、formattedSearchTime、formattedTotalResults、cseName、gl 等做分析，不要改写数据。我要你拆成 4-6 个彼此独立的分析轨道，适合并行给多个小助手分别跑，然后最后汇总成一份 analysis_summary.json。重点帮我看：1）整体数据是按什么时间跨度分布的，是否存在明显的日期聚类；2）不同 searchTerms 在各日期的覆盖是否均衡，是否有某些词在后期/前期明显增减；3）搜索结果质量和结构指标（如 rank、totalResults、searchTime）是否随时间变化；4）不同搜索词对应的结果来源域名结构是否随时间漂移；5）前几名结果的标题/摘要长度或可读性是否在时间上发生变化；6）如果能发现异常日期、异常搜索词或异常结果来源，请单独标出来并说明其趋势特征。请给我可执行的结论导向分析，不要只做静态统计。
```

### 407. D4_k983495_zh (domain=D4, difficulty=6)

```
请基于文件 glushko__seth-godins-blogs-dataset__seth-data.csv（字段包括 id、url、title、content_plain、content_html、stars、publication-date、referral-url）做一份面向内容/编辑分析的异常与离群审计，重点围绕“显式数值规则”来找出值得人工复核的极端样本。请把分析拆成 4-6 条彼此独立的轨道并行推进：1）stars 的极端值与分布异常（例如 IQR、分位数、极端高/低值）；2）publication-date 的时间异常（例如按年份/月份的稀有日期、非常规集中）；3）文本长度异常（content_plain 与 content_html 的字符长度/长度比异常）；4）标题异常（特别短、特别长、重复/近重复标题、稀有标题模式）；5）referral-url 的异常来源模式（空值、极少见域名或路径结构）；6）跨字段组合异常（例如高 stars 但超短内容、低 stars 但超长内容等）。最后输出一个可供编辑团队复核的异常清单思路，并总结哪些规则最能抓到“可能不正常”的文章。请同时回答下面的定量检查问题。
```

### 408. D4_k983936_en (domain=D4, difficulty=6)

```
Using inputs/eshummalik__socialbuzz-sentiment-analytics__sentimentdataset.csv, run a content/editorial analytics review focused mainly on anomaly and outlier detection using explicit numeric rules. Please split the work into 5 independent tracks: (1) identify extreme engagement posts using numeric thresholds on Retweets and Likes, (2) detect temporal anomalies by unusually high/low posting concentration across Year/Month/Day/Hour, (3) find rare or suspicious categorical patterns in Sentiment, Platform, and Country, (4) flag text-level outliers such as unusually long/short posts and unusual hashtag usage, and (5) summarize which combinations of sentiment/platform/country are most associated with numeric outliers. I need a concise executive summary plus a machine-readable analysis_summary.json with the key flagged records, thresholds used, and the top anomalous segments. Use the real columns exactly as named, and keep everything grounded in deterministic counts and aggregates from the dataset.
```

### 409. D4_k984130_en (domain=D4, difficulty=6)

```
Using abdallahwagih__books-dataset__data.csv, run a content/editorial analytics review focused mainly on temporal trends. I want a practical readout on how the catalog changes over published_year: identify release-volume shifts over time, how average_rating and ratings_count move year to year, whether page length is trending up or down, and which categories/authors are associated with the strongest and weakest recent-year performance. Please split the work into independent tracks so separate sub-analysts can handle the time trend, rating/engagement, catalog mix, and content-length angles independently, then synthesize the findings into a concise analysis_summary.json.
```

### 410. D4_k984194_zh (domain=D4, difficulty=6)

```
请基于文件 thedevastator__books-sales-and-ratings__Books_Data_Clean.csv 做一份偏“内容/编辑分析”的分群对比报告，重点看不同分类之间的差异、差距最大的分组，以及这些差异在销量和评分上的体现。请直接围绕现有字段分析，不要改数据。重点参考列包括 Publishing Year、Author_Rating、genre、language_code、Publisher、Book_average_rating、Book_ratings_count、gross sales、publisher revenue、sale price、sales rank、units sold。希望你把结果整理成一份可给编辑和选品团队看的结论，并输出 analysis_summary.json。请特别回答：不同作者评级、体裁、语言、出版社之间，平均销量、平均收入、平均评分、平均定价、平均销量排名分别有什么差异，哪几个分组的差距最大，哪些组合表现最好/最差，是否存在高评分但低销量或低评分但高销量的典型分群。
```

### 411. D4_k984520_zh (domain=D4, difficulty=6)

```
请基于文件 mihikaajayjadhav__books-dataset-15k-books-across-100-categories__google_books_dataset.csv 做一份内容/编辑分析，重点围绕“排名与集中度”来判断这批图书在选题、语言、出版社和定价上的头部集中情况。请优先回答：哪些分类、出版社、作者和语言最集中？头部项目是否贡献了大部分条目或销售价值？另外请结合 ratings_count、average_rating、page_count、published_date、buyable 和 list_price 做几个切面验证，看看高频/高价值内容是否也更受好评、更长篇幅、或更偏向某些年份与语言。最后请把结论整理成适合编辑和选品团队阅读的结构化摘要。
```

### 412. D4_k984533_zh (domain=D4, difficulty=6)

```
请基于文件 thebumpkin__300-world-music-tracks-with-spotify-data__WorldHits.csv 做一份面向内容/编辑团队的分析，重点围绕“哪些音频特征与歌曲热度/可编辑性最相关、哪些特征彼此高度相关”。请直接用表里的真实字段分析，不要臆造。希望你把结论拆成几个独立部分：先做数据概览和质量检查；再做数值特征之间的相关性与Top关联项；再看 Popularity 与各音频特征（如 Danceability、Energy、Acousticness、Instrumentalness、Speechiness、Valence、Tempo、Loudness、Duration）的驱动关系；再比较年份维度的变化趋势与相关结构是否变化；最后补一个按 Artist/Album 的编辑视角总结（比如哪些艺人/专辑在“更舞曲化/更高能量/更高人声性”上更突出）。输出时请给出可执行的结论、关键数字（相关系数请四舍五入到2位）、以及适合编辑决策的简短解读。文件中列包括 Track, Artist, Album, Year, Duration, Time_Signature, Danceability, Energy, Key, Loudness, Mode, Speechiness, Acousticness, Instrumentalness, Liveness, Valence, Tempo, Popularity。
```

### 413. D4_k984629_en (domain=D4, difficulty=6)

```
Using `inputs/samithsachidanandan__1000-most-trending-youtube-videos__top-1000-trending-youtube-videos.csv`, analyze the fixed 1000-row YouTube trending dataset with columns `rank`, `Video`, `Video views`, `Likes`, `Dislikes`, `Category`, and `published`. I need a content/editorial anomaly audit focused on explicit numeric rules: parse the comma-formatted metric columns, identify outlier videos and categories by view volume, engagement rates, missing/zero reactions, rare categories, publication-year extremes, rank-vs-performance mismatches, and duplicate-title issues. Keep the tracks independent so different analysts can work in parallel, and summarize the final findings in `analysis_summary.json` with clear thresholds, counts, and short ranked lists only.
```

### 414. D4_k984681_en (domain=D4, difficulty=6)

```
Using the file `thedevastator__books-sales-and-ratings__Books_Data_Clean.csv`, build a content/editorial analytics readout focused mainly on ranking and concentration. I want to know where the catalog is most concentrated by sales, ratings, authors, publishers, genre, and language, and whether a small set of titles or creators drives most of the value. Please use the columns `Book Name`, `Author`, `Author_Rating`, `Book_average_rating`, `Book_ratings_count`, `genre`, `gross sales`, `publisher revenue`, `sale price`, `sales rank`, `Publisher `, `units sold`, `Publishing Year`, and `language_code`. Break it into separate workstreams so different analysts could work independently, and make sure each workstream answers a distinct concentration question rather than repeating the same summary.
```

### 415. D4_k984820_en (domain=D4, difficulty=6)

```
Using paradisejoy__top-hits-spotify-from-20002019__songs_normalize.csv, do a content/editorial analytics pass focused mainly on correlation and driver analysis across the numeric fields. I need you to identify which audio features move together, which features are most associated with popularity, and where the strongest positive/negative relationships are. Please also segment the findings where useful by explicit vs non-explicit tracks, and by year bands, so I can turn it into editorial guidance. Use the real columns in the file: artist, song, duration_ms, explicit, year, popularity, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, genre. Keep the work practical: summarize the strongest rounded correlations, note any surprising pairings, and give me a compact take on what seems to drive popularity in this dataset.
```

### 416. D4_k984849_en (domain=D4, difficulty=6)

```
Using rishidamarla__podcasts-episodes-20072016__shows.csv, do a content/editorial analytics review focused mainly on ranking and concentration. I want to know which shows, categories, and languages dominate the catalog, how concentrated the catalog is in the top groups, and whether a small number of feeds or topics account for a disproportionate share of shows. Please work only from the real columns in the file (especially title, feed_url, category, subcategory, language, explicit, created_at, last_build_date) and return a concise analysis summary.json with ranked findings, concentration metrics, and a brief editorial interpretation. Break the work into independent tracks so different agents could handle them in parallel.
```

### 417. D4_k984949_en (domain=D4, difficulty=6)

```
Use the file dhritimanchakrabarty__podcasts__train.csv and build a content/editorial analytics readout focused mainly on temporal and sequence trends. I want a compact but rigorous analysis of how episode characteristics change over the episode sequence and across time-related features: Episode_Number, Is_Weekend, SinWeekday/CosWeekday, SinTime/CosTime, and the episode-length encoding fields. Please also connect those temporal patterns to editorial drivers like Ad_Density, Number_of_Ads_0/1/2/3, Has_Guest, Guest_Popularity_percentage, Host_Popularity_percentage, Sentiment_Numeric, and genre mix. Break it into several independent workstreams so different analysts can work in parallel: one on episode-number trend and period-over-period change, one on weekday/weekend scheduling, one on length/ad-load evolution, one on guest and popularity interactions over time, and one on genre-specific temporal differences. Summarize the key findings in a concise analysis_summary.json, with any notable shifts, top segments, and correlations that help explain how editorial choices evolve over the series.
```

### 418. D4_k984971_zh (domain=D4, difficulty=6)

```
请基于文件 chhavidhankhar11__amazon-books-dataset__Books_df.csv（字段包括：Title, Author, Main Genre, Sub Genre, Type, Price, Rating, No. of People rated, URLs）做一份面向内容/编辑决策的分层分析，重点看不同类别分组之间的表现差异：哪些主类目/子类目/类型组合的评分更高、哪些更低、差距最大在哪里，以及这些差异是否同时伴随样本量差异。请把结果拆成可并行推进的几个分析轨道，并最终输出一个适合给编辑团队阅读的精简结论摘要，重点说明“哪里值得加码、哪里需要谨慎”。
```

### 419. D5_g980330_en (domain=D5, difficulty=6)

```
Analyze the provided audit snapshot and produce a concise triage report. Identify the highest-signal issues across code, tests, and configuration, and summarize which items are confirmed by the supplied artifacts.
```

### 420. D5_g980417_zh (domain=D5, difficulty=6)

```
你正在审计一个混合型 Python 代码库与配置集。请基于提供的代码快照与说明，分析是否存在与以下三个种子相关的问题：1) RenameModel 在 db_table 已存在时应为 noop；2) JUnit XML testsuite 缺少 hostname/timestamp 元数据；3) QuerySet.only() 与 select_related() 在反向 OneToOne 关系上的交互异常。

请输出 2-3 个交付物：
1. 问题摘要（按优先级排序）
2. 可执行的验证思路/检查点
3. 风险与影响评估

tool_target: 代码库/日志联合审计
subanalyses_hint: 关注代码路径、配置安全性、元数据完整性和边界条件。
```

### 421. D5_g980423_zh (domain=D5, difficulty=6)

```
请基于输入文件 codebase_audit_bundle.xlsx 做一次代码库/日志联合审计，最后输出一个简洁的汇总报告文件。
- 先分别看代码审计日志、测试日志和配置审计三块内容，再合并成统一结论。
- 重点整理：三条真实种子问题的覆盖情况、测试失败归因、以及 prod 配置风险。
- 报告里只要保留关键发现、数量汇总和最终整改建议，不要展开成逐行明细。
```

### 422. D5_g980518_zh (domain=D5, difficulty=6)

```
我们刚刚完成了一个为期两周的代码审计项目，涉及VisioAnalytics系统的两个核心模块（A和B）。
测试日志和源代码都放在 inputs/ 目录下了，还有一份安全政策PDF。
请帮助我整合并行分析的结果，最终给出一个优先级排序的修复建议（recommendation.json）。
具体来说，我需要知道：
1. 静态审查发现多少危险调用？
2. 安全风险有哪些（对照政策PDF）？
3. 测试日志中有多少失败？与种子问题相关的失败是否仍然出现？
4. 配置中是否存在不安全的设置？
请完成所有分析后，输出一个 recommendation.json 文件，包含修复优先级和关键数量即可。
```

### 423. D5_g980583_zh (domain=D5, difficulty=6)

```
这次上线前需要把一个小型 Django 审计包先过一遍，避免把已知风险带进发布。请根据这三个输入文件 audit_issues.xlsx、test_logs.xlsx、config_and_deps.xlsx 做一次综合审计，分别看代码问题、测试失败、配置和依赖，再把结论合成一份简短的决策稿。我只需要你产出 decision_brief.md，里面给出排序后的优先处置建议、每个结论对应的关键数字，以及你建议先修哪些部分。
```

### 424. D5_g980685_en (domain=D5, difficulty=6)

```
You are given a small audit bundle containing source snippets, test results, runtime logs, and dependency metadata.

Your job is to produce a concise audit report with 2-3 deliverables:
1) a risk summary table grouped by module/package,
2) a short list of the most critical defects with evidence, and
3) a prioritized remediation plan.

Use the provided files only. Keep the analysis grounded in the artifacts.
Deliverables should be specific, terse, and organized.
```

### 425. D5_g980799_en (domain=D5, difficulty=6)

```
I need a compact audit report for the codebase and the test/log bundle because we need to decide what to fix first before the next release.
Please review project_codebase.xlsx and test_and_ci_logs.docx together, then give me one short report that groups the findings by module, security risk, test failures, and config/dependency issues, and ends with a practical fix-and-validation plan.
I do not want a huge dump of raw rows; I want the important issues summarized clearly enough for engineering and product to use in a meeting.
```

### 426. D5_g981207_en (domain=D5, difficulty=6)

```
I need a decision brief for a codebase audit because we have a release blocker and I want to know what to fix first. Please review audit_inventory.xlsx, manifest.json, and the combined_audit.log, then give me one short decision brief that ranks the issues by priority and explains the tradeoff using the numbers you find. I care about the static code review, the security review, the test failures, and the dependency/config check all being pulled together into one recommendation.
```

### 427. D5_g981228_zh (domain=D5, difficulty=6)

```
请帮我做一次这套代码库的合并审计，输入是 audit_catalog.xlsx、service_audit.log 和 deploy_config.json。我需要你分别看静态代码/安全问题、测试和运行日志、以及部署配置，然后把结果合成一份简短的决策简报。输出只要一个文件，里面给出优先级排序、需要先修什么、以及每一部分的关键数字。
```

### 428. D5_g981277_zh (domain=D5, difficulty=6)

```
我需要你把 inputs/project_audit.xlsx 和 inputs/audit_log.log 做一次联合审计，最后只输出一个简短的决策摘要文件 decision_brief.md。请分别核对代码审计、配置风险、测试失败和日志里的关键信号，把能支持结论的数字都整理出来，最后给出一个按优先级排序的修复建议和验证计划。
```

### 429. D5_g981648_en (domain=D5, difficulty=6)

```
I need a compact audit of the project files audit_dataset.xlsx, large_log.csv, and runtime_notes.txt. Please review the code/review records, the test log, and the config/dependency data as separate tracks, then combine them into one short report with the concrete issues you found and a unified fix-and-validation plan.
```

### 430. D5_g981685_en (domain=D5, difficulty=6)

```
I need a compact audit report from inputs/mini_project_app.py, inputs/mini_project_auth.py, inputs/mini_project_utils.py, inputs/prod_settings.ini, inputs/test_settings.ini, and inputs/ci_audit.log. Please review the code, config, and logs together, then give me one short deliverable that summarizes the risky patterns, the failing tests, the config problems, and a practical fix-and-validation plan.
```

### 431. D5_g981791_en (domain=D5, difficulty=6)

```
I need a compact audit of the files inputs/code_audit.xlsx, inputs/security_audit.xlsx, inputs/test_logs.xlsx, inputs/dependency_config.xlsx, and inputs/audit_instructions.txt. Please review them as one cross-check: summarize the code-risk findings, the prod config/security issues, the test-log failures and duplicates, and the dependency/version audit, then give me one short unified fix-and-validation plan in a single report file.
```

### 432. D5_g981824_zh (domain=D5, difficulty=6)

```
你在做一次小型 Python 服务的审计复盘。请结合代码、测试日志和安全扫描日志，总结最重要的风险点，并回答下面的定量问题。
```

### 433. D5_g982012_zh (domain=D5, difficulty=6)

```
这次需要我把一个小型代码库的审计结果一次性理清楚，避免把安全问题、配置问题、构建日志和测试失败分开看漏掉。请基于 inputs/audit_catalog.xlsx、inputs/build_and_test.log 和 inputs/audit_manifest.json，输出一份合并后的简报，说明哪些条目需要优先修复，并给出可执行的验证建议。重点是把代码审计、日志异常和测试失败的结论合在一起，别只看单一文件。
```

### 434. D5_g982038_en (domain=D5, difficulty=6)

```
You are given a codebase audit spreadsheet ('codebase_audit.xlsx') and test logs ('test_logs.csv').
Analyze the codebase for security vulnerabilities in the ModuleA and ModuleB functions, identify any flaky tests, and list any vulnerable dependencies (known CVEs).
Provide a concise summary report covering these three areas.
```

### 435. D5_g982080_en (domain=D5, difficulty=6)

```
You are a security engineer auditing a Python project. Analyze the provided materials (source code, test results, audit PDF) and answer the following questions. Provide a brief reasoning for each answer.
```

### 436. D5_g982111_en (domain=D5, difficulty=6)

```
Please audit the small project in inputs/codebase_audit.xlsx, inputs/test_logs.xlsx, and inputs/audit_memo.pdf, then give me one compact decision brief as a ranked remediation plan.
- Review the core management code for the explicit management-related pattern checks in the workbook.
- Review the auth/security code for the exact risky-token patterns listed there, and separate file-level findings from token hits.
- Review the prod and staging config files for the exact config checks called out there.
- Triage the test log failures, especially the human_eval::is_simple_power entries, and summarize the failure/pass split.
- End with a prioritized fix-and-validation plan that cites the key numbers from each track.
- Put the final answer in one file only: recommendation.json.
```

### 437. D5_g982256_en (domain=D5, difficulty=6)

```
I need a compound audit and decision brief over three inputs: multi_module_audit.xlsx, service_logs.txt, and test_matrix.xlsx.
Please review the small multi-module codebase, the service log file, and the test matrix as one connected case, but treat the work in parallel tracks where it makes sense: one track for static code review of the module audit sheet, one track for security/risk review of the same codebase plus the log file, one track for test-failure triage from the test matrix, and one track for dependency/config review using the explicit security/config markers in the code and logs. The final output should be a single concise decision brief that ranks the main remediation priorities and recommends the best next step for the project.

I want the analysis to be grounded in the exact files I provided. The code audit should focus only on the closed-set markers in the audit sheet and logs: literal occurrences of eval(, exec(, pickle.loads, yaml.load( without SafeLoader, md5( or sha1( used on passwords or auth material, subprocess(..., shell=True), debug=True in production config, and secret_key length < 16. For the test triage, count failing tests from the test matrix and separate out sqlite-suite failures. For the log review, count only the explicit greppable security/config patterns above and ignore unrelated noise. For the final ranking, I want the recommendation to be based on the combined severity signals from these four tracks, not on intuition.

Please cite the headline numbers you used and keep the deliverable compact and readable. The deliverable must be exactly one file named decision_brief.md.
```

### 438. D5_g982272_en (domain=D5, difficulty=6)

```
Audit audit_stream.log, code_audit_workbook.xlsx, and dependency_inventory.json. I need a ranked recommendation on what to fix first in this small codebase, based on the security/code smell hits, config issues, and the test failures in the workbook. Put the result in one brief decision brief and include the key counts you used.
```

### 439. D5_g982297_en (domain=D5, difficulty=6)

```
I need a compact audit brief for these three files: project_code_audit.xlsx, test_logs_audit.xlsx, and config_dependency_audit.xlsx. Please review the codebase, triage the test failures, check the production config and dependency sheet, and then put everything together in one findings.md with clear cross-source notes and a practical fix-and-validation plan.
```

### 440. D5_g982602_en (domain=D5, difficulty=6)

```
I need a compact decision brief for a small codebase audit. Please review the files project_audit.xlsx, source_bundle.json, and app.log, then produce a single recommendation file that ranks the issues and says what to fix first.

- Audit the Python modules for the exact security/config patterns listed in the workbook and JSON.
- Triage the log file for the test failures versus passes and note what they point to.
- Cross-check the embedded Django/timezone seed record and the two coding-task seed records for any relevance to the failures.
- Synthesize a prioritized fix plan with the supporting numbers called out clearly.
- Keep it brief and decision-focused; I only want one finished report file.
```

### 441. D5_g982613_en (domain=D5, difficulty=6)

```
I need a compact audit brief for the attached files because I need to decide what to fix first. Please review inputs/codebase.xlsx, inputs/test_logs.xlsx, and inputs/config_audit.json, then write findings.md. Please cover the code risks, the test log issues, the config/dependency problems, and any notes where the files disagree with each other. Keep it business-friendly, but make sure the file names and the main issues are clearly called out.
```

### 442. D5_g982678_en (domain=D5, difficulty=6)

```
Audit the three files inputs/audit_bundle.xlsx, inputs/runtime_audit.log, and inputs/seed_manifest.json. I need one compact report that covers the code review, security review, test-failure triage, and config/dependency audit, then rolls them into a single fix-and-validation plan.
```

### 443. D5_g982755_en (domain=D5, difficulty=6)

```
You are given a small codebase snapshot, a test summary CSV, and a large application log.
Analyze the inputs and identify the main quality and reliability issues.
```

### 444. D5_g982852_zh (domain=D5, difficulty=6)

```
我们要尽快做一次上线前审计，判断这套小项目里哪些地方需要优先修，并把结论整理成一份简洁的 findings.md。请同时查看 inputs/project_audit.xlsx、inputs/app.log 和 inputs/codebase.py，分别从代码安全、配置风险、日志和测试失败、以及依赖/问题单关联这几条线去核对。最后把发现和跨文件之间的对应关系讲清楚，特别是哪些日志或测试结果能和代码/配置问题对上。
```

### 445. D5_g982858_zh (domain=D5, difficulty=6)

```
请审计 inputs/codebase_audit.xlsx、inputs/test_logs.xlsx 和 inputs/dependencies.txt，把代码静态审查、配置检查、测试日志三组结果合并成一份简短的汇总报告。我需要看到每个模块的主要问题、测试失败的分布，以及依赖清单是否有明显异常。
```

### 446. D5_g982895_en (domain=D5, difficulty=6)

```
You are auditing a synthetic multi-module Python web application security package. Use the provided inputs to determine how many findings there are by module, which findings are high severity, and whether the audit package is internally consistent with the generated summary.

Your deliverables:
1) Provide a concise audit summary.
2) List the high-severity findings grouped by module.
3) State whether the module summary matches the raw findings.

Important: this task must be decomposed into multiple independent sub-analyses so a team can work in parallel.
```

### 447. D5_g983275_en (domain=D5, difficulty=6)

```
I need a compact audit package for the project in inputs/project_audit_bundle.xlsx, inputs/app_audit.log, and inputs/test_run.log.
- Review the codebase/static inventory for the exact risky tokens listed in the workbook and call out where they appear.
- Triage the test run and summarize the failures, passes, and timing picture from the logs.
- Check the config and dependency sheet for production misconfigurations and the specific dependency flags it records.
- Pull the findings into one short report with a clear fix-and-validation plan, grouped by area.
- Keep the output compact and decision-ready; I want the main counts, affected modules/files, and the recommended next steps in one file.
```

### 448. D5_g983294_zh (domain=D5, difficulty=6)

```
我需要你帮我做一次小型代码库和日志的综合审计，输入是 inputs/code_inventory.csv、inputs/service_logs.txt 和 inputs/config_and_tests.xlsx。请把模块静态审查、日志里的安全风险、测试失败归因、以及配置依赖检查合并成一份简洁的结论报告，最后给出一个统一的修复与验证计划。我只要一个汇总文件。
```

### 449. D5_g983359_en (domain=D5, difficulty=6)

```
You are given a small repository audit dataset plus a large log file. Using the inputs, produce a concise analysis with evidence-backed findings.
```

### 450. D6_g253_en (domain=D6, difficulty=6)

```
Use inputs/contracts_master.csv, inputs/policy_clauses.json, inputs/approvals_log.csv, and inputs/exceptions.md to produce a concise analysis brief (findings.md) and a small evidence table (evidence_table.csv or markdown) that reconciles the four sources and flags cross‑source conflicts. Focus on 3–4 independent analytical tracks that can be merged later, and include a short reconciliation note on the explicit conflicts in exceptions.md.
```

### 451. D6_g275_en (domain=D6, difficulty=6)

```
I need you to review these four files — contracts.csv, clause_library.csv, amendments.json, and policy_audit_log.txt — and put together a decision brief (decision_brief.md) that ranks the overall portfolio as APPROVE, APPROVE WITH CONDITIONS, or REJECT, and summarizes the key evidence with supporting numbers.
```

### 452. D6_g980403_en (domain=D6, difficulty=6)

```
You are given a synthetic contract-review dataset and a small set of seed records.
Analyze the data and produce a concise but evidence-based report identifying operational patterns, notable risk concentrations, and quality anomalies.
Use the provided files only.
```

### 453. D6_g980439_en (domain=D6, difficulty=6)

```
Review the supplied contract dataset and policy playbook. Identify the embedded real seed clause, reconcile it against policy guidance, and flag the deliberate duplicate/conflicting contract anomaly. Then provide a concise audit summary and a structured list of findings.
```

### 454. D6_g980544_en (domain=D6, difficulty=6)

```
We need to assess which of our contracts may have clauses that conflict with the new SWAMP Act. I've attached the policy PDF (Policy_SWAMP_Act.pdf), the clause extraction table (clauses.xlsx), and the contract metadata (metadata.xlsx). Please produce a ranked list of contracts that require renegotiation, highest priority first, and flag any data anomalies you find. Save the output as recommendation.json.
```

### 455. D6_g980588_zh (domain=D6, difficulty=6)

```
请结合 inputs/contract_review_pack.xlsx、inputs/anomaly_scope.txt 和 inputs/scope_map.json 做一版合同审阅决策简报，结论要按优先级排序，给出建议保留、需复核、需升级处理的清单。重点把重复条款、数据保留冲突，以及高风险/需升级项单独拎出来；最后输出成一份简短的 decision_brief.md。
```

### 456. D6_g980725_en (domain=D6, difficulty=6)

```
I need a single consolidated analyst report for doc-understanding QA on doc_understanding_compound_dataset.xlsx and source_digest.docx. Please extract the key contract, policy, and QA facts, reconcile duplicates, and flag the requested anomaly checks in one compact deliverable.
```

### 457. D6_g980806_zh (domain=D6, difficulty=6)

```
我们需要对这份多来源文档数据进行系统分析。输入文件是 'multi_source_data.xlsx'，包含四个工作表：Documents（合同条款）、Plots（电影叙事）、Legislation（立法摘要）以及参考准表 Rules 和 Taxonomy。请完成以下分析并输出一份综合报告 'compliance_report.xlsx'，报告应包含每项分析的汇总结果和异常清单。具体要求如下：
• 检查合同文件的字段完整性和日期合理性，特别是 start_at 与 end_at 的先后顺序。
• 验证每个文档的分类标签是否与类别 ID 一致（参考 Taxonomy 表）。
• 根据 Rules 表中的规则，检查合同文件是否满足关键词条件（如“change of control”必须出现在相应条款中）。
• 在电影叙事数据中，检测 no_answer 为 True 但 answers 字段非空的矛盾记录。
• 对于立法文件，检查标题是否出现在摘要文本中；若不出现则视为可能标题与内容不符。
• 统计所有文档的总数以及合同文件中的标签多样性。

请严格按照标准作业程序（SOP）定义执行，报告格式细则参考 SOP。
```

### 458. D6_g980994_zh (domain=D6, difficulty=6)

```
我需要你把 contracts_review_packet.xlsx、review_policy.json 和 clause_extract_log.txt 这三份材料一起看完，最后输出一份简短的决策摘要，告诉我这批合同/条款样本更适合走哪个处理方案，并把支撑判断的关键数字和排序写清楚。另外，帮我把文档里提到的几类异常也一并核对出来，方便我跟法务和运营对齐。
```

### 459. D6_g981176_zh (domain=D6, difficulty=6)

```
我需要你把这三份资料合成一份可直接给管理层看的决策简报。重点看合同条款抽取、政策表字段抽取，以及QA样本的一致性，最后给出一个按优先级排序的建议。请基于 clauses.xlsx、policy_and_table_extraction.xlsx 和 embedded_qa.csv 输出一份简短的决策文件。
```

### 460. D6_g981202_en (domain=D6, difficulty=6)

```
Using the provided inputs, perform a cross-file quality review. You will need to inspect the clause cross-reference table, the policy memo, the incident extract, and the review matrix. Identify anomalies, summarize the policy rule, and reconcile the seeded records.
```

### 461. D6_g981340_zh (domain=D6, difficulty=6)

```
我把三份材料都放在 inputs 里了：sources.xlsx、briefing_memo.pdf、aux_table.xlsx。请你综合这三份材料，分别从影片、立法摘要和表格三条线做核对，最后写一份 findings.md，里面要把每条结论的来源和跨来源冲突/一致点说清楚。
```

### 462. D6_g981412_en (domain=D6, difficulty=6)

```
I need a brief analysis synthesizing data from three input files: contracts.xlsx (contracts table and seeds sheet), policy_memo.pdf (policy memo), and contract_document.docx (service agreement). Extract and cross-reference key facts: contract counts, thresholds, references to policies, and any anomalies (duplicate IDs, negative amounts, dates out of range, duplicate clause numbers). Submit a single findings.md report with the synthesized results.
```

### 463. D6_g981451_zh (domain=D6, difficulty=6)

```
你是业务分析助理。请基于 inputs/ 中的发票、政策与案例材料，完成一份中文分析报告。
请重点识别高金额发票、币种结构、审批状态分布，以及与付款/供应商政策相关的风险点。
```

### 464. D6_g981651_en (domain=D6, difficulty=6)

```
Review policy_review_packet_01.docx, supporting_tables_01.xlsx, and policy_review_memo_01.pdf, then write a short findings.md that synthesizes the procurement-policy, contract-clause, and movie-QA tracks. Call out any cross-source mismatches or reconciliation notes, and keep the final brief compact.
```

### 465. D6_g981813_zh (domain=D6, difficulty=6)

```
请基于 inputs/source_materials.xlsx、inputs/clause_catalog.csv、inputs/policy_notes.json 这三份材料，输出一份 findings.md。我要你把合同条款、问答抽取、政策清单和汇总表四块内容合在一起写成研究简报，并把跨文件之间对不上的地方单独列出来。
```

### 466. D6_g982535_en (domain=D6, difficulty=6)

```
You are auditing two related synthetic datasets for QA and structural integrity.
Dataset A is a contract-clause table with labels, offsets, and seed flags.
Dataset B is a policy-instrument table with titles, summaries, years, and seed flags.

Your job is to inspect the provided files and produce a concise QA memo that identifies:
1) any anomalous or invalid records,
2) cross-file patterns that look intentionally seeded versus synthetic noise,
3) whether the datasets are internally consistent enough for downstream use.

Keep your analysis grounded in the files only. If you infer something, state the evidence.
```

### 467. D6_k982188_zh (domain=D6, difficulty=6)

```
请基于 chicago__chicago-contracts__contracts.csv 做一份围绕“相关性与驱动因素”的合同分析，重点看哪些数值字段会一起变化、哪些字段与 Award Amount 的相关性最高，以及这些关系在不同合同类型/采购类型下是否一致。请同时检查数据质量（如负金额、缺失日期、重复合同号等）是否会影响相关性解读。输出请尽量落到可执行的结论，最好能指出 4-6 个可独立分工的分析方向，并给出可复核的统计结果，所有金额统一保留两位小数。
```

### 468. D6_k982199_zh (domain=D6, difficulty=6)

```
请基于文件 chicago__chicago-contracts__contracts.csv 做一份面向合同与档案管理的深度分析，重点围绕“不同类别分组之间的差异”展开：例如按 Department、Contract Type、Procurement Type、Vendor 是否重复出现、以及时间阶段来比较 award amount、合同周期、审批时滞、负金额/缺失值等指标，找出最大分层差距和最异常的组合。我希望你把分析拆成若干彼此独立的子任务，分别从金额规模、周期时长、审批效率、供应商集中度、合同文本/档案可得性、以及异常记录几个角度去看，并最终汇总成一份可直接给业务负责人看的结构化结论。请严格使用表中的真实字段：Purchase Order Description、Purchase Order (Contract) Number、Revision Number、Specification Number、Contract Type、Start Date、End Date、Approval Date、Department、Vendor Name、Vendor ID、Award Amount、Procurement Type、Contract PDF 等；不要臆造任何值，所有结论都要能追溯到数据。请优先比较不同分组的均值/中位数/占比，找出差距最大的组别，并用可复现的 pandas 计算。最后输出一份 summary 文件。
```

### 469. D6_k982245_zh (domain=D6, difficulty=6)

```
请基于文件 chicago__chicago-contracts__contracts.csv 做一份围绕“排名与集中度”的合同/文书分析，重点看哪些部门、供应商、合同类型和采购类型在数量和金额上最集中，是否存在明显的 Pareto 现象，以及这些头部群体是否同时主导高金额合同。请尽量把分析拆成可并行的 4-6 个部分，最后汇总成一份适合管理层快速阅读的结果摘要（analysis_summary.json）。需要直接使用现有字段：Department、Vendor Name、Contract Type、Procurement Type、Award Amount、Approval Date、Start Date、End Date、Purchase Order (Contract) Number、Purchase Order Description、Revision Number、Specification Number、Contract PDF 等，所有结论必须来自数据本身，不要臆测。
```

### 470. D6_k982266_en (domain=D6, difficulty=6)

```
Using chicago__chicago-contracts__contracts.csv, please do a contract-and-records concentration review focused on ranking and Pareto share. I need a compact analysis that identifies which vendors, departments, procurement types, and contract descriptions dominate the file, how concentrated award dollars are in the top groups, and whether the biggest awards are tied to a small set of records. Please use the actual columns in the file, especially Vendor Name, Department, Procurement Type, Purchase Order Description, Award Amount, Purchase Order (Contract) Number, Revision Number, Contract Type, Start Date, End Date, and Approval Date. Break it into independent workstreams so different analysts can work in parallel, and make the final output suitable for a management briefing on concentration risk, top-N dependency, and record-level outliers.
```

### 471. D6_k982469_en (domain=D6, difficulty=6)

```
Using chicago__chicago-contracts__contracts.csv, build a contract portfolio review focused on ranking and concentration. I need a concise but rigorous analysis of which vendors, departments, contract types, and procurement types account for the largest shares of award amount and contract volume, plus whether spend is unusually concentrated. Please treat the file as fixed and use the actual columns: Purchase Order Description, Purchase Order (Contract) Number, Revision Number, Specification Number, Contract Type, Start Date, End Date, Approval Date, Department, Vendor Name, Vendor ID, Award Amount, Procurement Type, and Contract PDF. Break this into independent workstreams so different analysts could run them separately, then summarize the top groups, their shares of total award amount, and key Pareto-style concentration metrics. Also include a small check on date coverage and missingness where relevant.
```

### 472. D6_k982590_en (domain=D6, difficulty=6)

```
Using chicago__chicago-contracts__contracts.csv, produce a contract-analytics memo focused mainly on temporal trend analysis across the date fields (Start Date, End Date, Approval Date). I want a multi-part review that breaks the portfolio into independent tracks: (1) yearly and period-over-period changes in contract volume and award dollars by approval date, (2) how contract duration changes over time and whether long-running contracts are becoming more common, (3) department-level trends in award amounts and contract counts by approval year, (4) vendor recurrence over time, especially whether repeat vendors are concentrated in certain periods or dates, and (5) data quality around the date fields and their impact on the trend story. Please keep it grounded in the actual columns in the file, and summarize the main temporal patterns, notable spikes/drops, and any caveats from missing or malformed dates.
```

### 473. D6_k982834_en (domain=D6, difficulty=6)

```
Using chicago__chicago-contracts__contracts.csv, analyze the city contract records with a focus on distribution and threshold cohorts. I need a concise but rigorous review that looks at how award amounts are spread across the portfolio, how many contracts fall above/below key business thresholds, what share of total dollars each cohort represents, and whether thresholds differ meaningfully by contract type, department, and procurement type. Please use the real columns in the file (especially Award Amount, Contract Type, Procurement Type, Department, Start Date, End Date, Approval Date, Vendor Name, and Purchase Order (Contract) Number), and structure the work so it can be split across multiple independent workstreams.
```

### 474. D6_k982853_zh (domain=D6, difficulty=6)

```
请基于文件 chicago__chicago-contracts__contracts.csv 做一份面向“合同/记录分析”的多维诊断，重点放在相关性与驱动因素分析：先识别数值字段之间哪些变量一起变化、哪些关系最强（请把相关系数四舍五入到 2 位小数），再结合合同类型、采购类型、部门、供应商与时间字段，解释这些相关关系可能由什么业务因素驱动。请特别关注 Award Amount、Revision Number（可转为数值后分析）、以及日期字段可衍生出的合同周期/持续天数，并判断不同部门或采购类型是否会显著改变这些关系。输出需要能支持后续汇报：既要给出总体相关性排名，也要给出分组对比和异常点线索。请按 4-6 个彼此独立的分析轨道拆开：1) 数值字段相关性矩阵与最强关联；2) 按 Contract Type / Procurement Type 分组的 Award Amount 与修订次数关系；3) 按 Department 的高金额合同特征；4) 按合同持续时长与 Award Amount 的关系；5) 缺失值和记录完整性对相关性的潜在影响；6) 供应商层面的高金额/高修订合同识别。最后请生成适合管理层阅读的结论要点。
```

### 475. D6_k983422_zh (domain=D6, difficulty=6)

```
请基于文件 brunotavares__ibovespa-emini-future-contracts__indfut_2001_2014.csv（列为 dateTime, Open, High, Low, Close）做一版面向“文档/合约与记录分析”的正式分析，重点围绕“分布与阈值分层”展开：先把价格区间、日内波动、收盘相对开盘的变化都按业务阈值和分位数做分层，再看各层的样本量、占比和典型特征。我要的是可以直接给业务方看的结论，不是泛泛描述。请拆成 4-6 个彼此独立的分析轨道并并行推进，分别覆盖：1）阈值分层计数与占比；2）分位数桶分布；3）开收涨跌/平盘结构；4）日内振幅与极端波动记录；5）按时间段/年份的阈值结构变化；6）价格点位集中区间与高频区间。最终输出一份简洁的 summary，能回答这些问题：哪些阈值层最常见、样本主要集中在哪些分位桶、上涨/下跌/持平的 mix 是什么、极端波动记录占比多大、以及这些结构是否随年份明显变化。
```

### 476. D6_k983626_en (domain=D6, difficulty=6)

```
Using the file kanchana1990__new-york-sold-real-estate-intelligence-2026__ny_real_estate_sold_properties_2026.csv, please run a contract/records-style quality and trend analysis focused mainly on temporal change across the available sequence information. I need a practical summary of how sold-to-list dynamics evolve across size tiers and geographies, plus checks for data completeness and record consistency. Please break it into independent workstreams so different analysts could work in parallel: (1) period-over-period movement in sold_list_ratio and sold_vs_asking, (2) trend differences by size_tier and property type, (3) city/zip concentration and outlier patterns, (4) data quality and record completeness for pricing/square-foot fields, and (5) relationship checks among listPrice, lastSoldPrice, sqft, and price-per-sqft metrics. Keep the output concise and decision-oriented.
```

### 477. D6_k983634_en (domain=D6, difficulty=6)

```
Using the file theworldbank__procurement-notices__procurement-notices.csv, analyze the procurement-notices records as a document/contract analytics exercise with a strong focus on segment comparison across categorical groups. I need you to compare how notices differ by Notice Type, Procurement Type, Country Name, Country Code, and Major Sector, and identify the biggest gaps between segments in terms of publication volume, deadline coverage, and timing patterns. Please also flag any category-level anomalies from missingness or unusual concentration. Break the work into a few independent tracks so different analysts could work in parallel, and summarize the findings in a compact analysis_summary.json.
```

### 478. D6_k983729_zh (domain=D6, difficulty=6)

```
请基于文件 bhanageviraj__indian-traffic-e-challan-daily-dataset-20152026__echallan_daily_data.csv 做一份面向“文书 / 合同与档案分析”的日度执法记录分析，重点围绕“排名与集中度（Top-N、总量占比、Pareto 80/20）”展开。请把这份数据当作真实业务台账来做，不要泛泛而谈，直接回答我最关心的管理问题：1）哪些日期、哪些年份最集中地贡献了最多的 challan、金额和法院案件；2）前10%日期是否贡献了大部分总量；3）pending 与 disposed 在数量、金额、法院口径上是否存在明显集中；4）不同年份的峰值日期是否由少数异常高值驱动；5）总量、金额、法院数量三类指标的集中度是否一致；6）请输出一个可以给管理层看的结论摘要，并附上可复核的关键数字。请严格使用数据中的 date、totalChallan、disposedChallan、pendingChallan、pendingAmount、disposedAmount、totalAmount、pendingCourt、disposedCourt、totalCourt 字段。
```

### 479. D6_k983841_en (domain=D6, difficulty=6)

```
Using bhanageviraj__indian-traffic-e-challan-daily-dataset-20152026__echallan_daily_data.csv, please do a compact but rigorous document/contract & records analytics review focused mainly on ranking and concentration. I need to know which dates account for the largest volumes and values, how concentrated the workload is in the top days, and whether a small set of dates drives most challans, amounts, and court records. Break it into independent tracks so different people could work in parallel: (1) top-day ranking for totalChallan, totalAmount, and totalCourt; (2) Pareto-style concentration of volume/value in the top 10 and top 20 dates; (3) comparison of pending vs disposed shares for challans, amounts, and court records on the highest-volume dates; (4) identification of extreme outlier dates by each core metric and how much they contribute to the full-period totals; (5) consistency checks across the accounting identities among totalChallan, pendingChallan, disposedChallan and the amount/court counterparts; (6) a short concentration summary that can be used in an executive note. Please return the results in a concise, structured form suitable for an analysis_summary.json.
```

### 480. D6_k984306_en (domain=D6, difficulty=6)

```
Using the file theworldbank__procurement-notices__procurement-notices.csv and the real columns available (ID, URL, Notice Type, Publication Date, Project ID, Bid Description, Procurement Type, Deadline Date, Country Code, Country Name, Major Sector), build a procurement-notice analytics memo focused mainly on segment comparisons across categorical groups. I want you to compare notice composition, timing, and missingness across groups such as Notice Type, Procurement Type, Country Name, and Major Sector, and identify the biggest gaps between segments. Please split the work into several independent tracks so they can be handled in parallel: one track on segment size and distribution, one on publication/deadline timing by segment, one on geographic differences, one on sector differences, and one on data quality / missing-field patterns. Summarize the most important group-level contrasts and the largest absolute differences you find, with enough detail to support a concise decision memo.
```

### 481. D6_k984454_en (domain=D6, difficulty=6)

```
Using the file alitaqishah__llm-hallucination-benchmark-dataset__llm_hallucination_dataset_v1.csv, please do a document/contract-style records audit focused on anomaly and outlier detection using explicit numeric rules. I want a concise executive summary plus a structured findings file that flags unusual records by thresholds, IQR, rare categories, and extreme values. Break the work into separate tracks so different assistants can handle them independently: (1) label/severity anomalies and high-risk outliers, (2) unusual model/prompt combinations and rare categories, (3) confidence-score extremes and missingness issues, (4) mitigation effectiveness patterns, and (5) domain/language/task slices that are disproportionately concentrated in anomalous records. Use the actual columns in the dataset, especially hallucination_label, severity, domain_risk, annotation_confidence, mitigation_applied, intrinsic_or_extrinsic, model_name, prompt_type, domain, task_type, and language.
```

### 482. D6_k984508_zh (domain=D6, difficulty=6)

```
请基于文件 aakaash89__neet-2024-ug-results-citycenter-wise__NEET_2024_RESULTS.csv（字段：dummy_srlno、marks、state、city、center_name、center_number）做一份面向“文档/合同与档案管理”的分析简报，重点放在“序列/趋势分析”上：把 center_number 视为记录顺序，按记录顺序观察分数、地区与考点表现是否存在阶段性变化、异常波动和结构性差异。请把结论整理成 analysis_summary.json。为了便于并行处理，请拆成 4-6 个互相独立的分析轨道：1）按记录顺序的分段趋势（如按四等分/时间序列式窗口）比较 marks 的均值、分位数与变化率；2）按 state/city 的趋势分层，识别高分和低分在不同阶段是否迁移；3）按 center_name/center_number 的稳定性与波动性，找出最稳定和最波动的中心；4）检查记录顺序上是否存在“跳变点”或明显异常（例如相邻记录分数差）；5）从档案完整性角度检查是否有缺失值、重复 center_number 或异常取值；6）输出可直接复核的关键统计数字。请尽量用简洁、可审计的方式给出结论，并在每个结论后附上对应统计口径。
```

### 483. D6_k984709_zh (domain=D6, difficulty=6)

```
请基于文件 bhanageviraj__indian-traffic-e-challan-daily-dataset-20152026__echallan_daily_data.csv 做一份面向“文档 / 合同与记录分析”的深度盘点，重点围绕“排名与集中度”展开：找出日级记录里总罚单、已处理/待处理、金额、法院案件等指标最集中的日期、最高值的贡献度、Top-N 占比、以及是否存在明显的 Pareto 现象。请把分析拆成 4-6 个相互独立的子任务，方便并行给子分析员处理；每个子任务都要给出清晰结论，并尽量用表格/要点说明：1）总罚单与总金额的 Top 日期排名及集中度；2）待处理罚单/待处理金额的 Top 日期排名及其对全量的占比；3）已处理罚单/已处理金额的 Top 日期排名及其对全量的占比；4）法院相关指标（pendingCourt、disposedCourt、totalCourt）的 Top 日期与集中度；5）检查“头部 20% 日期是否贡献了约 80% 总量”的 Pareto 结构，并分别对数量和金额类指标做验证；6）补充识别极端高值是否主要集中在少数日期，以及这些极值日期在各指标中的重合程度。请输出适合管理层快速阅读的简明结论，同时给出可复核的计算口径。
```

### 484. D6_k984710_en (domain=D6, difficulty=6)

```
Using brunotavares__ibovespa-emini-future-contracts__indfut_2001_2014.csv, build a document-style records analysis focused on threshold cohorts and distribution mix for the contract observations. I need a compact but rigorous readout that treats the OHLC fields as record attributes, with emphasis on how the dataset splits around business thresholds and quantile bands. Please structure it as four to six independent workstreams so they could be handled in parallel: (1) overall record completeness and date coverage, (2) threshold cohorts for Close and range/volatility proxies, (3) quantile-bucket mix shares for prices and intraday spread, (4) year-by-year and time-slice cohort composition, and (5) cross-field consistency checks such as Open/High/Low/Close relationships. Focus the main narrative on counts above/below thresholds, bucket frequencies, and share-of-total comparisons rather than time-series forecasting. Return a concise analysis summary suitable for a records-analytics memo.
```

### 485. D6_k984779_zh (domain=D6, difficulty=6)

```
请基于文件 ramjasmaurya__nasa-patents__NASA_Patents.csv 做一份面向“文档/合同与档案分析”的深度盘点，重点围绕“数量排名与集中度（Top-N、占比、Pareto）”展开。请把结果拆成可并行的 4-6 条分析线，优先回答：1）哪些 NASA Center 的专利/申请数量最高，头部是否高度集中；2）Status（Issued / Application）在不同 Center 之间的分布是否有明显偏向；3）Title 中最常见的关键词/短语类文档主题是什么，头部主题是否集中；4）Patent Expiration Date 的缺失与时间分布是否存在集中现象，哪些年份最密集；5）Case Number 或 Application SN 的格式异常/缺失情况是否集中在少数 Center；6）如果按 Center 汇总，Top 3 / Top 5 覆盖了多少比例。请输出适合管理层阅读的结论摘要，以及可复核的统计结果。请严格使用数据文件中的真实值，不要补充或臆造任何信息。文件字段包括 Center、Status、Case Number、Application SN、Title、Patent Expiration Date。请按下面的核查问题逐项计算。
```

### 486. D6_k985053_zh (domain=D6, difficulty=6)

```
请基于文件 alitaqishah__llm-hallucination-benchmark-dataset__llm_hallucination_dataset_v1.csv 做一份面向“文档 / 合同与记录分析”的快速审计分析，重点围绕分布与阈值分层：请先看 hallucination_label 在不同阈值、分位数桶和业务风险层级下的占比、数量和结构，再结合 domain、task_type、model_name、mitigation_applied、intrinsic_or_extrinsic、severity 等字段，判断哪些组合更容易落入高风险区间。我要你把结果整理成可交付给业务方的 analysis_summary.json。请分成几个独立分析轨道并行做：一条看总体分布和阈值 cohort，一条看按 domain/task_type 的混合结构，一条看模型与版本的风险集中度，一条看缓解策略是否改变阈值分层，一条看内在/外在幻觉的差异，一条看缺失与异常记录是否影响结论。最后请给出简洁结论，指出最值得优先复核的阈值人群与组合。
```

### 487. D6_k985060_en (domain=D6, difficulty=6)

```
Using chicago__chicago-sidewalk-cafe-permits__sidewalk-cafe-permits.csv, analyze the sidewalk cafe permit records as a contract/records portfolio with a focus on distribution and threshold cohorts. I need a concise operational readout on how the permits are distributed across years, wards, geographies, and businesses, especially where the portfolio crosses business-relevant thresholds like “top decile”, “above/below median”, and other bucketed cutoffs. Please break this into independent workstreams so they can be handled in parallel: one track for permit issuance timing and annual volume concentration; one for cohorting businesses by permit count thresholds and quantiles; one for ward/community-area mix shares and concentration; one for address-level duplication/repeat-site behavior; one for missing-data and record-completeness thresholds across the geocoded fields; and one for a short list of the most frequent legal/DBA names and how much of the portfolio they represent. I want the final output to emphasize counts, shares, and threshold-bucket summaries rather than narrative.
```

### 488. D6_k985067_zh (domain=D6, difficulty=6)

```
请基于文件 mosapabdelghany__telcom-customer-churn-dataset__Telco_Cusomer_Churn.csv 做一版面向“文档 / 合同与记录分析”的业务诊断，重点围绕“分布与阈值分层（高低阈值人数、分位数组、占比结构）”来展开。请直接用现有字段分析，不要改任何原始值。我要你把这个 1500 行数据拆成 4-6 个彼此独立的分析轨道，适合并行给多个小组一起跑，最后汇总成一份可落地的分析摘要。重点要回答：
1）客户在 tenure、MonthlyCharges、TotalCharges 上的分布是否呈现明显的高低阈值分层；
2）不同阈值/分位数组下，Churn 的占比和 mix 是否显著不同；
3）合同类型、支付方式、纸质账单等记录/合同相关字段，在高低阈值人群中的结构差异；
4）哪些组合最像“高风险记录档案”，以及这些组合的样本占比有多大；
5）需要输出清晰的计数、占比、均值/中位数、分位数分桶结果，尽量用表格化 JSON 汇总。
请注意：TotalCharges 原始列是 object 类型，分析时如需数值化请谨慎转换，不能改变数据本身。最终产出请生成 analysis_summary.json，并把每个子分析轨道的关键发现整理成可执行建议。
```

### 489. D7_g160_zh (domain=D7, difficulty=6)

```
我需要你基于 `inputs/incident_registry.xlsx`、`inputs/service_logs.xlsx`、`inputs/config_snapshots.xlsx`、`inputs/ops_tickets.xlsx` 这四份文件，做一次面向值班复盘的事故调查和简版事后总结。这是两起独立的线上事故，分别是 payments-api 和 orders-api。请你输出 2-3 个紧凑文件（CSV/JSON/MD 都行，能直接交给管理层和值班团队用），内容包括：汇总两起事故的总数、受影响服务数、日志行数、总错误数和最高延迟；每起事故的首次错误日志时间、关联工单数、最终责任组、缓解耗时；配置异常三类统计；以及每起事故的简易时间线摘要（发现、升级、客户通知、解决四个节点，缺失的标 null）。最后给一个简短复盘结论，点出两起事故最主要的共性流程问题，并说明哪一起沟通节奏更慢（以首次客户通知工单距事故开始的时间为准）。
```

### 490. D7_g167_en (domain=D7, difficulty=6)

```
We need to understand the incident cluster from yesterday (May 17, 2024) and its impact on our finance operations. Use the files in inputs/ — incidents.xlsx, tickets.json, configs.json, incident_log.txt, and postmortem.md — to reconstruct what happened, who was affected, and what configuration risks may have contributed. Then produce three compact summary reports for leadership: an impact summary, a timeline with ownership notes, and a configuration risk / comms report. Keep the outputs small and aggregate‑level.
```

### 491. D7_g381_en (domain=D7, difficulty=6)

```
Hey — I need a decision brief for the exec-on-call review covering the May 12–13 incident cluster. Could you pull together a compact memo from the files in **inputs/** and write it as **decision_brief.md**? The memo should synthesize evidence from incidents.xlsx, tickets.jsonl, postmortems.md, config_snapshot.json, and ops_events.log, then present a ranked recommendation with supporting numbers. Specifically, I need the following computed and woven into the memo (not a raw dump, keep it under 60 lines as flowing prose):

* Count of Sev1 incidents that are resolved — treat “Sev1” as severity == 'sev1' and “resolved” as status == 'Resolved' (case-sensitive).
* Total customer tickets linked to incidents owned by the payments-platform team. From incidents.xlsx, get all incident_id where owner_team == 'payments-platform'; then in tickets.jsonl, count tickets whose incident_id matches any of those IDs (ignore tickets with null incident_id).
* The incident_id with the highest revenue_impact_usd and that value. If two incidents tie for highest, take the one with the smallest incident_id lexicographically. Treat null revenue values as absent (ignore them).
* Number of SLA‑breached tickets after excluding orphan tickets that have no matching incident_id in incidents.xlsx. A ticket is SLA‑breached if sla_breach is true; then drop any ticket whose incident_id is null or not found in the incident_id column of incidents.xlsx.
* Number of distinct incident IDs referenced in ops_events.log that also exist in incidents.xlsx. Each event in ops_events.log is JSON — extract the incident_id field; find all unique values; then count how many of those also appear in the incident_id column of incidents.xlsx.
* Longest resolved incident duration in hours, rounded to two decimal places. Only include incidents with status 'Resolved' and both start_time and end_time present and parseable. Duration = (end_time - start_time) in hours. Take the maximum across those, standard rounding (0.5 rounds up) to two decimals.
* Count of tickets created on 2025-05-12 UTC with priority p1. In tickets.jsonl, consider the created_at field — any ticket whose date (ignoring time-of-day) is exactly 2025-05-12 and whose priority equals 'p1' counts once.

For the decision brief itself: state a single primary recommendation sentence up front, then list the top operational priority areas ranked by evidence, and mention any anomalies that affected reconciliation (e.g., data gaps or mismatches you had to handle). Keep the memo concise and decision‑focused — no per‑row dumps, just the computed numbers that support your reasoning. Use the definitions and edge‑case rules I gave above so there’s no ambiguity. Thanks!
```

### 492. D7_g514_en (domain=D7, difficulty=6)

```
I need a decision brief for the current mailer incident review, using incident_log.json, workflow_config_history.json, ops_tickets.json, and incident_communications.json.

Please produce a concise decision_brief.md that ranks the best operational decision for the next 24 hours and explains it with the key numbers.
- Use a closed-world dedupe on incidents: keep the first record for any repeated incident_id/opened_at/service combination, and ignore later duplicates.
- For the config history, treat the latest snapshot per config name as current; if the same name and snapshot repeat, keep the first row.
- Score mailer impact as 5*sev1 + 3*sev2 + 2*sev3 + 1*sev4 across incidents whose service is mailer-api.
- Treat tickets with incident_id that does not appear in the deduped incidents as orphan tickets.
- For MTTR, average only resolved mailer-api incidents, in hours, rounded to 2 decimals.
- I want the decision ranked against three options: keep the current config, rollback the current config, or pause outbound mail until the open sev1s are cleared.

I also want a small machine-readable summary JSON with the headline metrics used in the brief.
```

### 493. D7_g532_en (domain=D7, difficulty=6)

```
Analyze the incident data from the provided error logs, config_changes.yaml, postmortem_draft.md, and ticket data. I need a findings.md and evidence_table.csv covering:

- Error logs with "exchange_rate_compute_error" and level=ERROR within the incident window (March 10–14, 2025). Show distinct affected customers and total financial impact (treat missing amounts as zero).
- Flag any single error transaction over $10,000 as a material variance.
- First and last error timestamps.
- Which deployer introduced the bug (use config_changes.yaml: the change at 2025-03-12T09:15:00Z is the cause).
- Whether the postmortem root cause claim (from postmortem_draft.md) conflicts with that deployer.
- Ticket classification: use the label set {card_payment_wrong_exchange_rate, card_linking, exchange_rate, negative, positive}. Flag tickets whose description contains "rate", "exchange", or "conversion" but category is not one of the two exchange-rate labels. Also list open tickets.
```

### 494. D7_g980620_en (domain=D7, difficulty=6)

```
I need a compact incident investigation report from the files "incident_ops_bundle.xlsx", "timeline_notes.txt", and "incident_comms_memo.pdf". Please pull together the impact assessment, the event timeline, and the owner/comms status into one concise deliverable, and call out the highest-risk config changes plus any open follow-up gaps.
```

### 495. D7_g980652_en (domain=D7, difficulty=6)

```
We suspect a spike in duplicate ticket submissions and potential exchange rate errors in our card payment system. Investigate the provided PayFlow incident dataset to identify duplicate groups, anomalous resolution patterns, and tickets related to card linking or wrong exchange rates. Summarize findings and propose remediation steps.
```

### 496. D7_g980676_zh (domain=D7, difficulty=6)

```
我需要一份基于 inputs/incident_ops_a.xlsx 和 inputs/incident_ops_b.xlsx 的事故分析简报，重点把影响范围、时间线、负责人和对外沟通串起来。请输出 findings.md，里面要把关键发现、跨文件对账结果、以及彼此冲突或需要解释的地方写清楚。
```

### 497. D7_g980713_zh (domain=D7, difficulty=6)

```
请分析生产环境支付同步故障的日志和工单数据。我需要一份综合报告 incident_report.xlsx，包含影响评估、时间线重建和负责人/沟通追踪。数据在 incident_data.xlsx 中，包含工单、配置、日志和负责人四个工作表。
```

### 498. D7_g980732_zh (domain=D7, difficulty=6)

```
请调查2025年3月10日发生的支付网关超时故障。
输入文件位于 inputs/ 目录下，包括：
  - postmortem.pdf (事故复盘报告)
  - system_logs.csv (系统日志)
  - integration_config.csv (集成配置)
请分析故障的根本原因，并完成以下交付物。
```

### 499. D7_g980860_zh (domain=D7, difficulty=6)

```
我需要你帮我做一份这次 incident 复盘的决策简报，把 inputs/incident_ops_data.xlsx、inputs/incident_timeline.log 和 inputs/ops_policy.json 一起看一下。重点是把影响面、时间线、owner 归属和对外沟通这几条线串起来，最后给我一个能直接拿去开会的简短结论。
```

### 500. D7_g980904_zh (domain=D7, difficulty=6)

```
请结合 inputs/incident_ops_bundle.xlsx 里的 incidents、events、tickets、comms 和 seed_records，输出一份单文件的事故复盘汇总，重点说明影响范围、时间线、责任 owner/沟通状态，以及需要标记出来的数据异常。我要的是一份可直接发给管理层的精简报告，别拆成多个文件。
```

### 501. D7_g981062_en (domain=D7, difficulty=6)

```
You are given an incident activity log and an integration configuration workbook. Investigate the data and produce a concise incident review.
```

### 502. D7_g981072_en (domain=D7, difficulty=6)

```
You are a security analyst investigating an incident that occurred on the night of September 7-8, 2023. You have access to three datasets: logs.csv (system logs), tickets.csv (customer support tickets), and configs.csv (integration configurations). The incident caused widespread payment gateway failures and customer complaints about extra charges and card linking issues. Identify the root cause, impacted services, number of affected users, and whether any expired API keys contributed. Provide a summary with supporting evidence from the data.
```

### 503. D7_g981078_en (domain=D7, difficulty=6)

```
You are given incident logs, configuration snapshots, customer tickets, and a daily brief for a support ops review. Analyze the provided files and produce a concise operational recommendation that identifies the highest-risk service areas, the most urgent incident cluster, and any configuration concerns that should be escalated.
```

### 504. D7_g981281_zh (domain=D7, difficulty=6)

```
我们需要尽快把这次 payments-api 事故复盘清楚，方便下午对内同步和之后写正式 postmortem。请基于 inputs/incident_ops_pack.xlsx、inputs/owner_comms.json 和 inputs/timeline.txt，先把影响、时间线和负责人/沟通情况理顺，再给我一份简短但可直接拿去开会的决策摘要，说明现在最该优先推进的修复和沟通动作。另外请把你发现的异常也一并写出来，尤其是重复日志和配置里的明显不合理项。
```

### 505. D7_g981317_zh (domain=D7, difficulty=6)

```
我们昨天经历了一次严重的服务中断。我需要一份全面的调查报告，包括影响评估、时间线、参与人员以及根因分析。所有数据都在 incident_tickets.csv、system_logs.csv 和 service_config.json 这三个文件里。请帮我生成一份PDF报告总结发现，再提供一个包含详细指标的Excel文件。谢谢。
```

### 506. D7_g981324_zh (domain=D7, difficulty=6)

```
请基于 inputs/incident_ops_bundle.xlsx 和 inputs/bundle_meta.json 出一份简短的决策简报，文件名用 decision_brief.md。我要看这次事故群的影响、时间线、工单/沟通责任链是否对得上，并给出你建议优先处理的 3 件事。顺手把你发现的关键异常点也写清楚。
```

### 507. D7_g981340_zh (domain=D7, difficulty=6)

```
我需要你看一下这组事故资料，帮我把 2024-08-13 到 2024-08-15 这段时间的这次线上事故做成一个简短的决策摘要。请结合 inputs/incident_ops_bundle.xlsx、inputs/ticket_index.csv 和 inputs/timeline_notes.txt，把影响范围、时间线、以及 owner/对外沟通情况一起梳理清楚，最后输出一个 decision_brief.md，给我一个按优先级排序的处置建议，并把关键数字写出来。
```

### 508. D7_g981775_zh (domain=D7, difficulty=6)

```
请帮我整理这次 report-archive 相关事故的决策简报，结合 inputs/incident_workflow_logs.xlsx、inputs/integration_config.xlsx 和 inputs/incident_tickets.xlsx 一起看。我要的是能直接给负责人和值班群发的单页结论。
- 先把影响范围、关键时间线和现状说清楚，尽量把几份文件里的信息对齐。
- 重点看 workflow 日志里的异常、配置里的超时/重试设置，以及工单状态和 owner/comms 记录。
- 请判断当前最应该优先推进的处理方向，并按优先级排个序，写明你为什么这样排。
- 最后补一段简短的后续动作建议，方便我直接转给相关 owner。
```

### 509. D7_g981797_zh (domain=D7, difficulty=6)

```
这次要做一次事件复盘，我需要把 tickets.xlsx、incident_logs.xlsx 和 incident_brief.pdf 里的信息合到一份简洁报告里，方便我发给管理层和值班团队。重点不是罗列原始数据，而是把影响面、时间线、责任人和沟通状态讲清楚，同时把需要人工跟进的异常点标出来。
```

### 510. D7_g981811_en (domain=D7, difficulty=6)

```
You are given an incident-ops workbook plus a small supporting JSON context file. Analyze the data and produce a concise ops summary that reconciles the logs, tickets, postmortems, communications, and embedded seed records.
```

### 511. D7_g981951_en (domain=D7, difficulty=6)

```
You are an SRE investigating a major incident on Nov 15. Review the provided datasets (incident_events.xlsx, support_tickets.xlsx, config_changes.xlsx) and produce a postmortem synthesis. Identify anomalies, correlate events with tickets and config changes, and propose actionable improvements.
```

### 512. D7_g982014_zh (domain=D7, difficulty=6)

```
帮我做一下最近一周的 incident 调查。数据在 incidents.xlsx, tickets.xlsx, config.pdf 里。我需要分析影响范围、时间线、归属团队，最后生成一个决策建议。结果存成 decision_brief.md。
```

### 513. D7_k982258_zh (domain=D7, difficulty=6)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维/日志与事件分析的深度排查，重点放在“相关性与驱动因素分析”：先找出哪些数值字段彼此一起变化、哪些指标最能解释 suspicious/normal 的差异，以及哪些连接模式最像异常。请不要只做描述统计，要把分析拆成可并行的几个轨道并最终汇总成一份可执行的结论。具体请覆盖：1）整体数据质量与字段分布核查；2）数值字段之间的相关性、强关联对与可能的驱动指标；3）按 class/Proto/Flags/端口分组对比关键数值指标；4）疑似异常与正常流量在时长、包数、字节数、Flows、Tos 上的差异；5）按源/目的地址与端口找出最可疑的连接模式和高频组合；6）输出一份用于运维复盘的结论摘要，说明最值得关注的关联关系和可疑模式。请直接给出结论，不要画图。
```

### 514. D7_k982321_en (domain=D7, difficulty=6)

```
Analyze the file speedwall10__iot-device-network-logs__Preprocessed_data.csv using the real columns frame.number, frame.time, frame.len, eth.src, eth.dst, ip.src, ip.dst, ip.proto, ip.len, tcp.len, tcp.srcport, tcp.dstport, Value, and normality. I need a correlation-and-driver analysis for IT ops / incident analytics: identify which numeric fields move together, surface the strongest associations, and explain whether normal vs anomalous traffic differs in the main drivers. Please break it into independent work streams so different analysts can work in parallel: one on overall correlation structure, one on correlations with Value and normality, one on packet/length/transport-port relationships, one on source/destination address patterns, and one on normal vs anomalous cohort comparisons. Return a compact analysis summary in analysis_summary.json with rounded correlations and the top associations I should care about first.
```

### 515. D7_k982440_zh (domain=D7, difficulty=6)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一次面向 IT 运维/日志与事件分析的深度排查，重点围绕“相关性与驱动因素分析”：哪些数值字段彼此联动、哪些字段对 suspicious/normal 的区分更强、以及这些关系在不同协议/端口/攻击类型下是否一致。请你把分析拆成可并行推进的 4-6 个独立方向，最后汇总成一份可直接给值班工程师和安全分析师看的结论：1）先检查数据质量与字段分布是否会影响相关性解读；2）计算主要数值字段（Duration、Src Pt、Dst Pt、Packets、Bytes、Flows、Tos）之间的相关矩阵，并找出最强的正/负相关对；3）比较 suspicious 与 normal 两类在关键数值字段上的差异，并识别最可能的驱动字段；4）按 Proto、class、attackType 分层，看看相关结构是否发生变化；5）重点审视端口与流量规模（Packets/Bytes/Duration/Flows）的关系，找出高风险特征组合；6）输出一个简洁的、带数值证据的结论摘要，说明哪些指标最值得纳入告警规则或关联分析。
```

### 516. D7_k982560_zh (domain=D7, difficulty=6)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一次面向 IT 运维 / 日志与事件分析的深度排查，重点围绕“频次与集中度（Top-N、总量占比、Pareto）”来展开。请结合这些真实列：Date first seen、Duration、Proto、Src IP Addr、Src Pt、Dst IP Addr、Dst Pt、Packets、Bytes、Flows、Flags、Tos、class、attackType、attackID、attackDescription，帮我回答：1）哪些源 IP / 目的 IP / 目的端口 / 协议最集中，前几名占了多少流量或记录数；2）正常、suspicious、unknown 三类在整体和 Top-N 中的集中度差异；3）Bytes、Packets、Duration 的重尾特征是否明显，是否由少数大流量连接主导；4）高频 Flags 组合是否高度集中，是否与 suspicious 类别相关；5）按日期/时间段看，异常是否集中在某些时间窗口；6）把这些结果整理成可交付给值班工程师的简明结论，并给出最值得优先追查的高频对象列表。请将分析拆成互相独立的 4-6 个轨道，便于并行处理。
```

### 517. D7_k982577_en (domain=D7, difficulty=6)

```
Using speedwall10__iot-device-network-logs__Preprocessed_data.csv, do a segmented incident-analysis pass on the preprocessed IoT network logs. I need the analysis centered on comparing groups and surfacing the biggest gaps between segments so I can see which traffic profiles look most anomalous. Break it into independent workstreams: compare normality groups on frame.len, ip.len, tcp.len, and Value; compare protocol segments using ip.proto; compare source and destination port behavior using tcp.srcport and tcp.dstport; look at source/destination IP concentration and whether the same hosts behave differently by normality; and compare time-based activity patterns by normality and by protocol. Please call out the largest mean/rate differences between segments, plus any segment-level counts that help interpret them.
```

### 518. D7_k982713_en (domain=D7, difficulty=6)

```
Analyze `speedwall10__iot-device-network-logs__Preprocessed_data.csv` for IT ops / logs & incident analytics, focusing mainly on correlation and driver analysis. I need you to identify which numeric fields move together, call out the strongest rounded correlations, and explain which fields look most associated with `normality` and `Value`. Please also break the work into parallel tracks so a small sub-agent team can work independently: one track for data quality / missingness, one for pairwise correlation structure, one for the strongest positive/negative associations with `normality`, one for associations with `Value`, and one for protocol/port-related behavioral summaries that may explain those relationships. Keep it practical and incident-oriented, using the real columns in the file: `frame.number`, `frame.time`, `frame.len`, `eth.src`, `eth.dst`, `ip.src`, `ip.dst`, `ip.proto`, `ip.len`, `tcp.len`, `tcp.srcport`, `tcp.dstport`, `Value`, and `normality`.
```

### 519. D7_k983023_en (domain=D7, difficulty=6)

```
Using `speedwall10__iot-device-network-logs__Preprocessed_data.csv`, do a compact incident-analytics review focused on distribution and threshold cohorts across the log fields `frame.number`, `frame.time`, `frame.len`, `eth.src`, `eth.dst`, `ip.src`, `ip.dst`, `ip.proto`, `ip.len`, `tcp.len`, `tcp.srcport`, `tcp.dstport`, `Value`, and `normality`. I need this as if I’m validating a suspicious-traffic report: segment the data into business-relevant cohorts (for example, below/at/above key packet-size and `Value` thresholds), quantify mix shares, and compare normal vs abnormal traffic patterns. Please break the work into independent tracks so different analysts can work in parallel, and return the results in `analysis_summary.json` with concise, decision-oriented findings.
```

### 520. D7_k983049_en (domain=D7, difficulty=6)

```
Use the file speedwall10__iot-device-network-logs__Preprocessed_data.csv and do a correlation-and-driver analysis for IT ops / logs & incident analytics. I want a compact incident-style readout that focuses on which numeric fields move together and what likely drives the normality labeling, using the actual columns frame.number, frame.time, frame.len, eth.src, eth.dst, ip.src, ip.dst, ip.proto, ip.len, tcp.len, tcp.srcport, tcp.dstport, Value, and normality. Please break it into 4-6 independent tracks so different analysts can work in parallel: (1) data quality and missingness in the numeric fields, (2) rounded pairwise correlations among the main size/protocol/port variables, (3) strongest positive and negative associations with Value and with normality, (4) normality-stratified summaries of the fields most tied to incidents, (5) port/protocol behavior splits that could explain the correlations, and (6) a short exception list of records where the usual patterns break. I need the final writeup to be concise, operational, and centered on correlation/driver findings rather than visualization.
```

### 521. D7_k983348_zh (domain=D7, difficulty=6)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维/日志与事件分析的异常排查分析，重点围绕“按明确数值规则识别异常和离群值”展开：比如用固定阈值、IQR、极端值、稀有类别、字段组合规则来找出可疑流量模式。请把结果拆成 4-6 个彼此独立的分析方向，方便并行推进。重点看这些字段：Duration、Src Pt、Dst Pt、Packets、Bytes、Flows、Proto、Flags、class、attackType、attackID、attackDescription，以及时间字段 Date first seen。请输出能直接支持值班/告警研判的结论：哪些记录/模式最异常、异常主要集中在哪些协议/端口/标志位、normal 与 suspicious 在数值分布上差异如何、以及是否存在明显的稀有类别或极端值组合。最终请给我一个可落地的分析摘要，最好能直接转成排查规则或告警条件。
```

### 522. D7_k983352_en (domain=D7, difficulty=6)

```
Using mikhailhushchyn__dss-performance__ssd_random.csv, I need a compact incident/performance analysis focused on distribution and threshold cohorts. Please segment the SSD random workload results using the real columns iops, lat, block_size, n_jobs, iodepth, read_fraction, load_type, io_type, raid, n_disks, device_type, offset, and id. I care most about how the latency and IOPS distributions behave around business thresholds, which quantile buckets they fall into, and how the mix shifts across configuration dimensions. Please break the work into independent tracks so different analysts can work in parallel: threshold cohort counts for latency and IOPS, quantile-bucket profiling, configuration mix by raid/device/block size, workload split by io_type/read_fraction, and outlier/edge-case identification by extreme performance cohorts. Summarize the results in analysis_summary.json with clear cohort counts, shares, and the key configuration patterns driving the tails.
```

### 523. D7_k983420_en (domain=D7, difficulty=6)

```
Analyze `inputs/gastondana__spacedos__SPACEDOS_ISS2020_slice.csv` for incident/ops behavior using the real columns `UTC`, `9` through `27`, `ddsi`, `flux`, and `SAA`. I want the analysis centered on correlation and driver analysis: identify which numeric fields move together, report the strongest rounded correlations, and separate patterns by SAA vs non-SAA where relevant. Please decompose this into independent workstreams so different people could handle them in parallel: one track for overall correlation structure, one for high-risk/strong-association pairs, one for SAA vs non-SAA comparison, one for time/UTC-based clustering or seasonality checks, and one for sanity checks on missingness and distributional outliers. Summarize the key operational signals and call out the top associations in a concise JSON deliverable.
```

### 524. D7_k983451_en (domain=D7, difficulty=6)

```
Analyze inputs/douglasdcm__computer-events-errors-defects-and-warnings__eventos.csv as an IT ops / incident-log dataset, with the main focus on temporal trend analysis. I need a compact but rigorous assessment of how event volume changes over time, whether certain event sources or severity levels are increasing or decreasing period-over-period, and whether there are recurring spikes or shifts that could indicate operational instability. Use the available date field (`Data e Hora`) and compare patterns across time slices, then connect those trends to the most frequent sources, logs, and event IDs so I can understand what is driving the changes. Please break the work into separate analysis tracks so different people can work independently and then combine the findings into one short summary.
```

### 525. D7_k983456_zh (domain=D7, difficulty=6)

```
请基于文件 speedwall10__iot-device-network-logs__Preprocessed_data.csv 做一次面向 IT 运维/日志与事件分析的综合排查，重点围绕“排名与集中度”展开：先找出流量/事件最集中的对象，再判断这些高频对象是否解释了大部分数据，并结合 normality、Value、协议/端口/IP 维度识别是否存在少数主导型模式。请直接用数据说话，输出可以支持行动决策的结论：例如 top-N 设备/端口/协议的占比、前几类累计覆盖率、是否符合帕累托特征、异常样本是否高度集中在少数模式上，以及 frame.len / ip.len / tcp.len / Value 的集中程度。由于我需要分工给多个子任务，请把分析拆成若干互相独立的轨道，至少覆盖：1) 总体频次集中度，2) normality 分布与集中度，3) 协议与端口的 top-N 集中度，4) IP 源/目的的 top-N 集中度，5) Value 与长度字段的高值集中度，6) 相关性或联合分布的辅助验证。最后请给一个简洁的 analysis_summary.json 结果结构，便于我直接放进汇报材料。
```

### 526. D7_k983568_zh (domain=D7, difficulty=6)

```
请基于文件 jpmiller__employee-attrition-for-healthcare__watson_healthcare_modified.csv 做一份面向 IT ops / 日志与事件分析的多维诊断，重点围绕“排名与集中度”来展开：先找出哪些维度的 Top-N 贡献最高、Top groups 是否占据了绝大部分样本/风险，再结合员工画像和工作状态变量判断是否存在明显的 Pareto 现象。请输出一份可直接给管理层看的分析摘要，要求结论尽量量化，并明确指出高频群组、占比、集中度和可能的运营含义。请务必使用真实字段（例如 Attrition、BusinessTravel、Department、JobRole、MaritalStatus、OverTime、Shift、Age、MonthlyIncome、TotalWorkingYears、YearsAtCompany、YearsSinceLastPromotion、WorkLifeBalance、JobSatisfaction、EnvironmentSatisfaction、RelationshipSatisfaction 等），不要编造任何值。
```

### 527. D7_k983735_en (domain=D7, difficulty=6)

```
Load inputs/supplejade__rt-iot2022real-time-internet-of-things__RT_IOT2022.csv and do a correlation-and-driver analysis for IT ops / incident analytics. Focus on which numeric telemetry fields move together, which features are the strongest drivers of attack labeling, and whether packet/header/window behavior differs by Attack_type. I need this split into independent workstreams so different agents can run in parallel: (1) data quality and distribution sanity checks on key numeric columns, (2) overall correlation structure and strongest pairwise associations among numeric features, especially flow_duration, packet counts, payload bytes, iat metrics, and window sizes, (3) correlation/driver analysis against Attack_type using the numeric fields and a compact ranking of the strongest positive/negative associations, (4) attack-vs-non-attack comparisons for the most informative metrics and protocol/service mix, and (5) a short incident-ops interpretation of likely operational patterns such as SYN-heavy vs DNS/UDP behaviors and any obvious redundancy among metrics. Please produce a concise analysis_summary.json with rounded correlations and top associations.
```

### 528. D7_k983795_en (domain=D7, difficulty=6)

```
Using ziya07__network-traffic-anomaly-detection-dataset__embedded_system_network_security_dataset.csv, I need a compact incident-analytics style review for IT ops focused mainly on segment comparisons across categorical groups. Please break it into independent tracks so different analysts can work in parallel: compare anomaly rates and key feature means by protocol_type_TCP vs protocol_type_UDP, by source IP and destination IP segments, and by TCP flag combinations; identify the biggest gaps between segments for packet_size, inter_arrival_time, packet_count_5s, spectral_entropy, and frequency_band_energy; check whether the label differs materially across these segments; and call out the most extreme categorical skews that could explain suspicious traffic patterns. Keep it practical and operational, not academic.
```

### 529. D7_k983812_zh (domain=D7, difficulty=6)

```
请基于文件 naiyakhalid__flood-prediction-dataset__train.csv 做一份面向 IT 运维 / 日志与事件分析 的深度分析报告。这个数据里虽然没有直接的日志字段，但我希望你把各个数值列当作不同的告警强度、基础设施健康度、环境压力和治理成熟度指标来理解，重点做“相关性与驱动因素分析”：哪些指标彼此最相关、哪些指标最容易一起升高、哪些因素与 FloodProbability 的关联最强，以及是否能从这些数值字段里识别出明显的协同/对冲关系。请输出一份适合给忙碌管理层看的结论摘要，最好能直接落到可执行的运维优先级建议。

请拆成 4-6 个彼此独立的分析轨道并分别完成：
1) 全量数值字段的相关性矩阵与最高相关对识别（重点看正相关和负相关的 Top 组合，必要时四舍五入到 2 位小数）；
2) 与 FloodProbability 的驱动因素分析（哪些字段相关性最高，方向如何，是否存在负相关保护因子）；
3) 与基础设施/治理相关变量的联动关系（例如 DrainageSystems、DamsQuality、RiverManagement、Watersheds、DeterioratingInfrastructure、InadequatePlanning、PoliticalFactors 等是否形成一个相关簇）；
4) 风险分层视角：按 FloodProbability 分位数或阈值分成高风险/低风险组，比较关键指标均值差异；
5) 变量分群或紧密耦合小团体识别：找出若干强相关三元组或成对组合，说明它们可能代表同一类运维/事件链路；
6) 给出一个非常简短的行动建议清单，优先级以“最值得先修复/监控”的指标为准。

请注意：这是一份真实固定数据分析，不要假设任何不存在的字段，不要改值，不要做预测模型。输出结果要可直接交付给业务方，侧重相关性、驱动因素、差异和优先级。
```

### 530. D7_k983953_en (domain=D7, difficulty=6)

```
Using the file dannyrevaldo__android-malware-detection-dataset__Android_Malware_Benign.csv, I need a compact incident-analytics style review of the most common Android permissions/features in this dataset. Please focus mainly on ranking and concentration: identify the top permissions by frequency, how much of the total permission occurrences they account for, and whether usage is Pareto-like. Break the work into independent tracks so different people can work in parallel: one track for global frequency ranking and concentration, one for malware-vs-benign comparison on the most common items, one for class-conditional concentration patterns, one for co-occurrence among the top permissions, and one for a short operational summary of rare vs ubiquitous permissions. Use the real columns in the file such as INTERNET, ACCESS_NETWORK_STATE, READ_PHONE_STATE, WRITE_SETTINGS, INSTALL_PACKAGES, CAMERA, GET_ACCOUNTS, and the binary target label if present. I want the final output organized as a concise analysis summary suitable for an IT ops / logs & incident analytics report.
```

### 531. D7_k983957_en (domain=D7, difficulty=6)

```
Analyze the fixed dataset in `inputs/esathyaprakash__electrical-fault-detection-and-classification__detect_dataset.csv` for IT ops / logs & incident analytics, treating each row as a telemetry event with fields `Output (S)`, `Ia`, `Ib`, `Ic`, `Va`, `Vb`, `Vc`, plus the two empty `Unnamed` columns. I want a focused incident-quality review built mainly around anomaly and outlier detection using explicit numeric rules: threshold breaches, IQR-based outliers, extreme values, and unusual class balance patterns. Please break the work into independent tracks so different agents can work in parallel, and summarize results in `analysis_summary.json`. I care about: which signals are most often extreme, whether anomalies concentrate in one output state, how many rows are flagged by multiple rules, whether any columns are effectively unusable because they are missing or empty, and whether the voltage/current behavior differs materially between the two `Output (S)` states.
```

### 532. D7_k983959_en (domain=D7, difficulty=6)

```
Analyze katehighnam__beth-dataset__labelled_training_data.csv as an IT ops / logs / incident-analytics dataset, with the main focus on correlation and driver analysis: identify which numeric fields move together, show rounded correlations, and surface the strongest associations that may explain suspicious/evil activity. I need this split into 4-6 independent work tracks so a small AI analyst team could work in parallel: one track on overall numeric correlation structure, one on correlations specifically with sus and evil, one on process/event-level driver patterns, one on host/process segmentation, and one on any noteworthy high-frequency or high-risk syscall combinations. Please produce a concise analysis summary in JSON and make sure the findings are grounded in the real columns in the file (timestamp, processId, threadId, parentProcessId, userId, mountNamespace, eventId, argsNum, returnValue, sus, evil, plus processName/hostName/eventName/args where useful).
```

### 533. D7_k984213_zh (domain=D7, difficulty=6)

```
请基于文件 dannyrevaldo__android-malware-detection-dataset__Android_Malware_Benign.csv 做一次面向 IT 运维 / 日志与事件分析 的多维排查：我想把这批安卓样本按“高风险权限密度”和“阈值分层”来做一次完整的分布分析，而不是只看单个字段。请你重点围绕访问类/敏感权限类特征的分布与阈值分层来分析：比如统计高于/低于业务阈值的样本数、按分位数分桶后的占比、不同桶之间的风险特征均值差异、以及在关键权限上各档位的 mix share。请结合真实列名（如 INTERNET、READ_SMS、SEND_SMS、READ_CONTACTS、WRITE_EXTERNAL_STORAGE、ACCESS_FINE_LOCATION、ACCESS_COARSE_LOCATION、CALL_PHONE、GET_TASKS、RECEIVE_BOOT_COMPLETED 等）输出可直接用于汇报的结论，最好能拆成多个互不依赖的分析轨道，分别完成总体分布、阈值 cohort、分位桶、头部权限组合、以及高风险样本占比等分析。最终请产出一个 analysis_summary.json 级别的结论草稿，供我后续写进 incident / malware review 报告。
```

### 534. D7_k984235_zh (domain=D7, difficulty=6)

```
请直接基于文件 rudrakumar96__web-firewall-good-and-bad-request__2bad_reqff.csv 做一份面向 IT 运维/日志与事件分析的综合分析，重点放在“按序列/时间推进的趋势变化”上。虽然这份数据没有显式日期字段，但我希望你把记录顺序当作事件流，按等分批次或滚动窗口分析 bad 请求特征、请求方法、路径模式、body 长度、badwords_count、以及各类特殊字符计数的变化趋势，重点找出：1）bad 与 good 在各窗口中的占比是否出现阶段性抬升；2）可疑特征（如 angle_brackets、percentages、semicolons、double_q、special_chars）的平均水平是否随序列推进而变化；3）POST/GET 的风险画像是否在不同阶段分化；4）高风险路径是否在后半段更集中；5）是否存在某些特征与 class 的稳定相关性；6）给出可以支持告警阈值或分段监控策略的结论。请把分析拆成多个相互独立的子任务，便于并行处理，并最终输出一份结构化结果。
```

### 535. D7_k984360_zh (domain=D7, difficulty=6)

```
请基于文件 djaouadnm__nasa-website-data__nasa_aug95_c.csv 做一份面向 IT 运维 / 日志与事件分析的分层阈值分析，重点围绕访问量在不同业务阈值下的分布、量级分桶和占比结构来找异常与关键流量来源。数据里只有 requesting_host、datetime、request、status、response_size 这几列，我希望你先把 datetime 解析成时间，再围绕以下几个方向拆开分析：1）按状态码和响应大小做阈值 cohort（例如 response_size 是否为 0、是否超过常见阈值、不同 status 的占比）；2）按请求类型/资源路径提取最常见的访问对象，并分析其在不同大小分桶里的 mix share；3）按主机请求频次做分位数分桶，识别高频主机与长尾主机的流量结构；4）按小时/日期粒度看高峰时段的请求量是否集中在某些阈值以上的响应大小；5）找出最值得关注的异常组合（例如某些 status + 大响应 + 高频 host 的交集）；6）输出一份适合运维复盘的摘要，优先用可复核的计数、比例、分位数和 Top-N 结果，避免泛泛而谈。请把结论聚焦在“阈值之上/之下的 cohort 构成”和“各 cohort 的占比变化”。
```

### 536. D7_k984425_zh (domain=D7, difficulty=6)

```
请基于文件 esathyaprakash__electrical-fault-detection-and-classification__detect_dataset.csv 做一份面向 IT 运维 / 日志与故障告警分析的多维诊断报告，重点围绕“不同故障/正常分组之间的指标差异”展开。数据里我只关心这些真实列：Output (S)、Ia、Ib、Ic、Va、Vb、Vc，另外 Unnamed: 7 和 Unnamed: 8 先当作疑似空列检查一下是否有异常值。请你把分析拆成多个可独立并行的部分，最后汇总成一个简洁的 analysis_summary.json。具体希望你至少覆盖：1）按 Output (S) 分组的电流/电压均值、中位数、离散程度对比，找出差异最大的指标；2）按 Output (S) 分组的样本量、故障率/占比及是否存在类别不平衡；3）在故障与非故障之间，找出绝对均值差最大的前几个特征；4）检查电流三相与电压三相的相关性、以及各特征与 Output (S) 的线性相关，判断哪些信号最像“告警触发因子”；5）对异常值或极端值做分组统计，看看故障组是否更容易出现极端电流/电压；6）检查 Unnamed: 7 和 Unnamed: 8 是否全空、是否需要忽略。请把结论写得像给值班经理看的：哪里差异最大、哪里最值得排查、是否存在明显分组信号。不要画图，不要建模，只做确定性统计汇总。
```

### 537. D7_k984492_zh (domain=D7, difficulty=6)

```
请基于文件 jancsg__cybersecurity-suspicious-web-threat-interactions__CloudWatch_Traffic_Web_Attack.csv 做一次面向 IT 运维 / 日志与事件分析的深度排查，重点围绕“排名与集中度”来分析这批可疑 Web 访问：先找出最活跃的来源 IP、国家、目标端口、响应码和检测类型分别由哪些 Top-N 项主导；再看这些 Top 项是否占据了大部分流量/事件，以及是否存在明显的 Pareto 集中现象；同时结合 bytes_in、bytes_out、时间窗口和关联规则名，判断是否是少数来源在短时间内驱动了大多数告警。请把分析拆成几个彼此独立的方向，最后输出可给值班同事直接看的结论摘要。
```

### 538. D7_k984562_zh (domain=D7, difficulty=6)

```
请基于文件 mirzayasirabdullah07__api-failure-intelligence-dataset-afid__api_error_logs_with_root_causes_220k_rows.csv 做一份面向 IT 运维 / 日志与故障分析的深度分析，重点围绕“排名与集中度”（Top-N、头部占比、帕累托/80-20）来回答：1）哪些 API、服务负责人、环境、状态码和错误类型是最集中的故障来源；2）这些头部群体是否贡献了绝大多数错误与高延迟请求；3）不同维度的集中度是否存在明显不均衡；4）retry_count 与 is_retry_successful 在头部故障中是否表现出特征；5）按 region / endpoint / root_cause 的头部模式是否能帮助优先排障。请把结果组织成可给管理层和一线排障团队直接使用的结论，并输出一个简洁的 analysis_summary.json。
```

### 539. D7_k984722_zh (domain=D7, difficulty=6)

```
请基于文件 naiyakhalid__flood-prediction-dataset__train.csv 做一份面向 IT 运维/日志与事件分析视角的相关性与驱动因素分析报告：重点看哪些数值字段彼此一起波动、哪些指标与 FloodProbability 的关联最强，以及这些关系在不同风险分层下是否稳定。请把结果整理成一个可复用的 analysis_summary.json，要求结论尽量量化、可核查，尤其要给出相关系数（四舍五入到 2 位）和 Top 关联项。数据里包含 MonsoonIntensity、TopographyDrainage、RiverManagement、Deforestation、Urbanization、ClimateChange、DamsQuality、Siltation、AgriculturalPractices、Encroachments、IneffectiveDisasterPreparedness、DrainageSystems、CoastalVulnerability、Landslides、Watersheds、DeterioratingInfrastructure、PopulationScore、WetlandLoss、InadequatePlanning、PoliticalFactors 以及 FloodProbability。请围绕以下 4-6 个独立分析线并行展开：1）目标值 FloodProbability 的单变量相关驱动排序；2）自变量之间的成组相关/共线性排查；3）高风险与低风险样本的差异对比；4）最强相关字段的组合联动与条件均值；5）分位数/分层稳定性检查；6）异常高值或极端组合的样本画像。请输出简明但可执行的结论与核查依据。
```

### 540. D7_k984748_zh (domain=D7, difficulty=6)

```
请基于文件 naiyakhalid__flood-prediction-dataset__train.csv 做一份面向 IT 运维 / 日志与事件分析场景的异常与离群点排查方案。这个数据集里没有真正的日志文本，但我希望你把每一行当作一条事件/站点/区域记录来分析，重点围绕“显式数值规则”的异常检测：比如基于 IQR 的极端值、阈值超限、稀有高值组合、以及多字段同时异常的记录。请先给我一个可执行的分析框架，再输出结论摘要，最好能帮助我回答：哪些指标最常触发异常、哪些记录最像高风险离群事件、哪些字段组合最值得做运维告警规则、以及 FloodProbability 与异常强度是否有关。请把分析拆成 4-6 个彼此独立的 track，方便并行处理；每个 track 都要能单独产出结果。请严格使用数据中的真实列名：id、MonsoonIntensity、TopographyDrainage、RiverManagement、Deforestation、Urbanization、ClimateChange、DamsQuality、Siltation、AgriculturalPractices、Encroachments、IneffectiveDisasterPreparedness、DrainageSystems、CoastalVulnerability、Landslides、Watersheds、DeterioratingInfrastructure、PopulationScore、WetlandLoss、InadequatePlanning、PoliticalFactors、FloodProbability。最后请给出一份 analysis_summary.json 风格的结论结构，便于我转交给下游同事继续做规则配置。
```

### 541. D7_k984876_en (domain=D7, difficulty=6)

```
Using algozee__agentic-ai-security-risk-dataset__agent_security_risk_scores.csv, do a security/logs-style risk review focused on correlation and driver analysis: identify which numeric fields move together most strongly, what the top positive and negative associations are, and which operational factors appear to drive access_decision outcomes. Please split this into independent workstreams so different agents can work in parallel: one on pairwise numeric correlations, one on access_decision by risk signals, one on permission_match/resource_sensitivity interactions, one on autonomy/approval/failures/audit logging effects, and one on role-specific patterns across agent_role and user_role. I need a concise analysis summary and the key associations rounded consistently.
```

### 542. D7_k984964_zh (domain=D7, difficulty=6)

```
请基于文件 naiyakhalid__flood-prediction-dataset__train.csv 做一份面向 IT 运维 / 日志与事件分析 的分群对比分析报告，重点围绕“不同事件/环境分组之间的风险均值差异、占比差异、以及最大差距来自哪些分组”来展开。数据里有 1500 条记录，字段包括 MonsoonIntensity、TopographyDrainage、RiverManagement、Deforestation、Urbanization、ClimateChange、DamsQuality、Siltation、AgriculturalPractices、Encroachments、IneffectiveDisasterPreparedness、DrainageSystems、CoastalVulnerability、Landslides、Watersheds、DeterioratingInfrastructure、PopulationScore、WetlandLoss、InadequatePlanning、PoliticalFactors，以及目标 FloodProbability。请把分析拆成 4-6 个彼此独立的 track，方便不同子任务并行：1）按关键强度字段分箱后比较 FloodProbability 的均值/中位数；2）按高风险与低风险分组比较各特征均值差异，找出最大 gap；3）按城市化/基础设施相关字段做分组，比较 FloodProbability 的分布和差异；4）找出 FloodProbability 最高的若干细分组合，并说明它们与全局均值差多少；5）检查哪些字段与 FloodProbability 的相关性最强，但重点仍然是分组对比而不是建模。最终输出请给出可直接给管理层看的简明结论、关键差异、以及最值得优先关注的分组。
```

### 543. D7_k985035_zh (domain=D7, difficulty=6)

```
请基于文件 sonalshinde123__vehicle-telemetry-for-driver-behavior-analysis__Driver_Behavior.csv 做一份面向 IT ops / 日志与事件分析风格的异常与离群点排查报告。重点不要做泛泛的描述，而是围绕“显式数值规则”来定位异常：例如基于 IQR 的极端值、人工阈值规则、稀有类别、组合异常（如高车速+高刹车+大车道偏离）、以及与行为标签的异常分布。请把分析拆成 4-6 条彼此独立的线索，适合并行分工：1）单变量离群点与阈值异常；2）多变量组合异常与规则命中；3）按 behavior_label 的异常率对比；4）phone_usage 这类离散稀有事件的风险画像；5）关键变量相关性或反常关联；6）如有必要，输出一个可落地的异常筛查规则清单。结果请输出一份可直接给业务方看的摘要 JSON（analysis_summary.json），并明确说明每条规则命中的样本数、占比、以及最值得人工复核的切片。
```

### 544. D7_k985040_en (domain=D7, difficulty=6)

```
Using algozee__agentic-ai-security-risk-dataset__agent_security_risk_scores.csv, analyze the agent security decisions for our IT ops / logs and incident analytics review. I need a trend-focused readout first: look at how access_decision outcomes change across the available sequence of records, including period-over-period shifts in Blocked / Allowed / Needs_Human_Approval rates, and whether risk indicators drift over the same sequence. Then break it into separate workstreams: (1) sequence-based trend analysis of access decisions and risk scores over record order, (2) role-based differences in how decision outcomes evolve over the sequence, (3) tool/resource combinations that show worsening security posture over time, (4) high-risk behavior patterns tied to prompt_injection_detected, data_exfiltration_risk, and human_approval_required, and (5) operational control signals like permission_match, audit_log_available, and previous_failed_attempts. Please keep the output concise but include the key trend deltas, the highest-risk segments, and any notable shifts by agent_role, tool_requested, and resource_type.
```

### 545. D7_k985045_zh (domain=D7, difficulty=6)

```
请基于文件 ffflores__redfish-api-logs__dataset.csv 做一份面向 IT 运维 / 日志与事件分析的多维度分析，重点围绕“频率排名与集中度”展开：先找出哪些 manufacturer、model、event_type、class、message_id 最集中，分别看 Top-N 贡献了多少占比、是否存在明显长尾/帕累托现象；再结合 message 内容对高频日志模式做归类，判断最常见的事件类型组合，以及不同 manufacturer/model 下的集中度是否明显不同；最后给出适合运维值班和告警治理的结论，例如应该优先盯哪些设备型号、哪些事件类别、哪些高频 message_id。请把结果整理成可交付的分析摘要（analysis_summary.json），并尽量拆成多个可并行的分析轨道，便于分配给不同子任务。字段只使用 manufacturer、model、message、message_id、event_type、class。
```

### 546. D8_g1081_zh (domain=D8, difficulty=6)

```
帮我做一次知识库的审计分析，重点看三个维度：陈旧内容、未正式发布的内容、以及日志中的孤儿引用。最后从这些缺口里筛出优先修复的候选。你手上应该有内容表和日志数据，按我们常规的审计逻辑来就行，不需要额外解释标准。
```

### 547. D8_g1177_en (domain=D8, difficulty=6)

```
I'm preparing a single decision brief from four input files: `kb_articles.xlsx`, `kb_usage_events.xlsx`, `kb_issues.json`, and `kb_reviews.md`. The goal is to recommend the one most urgent remediation focus for the knowledge base, synthesizing evidence across article inventory, user‑usage signals, issue registry, and review notes.

Output should be exactly one file named `recommendation.json` containing a ranked recommendation with supporting numbers cited. I need the following metrics computed precisely:

- Number of articles stale by more than 180 days as of 2026-01-01 (strictly greater, compare `last_reviewed_at` against that date).
- Number of articles stale by more than 365 days as of the same date.
- Average article quality score, rounded to 3 decimal places.
- Count of currently open issues (unresolved records are open).
- SLA breach rate across all issues, rounded to 3 decimals (record with `sla_days <= 0` is a breach).
- Most frequent non‑empty search query from valid 2025 events (use only events with timestamps in calendar year 2025, exclude exact duplicate event rows, and exclude events whose `article_id` is not present in `kb_articles.xlsx`; ignore blank/null queries).
- Frequency of that top search query.
- Count of top‑20‑by‑views articles that are stale by more than 180 days.

For the final recommendation, rank at least two remediation options and explicitly choose one, with justification drawn from the computed numbers. No need to output an answer key – just the `recommendation.json` file.
```

### 548. D8_g1311_en (domain=D8, difficulty=6)

```
I need you to prepare a single synthesis brief for a Knowledge Management audit, pulling together data from the following files in inputs/:

- kb_articles.xlsx
- support_tickets.csv
- usage_events.xlsx
- gap_register.csv
- source_catalog.csv
- kb_audit.sqlite

The deliverable should be a compact research/synthesis brief in markdown (e.g., findings.md) plus a small evidence table (at least 6 rows) that reconciles all sources and identifies stale content, gap pressure, and remediation priorities. Structure the analysis into four independent tracks that you later synthesize: article freshness/staleness audit, support‑ticket pressure and gap demand, usage behavior and escalation pressure, and source reconciliation with anomaly/conflict review.

Use the following definitions and business rules exactly:

- Snapshot date for all recency/staleness calculations: 2026‑05‑31.
- If a datetime field is blank or NULL, treat it as missing and exclude it from any age calculation that requires it.
- Deduplicate articles only by exact article_id if the same article appears across multiple sources – do not merge different article titles.
- An article is stale at the snapshot date if **any** of these conditions is true:
  1) days since last_reviewed_at > review SLA for that collection,
  2) days since last_updated_at > review SLA for that collection,
  3) status is "draft" and article age > 180 days.
- SLA by collection: Policy = 90 days, Runbook = 120, Troubleshooting = 180, FAQ = 240, Onboarding = 150.
- Ticket resolution rate = (resolved tickets) / (all tickets), using only the `resolved` field. The `closed_at` field may be inconsistent and must not override `resolved`.
- Usage escalation rate = (escalated usage events) / (all usage events).
- A gap overlaps a stale article if they share the same article_id.
- When a source has a known issue recorded in source_catalog.csv, mention it in the reconciliation notes if it affects interpretation.

In the brief, I need the following specific numbers and items (present these naturally within the analysis text, not as a checklist):

- Total article count, total stale article count, and stale article rate as a percentage rounded to one decimal.
- The number of stale articles by collection, sorted descending by count, then by collection name ascending.
- The top 5 articles by `priority_score`, returned as a list of article_id in descending priority order, breaking ties by article_id ascending.
- Total support ticket count, resolved ticket count, and resolution rate as a percentage rounded to one decimal.
- Total usage event count, escalated event count, and escalation rate as a percentage rounded to one decimal.
- Total gap count, open gap count, and how many gaps overlap stale articles.
- The count of articles that violate data consistency rules or edge cases, grouped into these categories (each anomaly counted once): `future_review`, `pre_creation_update`, `closed_without_resolved`, `duplicate_usage_reference`.
- The single collection with the highest stale‑article count; if tied, choose alphabetically.
- The single article_id with the highest number of `linked_tickets_90d` among stale articles; if tied, choose article_id ascending.
- A short cross‑source reconciliation note summarizing at least two conflicts or anomalies discovered from the inputs and how they affect interpretation.

Produce one concise markdown brief with clear headings for each analysis track and a final synthesis section. Include an evidence table (at least 6 rows) and explicit reconciliation/conflict notes wherever sources disagree or contain anomalies.
```

### 549. D8_g1318_en (domain=D8, difficulty=6)

```
Hey, can you audit the KB from the four files in inputs/ — kb_articles.xlsx, kb_usage_logs.csv, kb_audit_findings.csv, and kb_remediation_backlog.xlsx — and give me a compact MD report plus a small JSON summary? I need a clean staleness/gap-remediation readout for the articles that are in the closed set {active, needs_review, deprecated, superseded}; ignore archived or anything outside that set when counting coverage, and for time windows use 2025-02-01 through 2025-04-30 inclusive for the logs. Please score article risk as 0.5*staleness_band + 0.3*open_finding_severity + 0.2*log_pressure, where staleness_band is 0/1/2/3 for last_updated within 30/31-90/91-180/>180 days before 2025-05-01, open_finding_severity is the average severity points of open findings only (low=1, medium=2, high=3, critical=4; unknown labels count as 0), and log_pressure is min(1, views per 100 usage-days / 5). For the remediation backlog, treat priority only as {P1,P2,P3,P4}; invalid/missing priority is excluded from priority counts but still included in the overall backlog totals. I mainly want the top 10 highest-risk articles, the overall staleness rate, the finding-type mix, the overdue backlog count as of 2025-05-01, and a few cross-source notes on anomalies.
```

### 550. D8_g1365_zh (domain=D8, difficulty=6)

```
知识库该做次大扫除了。基于 inputs/ 下的 kb_articles.xlsx、search_logs.jsonl、support_tickets.csv、article_feedback.xlsx 给我做一份审计简报。口径定死：参考日 2025-06-01，published 文章中 last_updated 早于 2024-06-01 计为 stale，其中 views_30d>=500 的算 high-impact stale；搜索缺口看同一 query（小写、首尾去空格后）出现 >=20 次、zero_result_rate>=0.3 或 CTR<=0.15 的算 gap；工单 resolution_kb_id 为空算未解决；评分 avg_rating<2.5 且 ratings>=5 条的算低质；owner 不在 owner_001~owner_030 的算 orphan。重复标题就按 published 文章里 title 完全相同（>=2 篇）算一个 group。产出 findings.md（每个 track 的关键发现 + top 类目）和 evidence_table.csv（每个 track 一行核心指标），不要导全量明细，给我看结论。
```

### 551. D8_g980845_zh (domain=D8, difficulty=6)

```
请基于 KB_audit_master.xlsx、kb_feedback_logs.csv、source_registry.json 这三个文件，输出一份 findings.md。我要看到 2026 年 Q1 知识库审计结果：内容陈旧、缺口、重复/冲突、以及最该优先补齐的条目。另外把文件里提到的 3 个异常样本也单独写清楚，尤其是和上线评审、财务预算评审、打印机故障有关的记录。
```

### 552. D8_g980897_zh (domain=D8, difficulty=6)

```
我需要你先审一下这批知识库数据，再给出一个可执行的处置建议。请基于 inputs/kb_audit_staleness_gap.xlsx 和 inputs/kb_policy_notes.docx，输出一份简短的决策简报，说明现在应该优先处理哪些内容、为什么、以及最终推荐的处理顺序。重点看三件事：哪些条目已经明显过期、哪些主题还存在内容缺口、以及有没有重复或低质量内容拖累检索效果。
```

### 553. D8_g980914_zh (domain=D8, difficulty=6)

```
你是知识库运营分析助手。请基于提供的知识库文章和使用日志，完成一次数据调研与清洗分析任务，识别知识库中可能需要处理的异常内容，并为后续人工复核提供依据。
```

### 554. D8_g980950_zh (domain=D8, difficulty=6)

```
请基于 kb_articles.xlsx、kb_issues.xlsx、kb_remediation_candidates.xlsx 做一次知识库审计和修复决策，重点围绕“SSO guest access issues”这个场景，判断当前知识库的陈旧性、覆盖缺口和优先修复对象。我需要你输出一个简明的决策稿 decision_brief.md，直接给出排序后的修复建议，并把关键数字写清楚。请同时识别重复内容碰撞、过期但仍在发布的条目，以及最应该优先推进的修复候选。
```

### 555. D8_g980994_zh (domain=D8, difficulty=6)

```
需要做一轮知识库审计和补洞评估，目标是给出本周优先处理哪一组知识库问题的决策建议。请基于 inputs/kb_audit_dataset.xlsx 和 inputs/kb_audit_memo.pdf，整理出一份简短的决策简报，说明当前最该优先修哪些内容、为什么，以及要先做哪些动作。
```

### 556. D8_g981153_en (domain=D8, difficulty=6)

```
I need a compact audit report built from kb_audit_bundle.xlsx and kb_audit_brief.pdf. Please review the KB articles, interaction log, quality audit, and gap tracker together, then produce one concise report file that summarizes the main findings for staleness, missing content, duplicate records, quality issues, and overdue remediation work. I also want the report to call out the embedded real seed records that mention kb_search or label 0, because I need those preserved in the final summary. Please keep the output focused on counts, rates, the most frequent tool, and the key remediation priorities.
```

### 557. D8_g981218_zh (domain=D8, difficulty=6)

```
我需要你帮我做一次知识库审计。目前有两个文件：一个是知识库文章列表（kb_articles.xlsx），另一个是审核日志（kb_audit_log.xlsx）。请分析完整度、过期情况、答案一致性、内容质量、覆盖率，以及两个文件之间的数据一致性。最终给我一份 findings.md 汇总报告。
```

### 558. D8_g981267_zh (domain=D8, difficulty=6)

```
我需要你看一下这套知识库审计材料，文件是 kb_audit_main.xlsx、kb_audit_method.xlsx 和 kb_audit_brief.docx，帮我做一份决策简报 decision_brief.md：先把哪些内容最该优先整改排个序，再给出我该先投资源到哪一类问题上，最好能把关键数字一起写清楚，方便我直接拿去跟团队讨论。
```

### 559. D8_g981306_zh (domain=D8, difficulty=6)

```
我们要做一次知识库健康度盘点，重点看文章是否过期、是否有内容缺口，以及该先修哪些条目。
请基于 inputs/kb_articles.xlsx、inputs/search_log.csv 和 inputs/remediation_rules.json，输出一个简短的决策文件，说明这批知识库是应该先整体补修、优先处理哪几类问题，还是可以暂缓。
我更关心的是可执行结论：哪些主题风险最高、哪些文章最该更新、哪些缺口最影响一线检索命中。
```

### 560. D8_g981323_en (domain=D8, difficulty=6)

```
Use kb_inventory.xlsx, gap_tracker.xlsx, and kb_audit_memo.pdf to give me one ranked decision brief for the KB cleanup plan. I need the best recommendation for what to fix first, with the supporting numbers for staleness, gap backlog, and coverage.
```

### 561. D8_g981378_zh (domain=D8, difficulty=6)

```
我们准备把知识库做一次梳理，重点看旧内容是否过期、有没有缺口、以及哪些条目需要补录或修正。请基于 inputs/knowledge_audit_file_a.xlsx 和 inputs/knowledge_audit_file_b.xlsx 做一次合并审计，最后输出一份 compact 的汇总报告，能直接给内容运营和知识库负责人看。我更关心哪些条目是高优先级、哪些分类最容易出问题、以及两份文件交叉后到底剩下多少未覆盖或冲突的内容。
```

### 562. D8_g981463_en (domain=D8, difficulty=6)

```
You are given a small evidence bundle with meeting notes, a large audit log, and seed records.
Your task is to produce a concise but structured report that helps the team troubleshoot the login
redirect/callback issue and also summarizes the market analysis request for synthetic monitoring.
Keep the same language style as the source material and stay within the given size constraints.
```

### 563. D8_g981525_en (domain=D8, difficulty=6)

```
You are reviewing a small knowledge-base inventory for a support/content ops workflow.
Use the provided inputs to identify coverage gaps and audit priorities.

Deliverables:
1) Summarize the article inventory and its risk profile.
2) Recommend which articles should be prioritized for review or update.
3) Map the seed scenarios to the most relevant KB articles.

Tool target: function-calling / knowledge-base style analysis.
Subanalysis hint: compare lifecycle status, gap counts, and owner concentration; note the remote-control office PC scenario and the finance/web-search seed.
```

### 564. D8_g981773_zh (domain=D8, difficulty=6)

```
我们现在要把 KB 做一次针对 CloudPay 故障与云存储市场内容的联合审查，因为这会直接影响本周的支付应急方案和对外沟通口径。请基于 inputs/kb_articles.xlsx、inputs/kb_gaps.xlsx、inputs/cloudpay_signals.xlsx 和 inputs/compliance_notes.pdf，整理一份简短但结论明确的决策简报，重点回答：云存储与内容分发这一类知识里，哪些供应商最该优先保留、哪些内容已经明显过时、哪些知识缺口必须先补、CloudPay 这次异常的影响有多大，以及我们更适合继续观望、局部切换还是立刻调整主支付方案。
```

### 565. D8_g981818_zh (domain=D8, difficulty=6)

```
我需要你把这两份知识库审计材料做成一份决策简报：先看 kb_audit_inventory.xlsx 和 kb_gap_backlog.xlsx，再给我一个按优先级排序的整改建议，说明哪些条目该先修、哪些负责人需要重点跟进、以及整体风险和工时大概是什么水平。最后输出成一份简短的决策文件，方便我直接拿去开会。
```

### 566. D8_g981858_en (domain=D8, difficulty=6)

```
We need to clean up our knowledge base before the next review cycle. Please study `kb_audit_source_a.xlsx` and `kb_usage_and_issues_source_b.xlsx` and give me one concise findings report that separates the main audit work from the usage and issue patterns, then pulls it all together with clear cross-file reconciliation where the records disagree. I want the report to call out the stale pages, missing answers, duplicate conflicts, and the most problematic content area, so we can prioritize fixes quickly.
```

### 567. D8_g981879_zh (domain=D8, difficulty=6)

```
我需要你把 kb_audit_sources.xlsx 和 kb_crosscheck_sources.xlsx 这两份资料一起做完一版 KB 审计简报，重点看知识库过期情况、缺失负责人、重复标题、问题单和知识条目的关联情况，再顺带把厂商材料里能提炼的市场判断也放进去。最后请直接输出 findings.xlsx，内容要能给知识库维护和内容运营一起看。
```

### 568. D8_g981913_zh (domain=D8, difficulty=6)

```
请基于 inputs 里的 kb_articles.xlsx、kb_usage_logs.xlsx、kb_audit_findings.xlsx、kb_coverage_targets.xlsx 做一份知识库审计汇总，输出一个合并后的报告文件。我要看出当前知识库的陈旧、空洞和整改优先级，并把关键异常一并列出来。
```

### 569. D8_g982017_en (domain=D8, difficulty=6)

```
I need a consolidated KB audit from the three input files: inputs/kb_audit_dataset.xlsx, inputs/kb_audit_brief.pdf, and inputs/kb_audit_policy_memo.pdf. Please produce one compact report that pulls together the article inventory, staleness review, gap remediation priorities, integrity issues, and the supporting QA/search signals. Focus on the items that are most actionable for governance and remediation, and include a short executive summary plus a small table of the priority findings.
```

### 570. D8_g982026_zh (domain=D8, difficulty=6)

```
请基于 inputs/kb_audit_pack.xlsx 和 inputs/vendor_status_stream.csv 做一次知识库审计与事件复盘，重点围绕 AutomailCRM 这次异常展开，输出一份合并后的简短报告和一份配套明细表。
- 先判断知识库里哪些条目已经明显过时、长期未复核，哪些条目存在创建/更新时间异常或责任归属缺失。
- 再从大型事件流里提取 AutomailCRM 的官方公告、时间线、影响迹象，以及社区里可直接复用的应急建议。
- 把审计发现、事件结论、合规提醒和业务影响放在同一份材料里，给出可执行的短期处理建议和中长期改进建议。
- 报告里要尽量结构化，便于我直接转给管理层和支持团队；明细表保留关键条目、异常点和你引用到的事件证据。
- 只需要最终交付一个压缩过的分析包，不要拆成很多文件。
```

### 571. D8_g982029_zh (domain=D8, difficulty=6)

```
请基于以下三份输入文件做一份知识库审计决策简报：kb_inventory.xlsx、ticket_log.csv、feedback_log.csv。这次我需要你同时看三个角度：条目新鲜度、覆盖缺口、以及工单/反馈里暴露出来的高频问题。最后只输出一份简洁的决策简报，明确建议优先修哪些内容、哪些知识点可以暂缓、以及为什么。请把关键数字写清楚，尤其是过期条目占比、已确认缺口数、以及能够通过知识库直接解决的高频问题。另外把明显需要下架或改写的条目单独列出来。
```

### 572. D8_g983272_zh (domain=D8, difficulty=6)

```
这次要帮我做一次知识库盘点，找出哪些内容已经过期、哪些地方有重复或缺口，并把结果整理成一份能直接拿去开会的简短汇总。请结合 kb_inventory.xlsx、kb_audit_log.txt、gap_register.xlsx 三个文件，把关键发现和需要优先处理的事项放进一个报告里，让我能快速判断该先修哪几类内容。
```

### 573. D8_g994_zh (domain=D8, difficulty=6)

```
我需要你对公司知识库进行一次全量审计与修复计划分析。数据源包括：`knowledge_base.db`（SQLite，表 `articles` 含 id、title、category、tags、content_summary、author、created_date、updated_date、status）、`usage_log.xlsx`（浏览事件含 article_id、view_date、user_role）、`kb_metadata.json`（定义各类别最小文章数、过时阈值、零浏览阈值、修复优先级权重及异常说明），以及 `tag_coverage_gap.csv`（标签预期覆盖与实际覆盖的差距表）。产出三个文件：

1. **remediation_plan.json**：包含 `summary` 对象（total_articles、stale_count、zero_view_count、stale_high_view_count、categories_with_gaps 列表、total_tag_gap、duplicate_titles 列表）和 `top_5_articles` 数组（每项含 article_id、title、priority_score，按优先级降序取前5）。
2. **coverage_gaps.md**：两个 Markdown 表格——表1为类别覆盖缺口（列：Category、Expected、Actual、Gap）；表2为标签覆盖缺口（列：Tag、Expected、Actual、Gap）。
3. **stale_high_priority.csv**：列名 article_id、title、category、last_updated、view_count、priority_score，按优先级分数降序取前10条（不足则全部）。

关键定义和公式：
- **过时文章**：`updated_date` 距基准日期 2025-06-01 超过 365 天，或 `updated_date` 晚于 2025-06-01（未来日期）均视为过时。
- **零浏览文章**：在 `usage_log.xlsx` 中无任何浏览记录的文章。
- **高浏览文章**：所有文章按浏览数降序排列，取前 10%（向上取整）的 article_id；若浏览数相同则全部纳入。
- **优先级分数**：`priority_score = (如果文章同时过时且高浏览则 +5) + (如果过时且不高浏览则 +2)`。零浏览但不符合上述条件的无额外加分。
- **类别内容缺口**：`kb_metadata.json` 中每个 category（包括 Legacy）的 `actual articles < min_articles`。
- **标签缺口**：`tag_coverage_gap.csv` 中 gap > 0 的条目，总缺口为所有 gap 列之和。
- **重复标题**：`articles` 表中 `title` 列出现次数 > 1 的所有标题。

所有数值精确计算并四舍五入到整数；日期比较都以 2025-06-01 为当前时间。请直接开始处理，无需确认步骤。
```

### 574. D8_k982090_en (domain=D8, difficulty=6)

```
Using the CSV file tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv, run a support-ticket analytics deep dive focused mainly on correlation and driver analysis. I want to understand which numeric fields move together, how version relates to priority/queue/language patterns, and what the strongest rounded associations are across this dataset. Please split the work into independent tracks so multiple sub-analysts could work in parallel: one track for numeric correlation structure, one for version-linked patterns, one for priority/queue cross-drivers, one for language-based differences, and one for tag/issue-theme associations. Use the real columns subject, body, answer, type, queue, priority, language, version, and tag_1 through tag_8. I need a concise analysis summary plus a few deterministic validation checks.
```

### 575. D8_k982247_en (domain=D8, difficulty=6)

```
Using the file tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv, please run a support-ticket analytics review focused mainly on temporal / trend analysis over the data’s sequence fields. I want a concise but decision-ready readout on how ticket volume and ticket characteristics change over time, especially changes in issue mix, priority, language, and tags, plus any evidence of period-over-period shifts in workload or escalation risk. Please use the real columns subject, body, answer, type, queue, priority, language, tag_1 through tag_8, and infer time only if the dataset supports an explicit sequence/order proxy. Break the work into independent tracks so different analysts could handle them in parallel, and make sure the final summary is easy to use for knowledge/support operations planning.
```

### 576. D8_k982489_en (domain=D8, difficulty=6)

```
Using the dataset in tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv, run a support-ticket analytics review focused mainly on correlation and driver analysis. I need a concise but rigorous readout of which fields move together and what the strongest associations are, using the real columns subject, body, answer, type, queue, priority, language, version, and tag_1 through tag_8. Please split the work into a few independent tracks so different analysts can work in parallel: one track on numeric/categorical driver patterns tied to version, one on tag-based co-occurrence and associations, one on queue/priority/type cross-drivers, one on language-related patterns, and one on missingness / data quality signals that could distort correlations. Keep everything deterministic and based on counts, grouped summaries, or rounded correlations only.
```

### 577. D8_k982559_en (domain=D8, difficulty=6)

```
Use the file tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv and analyze this support-ticket data for correlation and driver patterns across the real columns subject, body, answer, type, queue, priority, language, tag_1 through tag_8. I need a compact but rigorous readout of which fields move together, what the strongest rounded correlations are between ticket metadata/label indicators we can derive from the text tags, and which combinations look like the clearest drivers of escalated or delayed support. Please break it into a few independent workstreams so I can hand them to different assistants, and keep the output focused on concrete counts, correlations, and top associations rather than narrative.
```

### 578. D8_k982583_en (domain=D8, difficulty=6)

```
Please analyze the file `inputs/tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv` using the real columns `subject`, `body`, `answer`, `type`, `queue`, `priority`, `language`, and `tag_1` through `tag_8`. I need a support-ticket analytics summary focused mainly on temporal or sequence-style trend analysis using the dataset ordering as the sequence axis (for example, how ticket mix changes from the start to the middle to the end of the file, period-over-period shifts, and whether categories become more or less frequent over the sequence). Break this into independent workstreams so different analysts could work in parallel: one track on trend shifts in `type`, one on queue/priorities over the sequence, one on language mix over time/order, one on tag prevalence and co-occurrence changes, and one on text-length / content complexity trends in `subject`, `body`, and `answer`. I want a concise deliverable named `analysis_summary.json` with the main findings, and I also want deterministic validation checks that can be reproduced directly in pandas from the loaded dataframe.
```

### 579. D8_k982826_zh (domain=D8, difficulty=6)

```
请基于文件 tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv 做一版知识/支持工单分析，重点围绕“排名与集中度”来展开：先找出最常见的工单类型、队列、优先级、语言，以及 tag_1 到 tag_8 中出现频率最高的标签；再评估这些头部类别/标签对整体工单量的集中程度（例如 Top-N 占比、Top1/Top3/Top5 占比、是否存在明显的帕累托特征）；同时比较不同队列、语言、优先级之间的头部模式是否一致。请把结果整理成一个适合管理层快速阅读的 summary，并给出可以直接落地的结论：哪些类别最集中、哪些长尾最明显、哪些组合最值得优先关注。注意要结合 subject、body、answer、type、queue、priority、language、tag_1~tag_8 这些真实列来分析，不要编造字段。
```

### 580. D8_k983036_en (domain=D8, difficulty=6)

```
Using the file `tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv`, please run a support-ticket concentration analysis for knowledge management. I want to understand where volume is most concentrated and whether a small number of categories dominate the workload. Please use the real columns `type`, `queue`, `priority`, `language`, `tag_1` through `tag_8`, plus `subject`, `body`, and `answer` only as needed for context. Break this into independent tracks so different people can work in parallel: (1) top categories and queues by ticket count with shares of total, (2) Pareto-style concentration for the most common values in `type`, `queue`, `priority`, and `language`, (3) how concentrated the tag system is overall and which tags dominate across `tag_1` to `tag_8`, (4) whether concentration changes when filtering by `language` or `priority`, and (5) a brief operational summary highlighting the biggest bottlenecks and any extreme skew. Please keep the analysis deterministic and grounded in the dataset only.
```

### 581. D8_k983081_zh (domain=D8, difficulty=6)

```
请基于文件 tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv 做一份知识/支持工单分析，重点放在不同分类分组之间的对比：比如 queue、priority、language、type、tag_1 这些类别下的工单量、占比、平均响应长度/工单长度差异，以及哪些分组之间的差距最大。请把分析拆成几个彼此独立的部分，适合并行处理，并最终汇总成一份面向业务的结论。特别关注：1) 不同 queue 的工单量和高优先级占比差异；2) 不同 language 的工单量、平均 body 长度、平均 answer 长度差异；3) 不同 type 的分布及在各 queue 中的偏好差异；4) 不同 priority 的 body/answer 长度差异；5) tag_1 中高频标签的跨 queue、跨 language 表现差异；6) 找出最明显的分组差距并给出可执行的运营建议。
```

### 582. D8_k983144_en (domain=D8, difficulty=6)

```
Use the file tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv and analyze it as a knowledge/support-ticket analytics dataset. I need a segment-comparison review focused mainly on categorical-group gaps: compare answer lengths, queue mix, priority mix, language mix, and tag patterns across segments, then identify the biggest differences between groups that could matter operationally. Please break this into a few independent workstreams so they can be handled in parallel: one track on queues, one on priorities, one on languages, one on tag coverage/patterns, and one on cross-segment text-size differences in subject/body/answer. Summarize the most meaningful gaps and any concentration or imbalance you find, using the real columns subject, body, answer, type, queue, priority, language, and tag_1 through tag_8.
```

### 583. D8_k983245_en (domain=D8, difficulty=6)

```
Using the file tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv, analyze the support-ticket dataset with a focus on correlation and driver analysis: determine which numeric fields move together, report rounded correlations, and identify the strongest associations that can explain ticket outcomes. Please break the work into separate threads covering ticket volume by version/language, priority and queue patterns, relationships among tags and ticket types, missing-data patterns, and any numeric correlation structure you can derive from the available fields. I need a concise analyst-ready summary that highlights the main drivers and any notable associations across the dataset.
```

### 584. D8_k983269_en (domain=D8, difficulty=6)

```
Using the file tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv, run a support-ticket analytics review centered on temporal/sequence behavior in the version field. I need to know whether ticket volume, priority mix, and queue/type composition change across versions, and whether those shifts differ by language. Please also check whether certain tags become more common in later versions and whether the answer length or missingness patterns change over time. Break this into independent workstreams so they can be analyzed in parallel, and give me a concise decision-ready summary plus a machine-readable JSON output.
```

### 585. D8_k983458_en (domain=D8, difficulty=6)

```
Use the file tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv to run a support-ticket analytics deep dive with a strong temporal/trend focus. I need you to examine how ticket volume and ticket mix change across the sequence field version, especially period-over-period shifts and any spikes or drops. Break it into a few independent workstreams so they can be analyzed in parallel: one track on overall volume trends by version and language, one on how queue/type/priority distributions evolve over time, one on whether the content fields (subject/body/answer) show changes in length or missingness over versions, one on whether tags become more or less common over time, and one on cross-language differences in the trend patterns. Please produce a concise analysis summary JSON with the most important findings and the key numbers behind them.
```

### 586. D8_k983626_zh (domain=D8, difficulty=6)

```
请基于文件 samyakrajbayar__python-questions-faq-dataset__python_faq_dataset.csv 做一份面向知识/支持工单的分析，重点放在时间/序列维度的趋势变化上。数据里没有显式日期，所以请把 quality_score、score、q_length、a_length 以及 difficulty 当作序列/分层轴，重点看不同质量分段、长度分段、难度层级之间的变化趋势、占比变化和相关性。我需要一份能直接给团队讨论的结果：先判断高质量问题是否集中在某些主题、标签和难度层；再看短问题/长答案与质量分数之间的关系；再做一个类似“从低到高”的分段趋势分析，比较各分位段的平均 score、平均 a_length、平均 q_length 和难度分布；最后总结出最值得优先优化的内容模式。请拆成 4-6 个彼此独立的分析轨道，方便不同人并行做。输出时请给我可核对的定量结果和简洁结论，不要画图。
```

### 587. D8_k983781_zh (domain=D8, difficulty=6)

```
请基于文件 safrin03__predictive-analytics-for-customer-churn-dataset__train.csv 做一份面向“知识/客服支持票据分析”的分群对比分析，重点围绕不同客户分组之间的流失率、支持工单率和关键行为均值差异来找出最大差距。请直接使用这些列：AccountAge、MonthlyCharges、TotalCharges、SubscriptionType、PaymentMethod、PaperlessBilling、ContentType、MultiDeviceAccess、DeviceRegistered、ViewingHoursPerWeek、AverageViewingDuration、ContentDownloadsPerMonth、GenrePreference、UserRating、SupportTicketsPerMonth、Gender、WatchlistSize、ParentalControl、SubtitlesEnabled、Churn。我要你把分析拆成几条彼此独立的分析线并并行推进：先比较不同订阅类型、支付方式、账单方式、内容类型、设备/功能使用习惯下的流失率与支持工单均值；再找出各类别里流失率最高/最低的组以及差值最大的组对；再把支持工单和观看行为联系起来，看哪些人群最容易高工单高流失；最后给出一份可落地的优先排查人群清单。所有结论都必须基于真实数据、可复核、以分组均值/比例/差值为主，不要建模，不要预测，不要画图。需要输出一个能让团队直接分工执行的分析摘要文件 analysis_summary.json。
```

### 588. D8_k983915_zh (domain=D8, difficulty=6)

```
请基于文件 `imoore__60k-stack-overflow-questions-with-quality-rate__train.csv`（已知列：Id、Title、Body、Tags、CreationDate、Y；共1500行）做一次面向知识库/支持工单质检的异常与离群分析。重点不要做预测模型，而是用明确的数值规则识别异常：例如长度 IQR 离群、极端标签数量、罕见标签、代码块/链接密度异常、异常创建时间、重复标题等。请把结果组织成可审计的规则、指标和异常样本摘要，用于后续人工复核低质量或可疑工单。
```

### 589. D8_k984025_zh (domain=D8, difficulty=6)

```
请基于文件 aniketg11__supportticketsclassification__all_tickets.csv 做一份支持工单分析，重点围绕时间/序列趋势来展开。请把分析拆成几条互相独立的线：一条看工单类型、类别、优先级/影响的整体分布是否随时间段有变化；一条看不同业务服务在序列上的占比变化和增长/下降最快的部分；一条看标题和正文长度、缺失情况或异常短文本是否和某些标签组合有关；一条看子类目与高紧急度/高影响工单在不同类别下的集中度；一条看题目中常见关键词在不同工单类型上的出现趋势；如果你发现明显的阶段性波动，请尽量量化为前后期对比、环比或分段差异。最终请输出可直接落地的分析结论摘要，并把所有关键统计结果整理成 analysis_summary.json。
```

### 590. D8_k984163_en (domain=D8, difficulty=6)

```
Using therohk__cyc-kb__cycmodel-extract.csv, please build a compact support-ticket knowledge audit focused on ranking and concentration. I need to know which ontology patterns and term families dominate the extract, where the long tail starts, and whether a small set of labels or term types accounts for most of the dataset. Please use the real columns tagName, termId, termAbout, termLabel, cycAnnot, termType, subClassOf, subPropertyOf, disjointWith, broaderTerm, superTaxons, requiredActorSlots, partitionedInto, quotedIsa, prettyString, comment, domain, range, arity, argsFormat, argsGenl, argsIsa, argsQuotedIsa, resultGenl, resultIsa, resultQuotedIsa, wikiName, dbpediaName, and synsetDenotes. I want a production-style summary that separates the analysis into a few independent tracks so different teammates can work in parallel.
```

### 591. D8_k984243_zh (domain=D8, difficulty=6)

```
请基于文件 samanemami__yeastcsv__yeast.csv 做一版面向知识/支持工单分析的分群对比报告。数据里有 8 个数值字段（mcg、gvh、alm、mit、erl、pox、vac、nuc）和一个分类字段 name。我要重点看不同 name 分组之间的指标差异：先做各组均值/中位数对比，找出组间差距最大的特征；再看各组样本量、异常稀有组和类别不平衡情况；然后分析“高值特征组合”在不同组里的出现率（比如某些字段高于整体中位数的比例）；最后补充字段间相关性在全体与分组内是否一致。请把结果整理成适合管理层快速阅读的分析摘要，并明确指出哪些组最像、哪些组差异最大、差异主要体现在哪些字段上。
```

### 592. D8_k984326_zh (domain=D8, difficulty=6)

```
请基于文件 parthpatil256__it-support-ticket-data__IT Support Ticket Data.csv 做一版可直接给管理层看的支持工单趋势分析，重点围绕时间序列/序列变化来展开。这个数据里只有现成字段：Unnamed: 0、Body、Department、Priority、Tags，没有明确日期列，所以请把 Unnamed: 0 当作工单进入系统的顺序索引，按它从小到大近似代表时间顺序，分析“前段 vs 后段”的变化、分段趋势、以及不同部门/优先级/标签组合在序列上的变化。我要的不只是静态统计，而是要看：整体工单量和高优先级占比是否在后期上升，哪些部门的工单量增长最快，优先级分布是否发生漂移，哪些标签在后半段更常出现，以及是否存在某些部门的高优先级工单增长尤其明显。请把结果整理成可执行的分析结论，适合用于后续资源调配和排障优先级调整。
```

### 593. D8_k984334_zh (domain=D8, difficulty=6)

```
请基于文件 suraj520__customer-support-ticket-dataset__customer_support_tickets.csv 做一份面向管理层的客服工单分层分析，重点围绕“不同客群/产品/渠道/优先级之间的表现差异”来找出最值得优先优化的环节。请结合这些字段：Ticket Status、Ticket Priority、Ticket Channel、Ticket Type、Ticket Subject、Product Purchased、Customer Gender、Customer Age、Customer Satisfaction Rating、First Response Time、Time to Resolution、Resolution。我要的不是简单汇总，而是要拆成可并行的 4-6 个分析轨道，分别比较各分组的工单量、关闭率、满意度、响应/解决时长，以及不同群体之间最大的差距；同时识别最差的细分组合、最强的细分组合，并判断这些差异是否主要由渠道、优先级还是产品驱动。最后请输出一份可直接给业务方讨论的结构化结论草稿。
```

### 594. D8_k984353_zh (domain=D8, difficulty=6)

```
请基于文件 safrin03__predictive-analytics-for-customer-churn-dataset__train.csv 做一份面向“知识/客服工单分析”的分层数据分析，重点围绕“分布与阈值 cohort（高/低于业务阈值的人群计数、分位数组、占比结构）”来展开。请不要建模，先把客户按可运营阈值切开，做出能直接给业务看的结论。

请至少拆成 5 个彼此独立的分析轨道，分别覆盖：
1）流失率在关键阈值上的分布：例如 AccountAge、MonthlyCharges、SupportTicketsPerMonth、ViewingHoursPerWeek、AverageViewingDuration 的高/低阈值 cohort；
2）支持工单密度与流失：按 SupportTicketsPerMonth 分层、并查看不同订阅/支付方式下的 mix share；
3）使用强度与内容消费分布：ViewingHoursPerWeek、AverageViewingDuration、ContentDownloadsPerMonth 的分位数组与高低分层占比；
4）收入/账单结构：MonthlyCharges、TotalCharges 的分位数分层、以及 PaperlessBilling 与 Churn 的结构差异；
5）客户画像组合：SubscriptionType、ContentType、MultiDeviceAccess、DeviceRegistered、ParentalControl、SubtitlesEnabled 的组合分布和流失差异；
6）异常/高风险运营人群：例如低 AccountAge + 高工单 + 高月费 的交集 cohort，给出这些 cohort 的规模和流失占比。

输出请以可直接落地的摘要为目标，先给我一个 analysis_summary.json 的结构化结论框架，再给出每个阈值 cohort 的计数、占比、以及流失率对比。所有阈值请使用数据分位数或明确的二元切分（高于/低于中位数、四分位、或业务可解释阈值），不要自行编造新字段。请确保结论可以被复核。文件中的真实字段包括：AccountAge, MonthlyCharges, TotalCharges, SubscriptionType, PaymentMethod, PaperlessBilling, ContentType, MultiDeviceAccess, DeviceRegistered, ViewingHoursPerWeek, AverageViewingDuration, ContentDownloadsPerMonth, GenrePreference, UserRating, SupportTicketsPerMonth, Gender, WatchlistSize, ParentalControl, SubtitlesEnabled, CustomerID, Churn。
```

### 595. D8_k984489_zh (domain=D8, difficulty=6)

```
请基于文件 sevgisarac__temperature-change__FAOSTAT_data_en_11-1-2024.csv 做一份面向“知识/支持工单分析”的异常检测报告。重点不要只做简单汇总，而是围绕“显式数值规则的异常与离群值识别”来展开：例如用固定阈值（如绝对温度变化大于 2℃）、IQR 规则、极端年份/月份、稀有类别（Area、Months）和重复/缺失线索，找出最需要人工复核的记录与对象。请结合列 Domain、Area、Element、Months、Year、Unit、Value、Flag、Flag Description 等字段，判断哪些区域、哪些月份、哪些年份更容易出现极端值或疑似异常，并给出可操作的排查建议。希望你把工作拆成 4-6 个彼此独立的分析轨道，方便不同子任务并行：1）全局异常值与离群点；2）按地区/国家的异常集中度；3）按月份与季节的异常模式；4）按年份的异常趋势与突变；5）Flag/Flag Description 与异常值的一致性；6）稀有类别和潜在数据质量问题。最后输出一份可供知识库/支持工单团队直接使用的摘要，突出“需要人工跟进的优先级清单”和“可自动化筛查的规则”。
```

### 596. D8_k984508_en (domain=D8, difficulty=6)

```
Using the file parthpatil256__it-support-ticket-data__IT Support Ticket Data.csv, build a support-ticket analytics readout focused mainly on temporal / trend analysis. I need a concise but rigorous summary of how ticket volume, priority mix, and department mix change over the ticket sequence in the dataset (use Unnamed: 0 as the ordering/index if there is no true date field), including period-over-period and rate-of-change style comparisons. Please also connect those trends to ticket content signals from Body and Tags so I can see whether specific issue types are becoming more or less common over time. Make it practical for an IT support manager: identify the biggest shifts, any spikes or dips, and any consistent patterns by Department and Priority, with the work split so different analysts can handle separate tracks in parallel.
```

### 597. D8_k984519_en (domain=D8, difficulty=6)

```
Using aniketg11__supportticketsclassification__all_tickets.csv, do a support-ticket analytics deep dive focused mainly on correlation and driver analysis across the numeric fields. I want you to treat ticket_type, category, sub_category1, sub_category2, business_service, urgency, and impact as the main variables, and also use title/body text only for light context if needed. Please split the work into separate tracks so it can be handled in parallel: identify which numeric fields move together most strongly, summarize the strongest positive and negative pairwise correlations, compare correlation patterns within key ticket_type/category slices, check whether urgency and impact behave differently across categories/subcategories, and flag any unusual combinations or missingness that might distort the driver story. Keep the output practical for an operations audience and include a concise summary of the top associations and any caveats.
```

### 598. D8_k984564_en (domain=D8, difficulty=6)

```
Using harshitstark__healthcare-documentation-database__Healthcare Documentation Database.csv, analyze the healthcare documentation database as a support-ticket style text corpus. I need a temporal/sequence-focused review of how the content changes across the dataset order, since there is no date column. Please treat Serial No as the sequence key and look for period-over-period shifts in volume, document length, specialty mix, and recurring issue categories. Break it into independent workstreams so different analysts can work in parallel: 1) sequence/order trends in transcription length and keyword richness, 2) changes in medical_specialty mix across early/mid/late segments, 3) recurring complaint/problem patterns in descriptions and keywords over the sequence, 4) consistency checks for cleaned_transcription coverage and missingness, and 5) compare the longest vs shortest documentation records to see what kinds of tickets are driving extremes. Summarize the findings in analysis_summary.json with clear trend tables and key takeaways.
```

### 599. D8_k984753_en (domain=D8, difficulty=6)

```
Analyze the support-ticket dataset in aniketg11__supportticketsclassification__all_tickets.csv, focusing mainly on temporal / sequence-based trend analysis using the available rows order as the sequence. I want a compact analyst-style writeup that identifies how ticket volume and ticket mix change over time, especially period-over-period shifts in ticket_type, category, sub_category1, sub_category2, business_service, urgency, and impact. Break the work into independent tracks so different people could handle them in parallel: (1) overall row-order trend and period-over-period volume change, (2) changes in ticket_type composition over early vs late portions of the dataset, (3) trend shifts in category and sub_category frequencies across sequential buckets, (4) whether urgency and impact patterns change over the sequence, and (5) a short outlier-focused check for unusually concentrated categories/services in the most recent portion versus the earlier portion. Use only the real columns in the file and make the findings operationally useful for support-ticket planning.
```

### 600. D8_k984760_zh (domain=D8, difficulty=6)

```
请基于文件 samyakrajbayar__python-questions-faq-dataset__python_faq_dataset.csv 里的数据做一份面向知识/支持工单分析的简报，重点放在时间/序列趋势上：先把 score、q_length、a_length、quality_score、difficulty、topic、source、tags 这些字段按时间顺序做趋势检查（如果没有显式日期，就按数据在文件中的原始顺序作为序列），再拆成几个独立分析方向，最后输出一份可交付的 analysis_summary.json。我要你重点看：1）整体质量分数和问题/答案长度是否随序列变化；2）不同 difficulty/topic/source 的占比是否在前后段发生变化；3）高分/低分样本在序列中的分布是否有漂移；4）tags 的常见类别是否在前后段更集中；5）关键字段之间是否存在稳定相关性；6）找出最值得我后续优先排查的异常趋势点。请直接给结论，不要写泛泛而谈。
```

### 601. D8_k984823_en (domain=D8, difficulty=6)

```
Using the file thedevastator__sciq-a-dataset-for-science-question-answering__train.csv with columns question, distractor3, distractor1, distractor2, correct_answer, and support, run a support-ticket style knowledge analysis focused mainly on temporal / trend analysis over the available sequence structure in the data. I need a multi-part review that treats row order as the sequence, checks whether answer patterns shift over the dataset, and breaks the work into independent tracks so different analysts can work in parallel. Please include: (1) overall row-order trend diagnostics on answer-length and support-length, including period-over-period change between early and late portions of the file; (2) whether the distribution of correct answers and distractors changes across sequence quartiles; (3) how frequently the correct answer exactly matches one of the distractors, and whether that rate changes over the sequence; (4) question/support text overlap trends over the file; and (5) a compact anomaly review of the longest and shortest support passages and question lengths. Summarize only from the dataset itself; do not invent any dates or external metadata.
```

### 602. D8_k984947_zh (domain=D8, difficulty=6)

```
请基于文件 ananthu017__squad-csv-format__SQuAD_csv.csv 做一份面向“知识库/支持工单”场景的分析，重点看问题与答案文本在数据中的排名与集中度表现：比如高频问题类型、最常见答案实体、少数高频条目是否占据大部分样本、以及长尾分布情况。请结合现有列（Unnamed: 0、context、question、id、answer_start、text）做一个可执行的分析方案，最好能拆成几条可以并行推进的分析线，并最终输出 analysis_summary.json。我要的不是泛泛描述，而是能直接落地的统计分析结果，尽量给出 Top-N、占比、累计覆盖率、以及必要的交叉对比。
```

### 603. D8_k984970_en (domain=D8, difficulty=6)

```
Using nasa__fireballs__cneos_fireball_data.csv, analyze the fireball records as if they were incident/support-ticket events over time. Focus mainly on temporal trend analysis: identify whether event frequency, radiated energy, and impact energy show meaningful changes over the years, and call out any period-over-period shifts or spikes. Please also segment the data by missing-vs-present location/trajectory fields so we can see whether data completeness changed over time, and compare the strongest events with the rest of the sample using the real columns Peak Brightness Date/Time (UT), Latitude (deg.), Longitude (deg.), Altitude (km), Velocity (km/s), vx, vy, vz, Total Radiated Energy (J), and Calculated Total Impact Energy (kt).
```

### 604. D8_k985031_zh (domain=D8, difficulty=6)

```
请基于文件 albertobircoci__support-ticket-priority-dataset-50k__Support_tickets.csv 做一份面向知识/支持工单管理的分析，重点围绕“排名与集中度”：先找出哪些因素最集中地驱动高优先级工单，再看头部组合是否形成明显的 Pareto 结构，并把结果拆成可并行推进的几条分析线。请重点使用真实列名（例如 priority、priority_cat、industry、customer_tier、region、product_area、booking_channel、reported_by_role、customer_sentiment、customers_affected、error_rate_pct、downtime_min、payment_impact_flag、security_incident_flag、data_loss_flag、has_runbook、past_30d_tickets、past_90d_incidents、day_of_week、company_size 等），不要臆造任何字段。最终请输出一份适合业务汇报的结构化结论，包含：1）高优先级工单的头部来源与集中度；2）高风险特征组合的排名；3）不同维度的 Pareto/集中度对比；4）高优先级与低优先级在关键字段上的差异；5）给出可执行的支持运营启示。若需要，可以按多个独立分析轨道并行处理，再汇总成一份简洁的结论。
```

### 605. D8_k985129_zh (domain=D8, difficulty=6)

```
请基于文件 sovannt__world-bank-youth-unemployment__API_ILO_country_YU.csv 做一份面向“知识/支持工单分析”视角的多阶段分析，但重点放在“排名与集中度”上：把各国家/地区在 2010–2014 年的青年失业率当作工单压力或问题热度的代理指标，找出每一年最突出的国家/地区、这些头部国家/地区占整体的集中度、以及 5 年里是否存在持续霸榜或快速上升的对象。请先按 Country Name、Country Code 和年份列理解数据结构，再围绕 top-N、占比、Pareto/集中度、年度排名变化、以及五年平均值的头部集中情况展开。最终请输出适合管理层读的结论摘要，并在附录里给出可复核的指标口径和关键排名结果。
```

### 606. D9_g397_zh (domain=D9, difficulty=6)

```
我需要你基于 inputs/ 目录下的 vulnerabilities.xlsx、assets.csv、patch_status.csv 和 exploit_intelligence.xlsx 做一个综合安全风险决策分析。输出一个 recommendation.json，汇总严重级别分布、风险评分、Top10紧急项、超期统计、利用情况、修复状态、超期最多资产，以及决策建议。按标准风险分析方法处理即可。
```

### 607. D9_g980796_zh (domain=D9, difficulty=6)

```
这次需要尽快把遗留漏洞整改情况整理成一份可直接给管理层看的汇总，重点是判断哪些资产和问题最该先处理，并把两份输入资料里的信息合并成统一口径。请读取 inputs/remediation_findings.xlsx 和 inputs/scanner_audit_log.txt，输出一份精简但完整的中文报告。我要看到总体数量、按严重等级的汇总、按优先级排出来的前10项，以及需要重点盯住的资产ID。报告不要做成逐条明细表，控制在一页多一点的汇总感即可。
```

### 608. D9_g980804_en (domain=D9, difficulty=6)

```
Triage the vulnerability set in inputs/vulnerability_triage_register.xlsx and cross-check it with inputs/asset_risk_profile.csv and inputs/triage_activity.log. I need one compact decision brief that ranks the top remediation priorities and calls out the assets I should escalate first.
```

### 609. D9_g980967_zh (domain=D9, difficulty=6)

```
请基于 inputs/findings_inventory.xlsx、inputs/asset_context.xlsx 和 inputs/triage_policy.xlsx 出一份安全漏洞修复分流汇总，输出一个 xlsx 总表和一份简短 PDF 说明。我要看总量、严重度分布、状态分布、Top 10 紧急项，以及需要重点盯住的资产名单。
```

### 610. D9_g981378_en (domain=D9, difficulty=6)

```
I need a security triage brief based on the vulnerability database (vulnerability_database.xlsx) and the remediation policy (remediation_policy.pdf). Please compute severity counts (Critical/High/Medium/Low using the CVSS thresholds defined in the policy), a top-10 list of most urgent findings using the risk formula from the policy, and flag all asset IDs that have any SLA breach (by the policy's SLA rules). Also include any cross-source reconciliation notes. Output a single findings.md file with these aggregates.
```

### 611. D9_g981386_zh (domain=D9, difficulty=6)

```
请基于 inputs/findings_inventory.xlsx、inputs/asset_context.xlsx 和 inputs/triage_notes.json 做一份简短的风险 triage 分析，输出 findings.md。我要看到跨源冲突怎么处理、总体严重性和状态汇总、最紧急的前 10 个问题，以及需要优先盯住的少量资产 ID。
```

### 612. D9_g981613_zh (domain=D9, difficulty=6)

```
请基于 inputs/vulnerability_registry.xlsx、inputs/control_owners.csv、inputs/scan_activity.log、inputs/committee_brief.json 和 inputs/scan_activity.log 里能交叉核对到的记录，整理一份用于风险委员会拍板的简报。我只需要一个简短的 decision_brief.md：先给出按严重度和状态汇总后的总体态势，再列出按统一风险分排序的前 10 个最紧急问题，并点名需要优先盯住的少数资产。请把结论写得像内部决策材料，能直接拿去开会。
```

### 613. D9_g981865_en (domain=D9, difficulty=6)

```
You are given asset inventory and vulnerability findings for a small enterprise environment. Analyze the data and produce a concise remediation brief that: (1) identifies the most urgent findings, (2) quantifies the main risk patterns and data quality issues, and (3) recommends a prioritized remediation strategy. Use only the provided files.
```

### 614. D9_g981962_zh (domain=D9, difficulty=6)

```
请基于 inputs/vulnerability_findings.xlsx、inputs/asset_inventory.xlsx 和 inputs/remediation_policy.docx 做一次漏洞整改分诊汇总，输出一份 compact 的总览报告。我要看分 severity 的数量、状态分布、SLA 超期情况、按统一风险分排序的 TOP 10 以及需要重点盯住的少量资产 ID；不要展开成逐条漏洞登记册。
```

### 615. D9_g981971_zh (domain=D9, difficulty=6)

```
请结合 `remediation_findings.xlsx`、`scan_metadata.csv` 和 `policy_rules.json` 做一次安全漏洞修复分诊，输出一份简短的决策文件，帮我判断当前最该优先推进哪些资产和漏洞。
- 先把所有记录按严重度、状态和是否超 SLA 做一个汇总，给出总量和关键占比。
- 按风险高低列出最紧急的前 10 项，并说明它们为什么排在前面。
- 标出最需要盯住的少量资产 ID，方便我直接拉 owner 跟进。
- 最后给我一个清晰的优先级结论：先修哪一类、哪几个资产，理由用数字说话。
- 输出文件只要一份，尽量简洁，适合直接发给管理层看。
```

### 616. D9_g982055_en (domain=D9, difficulty=6)

```
You are auditing a vulnerability inventory pack. Using the provided workbook and reference notes, produce a concise reconciliation that deduplicates repeated findings, identifies which findings link to known CVEs, and summarizes the risk picture for the current week.
```

### 617. D9_g982813_en (domain=D9, difficulty=6)

```
I need a compact decision brief from the security triage data in security_triage_main.xlsx, triage_settings.json, and remediation_plan.csv. Please reconcile the findings, flag the highest-risk assets, and give me a short ranked recommendation with the supporting counts and the top urgent findings.
```

### 618. D9_k982220_en (domain=D9, difficulty=6)

```
Using subhajournal__iotintrusion__IoT_Intrusion.csv, do a security-analytics review focused mainly on segment comparison across categorical groups: compare rates, means, and share differences across attack labels and protocol/service indicators, then identify the biggest gaps between segments. I need this broken into independent workstreams so a small sub-agent team can split the work: one track should compare label-level traffic behavior (e.g., flow_duration, Duration, Rate, Srate, Drate), another should compare protocol-service segments (HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC and TCP/UDP/DHCP/ARP), another should inspect flag/count behavior across labels, another should quantify which labels are most enriched for each categorical indicator, and another should summarize the most distinct numeric signatures by label. Use the actual columns in the file, including label and the categorical one-hot fields, and produce a concise analysis summary in analysis_summary.json.
```

### 619. D9_k982249_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全分析的异常与离群检测专项分析，重点围绕“显式数值规则”来找出可疑流量：例如按阈值筛选极端 src_bytes / dst_bytes / duration / count / srv_count / 速率类指标，结合 IQR、极值、稀有类别（protocol_type、service、flag）以及标志位组合，识别最异常的记录、最异常的类别组合和最容易出现异常的特征。请把结论整理成可直接给安全运营团队使用的简报式输出，并尽量给出可复核的统计口径。

我希望你把工作拆成 4-6 条相互独立的分析线并行推进，至少包括：1）基于数值阈值与 IQR 的异常样本筛查；2）按 protocol_type / service / flag 的稀有类别与异常率分析；3）高风险特征组合（如高 count、低 same_srv_rate、高 serror_rate 等）的共现分析；4）anomaly 与 normal 的分布差异对比；5）极端值与多重规则命中的样本清单。请最终输出一份结构化的分析摘要 JSON。
```

### 620. D9_k982262_zh (domain=D9, difficulty=6)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的分组对比报告，重点围绕“不同攻击/流量段之间的特征均值、比例和差异最大点”来展开。请直接读取并分析这些列：label、flow_duration、Header_Length、Protocol Type、Duration、Rate、Srate、Drate，以及各类标志位和协议指示列（如 fin_flag_number、syn_flag_number、rst_flag_number、ack_count、syn_count、HTTP、HTTPS、DNS、TCP、UDP、DHCP、ARP、ICMP 等）。我希望你把这份数据拆成 4-6 个彼此独立的分析轨道，分别比较各 label 组的均值/占比、找出组间差距最大的特征、识别最典型的协议与标志位组合、以及检查是否存在明显的类别不平衡或某些组的特征极端值。输出时请给出可执行的结论摘要，指出最值得关注的攻击类别差异和可用于后续检测规则设计的信号。
```

### 621. D9_k982415_en (domain=D9, difficulty=6)

```
Analyze the security analytics dataset in subhajournal__iotintrusion__IoT_Intrusion.csv with an emphasis on temporal / trend analysis over sequence-like behavior and rate changes. I need a compact but rigorous incident-style review that looks for how traffic evolves across the rows and whether any attack families show different progression patterns in flow_duration, Duration, Rate, Srate, and Drate. Use the real columns in the file, especially flow_duration, Duration, Rate, Srate, Drate, Protocol Type, ack_count, syn_count, fin_count, urg_count, rst_count, the transport/protocol indicator columns (TCP, UDP, DHCP, ARP, HTTP, HTTPS, DNS, Telnet, SMTP, SSH, IRC), and label. Break the work into independent tracks that can be handled in parallel: one track should profile overall row-order trends and change points in the rate features; one should compare trend behavior by label/attack family; one should isolate protocol-specific shifts across TCP vs UDP vs ARP/DHCP-heavy records; one should quantify flag/count bursts and their association with spikes in Rate/Srate/Drate; and one should summarize the most abrupt row-to-row transitions in the dataset. I want the final output written as analysis_summary.json with concise, decision-ready findings.
```

### 622. D9_k982497_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的分层排查报告，重点围绕“排名与集中度”来判断测试流量是否被少数协议/服务/标志状态主导，以及这些高频组合是否带来更高的异常信号。请至少覆盖 4-6 条彼此独立的分析线：1）按 protocol_type、service、flag 分别做 Top-N 排名与占比集中度（比如前几类是否覆盖了大部分样本）；2）找出最常见的 protocol_type-service-flag 组合，并判断其在整体中的集中度；3）比较高频类别与低频类别在 src_bytes、dst_bytes、count、srv_count 上的差异；4）检查关键异常相关指标（serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate）在高频组内是否更偏向攻击型特征；5）从 dst_host_* 相关主机侧特征里找出最常见模式及其集中度；6）给出一个可以直接交给同事继续深挖的结论摘要，说明哪些少数类别/组合最值得优先复核。请输出一份可执行的分析结论结构，适合安全运营/威胁狩猎场景。
```

### 623. D9_k982591_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全分析的分群对比报告，重点围绕“不同类别分组之间的行为差异”来找出最值得关注的异常模式。数据里已经有 protocol_type、service、flag、logged_in、is_guest_login、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、dst_host_* 这些字段，请不要建模，只做可解释的统计分析。我要你把分析拆成几个互不依赖的部分：先看 class=anomaly / normal 的总体占比，再按 protocol_type、service、flag 做分组对比，找出各组在连接行为和错误率上的最大差距；然后再看 logged_in、is_guest_login、land 等关键二元字段与 class 的关系；最后补充几个高风险特征（例如 src_bytes、dst_bytes、count、srv_count、serror_rate、same_srv_rate）在不同 class 或不同 categorical segment 中的均值/中位数差异，并指出差距最大的 segment。输出请尽量给出可直接用于汇报的结论性要点和少量表格，不要做可视化。
```

### 624. D9_k982636_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, I need a security-analytics readout focused mainly on correlation and driver analysis. Please break it into independent workstreams so different people can tackle them in parallel: identify which numeric features move together, which variables have the strongest rounded correlations with attack indicators, and what the most important co-varying patterns are by protocol/service/flag. Use the real columns in the file, including duration, src_bytes, dst_bytes, logged_in, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, and the destination-host rate fields. I want a concise analyst summary plus a machine-readable JSON output capturing the key correlations, top associations, and any notable differences between normal and anomaly traffic.
```

### 625. D9_k982639_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全运营的复杂分析，重点围绕“时间/序列趋势”来判断异常流量是否存在阶段性上升、突发聚集或周期性变化。虽然这份数据里没有真实日期字段，但请把行顺序当作采样顺序，按每 100 条记录作为一个时间窗口，分析从前到后各窗口里攻击/正常流量的变化、协议与服务分布的漂移、以及与攻击强相关特征（如 src_bytes、dst_bytes、count、srv_count、serror_rate、same_srv_rate、diff_srv_rate、dst_host_*）的趋势变化。请输出可供安全分析师直接汇报的结论，并在结论里尽量指出哪些窗口最异常、哪些特征在异常窗口里变化最大、以及这些变化是否能用于分层告警。请拆成 4-6 个互相独立的分析轨道，便于并行推进；每条轨道都要围绕趋势/环比/窗口变化展开，但也可以补充结构漂移、类别构成变化和关键特征对比。
```

### 626. D9_k982702_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, I need a security analytics review focused mainly on temporal/trend behavior over the sequence fields in the dataset. Treat the rows as an ordered observation stream and look for period-over-period changes in intrusion behavior. Please break this into independent workstreams: (1) anomaly rate trend across equal-sized row windows, (2) trend shifts in core traffic intensity features like duration, src_bytes, dst_bytes, count, and srv_count, (3) trend changes in protocol/service/flag mix over the sequence, (4) period-over-period movement in connection-error rates and host-based rates, (5) identify where the anomaly rate spikes relative to adjacent windows and what feature values characterize those windows, and (6) summarize the most stable vs most volatile signals over the sequence. I want a concise analysis summary plus a small JSON-ready output of the key findings.
```

### 627. D9_k982745_en (domain=D9, difficulty=6)

```
Using subhajournal__iotintrusion__IoT_Intrusion.csv, analyze the security traffic patterns with a main focus on segment comparison across categorical groups: compare rates, means, and the biggest gaps between segments. I need a practical analyst-style readout of how the attack labels differ across protocol/service flags and other categorical splits, and which groups stand out most. Please use the real columns in the file, especially label, Protocol Type, HTTP, HTTPS, DNS, Telnet, SMTP, SSH, IRC, TCP, UDP, DHCP, ARP, and the flag/count fields, and summarize the most important segment differences for security triage.
```

### 628. D9_k982797_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, do a security-analytics review centered on correlation and driver analysis: identify which numeric fields move together, quantify the strongest rounded correlations, and explain which features appear to be the main drivers of suspicious connection patterns. Please split the work into independent tracks so different analysts can work in parallel: one on overall numeric correlation structure, one on high-traffic/volume behavior, one on error-rate and failure-pattern relationships, one on host-based context variables, and one on protocol/service/flag context to see whether the strongest numeric relationships differ by connection type. Please keep the output focused on actionable findings, not generic EDA.
```

### 629. D9_k982806_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的分布与阈值分层分析，重点看“低/中/高”风险流量在各特征上的分布、占比和异常混合情况。这个数据里已经有 duration、protocol_type、service、flag、src_bytes、dst_bytes、land、wrong_fragment、urgent、hot、num_failed_logins、logged_in、num_compromised、root_shell、su_attempted、num_root、num_file_creations、num_shells、num_access_files、num_outbound_cmds、is_host_login、is_guest_login、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate 等字段。请你不要做建模，只做可落地的统计分析：先按业务阈值和分位数把样本分层，再看每层的规模、占比、典型值、极端值和协议/服务/flag 组合的构成。最后给我一个可以直接交给安全运营团队的结论摘要，指出哪些阈值段最值得优先排查、哪些协议/服务在高阈值段中最集中、以及哪些“正常感”较强的字段组合可能隐藏异常。
```

### 630. D9_k982877_en (domain=D9, difficulty=6)

```
Using subhajournal__iotintrusion__IoT_Intrusion.csv, analyze the intrusion patterns with a focus on temporal / trend behavior over the sequence of flows in the file. I need a practical security-analytics readout that compares how attack mix, traffic intensity, and flag/protocol behavior change across the dataset order, and that helps spot whether certain labels or indicators ramp up, spike, or decay over time. Please break it into independent workstreams so a team can split it up: one track on label mix and transitions across the ordered flows, one on rolling/period-over-period changes in flow_duration, Rate, Srate, and Drate, one on protocol/flag signature trends, one on differences between the earliest and latest portions of the file, and one on correlation between the temporal order and key numeric indicators. Use the real columns in the file, including label, flow_duration, Duration, Rate, Srate, Drate, fin_flag_number, syn_flag_number, rst_flag_number, psh_flag_number, ack_flag_number, TCP, UDP, HTTP, HTTPS, DNS, and the other listed fields as needed.
```

### 631. D9_k982944_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的关联性与驱动因素分析，重点围绕数值字段之间的联动关系、相关系数（按四舍五入保留 2 位小数）、以及最强的正/负相关对。请结合真实字段名（如 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_same_src_port_rate、dst_host_srv_diff_host_rate、dst_host_serror_rate、dst_host_srv_serror_rate、dst_host_rerror_rate、dst_host_srv_rerror_rate，以及 protocol_type/service/flag）做分析，判断哪些数值指标最可能共同变化、哪些指标呈现明显对立关系，并把结果整理成适合给安全团队复盘的结论。请分成 4-6 个彼此独立的分析轨道并产出一个简洁的 analysis_summary.json。
```

### 632. D9_k982951_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, do a security-analytics correlation and driver analysis focused on which numeric signals move together and which ones are the strongest associations. Please break it into independent workstreams so a small team can run them in parallel: (1) overall correlation structure across the numeric telemetry, (2) strongest positive and negative pairwise relationships among the core rate/count features, (3) how those relationships differ by class (normal vs anomaly), (4) which protocol/service/flag categories are most associated with high-risk numeric patterns, (5) whether connection volume features (count, srv_count, and host-based counts/rates) cluster together, and (6) a concise driver summary that calls out the most informative numeric fields and any near-duplicate features to watch for. Keep it grounded in the actual values in the file and report rounded correlations and top associations only.
```

### 633. D9_k982975_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, please do a security analytics review focused mainly on temporal / trend behavior over the sequence-like fields in this dataset. I need a concise but rigorous report that compares how traffic evolves across low-to-high count bands and other rate-based indicators, and that explains how anomaly patterns change as connection frequency rises. Use the real columns in the file, especially count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, dst_host_count, dst_host_srv_count, dst_host_same_srv_rate, dst_host_diff_srv_rate, dst_host_same_src_port_rate, dst_host_srv_diff_host_rate, dst_host_serror_rate, dst_host_srv_serror_rate, dst_host_rerror_rate, dst_host_srv_rerror_rate, plus class, protocol_type, service, and flag. I want the analysis organized into 4-6 independent tracks so different analysts can work in parallel: one track on period-over-period changes across count bands, one on anomaly share shifts over those bands, one on protocol/service mix drift, one on flag transitions, one on host-level rate changes, and one on how extreme byte/connection behaviors differ between normal and anomaly. Please summarize the main findings and produce a compact analysis_summary.json.
```

### 634. D9_k983002_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全运营的分布与阈值分层分析，重点围绕“超过/低于业务阈值的会话占比、分位数分桶、各桶的告警/正常混合情况”展开。请直接读取数据并结合真实字段来分析，不要假设字段含义。希望你把结果整理成 analysis_summary.json，重点回答：1）哪些流量/连接特征在高阈值区间最集中；2）不同阈值下 anomaly 与 normal 的占比如何变化；3）关键计数类特征的分桶分布；4）服务、协议、flag 在高风险阈值组中的混合差异；5）若把多项特征同时落入高阈值定义，样本会如何聚集。请使用真实列名：duration、protocol_type、service、flag、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_same_src_port_rate、dst_host_srv_diff_host_rate、dst_host_serror_rate、dst_host_srv_serror_rate、dst_host_rerror_rate、dst_host_srv_rerror_rate、class 等。
```

### 635. D9_k983065_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, run a security analytics review focused on distribution and threshold cohorts. I want a compact but thorough readout of how traffic splits across business-style cutoffs and quantile buckets, and which protocol/service/flag mixes dominate those cohorts. Please base it on the real columns in the file, especially duration, src_bytes, dst_bytes, count, srv_count, logged_in, protocol_type, service, flag, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, and class. Decompose the work into independent tracks so different analysts can work in parallel: 1) overall distribution profiling and missingness sanity checks, 2) threshold cohort sizing for high-volume / low-volume traffic and extreme byte transfer sessions, 3) quantile-bucket mix analysis for duration, src_bytes, dst_bytes, count, and srv_count, 4) cohort comparisons for attack vs normal across those buckets, 5) protocol/service/flag composition within the largest and most extreme cohorts, and 6) a short anomaly-focused summary of rate features and logged_in behavior across cohorts. Deliver the findings as a concise analysis summary.
```

### 636. D9_k983098_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, do a security-analytics correlation and driver analysis on the numeric features. I need you to identify which metrics move together, which variables are the strongest association drivers for attack-vs-normal traffic, and whether the high-signal protocol/service/flag combinations line up with the numeric patterns. Please split the work into independent tracks so separate analysts can work in parallel: (1) overall numeric correlation structure and top absolute correlations, (2) class-separated driver comparison for key numeric fields, (3) strong co-movement among the host/network rate features, (4) relationship between connection volume counters and service outcome flags, (5) categorical slices that explain the numeric drivers (protocol_type/service/flag), and (6) a concise risk summary that highlights the most associated metrics and any notable outliers.
```

### 637. D9_k983105_zh (domain=D9, difficulty=6)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的相关性与驱动因素分析，重点找出哪些数值字段彼此最同步、哪些字段最能区分不同攻击标签、以及哪些协议/标志位/流量统计指标构成了最强的关联链。请直接使用数据中的真实列名（例如 flow_duration、Header_Length、Protocol Type、Duration、Rate、Srate、Drate、ack_count、syn_count、HTTP、HTTPS、TCP、UDP、ICMP、Tot sum、Min、Max、AVG、Std、Tot size、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight、label 等），围绕“相关性 & 驱动因素”输出可落地结论。我要你把分析拆成 4-6 个相互独立的 track：1) 全局数值相关性结构与最强正/负相关对；2) 标志位/计数类字段之间的联动关系；3) 协议与服务指示位（HTTP/HTTPS/DNS/TCP/UDP/DHCP/ARP/ICMP/IPv/LLC）与流量统计指标的关联；4) 按 label 分组后哪些数值字段的均值/中位数差异最大；5) 找出在不同攻击标签中最具判别力的变量组合或模式；6) 若存在缺失/异常值，请先做最基础的完整性检查并说明是否会影响相关性判断。请将结果整理成可执行的结论摘要，并附上适合安全运营复盘的要点。输出文件只需要 analysis_summary.json。
```

### 638. D9_k983189_en (domain=D9, difficulty=6)

```
Using inputs/subhajournal__iotintrusion__IoT_Intrusion.csv, run a security-analytics review focused on correlation and driver analysis. I want you to identify which numeric fields move together, which features have the strongest rounded pairwise correlations, and how those associations differ across attack labels. Please break the work into independent tracks so separate sub-agents can handle them: one track for data quality and missingness, one for global correlation structure across all numeric columns, one for top positive/negative associations among traffic/flag/statistical fields, one for label-wise correlation differences for the main attack classes, and one for a compact driver summary of the most connected fields. Use the real columns in the file, including flow_duration, Header_Length, Protocol Type, Duration, Rate, Srate, Drate, the TCP/UDP/DNS/HTTP-style protocol flags, the packet/flag counts, the statistical columns like Tot sum/Min/Max/AVG/Std/Tot size/IAT/Number/Magnitue/Radius/Covariance/Variance/Weight, and label. Keep the output concise and deterministic.
```

### 639. D9_k983274_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的多维排查报告，重点围绕“排名与集中度”来展开：先识别哪些协议、服务、标志位（protocol_type / service / flag）在样本中最集中，再看这些高频组是否也对应更高的异常指标或连接特征（例如 src_bytes、dst_bytes、count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate）。请把分析拆成几个彼此独立的轨道，分别输出：1）Top-N 高频组及其总占比、2）长尾与帕累托集中度（比如前若干组覆盖多少样本）、3）按服务/协议/flag 的异常特征对比，4）在不同高频组内的关键数值特征排名，5）可疑组合的交叉排名（例如高频且异常率高的组）。最终请输出一个可直接交付给安全团队的结构化摘要，说明哪些组值得优先排查、它们在整体流量中的集中程度，以及是否存在少数组占据大部分样本的现象。
```

### 640. D9_k983291_en (domain=D9, difficulty=6)

```
Analyze `inputs/subhajournal__iotintrusion__IoT_Intrusion.csv` as a security analytics dataset, with the main goal of comparing attack segments across categorical groups and identifying the biggest gaps between them. I need a compact but rigorous review of how traffic patterns differ by label and protocol/service categories, using the real columns in the file (for example `label`, `Protocol Type`, `HTTP`, `HTTPS`, `DNS`, `TCP`, `UDP`, `ARP`, `ICMP`, `Tot size`, `Rate`, `Srate`, `Drate`, `Duration`, `flow_duration`, flag counts, and the derived size/stat columns). Please break it into independent tracks so the work can be split across a small sub-agent team: (1) label-level segment comparison for rates and traffic size metrics, (2) protocol-type and transport/service-category comparisons, (3) binary service-feature prevalence by label, (4) largest between-segment gaps in selected metrics, (5) within-label variability / consistency checks on key metrics, and (6) a short security interpretation of which categories look most distinct and why. I want a final `analysis_summary.json` style deliverable with the key segment gaps, the most discriminative groups, and a few concrete numbers.
```

### 641. D9_k983372_zh (domain=D9, difficulty=6)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的入侵流量审计，重点围绕“排名与集中度”展开：先找出各攻击标签（label）的频次排名、Top-N 的累计占比、以及是否存在明显的长尾/Pareto 集中；再比较不同标签在关键流量指标上的集中度与差异，比如 flow_duration、Rate、Srate、Drate、Duration，以及 TCP/UDP/HTTP/HTTPS 等协议/服务标志的占比。请把分析拆成 4-6 个彼此独立的方向，便于并行执行，并输出一个简洁的 analysis_summary.json，里面要能回答：哪几类攻击最常见、头部类别合计占了多少、哪些标签在速率或持续时间上最集中、以及协议使用是否呈现头部集中。请注意只能使用这个固定数据集中的真实值，不要补充或推测任何不存在的数据。
```

### 642. D9_k983417_en (domain=D9, difficulty=6)

```
Using `subhajournal__iotintrusion__IoT_Intrusion.csv`, do a security analytics review focused mainly on segment comparison across categorical groups. I need you to compare rates, means, and distributions across protocol / service-like segments and identify the biggest gaps between segments, with enough detail to support a short executive summary and a few concrete findings. Please use the real columns in the file, especially the categorical indicators and the label, and base the analysis on the actual data only. Decompose the work into independent tracks so different sub-agents can work in parallel, and return one concise JSON summary file for me.
```

### 643. D9_k983449_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, I need a security-analytics briefing focused mainly on ranking and concentration: identify the biggest traffic drivers, how much of total volume is concentrated in the top categories/flows, and whether attacks are similarly concentrated or more diffuse. Please work directly from the real columns in the file — especially protocol_type, service, flag, src_bytes, dst_bytes, count, srv_count, same_srv_rate, diff_srv_rate, and class — and structure the work so multiple analysts can work independently. I want the final output as analysis_summary.json with clear, decision-ready takeaways about top-N shares, Pareto concentration, and the most dominant attack vs normal segments.
```

### 644. D9_k983469_en (domain=D9, difficulty=6)

```
Analyze `inputs/sampadab17__network-intrusion-detection__Test_data.csv` for security analytics, focusing mainly on correlation and driver analysis across the numeric traffic/session features. I need you to identify which numeric fields move together most strongly, which variables look like the main drivers of the connection behavior, and whether the strongest relationships are positive or negative after rounding correlations to 2 decimals. Please also sanity-check the categorical split for `protocol_type`, `service`, and `flag`, and summarize whether the strongest numeric associations are concentrated around the host-based rate fields or the basic byte/count fields. Keep this practical for an incident-response review: I want a concise but defensible analysis that highlights the top associations, the highest-magnitude correlated pairs, and a few targeted breakdowns by protocol/flag so I can see whether certain connection states behave differently.
```

### 645. D9_k983480_zh (domain=D9, difficulty=6)

```
请基于数据文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份安全分析简报，重点围绕“按类别分组后的指标差异”展开。请结合真实字段（例如 label、Protocol Type、Rate、Srate、Drate、Duration、flow_duration、Header_Length、ack_count、syn_count、HTTP、HTTPS、DNS、TCP、UDP、ICMP 等）做一个多部分分析，目的是找出不同攻击/正常流量之间最显著的区分点，以及这些差异是否能用于快速识别可疑流量。请输出可供汇报的结论，不要只给描述，要尽量用定量结果支撑。

我希望你把工作拆成几条彼此独立的分析线：先做 label 级别的总体对比，再看协议类型与流量速率/持续时间的分布差异，然后从 TCP/UDP/ICMP 这类网络标志位和计数字段中找出各标签的模式，接着找出各类别在关键指标上的最大差距，并补充异常高值或极低值在不同标签中的集中情况。最后，请给出一个简洁的结构化总结，方便我直接放进分析文档。
```

### 646. D9_k983490_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的多维数据诊断，重点放在“数值特征之间的相关性与驱动因素”上：先找出哪些数值字段彼此最强相关、哪些指标组合最能区分异常/攻击迹象，再结合协议类型、服务类型和标志位做交叉验证。请把结果整理成可直接汇报的分析结论，并尽量用 2 位小数的相关系数来表达。需要覆盖的字段至少包括 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate，以及与会话行为相关的 logged_in、is_guest_login、land、wrong_fragment、hot、num_failed_logins 等。请按下面 4-6 个相互独立的分析方向分工推进：一条专门做相关矩阵与 top associations；一条做高相关对的安全含义解读；一条做协议/服务/flag 与关键数值特征的交叉比较；一条做异常会话特征画像；如有必要再补一条做整体分布与极端值检查。最后输出一个简洁的分析摘要，告诉我哪些特征最值得作为后续建模或规则告警的核心驱动因子。
```

### 647. D9_k983540_zh (domain=D9, difficulty=6)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的多维数据分析，重点围绕“排名与集中度”展开：先找出流量/攻击类型里最占比的头部项，再量化头部集中度（Top-N 占比、累计占比、Pareto 结构），并结合协议、TCP/UDP 相关特征、标志位计数、以及若干连续特征，解释这些头部攻击为什么会形成高集中。请同时检查数据完整性和标签分布，确认是否存在明显失衡，并把结论整理成可给管理层看的简短摘要。涉及的列包括 label、Protocol Type、Rate、Srate、Drate、TCP、UDP、HTTP、HTTPS、DNS、Telnet、SSH、ack_count、syn_count、fin_count、rst_count、flow_duration、Header_Length、Duration、Tot size、Weight 等。请输出 analysis_summary.json。请把分析拆成 4-6 个彼此独立的轨道，例如：1）标签频次与集中度，2）协议/服务特征的头部集中，3）TCP/UDP 与标志位模式，4）连续数值特征在头部标签中的差异，5）缺失值与基本数据质量检查。
```

### 648. D9_k983597_en (domain=D9, difficulty=6)

```
Using subhajournal__iotintrusion__IoT_Intrusion.csv, do a security-analytics review focused mainly on distribution and threshold cohorts. I need to know how the traffic splits across business thresholds and quantile buckets, and how the attack mix changes within those cohorts. Please use the real columns in the file, especially flow_duration, Header_Length, Duration, Rate, Srate, Drate, ack_count, syn_count, fin_count, urg_count, rst_count, TCP, UDP, HTTP, HTTPS, DNS, Telnet, SMTP, SSH, IRC, DHCP, ARP, ICMP, IPv, LLC, and label. I want a concise analyst-ready output with the key cohort counts, mix shares, and a few threshold-based comparisons that would help me set detection rules.
```

### 649. D9_k983625_en (domain=D9, difficulty=6)

```
Analyze the file sampadab17__network-intrusion-detection__Test_data.csv as a security analytics review focused mainly on distribution and threshold cohorts. I need a concise but rigorous breakdown of how traffic is distributed across key features and what share of records fall into business-relevant buckets. Please split the work into 4–6 independent tracks so different analysts could run them in parallel: 1) volume and protocol/service mix, 2) threshold cohorts for bytes, duration, and connection counts, 3) error-rate and success-rate bucket distributions, 4) rare-activity indicators and host-login/guest-login behavior, 5) cross-tabbed mix shares for the most important categorical fields, and 6) simple anomaly screening using the extreme tails of counts and rates. Use the real columns in the dataset, including duration, protocol_type, service, flag, src_bytes, dst_bytes, logged_in, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, and the dst_host_* features. The output should be suitable for a security analyst who wants a threshold-cohort summary, not a model.
```

### 650. D9_k983668_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全运营的多阶段分析，重点围绕“时间/序列趋势”来判断入侵行为是否在某些序列位置上呈现出阶段性变化。这个数据没有显式日期字段，所以请把记录顺序当作时间顺序，按原始行号把全量样本切成前 50%、后 50%，并进一步按 5 个等长窗口做 period-over-period 对比。请重点分析 class（normal/anomaly）在不同序列阶段的占比变化、关键流量与连接强度指标的趋势变化，以及这些变化是否与协议/服务/flag 组合的分布迁移相一致。需要同时考虑 protocol_type、service、flag、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、dst_host_* 相关字段。请产出适合忙碌安全分析师阅读的结论：说明是否存在明显的前后半段差异、哪个窗口异常最集中、哪些服务或标志位在后半段更偏向异常、以及这些序列变化是否支持‘攻击活动在数据后段升高’的判断。请将结果拆成可并行的 4-6 个独立分析轨道：整体趋势、标签趋势、协议/服务结构迁移、关键数值指标趋势、异常峰值窗口定位、以及交叉验证异常模式是否一致。
```

### 651. D9_k983669_en (domain=D9, difficulty=6)

```
Use the file subhajournal__iotintrusion__IoT_Intrusion.csv and analyze this IoT intrusion dataset for security analytics, focusing mainly on segment comparison across categorical groups. I need a practical readout of how attack behavior differs across labels and protocol/service indicators, especially rates and means per group, plus the biggest gaps between segments. Please break it into independent workstreams so multiple people could work in parallel: compare label-level distributions and feature means, compare protocol/service segments (HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC/TCP/UDP/DHCP/ARP) against key traffic metrics, identify the largest mean gaps between benign and attack-like classes, examine which categorical indicators are most associated with high-rate/high-duration flows, summarize flag/count differences by label, and produce a compact set of actionable findings for detection prioritization.
```

### 652. D9_k983679_en (domain=D9, difficulty=6)

```
Analyze `inputs/sampadab17__network-intrusion-detection__Test_data.csv` for security-analytics correlation and driver analysis. Use the real columns in the file, especially the numeric behavior fields (`duration`, `src_bytes`, `dst_bytes`, `count`, `srv_count`, `serror_rate`, `srv_serror_rate`, `rerror_rate`, `srv_rerror_rate`, `same_srv_rate`, `diff_srv_rate`, `srv_diff_host_rate`, `dst_host_*` rates/counts, plus the other numeric session flags). I need a compact but rigorous readout of which numeric fields move together, which pairs are strongest after rounding, how the host/session rate families cluster, and where the main operational drivers seem to be. Please split this into independent workstreams so multiple sub-agents can work in parallel: one on global numeric correlations/top pairs, one on host-based rate/count families, one on service/session activity drivers, one on binary/rare-event indicators, and one on category-conditioned patterns for `protocol_type`, `service`, and `flag`. I want a concise JSON-style deliverable I can hand to the security team, focused mainly on correlation & driver analysis.
```

### 653. D9_k983768_zh (domain=D9, difficulty=6)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的异常/离群检测分析，不要训练模型，重点围绕“显式数值规则”来找异常流量：例如基于 IQR 的极端值、固定阈值的高 Rate/Srate/Drate、罕见协议/业务类别、以及标志位组合异常。请把结果拆成多个彼此独立的分析轨道，方便分工并行：1）对 flow_duration、Header_Length、Duration、Rate、Srate、Drate、ack_count、syn_count、fin_count、urg_count、rst_count、Tot sum、Min、Max、AVG、Std、Tot size、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight 等数值列做 IQR/极端值离群统计，并指出最严重的列；2）基于 Protocol Type、label 以及 HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC/TCP/UDP/DHCP/ARP/ICMP/IPv/LLC 等类别/协议列，找出稀有值和最不常见攻击标签；3）检查明显可疑的流量规则组合，例如高 Srate 但低 Duration、同时存在多个旗标置位、ACK/SYN/FIN/RST 计数异常不一致等；4）按 label 汇总异常样本占比，比较不同攻击类型的异常程度；5）输出能直接用于告警规则设计的统计阈值建议（例如 95%/99% 分位数、IQR 上界、最常见稀有类别）。请最终给我一个可落地的分析摘要，说明哪些规则最值得优先做成检测条件。文件中真实列名包括：flow_duration、Header_Length、Protocol Type、Duration、Rate、Srate、Drate、fin_flag_number、syn_flag_number、rst_flag_number、psh_flag_number、ack_flag_number、ece_flag_number、cwr_flag_number、ack_count、syn_count、fin_count、urg_count、rst_count、HTTP、HTTPS、DNS、Telnet、SMTP、SSH、IRC、TCP、UDP、DHCP、ARP、ICMP、IPv、LLC、Tot sum、Min、Max、AVG、Std、Tot size、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight、label。请输出 analysis_summary.json 结构化结论。
```

### 654. D9_k983829_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, run a security analytics review focused mainly on temporal / sequence trend behavior in the test set. Treat the row order as the observation sequence and quantify whether attack-like indicators and traffic patterns are drifting over time: look at period-over-period changes in connection behavior, protocol/service mix, flag transitions, and how rate-based features evolve across the sequence. Tie the findings back to the actual columns in the file, especially duration, protocol_type, service, flag, src_bytes, dst_bytes, logged_in, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, and the dst_host_* rate/count columns. I need a concise analyst-ready summary plus a small set of supporting checks that can be reproduced directly from the CSV.
```

### 655. D9_k983833_en (domain=D9, difficulty=6)

```
Using inputs/sampadab17__network-intrusion-detection__Train_data.csv, run a security-analytics review focused mainly on correlation and driver analysis: identify which numeric fields move together, round correlations to 2 decimals, and call out the strongest associations that differ between normal and anomaly traffic. Please keep it practical for an intrusion-detection analyst: compare patterns across class, service, and protocol_type; check whether high-connection-count records behave differently; and summarize the numeric drivers most aligned with suspicious behavior. I need this split into several independent workstreams so different analysts could work in parallel, and I only want a concise JSON summary in the end.
```

### 656. D9_k983925_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一次面向安全分析的多部分审查，重点围绕“排名与集中度”展开：先找出最常见的协议、服务、flag 以及它们对总流量的集中程度，再识别哪些连接特征最能区分高频可疑流量与低频流量，最后从统计上判断是否存在少数服务/标志/协议主导了大部分连接。请结合真实列名（如 protocol_type、service、flag、src_bytes、dst_bytes、count、srv_count、serror_rate、same_srv_rate、diff_srv_rate、dst_host_count、dst_host_srv_count 等）输出一个可给管理层看的分析摘要，并把结论拆成可并行执行的多个分析轨道。
```

### 657. D9_k983937_en (domain=D9, difficulty=6)

```
Analyze the file sampadab17__network-intrusion-detection__Test_data.csv for a security-analytics data-quality audit first, then summarize any meaningful operational patterns you can infer from the cleaned data. I need this broken into independent workstreams so different people can work in parallel: 1) completeness and null-like token audit across all columns, especially any blank strings or literal '?' values in categorical fields; 2) duplicate and near-duplicate record audit, including exact duplicate rows and duplicate network sessions by the key traffic fields; 3) domain-range validation for numeric features such as duration, src_bytes, dst_bytes, count, srv_count, and all rate features that should stay in [0,1]; 4) categorical consistency audit for protocol_type, service, and flag, including uncommon or suspicious categories and whether any values appear malformed or inconsistent; 5) cross-field logic checks for impossible or suspicious combinations, such as logged_in vs. byte patterns, land=1 prevalence, or zero-activity rows; 6) a concise security-ops summary of the most frequent service/flag combinations and whether the dataset looks clean enough for downstream intrusion-detection analysis.
```

### 658. D9_k983961_en (domain=D9, difficulty=6)

```
Analyze sampadab17__network-intrusion-detection__Test_data.csv as a security analytics review focused mainly on distribution and threshold cohorts. I need a compact but rigorous readout on how traffic breaks across business thresholds and quantile buckets, especially for src_bytes, dst_bytes, count, srv_count, and the rate features. Please treat this as an operational triage question: identify low/high cohorts, mix shares, and how categorical protocol/service/flag composition shifts across those cohorts. Break the work into independent tracks so separate analysts could run them in parallel: 1) overall threshold cohort sizing for key numeric fields, 2) quantile-bucket mix and central tendency by bucket, 3) protocol/service/flag composition in the extreme cohorts, 4) rate-feature behavior across the same thresholds, 5) outlier and edge-case checks for zero/near-zero traffic and host-activity patterns. Return a concise analysis summary suitable for an incident-response stakeholder.
```

### 659. D9_k983982_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全运营的分布与阈值分层分析，重点围绕业务阈值、分位桶和占比结构来判断这批网络连接样本的风险画像。请直接使用现有字段（如 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、protocol_type、service、flag 等），不要改动任何原始值。我要的是能支持告警阈值、流量分层和重点协议/服务识别的结论，而不是建模。请把分析拆成多个可并行的小任务，最后汇总成一份 analysis_summary.json。
```

### 660. D9_k983992_en (domain=D9, difficulty=6)

```
Analyze inputs/sampadab17__network-intrusion-detection__Train_data.csv for security analytics with a focus on anomaly and outlier detection using explicit numeric rules, not machine learning. I need a practical assessment of where the dataset contains extreme or suspicious records based on hard thresholds, IQR-based outliers, rare categorical values, and unusual combinations of flags and traffic-volume features. Please break it into independent tracks so different people can work in parallel: (1) quantify how many rows are anomalous by the dataset’s class label and by simple numeric outlier rules on src_bytes, dst_bytes, count, srv_count, and the rate features; (2) identify rare protocol_type/service/flag categories and how they overlap with anomaly labels; (3) characterize extreme host-activity patterns using count/srv_count and the dst_host_* rate columns; (4) inspect records with privileged or shell-related indicators (logged_in, root_shell, su_attempted, num_compromised, num_root) and whether they coincide with outlier traffic; (5) summarize high-severity records that trip multiple numeric thresholds at once; and (6) produce a concise analyst-ready summary of the strongest anomaly signals and the most suspicious category combinations. Use only deterministic pandas/numpy analysis on the fixed file and report results as small JSON-ready aggregates.
```

### 661. D9_k984017_en (domain=D9, difficulty=6)

```
Analyze subhajournal__iotintrusion__IoT_Intrusion.csv for a security-analytics threshold/cohort review focused on how traffic is distributed across operational cutoffs and quantile buckets, and what that means for attack mix. I want a compact analysis that uses the real columns in the file, especially flow_duration, Duration, Rate, Srate, Drate, ack_count, syn_count, fin_count, rst_count, and the label. Please break it into independent workstreams so different agents could work in parallel: 1) global distribution and business-threshold cohorting for flow_duration, Duration, Rate, Srate, and Drate; 2) quantile-bucket mix shares by label and attack family; 3) above/below-threshold comparisons for TCP/UDP/HTTP/HTTPS/DNS activity and protocol-related flags; 4) label concentration and dominant class share within each threshold cohort; 5) a short outlier/high-risk cohort scan using the top tail of Rate and Srate; 6) a concise summary of the most operationally relevant cohort boundaries and how many rows fall into each. Return the results as a clean JSON summary with counts, percentages, and the exact thresholds used.
```

### 662. D9_k984057_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, run a security-analytics correlation and driver analysis on the numeric fields and the key categorical context columns. I need a concise but rigorous readout of which signals move together, especially rounded pairwise correlations among the numeric features, the strongest positive/negative associations, and how the main traffic flags differ by protocol/service/flag groups where it helps explain those correlations. Please structure it as a multi-part analysis with independent workstreams so different sub-analysts can work in parallel: one on the global correlation map, one on high-association feature pairs and redundancy, one on protocol/service/flag conditioning, one on anomaly-like subsets defined by unusual counts/bytes/rates, and one on a short executive summary of the main drivers and likely collinear blocks. Keep the output focused on practical security findings from this test set of 1500 rows.
```

### 663. D9_k984099_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, do a security-analytics correlation and driver analysis on the numeric features. I need a concise but rigorous readout of which fields move together, which network-burst and host-behavior measures are most associated with intrusion-like patterns, and where the strongest positive and negative relationships are. Please keep the work grounded in the real columns in the file, especially the traffic volume fields, flag/rate fields, and host-level rate fields. Break it into independent workstreams so different people could handle them in parallel: (1) global numeric correlation scan and top associations, (2) duration/bytes/connection-count driver patterns, (3) rate-feature clustering around serror/rerror and same/diff-srv behavior, (4) host-level rate relationships, and (5) categorical context by protocol/service/flag for the strongest numeric drivers.
```

### 664. D9_k984110_en (domain=D9, difficulty=6)

```
Using subhajournal__iotintrusion__IoT_Intrusion.csv, build a security-analytics memo centered on segment comparison across categorical groups. I need you to compare attack labels and protocol indicators to find the biggest gaps between segments, then explain what those gaps mean operationally. Please split the work into 5 independent tracks: (1) label-level comparisons of traffic volume and timing metrics, (2) protocol-flag segment differences for HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC/TCP/UDP/DHCP/ARP, (3) TCP vs UDP vs ICMP-style behavior using the protocol columns and packet/flag counters, (4) feature-gap analysis for the largest mean differences between attack labels on key numeric fields such as Rate, Srate, Drate, Duration, Header_Length, flow_duration, ack_count, syn_count, rst_count, and (5) a concise risk interpretation highlighting which label or protocol segments are most anomalous and which features most separate them. Use the real column names exactly as they appear in the file and keep the output grounded in the actual data.
```

### 665. D9_k984116_en (domain=D9, difficulty=6)

```
Analyze subhajournal__iotintrusion__IoT_Intrusion.csv for security-analytics patterns with a strong temporal/trend focus. I need a compact executive readout on how traffic changes across the sequence of observations, especially whether the core flow metrics and protocol/flag indicators show step changes, drift, or bursty behavior between early, middle, and late portions of the file. Please use the real columns in the dataset, including flow_duration, Header_Length, Protocol Type, Duration, Rate, Srate, Drate, the TCP/UDP/HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC/DHCP/ARP/ICMP/IPv/LLC indicators, the TCP flag/count fields, and the label. I want this framed for security operations: identify dominant attack labels over the sequence, compare early-vs-late behavior, and call out which metrics are most unstable over time. Please produce analysis suitable for a short JSON summary and split the work into independent tracks so different agents could handle them.
```

### 666. D9_k984142_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全分析的深度排查报告，重点围绕“排名与集中度”展开：先找出最主要的入侵/正常类别、最集中的协议/服务/标志组合、以及流量/连接特征在异常与正常之间的头部贡献差异；再评估是否存在典型的 Pareto 结构（少数类别或少数服务是否贡献了大部分样本），并把结果拆成可并行推进的 4-6 个独立分析轨道。请直接使用数据中的真实字段，例如 class、protocol_type、service、flag、src_bytes、dst_bytes、count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate、dst_host_* 等，输出一份可供安全运营复盘的摘要分析。
```

### 667. D9_k984188_zh (domain=D9, difficulty=6)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的异常与离群点排查，重点围绕“显式数值规则”来找可疑样本：比如按 IQR、分位数、极端值、罕见类别、0 值/高值模式等去识别异常流量，并把结果按攻击标签和协议特征拆开看。请结合真实列名（例如 flow_duration、Header_Length、Protocol Type、Duration、Rate、Srate、Drate、ack_count、syn_count、fin_count、HTTP、HTTPS、DNS、Telnet、SMTP、SSH、IRC、TCP、UDP、DHCP、ARP、ICMP、IPv、LLC、Tot sum、Min、Max、AVG、Std、Tot size、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight、label）做分析，输出一份可执行的安全排查结论摘要。我要你把任务拆成 4-6 个彼此独立的分析轨道，方便不同子代理并行处理：1) 全局数值离群点与极端阈值扫描；2) 按 label 分组的异常模式对比；3) 按协议/标志位/服务列的稀有组合与可疑共现；4) 高速率、长持续时间、零值/突增模式的规则化检测；5) 针对少数类别攻击的异常画像；6) 给出可供后续告警规则落地的阈值建议。请直接围绕异常检测与规则化排查展开，不要做模型训练或预测。
```

### 668. D9_k984246_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, do a security-analytics review focused mainly on correlation and driver analysis across the numeric fields: identify which measures move together, round correlations to 2 decimals, and call out the strongest associations overall and within attack-relevant subsets. Break it into independent workstreams so different analysts can work in parallel: one on global numeric correlation structure, one on protocol/service/flag splits, one on high-risk behavior indicators tied to login/privilege fields, one on connection-volume vs error-rate relationships, and one on host-based concentration patterns. I need a concise analysis summary that explains the main drivers and any notable segment differences without changing any data values.
```

### 669. D9_k984274_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, please do a security-analytics correlation and driver analysis on the numeric fields: identify which measurements move together, round correlations to 2 decimals, and call out the strongest associations that could explain anomaly behavior. Break it into a few independent workstreams so I can delegate: one track for an overall numeric correlation scan, one for class-conditioned comparison of the strongest numeric drivers, one for protocol/service/flag context behind those drivers, one for outlier-heavy volume fields versus rate fields, and one for a concise exec summary of the most actionable relationships.
```

### 670. D9_k984340_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, build a security analytics memo focused mainly on temporal / sequence-style trend analysis even though the file has no explicit timestamps. Treat the rows as an ordered event stream and examine whether attack behavior changes over the course of the dataset, especially around shifts in class mix, protocol/service usage, and traffic intensity. I need this broken into 5 independent tracks so different analysts can work in parallel: (1) row-order trend analysis by quartile/segment, especially anomaly rate and byte-volume changes over the sequence; (2) protocol/service/flag composition drift across the sequence; (3) compare early vs late segments on key numeric indicators such as src_bytes, dst_bytes, count, srv_count, and the rate features; (4) isolate where anomaly concentration spikes and identify the dominant protocol/service/flag patterns inside those spike windows; (5) summarize a compact set of operational indicators that would help a SOC monitor whether traffic is becoming more attack-like over time. Use the real columns in the file and keep all outputs deterministic.
```

### 671. D9_k984344_en (domain=D9, difficulty=6)

```
Analyze subhajournal__iotintrusion__IoT_Intrusion.csv for security analytics with a focus on correlation and driver analysis. I want a practical readout of which numeric fields move together, where the strongest positive and negative relationships are, and which protocol/flag/count features appear to be the main drivers of the traffic patterns and labels. Use the real columns in the file, especially flow_duration, Header_Length, Protocol Type, Duration, Rate, Srate, Drate, the TCP flag/count fields, the protocol indicator columns (HTTP, HTTPS, DNS, Telnet, SMTP, SSH, IRC, TCP, UDP, DHCP, ARP, ICMP, IPv, LLC), and the summary/statistical columns such as Tot sum, Min, Max, AVG, Std, Tot size, IAT, Number, Magnitue, Radius, Covariance, Variance, Weight, plus label. Please break this into independent work streams so it could be split across a small sub-agent team: one stream on global numeric correlations, one on label-vs-feature association patterns, one on protocol/flag co-occurrence and counts, one on the strongest feature pairs and redundancy groups, and one on distributional summaries for the most influential columns. Keep the output grounded in the actual data and report only deterministic findings.
```

### 672. D9_k984345_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的多部分诊断，重点围绕“排名与集中度”展开：先找出哪些协议、服务、标志位、主机计数区间和关键异常指标占据了流量/告警的绝大部分份额，再评估是否存在明显的 Pareto 集中现象。请你把分析拆成 4-6 个彼此独立的轨道并行推进：1）协议/服务/flag 的 top-N 频率排名与占比；2）src_bytes、dst_bytes、count、srv_count 的高值集中度与极端值贡献；3）基于告警/失败特征（如 serror_rate、rerror_rate、logged_in、is_guest_login 等）的集中分布；4）不同 service 与 flag 组合的头部模式及其累计覆盖率；5）按主机连接特征（dst_host_*、same_srv_rate、diff_srv_rate）识别最集中的风险模式；6）把各类头部群体的累计占比与前 10% 样本覆盖率整理成简明结论，判断是否需要重点监控少数高频组合或高风险模式。输出要适合安全运营人员快速阅读，并尽量给出可复核的定量结果。
```

### 673. D9_k984421_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全分析的深度排查，重点围绕“数值字段之间的相关性与驱动因素”展开：先找出哪些连续/计数特征彼此最强相关（使用四舍五入后的相关系数），再识别与 class（anomaly/normal）最相关的数值字段，并比较异常与正常流量在关键数值特征上的差异。请结合我关心的业务背景输出一份可复用的分析结论，能直接告诉我哪些指标是攻击流量的主要驱动信号、哪些指标高度同向变化、以及是否存在明显的冗余特征。数据中可用的关键列包括 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、srv_diff_host_rate、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_same_src_port_rate、dst_host_srv_diff_host_rate、dst_host_serror_rate、dst_host_srv_serror_rate、dst_host_rerror_rate、dst_host_srv_rerror_rate，以及 protocol_type、service、flag、class。请把结论拆成若干独立分析轨道，方便分别交给不同子助手并最终汇总成 analysis_summary.json。
```

### 674. D9_k984430_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, build a security analytics brief focused on distribution and threshold cohorts. I need you to quantify how traffic splits above/below practical business thresholds, bucket the data into quantiles, and summarize class mix shares for the key protocol/service/flag segments. Please base the analysis on the real columns in the file, especially duration, src_bytes, dst_bytes, count, srv_count, serror_rate, rerror_rate, same_srv_rate, diff_srv_rate, protocol_type, service, flag, and class. Break this into independent tracks so different analysts can work in parallel: threshold cohort sizing, quantile-bucket profiling, protocol/service/flag mix shares, anomaly concentration by cohort, and cross-threshold comparisons on selected features. Deliver a concise JSON summary plus any supporting tables needed for a security review.
```

### 675. D9_k984433_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全运营的异常与离群分析，重点围绕“显式数值规则”来找可疑流量：例如对 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate、dst_host_* 等字段用阈值、IQR、极端值和稀有类别规则筛出异常。请把结果拆成 4-6 个彼此独立的分析轨道，便于并行推进：1) 设计并统计高置信异常规则命中情况；2) 用 IQR/分位数找数值离群点并比较 normal vs anomaly 的差异；3) 识别协议/服务/flag 的稀有类别及其异常占比；4) 观察极端连接行为（如高 count、低 same_srv_rate、高 dst_host_rerror_rate 等）与标签的关系；5) 汇总最值得人工复核的规则组合与样本特征。最终输出一个可直接给安全团队评审的结构化摘要，说明哪些规则最有效、误报风险如何、以及哪些字段最适合做后续告警阈值。
```

### 676. D9_k984453_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的分组对比报告，重点围绕“不同类别分段之间的均值/占比差异”来找出最值得关注的异常画像。这个测试集有 1500 行，包含 duration、protocol_type、service、flag、src_bytes、dst_bytes、land、wrong_fragment、urgent、hot、num_failed_logins、logged_in、num_compromised、root_shell、su_attempted、num_root、num_file_creations、num_shells、num_access_files、num_outbound_cmds、is_host_login、is_guest_login、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate，以及若干 dst_host_* 指标。请按以下思路完成：1）先按 protocol_type、service、flag 三个类别字段分别做分组对比，找出各组在 src_bytes、dst_bytes、count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate 上的均值差异最大的类别；2）再结合 logged_in、is_guest_login、land、root_shell、su_attempted 等安全语义字段，比较不同组的风险画像；3）找出最极端的高风险组合（例如某些 service/flag 组合是否对应更高的错误率或更低的 same_srv_rate）；4）补充一版总体摘要，说明哪些类别分段最像正常流量、哪些最像扫描/拒绝服务/探测类流量。请输出一个结构化的分析摘要，突出“分组均值差异最大的地方”和“安全上最可疑的分段”，并给出可直接落地的结论建议。
```

### 677. D9_k984458_en (domain=D9, difficulty=6)

```
Using subhajournal__iotintrusion__IoT_Intrusion.csv, build a security-analytics review focused mainly on distribution and threshold cohorts. I need a concise but rigorous breakdown of how traffic is distributed across label types and key numeric risk signals, with special attention to counts below/above operational thresholds, quartile/quantile buckets, and mix shares. Please use the real columns in the file, especially flow_duration, Header_Length, Protocol Type, Duration, Rate, Srate, Drate, the TCP/UDP/HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC/DHCP/ARP/ICMP indicator columns, and label. I want this organized so different analysts could work independently on separate tracks.
```

### 678. D9_k984460_en (domain=D9, difficulty=6)

```
Using the file sampadab17__network-intrusion-detection__Train_data.csv, do a security-analytics review focused mainly on segment comparison across categorical groups. I need you to compare attack vs normal behavior across protocol_type, service, and flag, quantify the biggest gaps in key activity/risk metrics (like duration, src_bytes, dst_bytes, count, srv_count, serror_rate, rerror_rate, same_srv_rate, diff_srv_rate), and call out the most overrepresented categories in anomalies versus normal traffic. Please structure it as a compact analytical memo with enough detail for me to brief a SOC lead quickly.
```

### 679. D9_k984472_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, run a security analytics review focused mainly on distribution and threshold cohorts. I need a compact but rigorous breakdown of how normal vs anomaly traffic differs across business thresholds and quantile buckets, especially for src_bytes, dst_bytes, count, srv_count, and the key rate features. Please organize the work into independent tracks so different analysts can work in parallel: (1) label mix and overall cohort sizing, (2) threshold-bucket distributions for bytes and connection counts, (3) quantile-based cohort comparisons for high-activity vs low-activity traffic, (4) protocol/service/flag mix within the extreme cohorts, (5) rate-feature contrasts across the cohorts, and (6) a short operational interpretation of which thresholds best separate suspicious traffic from normal traffic. Keep the output suitable for a security analyst briefing and summarize the findings in analysis_summary.json.
```

### 680. D9_k984500_en (domain=D9, difficulty=6)

```
Analyze the real dataset in subhajournal__iotintrusion__IoT_Intrusion.csv for security analytics, focusing mainly on distribution and threshold cohorts. I want a compact but decision-useful report that tells me how the traffic and attack labels split across business-style thresholds and quantile buckets, and how the label mix changes across those cohorts. Use the actual columns in the file, especially flow_duration, Duration, Rate, Srate, Drate, Header_Length, and label. Break the work into independent tracks so they can be handled in parallel: (1) overall distributions and missingness for key numeric fields; (2) threshold cohorts for Rate/Srate/Drate and flow_duration; (3) quantile buckets for Duration and Header_Length; (4) label mix and concentration within each cohort; (5) protocol-flag and transport-protocol mix within the highest-risk cohorts; (6) a short anomaly scan for extreme values and whether they are dominated by specific labels. I need the final output as a concise analysis_summary.json with deterministic counts, percentages, and small cross-tabs only.
```

### 681. D9_k984519_en (domain=D9, difficulty=6)

```
Analyze the file sampadab17__network-intrusion-detection__Test_data.csv for security analytics, focusing mainly on correlation and driver analysis across the numeric features. I need a practical readout of which fields move together, where the strongest positive/negative associations are, and which variables seem to drive suspicious connection patterns. Please split the work into independent tracks so different analysts can work in parallel: one track on overall numeric correlation structure, one on the strongest pairwise associations involving traffic-volume and host-based fields, one on how attack-like indicators relate to error-rate and session-state variables, one on service/protocol segmentation of the key drivers, and one on outlier/edge-condition counts for rare flags and binary indicators. Keep it concise but actionable for a security analyst, and prioritize rounded correlations and top associations over broad narrative.
```

### 682. D9_k984532_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全运营的多部分数据分析，重点先做数据质量审计，再在此基础上补充异常流量画像。请围绕以下列展开：duration、protocol_type、service、flag、src_bytes、dst_bytes、land、wrong_fragment、urgent、hot、num_failed_logins、logged_in、num_compromised、root_shell、su_attempted、num_root、num_file_creations、num_shells、num_access_files、num_outbound_cmds、is_host_login、is_guest_login、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate 以及其他主机级衍生字段和 class。我要你先审计是否存在缺失值、'?'、空字符串、重复记录、数值列范围异常、类别列异常取值，再按 class 和协议/服务/flag 分层看异常样本分布、可疑字段组合、以及与高风险主机指标的关联。最终输出一份适合安全分析团队直接使用的结构化结果文件 analysis_summary.json，并在报告里明确指出哪些问题是数据质量问题，哪些是真实的异常流量特征。
```

### 683. D9_k984543_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份偏安全运营视角的多阶段分析，重点围绕“按连接序列/时间顺序变化的趋势”来找异常模式。请结合现有字段（例如 duration、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_serror_rate、dst_host_srv_serror_rate 等）完成以下内容：1）按记录顺序切分前后阶段，比较关键流量/失败率指标的阶段性变化；2）分析不同 protocol_type、service、flag 在各阶段的占比漂移与异常集中点；3）识别高失败率、低同服务率、以及主机级错误率上升是否同步出现；4）找出最可能的扫描/探测式行为序列特征（比如 count、srv_count 上升时相关比率如何变化）；5）给出可以直接放进汇报的结论，包括最值得关注的异常组合与它们的趋势特征。请输出适合安全分析汇报的结构化结果，并尽量把结论和具体字段变化联系起来。
```

### 684. D9_k984570_en (domain=D9, difficulty=6)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, run a security-analytics review focused mainly on distribution and threshold cohorts: tell me how the traffic breaks across business cutoffs and quantile buckets, and what the mix looks like by protocol/service/flag. I need the analysis centered on counts above/below thresholds, share-of-total, and cohort comparisons on the real columns in this file, especially duration, src_bytes, dst_bytes, count, srv_count, serror_rate, rerror_rate, same_srv_rate, diff_srv_rate, protocol_type, service, and flag. Please structure it so a small sub-agent team can work in parallel and then combine into one concise summary JSON.
```

### 685. D9_k984616_zh (domain=D9, difficulty=6)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一次面向安全分析的数据质量审计，重点检查缺失值、`?`/空白占位、重复记录、数值范围违规、以及类别字段是否存在异常取值或不一致。请把结果拆成 4-6 个彼此独立的分析轨道并分别给出结论，最后汇总成一份可直接交付给安全团队的简明审计摘要。重点关注这些字段：`protocol_type`、`service`、`flag`、`class`，以及所有数值型特征（如 `duration`、`src_bytes`、`dst_bytes`、`count`、`serror_rate`、`same_srv_rate` 等）。同时请识别：1）任何空值/`?`/空字符串占位；2）重复行及其占比；3）明显不合理的取值范围（例如负数、比例型字段不在 [0,1]、计数型字段为负）；4）类别字段中低频或异常类别；5）与标签 `class` 相关的数据质量偏差。请把每个分析轨道的发现都写清楚，并指出是否会影响后续入侵检测建模或规则分析。
```

### 686. D9_k984718_en (domain=D9, difficulty=6)

```
Using waddahali__fraud-detection__fraud.csv, run a security-analytics review focused mainly on temporal / sequence behavior: break the data into time-like sequence segments using hour_of_day and compare fraud rate changes, missingness patterns, and feature shifts over those segments. Please also look for operational patterns tied to is_weekend, prev_transactions, velocity_score, distance_from_home, and network_quality, and summarize any periods or segments where fraud concentration appears to rise or fall. I need this split into a small team’s workstream so the output should be organized into separate analysis tracks and end with a concise analysis_summary.json.
```

### 687. D9_k984764_zh (domain=D9, difficulty=6)

```
请基于文件 jorekai__anomaly-detection-falling-people-events__data_15.csv 做一份面向安防分析的关联与驱动因素分析，重点看哪些数值字段会一起变化、哪些特征和 anomaly 最相关，以及这些关系在不同标签通道下是否一致。请把结果整理成 analysis_summary.json，要求结论尽量量化、可复核，并且按下面 4-6 个相互独立的分析方向拆分给不同子任务并行完成：1）整体缺失与字段分布概览，确认 x/y/z 和四个通道列的基础质量；2）全量相关性矩阵与 top associations，重点输出与 anomaly 以及彼此之间相关性最高的字段对；3）按 anomaly 分组比较 x/y/z 和各通道的均值、中位数与样本量，判断异常样本是否有稳定的数值偏移；4）按四个通道（010-000-024-033、010-000-030-096、020-000-032-221、020-000-033-111）分别查看其对应样本的 x/y/z 分布与异常率，找出最像驱动因素的字段；5）从极值和边界值角度检查异常样本是否集中在某些 x/y/z 区间；6）补充输出若干最关键的成对相关性（四舍五入到 2 位小数）和对应样本占比，方便给安全运营团队直接使用。
```

### 688. D9_k984785_en (domain=D9, difficulty=6)

```
Using the file ajiboyetoluwalase__wordpress-ddos-log-dataset__wordpress_ddos_log_transform.csv, run a security analytics review focused mainly on correlation and driver analysis. I want you to identify which fields move together, highlight the strongest rounded correlations among usable numeric encodings, and explain what seems to drive the observed DDoS pattern in this WordPress log. Please use the real columns exactly as provided: Unnamed: 0, IP adress, Port, Wordpress Version, Website, DT, and Time. Break the work into independent tracks so it can be split across a small team: one track for data quality/field normalization, one for correlation analysis of numeric features, one for top association checks between Port and WordPress Version, one for temporal concentration patterns, and one for website/IP concentration drivers. Summarize the findings in analysis_summary.json with concise, analyst-ready bullets and a short list of the strongest associations.
```

### 689. D9_k984787_en (domain=D9, difficulty=6)

```
Using inputs/balaka18__email-spam-classification-dataset-csv__emails.csv, analyze this email security dataset with the main focus on distribution and threshold cohorts: how message-word counts behave above/below business thresholds, how emails split into quantile buckets, and how the mix of emails changes across those cohorts. Please treat the word-count columns as signal features and give me a concise security-analytics readout that I can use to understand which terms and sender-pattern features separate low-activity vs high-activity emails. Break the work into independent tracks so different analysts can work in parallel: (1) threshold cohort sizing and mix shares for key terms, (2) quantile bucket distributions for suspicious tokens, (3) top/bottom cohort comparison of email-length proxies and keyword intensity, (4) concentration of enron/company/sender-related tokens in high-frequency emails, and (5) overlap of multiple threshold conditions to identify dense-risk cohorts.
```

### 690. D9_k984911_en (domain=D9, difficulty=6)

```
Using the file ajiboyetoluwalase__wordpress-ddos-log-dataset__wordpress_ddos_log_transform.csv with the columns Unnamed: 0, IP adress, Port, Wordpress Version, Website, DT, and Time, I need a security-analytics deep dive focused mainly on correlation and driver analysis. Please identify which numeric or ordinal fields move together, which categorical combinations are most associated with the suspicious 503/913 port pattern, and what the strongest structural drivers look like in this log. Split the work into independent tracks so different analysts can work in parallel: one track on port-pattern prevalence and co-occurrence, one on WordPress version associations, one on temporal concentration, one on IP/website concentration and reuse, and one on cross-tab/association strength summaries. I only need concise, decision-ready outputs with rounded correlations where applicable and the top associations that look operationally meaningful.
```

### 691. D9_k984916_en (domain=D9, difficulty=6)

```
Using the file eswarchandt__phishing-website-detector__phishing.csv, I need a security analytics review focused mainly on anomaly and outlier detection using explicit numeric rules. Please break it into 4-6 independent workstreams so different analysts can work in parallel. I want you to identify unusual rows and feature patterns in the phishing indicators, especially values that are rare, extreme, or inconsistent under rule-based thresholds. Please center the analysis on columns like AgeofDomain, WebsiteTraffic, PageRank, LinksPointingToPage, DomainRegLen, SubDomains, and any other fields with obvious outlier behavior, while also checking for rare category/value combinations across the binary and ternary features. I need a concise final analysis summary in JSON format, plus the supporting checks that validate the main anomalies, their frequencies, and the most extreme observations.
```

### 692. D9_k984976_en (domain=D9, difficulty=6)

```
Using mryanm__luflow-network-intrusion-detection-data-set__2020.06.22.csv, build a security-analytics review focused mainly on distribution and threshold cohorts. I need a concise but rigorous readout of how traffic differs across benign vs outlier labels, especially around business thresholds like zero-vs-nonzero bytes, low vs high packet counts, short vs long duration, and lower/upper quantile buckets. Use the real columns in the file: avg_ipt, bytes_in, bytes_out, dest_ip, dest_port, entropy, num_pkts_out, num_pkts_in, proto, src_ip, src_port, time_end, time_start, total_entropy, label, duration. Decompose the work into separate tracks so it can be split across agents: threshold cohort sizing, quantile-bucket mix, label composition by cohort, port/protocol concentration, and cross-threshold interactions. Return the results as analysis_summary.json with deterministic counts and shares only.
```

### 693. D9_k984992_zh (domain=D9, difficulty=6)

```
请基于文件 arnobbhowmik__ton-iot-network-dataset__train_test_network.csv 做一次安全分析，重点是按不同分类分组看“差异/分段”——也就是比较各个标签、协议、服务、连接状态等组之间的速率、均值和占比差异，找出最大的分段鸿沟，并结合少量端口、DNS、SSL/HTTP 字段做交叉验证。请输出一个可直接给管理层看的 analysis_summary.json，里面至少要包含：1）按 label 和 type 的总体分布及不平衡程度；2）不同 label/type 在 proto、service、conn_state 上的占比/均值对比，以及差异最大的组；3）按 label/type 分组的流量强度指标（duration、src_bytes、dst_bytes、src_pkts、dst_pkts、src_ip_bytes、dst_ip_bytes）均值比较，指出最大均值差；4）DNS/SSL/HTTP 相关字段在正常与攻击流量之间的分段比较，特别是缺失率、出现率和关键类别的差异；5）端口分段（如 80/53/443/445/8080 等）在不同标签下的流量画像和最异常的组合；6）整理出最值得进一步调查的 5 个“高风险分段”结论。请尽量只围绕分组比较和组间差距展开，不要做建模预测。数据列包含 src_ip、src_port、dst_ip、dst_port、proto、service、duration、src_bytes、dst_bytes、conn_state、missed_bytes、src_pkts、src_ip_bytes、dst_pkts、dst_ip_bytes、dns_query、dns_qclass、dns_qtype、dns_rcode、dns_AA、dns_RD、dns_RA、dns_rejected、ssl_version、ssl_cipher、ssl_resumed、ssl_established、ssl_subject、ssl_issuer、http_trans_depth、label、type 等。
```

### 694. D9_k984998_en (domain=D9, difficulty=6)

```
Using the file manavkhambhayata__cve-2024-database-exploits-cvss-os__nvd_vulnerabilities_with_os.csv, build a security-analytics brief that focuses mainly on temporal and period-over-period trends in CVE severity and exploit characteristics. I need you to treat the CVE entries as a time sequence using the CVE ID year, then compare how the distribution of CVSS Score, Attack Vector, and Affected OS changes over time. Please split the work into independent tracks so different analysts could work in parallel: year-over-year volume and severity trends; attack-vector mix trends; affected-OS concentration and change over time; high-severity CVE incidence and its trend; and any notable anomalies or shifts in the most common attack vectors or OS targets. Use the real columns CVE ID, Description, CVSS Score, Attack Vector, and Affected OS only, and keep the output grounded in the dataset values.
```

### 695. D9_k985004_en (domain=D9, difficulty=6)

```
Using nudratabbas__healthcare-fraud-detection-dataset__healthcare_fraud_detection.csv, analyze the security-risk profile of claims with a focus on distribution and threshold cohorts. I want a compact but rigorous readout of how fraud-related behavior changes across business cutoffs such as high claim amounts, long delays between service and claim, high provider monthly volume, longer length of stay, and high prior-visit intensity. Use the real columns in the file, especially Claim_Amount, Approved_Amount, Days_Between_Service_and_Claim, Number_of_Claims_Per_Provider_Monthly, Length_of_Stay, Prior_Visits_12m, Claim_Status, Insurance_Type, Provider_Specialty, Patient_State, and Is_Fraud. Break the work into independent tracks so different analysts can work in parallel, and summarize the mix shares and cohort counts above/below thresholds, plus any concentration across quantile buckets.
```

### 696. D9_k985072_zh (domain=D9, difficulty=6)

```
请基于数据文件 eswarchandt__phishing-website-detector__phishing.csv 做一份面向安全分析的多维诊断，重点围绕“哪些数值特征彼此一起变化、哪些特征与 class 的关联最强、以及这些关联在不同特征簇里是否一致”来展开。请直接读取并分析 df（已加载），把结论整理成 analysis_summary.json。重点变量包括 UsingIP、LongURL、ShortURL、Symbol@、Redirecting//、PrefixSuffix-、SubDomains、HTTPS、DomainRegLen、Favicon、NonStdPort、HTTPSDomainURL、RequestURL、AnchorURL、LinksInScriptTags、ServerFormHandler、InfoEmail、AbnormalURL、WebsiteForwarding、StatusBarCust、DisableRightClick、UsingPopupWindow、IframeRedirection、AgeofDomain、DNSRecording、WebsiteTraffic、PageRank、GoogleIndex、LinksPointingToPage、StatsReport、class。需要尽量用相关系数、分组统计、Top-N 关联、以及与 class 的对照来解释驱动因素；不要做建模预测。请拆成 4-6 个彼此独立的分析轨道并分别给出结论：1）全局相关矩阵与最强正/负相关对；2）与 class 的相关性与排序；3）按强相关特征簇做局部关联检查；4）识别近乎冗余或方向一致的特征对；5）对高风险/低风险方向的特征做频次与均值对比；6）如果需要，补充离群或不一致特征的检查。
```

### 697. D9_k985081_zh (domain=D9, difficulty=6)

```
请基于文件 piyushrumao__malware-executable-detection__uci_malware_detection.csv 做一版安全分析，重点看各特征在不同阈值和分位数下的分布、分层占比和“高值 cohort”的混合结构。我想快速判断哪些特征在恶意/良性样本之间的高低分布差异最明显，以及在业务阈值下样本会如何被切分。请直接使用现成列 Label、F_1 到 F_29（如果你发现表里还有更多 F_* 列，也请一并纳入同样逻辑）来做，不要建模，不要画图，只要能支持我后续决策的统计结论。请把结果整理成可读摘要，并输出一份 analysis_summary.json。分析请拆成 4-6 个彼此独立的方向，方便并行处理：阈值 cohort 计数、分位数桶分布、Label 交叉混合、极端值集中度、特征间相关性、以及缺失/异常值排查。
```

### 698. D9_k985132_en (domain=D9, difficulty=6)

```
Using joebeachcapital__phiusiil-phishing-url__PhiUSIIL_Phishing_URL_Dataset.csv, run a security-analytics review focused mainly on segment comparison across categorical groups. I want to understand which URL/profile segments look most phishing-like versus legitimate-like by comparing rates and means across groups, and I want the biggest gaps called out clearly. Please structure the work into separate tracks so different analysts could handle them in parallel: (1) compare label rates and feature means by TLD, (2) compare the same by IsHTTPS and IsDomainIP, (3) compare by HasObfuscation and NoOfSubDomain buckets, (4) compare by HasTitle/HasFavicon/Robots/IsResponsive style page-structure flags, (5) compare by mixed URL character patterns like HasQuestionMark/HasEquals/NoOfOtherSpecialCharsInURL, and (6) identify the single strongest categorical segment gaps and provide concise security interpretation. Use the real columns in the file, keep results quantitative, and emphasize the largest between-group differences.
```

### 699. D10_g1048_en (domain=D10, difficulty=7)

```
I need you to analyze the files in inputs/ (customers.csv, campaigns.csv, feedback_tickets.csv, competitor_tracking.xlsx, and ops_data.sqlite) and produce 2-3 compact report files (CSV/JSON/MD) that synthesize CRM, churn, feedback, GTM, and competitor intelligence. Use the standard definitions and formulas you have for risk scoring, campaign ROI, complaint themes, etc. Just give me the key aggregates and top rankings.
```

### 700. D10_g1195_en (domain=D10, difficulty=7)

```
I need a synthesis brief from the files below in ./inputs. The goal is to reconcile evidence across sources into a compact findings brief plus an evidence table. Mention any cross-source conflicts, duplicates, nulls, or anomalies.

- crm_accounts.csv  
- campaign_performance.xlsx  
- customer_feedback.xlsx  
- interaction_log.csv  
- market_ops.sqlite  

Specifically, please provide:

- Top 3 complaint themes from customer feedback (deduplicated, using the closed theme set, with count and deficit).  
- Top 3 most at‑risk accounts (with risk score).  
- Top 3 best‑ROI campaigns (with ROI).  
- Dominant anomaly family from the interaction log (degraded rows only) and top 3 families.  
- The account with the most degraded rows (top 3 accounts with counts).  
- Largest feedback/account mismatch (top 3 accounts with mismatch count).  
- Watchlist account count.  
- Cross‑source checks: whether the top complaint theme matches the largest anomaly family, and whether the riskiest account is in the watchlist.  
- A one‑paragraph operational recommendation.

Keep deliverables concise: a markdown brief and a compact evidence table.
```

### 701. D10_g1200_zh (domain=D10, difficulty=7)

```
用 ./inputs/ 下的 customer_interactions.csv、crm_data.xlsx、campaigns.xlsx、theme_keywords.xlsx 和 competitors.xlsx，生成一份 executive_summary.md 综合报告（反馈聚类、流失分析、广告ROI、竞争对手跟踪及异常），以及 top_risky_customers.csv 和 top_campaigns_roi.csv。报告和CSV按常规口径处理即可。
```

### 702. D10_g1266_en (domain=D10, difficulty=7)

```
I need you to synthesize a compact research brief and an evidence table from the five files in `inputs/`: `customers_crm.csv`, `support_tickets.csv`, `campaigns_gttm.xlsx`, `customer_reviews.xlsx`, and `competitor_tracking.md`. The brief (`findings.md`) should cover 3–4 independent analysis tracks plus a cross-source reconciliation note; the table (`evidence_table.csv`) should contain the exact summary metrics you normally compute. Handle deduplication and missing values in the usual way.
```

### 703. D10_g980814_zh (domain=D10, difficulty=7)

```
我需要你把这三份文件合成一份面向销售和客户运营的简报，帮我判断本季度该先盯哪些客户、该推哪类活动、以及当前市场里最值得注意的竞争动向。请把结果做成一份紧凑的汇总文件，既要能给管理层看，也要能直接给团队执行。我还想顺手把客户主数据里的重复项、反馈里的主要投诉方向、最该优先的流失风险客户、回报最高的活动、以及竞争对手跟踪里的重点变化都一起整理出来。输入文件就是 customer_market_ops_master.xlsx、competitor_tracking_daily.csv 和 crm_activity_log.txt。
```

### 704. D10_g980899_zh (domain=D10, difficulty=7)

```
请基于 inputs/customer_accounts.xlsx、inputs/support_tickets.xlsx 和 inputs/market_signals.xlsx 做一份 customer & market ops 的综合分析简报，输出 findings.md。
- 需要同时看客户风险、工单主题、活动表现和竞品动态，并把三份来源之间的结论对齐。
- 重点帮我列出风险客户看板、最主要的投诉/反馈主题、ROI 最好的活动，以及值得跟进的竞品信号。
- 如果三份材料里有口径不一致或信息冲突，也请在简报里单独说明。
```

### 705. D10_g981118_zh (domain=D10, difficulty=7)

```
需要把这批客户与市场运营素材整理成一个可直接给销售、客服和市场团队看的简报，重点是：找出最值得优先跟进的科技客户、最需要关注的流失风险客户、最近反馈里最主要的投诉主题、回报最好的营销活动，以及竞争对手最近释放出的关键价格/续约信号。输入文件是 customer_accounts.xlsx、customer_metrics.xlsx、feedback_samples.docx、campaign_performance.xlsx、competitor_news_log.csv。请输出一份合并后的报告，内容要短，但每个结论都要带上对应的表格和关键数字，方便我直接拿去开会。
```

### 706. D10_g981534_zh (domain=D10, difficulty=7)

```
我把三份文件都放在 inputs 里了：customer_feedback_reviews.xlsx、churn_sales_crm.xlsx、campaign_competitor_tracking.xlsx，还有一份 briefing_memo.pdf。请你帮我把这次客户与市场运营的材料整合成一个简短汇总，重点看评论主题、流失风险、活动ROI、竞品态势和需要更新到CRM的客户，最后输出一份单文件结果。
```

### 707. D10_g981598_zh (domain=D10, difficulty=7)

```
公司最近收集了客户反馈数据、CRM数据、营销活动反馈和竞争对手动态。我需要一份汇总报告，包含以下四个部分：
1. 找出书评和应用评论中最主要的投诉主题（前三个），并给出每个主题的投诉数量和平均评分（投诉定义为评分≤2）。
2. 根据客户数据计算风险评分（风险评分 = 0.5*流失概率 + 0.3*逾期比率 + 0.2*工单数），识别前三名高风险客户。
3. 计算每个营销活动的ROI（(收入-支出)/支出），排名前三的活动。
4. 从竞争对手跟踪数据中找出影响评分最高的前三名对手。
请将结果整合到一个Excel文件（包含四个工作表）和一个Word文檔（简要说明）中。输入文件位于inputs/目录下：reviews.xlsx, customer_data.xlsx, campaign_feedback.xlsx, competitor_tracking.xlsx, customer_review_link.xlsx（链接客户与评论，可选）。
。
```

### 708. D10_g981685_zh (domain=D10, difficulty=7)

```
我需要你基于输入文件 `customer_market_ops_data.xlsx` 和 `market_brief.pdf` 做一份面向销售运营/客户运营的决策简报。请把评论聚类、客户流失风险、GTM活动ROI、竞品跟踪、以及CRM更新这几块一起合并，最后只输出一份简短的 `decision_brief.md`。我希望你先按去重规则处理重复的 `ticket_id`、`campaign_id` 和评论样本，再按定义好的口径算出各项指标，尤其是风险客户、最佳ROI活动、最高投诉主题和最需要跟进的竞品都请给出Top-3排名和对应分数，别只写一个ID。我还想看到一个明确的推荐结论：本周应该优先把预算、客服和销售跟进资源投到哪里，以及为什么。
```

### 709. D10_g981931_zh (domain=D10, difficulty=7)

```
请基于 customer_market_ops_core.xlsx、feedback_reviews.xlsx 和 event_log_large.csv 做一份合并版客户与市场运营简报，重点看客户流失风险、活动投放效率、投诉主题、竞品动态和日志里埋的几条关键信号。我希望最后只输出一份紧凑的汇总文件，里面把最重要的结论和对应的明细表都放一起。
```

### 710. D10_g981936_zh (domain=D10, difficulty=7)

```
请基于 customer_feedback.xlsx, campaign_performance.csv, CRM_updates.csv 这三份材料，整理一份面向客户与市场运营的综合分析简报，重点把客户反馈、流失风险、竞品动态和活动效果串起来看。
- 先把客户反馈按主题聚类，给出最主要的投诉/表扬主题，以及每个主题的规模和代表性例子。
- 再找出当前最值得优先跟进的高风险客户，并说明判断依据，同时给出风险最高的前三位。
- 结合活动与销售线索，判断哪类市场动作最有效，顺带指出需要复盘的低效活动。
- 最后把竞品追踪里提到的核心变化和CRM更新里需要同步的动作合并成一页结论，写清楚跨来源是否一致、哪里有冲突。
- 输出一份紧凑的 findings.md，要求有小标题、表格或要点，并明确写出各来源之间的对齐/差异。
```

### 711. D10_g982052_zh (domain=D10, difficulty=7)

```
请结合 inputs/customer_feedback_and_crm.xlsx、inputs/campaign_competitor_weekly.xlsx 和 inputs/theme_labels.json，帮我整理一份中文分析简报 findings.md。我要同时看客户反馈主题、CRM 风险客户、活动 ROI、竞品跟踪和周度流失信号，顺带把跨来源里有冲突或异常的地方也写清楚，最后给我一个可以直接拿去内部讨论的简版结论。
```

### 712. D10_g982115_zh (domain=D10, difficulty=7)

```
请基于这 4 个输入文件做一份面向销售运营和客户运营的综合分析简报，输出为 findings.md。
- 先把客户反馈、流失风险、活动表现、竞品动态这四条线各自梳理清楚，再合并成一份可执行的结论。
- 重点帮我找出：最需要优先处理的客户、最值得复投的活动、最突出的投诉主题、以及竞品上值得警惕的变化。
- 需要把跨文件之间的口径差异、冲突数据、重复记录或异常点单独写出来，别直接混在结论里。
- 最后给一个简短的行动建议列表，方便我直接转给团队跟进。
```

### 713. D10_k982343_en (domain=D10, difficulty=7)

```
Using radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv, build a customer analytics readout centered on ranking and concentration: identify which customer segments and product/behavior groups account for the largest shares of churn, complaints, and customer value. I need this split into independent workstreams so they can be analyzed in parallel. Please focus on the real columns in the file, especially Exited, Complain, CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Satisfaction Score, Card Type, and Point Earned, and quantify top-N concentration, Pareto-style shares, and the most extreme groups by frequency/value.
```

### 714. D10_k982462_zh (domain=D10, difficulty=7)

```
请基于文件 karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv 做一份面向客户分析的综合分析，重点围绕“排名与集中度”展开：看哪些游戏/评分/设备在评论量、点赞量和情绪分布上最集中，Top-N 贡献了多少总量，是否存在明显的头部效应或帕累托特征。请充分利用现有字段 rating、review_content、likes、publish_time、device_model、game_name、sentiment，不要改动任何原始值。我要的是可直接用于汇报的结论性分析，不要泛泛而谈。请拆成几个彼此独立、可以并行推进的分析轨道，并最终输出一份 analysis_summary.json。重点关注：1）评论量与点赞量的头部游戏排名；2）头部游戏对总评论/总点赞的集中度；3）评分与情绪标签的集中度及偏态；4）设备机型的头部集中度；5）时间维度上高峰期是否被少数日期/月份主导；6）在头部游戏中评论、点赞、评分、情绪的联动差异。
```

### 715. D10_k982596_zh (domain=D10, difficulty=7)

```
请基于文件 blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv 做一份面向客户分析的深度分析，重点围绕“分布与阈值分层（business thresholds / quantile buckets / mix shares）”展开。请直接使用现有字段（customerID、gender、SeniorCitizen、Partner、Dependents、tenure、PhoneService、MultipleLines、InternetService、OnlineSecurity、OnlineBackup、DeviceProtection、TechSupport、StreamingTV、StreamingMovies、Contract、PaperlessBilling、PaymentMethod、MonthlyCharges、TotalCharges、Churn），不要改动任何原始值。我要你把分析拆成 4-6 个彼此独立的分析轨道，便于并行推进；每条轨道都要输出能落地的业务结论，而不是只做描述统计。

重点要求：
1) 以阈值和分层为主线，例如按 tenure、MonthlyCharges、TotalCharges 做业务阈值分组（如低/中/高、四分位、业务门槛以上/以下），看 churn 的数量、占比、混合结构。
2) 结合合同类型、支付方式、是否开通纸质账单、是否为 SeniorCitizen 等，分析不同阈值群体的 churn mix share 和规模贡献。
3) 对互联网服务/增值服务组合做分布切片，找出高风险 cohort 的占比变化。
4) 需要输出可复核的关键数值：各阈值段样本数、churn 数、churn rate、分位数切片下的 mix share、Top N 类别的 churn 贡献。
5) 结果要适合最后整理成一份 analysis_summary.json，便于我直接给业务团队看。

请注意：这是固定真实数据，所有统计必须完全基于数据本身计算，不要假设任何额外字段或编造数值。
```

### 716. D10_k982924_zh (domain=D10, difficulty=7)

```
请基于文件 karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv 做一版面向客户分析的深度分析，重点围绕“排名与集中度”来展开：先看不同游戏、不同设备、不同评分/情感在评论量和点赞量上的Top-N分布，再评估头部是否高度集中（例如前几名游戏贡献了多少评论/点赞、是否符合帕累托特征），最后结合评论内容与发布时间补充解释哪些头部游戏/人群更容易形成集中度。请直接输出一个 analysis_summary.json 风格的结果，要求结论能支持业务决策，比如应该优先关注哪些游戏、哪些机型、哪些低评分/高点赞的高影响评论群体，以及集中度是否意味着资源应该优先投向头部对象。
```

### 717. D10_k982934_zh (domain=D10, difficulty=7)

```
请基于文件 radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv 做一份面向客户分析的深度分群对比报告。我最关心的是不同客户细分之间的差异，尤其是按类别分组后的流失率、均值和最大差距。请围绕 Geography、Gender、Card Type、Complain、Satisfaction Score、IsActiveMember、NumOfProducts、Age、Balance、CreditScore、EstimatedSalary、Point Earned、Exited 等字段展开分析，找出各细分组之间最显著的差距，并说明哪些群体更容易流失、哪些指标差异最大、这些差异是否与投诉、活跃度和产品数有关。请把分析拆成彼此独立的几个子任务，便于不同分析师并行处理，最后汇总成一个简洁的结论文件 analysis_summary.json。
```

### 718. D10_k982940_zh (domain=D10, difficulty=7)

```
请基于文件 radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv 做一份面向客户分析的综合诊断，重点围绕“时间/序列趋势”来展开：虽然这份数据没有真实日期列，但请把 RowNumber 当作数据采样顺序，用分位段（例如按 RowNumber 排序后分成前/中/后期，或每 300/500 条形成序列窗口）来观察流失相关指标的变化、阶段性拐点和结构性差异。我要你同时从 4-6 个互相独立的角度拆解，最后给出一份可交付给业务负责人的结论摘要，说明哪些群体在“序列前后”变化最明显、哪些因素与 Exited/Complain 的联动最强、以及是否存在某些产品/卡类型/地域组合在后期明显恶化。请尽量把分析做成可复核、可落地的统计结论，不要只给泛泛建议。数据中的字段包括 CreditScore、Geography、Gender、Age、Tenure、Balance、NumOfProducts、HasCrCard、IsActiveMember、EstimatedSalary、Exited、Complain、Satisfaction Score、Card Type、Point Earned 等。
```

### 719. D10_k983619_zh (domain=D10, difficulty=7)

```
请基于文件 blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv 做一份面向客户分析的综合诊断，重点围绕“时间/序列趋势”展开：我想知道客户流失是否存在明显的早期流失、随任期（tenure）推进的流失变化、不同合同类型在任期分层下的流失轨迹是否不同，以及账单/服务特征是否在这些趋势中起到放大或缓冲作用。请按可交付给业务团队的方式输出结论，并把分析拆成若干可并行推进的部分。务必结合真实字段：tenure、Contract、MonthlyCharges、TotalCharges、InternetService、TechSupport、OnlineSecurity、PaperlessBilling、PaymentMethod、SeniorCitizen、Partner、Dependents、Churn 等。最后请给出一个可复用的分析摘要文件 analysis_summary.json 的内容框架，方便后续汇总。
```

### 720. D10_k983701_zh (domain=D10, difficulty=7)

```
请基于文件 karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv 做一份面向客户分析的深度复盘，重点看“排行与集中度”——例如 Top-N 游戏/设备/评分/情感在评论量上的集中情况、头部占比、以及是否存在明显的 Pareto 现象。请结合真实列 rating、review_content、likes、publish_time、device_model、game_name、sentiment 来输出可执行结论，最好能判断哪些游戏/设备最值得优先关注，以及高热度评论是否高度集中在少数对象上。数据固定，不要臆造值；如果需要，先做基础清洗（例如去掉缺失或空字符串）。
```

### 721. D10_k983706_zh (domain=D10, difficulty=7)

```
请基于文件 blastchar__telco-customer-churn__WA_Fn-UseC_-Telco-Customer-Churn.csv 做一份面向客户分析的多部分数据分析，重点先做数据质量审计，再判断这些质量问题会不会影响我后续的流失分析。请直接围绕真实字段 customerID、gender、SeniorCitizen、Partner、Dependents、tenure、PhoneService、MultipleLines、InternetService、OnlineSecurity、OnlineBackup、DeviceProtection、TechSupport、StreamingTV、StreamingMovies、Contract、PaperlessBilling、PaymentMethod、MonthlyCharges、TotalCharges、Churn 展开，不要改值。我要你拆成 4-6 个彼此独立的分析轨道，方便我并行交给不同子任务：1）缺失值/空字符串/问号占比与分布审计，尤其是 TotalCharges 这类应为数值却是 object 的字段；2）重复客户与主键唯一性审计（customerID 是否重复、是否存在完全重复行）；3）类别字段一致性与异常值审计（比如 Yes/No、No internet service、No phone service、Contract、PaymentMethod 等是否存在拼写不一致、隐藏空格、未预期取值）；4）数值字段范围与逻辑一致性审计（tenure、MonthlyCharges、SeniorCitizen、TotalCharges 的范围、空值转换后是否异常，tenure=0 时 TotalCharges 是否为 0 或空）；5）这些质量问题对 churn 分布的潜在影响（按 Churn 分组比较缺失率、异常率、重复相关情况）；6）最后给出一份可落地的清洗优先级和验证清单。请输出适合我直接汇报给业务方的结论框架，并把可复核的统计结果放在 analysis_summary.json 里。
```

### 722. D10_k983815_zh (domain=D10, difficulty=7)

```
请基于数据文件 karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv 做一份面向客户分析的多维分析，重点围绕时间趋势和阶段性变化来判断用户口碑是否在变好/变差。数据里有这些字段：rating、review_content、likes、publish_time、device_model、game_name、sentiment。请你不要只做静态汇总，而是要按时间序列拆解，结合评分、情绪、点赞、游戏维度、设备维度一起看，尽量找到“什么时候发生了变化、变化有多大、影响集中在哪些游戏/设备上”。

我需要你把分析拆成多个可并行的子任务，最好能让不同分析人员分别负责：
1) 全局按月趋势：看评论量、平均评分、正向率、平均点赞数的月度变化，以及是否存在明显的环比波动；
2) 游戏维度趋势：识别评论量最高的游戏，并比较它们在月度评分/情绪上的变化路径，找出哪个游戏改善最快或下滑最快；
3) 设备维度趋势：看不同 device_model 的口碑是否随时间变化，特别是高频设备是否出现持续低分或持续高分；
4) 时间段对比：把整个时间范围切成前后两个阶段，比较关键指标的阶段差异，判断口碑拐点是否存在；
5) 点赞与口碑关系：分析点赞数在不同时间段、不同评分/情绪下的分布，看看高互动评论是否更偏正面或负面；
6) 重点异常定位：找出月度异常波动最大的游戏或设备，给出可解释的候选对象。

最终输出请面向业务阅读，重点回答：整体口碑趋势是否改善、变化发生在哪些月份、哪些游戏/设备是主要驱动、正负面评论在互动上是否有明显差别。请严格基于数据，不要编造。需要给我一个可直接落地的分析框架和结论要点。
```

### 723. D10_k983878_zh (domain=D10, difficulty=7)

```
请基于文件 karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv 做一份客户分析，重点围绕时间趋势和阶段性变化来回答：用户评分、情感、点赞、设备与不同游戏之间的口碑是如何随时间变化的。请结合列 rating、review_content、likes、publish_time、device_model、game_name、sentiment 做分析，尤其关注按时间序列的周期波动、月度/周度变化、前后期对比、以及不同游戏在时间维度上的差异。希望输出一份可供业务讨论的结论摘要，能指出哪些游戏的口碑在近期明显改善或下滑、哪些时间段互动更强、以及评分和情感是否同步变化。
```

### 724. D10_k983936_zh (domain=D10, difficulty=7)

```
请基于文件 radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv 做一份面向客户运营的异常与离群分析，重点围绕“显式数值规则”识别风险客户和数据异常：请把信用分、年龄、余额、产品数、消费/活跃状态、满意度、积分等字段结合起来，用清晰可复核的阈值（例如 IQR、极端分位数、业务规则、罕见类别）找出异常样本，并说明这些异常在流失（Exited）、投诉（Complain）和客户画像上的分布。请尽量把分析拆成多个独立轨道，方便并行推进：例如数值离群点、组合规则异常、罕见类别与极端值、异常与流失/投诉关联、以及按国家/性别/卡类型的异常分布。最终输出一份 analysis_summary.json，给出关键异常定义、异常客户数量、最极端的客户记录统计、以及异常群体的业务解释。请基于真实数据，不要臆造任何值。字段名请严格使用原始列名，包括 RowNumber, CustomerId, Surname, CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Exited, Complain, Satisfaction Score, Card Type, Point Earned。
```

### 725. D10_k984080_zh (domain=D10, difficulty=7)

```
请基于文件 radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv 做一份面向客户分析的深度数据解读，重点围绕“分布与阈值分层”展开：不要只看整体均值，而要回答不同阈值、分位数分层、以及各细分人群的占比和构成。请围绕真实字段（如 Exited、Complain、Age、CreditScore、Balance、EstimatedSalary、NumOfProducts、Tenure、IsActiveMember、HasCrCard、Geography、Gender、Card Type、Satisfaction Score、Point Earned）做分析，并输出可直接给业务讨论的结论。

请把分析拆成几个彼此相对独立、适合并行推进的子任务：先做整体分布与关键阈值切分，再做流失/投诉在各阈值 cohort 中的占比，再做分位数组与 mix share，再比较地理/性别/卡类型/会员状态等群体的阈值结构，最后汇总哪些阈值最能区分高风险人群。务必使用真实数据，不要编造任何数值。结果需要能支持业务决策，例如：超过某个年龄或余额阈值的人群占比、不同分层中的流失率、投诉率、活跃率、产品数结构、以及各组在总体中的份额。
```

### 726. D10_k984094_en (domain=D10, difficulty=7)

```
Using karwinwang__taptap-mobile-game-reviews-chinese__taptap_game_reviews.csv, build a customer-analytics readout focused mainly on distribution & threshold cohorts. I need a practical view of how reviews split across business thresholds and quantile buckets, with mix shares by game, sentiment, device, and time. Please use the real columns rating, review_content, likes, publish_time, device_model, game_name, sentiment only as available in the file. Decompose it into independent workstreams so it can be handled by a small sub-agent team, and keep the output oriented toward actionable cohort thresholds rather than generic summary stats.
```

### 727. D10_k984557_zh (domain=D10, difficulty=7)

```
请基于文件 radheshyamkollipara__bank-customer-churn__Customer-Churn-Records.csv（字段包括 RowNumber、CustomerId、Surname、CreditScore、Geography、Gender、Age、Tenure、Balance、NumOfProducts、HasCrCard、IsActiveMember、EstimatedSalary、Exited、Complain、Satisfaction Score、Card Type、Point Earned）做一份面向客户分析的多部分深度分析。重点围绕“序列/趋势”角度展开：把 RowNumber 视为记录序列，按记录顺序检查流失率、投诉率、活跃率、产品数、余额、满意度、积分等指标的阶段性变化、前后期对比、滚动趋势和峰值/拐点，并识别哪些人群在不同阶段变化最明显。请把分析拆成多个互相独立的 track，便于并行交付。最终输出 analysis_summary.json，要求给出可执行结论、关键对比、以及值得进一步跟进的客户分群建议。
```

### 728. D10_k984729_zh (domain=D10, difficulty=7)

```
请基于文件 gsagar12__dspp1__customer_product.csv 做一份面向客户分析的多阶段研究，重点放在“相关性与驱动因素分析”上：先把客户-产品订阅关系整理清楚，再判断不同产品、不同时间段、不同客户状态之间哪些数值特征最容易一起变化，并找出最强的关联模式。数据字段只有 customer_id、product、signup_date_time、cancel_date_time 以及一列索引；请围绕这些真实字段，分析产品组合、注册与取消行为、留存/流失时长、不同产品的取消率，以及时间维度上的关联变化。请把结论写成可直接给业务团队看的简洁总结，并明确哪些因素更像是取消的驱动项，哪些只是伴随变化。若有需要，请按产品、是否取消、注册年份/月、以及签约到取消时长拆分分析，重点输出 rounded correlations、top associations、和最关键的交叉对比结果。
```

### 729. D10_k984942_en (domain=D10, difficulty=7)

```
Using the file hopesb__hr-analytics-dataset__Messy_HR_Dataset_Detailed.csv, build a customer-analytics style retention/performance review focused mainly on temporal trends across the date fields (StartDate, ExitDate, Survey Date, Training Date). I need a concise but rigorous multi-part analysis that tells me how the population changes over time, whether engagement/satisfaction/performance is trending up or down by survey period, how turnover timing differs by employee segments, and whether training timing/duration/cost lines up with later employee outcomes. Please use the real columns in the file, especially EmployeeStatus, EmployeeType, DepartmentType, Division, Title, Supervisor, Performance Score, Current Employee Rating, Engagement Score, Satisfaction Score, Work-Life Balance Score, Training Date, Training Duration(Days), Training Cost, Training Outcome, and related demographic fields where useful. Organize the work as if a small team could split it into independent tracks, with the primary emphasis on period-over-period and cohort-style trend analysis rather than static cross-sections.
```

### 730. D11_g1063_zh (domain=D11, difficulty=7)

```
基于 inputs/budget_plan.csv、inputs/expense_transactions.xlsx、inputs/invoice_exceptions.xlsx、inputs/monthly_recon.csv 和 inputs/ops_audit_log.txt，帮我做一份月结支出/预算偏差与发票异常的研究简报。需要分析几条独立线索（预算 vs 实际、发票异常、月度对账、日志核对），最后合成 findings.md 和一张小型证据表格。简报里要包含结论、主要异常、跨源核对和限制这几个部分，所有数字按常规四舍五入保留两位小数。不需要逐笔明细，只要聚合统计和TOP-N异常。
```

### 731. D11_g1331_zh (domain=D11, difficulty=7)

```
基于以下输入文件完成2025年一季度的预算差异与异常审阅，输出2–3个紧凑的汇总报告（JSON + CSV ± MD组合），便于审阅和复核：
- inputs/budget_plan.xlsx
- inputs/exception_log.xlsx
- inputs/invoice_event_log.txt
- inputs/close_notes.json

按我们常规口径处理：仅纳入2025-01-01至2025-03-31数据；汇总粒度按category和cost_center两层；币种按标准汇率换算至USD（EUR 1.08, GBP 1.27, CAD 0.74）；差异公式variance = actual – budget，百分比用variance/budget；材料性阈值为绝对值≥10,000 USD或≥15%；排序按abs(variance)降序，同名按字母升序；金额保留2位小数，百分比报告保留2位小数（核对总差异率时用4位）。异常按exception_id去重计数，同一doc_id不同异常分别计。大日志仅用于核对关键异常埋点，不输出全文。

交付文件需覆盖：
- 整体总览（全公司预算、实际、差异、差异率）
- category与cost_center的预算/实际/差异/差异率及材料性标记
- 满足材料性阈值的category和cost_center排序列表
- exception_log中每种exception_type计数及总数
- 异常金额TOP 5 vendor（附金额及计数）
- invoice_event_log中与高金额异常相关的关键doc_id（至少覆盖已出现的异常埋点）
- 一段简短的季度关账说明（是否需管理层复核及原因）

报告紧凑、可独立复核，不输出逐笔交易或异常明细。
```

### 732. D11_g980974_zh (domain=D11, difficulty=7)

```
请基于 inputs/budget_spend_q1_2026.xlsx、inputs/AP_and_Expense_Exceptions_Q1_2026.xlsx、inputs/finance_policy_reference_q1_2026.xlsx 做一版 2026 年 Q1 的费用报销与预算偏差复核简报，输出 findings.md。我要看到按成本中心/类别的预算-实际汇总、异常类型计数、以及按材料性筛出来的 Top 异常交易和跨源对账结论。
```

### 733. D11_g981454_zh (domain=D11, difficulty=7)

```
本月关账要尽快把预算、实际支出和异常情况整理成一份可直接给管理层看的简报，我需要你综合 inputs/budget_plan.xlsx、inputs/expense_ledger.xlsx 和 inputs/market_news.xlsx，输出一个完整但精简的汇总文件，重点看各类别和成本中心的预算差异、异常类型数量、以及达到重要性门槛的前几条异常。同时把新闻里那批真实嵌入的样例也按标签汇总一下，方便我们确认数据口径没有跑偏。
```

### 734. D11_g982058_en (domain=D11, difficulty=7)

```
I need a finance close review brief based on finance_close_pack.xlsx, invoice_ledger.csv, and expense_audit_log.txt. Please synthesize the monthly spend variance review, the invoice/expense exception patterns, and the audit-log corroboration into one compact findings.md. I want variance by category and by cost center, totals, exception counts by exception type, and a top material exceptions table using the same materiality threshold throughout. Please also reconcile any mismatches between the workbook, the invoice ledger, and the audit log, and call out the specific lines or records that support the key findings. Keep the output concise but complete, and make sure the cross-source notes explain where the files agree or diverge.
```

### 735. D11_k982613_en (domain=D11, difficulty=7)

```
Using yasserh__loan-default-dataset__Loan_Default.csv, please run a finance-risk anomaly review focused on explicit numeric-rule outliers and unusual combinations. Use the real columns in the file, especially loan_amount, rate_of_interest, Interest_rate_spread, Upfront_charges, term, property_value, income, Credit_Score, LTV, and dtir1, plus categorical fields like loan_limit, Gender, loan_type, loan_purpose, Credit_Worthiness, open_credit, business_or_commercial, Neg_ammortization, interest_only, lump_sum_payment, occupancy_type, total_units, credit_type, co-applicant_credit_type, age, submission_of_application, Region, Security_Type, and Status. I want a compact but practical analyst output that identifies extreme numeric values, rare-category records, cross-field inconsistencies, and segments with the highest anomaly concentration. Split the work into 4-6 independent tracks so different sub-agents could work in parallel: (1) data-quality profiling and missingness, (2) numeric outlier detection with explicit thresholds/IQR/rule-based extremes, (3) rare-category and unusual-combination detection, (4) regional and product-segment concentration of anomalies, and (5) a concise remediation/prioritization view for risk review. Keep the conclusions business-facing and tied to loan-default monitoring.
```

### 736. D11_k982927_en (domain=D11, difficulty=7)

```
Using yasserh__loan-default-dataset__Loan_Default.csv, analyze loan-default risk and pricing differences across borrower segments with a focus on segment comparison across categorical groups (rates/means per group and the biggest gaps between segments). I need a finance-style readout that compares approval/rate/pricing outcomes by Gender, loan_limit, loan_type, loan_purpose, Credit_Worthiness, credit_type, age, and region-related fields where available, and then identifies the largest segment gaps and any notable missing-data concentration that could bias the comparison. Please decompose this into a few independent workstreams so different analysts can work in parallel, and summarize the findings in analysis_summary.json.
```

### 737. D11_k982995_zh (domain=D11, difficulty=7)

```
请基于文件 yasserh__loan-default-dataset__Loan_Default.csv 做一份面向金融风控的分层阈值分析，重点围绕“分布与阈值 cohort（高/低于业务阈值、四分位分桶、结构占比）”展开。请直接读取数据后，围绕 Status（是否违约）、loan_amount、LTV、Credit_Score、income、rate_of_interest、Interest_rate_spread、Upfront_charges、term、dtir1、property_value、year、Region、loan_type、loan_purpose、Gender、age、loan_limit、approv_in_adv、Credit_Worthiness、business_or_commercial、construction_type、occupancy_type、credit_type 等字段，回答以下分析目标：1）识别违约率在关键阈值两侧的变化（例如 LTV、Credit_Score、income、DTI、贷款金额）；2）按四分位/分桶比较违约率、样本占比和贷款金额占比；3）找出高风险与低风险 cohort 的结构差异（地区、贷款类型、用途、性别、年龄、审批方式、信用资质等）；4）检查缺失值是否在高风险 cohort 中更集中；5）输出可给管理层直接使用的阈值洞察和建议。请将结果整理成 analysis_summary.json，并确保所有结论都能追溯到可复算的 pandas 统计口径。
```

### 738. D11_k983049_zh (domain=D11, difficulty=7)

```
请基于文件 yasserh__loan-default-dataset__Loan_Default.csv 做一份面向管理层的贷款违约驱动分析，重点放在“数值变量之间的相关性与共同驱动因素”上。请先围绕 loan_amount、rate_of_interest、Interest_rate_spread、Upfront_charges、term、property_value、income、Credit_Score、LTV、dtir1（如有）以及 Status 做系统分析：1）先识别这些数值字段之间最强的正/负相关关系，并给出按相关系数绝对值排序的 Top 关联；2）分析违约 Status=1 与各数值字段的关系，比较违约/不违约组的均值、中位数和样本量；3）按 loan_type、loan_purpose、credit_type、Region 分组，查看这些分组下的关键数值指标均值和违约率差异；4）检查缺失值是否集中在某些关键数值字段，并判断这些缺失是否与违约状态有关；5）找出高风险组合（例如高 LTV、低 Credit_Score、高 rate_of_interest、低 income 等）的样本占比及违约率；6）输出一份可直接给业务团队的结论摘要，说明哪些数值因素最像违约的核心驱动、哪些更像伴随变量。请注意：结果必须严格基于数据本身，不要臆测；所有相关系数请四舍五入到 2 位小数。
```

### 739. D11_k983113_zh (domain=D11, difficulty=7)

```
请基于文件 yasserh__loan-default-dataset__Loan_Default.csv 做一份面向风控/信贷运营的复杂分析，重点围绕“排名与集中度”来展开：先找出哪些贷款分组最集中、哪些特征的违约/非违约占比最偏斜，再评估头部客户群、头部产品与头部区域是否贡献了大部分贷款金额或违约事件。请直接使用表中的真实字段（例如 year、loan_type、loan_purpose、Gender、age、credit_type、Region、Status、loan_amount、income、Credit_Score、LTV、rate_of_interest、Interest_rate_spread、property_value、Upfront_charges 等），不要改写数据。希望输出适合给管理层看的结论，并给出可落地的优先级排序。

请把分析拆成 4-6 个彼此独立的轨道，至少包括：
1）按贷款金额/违约数的 Top-N 排名与集中度（含 Pareto/前20%贡献）。
2）按客户属性与产品属性的分层集中度（如 loan_type、loan_purpose、Region、age、Gender、credit_type）。
3）违约状态下的高风险集中群体识别（哪些组合占了最多违约）。
4）金额、收入、LTV、信用分之间的集中与偏斜检查（例如头部区间占比、分位数对比）。
5）按年份或其他时间维度检查集中度是否变化。
6）最后给出一个管理层摘要：最该优先关注的 3 个集中点及原因。
```

### 740. D11_k983126_zh (domain=D11, difficulty=7)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向信贷风控与产品分析的多维诊断，重点围绕“数值变量之间的相关性与驱动因素”展开。先识别哪些数值字段彼此联动最强（请输出四舍五入到 2 位小数的相关系数），再区分不同贷款目的（purpose）与违约标签（not.fully.paid）下的差异，最后总结最值得业务关注的风险信号。请围绕 credit.policy、int.rate、installment、log.annual.inc、dti、fico、days.with.cr.line、revol.bal、revol.util、inq.last.6mths、delinq.2yrs、pub.rec、not.fully.paid 这些字段做分析，输出可落地的结论、关键排序、分组对比和异常样本特征。数据是固定真实数据，不能改值，结论要尽量具体。
```

### 741. D11_k983666_zh (domain=D11, difficulty=7)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向信贷业务的综合分析，重点围绕“排名与集中度”展开：先找出贷款申请中最常见的用途、最主要的高风险/低风险群体，以及哪些变量对违约最有解释力；再分析总量是否高度集中在少数分组中（例如 top-N 用途、fico 分段、信用政策分组等），看看是否存在明显的 Pareto 现象。请结合这些字段：credit.policy, purpose, int.rate, installment, log.annual.inc, dti, fico, days.with.cr.line, revol.bal, revol.util, inq.last.6mths, delinq.2yrs, pub.rec, not.fully.paid。输出应适合给忙碌的业务负责人快速决策，分成 4-6 个相互独立的分析轨道，并给出可落地的结论要点。
```

### 742. D11_k983824_zh (domain=D11, difficulty=7)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向信贷风控的异常与离群分析报告，重点围绕“显式数值规则下的异常识别”来展开。请先读入数据并围绕以下字段开展分析：credit.policy、purpose、int.rate、installment、log.annual.inc、dti、fico、days.with.cr.line、revol.bal、revol.util、inq.last.6mths、delinq.2yrs、pub.rec、not.fully.paid。我要你重点找出：1）按 IQR/分位数/业务阈值定义的数值异常样本；2）罕见 purpose 类别及其风险特征；3）高利率、高负债、高信用查询、低 FICO、超高 revolving utilization 等极端组合；4）违约标签 not.fully.paid 在异常群体中的集中度；5）credit.policy=0 与 1 在异常规则下的差异；6）输出可直接给风控团队使用的可执行结论。请把结果整理成一个可读的摘要，并尽量给出可以复核的统计口径。
```

### 743. D11_k983917_zh (domain=D11, difficulty=7)

```
请基于文件 yasserh__loan-default-dataset__Loan_Default.csv 做一份面向金融风控/贷款审批的相关性与驱动因素分析，重点回答“哪些数值字段彼此一起变化、哪些变量与违约/Status 最相关、以及这些关系在不同分组下是否稳定”。请直接使用现有列名（如 loan_amount、rate_of_interest、Interest_rate_spread、Upfront_charges、term、property_value、income、Credit_Score、LTV、Status、year、Region、Security_Type、Gender、loan_type、loan_purpose、occupancy_type、credit_type、age 等），不要改名或臆造字段。请把分析拆成多个独立轨道，分别覆盖：1）数值字段相关性总览与最强正/负相关对；2）与 Status 的相关/驱动因素排序；3）按贷款类型或用途分组后的相关结构差异；4）按 Region 或 Security_Type 分组的违约率与关键数值指标差异；5）缺失值与相关性/驱动分析的影响；6）对几个最关键变量做交叉验证式的描述性检查（例如高 LTV/低 Credit_Score/高 interest rate 是否对应更高 Status）。
```

### 744. D11_k983967_zh (domain=D11, difficulty=7)

```
请基于文件 yasserh__loan-default-dataset__Loan_Default.csv（直接读取 df = pd.read_csv('inputs/yasserh__loan-default-dataset__Loan_Default.csv')）做一份面向金融风控与业务投放的多部分分析报告，重点围绕“排名与集中度”展开：识别哪些分组在放款量、违约量、贷款金额、LTV、收入等维度上最集中，Top-N 群组是否贡献了大部分总量，是否存在明显的帕累托特征，并比较这些高集中群组的风险表现。请结合真实列名进行分析，包括但不限于 Status、loan_type、loan_purpose、loan_limit、Gender、age、Region、credit_type、loan_amount、property_value、income、LTV、Credit_Score、rate_of_interest、Interest_rate_spread、Upfront_charges、term、dtir1、year、Security_Type。输出一份可直接给管理层和风控团队看的结构化结果，要求分解为 4-6 个彼此独立的分析轨道：1）放款/样本量的 Top-N 集中度；2）违约样本与违约率的 Top-N 集中度；3）贷款金额与房产价值的集中度；4）按地区/贷款类型/目的的集中度对比；5）高集中组与低集中组的风险画像差异；6）必要时补充缺失值和关键指标分布概览。最终请生成 analysis_summary.json。
```

### 745. D11_k983974_zh (domain=D11, difficulty=7)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向金融分析的综合报告，重点围绕“排名与集中度”展开：先找出各贷款用途（purpose）在样本中的频次排名、头部用途对总量的集中占比（例如 Top 3 / Top 5 / Pareto 20%）以及是否存在明显的长尾；再按信用表现和风险信号拆分，比较不同组别在逾期、公开记录、最近 6 个月查询次数等维度上的集中情况；同时结合利率、FICO、收入、负债比（dti）等字段，分析高风险样本是否更集中于某些用途或某些分位段。请输出一份可直接交付给业务方的结论摘要，最好能回答：哪些用途最集中、风险最集中在哪里、头部群体是否贡献了大部分风险样本，以及这些集中现象是否和信用分、利率水平一致。数据文件中的真实列包括 credit.policy、purpose、int.rate、installment、log.annual.inc、dti、fico、days.with.cr.line、revol.bal、revol.util、inq.last.6mths、delinq.2yrs、pub.rec、not.fully.paid。
```

### 746. D11_k984263_zh (domain=D11, difficulty=7)

```
请基于文件 yasserh__loan-default-dataset__Loan_Default.csv 做一份面向金融风控的多部分分析，重点围绕 year 的时间趋势以及按时间序列变化的违约表现、定价变化和风险分层展开。请结合真实字段（如 year、Status、rate_of_interest、Interest_rate_spread、Upfront_charges、loan_amount、property_value、income、LTV、Credit_Score、loan_type、loan_purpose、Gender、Region、Security_Type、occupancy_type、loan_limit、age、submission_of_application 等）输出一份可直接给业务看的分析摘要。我要的不是简单描述，而是能支持决策的结论：1）按 year 看违约率是否有明显上升/下降及其环比变化；2）按 year 看贷款定价相关指标（rate_of_interest、Interest_rate_spread、Upfront_charges）的趋势和异常年份；3）比较不同 loan_type / loan_purpose 在各年份的违约率变化，找出风险恶化最快的分组；4）分析 Credit_Score、LTV、income、loan_amount 等核心风控变量在时间上的变化以及它们与 Status 的关联；5）按 Region、Security_Type、occupancy_type 做时间切片，识别哪些区域或资产类型在某些年份风险抬头；6）最后汇总成一份结构化结论，说明哪些趋势最值得持续监控。
```

### 747. D11_k984575_zh (domain=D11, difficulty=7)

```
请基于文件 yasserh__loan-default-dataset__Loan_Default.csv 做一份面向金融风控分析的多部分深度分析，重点围绕“数值变量之间的相关性与驱动因素”展开，要求识别哪些数值字段会一起变化、哪些变量对 Status（是否违约）最相关，并结合分组视角给出可执行解读。请务必使用数据中的真实列名（例如 loan_amount、rate_of_interest、Interest_rate_spread、Upfront_charges、term、property_value、income、Credit_Score、LTV、dtir1、Status 等），不要改动任何值。希望最终输出一份可交付给业务团队的简洁总结，并把关键发现组织成 analysis_summary.json。

请拆成 4-6 个彼此独立的分析轨道并并行推进：
1) 数值字段相关性矩阵与 Top 正/负相关对：找出最强的数值相关关系，按绝对值排序，给出保留两位小数的相关系数。
2) 违约驱动因素分析：比较 Status=1 与 Status=0 在核心数值字段（loan_amount、rate_of_interest、Interest_rate_spread、Upfront_charges、term、property_value、income、Credit_Score、LTV、dtir1）上的均值/中位数差异，并找出差异最大的指标。
3) 分层关联分析：按 loan_type、loan_purpose、Credit_Worthiness、age、Gender 等类别分组，比较违约率及关键数值均值，识别高风险组合。
4) 缺失值与字段稳定性检查：统计关键数值字段缺失率，判断哪些字段在样本中最不稳定，并确认这是否影响相关性解释。
5) 业务可解释性校验：检查 LTV、property_value、loan_amount、income、dtir1 之间的方向关系是否符合风控常识，并总结异常点。
6) 输出可操作建议：基于相关性和分层结果，提出 3-5 条风控或审批流程建议，强调哪些变量应优先纳入人工复核或规则阈值。

请注意：所有结论都必须严格基于该 CSV 的实际数据，数字需四舍五入到 2 位小数，且不要编造任何字段或结果。
```

### 748. D11_k984593_zh (domain=D11, difficulty=7)

```
请基于文件 yasserh__loan-default-dataset__Loan_Default.csv 做一份面向金融风控/贷款审批的分群分析，重点看不同类别分组之间的指标差异、均值差距和违约率差距。请围绕这些真实字段展开：Status、Region、Security_Type、Gender、loan_type、loan_purpose、Credit_Worthiness、approv_in_adv、loan_limit、credit_type、co-applicant_credit_type、age、loan_amount、rate_of_interest、Interest_rate_spread、Upfront_charges、term、property_value、income、Credit_Score、LTV、dtir1。我要你输出可直接给管理层看的结论，并尽量找出“哪个分组最好/最差、差距最大在哪里、哪些组合风险最高”。分析至少拆成 4-6 个彼此独立的子任务，便于并行处理：1）按 Region / Security_Type / loan_type 的违约率对比；2）按 Gender / age / co-applicant_credit_type 的利率、LTV、违约率对比；3）按 loan_purpose / approv_in_adv / loan_limit 的费用和期限差异；4）按 Credit_Worthiness / credit_type / Credit_Score 分段看风险与贷款条件差异；5）找出关键数值指标在各组间最大的均值差距；6）补充缺失值模式是否在不同违约状态或分组中集中出现。请用简体中文输出。
```

### 749. D11_k984757_en (domain=D11, difficulty=7)

```
Using yasserh__loan-default-dataset__Loan_Default.csv, run a finance analytics deep-dive focused mainly on correlation and driver analysis across the numeric fields. I need you to identify which numeric variables move together, highlight the strongest positive and negative relationships, and explain where default risk appears to concentrate using the real columns such as loan_amount, rate_of_interest, Interest_rate_spread, Upfront_charges, term, property_value, income, Credit_Score, LTV, dtir1, and Status. Please break the work into independent tracks so different analysts can work in parallel: overall numeric correlation structure; default-vs-nondefault driver comparison; segmenting correlations by key business slices like loan_type and loan_purpose; missingness and data-quality checks for numeric drivers; and a compact executive summary of the top associations worth monitoring.
```

### 750. D11_k984824_zh (domain=D11, difficulty=7)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向金融风控/信贷分析的分群对比报告，重点看不同类别之间的利率、收入、负债、FICO、逾期等指标均值/中位数差异，以及哪些细分群体之间的差距最大。请结合真实列名（credit.policy、purpose、int.rate、installment、log.annual.inc、dti、fico、days.with.cr.line、revol.bal、revol.util、inq.last.6mths、delinq.2yrs、pub.rec、not.fully.paid）完成分析，并把结论整理成可直接交付的结果。除了主线“按类别分组比较”外，也请顺带看：1）credit.policy 与是否未还清的差异；2）purpose 之间的风险/成本对比；3）FICO 分段后的表现；4）高查询/高负债/高循环利用率人群的组合差异；5）关键变量之间的相关性与异常分层。请输出一份简洁但完整的分析结果，便于我向业务方汇报。
```

### 751. D11_k984953_zh (domain=D11, difficulty=7)

```
请基于文件 yasserh__loan-default-dataset__Loan_Default.csv 做一份面向风控/信贷分析的多维诊断，重点围绕“相关性与驱动因素分析”：哪些数值字段彼此联动、它们与违约 Status 的关联强弱、以及按业务分组后这种关系是否稳定。请把结果整理成可交付的 analysis_summary.json。分析时请直接使用现有字段（例如 loan_amount、rate_of_interest、Interest_rate_spread、Upfront_charges、term、property_value、income、Credit_Score、LTV、dtir1、Status，以及 Region、loan_type、loan_purpose、loan_limit、Gender、age、credit_type、occupancy_type、Security_Type 等），不要臆造字段或改写数据。希望输出的结论能回答：1）哪些数值变量的相关性最强；2）与违约最相关的数值驱动因素有哪些；3）这些关系在不同 Region / loan_type / loan_purpose 下是否一致；4）缺失值是否集中在某些关键驱动变量上；5）是否存在明显的高相关变量对，可能意味着冗余或共线性风险；6）给出可供后续建模或策略分层使用的简明结论。
```

### 752. D11_k985257_zh (domain=D11, difficulty=7)

```
请基于文件 sanaijlalshahrukh__gold-price-analysis-10-year-historical-data__gold_historical_data.csv 做一份面向财务分析的黄金价格时序分析，重点围绕 Date 维度上的趋势、涨跌节奏和阶段性变化来展开。请先确认各字段含义并用 Close/Adj Close 作为核心价格序列，结合 Open、High、Low、Volume 做交叉验证。我要你把分析拆成几条可以并行推进的子任务：例如按年/月/季度的价格趋势、日度涨跌幅与极端波动、不同年份的涨跌节奏比较、成交量与价格变化的关系、历史高低点与阶段性拐点识别、以及收盘价与其他价格字段的一致性检查。最后给我一个可直接汇报的结构化总结，突出关键时间段、变化幅度、频率和异常点，并尽量用可复核的统计结果支撑结论。
```

### 753. D12_g114_en (domain=D12, difficulty=7)

```
I need you to analyze the five source files in `inputs/` – `employees.xlsx`, `onboarding_cases.xlsx`, `interview_scorecards.csv`, `skills_matrix.xlsx`, and `performance_calibration.xlsx` – and put together a compact synthesis brief in markdown plus a small evidence table. Cover interview scorecards, onboarding completion, skills gaps, performance calibration, and cross-source reconciliation. Keep it executive-friendly.
```

### 754. D12_g151_zh (domain=D12, difficulty=7)

```
基于以下输入文件完成一轮跨源盘点，输出2-3份紧凑报告（JSON/CSV/MD均可），每份不超过60行，只包含聚合摘要，不得输出逐行明细：

- inputs/employees.csv
- inputs/candidates.csv
- inputs/interview_scorecards.xlsx
- inputs/performance_calibration.xlsx
- inputs/skills_matrix.csv
- inputs/onboarding_gaps.xlsx
- inputs/training_completion_log.csv
- inputs/people_training_enablement.db

覆盖以下检查项（按我们的标准定义处理）：
1) 录用匹配率（仅hired记录，linked_employee_id非空视为匹配）
2) 面试评分风险（重复键定义、低分标准、风险占比）
3) 绩效校准偏移（calibrated_rating vs rating的绝对差，平均差、P90、差异记录数）
4) 技能缺口（gap = target - current，统计gap≥2条目及平均gap最高技能）
5) 入职逾期（逾期定义：status属于late/pending/blocked或completed_date晚于due_date；输出逾期率、blocked数、late数）
6) 培训完成率（complete率、缺失employee_id数、blocked数）
7) 培训负荷（按department汇总hours，输出总工时最高部门及其工时）

引用ID时最多5个，并标注问题类型。建议并行处理招聘/面试、绩效/技能、入职/培训三个子域再汇总。
```

### 755. D12_g322_en (domain=D12, difficulty=7)

```
I need you to produce a decision brief from our people analytics data. Here's what I'm looking for:

- **Hire interview-performance gap**: Using hires.csv, interview_scorecards.csv, and performance_calibration.xlsx, figure out how many hired candidates have interview scores and performance ratings, highlight discrepancies, and flag the biggest mismatches.
- **Skills vs onboarding completion**: From skills_matrix.csv and onboarding_gaps.csv, find employees who are highly skilled but behind on onboarding, and compare performance ratings of those who finished all tasks vs. those who didn't.
- **Performance vs critical skills**: From performance_calibration.xlsx and skills_matrix.csv, identify high performers who are weak or missing entirely in a critical skill (skill S01).
- **Synthesize all three into a single `recommendation.json`** with a ranked list of training/resource options (2–3), supporting numbers from the analyses, and a dictionary of flagged employee IDs (incomplete onboarding, critical skill gaps, interview‑performance mismatches). Apply standard data cleaning (drop missing/out‑of‑range records, deduplicate sensibly) as you go.
```

### 756. D12_g32_en (domain=D12, difficulty=7)

```
Use the four files in OUT_DIR/inputs/ (recruiting_interview_scorecards.xlsx, employee_skills_matrix.csv, onboarding_checklist.xlsx, calibration_feedback_big.xlsx) to produce a JSON reconciliation summary, a CSV aggregate table, and a Markdown executive summary in OUT_DIR/reports/. Synthesize across the files to reconcile hiring/interview quality with onboarding and skills outcomes.
```

### 757. D12_g340_zh (domain=D12, difficulty=7)

```
请根据 inputs/employees.xlsx、inputs/training_completions.xlsx、inputs/performance_calibration.csv、inputs/skills_matrix.xlsx 做一份跨源分析，输出 2-3 个紧凑的汇总报告（CSV/JSON/MD 组合），给 HRBP、L&D 和用人经理看。重点分析关键培训完成缺口、绩效校准偏差以及数据异常记录。只要汇总级结果，不要逐行明细。
```

### 758. D12_g398_en (domain=D12, difficulty=7)

```
I need you to put together a short research brief from the People/Training & Enablement data in inputs/employees.csv, ats_candidates.xlsx, interview_scorecards.csv, onboarding_training.xlsx, performance_calibration.xlsx, skills_matrix.xlsx, source_notes.md, and people_enablement.db. The goal is a concise findings.md with sections on ATS-HRIS linkage, interview scorecard integrity, onboarding coverage, and calibration/skills gaps, plus a cross-source reconciliation section. Also produce a compact evidence_summary.json with the key metrics (match rates, orphan rows, conflicting recommendations, completion rates, gap counts, etc.) and a few flagged IDs. Keep everything aggregate, no row-level joins. Reconcile any inconsistencies across sources.
```

### 759. D12_g421_en (domain=D12, difficulty=7)

```
We need to reconcile data across our hiring, performance calibration, and skills records. I’ve placed four files in inputs/: employees.csv, interview_scorecards.csv, performance_calibration.xlsx, and skills_matrix.csv. Please produce a concise research brief in markdown and a small evidence table that highlights key findings, including deduplicated counts, offer and hire rates, calibration conflicts, onboarding status, skill gaps, and top mismatch reasons. Focus on cross-source anomalies and flag any problematic IDs. Keep it compact – no row-by-row dump.
```

### 760. D12_g425_zh (domain=D12, difficulty=7)

```
基于 inputs/ 下的 interview_scorecards.csv、performance_calibration.csv、skills_matrix.xlsx、onboarding_modules.xlsx、onboarding_activity_log.csv 和 metadata.json，做一次跨来源的人才与赋能诊断，重点看面试评分质量、绩效校准偏差、技能缺口和入职推进健康度。输出 2–3 个紧凑的汇总文件（CSV/JSON/MD），只包含聚合指标和少量异常线索 ID，不要逐行明细。
```

### 761. D12_g445_zh (domain=D12, difficulty=7)

```
我需要你基于 inputs/recruiting_interviews.csv、inputs/performance_reviews.xlsx、inputs/skills_matrix.xlsx 和 inputs/onboarding_tracker.xlsx 做一份人事与培训启用（People / Training & Enablement）的决策简报，最后只输出一个文件：decision_brief.md。请把它写成能直接给 HRBP、TA、L&D 和用人经理看的内部简报，核心是帮我决定下一季度优先把资源投到哪里：招聘面试官校准、绩效校准、技能矩阵补强，还是入职培训优化。

我希望你按我下面这套口径来做，口径请严格一致：招聘分析里，面试评分只看 score_1_5 不为空的记录，同一个 hire_id + stage 只算一次，重复记录保留 interview_date 更早的那条；面试质量看两个东西，一是各 interviewer_id 的平均分与全体平均分的偏差，二是每个 stage 的 Strong Yes 占比。绩效校准里，比较 manager_rating_1_5 和 committee_rating_1_5 的绝对差，差值 >= 0.7 记为显著分歧，同一 employee_id + cycle 如有重复，保留 committee_rating_1_5 非空且最新的一条；如果 committee_rating_1_5 为空，这条只用于计数，不用于差值均值。技能矩阵里，以 role_family 为单位，对每个 skill_name 计算熟练度 < 3.0 的缺口率，一个员工在同一 skill_name 的重复行保留 proficiency_1_5 更高的一条；我只关心 closed set 里的 10 个技能名称。入职分析里，completion time 定义为 end_date 减 start_date 的自然日天数，start_date 当天算 0 天，只统计 status = Complete 且 end_date 不为空的任务；如果 end_date 早于 start_date，视为数据异常，单独计入异常数但不纳入时长分布。

请在简报里给我一份清晰的优先级建议，必须说明推荐顺序、每项优先级背后的数字依据，以及我应该先做什么、后做什么。我还希望你在文中明确写出：面试、绩效、技能、入职四条线各自最关键的发现；再加一个很短的 cross-source 对照，说明招聘、绩效、技能和入职这四个来源对同一批员工的总体对齐情况，但不要做逐行映射表，只要汇总比例、未匹配数量和前 3 类差异原因就行。文风请像一个非常仔细的分析师写给管理层的简报：具体、简洁、但把定义说清楚。
```

### 762. D12_g461_en (domain=D12, difficulty=7)

```
I need a compact cross-source people report because we’re trying to tighten hiring quality, performance calibration, and onboarding. Please review the files inputs/ats_candidates.xlsx, inputs/interview_scorecards.csv, inputs/employee_performance.csv, inputs/skills_matrix.xlsx, and inputs/onboarding_training.xlsx and give me one brief with the main findings plus a small evidence table. Use the date window from 2024-01-01 through 2024-12-31 inclusive.

For matching hires to candidates, count a hire as matched only when employee_performance.csv has exactly one candidate_id that appears in ats_candidates.xlsx; if the same employee or candidate shows up more than once, treat that as a reconciliation problem and count it separately. For interview scorecards, only use rows where scorecard_completed = Y and overall_score is present; use the 1-5 competency fields as-is, and flag any score outside 1-5 as an anomaly. For calibration, use performance_rating and calibrated_rating; treat a difference of 0.5 or more as material. For skills gaps, use gap = required_level - current_level and flag any negative gap as an overqualified/mismatched entry. For onboarding, completion is on-time only if completed_date is on or before due_date; if completed_date is blank, count it as incomplete. Please summarize the big counts, match rates, top mismatch reasons, and a few flagged IDs, but do not give me a row-by-row dump.
```

### 763. D12_g566_zh (domain=D12, difficulty=7)

```
我这边要做一份 People / Training & Enablement 的跨源分析简报，请基于 inputs/employees.xlsx、inputs/skills_matrix.xlsx、inputs/onboarding_gaps.xlsx、inputs/candidates_interviews.xlsx、inputs/interview_scorecards.xlsx、inputs/hiring_reconciliation.xlsx 和 inputs/performance_calibration.xlsx 产出 1) 一份 findings.md，2) 一份小的 evidence_table.csv。

我关心的是四条主线：第一，招聘面试与打分卡质量，重点看面试覆盖率、打分卡提交率、带 bias_flag 的记录占比，以及按 stage 汇总后的主要问题类型；第二，招聘到入职的跨源对账，重点看候选人和 hire 之间的匹配率、无法匹配的 hire 数量、以及前 3 个不一致原因；第三，技能矩阵和岗位要求的差距，重点看每个职能/层级的关键技能达标率、低于 target_proficiency 的人数和最常见短板；第四，入职和绩效校准是否存在同一批员工的系统性问题，重点看 onboarding 30 天缺口、经理 check-in 缺失、以及 Q1/Q2 校准调整率。

请把所有比率统一保留到小数点后 1 位，百分比按 100% 制；计数直接给整数。时间口径我固定如下：面试覆盖率按 candidates_interviews.xlsx 里有至少 1 条 interview 记录的 candidate_id / 候选人总数计算；打分卡提交率按 interview 记录中 scorecard_submitted = Y 的条数 / 全部 interview 条数计算；跨源匹配只允许 exact candidate_id 等值匹配，不允许模糊匹配，若 hiring_reconciliation.xlsx 里的 candidate_id 在 candidates_interviews.xlsx 中不存在就算 unmatched；onboarding 的 30 天缺口定义为 completed_modules < required_modules，且 first_30d_manager_checkin_done = N 也算一个单独缺口原因，二者可同时计入同一员工；校准调整率按 calibration_outcome = Adjusted 的记录数 / 该季度全部 calibration 记录数算。所有汇总都只要 compact aggregate，不要逐行明细表。
```

### 764. D12_g575_zh (domain=D12, difficulty=7)

```
请帮我基于这 5 个输入文件做一份面向 HR / People Ops 的综合复盘：`employees_hires.xlsx`、`performance_calibration.csv`、`skills_matrix.xlsx`、`onboarding_training.xlsx`、`interview_scorecards.xlsx`。我需要输出 3 个文件，分别是 `summary_metrics.json`、`flagged_ids.csv`、`exec_brief.md`。其中 `summary_metrics.json` 要是紧凑的汇总结构，只放关键聚合指标，不要展开到逐人逐题的明细；`flagged_ids.csv` 只保留少量需要跟进的员工或候选人 ID；`exec_brief.md` 写给管理层看，要求是短报告，能直接读。

我关心的是跨来源的一致性和缺口，不是单表统计。请把员工花名册、绩效校准、技能矩阵、入职培训、面试评分卡串起来看，但最终呈现必须是汇总级别：比如匹配率、未匹配数量、Top 不一致原因、逾期率、技能缺口率、阶段平均分、以及少量被标记的 ID。不要输出任何逐行 employee->candidate 或 employee->skill 的全量映射表。

指标口径我先说清楚：员工主键以 `employees_hires.xlsx` 里的 `employee_id` 为准，唯一性按这个字段去重；`performance_calibration.csv` 如果同一个 `employee_id + quarter` 出现多行，按文件中最后出现的那一行作为最终记录；`skills_matrix.xlsx` 如果同一个 `employee_id + skill` 重复，也按最后出现的那一行；`interview_scorecards.xlsx` 如果同一个 `candidate_id + dimension` 重复，也按最后出现的那一行。培训逾期只在 `due_date` 和 `completion_date` 都不为空时计算，逾期天数 = `completion_date - due_date` 的自然日天数；`status` 为 `Completed` 或 `Completed Late` 才算完成；其余状态都视为未完成。

我希望你把结果压缩成几个我能直接拿去开会的结论：1）按员工层面统计：入职培训 7 个模块的完成覆盖率、培训逾期率、至少有一个严重缺口的员工数、以及 2024Q2 绩效校准均分达到 3.8 以上的员工占比；2）按技能层面统计：当前熟练度低于目标熟练度的技能缺口率，以及缺口数 Top 3 的技能名称和数量；3）按招聘侧统计：`interview_scorecards.xlsx` 中被标记为 `Hired` 的候选人里，有多少能在候选人集合中被匹配到、匹配率是多少、未匹配数量是多少；4）按面试阶段统计：`Screen`、`Hiring Manager`、`Panel`、`Offer` 四个阶段的平均分，找出平均分最高的阶段；5）给我一个简短的风险清单，只列少量需要跟进的 ID，最多 10 个，优先放严重培训缺口或绩效/技能组合风险的人。

请把所有比例统一保留到小数点后 4 位，均分保留到小数点后 2 位，数量用整数。如果你需要写出一个总体结论，我更想看到像“培训覆盖率偏低/技能缺口集中在某些技能/招聘评分在某一阶段更强”这种汇总判断。另外，任何时间范围都按自然日口径，不用业务日；日期边界按整天包含。
```

### 765. D12_g57_zh (domain=D12, difficulty=7)

```
我们需要全面了解当前的人才状况，为后续招聘和培训决策提供依据。请基于输入目录中的人才、技能、面试、绩效和 onboarding 数据，做一份紧凑的综合分析，重点说明人才结构、跨源数据之间的差异和潜在风险，并解释关键指标的计算口径。
```

### 766. D12_g622_zh (domain=D12, difficulty=7)

```
请帮我把这四份数据做成一份可直接给业务负责人的决策简报：employees.csv、interview_scorecards.xlsx、performance_calibration.xlsx、training_activity.sqlite。

我想看的是“当前人才供给是否健康、哪里最需要先补救”。请输出一份简短的决策文件，最好能直接拿去开会。
- 先做一版跨源汇总：员工、面试、绩效校准、培训进度之间有哪些关键不一致；所有跨源对齐都只要汇总结果，不要逐行明细。
- 面试分数按 1-5 分看，超过 5 或低于 1 的记为无效；缺失 interviewer 也单独计数。入职候选人匹配率按在职员工里是否能找到 ATS candidate_id 来算。
- 绩效校准看 manager_initial_rating 和 calibrated_rating 的差值，差值绝对值 >= 2 算“大偏差”；如果 calibrated_rating 缺失，单独计数。培训 SLA 里，mandatory 模块只看 completed_date 不为空的已完成项，逾期定义为 completed_date > due_date；on-time rate = (已完成强制培训 - 逾期强制培训) / 已完成强制培训。
- 我希望你用“先修哪个问题最能改善整体质量”的思路给出排序，最好给出一个推荐优先级，并注明支撑这个排序的数字。
- 请额外列出几个最值得追踪的异常员工/候选人 ID，但不要输出完整映射表。

我需要的交付物只有一份简短文件，内容是结论 + 关键数字 + 排名 + 需要关注的例外 ID。
```

### 767. D12_g981014_zh (domain=D12, difficulty=7)

```
请基于 inputs/interviews.xlsx、inputs/performance.xlsx 和 inputs/audit_log.xlsx 做一份综合分析简报，重点看面试评分、绩效校准、技能缺口和入职完成度之间的交叉问题。输出一个 findings.md，里面要有跨源一致性/冲突说明、各部分的关键汇总，以及我需要优先跟进的少数异常编号。
```

### 768. D12_g981461_zh (domain=D12, difficulty=7)

```
请基于 inputs/people_ops_sources.xlsx、inputs/skills_matrix.xlsx 和 inputs/enablement_notes.docx，输出一份 findings.md，重点做候选人、员工、面试评分卡、技能矩阵、入职与绩效校准的交叉分析，给我一页可直接发给管理层的结论摘要，并把需要我盯住的异常点单独列出来。
```

### 769. D12_g982401_zh (domain=D12, difficulty=7)

```
请基于 inputs/people_training_enablement_data.xlsx、inputs/seed_context_notes.docx 和 inputs/anomaly_scope.xlsx 做一份 汇总报告，覆盖面试评分、绩效校准、技能矩阵和入职培训四块内容。我要一个能直接给管理层看的单文件结果，重点是整体匹配率、缺口率、逾期率、前几类不一致原因，以及少量需要跟进的ID。
```

### 770. D12_k982968_zh (domain=D12, difficulty=7)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向 HR 的离职风险分析，重点围绕“时间/序列趋势”来展开。由于数据里没有真实日期，请把 TotalWorkingYears、YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager 视为员工职业序列上的时间/阶段变量，重点分析这些阶段变量的变化与 Attrition 的关系，并补充对 OverTime、JobLevel、MonthlyIncome、JobSatisfaction 等因素的趋势性解读。请把分析拆成多个相互独立的部分，方便并行推进：先做整体离职率在不同职业阶段的变化，再看关键人群分组的阶段趋势差异，然后分析晋升/任职时长/管理关系的“滞后效应”，最后把这些趋势转成可执行的人力资源管理建议。需要输出一份可直接给管理层看的结论汇总，强调哪里是离职高风险窗口、哪些因素在不同阶段的影响最明显、以及应优先干预哪些员工群体。
```

### 771. D12_k983115_en (domain=D12, difficulty=7)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a people/HR analytics readout focused mainly on temporal / trend analysis over the available sequence fields. I want you to examine how attrition risk, workforce composition, and employee experience change across tenure-related measures such as TotalWorkingYears, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, and YearsWithCurrManager, and connect that with Attrition, BusinessTravel, OverTime, JobRole, Department, MonthlyIncome, JobLevel, and satisfaction scores. Please split the work into a few independent tracks so they can be handled in parallel: one track for tenure-based attrition trends and inflection points, one for promotion/career stagnation patterns over time, one for manager/role tenure effects, one for travel and overtime interactions across tenure bands, and one for compensation/satisfaction drift by tenure. I need a concise summary plus a JSON artifact with the key findings and any notable thresholds or jumps in attrition over the sequence fields.
```

### 772. D12_k983521_zh (domain=D12, difficulty=7)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的离职风险分析，但重点放在“时间/序列趋势”上：把员工的任职阶段、职业发展阶段和组织经验当作时间轴，分析离职率在不同“工龄/晋升/同经理时长”阶段的变化，并找出哪些群体在不同阶段的离职风险上升最快。请同时结合 Attrition、TotalWorkingYears、YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager、TrainingTimesLastYear、MonthlyIncome、JobLevel、BusinessTravel、OverTime、Department、JobRole、MaritalStatus 等字段，输出可以直接给 HR 负责人看的结论和可执行建议。你需要把分析拆成几个互相独立的轨道，适合分给 4-6 个子分析员并行完成。最后请给出一份简洁的分析摘要，并把关键统计结果整理成结构化结论。相关问题请逐项回答。
```

### 773. D12_k983619_zh (domain=D12, difficulty=7)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的 HR 分析，重点围绕“时间/序列趋势”来讲清楚员工流失的变化规律。这个数据没有显式日期列，所以请把 EmployeeNumber 视为录入/入职序列的近似时间顺序，按 EmployeeNumber 升序切成 4 个等频阶段（或按自然顺序分段），分析不同阶段的 Attrition 变化、关键人群的变化，以及哪些组织/岗位/个人特征在阶段之间的波动最明显。请同时结合 Age、JobLevel、MonthlyIncome、OverTime、BusinessTravel、Department、JobRole、YearsAtCompany、YearsSinceLastPromotion、TotalWorkingYears、DistanceFromHome、EnvironmentSatisfaction、JobSatisfaction、WorkLifeBalance、StockOptionLevel 等字段，输出一份可执行的结论摘要和优先级建议。需要拆成多个独立分析轨道，方便并行处理：例如总体流失趋势、按部门/岗位趋势、加班与差旅趋势、薪酬与晋升停滞趋势、生命周期/任期趋势、满意度与工作生活平衡趋势。
```

### 774. D12_k983800_zh (domain=D12, difficulty=7)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的员工流失分析，重点围绕“分布与阈值分层”来展开：把员工按年龄、通勤距离、月收入、总工龄、加薪幅度、在岗年限等维度切成阈值 cohorts/分位数组，比较各组的流失率、人数占比、以及关键人群的构成差异。请结合真实字段（如 Attrition, Age, DistanceFromHome, MonthlyIncome, TotalWorkingYears, PercentSalaryHike, YearsAtCompany, YearsInCurrentRole, OverTime, JobLevel, JobRole, Department, BusinessTravel, MaritalStatus, StockOptionLevel, JobSatisfaction, EnvironmentSatisfaction, WorkLifeBalance 等）做成可执行的分析方案，并给出能支持人力资源优先级决策的结论。

我希望你把工作拆成多个独立分析轨道，彼此尽量不依赖，便于并行推进：
1) 阈值分层流失画像：围绕年龄、通勤距离、总工龄、在岗年限、月收入等做高/低阈值 cohorts，比较流失率和样本占比；
2) 分位数桶分析：对收入、工龄、加薪幅度、近年任职年限等做四分位/五分位桶，观察流失率是否单调变化；
3) 人群混合结构：看 OverTime、JobRole、Department、MaritalStatus、StockOptionLevel 等组合下的流失构成与占比；
4) 满意度/投入度阈值分析：比较 JobSatisfaction、EnvironmentSatisfaction、WorkLifeBalance、JobInvolvement 低分阈值人群的流失差异；
5) 薪酬与晋升信号分析：按 JobLevel、PercentSalaryHike、YearsSinceLastPromotion、YearsAtCompany 的阈值与分层看流失集中度；
6) 输出管理摘要：提炼最值得优先干预的高风险 cohorts，并给出可量化的规模和流失率。
```

### 775. D12_k983808_en (domain=D12, difficulty=7)

```
Using the file patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv, build an HR analytics readout focused mainly on temporal / trend analysis over the available sequence fields. I need a compact but rigorous investigation of how employee outcomes evolve over tenure: compare attrition and key workforce signals across tenure-related buckets derived from TotalWorkingYears, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, and YearsWithCurrManager, and connect any changes to business travel, overtime, job level, marital status, department, and job role. Please break it into independent workstreams so different analysts could work in parallel, then summarize the most important period-over-period or stage-over-stage shifts, identify where attrition is accelerating or slowing, and call out any tenure segments that look unusually risky or stable.
```

### 776. D12_k983808_zh (domain=D12, difficulty=7)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向人力资源管理层的员工流失分析，重点放在“时间/序列趋势”上：把 YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager、TotalWorkingYears、TrainingTimesLastYear、Age 等视为员工职业阶段和任职序列，分析这些序列指标如何随员工在公司的停留时间变化，以及流失与留任在不同阶段的趋势差异。请同时结合 Attrition、OverTime、BusinessTravel、JobRole、Department、MaritalStatus、JobLevel、MonthlyIncome、JobSatisfaction、EnvironmentSatisfaction、StockOptionLevel、NumCompaniesWorked 等字段，给出可执行的管理结论。请拆成 4-6 个彼此独立的分析轨道：1）按任职年限分组的流失率趋势与关键拐点；2）晋升/轮岗/任职时长的序列滞后与流失关系；3）加班、出差、岗位层级在不同任职阶段的流失趋势；4）不同部门/岗位的流失趋势与阶段性差异；5）满意度、薪酬与流失趋势在任职序列中的联动；6）如果数据支持，再比较首年、入职 1-3 年、3-5 年、5 年以上员工的流失画像变化。输出请面向业务决策，给出清晰图表建议和重点观察结论，但不要编造任何不存在的时间字段。
```

### 777. D12_k983836_zh (domain=D12, difficulty=7)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的人力资源分析，重点围绕“时间/序列变化”的角度展开：不要只看静态分布，而要把员工在公司内的年限、晋升滞后、角色变化、培训次数等视作序列进展来分析，识别离职风险是如何随时间演化的。请结合真实字段（例如 Attrition、TotalWorkingYears、YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager、TrainingTimesLastYear、OverTime、JobRole、Department、BusinessTravel、Age、MonthlyIncome 等）完成一份可执行的分析方案，并输出可落地的结论框架。请把工作拆成 4-6 个彼此独立的分析轨道，便于并行给不同子分析员处理：1）员工生命周期/任期分段下的离职趋势；2）晋升停滞与在岗时间序列对离职的影响；3）不同部门/岗位在年限推进过程中的离职率变化；4）加班、出差、培训等“时间型行为”与离职的联动；5）薪酬/职级随工龄变化的离职差异；6）按年龄或总工龄做滚动/分段对比，找出风险拐点。请最终形成适合汇报给 HR 负责人和业务经理的分析要点、异常点和建议。
```

### 778. D12_k984060_en (domain=D12, difficulty=7)

```
Using patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv, build a people-analytics attrition review centered on trend/sequence analysis across the tenure-related fields. I need a concise executive summary plus evidence-backed breakouts on how attrition changes over employee lifecycle stages and time-in-company proxies. Please use the real columns in this file, especially Attrition, Age, BusinessTravel, Department, DistanceFromHome, Education, EducationField, Gender, JobLevel, JobRole, MonthlyIncome, NumCompaniesWorked, OverTime, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, and YearsWithCurrManager. Please decompose the work into separate tracks so different analysts can work in parallel: one track on attrition by tenure bands and promotion/manager tenure progression, one on age and career-stage trends, one on overtime/travel effects over tenure, one on department/job-role differences, and one on pay/experience interactions. I want period-over-period style comparisons using the sequence-like fields in the dataset (for example years at company, years in role, years since last promotion, years with current manager, and total working years), with clear callouts of where attrition rises or falls as tenure advances.
```

### 779. D12_k984179_zh (domain=D12, difficulty=7)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的员工流失趋势分析，重点围绕“时间/序列变化”来拆解：虽然数据里没有日期列，但可以把 YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager、TotalWorkingYears 视为员工经历的序列阶段，分析不同阶段的流失率、流失前后的变化模式，以及这些阶段与业务旅行、加班、职位层级、满意度之间的联动。请输出可直接汇报的结论，明确指出哪些序列阶段的风险上升最快、哪些人群的变化最明显、以及哪些因素在不同任职阶段最能放大或缓解流失。请把分析拆成几个可并行推进的部分：先做整体流失趋势，再做任职年限分段趋势，再做晋升滞后趋势，再做管理者/岗位停留趋势，最后做关键驱动因素在这些阶段上的交互对比。
```

### 780. D12_k984417_en (domain=D12, difficulty=7)

```
Using the file pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv, run a people-analytics attrition review focused mainly on temporal/trend analysis using the sequence fields we do have (especially YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager, TotalWorkingYears, and TrainingTimesLastYear). I want a multi-part analysis that looks at how attrition risk appears to change across tenure/progression stages, whether promotion/managerial stagnation patterns differ for leavers vs stayers, how recent training intensity relates to those stage-based patterns, and whether those trends vary across key segments like Department, JobRole, BusinessTravel, and OverTime. Please also tie in a compact demographic overlay where useful (Age, Gender, MaritalStatus, JobLevel, MonthlyIncome) and keep the output practical for an HR leadership readout with clear trend takeaways and prioritized actions.
```

### 781. D12_k984731_zh (domain=D12, difficulty=7)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的人力资源分析，重点围绕“分布与阈值分层”来讲清楚员工流失风险：请不要只看整体均值，而是把 Age、MonthlyIncome、TotalWorkingYears、DistanceFromHome、OverTime、JobSatisfaction、EnvironmentSatisfaction、JobLevel、MonthlyIncome、PercentSalaryHike、TrainingTimesLastYear、YearsAtCompany、YearsSinceLastPromotion、YearsWithCurrManager 等字段按业务阈值、分位数分组、上下区间、以及流失/未流失混合占比来拆解，给出哪些人群在阈值附近最值得关注。请同时结合 Attrition、BusinessTravel、Department、JobRole、MaritalStatus、Gender、OverTime 的结构差异，识别高风险 cohort，并总结可以落地的优先干预人群。请按可执行的分析结果输出，便于我直接写进汇报材料。
```

### 782. D12_k984788_zh (domain=D12, difficulty=7)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份人力资源流失分析，重点围绕“时间/序列趋势”来展开：虽然数据里没有明确日期，但可以把员工的年龄、总工作年限、司龄（YearsAtCompany）、当前岗位年限（YearsInCurrentRole）、晋升间隔（YearsSinceLastPromotion）和当前经理年限（YearsWithCurrManager）视为职业生命周期序列，分析这些阶段上的流失变化、流失风险拐点、以及不同人群在职业进程中的变化趋势。请你把结果整理成可给管理层汇报的结论，尤其要回答：流失是否随职业阶段推进而上升/下降、哪些阶段变化最明显、以及哪些人群在时间序列上呈现更高风险。请拆成多个彼此独立的分析轨道，方便并行完成。
```

### 783. D12_k984794_zh (domain=D12, difficulty=7)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份偏 HR 运营视角的员工流失分析，重点围绕“分布与阈值 cohort”展开：不要只看总体比例，而要把员工按明确业务阈值分层，比较各 cohort 的流失率、人数占比、收入/年资/通勤等关键指标差异，并识别最需要优先关注的群体。请特别结合以下字段：Attrition、Age、MonthlyIncome、MonthlyRate、TotalWorkingYears、YearsAtCompany、DistanceFromHome、OverTime、JobLevel、JobRole、BusinessTravel、MaritalStatus、EducationField、JobSatisfaction、EnvironmentSatisfaction、StockOptionLevel、TrainingTimesLastYear、WorkLifeBalance。输出时请按 4-6 个相互独立的分析轨道拆分，便于不同子任务并行推进。每个轨道都要尽量使用阈值分组、分位数分箱、上下区间对比、以及 cohort mix share（占比）来表达结论，并给出可执行的 HR 解读。最后汇总成一份适合管理层阅读的 analysis_summary.json。
```

### 784. D12_k984891_zh (domain=D12, difficulty=7)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的人力资源流失分析，重点围绕“排名与集中度”来展开：找出离职人数/离职率最高的群体、这些高风险群体贡献了多少离职、是否存在明显的 80/20 现象，以及离职风险在不同部门、岗位、加班、差旅、婚姻状态、工龄和薪资层级中的集中情况。请把分析拆成多个可并行的子任务，最后输出可直接给业务汇报使用的结论摘要和关键名单。请务必使用数据中真实字段：Attrition、Department、JobRole、OverTime、BusinessTravel、MaritalStatus、Age、MonthlyIncome、TotalWorkingYears、YearsAtCompany、JobLevel、DistanceFromHome、StockOptionLevel、EnvironmentSatisfaction、JobSatisfaction、WorkLifeBalance、TrainingTimesLastYear 等，并尽量用 top-N、占比、累计占比、帕累托/集中度指标来组织结论。
```

### 785. D12_k984998_zh (domain=D12, difficulty=7)

```
请基于文件 patelprashant__employee-attrition__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向人力资源管理的深度分析，重点围绕“随时间/序列变化的趋势”来解释员工流失风险：虽然数据里没有日期列，但有一组天然的序列字段（如 TotalWorkingYears、YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager、TrainingTimesLastYear），请把它们当作员工职业路径的时间轴，分析不同阶段的变化规律、拐点和风险信号。请同时结合 Attrition、OverTime、JobRole、Department、BusinessTravel、MonthlyIncome、JobLevel、DistanceFromHome、JobSatisfaction、EnvironmentSatisfaction、RelationshipSatisfaction、WorkLifeBalance 等变量，输出可直接给 HR 管理层讨论的结论。

我需要你把任务拆成 4-6 个彼此独立的分析轨道，适合并行给子团队做：
1) 职业生命周期/工龄阶段的流失趋势：按 TotalWorkingYears、YearsAtCompany、YearsInCurrentRole 分层，看流失率如何随“阶段”变化，识别高风险拐点；
2) 晋升与停滞轨迹：围绕 YearsSinceLastPromotion、YearsWithCurrManager、JobLevel 的变化，找出长期未晋升/岗位停滞与流失的关系；
3) 培训与成长投入趋势：分析 TrainingTimesLastYear、JobSatisfaction、EnvironmentSatisfaction、WorkLifeBalance 与流失之间的联动；
4) 工作负荷与通勤压力序列：结合 OverTime、DistanceFromHome、BusinessTravel、MonthlyRate/MonthlyIncome，分析压力暴露对流失的影响；
5) 组织结构差异：按 Department、JobRole、MaritalStatus、Gender 分组，比较上述趋势在不同人群中的差异；
6) 解释型汇总：把最关键的风险画像整理成管理层可读的摘要，优先突出“哪些阶段的员工最容易离开、为什么、应该怎么干预”。

请输出一份结构化的 analysis_summary.json，要求结论尽量量化、可复核，并明确指出哪些结论来自趋势分析，哪些来自分组对比。
```

### 786. D13_g178_zh (domain=D13, difficulty=7)

```
基于附件中的五个文件：`inputs/experiments_assignments.csv`、`inputs/app_events.xlsx`、`inputs/checkout_sessions.csv`、`inputs/data_quality_flags.csv` 和 `inputs/metadata.md`，请完成实验 `exp_checkout_v3` 的读数分析。时间窗口为 **2024-05-01 00:00:00 至 2024-05-24 23:59:59**，仅关注 `control` 和 `treatment` 两个变体。按我们的标准去重逻辑处理各表：assignment 表去除完全重复行，同一 user_id+experiment_id 出现多个 variant 时保留 assigned_at 最晚的一条；event 和 session 表先去除完全重复行再统计。会话漏斗以会话为单位，步骤顺序为 `session_start → first_product_view_at → first_add_to_cart_at → checkout_start_at → payment_submit_at → payment_success_at`，某步时间非空即视为到达。会话的实验归属优先使用 assignment 表的最终分组，若无则使用会话表自身的 variant。数据质量问题需整合主表异常（重复、未来日期、冲突）和 `data_quality_flags.csv` 中的 issue_type，但每类问题只汇总一次，不拆分口径。请生成三个紧凑的聚合报告文件：一个 JSON 汇总（包含实验样本量、支付成功率、treatment 相对 control 的绝对提升百分点、关键漏斗步骤流失量及流失率、数据质量计数）；一个 CSV 按 variant 列出漏斗各步会话计数与转化率；一个 MD 中文简报，概述实验结论及需要立即排查的数据质量风险。
```

### 787. D13_g218_zh (domain=D13, difficulty=7)

```
我需要你基于以下文件完成一份实验读数与数据质量报告：inputs/experiment_assignments.csv、inputs/events.xlsx、inputs/orders.csv、inputs/user_attributes.xlsx、inputs/experiment_notes.md、inputs/event_stream_2026-04.ndjson。这是checkout_v12的A/B实验，目标是判断B方案是否提升购买转化，同时识别关键数据质量问题。请以experiment_notes.md的口径为准，输出2–3个紧凑的报告文件（CSV/JSON/MD），覆盖实验结论、漏斗与质量问题。不要输出明细全表。
```

### 788. D13_g250_zh (domain=D13, difficulty=7)

```
我们刚上线了 exp_checkout_v3 这个实验，需要你基于 inputs/ 下的所有数据（users.xlsx、experiment_assignments.csv、sessions.csv、events.csv、orders.csv、billing_ledger.xlsx、analytics_snapshot.sqlite）做一次完整的 A/B 解读和数据质量审计。请帮我输出三个紧凑的汇总文件：一个抽样/审计摘要 JSON、一个漏斗与实验结果 CSV、一个发现与建议的 Markdown。重点是看看实验有没有分配冲突、重复事件、未来日期等数据问题，以及控制组和治疗组在漏斗各步的转化情况，特别是 purchase 转化率的提升。另外还要看总体漏斗中 landing→add_to_cart 和 checkout_start→payment_submit 的掉失率，以及去重后的净收入。不用逐行明细，只要关键摘要就好。
```

### 789. D13_g265_zh (domain=D13, difficulty=7)

```
请基于以下输入文件完成一次 A/B 实验读出、漏斗分析以及数据质量核查，输出三份紧凑报告：

输入文件：
- inputs/assignments.xlsx
- inputs/events.csv
- inputs/sessions.csv
- inputs/experiment_notes.md

实验目标是评估新注册引导页（Variant B）是否提升“注册后 24 小时内完成首次关键动作”的转化。随机分配单位是 user_id，实验组别记录在 assignments.xlsx。事件流水很长，相关事件只占少量，其余是噪声，请按定义筛选。需要同时做数据质量核查，重点关注重复事件、未来日期事件、冲突分配、会话归属异常。比率定义均为分子除以分母，分母为 0 时结果记为 null。所有日期时间为 UTC，边界采用左闭右开区间 [start, end)。去重、归属与冲突处理规则必须严格一致。

输出三个文件：
- report_summary.json：实验总览、漏斗、关键分组对比、数据质量汇总。
- report_segments.csv：按用户分段的紧凑结果表。
- report_notes.md：简短方法说明与异常说明。

具体需要完成以下分析，每个结果都要能在输出中直接对应到字段或列：

1. 实验有效分配用户数：仅统计 assignments.xlsx 中 assignment_status = 'assigned' 且 arm 属于 'control' 或 'variant_b' 的唯一 user_id 数。
2. 两组的实验内用户数：分别统计 control 与 variant_b 的有效分配用户数。
3. 冲突分配用户数：统计 assignments.xlsx 中同一 user_id 出现多个不同 arm 的用户数。
4. 注册后 24 小时内激活转化率：分子为有效分配用户中，在其注册时间后 24 小时内至少出现 1 次 event_type = 'activate' 的用户数；分母为该组有效分配用户数。
5. 注册后 24 小时内购买转化率：分子为有效分配用户中，在其注册时间后 24 小时内至少出现 1 次 event_type = 'purchase' 的用户数；分母为该组有效分配用户数。
6. 注册到首次激活的中位耗时（小时）：仅对在 24 小时内发生激活的有效分配用户，按首次激活时间减注册时间计算，结果保留 2 位小数。
7. 关键漏斗四步总量：step1=有效注册用户数；step2=注册后 24 小时内至少激活的用户数；step3=在首次激活后 24 小时内至少完成一次 purchase 的用户数；step4=在首次激活后 24 小时内至少完成一次 upsell 的用户数。分别输出总量及分组总量。
8. 会话归属异常数：统计 sessions.csv 中 session_start 早于用户注册时间、或 session_end 晚于注册后 48 小时、或 session_start > session_end 的会话数。
9. 未来日期事件数：统计 events.csv 中 event_time 晚于 2024-07-15 00:00:00Z 的事件数。
10. 重复事件行数与受影响用户数：按 user_id, event_type, event_time, event_id 完全一致判定重复。
11. 购买转化率差值（variant_b - control），保留 4 位小数。
12. 三个用户分段：low_activity、mid_activity、high_activity，按注册后 24 小时内总事件数的分位数切分：低于全体用户 33 百分位为 low_activity，33 到 66 百分位为 mid_activity，高于 66 百分位为 high_activity。分位数按 type=linear 计算。每个分段输出用户数、激活率、购买率。

报告要求：紧凑汇总，不要逐事件明细。report_summary.json 使用清晰字段名，关键指标统一精度。report_segments.csv 至少包含 segment, users, activate_users, purchase_users, activate_rate, purchase_rate 六列。report_notes.md 简述口径、去重规则、异常处理方式以及最重要的 2-3 个异常观察。

注意 assignments.xlsx 可能存在重复记录与冲突分配，必须先按规则处理再计算。events.csv 很大，只有少量行是真正相关事件和异常，请按定义筛选。sessions.csv 的异常判断要依赖注册时间与会话时间的联表结果。仅依据上述 4 个文件，不要假设额外口径。
```

### 790. D13_g324_en (domain=D13, difficulty=7)

```
Use the four input files (users.xlsx, assignments.xlsx, events.csv, funnel_snapshot.xlsx) to produce a Markdown analysis brief covering experiment assignment integrity, event/funnel measurement quality, and A/B funnel performance reconciliation for experiment exp_checkout_cta_v1. Also generate an evidence_table.csv with compact aggregates. Keep it concise and focus on reconciling raw events against the funnel snapshot and flagging data-quality issues.
```

### 791. D13_g342_en (domain=D13, difficulty=7)

```
Produce a compact analysis brief (findings.md) and a supporting evidence table (evidence.json) synthesizing four independent tracks across the four input files in inputs/: experiment_assignments.xlsx, session_events.csv, user_attributes.xlsx, and report_notes.md. The tracks are: experiment assignment integrity/data-quality reconciliation, funnel progression and drop-off analysis, treatment vs control purchase conversion readout, and source reconciliation against user attributes and experiment notes. Use report_notes.md as the methodological source of truth. Our standard definitions apply: user-level purchase conversion for experiment_id=checkout_button_copy_v3 counts only users with exactly one unique assigned_variant; conflicting assignments are excluded and noted separately. Funnel order is landing_view → product_view → add_to_cart → checkout_start → purchase, using session-level presence. Ignore events after 2024-05-10T23:59:59Z. Treat duplicate assignment rows (same user_id+experiment_id+assigned_variant+assigned_at) and duplicate event_id rows as duplicates. Flag sessions where purchase appears before checkout_start in event order as sequence-conflicted. Reconcile any cross-source mismatches explicitly in the brief.
```

### 792. D13_g345_zh (domain=D13, difficulty=7)

```
我这边需要你分析一下 checkout_v3 实验的数据。文件在 inputs/ 下：experiments.xlsx（分流记录）、events_large.xlsx（事件日志）、support_tickets.xlsx（客服工单）、variant_notes.md（业务说明）。这是结账页改版实验，目标是提高 7 天内 purchase 转化。请你综合实验分流、主漏斗、客服反馈和数据质量四个部分，输出一个紧凑的决策简报，给出是否建议全面推广 treatment 的排序结论（推荐/备选/不推荐），并附上关键数字和理由。
```

### 793. D13_g542_zh (domain=D13, difficulty=7)

```
这个试验已经跑完了，我要一版能直接发给业务和产品一起看的结果，帮我把 `experiments.xlsx`、`funnel_events.csv`、`orders.csv` 和 `web_event_log.txt` 里能互相对上的内容整理出来。

我最关心三件事：一是实验两组的购买转化有没有差异，二是漏斗每一步掉了多少，三是数据里有没有明显脏点会影响结论。分组规则就按 experiments 里的分配来，**同一个 user_id 只算最早那条分配**；如果同一个 user_id 出现了不同 variant，就把它记成“冲突分配”。漏斗顺序固定是 landing -> product_view -> add_to_cart -> checkout_start -> purchase，转化就看用户是否真的走到 purchase。订单金额只统计 status = paid 的订单。

另外，`web_event_log.txt` 里有很多正常噪音，但我也怀疑埋了少量异常记录，麻烦一起把未来日期、重复记录、以及任何和订单/漏斗对不上的关键异常找出来。最后给我 3 个文件：一份汇总 JSON、一份漏斗与实验结果 CSV、还有一份简短 MD 说明，格式要适合我直接转发。
```

### 794. D13_g654_zh (domain=D13, difficulty=7)

```
请基于 inputs/ 下的 users.xlsx、user_segments.xlsx、experiment_assignments.csv、events.xlsx、daily_funnel_summary.csv 做一版 2024-05-06 到 2024-05-12 的实验复盘，输出 3 个文件：1) markdown 结论摘要，2) JSON 明细，3) CSV 汇总表。实验口径按 checkout_redesign_2024q2；分流冲突按“同一 user_id 出现多条 assignment 视为冲突，先保留最早 assigned_ts 作为最终分组”，事件去重按 event_id 全局唯一；未来日期事件（event_ts > 2024-05-12 23:59:59）要单独标记但不纳入主指标。主指标只看 session_start→product_view→add_to_cart→checkout_start→payment_success 漏斗，转化率按相邻步骤的去重用户数计算；实验 uplift 用 treatment 相对 control 的绝对百分点差。再把新老用户、设备（ios/android/web）、地区（NA/EMEA/APAC）拆开看 payment_success 转化率和 revenue/visitor；同时给出数据质量统计：重复 event_id 数、重复 assignment 数、冲突 assignment 数、未来日期事件数。
```

### 795. D13_g981739_zh (domain=D13, difficulty=7)

```
请基于 inputs/experiment_assignments.xlsx、inputs/funnel_events.xlsx、inputs/orders_revenue.xlsx 和 inputs/dq_seed_samples.xlsx 出一份合并分析报告，重点看 checkout_v2 相对 checkout_v1 的漏斗转化和收入表现，并把数据质量问题一并标出来。我需要一个可以直接给业务和数据团队看的成稿，结果要尽量压缩成表格化摘要。另外，报告里请明确列出冲突分配、未来日期事件、以及重复订单号这几类问题的规模。
```

### 796. D13_g982332_zh (domain=D13, difficulty=7)

```
我需要你看一下这批实验和漏斗数据，帮我做一个简短的决策稿：判断这个新版本值不值得继续推进，并把最关键的实验结果、漏斗表现和数据质量问题一起讲清楚。输入文件是 product_analytics_data.xlsx、event_log.txt 和 seed_context.docx；最后请输出一个 decision_brief.md。
```

### 797. D13_g982666_en (domain=D13, difficulty=7)

```
We need a decision on whether to roll out Variant B of our new checkout flow or stick with A. I have three datasets: user_profiles.xlsx (user attributes), event_log.xlsx (event stream with funnel steps page_view -> add_to_cart -> checkout -> purchase), and assignment_table.xlsx (A/B assignments). There's also a PDF with data quality rules. Could you produce a brief decision report that ranks the evidence: conversion rates, funnel drop-offs, and any data quality issues that might affect the analysis? I want the key numbers supporting your recommendation.
```

### 798. D13_k982895_zh (domain=D13, difficulty=7)

```
请基于文件 yasserh__amazon-product-reviews-dataset__7817_1.csv 做一份面向产品分析的深度诊断，重点放在“相关性与驱动因素”上：先判断数据里哪些数值字段彼此相关、哪些字段最可能驱动评分和帮助性，再结合品牌/类目/价格区间做分层验证。请直接围绕真实列名分析：reviews.rating、reviews.numHelpful、ean、sizes、upc，以及 prices 里可解析出来的价格信息（如果需要请先从 prices 字段提取 amountMin/amountMax 或其他可用数值）。我需要你把结论整理成可交付的结构化结果，而不是泛泛描述。具体请拆成 4-6 条彼此独立的分析线并并行推进：1）数值字段相关矩阵与最强正/负相关对；2）评分与帮助性（reviews.numHelpful）的驱动因素，尤其按品牌、类目、价格分层；3）价格与评分/帮助性之间的关系；4）不同品牌/类目下的高评分与高帮助性是否一致；5）缺失值和脏字段对分析可靠性的影响；6）如果可行，识别少量异常组合（例如高价低分、低价高帮助）作为运营关注点。最后给我一个简洁的 JSON 式结论摘要，包含关键数值、Top 关联项、以及你认为最值得进一步验证的 3 个假设。
```

### 799. D13_k983107_zh (domain=D13, difficulty=7)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv（字段：user_id、auction_id、cat_id、cat1、property、buy_mount、day）做一版面向产品分析的深度分析，重点围绕“分布与阈值分层（高于/低于业务阈值的占比、分位数分桶、结构占比）”展开。我要的是能直接用于汇报的结论，不要泛泛而谈。请拆成多个彼此独立的分析轨道，至少覆盖：1）买次数/买量在用户层面的分布与阈值分层；2）按时间维度看交易活跃与高低活跃用户占比变化；3）按类目(cat_id/cat1)的集中度、头部/长尾分布与份额；4）按商品属性(property)里关键属性的出现频次、覆盖率和混合结构；5）高频购买用户与低频用户在品类偏好和购买量上的差异；6）给出可以落地的业务分层建议（例如如何定义高价值/潜力/沉默用户）。请输出成 analysis_summary.json 的分析思路与结果框架。
```

### 800. D13_k983265_zh (domain=D13, difficulty=7)

```
请基于文件 PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv 做一份面向产品分析的数据质量审计，重点围绕缺失值、`?`/空字符串、重复记录、数值范围异常、类别不一致这几类问题展开。请先按字段级别把问题讲清楚，再结合商品维度（如 brand、product_category_tree、product_rating、overall_rating、价格字段）判断这些问题会如何影响后续的产品分析、定价分析和类目分析。不要只做总览，我需要你拆成多个可并行的分析轨道，分别输出每条轨道的发现、证据和可执行修复建议，最后汇总成一份适合发给业务和数据工程同事的分析摘要。
```

### 801. D13_k983366_en (domain=D13, difficulty=7)

```
Using yasserh__amazon-product-reviews-dataset__7817_1.csv, build a product-analytics readout focused mainly on distribution and threshold cohorts. I want a concise executive summary plus 4–6 independent analysis tracks that can be run in parallel: (1) review-rating cohorting around business thresholds like <3, =3, >3 and <4 vs >=4, with overall mix shares; (2) rating distributions by brand and product name, including quantile buckets and which items are most concentrated in the top/bottom cohort; (3) helpfulness and recommendation behavior by rating cohort, including missing-data rates for reviews.doRecommend, reviews.numHelpful, reviews.rating, and username; (4) review text volume and sentiment proxy proxies from reviews.text/reviews.title lengths across rating buckets; (5) category-level mix and threshold penetration using categories, focusing on which category strings skew toward high ratings; and (6) any notable outliers in prices or product metadata that could affect interpretation. Please use only the real columns in the file and keep outputs decision-ready.
```

### 802. D13_k983383_zh (domain=D13, difficulty=7)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv（列：user_id, auction_id, cat_id, cat1, property, buy_mount, day）做一份面向产品分析的异常与离群点排查报告，重点围绕“显式数值规则”的异常识别：例如 buy_mount 的极端值、day 的异常集中/断点、property 字段中罕见属性组合、重复购买/重复交易模式、以及按 cat_id / cat1 / user_id 维度的高风险异常群体。请把分析拆成多个彼此独立的子任务，输出可直接给业务/风控/增长团队看的结论，并且明确写出每条规则命中的样本数、占比、涉及的关键维度和值。请特别关注：1）buy_mount 是否存在明显高于整体分布的离群值；2）同一 user_id 在短时间或同日内的异常高频交易；3）极少出现的 cat_id / cat1 / property 组合；4）重复 auction_id 或重复 user_id- auction_id 组合；5）按 day 分布是否存在异常峰值或低频尾部日期；6）对这些异常是否能做出可落地的业务解释建议。请给出分 track 的分析结论、可复核的规则、以及建议后续需要进一步排查的数据点。
```

### 803. D13_k983490_en (domain=D13, difficulty=7)

```
Using PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv, I need a product-analytics readout focused mainly on correlation and driver analysis. Please split it into 5 independent tracks so they can be worked in parallel: (1) quantify how retail_price and discounted_price move together overall and within key product categories, including rounded correlations and price-gap summaries; (2) find the strongest numeric drivers of discounting, especially relationships between retail_price, discounted_price, discount percent, and any price-gap derived metric; (3) check whether product_rating / overall_rating are associated with pricing behavior or discount intensity, with missing-value awareness because the rating fields are messy; (4) compare those relationships across brands and product_category_tree to identify segments where pricing signals are unusually strong or weak; (5) flag the most extreme products and categories by price gap, discount ratio, and any unusual correlation patterns so I can sanity-check the findings. Keep it tightly grounded in the actual columns: retail_price, discounted_price, product_rating, overall_rating, brand, product_category_tree, and any derived numeric metrics you need from them.
```

### 804. D13_k983546_en (domain=D13, difficulty=7)

```
Using yasserh__amazon-product-reviews-dataset__7817_1.csv, run a product analytics deep-dive focused on correlation and driver analysis. I need one integrated readout that explains which numeric fields move together, where the strongest associations are after rounding correlations, and what operational/product signals seem to drive review performance. Please anchor the work on the real columns in this file, especially reviews.rating, reviews.numHelpful, ean, sizes, and upc, and also check whether review sentiment/recommendation patterns differ by brand, manufacturer, and product name. Break it into independent workstreams so different analysts can tackle them in parallel, then synthesize the findings into a concise summary and a small set of evidence tables I can share with product leadership.
```

### 805. D13_k983878_en (domain=D13, difficulty=7)

```
Using akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv, give me a product-analytics readout focused mainly on temporal trend analysis of purchase activity in this trade history. I need a concise but decision-ready summary that uses the real columns user_id, auction_id, cat_id, cat1, property, buy_mount, and day. Please break it into a few independent workstreams so multiple analysts could work in parallel: overall demand trends by day/month, changes in order value via buy_mount over time, category and parent-category trend shifts over time, repeat-vs-new user behavior over time, and a short anomaly/seasonality scan for unusual spikes or dips. If there are any obvious period-over-period changes, call them out with exact figures based on the data.
```

### 806. D13_k984058_zh (domain=D13, difficulty=7)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一次产品分析，重点看“排名与集中度”：哪些品类、哪些商品、哪些用户贡献了最多交易，头部是否高度集中，是否符合二八法则。请结合真实字段 user_id、auction_id、cat_id、cat1、property、buy_mount、day 做 4-6 个相互独立的分析轨道，尽量拆给不同子任务并最后汇总成 analysis_summary.json。具体希望你覆盖：1）按 cat_id / cat1 / auction_id / user_id 的交易次数 Top-N 排名；2）Top-N 贡献的交易占比、累计占比、是否存在明显 Pareto 集中；3）买量 buy_mount 在头部组与长尾组中的差异；4）按 day 看头部交易是否集中在少数日期；5）property 字段的高频特征及其集中度；6）如果能做，补充用户与商品的交叉集中度（例如头部用户是否只集中在少数 auction_id 或 cat_id）。请输出可直接给我决策参考的结论，所有统计必须基于这份固定数据，不要编造。
```

### 807. D13_k984074_zh (domain=D13, difficulty=7)

```
请基于文件 yasserh__amazon-product-reviews-dataset__7817_1.csv 做一份面向产品分析的多部分深度分析，重点放在时间趋势与环比变化上。请围绕 reviews.date、dateAdded、dateUpdated 这类时间字段，结合 reviews.rating、reviews.doRecommend、reviews.numHelpful、brand、name、categories、prices 等列，判断：1）整体评分和推荐意愿随时间是否有变化，最近阶段相较更早阶段是改善还是恶化；2）不同品牌/产品的评分趋势是否分化，哪些品牌是长期高分、哪些是近期下滑；3）高评价、低评价、强烈推荐等评论在时间上的占比变化，以及是否存在明显的峰值月份或阶段；4）评论有帮助数与评分/推荐的关系是否随时间变化；5）新近上架/更新的商品是否和更早商品在口碑上有系统差异。请输出一份可直接给业务团队看的结论摘要，并按可执行的分析步骤拆分任务。
```

### 808. D13_k984109_zh (domain=D13, difficulty=7)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份偏产品分析的时序复盘：重点围绕 day 这一时间字段，分析这 1500 条交易记录在时间上的变化趋势、峰值/低谷、周期性和结构性变化，并结合 user_id、auction_id、cat_id、cat1、property、buy_mount 这些字段一起看。我要的是能直接指导后续运营和商品策略的结论，不要只做描述性统计。请把分析拆成多个相互独立的方向并行推进，最后汇总成一份可以落地的总结，最好能指出：1）整体交易量随时间如何变化，是否有明显的周/月级别波动；2）高峰期主要由哪些品类/一级类目驱动；3）不同商品属性组合在不同时段是否有差异；4）买量 buy_mount 是否存在时间上的异常波动；5）老客/新客在时间趋势上的贡献是否不同；6）如果把时间切成前后两个阶段，哪些关键指标发生了最明显的变化。
```

### 809. D13_k984344_zh (domain=D13, difficulty=7)

```
请基于数据文件 yasserh__amazon-product-reviews-dataset__7817_1.csv 做一份面向产品分析的多部分诊断，重点围绕“相关性与驱动因素分析”：看哪些数值字段彼此同向变化、哪些字段与评分/有帮助数形成主要关联、以及不同品牌/品类/时间维度下这些关系是否稳定。请只使用现有列（例如 reviews.rating、reviews.numHelpful、ean、upc、sizes、reviews.doRecommend，以及 prices 里的价格信息如果需要先解析也可以），不要臆造字段。希望输出可落地的结论：1）核心数值字段相关矩阵的关键配对及其强弱；2）评分与是否推荐、有帮助数之间的关系；3）价格/价格层级与评分、推荐之间的关系；4）品牌或品类层面的驱动差异；5）文本/标题长度等简单可量化特征与互动指标的关系；6）如果存在日期字段，就补充按时间切片后的相关性稳定性检查。请把结论整理成一个适合汇报的 analysis_summary.json。
```

### 810. D13_k984449_zh (domain=D13, difficulty=7)

```
请基于文件 yasserh__amazon-product-reviews-dataset__7817_1.csv 做一份面向产品分析的多部分深度分析，重点放在“相关性与驱动因素分析”：先找出数值字段之间哪些指标彼此同步变化、哪些字段相关性最强，并尽量识别出可能影响评分或有用性反馈的关键因子。请围绕 reviews.rating、reviews.numHelpful、ean、upc、sizes、prices 等数值字段展开，结合 brand、manufacturer、categories、reviews.doRecommend、reviews.title、reviews.text 等字段做交叉验证。我要的是可直接用于汇报的结论，而不是单纯的统计表。请把分析拆成几个彼此独立的轨道，分别覆盖：总体数据质量与可用性、数值字段相关结构、评分驱动因素、帮助性反馈驱动因素、品牌/品类层面的差异，以及文本与评分/推荐倾向的简单关联。请输出简洁结论，所有数值尽量四舍五入到2位小数。
```

### 811. D13_k984658_zh (domain=D13, difficulty=7)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv（字段：user_id、auction_id、cat_id、cat1、property、buy_mount、day）做一份面向产品分析的多线程数据质量审计，重点围绕缺失值/空字符串/“?”、重复记录、字段取值范围是否合理、分类口径是否一致、以及基础业务分布是否异常。请把结论整理成 analysis_summary.json，要求能直接支持我判断这份交易明细能不能进入后续用户购买分析。请拆成 4-6 个彼此独立的分析轨道并行推进：1）整体数据完整性与缺失/异常字符扫描；2）重复行、重复主键和疑似重复交易检查；3）数值字段范围、非法值、极端值与日期合法性检查；4）cat_id 与 cat1 的层级一致性和分类分布异常检查；5）property 字段的结构化质量检查（分隔符、键值对格式、空值占比、异常模式）；6）从 user/auction 层面的基础业务分布与异常集中度检查。最后给出一页式结论：哪些问题最严重、影响哪些分析、建议的清洗优先级。
```

### 812. D13_k984702_en (domain=D13, difficulty=7)

```
Using PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv, I need a product-analytics deep dive focused on ranking and concentration. Please analyze which brands, categories, and products dominate the catalog by frequency and by value, and quantify how concentrated the assortment and pricing are (top-N shares, Pareto-style concentration, and long-tail behavior). I also want a practical readout of where discounts are most concentrated and whether high-value items are driven by a small set of brands or categories. Use the existing columns only: product_name, product_category_tree, brand, retail_price, discounted_price, product_rating, overall_rating, is_FK_Advantage_product, and pid. Please structure the work so separate analyses can run independently and then be combined into one concise summary.
```

### 813. D13_k984829_zh (domain=D13, difficulty=7)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一次偏产品分析的深度诊断，重点围绕“分布与阈值分层（高于/低于业务阈值、分位数组、结构占比）”来展开。请先读懂数据里的 user_id、auction_id、cat_id、cat1、property、buy_mount、day 这些字段，再从交易行为、商品属性复杂度、类目集中度、时间分布、以及高低阈值人群结构几个角度拆成多条独立分析线，最后给我一个可直接汇总到 analysis_summary.json 的结果。我要的是能支持业务讨论的结论，不要泛泛而谈；尤其请重点回答：样本里有多少交易落在不同购买量阈值之上/之下、不同分位数组的人群结构如何、以及这些阈值人群在类目与属性上的 mix share 是否明显不同。
```

### 814. D13_k984933_en (domain=D13, difficulty=7)

```
Using PromptCloudHQ__flipkart-products__flipkart_com-ecommerce_sample.csv, build a product-analytics readout focused on ranking and concentration. I want to know which brands, categories, and price bands dominate the catalog and value pool, and whether a small set of products drives most of the assortment and revenue proxy. Please analyze the real columns product_name, product_category_tree, retail_price, discounted_price, brand, product_rating, overall_rating, is_FK_Advantage_product, and product_specifications. Decompose this into independent workstreams so a small sub-agent team can split up the work: one track for brand concentration, one for category concentration, one for price/value concentration using retail_price and discounted_price, one for product-rating concentration, and one for catalog breadth using product counts and missingness. I need the output framed as a concise executive summary plus supporting ranked lists, Pareto-style share calculations, and a few sanity checks on the top contributors.
```

### 815. D13_k985105_zh (domain=D13, difficulty=7)

```
请帮我基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份面向产品分析的异常与离群点诊断，重点围绕明确数值规则（阈值、IQR、罕见类别、极端值）来排查交易日志中的异常行为。请直接用数据说话，不要泛泛而谈；输出一个可交付给业务方的 analysis_summary.json。请至少拆成 5 个彼此独立的分析轨道：1）buy_mount 的极端大单/异常大单识别；2）day 的极端日期与时间分布异常（例如异常早/晚、超长尾）；3）cat_id 与 cat1 的罕见类目、低频类目占比及是否集中在异常交易中；4）property 字段的稀有属性组合、空值/超长属性串与异常单的关联；5）按用户和按商品的异常聚集（如同一 user_id 或 auction_id 的重复出现、异常集中）；6）把上述规则串起来给出一份综合异常清单与可复核指标。请在分析里明确写出你使用的阈值规则、IQR 规则、Top-N/Bottom-N 罕见项、以及各异常类型的数量和占比。最后请给出你认为最值得人工复核的异常模式。
```

### 816. D13_k985201_zh (domain=D13, difficulty=7)

```
请基于文件 akacoder404__taobao-maternal-and-infant-shopping-data-set__sam_tianchi_mum_baby_trade_history.csv 做一份面向产品分析的多阶段分析，重点围绕 day 字段的时间趋势与阶段性变化展开。这个数据里有 user_id、auction_id、cat_id、cat1、property、buy_mount、day，请不要改动任何原始值。我要你重点回答：1）整体交易量、购买量、独立用户数在时间上怎么变化，是否存在明显的月度/季度波动；2）不同品类(cat1、cat_id)的增长/下滑是否与整体趋势一致，哪些品类在后期更活跃；3）高频用户与低频用户在不同时间段的购买贡献是否发生迁移；4）商品属性(property)的复杂度或属性数量是否与购买行为、时间段有关；5）是否存在异常日期或突增突降的交易日，需要给出可落地的产品解释。请把分析拆成多个互相独立的 track 交给不同子任务并行做，最后汇总成一份适合产品团队阅读的结论。
```

### 817. D13_k985458_zh (domain=D13, difficulty=7)

```
请基于 datafiniti__grammar-and-online-product-reviews__GrammarandProductReviews.csv 这份数据，围绕“排名与集中度”帮我做一版产品分析：先看评论在品牌、品类、商品、评论来源等维度上的头部集中情况，再结合评分、推荐意愿和有帮助票数判断头部是否真的代表高质量。请重点输出可执行结论：哪些品牌/商品/品类/来源贡献了大部分评论，Top N 占比和累计占比是否呈现明显二八分布，低频长尾是否值得继续投入，以及是否存在“高声量但低口碑”或“低声量但高口碑”的异常对象。数据里可用的关键列包括 brand、categories、name、reviews.rating、reviews.doRecommend、reviews.numHelpful、reviews.sourceURLs、reviews.username、reviews.didPurchase、reviews.dateSeen、reviews.text、manufacturer、upc、ean、reviews.id。请按 4-6 个彼此独立的分析轨道拆开做，方便并行处理，并最终汇总成一份可直接给业务看的 analysis_summary.json。
```

### 818. D13_k985496_zh (domain=D13, difficulty=7)

```
请基于文件 mfaaris__spotify-app-reviews-2022__reviews.csv（字段包括 Time_submitted、Review、Rating、Total_thumbsup、Reply）帮我做一份面向产品分析的分群对比分析，重点看不同评分/互动/时间段/评论回复之间的差异，找出最大的分群差距和可能对应的产品问题。请把结论写成可直接给产品、运营和客服看的分析摘要，并尽量用可量化指标说明：例如各分组的评分均值、点赞均值、评论长度差异、回复覆盖率差异、极端高低分组的规模和差距。因为我时间很紧，请按独立分析轨道拆分并分别产出结果，最后汇总成一个简洁的 analysis_summary.json。需要特别关注：1）不同 Rating 之间的 Total_thumbsup 差异；2）不同 Rating 之间评论长度与评论内容倾向差异；3）是否存在客服 Reply 的覆盖或响应偏差；4）按时间段（月份/周内）比较评分或点赞表现；5）找出最大差距的分群组合并给出具体数值。
```

### 819. D13_k985628_zh (domain=D13, difficulty=7)

```
请基于文件 ayeshaimran1619__foodpanda-data-analysis__Foodpanda Analysis Dataset.csv 做一份面向产品分析的多阶段分析，重点围绕时间趋势/周期变化来判断业务和体验的变化情况。请不要只做静态描述，而是按时间维度把订单、评分、配送、留存/流失、支付方式的变化串起来分析，并尽量识别最近与较早时期的差异。需要结合这些真实字段：customer_id、gender、age、city、signup_date、order_id、order_date、restaurant_name、dish_name、category、quantity、price、payment_method、order_frequency、last_order_date、loyalty_points、churned、rating、rating_date、delivery_status。请输出一份适合产品团队使用的结论摘要和可行动建议。要求把工作拆成 4-6 个彼此独立的分析轨道，便于不同子任务并行推进：例如订单/GMV 时间趋势、评分与配送时效趋势、不同城市或人群的时序变化、支付方式随时间的迁移、流失与活跃用户的时序对比、以及复购/频次变化等。
```

### 820. D13_k985640_zh (domain=D13, difficulty=7)

```
请基于文件 nisargpatel__automobiles__Automobile.csv 做一份面向产品分析的深度分析，重点围绕“排名与集中度”来展开：先找出不同车型属性下的头部贡献者，再量化头部集中度、长尾分布以及关键细分市场的价值集中情况。请结合真实字段（如 make、body_style、drive_wheels、fuel_type、engine_type、number_of_cylinders、price、horsepower、city_mpg、highway_mpg、curb_weight、wheel_base、length、width、height、symboling 等）输出可直接给业务看的结论，最好能指出哪些品牌/车型组合、哪些驱动形式、哪些车身类型、哪些发动机结构在销量代理指标（样本频次）和价值指标（价格）上最集中。也请补充一个简短的异常/反直觉观察：例如高价并不一定来自最常见的品牌，或者高集中度细分是否同时伴随更高/更低的能耗表现。
```

### 821. D13_k985667_zh (domain=D13, difficulty=7)

```
请基于文件 muhammadadiltalay__imdb-video-games__imdb-videogames.csv 做一份面向产品分析的深度分析，重点围绕“相关性与驱动因素分析”：看哪些数值字段彼此一起变化、哪些变量对评分/热度（rating、votes）最相关，以及不同年份、类型标签、证书（certificate）和文本质量（例如 plot 是否缺失）对这些指标的影响。请把分析拆成几个彼此独立的工作流，方便并行推进：1）数据质量与字段可用性检查（year、rating、votes、certificate、plot 缺失情况）；2）核心数值变量相关性分析（year、rating、votes 之间的相关系数，含四舍五入）；3）评分驱动因素分析（按证书、类型标签、年份分组，看 rating 均值/中位数/样本量）；4）热度驱动因素分析（votes 与 rating、year 的关系，以及高票样本的共同特征）；5）类型组合与交叉标签分析（Action/Adventure/Comedy/Crime/Family/Fantasy/Mystery/Sci-Fi/Thriller 的共现模式及其与 rating/votes 的关系）；6）输出一页式结论，明确哪些因素更像是“评分驱动”、哪些更像是“热度驱动”，并给出可执行的产品建议。请直接用真实数据回答，不要臆测。
```

### 822. D13_k985720_zh (domain=D13, difficulty=7)

```
请基于文件 jmmvutu__summer-products-and-sales-in-ecommerce-wish__summer-products-with-rating-and-performance_2020-08.csv 做一份面向产品分析的分群对比分析，重点看不同类别/标签/物流/国家之间的表现差异，以及这些差异在销量、评分、价格和转化相关指标上的体现。请围绕以下字段展开：price、retail_price、units_sold、rating、rating_count、uses_ad_boosts、badges_count、badge_local_product、badge_product_quality、badge_fast_shipping、shipping_option_price、shipping_is_express、countries_shipped_to、inventory_total、has_urgency_banner、origin_country、shipping_option_name、product_color、product_variation_size_id、theme、crawl_month。请输出一个可交付给业务团队的分析摘要，并明确说明哪些分组之间的差距最大、哪些组表现最好/最差、以及这些差异是否可能与促销、物流或商品属性有关。请把任务拆成多个互不依赖的分析轨道，便于并行处理。
```

### 823. D13_k985775_zh (domain=D13, difficulty=7)

```
请基于文件 jessicali9530__animal-crossing-new-horizons-nookplaza-dataset__housewares.csv 做一份面向产品分析的深度拆解，重点围绕“时间/序列趋势”来观察家居类物品在不同版本（Version）上的变化，以及各类物品属性在版本序列中的迁移与结构变化。请把分析拆成多个互相独立的工作流，便于并行推进：1）按 Version 做整体规模与结构趋势，观察每个版本新增/存量/稀缺属性的变化；2）按 Source、Source Notes 做版本演进中的获取方式变化，比较 Nook's Cranny / Nook Miles Shop / Crafting 等来源的占比与价格特征随版本的变化；3）按 Tag、HHA Series、HHA Set 做品类结构与主题迁移，找出不同版本中最活跃的主题和标签；4）按 Buy、Sell、Miles Price、Kit Cost 做价格带与收益结构的版本趋势，关注中位数、均值和极值的变化；5）按 Interact、Outdoor、Lighting Type、Speaker Type 做功能属性的版本变化，识别交互性/户外适配/灯光与音频能力的升级路径；6）如果某些字段存在缺失或空值，请把它们当成数据质量/产品覆盖面的信号，分析缺失率是否在不同版本中系统性变化。输出要像给产品负责人看的结论：每个子分析都要有明确的趋势判断、变化幅度、可能的业务解释，并尽量指出最值得关注的版本拐点。数据里可直接使用的字段包括 Name、Variation、DIY、Buy、Sell、Kit Cost、Miles Price、Source、Source Notes、Version、HHA Series、HHA Set、Interact、Tag、Outdoor、Speaker Type、Lighting Type、Catalog、Variant ID 等；请只基于这些真实列做分析，不要臆造时间字段，Version 就是主序列维度。
```

### 824. D13_k985822_zh (domain=D13, difficulty=7)

```
请基于文件 avinashsingh004__co2-emissions-by-sectors__Co2_Emissions_by_Sectors.csv 做一份面向产品分析的深度分析，重点围绕“排名与集中度”展开：先找出 Co2_Emissions_MetricTons、Energy_Consumption_TWh、GDP_Billion_USD、Population_Millions、Renewable_Energy_Percentage 等核心指标的 Top-N 组别（按 Country、Region、Industry_Type、Year 分组都要看），再衡量头部集中度（例如 Top 10/Top 20 占总量比例、是否符合帕累托特征），同时结合 Industry_Type、Region、Country 的交叉维度看哪些国家/地区/行业长期处于头部，以及这些头部组别在能源消耗、工业排放、交通排放和可再生能源占比上的共同特征。请把分析拆成 4-6 个相互独立的 track，分别覆盖：1）总体分布与头部集中度，2）按国家的排放/能耗排名与份额，3）按地区的集中度与差异，4）按行业类型的头部贡献与长期趋势，5）Top 组别的可再生能源/城市化/增长指标画像，6）找出最极端的年份或组合（例如某年某国某行业的峰值）。输出需要能支撑产品决策，重点是哪些少数对象贡献了大部分风险/机会。
```

### 825. D1_g1280_en (domain=D1, difficulty=7)

```
I need a research brief on Office Collaboration using the source files in inputs/. I've got contacts.xlsx, calendar_events.xlsx, action_items.xlsx, status_rollups.csv, meeting_notes.txt, and office_collab.sqlite. Please synthesize findings from these into a findings.md with 3–4 independent analysis tracks, note any cross-source conflicts or inconsistencies, and end with a short conclusion. Also produce a small evidence table (evidence_table.csv or .md) that maps each major finding to the supporting files and records.; just compute what's needed and reconcile any discrepancies across sources.
```

### 826. D1_g1470_zh (domain=D1, difficulty=7)

```
请基于我放在 inputs/ 里的 4 个材料做一版会议与执行复盘简报，输出两份文件：一份 findings.md，另一份 evidence_table.csv。简报要覆盖 4 条彼此独立但需要最后合并的分析线：① 2025-06-16 到 2025-06-30 的核心项目/例会日程梳理，按事件类型分组并标出冲突；② 同期行动项的交付状态与逾期情况，逾期定义按 due_date 早于 2025-06-30 且状态不在 closed/done/cancelled；③ 同期状态回传与风险升级的口径一致性，重点看风险等级、升级渠道、以及是否被后续回写修正；④ 跨来源冲突核对：日历、任务表、状态纪要、会议纪要之间凡是同一主题/同一日期但时间、负责人、结论不一致的，都要单独列出并说明你最后采用哪条口径。我们的标准是：优先级按 P0>P1>P2>P3；风险分数 = 0.5*churn_score + 0.3*overdue_ratio + 0.2*ticket_pressure，其中 churn_score 取 0/1，overdue_ratio = overdue_open_items / open_items（若 open_items 为 0 则记 0），ticket_pressure 取 0/1；risk_score >= 0.7 记为高风险，0.4-0.699 记为中风险，低于 0.4 记为低风险。事件去重按 event_id；任务去重按 task_id；状态纪要按 update_id；会议纪要按 note_id。输出里要给出每条分析线的结论、关键数字、以及一张小型证据表（不要铺全量明细）。另外，请把互相打架的地方明确写出来：哪些来源冲突、你如何裁决、裁决后对总数有什么影响。文件名必须严格使用 inputs/ 下的原始文件名。
```

### 827. D1_g967_en (domain=D1, difficulty=7)

```
I need a synthesis brief reconciling these files: inputs/employees.json, inputs/meetings.xlsx, inputs/action_items.csv, inputs/status_messages.xlsx, inputs/agenda_notes.xlsx. Use 2026-04-25 as the as-of date. Please deliver:

- findings.md with parallel analysis tracks, cross-source reconciliation, and takeaways.
- A compact evidence table (JSON or table) with these metrics:
  - Total unique meetings; valid deduped action items; overdue open items; on-time done items; close‑date anomalies.
  - Owner with most open valid items; meeting with most valid items.
  - Deduped messages; unique senders; valid status‑category messages.
  - action_ids tied to invalid meetings; duplicate action_ids.

Keep it concise, no row‑by‑row dumps.
```

### 828. D1_g980089_zh (domain=D1, difficulty=7)

```
我在整理办公室协作周报，需要你把这 5 个输入文件串起来做一次完整的汇总分析：inputs/calendar_events.xlsx、inputs/contacts.xlsx、inputs/inbox_messages.xlsx、inputs/action_items.json、inputs/status_rollups.csv。请最后输出一份单文件的中文汇总报告。
- 先把日历、联系人、邮件、行动项、状态汇总各自清点一遍，找出重复、缺失和明显异常。
- 再围绕 4 月下旬到 5 月下旬这几封 Partner Corp 相关邮件，把需要回复的事项、联系人可达性和会议排期情况合在一起看。
- 报告里要有一页/一节简短结论，外加一张关键统计表，方便我直接转发给团队。
- 另外把你发现的异常点单独列出来，尤其是重复记录、缺失日期、冲突排期和状态汇总里的异常峰值。
```

### 829. D1_g980611_zh (domain=D1, difficulty=7)

```
我把三个输入文件都放在 inputs 下面了：meetings_calendar.xlsx、action_items.xlsx、status_rollup_noise.log。请基于这三份材料做一份汇总报告，重点帮我把会议、待办和状态回溯串起来看。我需要你先分别梳理会议日程、行动项和日志里的状态信息，再合并成一份能给管理层看的简明结论。报告里要特别处理三类情况：第一，会议表和任务表里都可能有重复编号，但我只关心编号一致且状态不一致的冲突记录；第二，日志文件很长，里面夹着大量噪声，只需要识别出我明确嵌进去的 seed_record 文本，以及那组重复但状态冲突的 rollup 记录；第三，行动项里要统计 Open、Blocked、逾期、以及负责人分布，会议里要统计去重后的会议总量和周经理相关的会议量。最后请把所有结果整理到一个 Excel 报告里，内容要紧凑但完整，最好包含一个总览页和若干明细页，方便我直接转给团队。
```

### 830. D1_g981372_zh (domain=D1, difficulty=7)

```
请基于 project_calendar_actions.xlsx、action_items_log.xlsx、status_rollup_source.xlsx、contacts_directory.xlsx 和 partner_meeting_request_memo.pdf 做一个会议与行动项决策简报，输出 D1_g981372_zh__gpt5.4mini/decision_brief.md。我要你综合判断 2026-05-23 17:00-18:00 这场会是否能按原计划推进，还是直接建议切到次日同一时间，并把理由、影响和建议动作写清楚。另外顺手把需要先处理的行动项、异常数据和联系人可达性一起梳理进去，结论要按推荐优先级排好。
```

### 831. D1_k982275_zh (domain=D1, difficulty=7)

```
请基于数据文件 ka66ledata__project-management-risk-raw__project_risk_raw_dataset.csv 做一份面向办公室/运营与协作分析的项目风险诊断。重点围绕“时间序列/阶段推进中的变化趋势”展开：例如按 Project_Phase、Project_Start_Month、Current_Phase_Duration_Months、Estimated_Timeline_Months、Change_Request_Frequency、Schedule_Pressure、Budget_Utilization_Rate、Risk_Level、Historical_Risk_Incidents 等字段，分析项目在不同阶段、不同开始月份、不同持续时长区间里的风险变化、协作压力变化和偏差趋势。请把结果整理成适合管理层阅读的结论，并明确指出哪些阶段/月份/组合最容易出现风险上升、协作效率下降或预算/进度失控；同时给出可执行的运营建议。不要只做静态分组，要尽量比较前后变化、月度差异、阶段推进差异和高低风险组之间的趋势差别。
```

### 832. D1_k983186_zh (domain=D1, difficulty=7)

```
请基于文件 sumeakash__ai-impact-on-job-sector__ai_job_impact.csv 做一份面向办公室/运营/协作场景的分析简报，重点看不同员工细分群体之间的差异：哪些群体在 AI 采用、自动化风险、薪酬变化、生产率变化和工作满意度上差距最大。请围绕这些字段做分组对比与交叉分析，结合 Education_Level、Industry、Job_Role、Gender、Remote_Work、AI_Adoption_Level、Automation_Risk、Upskilling_Required、Job_Status 等维度，找出最值得管理层关注的 segment gaps，并给出可执行结论。需要把分析拆成多个互相独立的部分，便于并行推进，最后汇总成 analysis_summary.json。
```

### 833. D1_k983871_en (domain=D1, difficulty=7)

```
Using vetrirah__av-healthcare2__train.csv, please analyze how hospital stay patterns change over time/sequence and what that means for office operations and collaboration planning. Build the main story around temporal trend analysis: compare stay-duration mix, admission deposits, visitor load, and severity mix across ordered sequences of cases, and look for period-over-period shifts by hospital/ward/city segments. I also want practical operational takeaways on which service lines or locations show worsening throughput risk, where collaboration demand is rising, and whether admission/deposit patterns are moving in the same direction as longer stays. Use the real columns in the file, including case_id, Hospital_code, Hospital_type_code, City_Code_Hospital, Hospital_region_code, Available Extra Rooms in Hospital, Department, Ward_Type, Ward_Facility_Code, Bed Grade, patientid, City_Code_Patient, Type of Admission, Severity of Illness, Visitors with Patient, Age, Admission_Deposit, and Stay.
```

### 834. D1_k983899_zh (domain=D1, difficulty=7)

```
请基于文件 nehaprabhavalkar__av-healthcare-analytics-ii__train_data.csv 做一份面向办公室/运营协作分析的深度诊断，重点围绕“时间/序列变化”来讲清楚入院量、等待体验、住院时长和患者结构的变化趋势。数据里没有真实日期字段，所以请把 Stay 当作有序的住院阶段序列来做趋势切分（例如按 0-10、11-20、...、91-100 分段），分析不同阶段之间的变化率、占比变化和结构迁移，并结合 Hospital_region_code、Hospital_type_code、Department、Type of Admission、Severity of Illness、Age、Bed Grade、Visitors with Patient、Admission_Deposit 等字段解释运营含义。请把结果拆成 4-6 个彼此独立的分析轨道，适合分给多个子任务并行完成：1）总体序列分布与阶段迁移；2）不同医院/区域的序列对比；3）科室与入院类型在序列上的变化；4）患者年龄、病情严重程度与陪护人数的联动趋势；5）押金与床位等级在不同序列阶段的变化；6）找出最值得关注的异常组合和运营机会。最后给一份可直接汇报的结构化结论，明确哪些阶段/群体最需要优先优化。
```

### 835. D1_k983920_en (domain=D1, difficulty=7)

```
Using vladtasca__fomc-meeting-statements-and-minutes__communications.csv, analyze FOMC communications with an office/operations & collaboration lens, but make the main focus temporal: how communication volume and content evolve over time across Date, Release Date, and Type. I need a practical readout on trends, release-lag patterns, and shifts in the language of the texts so I can understand operational cadence and collaboration intensity across periods. Please break it into separate workstreams for time-series volume trends, period-over-period changes by communication Type, release-delay analysis, and text-length/content-intensity trend analysis. Also flag any notable concentration of communications in specific years/months and summarize the strongest time-based patterns in a compact JSON output.
```

### 836. D3_g1019_zh (domain=D3, difficulty=7)

```
我需要你基于以下四个输入源，输出一份面向业务管理层的综合分析简报（建议文件名 findings.md），并附带一个小型证据表（建议文件名 findings_evidence.csv 或放在 Excel 的一个 sheet 里）。简报要分成 3–4 条相互独立的分析轨道，最后合成为统一结论；证据表列出关键证据、来源和结论。两个交付件都要简洁，不要逐行明细。

输入文件：
- inputs/employee_roster.xlsx：员工花名册，包含 employee_id、dept、age、workclass、education、education.num、occupation、relationship、salary、hire_date。
- inputs/monthly_kpis.xlsx：按月/部门的经营 KPI，包含 month、dept、revenue、cost、tickets、sla_rate、churn_rate。
- inputs/customer_feedback.jsonl：客户反馈明细，包含 feedback_id、month、dept、topic、sentiment、score。
- inputs/QA_log_big.txt：大体量审计日志，绝大多数是普通流水，少量关键异常埋在其中。
- 可选参考：inputs/reference.db 中有部门别名映射表，按需使用。

请完成以下分析（我把所有要求和规则写在下面，你按规则严格执行）：

1. 统计四个输入源的记录规模（行数/条数），并分别给出每个源中需要剔除的数据量：
   - 员工花名册：重复 employee_id 数（去重时保留最后一条）、负薪资数（salary ≤ 0）、education.num 不一致数（只接受 9、10、12、13、14、16，其余算不一致）、年龄不在 18–70（含边界）的条数。
   - KPI 表：非法 sla_rate 条数（不在 [0,1] 内）、负 tickets 条数（tickets < 0）。
   - 反馈表：非法 score 条数（不在 1–5 范围内）、非法 month 条数（必须满足 YYYY-MM 且月份合法，如 2024-03 合法，2024-13 不合法）。
   异常数据计数时保留在原始规模统计里，但后续 KPI 计算只用清洗后数据。

2. 清洗后（花名册去重且 salary > 0，KPI 表剔除非法记录，反馈表剔除非法记录），找出 revenue 最高的“月-部门”组合，给出 month、dept、revenue。

3. 清洗后找出 sla_rate 最低的“月-部门”组合，给出 month、dept、sla_rate。

4. 在去重并清洗后的员工花名册中（仅用 salary > 0 的记录），计算全体员工的平均 salary、中位数 salary，以及 Engineering 部门的平均 salary。

5. 在清洗后的反馈数据中，统计 positive / neutral / negative 的条数，以及 positive 占比。

6. 在清洗后的反馈数据中，找出 negative feedback 数量最多的前 2 个 topic，给出 topic 和 count。

7. 识别跨源冲突：说明 2024‑03 的 Support revenue 异常（与 KPI 表中该月 Support 的 revenue 相关），以及该月 Support 负面反馈是否同步增加；把这两个数字都写出来（Support revenue 值、Support negative 反馈条数）。

8. 从 QA_log_big.txt 中定位并汇总以下 6 类关键审计事件的出现次数（只统计包含明确关键短语的行，不要把普通 INFO 行算进去）：negative salary、education.num 不一致、impossible sla_rate、duplicate employee_id、negative tickets、revenue spike suspected。

9. 在去重并清洗后的员工花名册中，找出平均 salary 最高的部门，给出 dept 与 mean_salary。

10. 在清洗后的反馈数据中，找出 median score 最高的部门，给出 dept 与 median_score。

清洗与计算规则（必须严格执行）：
- 员工花名册去重：以 employee_id 去重，保留最后出现的一条。salary ≤ 0 视为无效并在异常统计中计数，但仍保留在原始规模统计里；age 不在 18–70 之间视为异常；education.num 仅接受 {9,10,12,13,14,16}，否则计为不一致。所有均值、中位数等 KPI 计算仅使用“去重后且 salary > 0”的记录。
- KPI 表：month 必须满足 YYYY-MM 且月份合法（如 2024-00 或 2024-13 非法）；sla_rate 必须在 [0,1] 内（含边界）；tickets 必须 ≥ 0。任何违反条件的记录都要在异常统计中计数，且不参与 KPI 计算。所有“月-部门”汇总都按清洗后数据分组。
- 反馈表：month 必须满足 YYYY-MM 且月份合法；score 必须在 1–5 范围内；dept 中的 “Eng” 视为 “Engineering”（请用 reference.db 确认别名，若没有则默认 “Eng” = “Engineering”）。所有有效反馈才进入统计。
- 日志文件：只统计包含明确关键短语的行，按短语计数；短语即为第 8 条列出的六个短语（忽略大小写，但完全匹配即可）。
- 结果数字四舍五入到 2 位小数（计数除外）。若同一指标出现并列，按 month、dept 或 topic 的字典序升序打破并列。
- 简报中必须明确写出你如何在三类来源之间进行核对：哪些异常在日志里被证实、哪些只在结构化数据里出现、哪些存在口径冲突。简报要体现 3–4 条独立分析轨道后再做统一结论，而不是只给结论列表。
```

### 837. D3_g1193_zh (domain=D3, difficulty=7)

```
我需要你基于以下三个数据文件做一份数据审计简报：survey_data.xlsx（原始调查数据）、occupation_ref.xlsx（职业对照表）、external_pop.xlsx（外部基准数据）。请先检查数据质量，找出所有异常记录（比如缺失职业、无效fnlwgt、重复行、年龄异常、逻辑矛盾等），然后清洗数据，计算清洗后每个职业的平均收入，列出最高的三个职业；再按年龄组计算平均收入率，与外部基准对比，找出偏差超20%的年龄组。最后把结果整理成一份分析简报analysis_brief.md，里面要包含一个汇总表格。
```

### 838. D3_g980274_en (domain=D3, difficulty=7)

```
We have customer data from different departments stored in the inputs/ folder. I need a consolidated report that cleans each dataset, detects anomalies, and computes key metrics. Please analyze the demographic data (demographic_data.xlsx), sensor measurements (sensor_measurements.csv), error logs (error_log.txt), the reference guidelines (reference_doc.docx), and system configuration (config.json). Then produce a findings.md file that includes a summary of data quality issues, key KPIs, anomaly counts, and a cross-source reconciliation section highlighting any discrepancies between documented guidelines and the config file. Make sure to note conflicts explicitly.
```

### 839. D3_g980389_zh (domain=D3, difficulty=7)

```
我要你帮忙处理三个数据集，它们在 data_mart.xlsx 里（分别是 adult、shellfish、wine 工作表）。请把每个数据集清洗一遍，找出那些异常值（比如年龄不符合常识、重量为负、酸度超范围等等），然后对照同目录下的 quality_report.pdf 里的质量标准，看看哪些数据和标准对不上号。最后把所有发现汇总成一个 findings.md 文件，里面要写清楚每个数据集的清洗结果、异常个数和类型，以及跨来源的不一致点。
```

### 840. D3_k982107_zh (domain=D3, difficulty=7)

```
请基于文件 usdot__pipeline-accidents__database.csv 做一份面向管理层的时序/趋势分析，重点看事故在不同年份的变化、近年异常波动、以及与事故严重性相关的时间演变。请围绕这些真实字段展开：Accident Year、Accident Date/Time、Unintentional Release (Barrels)、Net Loss (Barrels)、Liquid Recovery (Barrels)、All Costs、Cause Category、Pipeline Type、Accident State、Pipeline Shutdown、Liquid Ignition、Public Evacuations、All Injuries。希望你输出可直接给业务汇报用的结论，并且把分析拆成可并行推进的多个部分，最后汇总成一个 analysis_summary.json。请特别关注按年份的事故数量、泄漏量、损失、成本的同比/环比变化，以及主要原因类别随时间的结构变化；如果有明显的峰值、拐点或结构性变化，请说明对应年份和可能的业务含义。
```

### 841. D3_k982245_zh (domain=D3, difficulty=7)

```
请基于文件 open-source-sports__professional-hockey-database__Scoring.csv 做一份面向业务决策的冰球进攻表现分析，重点围绕“排名与集中度”展开：找出哪些球员、哪些赛季、哪些球队/位置对总得分贡献最集中，Top-N 是否占据了大部分产出，以及是否存在明显的帕累托特征。请结合字段 playerID、year、stint、tmID、lgID、pos、GP、G、A、Pts、PIM、+/-、PPG、PPA、SHG、SHA、GWG、GTG、SOG、PostGP、PostG、PostA、PostPts、PostPIM、Post+/-、PostPPG、PostPPA、PostSHG、PostSHA、PostGWG 等，输出一份可直接给管理层看的分析结论。请把工作拆成 4-6 个彼此独立的分析轨道，分别从：1）历史总产出排名与集中度；2）单赛季 Top 球员集中度；3）球队层面的得分集中度；4）位置维度的集中度差异；5）常规赛与季后赛的产出集中度对比；6）高产出球员的出场与效率关系。请在结论中明确指出 Top 10、Top 20、Top 5% 等群体占比，以及是否满足/接近 80/20 现象，并给出适合落地到 BI 看板的指标口径。
```

### 842. D3_k982475_zh (domain=D3, difficulty=7)

```
请基于文件 syedanwarafridi__vehicle-sales-data__car_prices.csv 做一份面向业务的车辆成交数据分析，重点围绕“相关性与驱动因素分析”展开：先判断 sellingprice、mmr、condition、odometer、year 这些数值字段之间谁和谁最相关，再找出成交价最可能受哪些因素驱动。请结合真实字段 year、make、model、body、transmission、state、condition、odometer、mmr、sellingprice、saledate 做一个可落地的 BI 分析结论。具体希望拆成 4-6 个互相独立的分析方向：例如总体数值相关性、按品牌/车型的价格驱动差异、里程与车龄对成交价的影响、condition 与 mmr/sellingprice 的关系、不同 transmission/body 的价差，以及缺失值或异常值对相关性的影响。最后请输出一个简洁的分析摘要（analysis_summary.json），并给出适合管理层阅读的关键结论、可执行建议和需要进一步跟进的数据问题。
```

### 843. D3_k982751_zh (domain=D3, difficulty=7)

```
请基于文件 utkarshtomar736__ipl-mens-cricket-matches-data-2008-2023__match_data.csv 做一份面向 BI/运营的多阶段分析，重点围绕时间趋势与赛季变化：我想看 2008–2023 各赛季的比赛/球员/球队表现是如何变化的，尤其是得分效率、边界得分占比、失误球（extras）趋势、以及关键球员和场地在不同年份的波动。请把结果整理成可交付给管理层的分析摘要，并确保所有结论都能追溯到数据字段（如 season、start_date、venue、innings、ball、batting_team、bowling_team、striker、bowler、runs_off_bat、extras、wides、noballs、wicket_type、player_dismissed 等）。
```

### 844. D3_k982763_zh (domain=D3, difficulty=7)

```
请基于文件 dikisahkan__transjakarta-transportation-transaction__dfTransjakarta180kRows.csv 做一份面向业务决策的复杂分析，重点围绕“排名与集中度（Top-N、头部占比、Pareto）”展开。先帮我识别这批交易里最集中的几个维度：哪些走廊（corridorID / corridorName）、哪些支付银行（payCardBank）、哪些乘客性别（payCardSex）、哪些发卡年份（由 payCardBirthDate 反推年龄也可以）、哪些上下车站点（tapInStopsName / tapOutStopsName）最集中。然后把“金额集中度”和“频次集中度”分开看：例如按 payAmount 汇总的头部走廊、头部银行、头部站点分别贡献了多少总金额，以及它们的交易量占比。再进一步检查高金额交易是否也更集中于某些走廊/站点组合，看看是否存在明显的 Pareto 现象。最后，请把结果整理成可以给管理层看的简短结论，并输出一个 analysis_summary.json，里面至少包括各维度 Top 5、Top 3 贡献占比、以及你认为最值得关注的集中风险点。
```

### 845. D3_k983716_zh (domain=D3, difficulty=7)

```
请基于文件 manishabhatt22__marketing-campaign-performance-dataset__marketing_campaign_dataset.csv 做一份偏 BI/经营分析的深度解读，重点围绕“分布与阈值分层”来判断营销活动质量：请按 Conversion_Rate、ROI、Acquisition_Cost、Clicks、Impressions、Engagement_Score 这些字段，识别高于/低于业务阈值的活动占比、分位数分层、以及不同层级的构成占比；同时结合 Company、Campaign_Type、Channel_Used、Target_Audience、Location、Language、Customer_Segment、Date 做交叉拆解，找出哪些细分组合更容易落入高转化/高ROI/低成本/高互动的 cohort。请输出可直接用于管理层汇报的结论框架，不要只做单点统计，要拆成若干相互独立的分析轨道，便于并行处理和汇总。请至少覆盖：总体阈值达标率、分位桶分布、阈值人群/活动画像、渠道与活动类型 mix share、以及按月或按日期的分层变化。数据列以实际 CSV 为准，所有分析必须严格基于该文件中的真实值。请给出可执行的 pandas 口径，并输出便于复核的结果清单。
```

### 846. D3_k983836_en (domain=D3, difficulty=7)

```
Using the file arunavakrchakraborty__australia-weather-data__Weather Training Data.csv, run a real BI-style weather risk analysis focused mainly on temporal/sequence effects using the row ID as the ordered sequence. I need you to quantify how RainTomorrow changes across the sequence, identify any period-over-period shifts in rain risk, and connect those shifts to the weather drivers in the available columns. Please split the work into independent tracks so different analysts can work in parallel: one track on overall RainTomorrow trend by sequence buckets, one on changes in RainToday vs RainTomorrow behavior over the sequence, one on the strongest weather-condition signals tied to rain outcome, one on location-level differences in rain risk, and one on missing-data patterns that could bias trend interpretation. Use only the real columns in the dataset: row ID, Location, MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, WindGustDir, WindGustSpeed, WindDir9am, WindDir3pm, WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Cloud9am, Cloud3pm, Temp9am, Temp3pm, RainToday, RainTomorrow. I need a concise deliverable and a deterministic QA pack with exact numeric checks.
```

### 847. D3_k983967_zh (domain=D3, difficulty=7)

```
请基于文件 vinothkannaece__sales-dataset__sales_data.csv 做一份面向管理层的销售 BI 分析，重点围绕“排名与集中度”展开：找出销量、销售额、折扣和渠道/区域/人员维度上的头部集中现象，判断是否存在明显的 Pareto 结构，并识别最值得关注的高贡献组合。请结合这些真实字段一起分析：Product_ID、Sale_Date、Sales_Rep、Region、Sales_Amount、Quantity_Sold、Product_Category、Unit_Cost、Unit_Price、Customer_Type、Discount、Payment_Method、Sales_Channel、Region_and_Sales_Rep。不要只做简单汇总，我需要能直接用于汇报的结论框架：哪些 Top-N 组合贡献最大、头部占比有多高、集中度是否过高、以及不同维度之间的集中是否一致。请把分析拆成多个相互独立的 track，便于并行推进，最后输出可落地的管理建议。
```

### 848. D3_k984375_zh (domain=D3, difficulty=7)

```
请基于文件 sameerk2004__global-college-statistics-dataset__College Data.csv 做一份面向管理层的 BI 分析，重点围绕“趋势/变化”来判断高校表现是否在不同阶段发生了变化。请你先把数据按一个合理的序列维度整理成可分析的趋势口径（例如按 Country、Branch、Sports、College ID 的排序序列，或按你认为最稳妥的分组顺序），然后重点回答：1）不同国家、不同院系、不同运动偏好的高校，在 CGPA、Placement Rate、Research Papers Published、Faculty Count 上是否呈现出明显的阶段性差异；2）这些指标在序列上的变化是否存在“前后段”或“高低分位”差异；3）哪些国家/专业/运动类别的近端与远端表现差距最大；4）这些趋势是否能解释学生规模、家庭收入与就业率之间的联动关系。请输出一份可直接用于汇报的结论摘要，并把关键对比结果整理成结构化 JSON，便于我后续接仪表盘。
```

### 849. D4_g1326_en (domain=D4, difficulty=7)

```
I need a clean audit pack from inputs/articles.jsonl, inputs/translation_memory.csv, inputs/review_log.sqlite, and inputs/editorial_brief.md. Give me compact deliverables only: one JSON summary, one CSV table, and one MD memo; use the brief’s required sections and the usual counts/rates with the freshness window 2024-02-01 through 2024-06-30, near-duplicates at Jaccard >= 0.72 across languages only, and the standard keyword list from the brief.
```

### 850. D4_g1350_zh (domain=D4, difficulty=7)

```
请基于 inputs/content_inventory.csv、inputs/localization_qa.csv、inputs/campaign_performance.csv、inputs/article_excerpts.txt 和 inputs/content_sources.sqlite 做一份 cross-source 分析简报，输出 findings.md 和 evidence_table.csv。我需要 4 条并行分析线：内容库存概览、QA 问题分布、投放表现、以及 excerpts 里的重复/异常线索；最后要把冲突和对不上口径的地方单独列出来。计数口径请固定：status 只看 published/draft/localized/needs_review/rejected 这 5 类，QA 只统计 passed=0 的记录，严重级别 high 记为高风险，表现分数用 0.5*CTR + 0.3*CVR + 0.2*ROAS（CTR=clicks/impressions，CVR=conversions/clicks，ROAS=revenue_usd/spend_usd），只算 spend_usd>0 且 impressions>0 的行；日期窗口统一按 2025-01-01 到 2025-03-31（含首尾）。
```

### 851. D4_g980217_zh (domain=D4, difficulty=7)

```
我们最近收到一批英文新闻文章和其中文机器翻译版本，需要快速评估本地化质量。请对以下五个文件进行分析：英文文章（English_articles.xlsx）、中文翻译（Chinese_articles.xlsx）、风格指南（Style_Guide.xlsx）、审核日志（Review_Logs.xlsx）以及原始语料库（Original_English_Source_Corpus.json）。目标是生成一份综合性的分析简报（findings.md），内容包括：文章结构完整性（是否缺失标题、作者、日期）、可读性指标（英文Flesch分数、中文字数是否在200-1000范围内）、关键词覆盖情况（提供的列表）、重复内容检测（精确和近似）以及本地化一致性（段落数、链接数差异）。需要将各分析结果交叉验证，并指出任何冲突。请使用风格指南中的阈值和定义。
```

### 852. D4_g980505_zh (domain=D4, difficulty=7)

```
我需要你帮忙做一份内容分析简报。输入文件在 inputs 文件夹里：source_articles.xlsx 是原始文章，review_comments.xlsx 是编辑评审意见，localization_versions.xlsx 是翻译版本，keyword_coverage.xlsx 是关键词覆盖情况，section_requirements.xlsx 是文章结构要求。请综合这些数据，写一个 findings.md，汇总关键指标，比如文章数量、可读性、评审冲突、本地化异常、关键词覆盖等等。特别要注意那些异常情况。具体规则你那边应该都有。谢谢。
```

### 853. D4_g981817_en (domain=D4, difficulty=7)

```
I need a single findings.md brief based on content audit work over content_sources.xlsx and task_support.json. Please organize it into four sections: an executive summary, a content inventory, a label-and-domain audit, and a cross-source reconciliation with a short anomaly log. I want the report to reconcile the two sources, call out duplicate normalized-body rows, and note any missing or malformed support fields that affect the review. Please keep the document compact and factual, with the counts and coverage results clearly stated.
```

### 854. D4_k981827_en (domain=D4, difficulty=7)

```
Using `inputs/bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv`, analyse publication trends over time for the BBC articles dataset. The file has `title`, `pubDate`, `guid`, `link`, and `description`. I need a content/editorial analytics readout focused on temporal patterns: how publishing volume changes by month/quarter/year, which days and hours are strongest, whether major URL sections such as news vs sport show different momentum, how recurring formats like “The Papers” behave over time, and whether headline/description themes shift across the covered period. Keep the work evidence-based and reproducible, and return the key outputs in `analysis_summary.json`.
```

### 855. D4_k981873_zh (domain=D4, difficulty=7)

```
请基于文件 chanemo__weibo-hot-searchlabeled__weibo-hot-search-labeled.csv 做一份面向内容/编辑运营的深度分析，重点看“热搜词条”在不同“标签（时政、科技、科普、娱乐、体育、社会讨论/话题、时事、经济）”上的共现规律、相关性和驱动因素。数据列只有“日期”“热搜词条”“链接”“标签（时政、科技、科普、娱乐、体育、社会讨论/话题、时事、经济）”，请不要做任何预测或建模，只做可复核的描述性分析。请按下面 4-6 个互相独立的分析方向拆分：1）按日期和标签的热搜分布与波动；2）标签之间的相关性/共现强度（重点看可量化指标，输出四舍五入后的相关系数或关联度排序）；3）高频词条与其标签偏好，识别最容易带来某类标签的内容主题；4）异常高集中日期/标签组合（例如某几天某类标签明显放大）及其代表词条；5）编辑策略启示：哪些标签组合最稳定、哪些最容易被单一事件驱动。请输出一份结构化结论，并给出可复核的统计结果。请把分析尽量围绕“相关性 & 驱动因素”展开，回答中要明确指出哪些数值字段/统计量是一起变化的、相关性最强的配对、以及最值得关注的前几组关联。
```

### 856. D4_k982183_zh (domain=D4, difficulty=7)

```
请基于文件 sentinel3734__neurologica-blog-posts__neurologica_articles.csv 做一套偏“内容 / 编辑分析”的深度拆解，重点围绕“分布与阈值分层”来做：我想知道这批文章在 publication_date、title、author、categories、text、url 这些字段下，哪些内容主题/作者/时间段明显超出业务阈值，哪些又明显低于阈值，以及不同分层里的占比结构。请把分析拆成 4-6 条彼此独立的轨道，适合分给多个子分析员并行跑。重点至少包括：1）按年/月的内容产出分布和极端高产低产时段；2）按作者的产出长尾分布、Top 作者集中度、以及达到某个数量阈值的作者占比；3）按 categories 的主题分布，做量化分层（例如按文章数四分位/阈值桶）和份额；4）按文本长度的分布、阈值分层（短/中/长/超长）与占比；5）如果可能，再看标题长度或 URL 结构相关的分布阈值。请输出适合管理层阅读的结论要点，并保留可复算的统计口径。不要编造字段含义；publication_date 需要先解析为日期。请同时给出适合我交给子团队的分析轨道拆分建议，以及一份可落地的数据核对清单。
```

### 857. D4_k982401_zh (domain=D4, difficulty=7)

```
请基于文件 chanemo__weibo-hot-searchlabeled__weibo-hot-search-labeled.csv 做一份面向内容/编辑分析的多维诊断，重点围绕“时间趋势和周期变化”展开。数据字段只有 日期、热搜词条、链接、标签（时政、科技、科普、娱乐、体育、社会讨论/话题、时事、经济）。我需要你把 1500 条热搜按时间拆开看，判断不同标签在不同时间段的变化、峰值、连续上榜特征，以及内容结构是否在月内/周内发生明显迁移。请把结论整理成 analysis_summary.json。请至少覆盖：总体按日期的热度分布、按标签的时间走势对比、周内周期性、月内前后期变化、各标签峰值日期和峰值强度、以及高频词条的持续性/重复性分析。结果要能直接支持编辑选题排期和热点预警。
```

### 858. D4_k982444_zh (domain=D4, difficulty=7)

```
请基于文件 kuberiitb__indian-news-articles__historic_articles.csv 做一份面向编辑/内容运营的深度分析，重点看不同分组之间的表现差异，帮我找出最值得优化的内容与来源组合。请直接使用这些列：source、category、link、author、published_at、header、subheader、content。我的目标不是泛泛总结，而是要回答：不同 source 和 category 之间在文章长度、发布时间分布、作者覆盖、标题/副标题风格上是否存在显著差异，以及哪些分组的内容更“长”、更“短”、更“稀疏”、更“密集”。请把分析拆成几个互不依赖的部分，分别产出可执行结论：1）按 source 和 category 比较文章量、平均内容长度、平均标题长度、平均副标题长度，找出差距最大的分组；2）看不同 category 在不同 source 中的覆盖是否均衡，找出偏科最严重的组合；3）分析发布时间（按月份/星期几/小时）在不同 source 或 category 之间的集中度差异，找出最明显的时段偏移；4）统计作者覆盖度与专栏化程度，比较各 source/category 的作者数量、单作者集中度；5）找出最常见的标题与副标题写法特征，并比较不同组的文本缺失率；6）最后给我一个可落地的优先级列表，指出最值得优先深挖的 3 个 source-category 组合及原因。请输出适合我直接转成汇报材料的结论和必要的数值依据。
```

### 859. D4_k983017_zh (domain=D4, difficulty=7)

```
请基于文件 `chanemo__weibo-hot-searchlabeled__weibo-hot-search-labeled.csv` 做一份偏内容/编辑策略视角的热点舆情分析，重点围绕“时间趋势”展开：先看整体热搜在日期维度上的活跃度变化，再比较不同标签（时政、科技、科普、娱乐、体育、社会讨论/话题、时事、经济）在不同时间段的占比、增速和波动，找出哪些类别在某些阶段明显抬升或回落；同时结合热词本身，识别在不同阶段反复出现、以及各标签下最具代表性的关键词。请把结果整理成可交付给编辑/运营团队的分析结论，最好能指出需要重点关注的时间窗口、内容类型迁移，以及潜在的选题节奏变化。
```

### 860. D4_k983138_en (domain=D4, difficulty=7)

```
Using the file thebumpkin__10400-classic-hits-10-genres-1923-to-2023__ClassicHit.csv, build an editorial-quality anomaly review of the catalog using the real columns Track, Artist, Year, Duration, Time_Signature, Danceability, Energy, Key, Loudness, Mode, Speechiness, Acousticness, Instrumentalness, Liveness, Valence, Tempo, Popularity, and Genre. I need a multi-part audit focused mainly on anomaly and outlier detection by explicit numeric rules: flag extreme values using IQR/threshold logic, identify rare categories, and surface unusual combinations that content editors should review. Break it into separate workstreams so different analysts can run in parallel: 1) numeric outlier scan across audio features and popularity, 2) temporal anomalies by Year and Duration, 3) category rarity and genre concentration, 4) artist/track-level repeated anomalies, and 5) suspicious content-pattern combinations (for example very low popularity but extreme audio values, or high speechiness/instrumentalness outliers). Please summarize which records are most unusual and which anomaly rules are triggered most often.
```

### 861. D4_k983255_zh (domain=D4, difficulty=7)

```
请基于文件 eliasdabbas__search-engine-results-flights-tickets-keywords__flights_tickets_serp2019-10-01.csv 做一份面向内容/编辑分析的深度检查，重点放在时间趋势和环比变化上。请围绕 searchTerms、rank、title、snippet、displayLink、queryTime、searchTime、totalResults、count、startIndex 这些字段，分析 2019-10-01 当天不同查询词在 SERP 里的表现变化、结果规模与抓取耗时的关系，以及内容供给侧（不同域名/标题/摘要）在不同搜索意图下的波动。我要你把工作拆成几个彼此独立的分析轨道，能让不同小组并行处理：先看整体时间序列分布，再看按搜索词/意图分组的趋势，再看前排结果和结果总量的变化，再看域名与内容形态的变化，最后做一个简洁的异常与波动清单。输出请以 analysis_summary.json 的结构化结果为目标，不需要图，只要能直接支持编辑和运营讨论的定量结论。
```

### 862. D4_k983318_zh (domain=D4, difficulty=7)

```
请基于文件 banuprakashv__news-articles-classification-dataset-for-nlp-and-ml__business_data.csv（字段：headlines, description, content, url, category）做一份面向内容/编辑分析的深度诊断，重点放在时间/序列趋势分析上：我想知道这批 business 类文章在发布时间序列上的热度变化、篇幅变化、标题/摘要/正文的长度趋势、重复或近重复内容是否在某些阶段集中出现，以及不同文章特征之间的周期性关联。请把分析拆成几个彼此独立的部分，最后输出一份可直接给编辑/内容团队看的结论摘要，重点标注任何明显的环比/阶段性变化、异常高发区间，以及可执行的编辑策略建议。请务必只使用该数据集中的真实值，不要补充外部信息。
```

### 863. D4_k983436_zh (domain=D4, difficulty=7)

```
请基于文件 raedaddala__top-500-600-movies-of-each-year-from-1960-to-2024__final_dataset.csv 做一份面向内容/编审的多维分析，重点围绕“分布与阈值分层”来回答业务问题：先把影片按评分、元评分、时长、投票量、票房等指标做阈值分组和分位数分桶，再看不同桶内的影片构成、缺失情况、类型/语言/国家的混合结构，以及高表现影片的内容特征。请输出一份可落地的 analysis_summary.json，要求结论尽量量化、可比较、能直接给编辑选片或内容运营参考。请至少拆成 4-6 个彼此独立的分析轨道，分别覆盖：1) 评分/元评分阈值 cohort 的规模与占比；2) 投票量与票房的分位数桶和头部集中度；3) 时长阈值下的内容分层与类型差异；4) 高分但低元评分、以及高元评分但低分的“偏离”影片画像；5) 缺失值与可用性检查（预算/开画/票房/元评分等）；6) 国家、语言、类型在头部 cohort 中的 mix share。请在结论中明确哪些阈值最能区分高质量/高热度影片，哪些类别最值得优先内容投入。
```

### 864. D4_k983465_zh (domain=D4, difficulty=7)

```
请基于文件 kuberiitb__indian-news-articles__historic_articles.csv 做一份面向内容/编辑分析的深度诊断，重点围绕发布时间（published_at）的时间趋势来拆解。请结合 source、category、author、header、subheader、content 这些字段，回答：1）不同来源和栏目在不同时间段的发文节奏是否发生了明显变化；2）疫情前后或月度/季度层面的发文量、平均内容长度、标题/副标题缺失率有没有趋势性变化；3）各来源和栏目在高峰期与低谷期的结构是否不同；4）作者维度是否存在稳定高产作者及其发文节奏变化；5）标题长度、正文长度、发布时间之间是否存在时间相关的内容形态变化。请把分析拆成多个可并行的独立轨道，输出可直接交付的分析摘要（analysis_summary.json）。
```

### 865. D4_k983547_zh (domain=D4, difficulty=7)

```
请基于文件 thebumpkin__300-world-music-tracks-with-spotify-data__WorldHits.csv 做一份面向内容/编辑分析的深度诊断，重点围绕“排名与集中度”展开：先找出哪些艺人、年份、专辑和曲目在这 326 首世界音乐里最集中、最能代表头部；再量化 top-N 对总播放热度（Popularity）和曲目数量的占比，以及是否存在明显的 Pareto 现象。请把分析拆成 4-6 个相互独立的子任务，便于并行推进；同时请结合 Track、Artist、Album、Year、Popularity，以及 Danceability、Energy、Acousticness、Instrumentalness、Valence 等音频特征，判断头部内容是否在风格上也更集中。最终输出适合编辑团队决策的结论摘要和可执行建议。
```

### 866. D4_k983617_zh (domain=D4, difficulty=7)

```
请基于文件 thedevastator__youtube-trending-videos-dataset__youtube.csv 做一份面向内容/编辑分析的深度拆解，重点围绕“排名与集中度”来回答：哪些频道、国家、类别、标签在趋势热视频里占据了绝大部分曝光和互动？请同时从频次和影响力两个角度看 Top-N、总量占比、以及是否存在明显的 80/20 或头部集中现象。需要结合真实列：channel_title、publish_country、category_id、title、tags、views、likes、dislikes、comment_count、trending_date、published_day_of_week、time_frame、comments_disabled、ratings_disabled、video_error_or_removed。请把分析拆成 4-6 个彼此独立的轨道，分别覆盖：1）频道头部集中度与长尾分布；2）国家/地区的趋势热视频份额与头部集中度；3）类别维度的排名、份额和互动贡献；4）标签/标题关键词的高频与高影响力内容聚类；5）按发布时间维度（星期几、时段）的集中度与峰值；6）互动行为（点赞/评论/禁评/禁评率）与头部内容的关系。最终请输出一份可直接给编辑团队决策的 summary，并明确指出有哪些最值得持续追踪的头部群体和分发窗口。
```

### 867. D4_k983677_en (domain=D4, difficulty=7)

```
Using the file samithsachidanandan__1000-most-trending-youtube-videos__top-1000-trending-youtube-videos.csv, build a content/editorial analytics readout focused mainly on anomaly and outlier detection using explicit numeric rules. I need you to flag unusually extreme videos and categories in a way I can hand to editors. Please work from the real columns rank, Video, Video views, Likes, Dislikes, Category, and published only. Decompose the work into separate analysis tracks so different people can work in parallel: 1) define numeric outlier rules for views/likes/dislikes and identify the most extreme videos, 2) look for suspicious or rare category patterns and category-level concentration, 3) compare performance by published year to spot year-level anomalies, 4) quantify missingness and data quality issues in the engagement fields/category field, 5) check consistency between views and engagement metrics for unusually high or low engagement ratios, and 6) summarize a concise editorial action list for what should be reviewed first. Use deterministic thresholds and explicit rules (e.g. IQR-based fences, percentile cutoffs, rare-category counts, and extreme top/bottom rankings).
```

### 868. D4_k983716_zh (domain=D4, difficulty=7)

```
请基于文件 thebumpkin__10400-classic-hits-10-genres-1923-to-2023__ClassicHit.csv 做一份面向内容/编辑运营的分析，重点围绕“分布与阈值分层”来判断不同类型经典歌在编辑选题、栏目分发和推荐池里的结构差异。请你围绕真实字段（Track、Artist、Year、Duration、Time_Signature、Danceability、Energy、Key、Loudness、Mode、Speechiness、Acousticness、Instrumentalness、Liveness、Valence、Tempo、Popularity、Genre）完成一个可直接用于汇报的 analysis_summary.json。核心希望你回答：1）哪些流行度阈值/分位桶最能区分不同 Genre 的内容供给；2）不同 Genre 在高/中/低热门、长/短时长、快/慢节奏上的覆盖和占比；3）跨年份的热门门槛是否在变化；4）哪些特征组合最适合做编辑精选/怀旧/高能/低语音等栏目池。请把分析拆成多个互相独立的轨道，便于并行推进，并在最终摘要里给出每个轨道的关键数字、阈值口径和一句编辑结论。
```

### 869. D4_k983736_en (domain=D4, difficulty=7)

```
Using kimjihoo__coronavirusdataset__SeoulFloating.csv, build a content/editorial analytics readout focused on ranking and concentration in Seoul floating-population activity. I need a concise but decision-ready analysis that identifies the top cities, demographic segments, and date/hour windows by floating population, and quantifies how concentrated the total is in the top groups (top-N share, Pareto-style concentration, and whether a small set of segments drives most of the volume). Please decompose this into separate workstreams so different analysts could work independently: one on city concentration, one on demographic concentration by sex and birth year, one on temporal concentration by date and hour, one on province-level concentration (even if it is mostly Seoul), and one on combined segment ranking (city x demographic or city x time). Use the actual columns date, hour, birth_year, sex, province, city, and fp_num only. Return the final output as analysis_summary.json with clear rankings, shares, and short editorial takeaways.
```

### 870. D4_k983903_zh (domain=D4, difficulty=7)

```
请基于文件 glushko__seth-godins-blogs-dataset__seth-data.csv 做一份面向内容/编辑分析的相关性与驱动因素分析报告，重点看这些数值字段之间到底谁和谁一起变化：stars、发布时间（publication-date 需要先转成日期后再拆成年/月/星期/季度/是否周末等特征）、以及文章发布时间的长期趋势。请结合 title、content_plain、content_html 做必要的文本长度派生指标（例如字符数、词数、HTML 与纯文本长度差），找出和 stars 关联最强的指标、相关性排名、以及几个最值得编辑团队关注的信号。请把结论整理成可直接交付的 analysis_summary.json，要求结论尽量具体、可复核、少主观判断。由于我很忙，请把工作拆成多个彼此独立的分析轨道并并行推进。
```

### 871. D4_k983948_zh (domain=D4, difficulty=7)

```
请基于文件 roman6335__13000-itunes-podcasts-april-2018__poddf.csv 做一份面向内容/编辑分析的多维诊断，重点放在“时间/序列趋势”的视角上。虽然这份数据没有明确日期，但我希望你把 index 视为采样顺序/发布顺序的代理序列，分析不同内容类别在该序列上的评分变化、评分量变化、以及低质量内容是否在后段更集中。请结合 Name、Rating_Volume、Rating、Genre、Description 这几列，拆成几个彼此独立的分析轨道，最后输出能给编辑和选题团队直接使用的结论摘要与异常清单。请特别关注：1）按序列分段后的评分均值和评分量均值变化；2）各 Genre 的评分趋势差异；3）高评分但低评分量、或低评分但高评分量的内容是否集中在某些序列段；4）描述文本长度与评分/评分量的关系；5）缺失值与 Not Found 是否在某些序列段异常集中。请直接给我可执行的分析检查项和结论验证点。
```

### 872. D4_k983994_zh (domain=D4, difficulty=7)

```
请基于数据文件 abdallahwagih__books-dataset__data.csv 做一份面向内容/编辑分析的联合诊断，重点放在“数值字段之间的相关性与驱动因素”上。数据里我关心的核心字段是 published_year、average_rating、num_pages、ratings_count，以及分类字段 categories、authors、title、subtitle、description、thumbnail。请不要只做单一结论，而是拆成多个彼此独立的分析轨道，帮我回答：哪些数值指标彼此同步变化最明显；哪些类别/作者更像是高评分、高讨论度、长篇幅书；年份是否会影响评分、页数或热度；以及在标题/副标题/简介缺失、分类缺失时，这些数值关系会不会变弱。最后请把最关键的相关系数、Top 关联对、以及按类别/作者分组后的驱动信号整理成一个可供编辑团队直接阅读的结论摘要。
```

### 873. D4_k984172_zh (domain=D4, difficulty=7)

```
请基于文件 chanemo__weibo-hot-searchlabeled__weibo-hot-search-labeled.csv 做一份偏“内容/编辑运营视角”的热点趋势分析，重点围绕【时间趋势】展开。字段只有 日期、热搜词条、链接、标签（时政、科技、科普、娱乐、体育、社会讨论/话题、时事、经济），请不要改动数据。我要你把分析拆成 4-6 个彼此独立的方向，最好能让不同人并行做：1）整体按日期的热点量变化与峰谷日期；2）不同标签在时间上的占比变化、周/月节奏和增速；3）关键时间窗口里各标签的环比/同比式波动（按周对比即可）；4）高频热点词条的重复出现与跨日持续性；5）不同标签的发布时间集中度与尾部日期表现；6）如果能做，再补一个日期维度上的内容结构变化结论。最后请输出一个可用于汇报的 analysis_summary.json，里面要能直接看到趋势结论、异常点和运营建议。请注意所有结论都必须严格基于这份表，不要编造。
```

### 874. D4_k984191_en (domain=D4, difficulty=7)

```
Using stackoverflow__stack-overflow-2023-developers-survey__survey_results_public.csv, build a content/editorial analytics brief focused mainly on ranking and concentration patterns in the survey responses. I need 4-6 independent tracks that a small team can work on in parallel: (1) rank the most common audience segments and how concentrated the sample is in the top groups, (2) analyze which learning content sources and online resources dominate, including top-N shares and Pareto-style concentration, (3) rank the most common technical stacks used and wanted across languages/databases/frameworks/platforms, (4) compare where respondents get and want AI/tooling content, including the most common choices and how concentrated preferences are, (5) summarize country-level concentration among the largest respondent markets, and (6) optionally compare compensation concentration for the most represented segments using CompTotal and ConvertedCompYearly where available. Please keep the outputs decision-oriented, with clear top groups, shares of total, and any notable concentration ratios or top-3/top-5 shares.
```

### 875. D4_k984219_zh (domain=D4, difficulty=7)

```
请基于文件 rishidamarla__podcasts-episodes-20072016__shows.csv 做一份内容/编辑分析，重点围绕“排名与集中度”展开：先找出哪些播客栏目在样本里最集中、最头部，哪些分类/子分类和语言最偏向头部集中，再看这些头部栏目在作者、explicit 标记、创建时间等维度上是否有明显特征。请把结果做成适合管理层快速决策的摘要，尤其要回答：Top-N 频道占了多少比例、前 10/20 是否形成明显的长尾/二八集中、不同分类和语言的头部占比差异、以及头部内容是否更容易出现某些属性。字段只用这张表里的真实列：id, feed_url, title, subtitle, description, summary, author, email, link, language, explicit, image, category, subcategory, created_at, last_build_date。请拆成多个相互独立的分析轨道，方便并行推进。
```

### 876. D4_k984246_zh (domain=D4, difficulty=7)

```
请基于文件 kimjihoo__coronavirusdataset__SeoulFloating.csv（字段：date、hour、birth_year、sex、province、city、fp_num）做一份面向内容/编辑分析的多部分研究，重点围绕“相关性与驱动因素分析”：先判断哪些数值字段之间联动最明显，再找出影响 fp_num 的主要结构性因素，并把结果整理成可直接给编辑团队看的结论。请把分析拆成多个彼此独立的轨道，便于并行推进：1）整体相关性与最强关联对（包括 round 后的相关系数排序）；2）按性别、年龄段、小时的 fp_num 差异与驱动方向；3）高浮动/低浮动的城市（city）及其与人口属性的联动；4）日期维度上 fp_num 与时间变量（hour、birth_year）的关系是否稳定；5）筛选若干核心细分群体，查看它们在高低 fp_num 区间的分布差异。最后输出一个简洁的结论摘要，说明最值得编辑侧关注的驱动因素和异常组合。
```

### 877. D4_k984324_zh (domain=D4, difficulty=7)

```
请基于文件 sanjidh090__resultpf__bd_eng_news_daily.csv 做一份面向内容/编辑运营的深度分析，重点围绕“排名与集中度”（top-N、头部份额、Pareto/80-20）来判断这批新闻数据的内容分布是否过度集中。请务必使用真实列：title、text、publish_date、urls、news_collection_time、publisher，并把结果整理成 analysis_summary.json。我要你拆成多个彼此独立的分析轨道，便于不同同事并行看：先按 publisher 看头部媒体的覆盖与集中度；再按 publish_date 看按发布时间的日/周/月发布量排行与集中度；再按 title 做标题层面的重复/近重复与头部标题占比；再按 text 长度或正文特征看长短内容是否被少数头部文章垄断；再看 url 域名/来源的集中度（若可从 urls 提取）；最后做一个 Pareto 视角，验证前20%头部来源/标题是否贡献了大部分内容量。请在结论里给出可执行的编辑策略建议，例如是否需要分散来源、提升长尾覆盖、减少标题重复、优化发布时间分布等。
```

### 878. D4_k984395_en (domain=D4, difficulty=7)

```
Using `stackoverflow__stack-overflow-2023-developers-survey__survey_results_public.csv`, build a content/editorial analytics readout focused on distribution and threshold cohorts. I need you to segment respondents by business-relevant cutoffs and quantile buckets, then summarize who over-indexes in different content-editorial signals. Please base this mainly on `Country`, `Age`, `EdLevel`, `YearsCode`, `YearsCodePro`, `Employment`, `RemoteWork`, `CodingActivities`, `LanguageHaveWorkedWith`, `LanguageWantToWorkWith`, `DatabaseHaveWorkedWith`, `WebframeHaveWorkedWith`, `MiscTechHaveWorkedWith`, `News*`/`SO*` fields, `AI*` fields, `SurveyEase`, `SurveyLength`, `ConvertedCompYearly`, and `CompTotal` where available. I want 4-6 independent analysis tracks so this can be split across analysts: 1) threshold cohorts on experience and compensation, 2) quantile buckets for compensation and their content-tooling mix, 3) age/education/career-stage distribution shifts, 4) geography and employment/remote-work mix shares, 5) Stack Overflow / AI usage and sentiment by cohort, and 6) a compact set of editorial recommendations tied to the observed distribution breaks. Please return the findings as a concise analysis summary.
```

### 879. D4_k984396_zh (domain=D4, difficulty=7)

```
请基于文件 thebumpkin__10400-classic-hits-10-genres-1923-to-2023__ClassicHit.csv 做一版面向内容/编辑分析的深度诊断，重点围绕时间趋势与阶段性变化：先按 Year 做全局趋势，再拆到 Genre、Artist 和音频特征层面，找出哪些年代/年份的内容表现、风格结构和用户偏好发生了明显变化。请把结论整理成 analysis_summary.json，并尽量给出可执行的编辑建议（比如哪些年代应该加大选题、哪些风格在近年回升、哪些风格长期下滑）。需要覆盖表中的真实字段：Year、Duration、Danceability、Energy、Loudness、Speechiness、Acousticness、Instrumentalness、Liveness、Valence、Tempo、Popularity、Genre、Track、Artist。不要只做单一维度；请把时间序列变化、分阶段对比、同比/环比式的变化率、以及头部内容与长尾内容的变化都纳入分析。
```

### 880. D4_k984435_en (domain=D4, difficulty=7)

```
Using wardabilal__spotify-global-music-dataset-20092025__track_data_final.csv, do a correlation and driver analysis for content/editorial analytics: identify which numeric fields move together, where the strongest rounded correlations are, and what that implies for track, artist, and album editorial performance. Break it into independent workstreams so different analysts can work in parallel: (1) numeric data quality and coverage for track_popularity, track_duration_ms, artist_popularity, artist_followers, album_total_tracks; (2) full correlation matrix with rounded coefficients and top positive/negative associations; (3) driver analysis of track_popularity against artist_popularity, artist_followers, duration, track_number, and album_total_tracks; (4) segmentation by explicit vs non-explicit and album_type to see whether correlations change; (5) artist-level rollups to find artists whose catalogs show unusually high or low track_popularity relative to follower scale; (6) editorial takeaways that translate the numeric relationships into actionable playlisting and catalog strategy recommendations.
```

### 881. D4_k984436_zh (domain=D4, difficulty=7)

```
请基于文件 abdallahwagih__books-dataset__data.csv 做一份面向内容/编辑分析的深度拆解，重点围绕“排名与集中度”来判断这个书库里的头部内容、头部作者和头部品类是否高度集中，以及头部是否贡献了大部分热度。请结合字段 isbn13、isbn10、title、subtitle、authors、categories、published_year、average_rating、num_pages、ratings_count，完成一份可直接给编辑团队看的分析结论。希望你把任务拆成多个彼此独立的分析轨道，适合并行处理，并最终汇总成一个 analysis_summary.json。请重点回答：1）哪些作者/品类/年份在数量和热度上最集中；2）ratings_count 的头部内容是否符合 80/20 特征；3）高评分、高热度、高页数内容之间是否存在明显集中层；4）头部书单能否作为选题或专题推荐的优先池。
```

### 882. D4_k984438_zh (domain=D4, difficulty=7)

```
请基于文件 algord__fake-news__FakeNewsNet.csv 做一份面向内容/编辑分析的综合诊断，重点围绕“时间/序列趋势”来展开：把 tweet_num 视为内容传播序列变量，分析真实/虚假内容在传播量分布、传播爬升速度、区间变化、来源域差异、以及标题文本特征上的时间序列式变化信号。请输出一份适合编辑团队决策的结论摘要，重点回答：哪些来源域的内容更容易快速获得高传播、真实与虚假内容在不同传播阶段的结构差异是什么、以及这些差异是否稳定。数据列只有 title、news_url、source_domain、tweet_num、real。请将分析拆成多个可并行的部分，并最终给出可执行的内容监测建议。
```

### 883. D4_k984442_zh (domain=D4, difficulty=7)

```
请基于文件 bhavikjikadara__bbc-news-articles__bbc_news_20220307_20240703.csv 做一份面向内容/编辑分析的深度诊断，重点放在“相关性与驱动因素”上：先从 pubDate、title、guid、link、description 这几列里整理出可用于内容运营的时间、文本长度、链接形态等衍生指标，再分析哪些指标彼此同向/反向移动、哪些是最强关联、以及它们在不同年份和不同日期维度上的差异。我要你把任务拆成若干独立分析轨道，最后给我一个适合内部汇报的简洁结论包：1）先做整体数据质量与字段基础画像；2）再做标题/描述长度与发布时间的关联分析；3）再做年份维度的相关性对比；4）再做按星期几和月份的内容节奏分析；5）最后找出最值得关注的 top 关联组合，并解释这些关系对编辑排期和内容生产意味着什么。请尽量输出可落地的判断，而不是泛泛描述。
```

### 884. D4_k984709_zh (domain=D4, difficulty=7)

```
请基于文件 ziya07__seo-web-content-dataset__seo_dataset.csv 做一份面向内容/编辑团队的 SEO 分析，重点围绕“排名与集中度（Top-N、份额、Pareto）”展开。请不要只看平均值，我更想知道哪些内容特征、页面特征和排名结果集中在少数高贡献样本里。请把分析拆成 4-6 个彼此独立的 track，便于分工并行推进：1）按 ranking_improved 和 serp_position_before 做 Top-N / 分位集中度分析，看看提升样本是否在前 20%/前 10% 的 SERP 起始位置上更集中；2）按内容特征做集中度分析，例如 content_length、keyword_density、num_internal_links、num_external_links 的 top groups/分位组贡献份额；3）按站内基础优化信号做覆盖与集中度分析，例如 has_meta_description、has_alt_text 的覆盖率，以及这些组的 ranking_improved 占比；4）按用户行为指标做集中度分析，例如 avg_time_on_page_sec、bounce_rate、scroll_depth_percent 在提升组与未提升组之间的 top-N/分位差异；5）按权威与外链信号做集中度分析，例如 domain_authority、page_authority、backlink_count 的 top decile 贡献和与排名提升的关系；6）做一个简洁的相关性与联合特征分析，找出最可能与 ranking_improved 同向变化的变量，并说明是否存在明显的集中现象。最后请输出一份可直接给管理层看的分析结论摘要，包含“最值得优先优化的少数页面/特征”和“是否符合 Pareto 规律”。
```

### 885. D4_k984739_zh (domain=D4, difficulty=7)

```
请基于文件 thebumpkin__300-world-music-tracks-with-spotify-data__WorldHits.csv 做一份面向内容/编辑分析的综合报告，重点围绕时间趋势和阶段变化来拆解：我想知道这 326 首世界音乐曲目在不同年份段的发行、流行度、音频特征和歌词/可听性相关指标是怎么变化的，以及哪些艺术家/专辑更像是“高表现内容”。请直接用数据回答，不要做泛泛描述。需要结合 Track、Artist、Album、Year、Duration、Time_Signature、Danceability、Energy、Key、Loudness、Mode、Speechiness、Acousticness、Instrumentalness、Liveness、Valence、Tempo、Popularity 这些列，给出可供编辑决策参考的结论。
```

### 886. D4_k984771_zh (domain=D4, difficulty=7)

```
请基于文件 algord__fake-news__FakeNewsNet.csv 做一份面向内容/编辑运营的分析，重点看“传播量与真假标记之间的关联”和“哪些标题/来源特征更容易带来高传播”。数据里只有这几个字段：title、news_url、source_domain、tweet_num、real。请重点围绕 tweet_num 与 real 的相关性、不同真假标签下的传播差异、来源域名的传播表现，以及标题长度/关键词与传播量的驱动关系来做。我要的是能直接支持选题、分发和审校策略的结论，不要泛泛描述。请把结果整理成 analysis_summary.json。分析时请至少拆成 4-6 个彼此独立的轨道，方便并行推进。
```

### 887. D4_k984858_zh (domain=D4, difficulty=7)

```
请基于文件 thedevastator__books-sales-and-ratings__Books_Data_Clean.csv 做一份面向内容/编辑分析的多部分诊断报告，重点围绕时间趋势来展开。请围绕 Publishing Year 识别图书销量、销售额、评分与定价在不同年份的变化规律，找出增长/下滑拐点、年度同比变化最大的年份，以及不同作者评级、语言代码、出版社与 genre 在时间上的表现差异。也请检查是否存在某些年份里高评分但低销量、或高销售额但低 publisher revenue 的异常组合，并给出可行动的编辑选品建议。请把结果整理成 analysis_summary.json。
```

### 888. D5_g141_en (domain=D5, difficulty=7)

```
I need you to put together a compact audit package for a small multi-module Python service. Use these four input files: inputs/codebase_snapshot.json, inputs/config_manifest.json, inputs/test_run.log, and inputs/runtime_events.json. The deliverables should be report_summary.json, findings_table.csv, and remediation_plan.md. The audit needs to cover static code review, production config and dependency risk, test failure triage from the log, and runtime event anomalies—synthesize the results into those three files.
```

### 889. D5_g160_en (domain=D5, difficulty=7)

```
Run a multi-track audit on these files: inputs/billing_api.py, inputs/reports_renderer.py, inputs/auth_prod.ini, inputs/auth_dev.ini, inputs/pyproject.toml, inputs/requirements.txt, inputs/unit_test_log.txt, inputs/integration_log.txt, inputs/audit_index.sqlite. I need synthesized reports covering static code review of billing_api.py, security review of reports_renderer.py, test-failure triage from the log files, and a dependency/config audit across the config files. Output 2–3 compact report files (markdown, CSV, or JSON as appropriate). Keep it concise but actionable.
```

### 890. D5_g272_en (domain=D5, difficulty=7)

```
We need to audit our codebase across several areas: static review of module_a.py, security check of module_b.py, triage test failures from test.log and runtime.log, and a config/dependency audit using module_c.py, prod.ini, dev.ini, and prod.yaml. Please produce a concise findings brief (like a markdown file) with sections for each area, and include a small evidence table showing the key issues and counts. Keep it evidence-backed with file references.
```

### 891. D5_g335_en (domain=D5, difficulty=7)

```
Run a compound codebase and log audit using the following inputs: inputs/app.py, inputs/api.py, inputs/worker.py, inputs/utils.py, inputs/config.prod.env, inputs/config.staging.env, inputs/requirements.txt, inputs/test_failures.log, inputs/app_runtime.log, inputs/security_scan.log. Perform four independent tracks: static security/code review of source files, config/deployment audit (checking production config), test-failure triage from the test log, and runtime/dependency audit from the runtime log and requirements. Synthesize a single ranked remediation brief into decision_brief.md.
```

### 892. D5_g344_zh (domain=D5, difficulty=7)

```
我们工程平台的代码、配置、测试和日志需要做一次并行审计，目的是识别高风险代码模式、生产环境危险配置、测试失败原因，并通过日志交叉验证。请基于 inputs/ 下的 5 个文件完成审计：

- code_snapshot.txt
- config_profiles.xlsx
- test_results.xlsx
- app_runtime.log
- requirements.lock

最终输出 3 份文件：
1. JSON 文件：审计汇总，包含所有定量结果
2. MD 文件：统一的整改与验证计划
3. CSV 文件：问题清单，只列出本次审计范围内命中的问题

请直接开始处理，不需要解释方法，我只要最终结果。
```

### 893. D5_g574_zh (domain=D5, difficulty=7)

```
我需要你对这套小项目做一次并行化的代码库/日志审计，最后只输出 3 个紧凑的汇总文件：audit_summary.json、risk_register.csv、validation_plan.md。请同时查看 inputs/module_app.py、inputs/module_billing.py、inputs/module_auth.py、inputs/settings_prod.py、inputs/settings_dev.py、inputs/requirements.txt、inputs/test_log.txt、inputs/project_meta.sqlite 和 inputs/runtime_2024-05.log。这不是单点修 bug，而是一次合并审计：我希望你把工作拆成互相独立的几个轨道并最终汇总。

我关心的检查范围必须严格按下面的闭集来做，超出范围的不算：
1) 静态安全扫描只统计代码里直接出现这些字面模式的函数或语句：eval(、exec(、pickle.loads、yaml.load(、且不是 SafeLoader、hashlib.md5(、hashlib.sha1(、subprocess.Popen(..., shell=True) 或 subprocess.run(..., shell=True)。如果同一个函数里命中多个模式，按模式分别计数，但同一模式在同一函数里只算 1 次。
2) 配置审计只检查：生产配置文件中出现 DEBUG = True 或 debug=True；SECRET_KEY 长度小于 16；ALLOWED_HOSTS 包含 "*"；requirements.txt 里出现 PyYAML 但版本低于 6.0.0、Django 版本低于 4.2.0、Flask 版本低于 2.2.0。版本比较按语义版本号比较，忽略大小写。
3) 测试日志只看 test_log.txt 中明确写出的失败用例名，统计失败用例总数、其中名字包含 parser/payments/config/crypto 的各自失败数，以及所有失败里是否存在和 runtime_2024-05.log 中同名 test=... 条目对应的重复信号。重复信号的定义是：同一个测试名在 test_log.txt 与 runtime_2024-05.log 都出现至少一次。
4) 运行日志只在 runtime_2024-05.log 中找这 7 类闭集事件：security 扫描命中的 4 个模式、以及 test=... 的 4 个失败条目；另外统计 level=ERROR 的总行数，但只针对这 8 个目标事件附近 1 行窗口内是否同时出现 module=auth、module=billing、module=search、module=cache、module=worker 这几个模块标记，按模块出现次数汇总。窗口的定义就是目标行本身及其上一行、下一行。

我最后要的是：
a) audit_summary.json：给我一个总览 JSON，里面要有各轨道的发现数量、一个按风险优先级排序的整改建议列表，以及一个最终统一修复顺序。风险优先级按这个公式算：severity_score = 3*security_hits + 2*config_hits + 2*failed_tests + duplicate_signals。同分时按字母序排模块名/项目名。json 里每个建议要包含 id、category、evidence、score、priority_rank。
b) risk_register.csv：一行一个发现，至少包含 finding_id、source_file、category、matched_pattern、evidence_snippet、owner_hint、severity_score、recommended_action。只列出上面闭集内命中的发现，不要扩展别的风险。
c) validation_plan.md：给出一个精简但可执行的验证计划，按轨道分段写清楚，我需要能据此安排代码修复、复测和上线前检查。请注意，所有统计都要去重规则明确：同一文件内同一闭集模式重复出现多次只算一次；但不同文件中的同一模式要分别计入。
```

### 894. D5_g90_en (domain=D5, difficulty=7)

```
I need a compound audit of the attached multi-module codebase, logs, and test results. Please perform four parallel analyses: static code review, security/risk review (especially the prod config), test-failure triage, and dependency/config audit. Then synthesize a unified fix-and-validation plan.

Inputs:
- inputs/project/core.py
- inputs/project/auth.py
- inputs/project/db.py
- inputs/project/worker.py
- inputs/project/config_prod.py
- inputs/project/config_dev.py
- inputs/service_tests.log.xlsx
- inputs/test_results.xlsx
- inputs/dependency_audit.xlsx
- inputs/audit.sqlite

What I need from you:
- Count code files containing dangerous patterns (e.g., `eval(`, `exec(`, unsafe deserialization, weak hashes, `shell=True`). List them and the total.
- Count prod config issues in config_prod.py (e.g., DEBUG=True, weak secret key, overly permissive ALLOWED_HOSTS).
- Count dependency rows matching PyYAML 5.1 or openssl 1.0.2.
- Count failed tests; list distinct failing test names (sorted ascending).
- Compute average duration of failed tests (3 decimals).
- Identify top 3 tests by failure count (ties broken alphabetically).
- Count ERROR log entries containing security-related keywords (Traceback, Security warning, unsafe yaml.load(), md5 password hash, pickle restore).
- Count distinct services in the service_tests log.

Deliverables: one JSON summary report, one Markdown synthesis report, and one CSV findings table. Keep them compact and include findings from all tracks.
```

### 895. D5_g980513_zh (domain=D5, difficulty=7)

```
我需要你审一下这批输入文件：inputs/audit_pack.xlsx、inputs/security_config_snippets.txt、inputs/manifest.json。请分别做代码审查、安全风险审查、测试失败归因、依赖/配置审计，然后合成一份排序后的决策简报。
```

### 896. D5_g980562_zh (domain=D5, difficulty=7)

```
我需要你看一下这组代码和日志：inputs/repo_audit.xlsx、inputs/app.log、inputs/test_results.csv、inputs/module_a.py、inputs/module_b.py、inputs/module_c.py、inputs/settings_prod.py。请把静态代码审计、生产配置审计、测试失败日志排查、运行日志异常统计和依赖风险检查合并成一份简短的中文汇总报告，最后给出一个统一的修复与验证计划。
```

### 897. D5_g980667_zh (domain=D5, difficulty=7)

```
这次要做一次上线前的综合审计，目的是把代码、日志、测试和依赖配置里的风险一次性梳理清楚，避免我们下周发版时再临时返工。请基于 audit_master.xlsx、service.log、test_results.json 和代码目录里的 Python 文件，整理成一份简洁的汇总报告，说明哪些地方需要修、哪些地方需要补测，并给出一个统一的处理顺序。
```

### 898. D5_g980693_zh (domain=D5, difficulty=7)

```
我整理了一个单文件审计包：inputs/codebase_audit_bundle.xlsx。请你把里面的代码清单、配置、测试日志和嵌入的真实 seed 文本一起做一轮综合审计，最后输出一份 findings.md。
- 先分别做静态代码风险复核、生产配置检查、测试失败归因、以及 seed 文本交叉核对。
- 只关注文件里能直接定位的项目，不要泛泛而谈；结果里要把命中的模块名、配置文件名和测试统计写清楚。
- 需要在报告末尾补一个简短的跨来源一致性说明：哪些代码风险和哪些测试失败/配置问题彼此呼应，哪些地方只是文本证据而不是直接失败证据。
```

### 899. D5_g980780_zh (domain=D5, difficulty=7)

```
请检查 inputs/code_audit.xlsx、inputs/test_logs.xlsx、inputs/config_audit.xlsx，分别完成代码静态审查、测试失败日志梳理、配置/依赖审计，并把结果合并成一份简洁的汇总报告。我只需要一个输出文件，里面要有各部分结论、问题统计和最终修复建议。
```

### 900. D5_g980893_zh (domain=D5, difficulty=7)

```
我需要你审计一下 compound_audit.xlsx 和 incident_log.txt 这两个输入，做成一份精简的汇总报告，重点把代码安全、生产配置、测试失败和依赖/日志风险这几条线并行查清楚，然后合并成最终的修复与验证计划。
```

### 901. D5_g980921_en (domain=D5, difficulty=7)

```
Audit the small project in inputs/project_modules.xlsx, inputs/test_results.xlsx, inputs/pipeline.log, inputs/seed_records.xlsx, and inputs/scan_targets.xlsx. I need one compact report that pulls together the static code review, security/config review, test-failure triage, log-pattern review, and dependency check.
- Flag the exact issues you can confirm from the files.
- Summarize which modules/tests/configs are affected and which areas look clean.
- Finish with a short fix-and-validation plan that ties the findings together.
- Keep the output concise and table-driven if that helps.
```

### 902. D5_g980974_zh (domain=D5, difficulty=7)

```
请审计 inputs/audit_bundle.xlsx 和 inputs/project_audit_memo.pdf，输出一个简短的决策摘要文件 decision_brief.md。我要看到四条并行结论：代码静态审查、security 风险、测试失败归因、依赖/配置审计，最后给出统一修复优先级。重点是把可直接落地的结论写清楚，并引用你算出来的关键数字。
```

### 903. D5_g981036_en (domain=D5, difficulty=7)

```
I need a single findings.md that audits code_audit_inventory.xlsx, ops_audit.log, and audit_memo.pdf together. Please split it into separate analysis tracks for module-level code review, security/risk checks, test-log triage, and dependency/config review, then reconcile anything that overlaps across the files and call out any conflicts you see.
```

### 904. D5_g981091_en (domain=D5, difficulty=7)

```
Audit the four input files code_audit.xlsx, config_audit.xlsx, dependency_audit.xlsx, and test_results.xlsx, plus the large audit_log.jsonl file, and produce one findings.md brief. I need a compact but rigorous cross-source review that separates static code issues, config risk, dependency risk, and test-failure triage, then reconciles anything that appears in more than one source.
```

### 905. D5_g981094_en (domain=D5, difficulty=7)

```
Review inputs/compound_audit_dataset.xlsx, inputs/audit_log.txt, and inputs/postmortem_brief.pdf. I need one ranked decision brief for what to fix first across code, security/config, failing tests, and dependencies, with the supporting counts and the validation plan in one file.
```

### 906. D5_g981120_zh (domain=D5, difficulty=7)

```
我需要你把这次代码库审计和测试日志一起做个决策简报，输入是 `code_audit.xlsx`、`real_seeds.txt` 和 `inventory.csv`。请先分别梳理静态代码风险、配置风险、测试失败归因、以及模块覆盖情况，最后输出一个很短的结论文件，给出优先级排序和建议处理顺序。
```

### 907. D5_g981139_en (domain=D5, difficulty=7)

```
I need a compact audit decision brief for this codebase. Review project files in inputs/project/, the test log inputs/test_run.log, the workbook inputs/audit_inputs.xlsx, and the summary in inputs/audit_brief.docx. I want one ranked recommendation file that compares the major risk areas across code, tests, and config, then says what should be fixed first before release.
```

### 908. D5_g981178_zh (domain=D5, difficulty=7)

```
请基于 inputs/audit_pack.xlsx、inputs/service_audit.log 和 inputs/dependencies.json 做一份合并审计报告，输出成一个紧凑的结果文件。我要看到代码审查、日志异常、测试失败和依赖/配置四条线的结论，并把需要修的地方汇总成可执行的修复与验证计划。
```

### 909. D5_g981262_zh (domain=D5, difficulty=7)

```
请审核这三个输入文件：code_audit.xlsx、test_run.log、dependency_audit.xlsx，输出一份合并后的简报文件，给出代码审计、配置审计、测试日志梳理和依赖检查的结论，并附上统一的修复与验证建议。我要的是一份能直接发给研发和测试团队的汇总报告，不要拆成多份。
```

### 910. D5_g981272_zh (domain=D5, difficulty=7)

```
我有个项目的审计数据在 project_audit.xlsx 里。里面包含了源代码、测试日志、配置和依赖信息。帮我做一份综合审计报告，包括代码安全、测试失败分析、配置和依赖审计，最后给出修复建议。输出到 findings.md。
```

### 911. D5_g981387_zh (domain=D5, difficulty=7)

```
需要你把这套小项目做一次完整审计，并把结果整理成一份简洁的汇总报告。请重点查看 inputs/audit_bundle.xlsx、inputs/project_a.py、inputs/project_config.json、inputs/service.log，分别梳理高风险代码模式、生产配置风险、测试失败情况和日志里的异常线索，最后合并成一个统一的修复与验证计划，说明优先级、影响范围和建议的验证顺序。
```

### 912. D5_g981395_en (domain=D5, difficulty=7)

```
You are given an audit spreadsheet, a test-run table, and a PDF log excerpt from a software engineering review.

Goal: produce a concise audit brief that identifies the most important recurring findings and cross-checks them against the test/log evidence.

Deliverables:
1. A ranked summary of the top issues by severity and recurrence.
2. A cross-reference of any findings that appear in both the spreadsheet and the logs/tests.
3. A short recommendation list focused on the highest-risk patterns.

Constraints:
- Use only the provided files in inputs/.
- Keep the brief structured and specific.
- Cite the most relevant item IDs, modules, and test names when applicable.
```

### 913. D5_g981449_zh (domain=D5, difficulty=7)

```
我这边要做一次小型项目的代码与日志联合审计，输入文件是 inputs/audit_summary.xlsx、inputs/modules.csv、inputs/tests.csv、inputs/dependency_audit.csv、inputs/app.log 和 inputs/audit_brief.docx。请你基于这些材料输出一份合并后的审计报告，重点把代码风险、测试失败、配置/依赖问题和运行日志里的异常串起来说明，并给出一份可执行的修复与验证计划。
- 先把模块代码里的高风险调用、测试失败模式、prod 配置问题、以及日志里的关键异常分别梳理出来
- 再按影响面和修复优先级汇总成一个统一结论，说明哪些问题最先处理
- 最后给出一份简洁的验证清单，方便我后续回归检查
- 结果只要一个汇总文件，内容尽量紧凑，但要能直接用于推进修复
```

### 914. D5_g981586_en (domain=D5, difficulty=7)

```
Audit codebase_audit.xlsx, app_runtime.log, and test_results.xlsx as one package. I need a compact report that pulls together the code review, security/config checks, and the test-log triage, then ends with a single fix-and-validation plan.
```

### 915. D5_g981621_zh (domain=D5, difficulty=7)

```
请审计这三份文件：inputs/code_audit.xlsx、inputs/test_and_ci_logs.xlsx、inputs/dependency_config_audit.xlsx，并把结论合并成一份决策摘要。我要看到代码静态审查、测试失败归因、配置/依赖风险和最终优先级建议，输出到一个短文件里。
```

### 916. D5_g981638_en (domain=D5, difficulty=7)

```
We need to run a quick security and quality check on our project. I've attached three files: codebase.py with our Python functions, test_log.log from our last CI pipeline, and config.xlsx with our configuration settings. Please analyze them and give me a single summary report (Excel file) that lists:
- how many dangerous code patterns exist (like eval, exec, pickle.loads, weak hashes, etc.)
- how many hardcoded secrets or other security risks in the code
- test results: total tests, passes, failures, errors, and which test suites failed most
- configuration issues: debug enabled in production, short secret keys
Also include a short fix plan. I need the numbers and a clear overview, not the full code dump.
```

### 917. D5_g981652_zh (domain=D5, difficulty=7)

```
请基于 `code_audit_bundle.xlsx` 和 `runtime_audit.log` 做一份合并审计简报，输出为 `findings.md`。
- 先分别梳理问题清单、配置项和运行日志三部分，再做一次交叉核对，说明哪些结论彼此一致，哪些地方存在冲突或需要复核。
- 重点看 Django 相关的多模块线索：迁移/约束/SQLite/DDL 参考，以及日志里明显的高风险代码模式。
- 结论里要给出每条审计线的要点、风险判断和建议的验证动作，最后写一个统一的修复与验证计划。
- 如果发现配置里有明显不适合生产的项，也请单独列出来。
```

### 918. D5_g981717_zh (domain=D5, difficulty=7)

```
请审计 inputs/project_audit_pack.xlsx 和 inputs/app_audit.log，把代码静态审查、测试失败归因、配置/依赖风险和最终处置建议合并成一份简短决策稿。我要看到按优先级排序的结论、每个模块的主要问题数，以及你建议先修什么、后验证什么。
```

### 919. D5_g981870_en (domain=D5, difficulty=7)

```
I need you to audit the codebase and test logs for the project 'FinancialCalc'. The files are in the inputs folder: codebase.docx (source code), test_logs.xlsx (test results), config.yaml (application config). Please run a static code review for security issues, triage test failures, and check the configuration for common problems. Consolidate all findings into a single report (xlsx for tabular data and a docx summary).
```

### 920. D5_g981888_zh (domain=D5, difficulty=7)

```
需要你把这套小项目做一次并行审计，输入文件是 inputs/codebase_manifest.xlsx、inputs/system_audit.log、inputs/qa_bundle.json。我要一份合并后的简报，重点是代码风险、日志异常、测试/样例质量和配置问题，最后给出统一的修复与验证建议。

- 先分别审查 core/auth.py、core/payment.py、core/reporting.py、core/config.py 这四个模块，找出我关心的那几类明显风险点。
- 再扫一遍 system_audit.log，抓出和这些风险对应得上的异常记录，并按类型归类。
- 对 qa_bundle.json 里的测试/样例做一次 triage，特别关注实际 seed 记录和 synthetic 记录的数量、覆盖情况，以及是否有和代码风险相关的线索。
- 最后把代码、日志、测试三路结果合并成一页式结论：哪些问题需要先修、建议怎么修、修完怎么验证。
- 输出一个精简的结构化报告文件，能让我直接转给研发和测试同事。
```

### 921. D5_g982000_zh (domain=D5, difficulty=7)

```
这次发布前我需要你把三个输入文件一起做一次联合审计：inputs/core.py、inputs/auth.py、inputs/settings_prod.py，再结合 inputs/ci_scan.log、inputs/app_runtime.log 和 inputs/test_suite_inventory.xlsx。我需要你先把代码风险、配置风险、测试失败和日志异常分开看，再合成一份可以给研发和发布团队看的简短结论。最后请输出一份汇总报告和一份表格结果，里面要写清楚哪些地方需要优先修、哪些测试和日志证据支持你的结论。
```

### 922. D5_g982085_en (domain=D5, difficulty=7)

```
We need a security and quality audit report for our data_utils project. The project has a few Python modules, a config file, test logs, and a dependency list. I want you to analyze the static code for dangerous functions (like eval, exec, pickle, unsafe yaml, subprocess with shell=True, weak hash functions), check the config for production security issues (debug mode enabled and secret key length), triage test failures from the test log, and review dependencies for known vulnerable packages. Please compile a unified report in an Excel file summarizing all findings with counts and lists. The input files are in the 'inputs' folder.
```

### 923. D5_g982142_en (domain=D5, difficulty=7)

```
I need a single findings.md that audits the codebase_audit.xlsx workbook plus test_failures.log, security_scan.log, and config_audit.json. Please split it into four independent tracks: a static review of the code files for the exact risky tokens listed in the workbook, a test-failure triage from the log, a config/dependency risk review, and a short cross-source reconciliation that ties the Django issue text to the current failure log. I want one concise report with the findings, what changed, what still looks broken, and a unified fix-and-validation plan.
```

### 924. D5_g982434_zh (domain=D5, difficulty=7)

```
请帮我做一次代码库和日志的联合审计，输入是 inputs/audit_inputs.xlsx、inputs/audit_brief.docx 和 inputs/artifacts_bundle.txt。这个项目是一个小型多模块工程，我需要你把静态代码检查、安全风险、测试失败和配置/依赖问题一起梳理出来，最后给我一份能直接发给研发团队的汇总结论。
- 先分别检查 module_a、module_b、module_c 的代码问题，尤其关注可 grepping 的明显风险点。
- 再看测试结果和运行日志，把失败项、重复报错和对应模块的关联关系整理清楚。
- 依赖和配置也要一起审一下，尤其是生产环境配置和高风险依赖。
- 最后输出一份合并后的修复与验证计划，内容要短，但要能落地。
```

### 925. D5_g982442_zh (domain=D5, difficulty=7)

```
我需要你把这次代码库和测试日志一起做个联合审计，文件是 audit_workbook.xlsx、run_tests.log 和 test_runs.csv。请分别看代码安全、配置和依赖、测试失败日志、还有评审清单这几块，最后合成一份简短的决策说明，直接告诉我现在该优先处理什么、风险点怎么排序、以及建议的修复和验证顺序。
```

### 926. D5_g982754_zh (domain=D5, difficulty=7)

```
我需要你把这套审计材料整理成一份 findings.md：请同时看 inputs/source_pack.docx、inputs/audit_inputs.xlsx、inputs/test_run.log 和 inputs/config_prod.yml / config_staging.yml / requirements.txt，分别做代码审计、配置与依赖审计、测试日志排查，再把结论合成一页左右的中文分析 brief，重点写清楚各模块的问题、测试失败和跨文件能对上的地方。
```

### 927. D5_g982855_en (domain=D5, difficulty=7)

```
I need a compact audit report for the files inventory.xlsx, logs.txt, and codebase.txt. Please review the codebase, logs, and dependency inventory together and give me one consolidated output file.
- Do a static review of the core queryset module and call out any combined-query behavior issue.
- Do a security scan of the auth/worker modules for obvious unsafe patterns, using grep-style detection.
- Triage the failure log and summarize the failed test categories.
- Audit the prod config and dependency pins for the specific issues that stand out.
- Finish with a short fix-and-validation plan that ties the findings together.
```

### 928. D5_g982916_zh (domain=D5, difficulty=7)

```
你好，我需要你帮我做一个代码库的综合审计。这个项目包含四个模块（module_a, module_b, module_c, module_d）的源代码，存放在“codebase.xlsx”文件中（每个模块一个sheet）。另外，还有测试运行结果在“test_results.xlsx”里，以及配置和依赖信息在“config_and_deps.xlsx”里。我希望你从四个独立维度进行分析：①静态代码安全审查——检查所有代码中是否包含危险函数调用（比如eval、exec、不安全的yaml.load、subprocess带shell=True、使用md5/sha1处理密码等）；②测试失败分类——统计哪些测试失败，按模块分组，并且记录错误类型（比如AssertionError、TypeError）；③配置审查——检查是否为生产环境而debug却设为true、secret_key长度是否太短；④依赖版本审计——对比已知漏洞版本列表，找出有风险的包。最后，请综合所有发现，生成一个决策建议文件“decision_brief.md”，按照风险高低排列需要修复的问题，并引用关键数字支持你的建议。请在decision_brief.md中用中文撰写，并包含表格或列表形式。注意：所有分析必须使用Python脚本或grep类的方式处理文件，不能仅凭推理。
```

### 929. D5_g982927_zh (domain=D5, difficulty=7)

```
请审计 inputs/codebase_audit_bundle.xlsx 里的这套小型代码库与测试记录，输出一份简洁的统一报告。
- 先分别看代码静态风险、配置风险、依赖风险和测试日志，最后汇总成一个可执行的修复与验证计划。
- 重点说明哪些风险是明确命中的、哪些测试失败属于同一类问题、以及优先级怎么排。
- 报告里请把能直接落地的修复建议写清楚，最好能对应到具体文件或模块。
- 只需要一份最终汇总文件，不要拆成多份报告。
```

### 930. D5_g982971_en (domain=D5, difficulty=7)

```
I need you to audit a small multi-module project. I've put together two files for you: audit_data.xlsx (with code, dependencies, and config sheets) and test_log.pdf (test results). I want you to run a thorough audit: static code review for dangerous patterns in modules A and B, triage the test failures from the log, and audit the dependencies and config for security issues. Then synthesize everything into a ranked recommendation plan in a file called decision_brief.md. Please use Python/grep to extract the numbers;. Let me know if anything is unclear.
```

### 931. D5_g983100_zh (domain=D5, difficulty=7)

```
请对附件中的 code_review.py、test_run.log 和 project_config.xlsx 进行综合审计。
要求：
1) 静态代码安全扫描（检测不安全函数调用）；
2) 测试日志失败分析（统计失败率及错误类型分布）；
3) 配置安全问题检查（如生产环境开启了 Debug、密钥长度不足）。
最终输出一份 .xlsx 报告文件和一个中文 PDF 摘要文件。
```

### 932. D5_g983129_zh (domain=D5, difficulty=7)

```
我们需要对遗留项目进行安全审计，确保代码没有危险函数、测试日志稳定、配置安全。
请使用 codebase_logs.xlsx（包含代码、日志、配置）和 security_policy.pdf（安全政策参考）进行分析，
输出一个综合修复决策报告 decision_brief.md。
```

### 933. D5_g983174_en (domain=D5, difficulty=7)

```
I need a consolidated audit brief from audit_inputs.xlsx, seed_notes.docx, and combined_audit.log. Please review the code, config, test results, and dependency data as four parallel tracks, reconcile anything that overlaps, and write one findings.md with a clear fix-and-validation plan plus cross-source conflict notes.
```

### 934. D5_g983333_en (domain=D5, difficulty=7)

```
I need a single compact report that pulls together a review of the attached project files so I can decide what to fix first. Use the spreadsheet in project_audit.xlsx, the code files, and nightly_run.log to check the risky code patterns, the failing tests, and the dependency/config problems, then give me one concise report with the key counts, the specific files or modules involved, and a practical fix-and-validation plan.
```

### 935. D5_g983508_en (domain=D5, difficulty=7)

```
Review the workbook inputs/project_audit_workbook.xlsx and produce one compact audit report file. I need a combined code review, security review, test-failure triage, and dependency/config audit, then a short fix-and-validation plan.
```

### 936. D6_g111_en (domain=D6, difficulty=7)

```
I have five files in the inputs folder: contracts.csv, policy_summaries.md, review_notes.xlsx, contract_audit_log.txt, and ops_metrics.sqlite. Please produce a compact research brief that synthesizes information from all these sources (not just summarizing each one individually) and a small evidence table with key metrics and cited record IDs. Since the sources are diverse in format, split the analysis into 3–4 parallel sub-analyses, then reconcile any cross-source conflicts or anomalies. I need the brief to cover contract counts and anomalies, durations, top contract values, review approval rates, notable audit events, invoice totals and unpaid share, and policy-related metrics. Use your best judgment on the specific calculations. Deliver the brief as findings.md and the table as evidence_table.csv.
```

### 937. D6_g284_en (domain=D6, difficulty=7)

```
I need you to prepare a research synthesis brief from four source files in inputs/: contracts_register.csv, obligations_extracted.xlsx, policy_controls.xlsx, and invoices.csv. The goal is to reconcile the sources and explain findings, not just dump raw rows. Produce findings.md with a synthesized analysis and an evidence table (csv or markdown) supporting major findings. Cover contract term reconciliation, clause extraction vs policy controls, invoice/payment integrity, and cross-source exceptions and risk summary. Note any cross-source conflicts and how you resolved them.
```

### 938. D6_g328_zh (domain=D6, difficulty=7)

```
请基于以下多源输入文件完成一份综合分析简报，作为向法务、采购、财务和运营的报告：

- `contracts_extract.csv`
- `policy_handbook.xlsx`
- `invoice_lines.xlsx`
- `vendor_master.xlsx`
- `vendor_status.xlsx`
- `exceptions.xlsx`
- `project_brief.md`

分析覆盖四个独立线索：合同条款、制度手册、发票明细、供应商对账。重点包括：

- 合同：自动续约数量、数据处理条款数、通知天数均值、年费最大值、SLA保底≥10%的合同数。
- 制度手册： section 总数、不同负责人数量。
- 发票：按标准去重规则（同一 invoice_id 保留最后一行，重算 `quantity * unit_price`）后统计唯一 ID 数、原始重复 ID 数、金额不一致数、重算后总金额。
- 跨源对账：已批准供应商的发票数量，并通过 `vendor_id` 关联 `vendor_status` 与 `vendor_master`。

最终交付：

1. `findings.md`：一页左右的中文简报，包含四条线索的结论、跨源 reconciliation 及冲突说明。
2. `evidence.csv` 或 `evidence.md`：关键证据行（少量），便于人工复核。

简报中需单独列出“小结：异常与冲突”（至少涵盖重复 invoice_id、金额不一致、未批准供应商发票、未解决高严重度异常）以及“建议后续动作”。

请按我们的标准方法论处理，无需输出逐行全量数据。
```

### 939. D6_g357_zh (domain=D6, difficulty=7)

```
请基于 inputs/policies.xlsx、inputs/contracts.xlsx、inputs/expenses.xlsx、inputs/invoices.csv 和 inputs/document_sources.sqlite 这五个文件，做一份跨来源复核的分析简报，输出 findings.md（中文，含综合结论和异常说明）和 evidence_table.csv（关键证据行）。
```

### 940. D6_g360_zh (domain=D6, difficulty=7)

```
请基于 inputs/contracts.xlsx、inputs/policies.csv、inputs/contract_policy_mappings.csv、inputs/invoices.xlsx 和 inputs/issues.csv 生成 decision_brief.md，用于管理层决定本季度优先整改与复审的合同/政策范围。简报需综合多来源数据，给出可执行的优先级建议和排名依据。
```

### 941. D6_g446_zh (domain=D6, difficulty=7)

```
请帮我把这批合同、政策、条款和工单材料做一版交叉核对的分析简报，重点看哪些客户和合同最值得优先跟进。请直接基于下面这几个文件输出 1 个 findings.md，再附 1 个简短 evidence_table.csv，内容要能给管理层看。

- 需要同时看 contracts.csv、policies.xlsx、contract_clauses.xlsx、support_tickets.xlsx、usage_finance.xlsx。
- 合同侧请按“合同有效期内、年化金额、折扣、续约方式、合同评分”综合看风险；风险分用 0.5*短板合同风险 + 0.3*工单压力 + 0.2*条款风险，其中短板合同风险按年化金额低于 180000 记 1，否则记 0，工单压力按已关闭/已升级工单里的超期率算，条款风险按高严重度且需复核条款占比算。需要把所有分数标准化到 0-100。
- 政策侧请只看 2024-01-01 到 2024-12-31 之间生效的正式版本；同一个 policy_id 如果有重复，优先保留更晚的有效日期，若日期缺失或是 TBD 就单独列为异常，不并入正式统计。
- 工单侧请只统计状态为 Closed 或 Escalated 的工单；超期定义为 resolved_date 晚于 due_date，或者 Escalated 状态但 resolved_date 为空；重复 ticket_id 只算一次，优先保留 latest created_date，其次保留非空 resolved_date。
- 需要做 4 个独立分析块：① 合同风险与优先级；② 政策覆盖与异常；③ 条款高风险与复核；④ 工单 SLA 压力与客户聚焦。每块都要各自给出关键结论，并在最后合成一段“跨来源冲突/一致性说明”，专门指出哪些合同、政策或工单记录互相对不上。
- 最后请给一个 10 行以内的小表，列出最该优先跟进的前 5 个合同（按综合风险分降序，分数并列时按年化金额升序）、以及每个合同对应的客户名、风险分、工单数、超期工单数和高风险条款数。

请注意：如果某些字段为空、日期无效或重复冲突，请按我上面说的规则处理，不要自己补。
```

### 942. D6_g593_en (domain=D6, difficulty=7)

```
I need a short research brief that ties together the policy library, contract register, expense claims, and exceptions file. Please pull out the main findings on which policy version actually governs each situation, where the claims or contracts conflict with the written rules, and any pattern that looks risky or inconsistent. I want one concise findings.md plus a small evidence table file.
```

### 943. D6_g87_zh (domain=D6, difficulty=7)

```
基于以下5个文件做一份合同与政策交叉核对分析brief，用于月底经营复盘：
- inputs/contracts_master.csv
- inputs/approvals_log.xlsx
- inputs/payment_ledger.csv
- inputs/renewal_reminders.csv
- inputs/policy_excerpt.txt

需要覆盖治理合规、财务对账、续约监控、政策例外等方面，输出findings.md和evidence_table.csv。按标准口径处理数据去重和判定。
```

### 944. D6_g980469_zh (domain=D6, difficulty=7)

```
我需要你把 inputs/contracts.xlsx、inputs/clauses.xlsx 和 inputs/policy_brief.docx 这三份材料一起看完，最后只输出一个简短的决策文件，告诉我这批内容里最值得优先推进的合同供应商/合同组合是哪一个，并按优先级排个名。重点帮我把条款覆盖、风险问题、重复记录和参考合同里的关键信息都核对清楚，结果里把支撑结论的数字写明白就行。
```

### 945. D6_g980605_zh (domain=D6, difficulty=7)

```
我有三个文件：合同条款表（contract_clauses.xlsx）、审查政策手册（policy_manual.pdf）和变更事件日志（incident_log.xlsx）。请你综合分析这些文件，找出所有不符合政策要求的控制权变更条款，检测数据中的异常（如重复、缺失、矛盾），并检查跨文件一致性。最后生成一份 findings.md 简要报告。具体分析规则和异常定义见详细要求。
```

### 946. D6_g980785_en (domain=D6, difficulty=7)

```
Review clause_dataset.xlsx together with seed_clauses.docx and produce a single findings.md brief. I need four parallel analyses: (1) classify the change-of-control response by clause effect, (2) extract and reconcile any numeric notice periods and account/coverage constraints, (3) audit written-approval and control-trigger language for policy exceptions, and (4) reconcile the seed clauses in the DOCX against the workbook records, including the explicit anomalies we planted: the duplicate record_id, the missing notice period, and the conflicting control wording. Please synthesize the results into one concise brief with cross-source reconciliation notes and the key counts/totals.
```

### 947. D6_g981013_en (domain=D6, difficulty=7)

```
You are a due diligence analyst. Your task is to analyze the provided documents (contract clauses, movie plot descriptions, and legal texts) and produce a coherent assessment. Identify key clauses, answer movie questions, summarize legal provisions, and cross-reference any inconsistencies or hidden relations across the different document types.
```

### 948. D6_g981178_zh (domain=D6, difficulty=7)

```
你好！我需要你分析三份输入文件，完成一份综合报告。文件如下：

- inputs/contracts.xlsx：合同条款数据，包含真实种子和合成记录。
- inputs/legislation.xlsx：法案数据，包含小型企业法案、加州体育委员会法案等。
- inputs/qa_plots.xlsx：剧情问答数据，包含一些真实剧情和问题。

请帮我完成以下工作（每个都是独立分析轨道）：

1. 提取合同中的关键条款（特别是最惠国待遇条款），识别标签与内容不一致的情况。
2. 分析法案中的贷款限额变化，计算净增加总额，并找出任何异常（如新限额反而降低）。
3. 从剧情问答中提取真实答案，检查是否存在重复plot_id或no_answer标记错误。
4. 跨源核验：将引用"Small Business Act"的合同与法案中的贷款限额进行对比，标记价格超过新限额的合同。
5. 检测数据完整性问题：空字段、日期逻辑错误（结束<开始）、重复行等。

请将以上所有发现整合到一个 findings.md 文件中，包含汇总表格、异常清单和交叉引用说明。不需要输出原始数据。
```

### 949. D6_g981259_en (domain=D6, difficulty=7)

```
I need you to analyze a set of contract clauses and policy documents for a compliance review. There are three input files in the inputs folder: contracts.xlsx (table of contract clauses), policies.docx (policy text), and metadata.xlsx (document metadata). Please produce a findings.md report that synthesizes insights across these sources, including clause analysis, label analysis, policy text extraction, cross-source reconciliation, and anomaly detection. Focus on consistency and flag any issues.
```

### 950. D6_g981307_zh (domain=D6, difficulty=7)

```
我需要你分析contract_clauses.xlsx文件中的合同条款，对照policy_definitions.csv中的政策定义。请生成一个合规风险报告，按风险排名，列出风险最高的合同，并引用各个子分析的关键数据来支撑建议。输出文件名为compliance_risk_report.json。
```

### 951. D6_g981330_en (domain=D6, difficulty=7)

```
You are reviewing a small media-rights packet and two spreadsheets.
Use the documents to produce a concise internal memo.

Deliverables:
1) A 2-3 paragraph memo summarizing the most important policy and contract risks.
2) A bullet list of the five highest-priority issues with supporting file references.
3) A short appendix with computed counts/aggregates from the spreadsheets.

Tool target: cross-check the DOCX schedule against the two XLSX files, identify threshold/policy violations, and cite the relevant row IDs or question IDs.

Sub-analyses hint: look for invoice amounts above the CFO threshold, zero-value anomalies, notice timing issues, retention/publication policy mismatches, and repeated title/vendor patterns.
```

### 952. D6_g981345_zh (domain=D6, difficulty=7)

```
这批合同、合规义务和票据抽取结果要做一次统一复核，方便我们给法务和财务出一版可直接汇报的摘要。请读取 `contract_policy_extraction_dataset.xlsx` 和 `review_notes_buried_references.docx`，把关键结论整理成一个紧凑的汇总文件。我需要你同时看合同主数据、条款抽取、合规义务、票据明细，以及文档里埋着的参考信息，最后把异常和重点数字合在一起。输出请尽量简洁，但要把能影响汇报的事实都列清楚。
```

### 953. D6_g981470_zh (domain=D6, difficulty=7)

```
请基于 contracts_register.xlsx、policy_matrix.xlsx 和 evidence_bundle.pdf 整理一份合并分析报告，重点看合同条款、政策台账和证据汇编里的抽样内容。我只要一份最终汇总文件，里面把关键统计、异常点和需要我关注的结论放在一起。
```

### 954. D6_g981513_zh (domain=D6, difficulty=7)

```
我需要你把这三份资料合并做一版给管理层看的简报：contracts_master.xlsx、policy_register.xlsx、document_review_events.csv。重点是把合同条款、制度文本和文档审查事件放在一起看，帮我识别出当前最值得关注的风险和结构性问题，最后只输出一份汇总报告。
```

### 955. D6_g981515_en (domain=D6, difficulty=7)

```
Please review the three input files — contracts.xlsx, obligations.docx, and audit_log.txt — and give me a single decision brief on the strongest compliance risk and the recommended priority order for follow-up.
- Pull the key contract counts, obligation patterns, and audit-log events that matter.
- Compare the contract portfolio against the policy limits and notice requirements in the DOCX.
- Call out any material concentration or overlap patterns that would change the risk ranking.
- Put the result in one short brief with a ranked recommendation and the supporting numbers.
```

### 956. D6_k982049_zh (domain=D6, difficulty=7)

```
请帮我对文件 chicago__chicago-contracts__contracts.csv 做一版偏“档案/合同台账分析”的深度审阅，重点围绕“排名与集中度”展开：先找出合同数量和金额都最集中的部门、供应商、合同类型和采购类型，再看这些头部群体是否主导了总金额与总合同数，并补充识别异常记录（例如负金额、缺失日期/采购类型）。我希望结果能直接支持管理层判断：哪些部门/供应商是绝对头部，Top-N 覆盖了多少比例，金额分布是否呈现明显的 Pareto 集中，以及不同维度之间是否有共同的高集中现象。请基于真实字段（如 Department、Vendor Name、Contract Type、Procurement Type、Award Amount、Start Date、End Date、Approval Date、Purchase Order (Contract) Number、Revision Number、Specification Number）做分析，不要编造任何值。最好把结论拆成 4-6 个彼此独立的分析轨道，最后汇总成一份可用于汇报的结构化摘要。
```

### 957. D6_k982113_zh (domain=D6, difficulty=7)

```
请基于文件 chicago__chicago-contracts__contracts.csv 做一份围绕“阈值分布与区间 cohort（above/below business thresholds、分位数分桶、mix share）”的合同/文档分析。请你重点回答：1）Award Amount 在不同业务阈值下的合同数量、金额占比和平均金额分别是什么；2）把合同金额按分位数分桶后，各桶的数量、总金额和部门/采购类型 mix 是怎样的；3）不同 Contract Type、Department、Procurement Type 在这些阈值 cohort 中的分布是否明显不同；4）哪些供应商/部门更集中在小额合同、零金额合同或超大额合同；5）审批时间、合同周期与金额阈值之间是否存在可解释的模式；6）把这些发现整理成适合管理层阅读的简短结论，并输出可复核的统计口径。请注意所有结果都必须严格基于原始数据，不要假设或补全缺失值。
```

### 958. D6_k982366_zh (domain=D6, difficulty=7)

```
请基于文件 chicago__chicago-contracts__contracts.csv 做一份围绕“时间/趋势变化”的合同与记录分析，重点看采购与合同在不同年份、月份、审批时点、起止跨度上的变化规律。请尽量从业务角度回答：总量是否有明显波动、金额是否随时间变化、不同部门/采购类型在时间上的结构是否变化、合同延期/超期是否集中在某些时期、以及审批滞后是否存在季节性。数据里请重点使用这些字段：Start Date、End Date、Approval Date、Department、Vendor Name、Award Amount、Procurement Type、Purchase Order (Contract) Number、Revision Number、Contract Type、Contract PDF。请把分析拆成可并行的几条线，最后汇总成一个适合管理层快速阅读的结论摘要，并附上可复核的关键统计口径。
```

### 959. D6_k982799_zh (domain=D6, difficulty=7)

```
请基于文件 chicago__chicago-contracts__contracts.csv 做一份面向合同/档案记录的分层分析，重点围绕“金额分布与阈值 cohort”来判断哪些合同更集中在不同金额带、不同采购类型和合同类型中。请结合 Purchase Order Description、Purchase Order (Contract) Number、Contract Type、Start Date、End Date、Approval Date、Department、Vendor Name、Award Amount、Procurement Type、Contract PDF 等字段，至少拆成 5 个彼此独立的分析轨道：1）总体金额阈值 cohort（如负值、0、1-1万、1万-10万、10万-100万、100万以上）的数量与金额占比；2）按 Procurement Type 和 Contract Type 的金额 cohort mix 对比；3）按 Department 看高金额合同集中度及其份额；4）按时间维度（Approval Date）看每年合同是否更偏向高金额 cohort；5）识别重复/异常记录特征（例如缺失日期、负金额、合同编号重复）；6）从 Vendor Name 角度找出高金额合同最集中的供应商。请输出可直接用于汇报的简洁结论和一个 analysis_summary.json 风格的结构化结果，所有结论必须严格基于数据本身，不要臆测。另请说明哪些 cohort 最能代表预算压力最大的合同，以及它们主要分布在哪些部门/采购方式中。文件中的真实列名必须原样使用，不要改列名。
```

### 960. D6_k983079_zh (domain=D6, difficulty=7)

```
请基于文件 chicago__chicago-contracts__contracts.csv 做一份面向合同/档案分析的分布与阈值分层报告，重点看 Award Amount 在不同业务阈值下的覆盖情况、分位数分桶后的金额与数量结构、以及这些阈值/分桶在 Contract Type、Procurement Type、Department、Vendor Name 之间的混合分布。请同时结合关键日期字段（Start Date、End Date、Approval Date）做最基本的数据完整性检查，但不要把时间分析作为主线。我要的是一个适合向业务方汇报的、可落地的多轨并行分析：先确认金额分布和缺失，再看固定阈值 cohort（例如 0、1万、5万、10万、25万、50万、100万以上），再看按四分位/十分位切分后的桶内占比与金额贡献，最后识别主要合同类型、采购方式、部门和供应商在不同阈值段中的集中度与结构差异。输出时请围绕“业务阈值、分位桶、占比、集中度、异常高低金额合同”来组织结论，并指出哪些类别明显偏向高额合同、哪些偏向低额或零额合同。请直接使用 df 中现成字段：Purchase Order Description, Purchase Order (Contract) Number, Revision Number, Specification Number, Contract Type, Start Date, End Date, Approval Date, Department, Vendor Name, Vendor ID, Address 1, Address 2, City, State, Zip, Award Amount, Procurement Type, Contract PDF。
```

### 961. D6_k983291_en (domain=D6, difficulty=7)

```
Using the file mohankrishnathalla__global-house-purchase-decision-dataset__global_house_purchase_dataset.csv, analyze the dataset as a document / contract & records analytics problem with the main focus on segment comparison across categorical groups. I need a practical, decision-oriented readout that compares rates and average values across countries, cities, property_type, and furnishing_status, and highlights the biggest gaps between segments. Please also relate those segment differences back to affordability and decision outcomes using fields like price, customer_salary, loan_amount, monthly_expenses, emi_to_income_ratio, satisfaction_score, neighbourhood_rating, connectivity_score, crime_cases_reported, and legal_cases_on_property. Break the work into independent tracks so separate analysts could work in parallel, and summarize the most important contrasts, best-performing segments, and worst-performing segments for purchase decision patterns.
```

### 962. D6_k983325_zh (domain=D6, difficulty=7)

```
请基于文件 theworldbank__procurement-notices__procurement-notices.csv 做一份面向“文档/合同与记录分析”的多维度分析，重点放在时间趋势和周期变化上。请先检查并清洗日期字段 Publication Date 和 Deadline Date，再围绕 Notice Type、Procurement Type、Country Name、Major Sector、Project ID、Bid Description 等字段，分析采购公告在时间上的发布节奏、截止期分布、不同公告类型的月度变化、国家层面的趋势差异，以及文本描述与时间/类型之间的关联。希望输出适合给业务方快速阅读的结论，并把异常值、缺失值、重复 Project ID、以及关键类别在不同时间段的变化都纳入考虑。请按独立分析轨道拆分，便于并行处理，最后汇总成一份简洁的 analysis_summary.json。
```

### 963. D6_k983513_zh (domain=D6, difficulty=7)

```
请基于文件 gsutters__economic-freedom__efw_cc.csv 做一份面向“文档 / 合同 & records analytics”的分布与阈值分层分析，重点看经济自由度在不同业务阈值下的国家/年份 cohort 表现。请围绕 ECONOMIC FREEDOM、quartile、rank，以及各分项（1_size_government、2_property_rights、3_sound_money、4_trade、5_regulation）做分析：先按阈值统计样本覆盖与占比，再看各分位桶的构成、缺失情况、以及高/低自由度 cohort 的指标差异。请把结果拆成可并行的 4-6 个独立分析轨道，最后形成一个 analysis_summary.json，内容至少包括阈值 cohort、分位桶分布、各分项 mix share、以及关键国家/年份的异常点概览。注意所有结论必须严格来自数据本身，不要推测。
```

### 964. D6_k983668_en (domain=D6, difficulty=7)

```
Using the file aakaash89__neet-2024-ug-results-citycenter-wise__NEET_2024_RESULTS.csv, run a document/contract-style records analysis on the NEET 2024 city-center results using the columns dummy_srlno, marks, state, city, center_name, and center_number. I need this framed as a multi-part operational review with the main emphasis on temporal/trend analysis over the sequence implied by dummy_srlno and center_number: look for run-rate changes, period-over-period shifts, and whether scoring patterns move differently across segments as the record sequence progresses. Split the work into independent tracks so they can be handled in parallel: overall sequence trend, state-level trend shifts, city-center concentration and outliers, center-number progression patterns, and score-band movement over the record sequence. Please summarize the findings in a compact analysis_summary.json and include only deterministic, reproducible outputs.
```

### 965. D6_k983768_zh (domain=D6, difficulty=7)

```
请基于文件 mosapabdelghany__telcom-customer-churn-dataset__Telco_Cusomer_Churn.csv 做一份面向“合同/档案运营审计”的异常与离群分析。重点不是建模，而是按明确规则找出可疑记录、异常群体和需要复核的档案。请围绕以下主线展开：1）数值字段的极端值与IQR离群（tenure、MonthlyCharges、TotalCharges）；2）字符/类别字段中的稀有类别与异常组合（如不存在互联网服务却出现在线安全/备份等服务状态、付款方式极少见的组合）；3）按合同类型、互联网服务类型、纸质账单、支付方式分层，识别异常集中分布；4）从 churn 角度找出异常高风险子群与反常低风险子群；5）检查可能的数据质量问题（TotalCharges 的非数值/空白、字段间逻辑冲突、离群值与缺失是否集中在某些客户群）；6）输出一份可以交给人工复核的精简审计结论。请把分析拆成 4-6 个彼此独立的轨道，便于分工并行处理。请注意：所有结论必须严格基于该数据集中的真实值，不要假设或编造任何记录。
```

### 966. D6_k983877_en (domain=D6, difficulty=7)

```
Using gsutters__economic-freedom__efw_cc.csv, I need a contract/records-style cohort review focused on distribution and threshold analysis. Please break it into separate tracks so different people can work independently: (1) build country-year cohorts by economic-freedom quartile and summarize how records are distributed across quartiles and years; (2) measure counts and shares above/below practical business thresholds for ECONOMIC FREEDOM and the major pillars (1_size_government, 2_property_rights, 3_sound_money, 4_trade, 5_regulation); (3) compare the mix of countries in the top and bottom threshold cohorts, including the most frequent countries and years; (4) test how missingness and incomplete records cluster around the threshold cohorts and specific document-style fields; (5) look for concentration/dispersion in subscore baskets across quantile buckets, especially whether low-freedom cases are dominated by one or two weak pillars; and (6) produce a concise summary of the threshold gaps that would matter for contract enforcement and records reliability review. Keep the output focused on counts, shares, bucketed distributions, and simple deterministic comparisons using the actual columns in the file.
```

### 967. D6_k983971_zh (domain=D6, difficulty=7)

```
请基于文件 theworldbank__world-banks-major-contracts__Major_Contract_Awards.csv 做一份面向合同/档案记录分析的异常排查简报，重点围绕“按明确数值规则识别异常与离群点”来展开。请不要只做总体统计，我需要你把数据分成几个互相独立的分析轨道并分别输出结论，方便我分给不同同事并行核查。请至少覆盖以下几个方向：1）金额异常：用明确阈值、极值和四分位距（IQR）识别 Total Contract Amount (USD) 的超大/超小合同，并按 Region、Major Sector、Procurement Method 分层看异常集中在哪里；2）合同编号与记录质量：检查 WB Contract Number 是否存在重复、同号多记录、以及 Contract Signing Date / As of Date 的时间顺序异常；3）稀有类别：找出 Supplier Country、Borrower Country、Procurement Type、Procurement Category、Procurement Method 中出现频次极低的类别，并判断这些稀有类别是否更容易对应异常金额；4）供应商异常：识别单一 Supplier 在金额分布上是否存在明显离群值，尤其是同一供应商的高额合同占比、极端金额重复出现、以及跨国家中标的情况；5）项目级异常：按 Project ID 聚合，找出合同笔数少但总金额极高、单笔金额极端、或者金额变异系数异常高的项目；6）文本与字段一致性：检查 Contract Description、Borrower Contract Reference Number、Supplier Country Code 与 Supplier Country、Borrower Country Code 与 Borrower Country 是否存在明显不一致或缺失模式。请输出一个可直接交付的分析摘要结构，并把每个异常点尽量量化到可以复核的程度。需要你基于真实数据给出具体数值、排名和计数，而不是泛泛建议。
```

### 968. D6_k984017_en (domain=D6, difficulty=7)

```
Using gsutters__economic-freedom__efw_cc.csv, analyze the distribution of ECONOMIC FREEDOM and the related sub-scores with an emphasis on threshold cohorts and mix shares. I need a contract/records-analytics style review that tells me how many country-year records fall below vs. above key business thresholds, how those cohorts differ by quartile, and how the composition changes across the core component groupings (1_size_government, 2_property_rights, 3_sound_money, 4_trade, 5_regulation). Please break this into independent workstreams so multiple analysts can work in parallel: one on global threshold counts and quantile buckets, one on cohort mix shares by year and quartile, one on country-level concentration of low/high freedom records, one on missingness patterns across the score components, and one on relationships between the overall score and the five major component groups.
```

### 969. D6_k984095_zh (domain=D6, difficulty=7)

```
请基于文件 cankatsrc__invoices__invoices.csv 做一版面向“文档/合同与记录分析”的深度分析，重点放在时间序列和趋势变化上。这个数据里我最关心的是 invoice_date、amount、qty 以及不同 product_id / city / job 的变化规律。请你帮我把分析拆成几条可并行的线索，最终输出一份 analysis_summary.json，内容要能直接支持给业务和风控同事汇报。

具体来说，请重点回答：
1）按月/按季度看发票金额与数量的变化趋势，找出增长、回落和异常波动；
2）不同 product_id 的销售/开票节奏是否存在明显的时间集中或持续性变化，哪些品类在后期更活跃；
3）按 city 看金额与单据数量的时间趋势，识别哪些城市在某些月份突然放大或下滑；
4）按 job 看不同职业对应的开票金额、数量和时间分布差异，是否存在某些职业在特定时期更集中；
5）检查 invoice_date 是否存在明显的日期记录质量问题或极端时间点；
6）补充一个合同/记录分析视角的风险观察，例如高金额单据、重复模式、或某些维度的集中度变化。

请把结果写得像给忙碌的业务负责人看的结论：每条线索都要有清晰的趋势判断、关键时间点、以及可执行的后续建议。分析时请严格基于真实数据，不要编造任何值。最终请输出 analysis_summary.json。
```

### 970. D6_k984226_zh (domain=D6, difficulty=7)

```
请基于文件 utkarshx27__monthly-transportation-statistics__Monthly_Transportation_Statistics.csv 做一份面向“文档 / 合同 & 档案分析”的多维度统计分析，但重点放在“排名与集中度”上：找出哪些交通与基建指标长期占据总量的主要份额，是否存在明显的头部集中、前 N 项贡献、以及不同子领域（航空、道路、公交/轨道、货运铁路、水务/市政建设）之间的集中结构差异。请把分析拆成几个彼此独立的轨道，适合并行分工。每个轨道都要给出可核验的结论，尤其关注 Top-N 排名、累计占比、帕累托特征、以及按时间窗口（如近几年 vs 全样本）是否有集中度变化。请直接使用数据中的真实列名，例如 Highway Fatalities、Highway Vehicle Miles Traveled - All Systems、U.S. Airline Traffic - Total - Seasonally Adjusted、Transit Ridership - Urban Rail - Adjusted、Freight Rail Intermodal Units、State and Local Government Construction Spending - Highway and Street 等。最后输出一份适合汇报给忙碌决策者的结论摘要，以及一份可复核的结构化结果文件 analysis_summary.json。
```

### 971. D6_k984270_en (domain=D6, difficulty=7)

```
Using `kanchana1990__new-york-sold-real-estate-intelligence-2026__ny_real_estate_sold_properties_2026.csv`, build a contract-records style intelligence memo focused mainly on temporal / trend analysis over the available sequence fields (especially `sold_list_ratio`, `price_per_sqft_sold`, `price_per_sqft_list`, `lastSoldPrice`, and any size/condition proxies). I need you to break it into independent workstreams so a small sub-agent team can run in parallel: 1) time/sequence trend diagnostics on sale-to-list behavior and pricing efficiency, 2) segment-level trend comparison by `type`, `sub_type`, `size_tier`, and `city`, 3) outlier and anomaly review for unusually high/low realized-vs-list outcomes, 4) data quality and completeness review of fields that could bias the trend readout, and 5) a short executive summary of the most important directional shifts and concentrations. Please quantify the patterns, call out the strongest and weakest segments, and make the output suitable for an analyst handoff.
```

### 972. D6_k984277_en (domain=D6, difficulty=7)

```
Analyze the file shahriarkabir__procurement-strategy-dataset-for-kraljic-matrix__realistic_kraljic_dataset.csv using the real columns in the dataset, and focus the work mainly on temporal / trend analysis over the sequence-like operational fields (especially Lead_Time_Days and any period-over-period style comparisons you can derive from the data ordering or segmented slices). I need a procurement analytics readout for document / contract & records use: identify how lead times, risk, impact, cost, and Kraljic positioning change across the dataset and where the biggest shifts or concentration points are. Please split the work into independent tracks so different analysts can work in parallel, and make sure the final output is a concise analysis summary JSON with clear evidence-based findings from the actual data.
```

### 973. D6_k984449_en (domain=D6, difficulty=7)

```
Using usdpic__execution-database__database.csv, build a records-analytics memo focused mainly on correlation and driver analysis across the numeric fields and key categorical splits. I need you to assess which numeric fields move together, identify the strongest rounded Pearson correlations, and then test whether those relationships change by crime type, region, sex, race, and method. Also summarize the main records patterns that could affect downstream document/contract review, including age distribution, victim-count concentration, and any notable differences in juvenile, volunteer, federal, or foreign-national cases. Please keep the analysis grounded in the real columns in the file and make it decision-useful, not just descriptive.
```

### 974. D6_k984464_zh (domain=D6, difficulty=7)

```
请基于文件 ghassenkhaled__invoices-data__newest_invoices_data.csv 做一份面向“文档/合同与记录分析”的专题分析，重点围绕发票记录的“排名与集中度”展开：请找出金额、数量、逾期、行业/服务、国家、客户维度中的 Top-N 贡献者，计算头部集中度（例如 Top 3 / Top 5 / Top 10 占比、累计占比、Pareto 80/20 现象），并结合 invoiceStatus、balance、discount、tax、issuedDate、dueDate 做补充验证。我要的是可直接交付给管理层的结论，不要泛泛而谈；请把分析拆成 4-6 个彼此独立的轨道，方便不同人并行处理。最终输出请总结成一个 analysis_summary.json，里面要能看出头部客户、头部国家、头部服务、逾期金额与记录数的集中程度，以及是否存在明显的风险/依赖集中。
```

### 975. D6_k984668_en (domain=D6, difficulty=7)

```
Using shahriarkabir__procurement-kpi-analysis-dataset__Procurement KPI Analysis Dataset.csv, please build a contract/procurement records analysis focused mainly on distribution and threshold cohorts. I need a concise executive summary plus evidence-backed cutoff analysis across the real columns PO_ID, Supplier, Order_Date, Delivery_Date, Item_Category, Order_Status, Quantity, Unit_Price, Negotiated_Price, Defective_Units, and Compliance. Please break it into several independent workstreams so different analysts can work in parallel: one on quantity/value threshold buckets, one on negotiated-vs-list price savings cohorts, one on delivery-status and delay thresholds, one on quality/defect-rate cohorts, one on compliance mix shares, and one on category/supplier concentration around the high-volume/high-value tail. Use the actual dataset values only and keep everything deterministic.
```

### 976. D6_k984687_zh (domain=D6, difficulty=7)

```
请基于文件 eugeniyosetrov__building-permits__Building_Permits.csv 做一份面向“文档/合同与档案管理”的分析报告，重点看“数值字段之间的相关性与驱动因素”：哪些数值列彼此同步变化、哪些指标关联最强、以及按业务维度（许可类型、状态、社区、施工类型）看这些相关性是否一致。请把分析拆成几个并行可做的部分，最后汇总成一份 analysis_summary.json。需要重点结合这些真实字段：Permit Type、Permit Type Definition、Current Status、Estimated Cost、Revised Cost、Number of Existing Stories、Number of Proposed Stories、Existing Units、Proposed Units、Plansets、Existing Construction Type、Proposed Construction Type、Supervisor District、Neighborhoods - Analysis Boundaries、Zipcode、Site Permit、Fire Only Permit、Voluntary Soft-Story Retrofit、Permit Creation Date、Filed Date、Issued Date、Completed Date。请输出：1）数值字段相关性概览（含四舍五入后的相关系数）；2）最高相关的字段对及其业务解释；3）按许可类型/状态/社区分组后的关键数值差异；4）缺失值与可用性对相关性分析的影响；5）一个可执行的结论清单，指出最可能的驱动关系和需要注意的数据偏差。各部分尽量独立，便于并行分析。
```

### 977. D6_k985014_en (domain=D6, difficulty=7)

```
Using mexwell__drug-consumption-classification__drug_consumption.csv, I need a document/contract-style records QA review focused on anomaly and outlier detection using explicit numeric rules. Please run a structured analysis that flags unusual participant records, rare or inconsistent substance-use patterns, and extreme psychometric profiles. I want this broken into independent tracks so different people can work in parallel: (1) numeric outlier screening on the score variables and impulse/sensation-seeking measures using IQR and extreme z-like thresholds; (2) categorical rarity checks for the CL-coded substance columns, especially uncommon high-use categories and uncommon combinations; (3) record-level anomaly detection for impossible-looking or highly unusual multi-field profiles across demographics and psychometrics; (4) cross-tab comparisons to see which demographic groups over-index in the flagged rows; (5) duplicate/near-duplicate record checks using ID and identical feature profiles; and (6) a concise exception report with the exact counts, top offending fields, and the most extreme records to support a records-audit memo.
```

### 978. D6_k985016_zh (domain=D6, difficulty=7)

```
请基于文件 new-york-city__new-york-city-film-permits__film-permits.csv 做一份偏“文档/合同与记录分析”的深度分析，重点放在相关性和驱动因素上：哪些数值字段、时间字段和许可记录特征会一起变化，相关性最强的组合是什么，哪些维度最能解释许可数量、提前录入天数、许可时长、以及不同类型/地点的分布差异。请把分析拆成多个彼此独立的工作流，便于并行处理；每个工作流都要给出可落地的结论、关键指标、以及必要的交叉表/汇总。务必只使用数据中真实存在的字段，不要编造。重点围绕 EventID、StartDateTime、EndDateTime、EnteredOn、EventType、EventAgency、ParkingHeld、Borough、CommunityBoard(s)、PolicePrecinct(s)、Category、SubCategoryName、Country、ZipCode(s) 这些字段，尤其分析它们之间的相关性、关联强度、Top 关联组合、以及对许可记录特征的驱动关系。最后请输出一个适合管理层快速阅读的 summary，并附上可复核的指标口径。
```

### 979. D6_k985102_en (domain=D6, difficulty=7)

```
Use the file thirumani__shark-tank-india__Shark Tank India.csv to do a contract-and-records style analysis focused mainly on distribution and threshold cohorts. I want to know how the dataset splits around practical business thresholds like revenue, margin, EBITDA, SKU count, and deal size, and how those cohorts differ across season, industry, and founder mix. Please also check where the record is sparse or inconsistent, especially in fields tied to deal terms and founder demographics. Build this as a compact analyst memo plus a machine-readable summary.
```

### 980. D7_D7_dbg0 (domain=D7, difficulty=7)

```
I need you to pull together compact incident deliverables for the card-routing production incident using the files in inputs/: api_gateway_logs.jsonl, support_tickets.csv, ops_events.json, and service_catalog.json. I want three outputs—impact_summary.json (incident window, API impact, top error codes, support spike, top impacted users), incident_timeline.md (key events), and owner_comms_report.csv (owner/on‑call/commander and the external‑update SLA result). You know the usual definitions for dedup, affected minutes, etc.
```

### 981. D7_b1 (domain=D7, difficulty=7)

```
Analyze the four files in inputs/ for the support-routing automation incident on 2026-06-07:

- support_tickets.xlsx
- ledger_transactions.xlsx
- api_workflow_logs.jsonl
- ops_incident_config_and_comms.json

The incident involved a taxonomy/config rollout that sent certain customer-support tickets to a bot auto-close path. Produce these deliverables in the working directory:

- incident_summary.json — compact JSON covering incident window, impacted tickets, monetary exposure, API health metrics, timeline with latency calculations, and follow-up backlog.
- impact_by_intent.csv — one row per impacted final_intent with counts, ledger exposure, backlog.
- timeline.md — ordered timeline with owner/comms handoff notes and the three latency calculations.

Use our standard methodology: de-duplicate /support/route route_decision logs (keep first by request_id). Bad routes are those with config_version "cfg-2026-06-07.3", intent_name in {"extra_charge_on_statement", "card_payment_wrong_exchange_rate"}, routed_queue "general_inquiry_bot", and auto_closed true. Unique impacted tickets are non-duplicate tickets matching those intents. Monetary exposure: posted, unreversed ledger rows for impacted tickets where amount_gbp > expected_amount_gbp, category matches intent, and occurred within 7 days before to 2 days after ticket creation. Use percent error rate and p95 latency (linear 95th percentile) for API health comparison (baseline window before first bad route vs incident window). The follow-up backlog cutoff is 2026-06-07T18:00:00Z.

Summarize compactly — no per-ticket or per-log dumps.
```

### 982. D7_b6 (domain=D7, difficulty=7)

```
I need you to look into the suspected erroneous statement-fee rollout for INC-2026-0215-FEE. Use the files in inputs/: billing_events.sqlite, support_tickets.xlsx, api_gateway.jsonl, and ops_records.json. Put together an impact summary (JSON), an incident timeline (Markdown), and a short owner/comms report (CSV).
```

### 983. D7_g105_en (domain=D7, difficulty=7)

```
请调查 INC-4832 故障。使用文件：service_events_large.log、integrations.xlsx、ops_tickets.json 和 postmortem_notes.md。输出一个 JSON 总结、一个 CSV 影响表和一个 Markdown 时间线/通信报告。要求：重构时间线、量化影响、核对负责人和通信记录。
```

### 984. D7_g119_en (domain=D7, difficulty=7)

```
Investigate the ops incident and change-management dataset from these sources:  
- inputs/incidents.sqlite (incident records, notes, and API events)  
- inputs/change_tickets.xlsx  
- inputs/comms_timeline.json  
- inputs/postmortems.md  

I need a concise analysis brief (findings.md) and a supporting evidence table (evidence_table.csv or .md table). Cover the standard incident and change metrics: total incidents, SEV1 count, unresolved at extraction, incidents where detected_at precedes created_at, average MTTA and MTTR (resolved only), production change tickets with customer-visible impact, number of change tickets with rollback timestamps, duplicate request_id rows in api_events, duplicate message_id rows in communications, the service with the most incidents, and any cross-source conflict IDs that require reconciliation.  

Structure the brief into 3–4 independent analysis tracks (e.g., impact assessment, timeline reconstruction, owner/comms tracking, anomaly reconciliation). Include a short evidence table that cites source files for key facts. Reconcile any conflicts across the files using the data as the sole source of truth.
```

### 985. D7_g11_en (domain=D7, difficulty=7)

```
Investigate the multi-service incident cluster using inputs/incidents.json, inputs/logs.xlsx, inputs/configs.json, inputs/tickets.json, and inputs/postmortem_notes.md. Produce out_summary.json, timeline.md, and owner_comms_table.csv, reconciling the incident timeline, impact, and owner/comms context.
```

### 986. D7_g120_zh (domain=D7, difficulty=7)

```
基于 inputs/ 下的事故日志、配置快照和工单记录，写一份中文事故复盘摘要，包含结构化指标与管理层汇总。重点判断 billing 服务是否因 2026-03-18 08:12 之后部署的激进重试策略引发了 5xx/超时/队列堆积，并在回滚后恢复。
```

### 987. D7_g170_zh (domain=D7, difficulty=7)

```
基于 inputs/ 目录下的 incident_events.csv、api_requests_5m.xlsx、tickets.xlsx、config_changes.csv、communications.csv 和 README.md，整理一份给 SRE 负责人、业务负责人和客服主管共用的简明复盘包。输出 report_summary.json、report_timeline.md 和 report_ops。直接输出文件，不要解释。
```

### 988. D7_g187_en (domain=D7, difficulty=7)

```
Look at the files in `inputs/`: `services.xlsx`, `incident_logs.xlsx`, `tickets.xlsx`, `service_configs.csv`, `postmortem_draft.md`, and `incident_ops.sqlite`. Synthesize the incident into a concise markdown brief and an evidence table (CSV or markdown table). Cover impact, timeline, ownership/comms, and reconciliation notes, and call out any cross‑source conflicts or normalization issues.
```

### 989. D7_g233_zh (domain=D7, difficulty=7)

```
我们有一起线上事故，相关数据在四份文件里：`service_logs.csv`（支付和认证微服务的日志）、`config_changes.json`（配置变更记录）、`tickets.csv`（工单）、`on_call_schedule.csv`（值班排班）。请帮我做三个方向的并行分析，然后合成一份决策简报 `decision_brief.md`，里面要包括优先级建议（最多三条），每条建议附上关键数据支撑。

分析方向：
1. 从日志里弄清楚事件影响了多少用户、支付服务的错误率、持续了多久、波及了几个微服务。
2. 结合日志和配置变更记录，定位是哪次配置改动导致的问题、首次报错时间、有没有回滚、以及从改配置到出错的间隔、从出错到消退花了多久、事件前还有多少配置变更。
3. 看工单和值班表：关键工单有没有违反SLA、有响应的工单平均响应时间、事件开始时谁在值班、总工单数。

最后把这些结果整合到一份简报里，不用太死板，但要清晰可验证。
```

### 990. D7_g24_zh (domain=D7, difficulty=7)

```
我需要你基于以下文件做一次生产事故与流程影响调查：inputs/incidents_api.csv、inputs/api_events.jsonl、inputs/integrations_config.json、inputs/tickets.csv、inputs/comms_log.md。输出三个东西：一份事故时间线摘要（markdown）、一份影响与风险汇总（JSON）、一份面向负责人和沟通状态的核对表（CSV）。目标是整合多源信息，形成可执行结论。
```

### 991. D7_g278_zh (domain=D7, difficulty=7)

```
基于以下事故与沟通资料，我需要你整理一次跨服务事故复盘的最终汇总，输出三个紧凑文件：`summary.json`、`timeline.md` 和 `impact.csv`。不要输出原始明细或整段日志复制。

这批材料覆盖 2026-05-18 到 2026-05-19 凌晨的 8 起关联事故，涉及 `api-gateway`、`billing-webhook`、`report-archive`、`auth-session`、`worker-scheduler` 等服务。你需要把事故影响、时间线、owner/沟通情况串起来，形成适合发给管理层和相关团队的简报。

输入文件如下：
- `incidents.xlsx`：事故主表，含 opened/detected/ack/resolved/last_update 时间、严重级别、受影响用户数估计、工单数、owner_team。
- `tickets.xlsx`：相关工单/沟通记录，含 channel、owner、message_type、created_at。注意该表中同一 `ticket_id` 可能存在重复行，需去重处理（每个 ticket_id 只计一次）。
- `postmortem_actions.csv`：复盘行动项，含 owner、due_date、status、priority。
- `config_snapshot.json`：当前集成与路由配置，含服务到团队/值班的映射。
- `api_gateway_events.log`：大日志文件，混合正常流量与异常片段。你需要定位与事故相关的异常行：仅统计 `incident_id` 出现在日志行中且 `status` 为 500/502/503/504/429 的行。忽略无法解析 status 或 incident_id 的坏行。
- `incident_support.sqlite`：支持工单库，用于验证事故对应的支撑案例数量。

请按以下规则计算并输出结果（所有时间字段均为 UTC ISO8601，直接比较）：

1. **事故统计**：统计事故总数、SEV1 数、SEV2 数、SEV3 数（从 incidents.xlsx 中按 severity 字段归类）。
2. **确认延迟**：计算 `ack_delay_minutes` 的全体平均值，定义为 `ack_at - detected_at` 的分钟数；若为负数则按 0 处理；保留 2 位小数。
3. **解决延迟**：计算 `resolve_latency_minutes` 的全体平均值，定义为 `resolved_at - ack_at` 的分钟数；若为负数则按 0 处理；保留 2 位小数。
4. **最高影响事故**：找出受影响用户数估计（`impact_estimated_users`）最高的 3 起事故，按该值降序排列；并列时按 `incident_id` 字典序升序。
5. **行动项状态**：统计 `postmortem_actions.csv` 中 `status=done` 的行动项数量；以及逾期未完成行动项（`status != done` 且 `due_date < 2026-05-30`，按 UTC 比较）的数量。
6. **工单沟通**：统计 `tickets.xlsx` 中每个事故的沟通记录数（去重后的 ticket_id 计数），指出沟通记录数最多的事故 ID；如并列，按 incident_id 字典序升序。
7. **日志异常行**：从 `api_gateway_events.log` 中找出与事故相关的异常行（上述过滤条件），统计这些相关异常行的总数，以及其中涉及的不同 `incident_id` 数量。
8. **支撑案例**：统计 `incident_support.sqlite` 中与 8 起事故有关的支撑案例总数（按 incident_id 去重后，再按行计数，不去重 case_id，即统计所有符合条件行的数量）。
9. **活跃集成**：统计 `config_snapshot.json` 中仍处于 `enabled=true` 的集成数量，并列出其名称，按名称字典序升序。
10. **最早逾期行动项所属事故**：仅考虑 `status != done` 的行动项，找出其中 `due_date` 最早的日期（UTC），返回该日期对应的所有 `incident_id` 列表，按 incident_id 字典序升序。

输出文件要求：
- **summary.json**：包含上述 10 项结果，字段名清晰，适合机器读取。
- **timeline.md**：一段简短的事故时间线摘要，按时间顺序合并 `incidents.xlsx`、`tickets.xlsx` 和日志中的异常片段，至少列出 5 个关键时间点，明确标出哪个服务/哪个事故在何时出现、何时升级、何时缓解、何时恢复。
- **impact.csv**：一个不超过 12 行的汇总表，至少包含列：`incident_id, service, severity, impact_estimated_users, ticket_count, support_case_count, owner_team`。按 `impact_estimated_users` 降序排序，无需多余的格式化（如保留小数位数仅对必要数值字段按实际值输出）。

请直接完成检索、归并和核算，生成上述三个文件。
```

### 992. D7_g320_zh (domain=D7, difficulty=7)

```
我需要你基于四个输入文件——`inputs/incidents_log.csv`、`inputs/service_metrics.xlsx`、`inputs/tickets.json`、`inputs/change_log.md`——完成一次事故调查分析。3月18日下午发生了涉及卡片绑定/支付认证链路的严重事故，随后又有两个相关事件。把四个文件交叉对照，处理异常数据，输出一份简短决策简报 `decision_brief.md`，用于复盘会。简报要包含结论摘要、关键证据数字、决策建议和风险备注，并明确给出排名第一的后续改进建议。
```

### 993. D7_g371_en (domain=D7, difficulty=7)

```
I need you to investigate the production outage on 2025-01-15. Use the files app_logs.xlsx, config_changes.xlsx, deployment_history.xlsx, incident_tickets.csv, ticket_events.csv, and alert_history.csv. Produce a findings.md report and an evidence.csv table covering impact assessment (blast radius, error rates, services), timeline reconstruction (chronology with discrepancies), and owner/comms tracking (response time, escalation path). Include key numbers and cross-source conflicts.
```

### 994. D7_g378_zh (domain=D7, difficulty=7)

```
基于 inputs/incidents.xlsx、inputs/tickets.json、inputs/postmortem_actions.csv、inputs/api_gateway_logs.txt 和 inputs/integration_snapshot_2024-05-15.md，做一次事故/运维调查，覆盖 5月12日至15日 payments-api、identity-sync 及集成链路的高优先级波动。管理层需要影响评估、时间线复原以及 owner/沟通责任分析，最终输出一份单文件决策简报，文件名自定（如 decision_brief.md）。简报应给出 payments-api、identity-sync 及 onboarding 相关集成链路的优先级排序建议，明确 owner、内外部沟通负责人，以及需加速的行动项。建议需引用关键量化支撑（如 SEV1 数量、P1 超 SLA 工单、响应时间均值、风险降分汇总、异常日志条数等），至少涵盖5个独立数字。如有数据异常也需指出。不需要输出明细表或分步清单，只要收敛后的排序决策。
```

### 995. D7_g398_en (domain=D7, difficulty=7)

```
I need you to look at the files in inputs/ — incident_events.csv, api_workflow_logs.csv, tickets.csv, services_config.csv, ops_incident.db, and postmortem_draft.md — to reconstruct the incident, assess its impact, and produce three compact summary reports: a Markdown incident narrative, a CSV timeline/impact summary, and a JSON owner/comms tracking file. Cover the key metrics (ticket counts, affected services, event timeline, API failures, owner workload, etc.) without dumping raw data.
```

### 996. D7_g510_zh (domain=D7, difficulty=7)

```
昨天 (2024-03-15) 我们 payment-service 的 v2.4.1 上线后出了一次比较严重的事故,需要你带队做事故复盘 (postmortem)。原始数据已经放在 inputs/ 目录下:`deploys.json`、`alerts.xlsx`、`transactions.csv`、`service_logs.csv`、`tickets.xlsx`、`service_catalog.json`、`oncall_schedule.xlsx`。

请按我们组里一贯的口径来算,别自己发明定义:

- **事故起点 T_start** 取这次 payment-service 引入问题的那次 deploy 的 `deployed_at` (UTC),**事故终点 T_end** 取后续 payment-service 那次 `status=="rollback"` 的 deploy 时间。事故窗口对 transactions/logs 用 **[T_start, T_end)** (左闭右开),对客服工单用 **[T_start, T_start+4h]** (两端均含)。
- **MTTD** = T_start 到事故窗口内首次 SEV1 或 SEV2 告警的分钟数 (整数,四舍五入)。alerts 在统计前按 `(fired_at, service, metric)` 三元组**去重**,丢掉重复信号。
- **MTTR** = T_end - T_start (分钟,整数)。
- **影响交易** = `status=='failed'` 且 `created_at` 落在事故窗口的笔数;**收入影响**为这些交易的 `amount_usd` 之和,保留 2 位小数;**爆炸半径**为这些失败交易涉及的 distinct `user_id` 数。
- **首责服务** = 事故窗口内 `level=='ERROR'` 日志条数最多的 service;再到 `service_catalog.json` 拿到对应的 owning team,并到 `oncall_schedule.xlsx` 里查 T_start 落在哪个值班区间 (`shift_start <= T_start < shift_end`) 来确定值班工程师。
- **工单口径**: 只统计 category 落在我们标准闭集里的那些,集合就是 `["payment_declined","extra_charge_on_statement","transfer_failed","app_crash","slow_response","refund_pending","login_issue","card_blocked"]` —— 集合外的 (例如 `other_misc`) **不计**。注意 tickets 里有非 UTC 时区的时间戳,统一换算到 UTC 再做窗口判断。给出窗口内总工单数和占比最高的 category。
- 顺便列一下窗口内**至少出现 1 条 ERROR 日志的 service 集合** (排序后)。

最终交付两个文件,放在输出根目录:

1. `incident_report.md` —— 一页纸事故简报,包含事故起止时间、bad deploy / rollback deploy 的 ID、MTTD、MTTR、首责服务和 owning team、值班工程师、影响交易数、收入影响、爆炸半径、窗口内工单数与 top category、涉事服务清单。
2. `impact_summary.json` —— 上述关键聚合量的机器可读版本 (扁平 JSON,字段名见 spec_detailed)。

数据量不算大但跨源对账比较啰嗦 (告警去重、时区、闭集过滤、值班区间匹配),建议拆几路并行做完再汇总。
```

### 997. D7_g564_en (domain=D7, difficulty=7)

```
Need a Jan-2024 incident retrospective from inputs/incidents.xlsx, inputs/tickets.json, inputs/postmortems.md, inputs/status_page.xlsx, and inputs/alerts.log. Give me findings.md (the brief) plus evidence_table.csv (per-service roll-up: impact_minutes, ticket_count, overdue_action_items, risk_score). Use sev-weighted impact-minutes (SEV1=3, SEV2=2, SEV3=1; resolved incidents only) and composite service risk = 0.5*impact + 0.3*overdue_AIs + 0.2*tickets, each axis normalized to its max across services; pick top 3. MTTR is SEV1+SEV2 only, in minutes. Snapshot date for 'overdue' = 2024-02-01. Bucket tickets into {card_linking, card_arrival, exchange_rate, transfer_failed, login_issue, other}. Flag every SEV1 with no status_page entry and count orphan status_page refs (incident_ref not in incidents.xlsx).
```

### 998. D7_g596_zh (domain=D7, difficulty=7)

```
您好，我是产品部门的张经理。我们刚经历了一次严重的线上故障，支付网关服务在3月2日下午出现大面积失败，导致许多客户无法完成支付。我需要一份全面的故障调查报告，不需要技术细节，但要能回答以下几个问题：

1. **商业影响**：这次故障影响了多少客户？收入损失大概有多少？其他服务（比如认证服务）有没有连带受损？我们跟客户签的SLO是否被违反？（请将收入损失定义为所有critical级别的PAYMENT_FAILED错误中金额超过1000美元的订单金额总和。受影响的客户指这些订单对应的不重复客户ID。SLO违规指auth服务在3月3日早8点到8点05分之间的critical TIMEOUT错误次数。）

2. **时间线**：到底什么时候开始出问题？什么时候结束？故障根因是什么配置变更？什么时候拉起的事故工单？请给出精确时间点和配置变更ID。

3. **响应情况**：我们的事故管理团队响应速度如何？平均多久回复的？这次事故是谁在负责？请计算所有critical工单的首次响应时间（工单创建到首次回复的分钟数）的平均值，并给出针对事故INC-001的指派团队。

我需要你产出三份文件：
- `impact_report.json`：包含上面“商业影响”部分的所有指标和总结。
- `timeline.json`：包含“时间线”要求的全部时间点、变更ID和一句根因说明。
- `comms_report.csv`：包含“响应情况”的统计数据，以及所有critical工单的明细（至少包括工单ID、创建时间、响应时间、指派团队）。

数据在inputs文件夹下：error_logs.xlsx（主日志，有20万条记录）、config_changes.json（配置变更历史）、incident_tickets.csv（工单记录）、services.yaml（服务依赖）。请你团队分工协作，尽快给我报告。
```

### 999. D7_g62_en (domain=D7, difficulty=7)

```
Hey, could you take a look at this set of exports from the synthetic ops review? We've got incident data, logs, configs, and ticket records. I need you to dig into the incidents, spot the key anomalies, and then piece together the most likely root cause with a clear timeline.

Here's what I'm after:

- A rundown of the main incidents, with the unusual patterns that stand out (e.g., any weird timing, repeated failures, or config mismatches).
- Your best root‑cause hypothesis, backed by specific log/ticket evidence that ties the incidents together.
- A chronological timeline showing what happened and when, based on the timestamps you find.
- Any system or process changes you see that could have prevented this, especially from the config side.
- Deliver it as a short write‑up (couple of pages max) – bullet points and a simple timeline are fine – no need for formal prose.
```

### 1000. D7_g65_zh (domain=D7, difficulty=7)

```
我需要你基于 `inputs/incidents.csv`、`inputs/incident_events.csv`、`inputs/api_logs.xlsx`、`inputs/tickets.json` 和 `inputs/comms.md`，完成一次面向管理层的事故复盘与运营影响核对。输出三个文件：`incident_summary.json`（汇总主事件 INC‑4801 的影响、时间线、处置状态与建议）、`owner_and_comms.csv`（整理工单归属、未分配事项及需要补发/追踪的沟通对象）、`risk_snapshot.md`（按服务维度的风险快照与后续动作）。具体统计包括：INC‑4801 在 opened_at 起始后 60 分钟窗口内（左闭右开）的唯一受影响请求数；列出直接相关服务名并字母序升序；统计 pay_core 的 5xx 响应总数（先去 status 字段首尾空格再转数值）；识别全量日志中异常记录（latency_ms<0、原始 status 与去空格后不一致、request_id 重复）；给出重复 request_id 列表（字母序升序）；计算从首个
```

### 1001. D7_g980542_en (domain=D7, difficulty=7)

```
I need a decision brief based on three files: incident_cases.xlsx, incident_timeline.pdf, and incident_comms.docx. I want you to assess the incident impact, reconstruct the timeline, and track ownership and communications, then produce a single brief recommendation file called decision_brief.md.

Please treat the incident scope as the active payment-processing integration used for subscription payments and checkout events. I want the final recommendation to be ranked and supported by the key numbers from the evidence, not just a narrative. I also want you to explicitly account for three anomaly scopes: duplicate incident references, conflicting severity labels between the case log and the timeline notes, and a missing ticket owner on one of the customer-facing updates. Use the same incident window across all files, and if there are reopenings, count them as a separate incident recurrence only when the case record says it was reopened. For impact, count only customer-facing checkout/payment incidents in the defined window, and for the comms analysis, only count messages that were actually sent, not drafts. The deliverable should recommend the best operational decision for the incident review, with the reasoning tied back to the computed figures.
```

### 1002. D7_g980568_zh (domain=D7, difficulty=7)

```
请基于 inputs/ops_incident_bundle.xlsx、inputs/integration_config_snapshot.xlsx、inputs/incident_timeline_and_comm.xlsx 做一次这起订阅计费告警的事故梳理，最后只输出一个 compact 的汇总报告文件。我要看到影响范围、时间线复盘、负责人和沟通流转，以及你发现的关键异常点。
```

### 1003. D7_g980766_zh (domain=D7, difficulty=7)

```
我们最近发生了一次API集成事故，影响了多个服务。我这边有四个文件：集成配置、日志、工单和变更记录。请你帮我做一次彻底的调查分析，重点搞清楚：哪些服务受影响最严重？整个事故的时间线是怎样的？各负责人的响应效率如何？最后给我一个风险排序，告诉我应该优先处理哪些服务，具体建议是什么。最终输出一个简单的决策简报文件（decision_brief.md），里面列明关键数据和你的建议。
```

### 1004. D7_g980877_zh (domain=D7, difficulty=7)

```
我需要你把这次 2024-05-18 的线上事故做成一份可直接发给管理层和值班团队的综合报告，输入文件是 inputs/ops_event_log_large.csv、inputs/service_config.xlsx、inputs/incident_tickets_and_comms.xlsx。我希望你同时梳理影响范围、时间线、负责人和对外/对内沟通状态，最后输出一份中文的简明结论文档，以及一份包含汇总结果的表格文件。日志文件很大，相关异常只占很小一部分，请先定位事故窗口再做分析，不要把所有日志逐行展开。报告里需要明确写出：受影响的服务、每个工单的影响时长、日志里是否存在重复 trace、事故窗口内错误量最大的服务、配置里是否存在不在允许集合里的 sev_target、以及最早的有效 ack 是谁发出的。
```

### 1005. D7_g980894_zh (domain=D7, difficulty=7)

```
我需要你帮我把这次 INC-2024-0611 的事故做成一份决策简报，结合 incident_timeline.xlsx、workflow_config.xlsx、api_gateway_logs.xlsx 和 owner_comms_tickets.xlsx，把影响范围、时间线、配置变化、以及 owner 和沟通跟进情况串起来，最后给出一个按优先级排序的处置建议。我只要一份简短的结果文件。
```

### 1006. D7_g981102_en (domain=D7, difficulty=7)

```
I need a clean incident review package because leadership wants one compact summary of what happened, what was affected, and who still needs follow-up. Please use the three files in inputs/ — incidents_and_tickets.xlsx, api_gateway_logs.csv, and integration_config_and_comms.docx — and give me a single report file that pulls the story together. I want the final file to highlight the impact, the timeline, and any ownership or communication gaps, including the specific data issues we need to fix before we close this out.
```

### 1007. D7_g981122_zh (domain=D7, difficulty=7)

```
我在做这次线上故障复盘，想让你一起看这 3 个文件：inputs/incident_tickets.xlsx、inputs/api_gateway.log、inputs/ops_brief.docx。请把工单、日志和简报里的信息串起来，整理成一份简短但完整的事故分析报告，重点说明影响范围、关键时间线、当前责任人和对外沟通状态；另外把我需要优先跟进的异常也标出来，比如重复工单、长时间未处理的 open 工单、以及事故窗口内的错误和延迟情况。
```

### 1008. D7_g981126_zh (domain=D7, difficulty=7)

```
这次要把 5 月中旬那段支付/配置异常的排查结果一次性整理清楚，方便我向管理层和支持团队同步。请结合这些文件：incident_events.xlsx、config_integrations.xlsx、tickets.xlsx、ops_event_log.txt，输出一份合并报告，重点看四件事：影响范围、事件时间线、相关工单的负责人和沟通进度，以及第三方集成里哪些项目有异常、过期或安全风险。如果发现和 Stripe 订阅/checkout 相关的配置或服务有问题，也请把对应的 key 和结论写进去。
```

### 1009. D7_g981181_zh (domain=D7, difficulty=7)

```
请基于 inputs/incident_events.log、inputs/ops_bundle.xlsx、inputs/manifest.json 做一次完整的事故复盘，输出一份简洁的单文件汇总报告。我要看到影响范围、关键时间线、工单/负责人/沟通归属的对齐结果，并把文件里的异常样本一起核对清楚。
```

### 1010. D7_g981434_zh (domain=D7, difficulty=7)

```
我需要你帮我把这次 API 相关的运营事件梳理成一个可直接给管理层看的决策简报。请基于 inputs/incidents_tickets.xlsx、inputs/ops_logs.xlsx、inputs/integration_configs.xlsx 这三份文件，结合事故影响、时间线、票据/沟通归属和配置风险，判断现在应该先推进哪一条修复/缓解路径，并给出排序和理由。最后只要输出一个简短的 markdown 文件就行。
```

### 1011. D7_g981506_zh (domain=D7, difficulty=7)

```
我需要你帮我做一次这周故障复盘材料，输入是 inputs/incident_tickets.xlsx、inputs/api_event_log.xlsx、inputs/comms_threads.xlsx 和 inputs/workflow_config.xlsx。请你把工单影响、接口调用异常、沟通跟进和配置缺口一起串起来，最后输出一份 decision_brief.md，给出你建议优先处理的根因方向和对应的 owner/comms 处理顺序，并把你用到的关键数字写清楚。
```

### 1012. D7_g981538_zh (domain=D7, difficulty=7)

```
请基于 incident_event_log.txt、service_config_snapshot.xlsx 和 incident_tickets.xlsx 做一次完整的事故复盘整理，重点看影响范围、时间线、配置漂移和工单/对外沟通是否对齐。我需要你把关键结论收敛成一份可直接发给管理层和值班团队的简报。日志里混着大量正常流量和少量异常记录，别漏掉重复请求和边界时间点。
```

### 1013. D7_g981564_en (domain=D7, difficulty=7)

```
You are supporting an incident review for a payment-webhook degradation. Analyze the provided workbook files and summarize the incident using evidence from tickets, seed records, and logs.
```

### 1014. D7_g981667_en (domain=D7, difficulty=7)

```
I need a compact incident review packet for the auth-api event on 2024-11-18. Please review incidents.xlsx, logs.csv, config.yml, tickets.xlsx, and comms_thread.txt, then produce one consolidated report.
- Reconstruct the incident timeline and identify the main impact window.
- Summarize customer impact, log symptoms, and the key owner/ticket status trail.
- Check the comms thread for what was said and whether the response cadence looks complete.
- Call out any notable anomalies in the data that affect the timeline or ownership picture.
- Keep the output brief and decision-ready, since this is for a post-incident review.
```

### 1015. D7_g981710_zh (domain=D7, difficulty=7)

```
我需要你看一下这份排障包 `ops_incident_bundle.xlsx`，帮我把这次线上事件整理成一份简短但完整的复盘报告，重点把影响范围、时间线、工单/沟通归属和 API 工作流的异常串起来，最好能直接给我一个可以发给管理层的版本。我还想顺手把里面重复记录、状态不一致和对外沟通的冲突一起标出来。
```

### 1016. D7_g981740_en (domain=D7, difficulty=7)

```
Please review incidents_master.xlsx, comms_tracker.csv, and ops_events.jsonl and turn the incident package into a concise findings brief.
- Compare the incident timeline, impact, and communications across the files.
- Flag the explicitly relevant data quality issues that affect the incident story and owner tracking.
- Reconcile any mismatches between the spreadsheet, comms tracker, and event log, and call out where the sources disagree.
- Include a short recommended next-step section for ops follow-up.
```

### 1017. D7_g981795_zh (domain=D7, difficulty=7)

```
我需要你把这三份文件 incident_timeline.xlsx、ticket_comms_tracker.xlsx、api_workflow_postmortem.xlsx 串起来做一份事故复盘简报 findings.md，重点帮我梳理影响范围、时间线、负责人和沟通状态，并把各来源里不一致或时间顺序异常的地方单独写清楚。尽量按不同分析线并行看，最后合成一版可以直接发给管理层的结论。
```

### 1018. D7_g981907_zh (domain=D7, difficulty=7)

```
我需要你帮我把这次 2024-05-21 的线上 incident 做成一份合并报告，输入看这三个文件：inputs/ops_incident_bundle.xlsx、inputs/api_events.csv 和 inputs/incident_briefing.docx。重点把影响面、时间线、owner/comms 这三块串起来，顺便把里面明显的重复/不一致点标出来，最后输出一份可以直接发给管理层的简洁汇总。
```

### 1019. D7_g983174_zh (domain=D7, difficulty=7)

```
请基于 inputs/incident_ops_pack.xlsx、inputs/workflow_policy_and_notes.xlsx 和 inputs/incident_postmortem_memo.pdf，整理一份 findings.md。我要的是一份能直接拿去开复盘会的分析 brief：把影响面、时间线、owner/comms 追踪和配置口径冲突都讲清楚，并且把你发现的异常点单独列出来。文档里要明确写出跨文件的对照结论，尤其是 ticket、log、config 之间哪些地方一致、哪些地方不一致。
```

### 1020. D7_k982051_zh (domain=D7, difficulty=7)

```
请基于文件 speedwall10__iot-device-network-logs__Preprocessed_data.csv 做一份面向 IT 运维/日志与事件分析的深度分析，重点围绕时间序列和趋势变化来展开。请直接使用这些真实列：frame.number、frame.time、frame.len、eth.src、eth.dst、ip.src、ip.dst、ip.proto、ip.len、tcp.len、tcp.srcport、tcp.dstport、Value、normality。我要你帮我看：1）按 frame.time 的先后，把流量和异常程度做时间趋势分析，找出最活跃和最异常的时间段；2）比较不同 normality 等级在时间上的分布和变化，看看是否存在异常激增或阶段性漂移；3）从协议和端口维度拆解时间变化，识别哪些协议/端口在不同阶段贡献了主要流量；4）从源/目的 IP 维度梳理通信关系在时间上的变化，找出高频对话是否与异常值同步；5）结合 frame.len、ip.len、tcp.len、Value 做跨指标的趋势与相关性分析，判断哪些指标最能解释异常波动；6）输出可供后续排障的结论：哪些时间窗口、协议、端口、IP 对组合最值得优先排查。请把结果整理成可执行的分析摘要，并确保结论只基于数据本身，不要编造任何背景。
```

### 1021. D7_k982233_en (domain=D7, difficulty=7)

```
Use the file speedwall10__iot-device-network-logs__Preprocessed_data.csv and analyze it like an IT ops / incident analytics log review, with the main focus on temporal behavior in the sequence fields frame.time and frame.number. I need a practical readout of how traffic and suspicious states evolve over time: identify any bursts, regime shifts, and period-over-period changes in packet characteristics, and separate normal vs non-normal behavior using the normality flag. Please break this into independent workstreams so different analysts could handle them in parallel: one track on time-bucketed traffic volume and packet-size trends, one on normality/incident-state transitions over time, one on protocol/port mix shifts over time, one on source/destination entity concentration over time, and one on outlier or anomaly-like rows that coincide with abrupt temporal changes. Keep it operational and concise, but grounded in the actual columns frame.number, frame.time, frame.len, eth.src, eth.dst, ip.src, ip.dst, ip.proto, ip.len, tcp.len, tcp.srcport, tcp.dstport, Value, and normality.
```

### 1022. D7_k982342_zh (domain=D7, difficulty=7)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维 / 日志与事件分析的多阶段分析，重点放在“数值字段的相关性与驱动因素”上：请找出哪些数值列彼此最相关、哪些业务场景下相关性更强、以及哪些字段组合最能解释异常/可疑流量特征。希望你把分析拆成几个彼此独立的方向，便于并行处理，并最终输出一份可直接给运维/安全团队看的结论摘要（例如 analysis_summary.json）。请特别关注这些真实列：Duration、Src Pt、Dst Pt、Packets、Tos、Flows、Bytes（注意 Bytes 当前是字符串但包含数值）、以及 class、Proto、Flags、Src IP Addr、Dst IP Addr、attackType、attackID、attackDescription。分析时请给出相关系数（保留 2 位小数）、Top 关联对、按 class / Proto / Flags 分组后的差异，以及对可疑流量的驱动因素解释。
```

### 1023. D7_k982606_zh (domain=D7, difficulty=7)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维 / 日志与事件分析的异常排查报告，重点围绕“显式数值规则”的异常与离群检测来查找可疑流量和潜在事件。请直接使用现有字段：Date first seen、Duration、Proto、Src IP Addr、Src Pt、Dst IP Addr、Dst Pt、Packets、Bytes、Flows、Flags、Tos、class、attackType、attackID、attackDescription。任务请拆成 4-6 条彼此独立的分析线，方便不同子任务并行：1）基于 Duration、Packets、Bytes、Flows 的极端值/离群值识别（例如 IQR、P95、P99、超阈值计数）；2）基于 Src Pt、Dst Pt 的异常端口与稀有端口模式识别（例如高频端口、极端端口值、端口范围外/异常稀有值）；3）基于 Proto、Flags、class、attackType 的稀有类别与可疑组合分析（例如低频协议、罕见 flags、异常标签组合）；4）按 Src IP Addr / Dst IP Addr 聚合的高风险主机画像（例如单个主机产生的异常流量集中度、离群主机、最活跃可疑源/目的）；5）按日期（Date first seen）做时间切片，找异常在时间上的集中爆发与跨日变化；6）如有必要，结合 Bytes、Packets、Duration 的比值或相关性检查“短时高包/高字节”与“长时低包/低字节”的异常模式。请输出一个可执行的分析结论摘要，并给出明确、可复核的数值阈值和统计口径。
```

### 1024. D7_k982624_en (domain=D7, difficulty=7)

```
Using kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv, I need an ops-ready incident analytics pass focused mainly on distribution and threshold cohorts. Please break it into independent tracks so a small team can work in parallel: 1) volume segmentation by Duration, Packets, Bytes, and Flows against business thresholds and quantile buckets; 2) suspicious vs normal mix shares across those cohorts; 3) protocol and flag composition inside the high-risk threshold buckets; 4) source and destination port concentration in the extreme tails; 5) time-of-day / day-level clustering of threshold exceedances from Date first seen; 6) any cross-feature pattern that helps explain which flows are most likely to land in the top cohort. Keep the analysis grounded in the real columns (Date first seen, Duration, Proto, Src IP Addr, Src Pt, Dst IP Addr, Dst Pt, Packets, Bytes, Flows, Flags, Tos, class, attackType, attackID, attackDescription) and make the conclusions directly usable for incident triage.
```

### 1025. D7_k982644_zh (domain=D7, difficulty=7)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维 / 日志与事件分析的多阶段分析报告，重点围绕“排名与集中度”展开：先找出最主要的流量来源、目的地址、协议和端口的 Top-N 贡献，再量化这些 Top 群体对总流量/总包数/总会话数的占比，判断是否存在明显的长尾或 Pareto 集中现象。请结合真实列（Date first seen、Duration、Proto、Src IP Addr、Src Pt、Dst IP Addr、Dst Pt、Packets、Bytes、Flows、Flags、class、attackType、attackID、attackDescription）输出可直接交付给值班/安全运营同事的结论，并把分析拆成多个彼此独立的子任务，方便并行处理：一条线看来源侧集中度，一条线看目的侧集中度，一条线看协议/端口组合集中度，一条线看 suspicious vs normal 的分布差异，一条线看高流量/高包数连接的集中度与异常特征。最后请给出一个简洁的结论：哪些对象最集中、集中度有多高、是否需要优先排查。
```

### 1026. D7_k982984_zh (domain=D7, difficulty=7)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维/日志与事件分析的异常排查简报，重点围绕“显式数值规则”的异常与离群检测来展开。请先快速判断这批外部流量日志里哪些记录最像异常连接，再按可落地的规则拆成几条独立分析线：例如用 Duration、Packets、Bytes、Src Pt、Dst Pt、Flows、Tos 的阈值/IQR/极端值找异常；结合 Proto、Flags、Src IP Addr、Dst IP Addr、Dst Pt、class、attackType/attackID/attackDescription 识别稀有类别和高风险组合；再看按天或按时间段的异常集中度；最后汇总哪些规则最能解释 suspicious/normal 的差异。请输出适合给值班同学直接看的结论，并附上可复核的统计结果。注意：所有判断都必须基于现有数据，不要臆造任何值。数据列包括 Date first seen、Duration、Proto、Src IP Addr、Src Pt、Dst IP Addr、Dst Pt、Packets、Bytes、Flows、Flags、Tos、class、attackType、attackID、attackDescription。
```

### 1027. D7_k983016_zh (domain=D7, difficulty=7)

```
请基于数据文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维/日志与事件分析的实战分析，重点围绕“分布与阈值分层”（例如高于/低于业务阈值的次数、分位数桶、以及各层占比）来判断这批外部周日志的风险与流量结构。请直接使用现有字段：Date first seen、Duration、Proto、Src IP Addr、Src Pt、Dst IP Addr、Dst Pt、Packets、Bytes、Flows、Flags、Tos、class、attackType、attackID、attackDescription。我要你把分析拆成可并行执行的 4-6 条独立分析线，并最终汇总成 analysis_summary.json。请重点回答：1）Duration、Packets、Bytes、Dst Pt 在不同阈值/分位数下的分布和占比；2）不同 class / Proto / Flags 的结构差异；3）按源/目的端口和 IP 的高频集合是否集中；4）异常样本在这些阈值层中的集中程度；5）可操作的运维告警阈值建议（基于数据分布而不是拍脑袋）。
```

### 1028. D7_k983031_en (domain=D7, difficulty=7)

```
Analyze the file speedwall10__iot-device-network-logs__Preprocessed_data.csv for incident-ops trends and anomaly behavior. I need a temporal/sequencing-focused review first: quantify how traffic changes across the frame.number sequence and frame.time, identify any period-over-period shifts in frame.len, ip.len, tcp.len, and Value, and flag whether normality changes over the run. Please break this into separate workstreams so different analysts can run independently: one track on overall time/sequence trends and change points, one on protocol/port behavior over time, one on source/destination concentration and drift, one on anomaly/normality progression, and one on correlations between traffic size fields and Value. Use the real columns in the dataset exactly as named, and keep the output suitable for an IT ops incident summary.
```

### 1029. D7_k983136_zh (domain=D7, difficulty=7)

```
请帮我分析文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv（已加载为 df），重点围绕时间/序列趋势做一次 IT 运维/日志与事件分析：把 Date first seen 当作时间主轴，结合 class、attackType、Proto、Src IP Addr、Dst IP Addr、Src Pt、Dst Pt、Packets、Bytes、Flags、Duration、Tos 等字段，找出这一周内外部流量与可疑事件的时间分布、峰值时段、日内变化、异常协议/端口在不同时间段的变化，以及不同攻击/正常/unknown 的趋势差异。希望输出可直接给运营值班和安全分析使用的结论摘要、重点时间窗、以及可疑连接的变化特征，并尽量把分析拆成多个互不依赖的子任务，方便并行处理。
```

### 1030. D7_k983142_zh (domain=D7, difficulty=7)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维 / 日志与告警分析的多维排查报告，重点围绕“分布与阈值分层（超过/低于业务阈值的计数、分位数组、占比结构）”展开。请直接使用现有字段：Date first seen、Duration、Proto、Src IP Addr、Src Pt、Dst IP Addr、Dst Pt、Packets、Bytes、Flows、Flags、Tos、class、attackType、attackID、attackDescription。我要你把数据切成 4-6 个彼此独立的分析轨道，适合分给多个子分析器并行做：1）按 class / attackType 看正常与可疑流量的总量、占比、以及在阈值上的分层；2）按 Duration、Packets、Bytes、Flows 做分位数桶和阈值上下穿越统计，找出长连接/大流量/高包数会话的占比；3）按 Proto、Flags、Dst Pt、Src Pt 看不同通信模式在阈值上的分布差异；4）按时间粒度（Date first seen）观察各时段可疑流量占比及高阈值会话集中度；5）按 Src IP Addr / Dst IP Addr 做 Top-N 集中度与阈值覆盖率分析，识别是否少数主机贡献了大部分异常；6）如果存在明显空值或占位值，也请统计其占比并判断是否影响阈值分层。最后请输出一个能给管理层看的简洁结论：哪些阈值最能区分 suspicious 与 normal、哪些桶/类别最值得优先排查。
```

### 1031. D7_k983198_zh (domain=D7, difficulty=7)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维 / 日志与事件分析的实战分析，重点围绕“分布与阈值分层”来判断哪些流量形态更值得优先排查。请直接用表里的真实字段（Date first seen, Duration, Proto, Src IP Addr, Src Pt, Dst IP Addr, Dst Pt, Packets, Bytes, Flows, Flags, Tos, class, attackType, attackID, attackDescription）完成分析，不要编造任何值。我要的不是泛泛总结，而是能支持处置决策的分层结果：请按业务阈值、分位数桶、占比结构、协议/标志组合、目的端口集中度来拆解，识别高字节/高包数/长持续时间/异常端口的组合特征，并比较 normal、unknown、suspicious 三类流量在这些阈值上的差异。最终输出请以 analysis_summary.json 的形式组织，方便我直接交给值班同事和 SOC 做复核。
```

### 1032. D7_k983276_zh (domain=D7, difficulty=7)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维/日志与事件分析的多阶段分析，重点围绕时间趋势和周期变化。请直接使用字段 Date first seen、Duration、Proto、Src IP Addr、Src Pt、Dst IP Addr、Dst Pt、Packets、Bytes、Flows、Flags、Tos、class、attackType、attackID、attackDescription，完成以下工作：1）按日期粒度梳理 normal / suspicious / unknown 的日趋势、环比变化和峰值时点，识别异常波动；2）按小时粒度分析当天不同时段的流量/会话活跃度变化，并比较 suspicious 与 normal 的时段分布差异；3）按 Proto、Dst Pt、Flags 这些日志特征分组，找出在时间上增长最快或最集中的模式；4）按 Src IP Addr 和 Dst IP Addr 识别重复出现的高频来源/目标，并观察其在时间上的持续性；5）检查 Bytes、Packets、Duration 的趋势关系，判断是否存在短时高包量、长时低包量等异常形态；6）结合 attackType、attackID、attackDescription 对 suspicious 记录做时间聚集分析，给出最值得关注的时间段和特征组合。请输出一份可供值班分析和后续告警规则设计使用的结构化结果。
```

### 1033. D7_k983278_zh (domain=D7, difficulty=7)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一份面向 IT 运维/日志与事件分析的异常审计。重点围绕“显式数值规则”的异常与离群检测来展开：例如按 Duration、Packets、Bytes、Src Pt、Dst Pt、Flows、Tos 设定阈值/IQR/极端值/稀有类别规则，识别 suspicious vs normal 的差异，找出最异常的连接、最稀有的协议/标志组合，以及按源/目的地址聚合后的异常热点。请把结论拆成多个独立分析轨道，便于不同小组并行推进：1）数值字段的极端值与 IQR 离群点；2）按 class 的异常比例和阈值命中率；3）稀有 Proto/Flags/attackDescription 组合；4）按 Src IP Addr、Dst IP Addr 聚合的高风险热点；5）按时间 Date first seen 的异常时段分布；6）字段缺失、类型清洗和 Bytes 字段数值化后的影响。最后输出一份可直接给值班经理看的简明总结，并附上可复核的统计结果。
```

### 1034. D7_k983574_en (domain=D7, difficulty=7)

```
Using the file mirzayasirabdullah07__api-failure-intelligence-dataset-afid__api_error_logs_with_root_causes_220k_rows.csv, do a root-cause-oriented incident analytics deep dive for IT ops with emphasis on correlation and driver analysis. I want you to identify which numeric fields move together, where strong positive/negative correlations show up, and which categories tend to amplify latency, retries, and failed recovery. Please split the work into 4-6 independent tracks so it can be run by a small analyst team: (1) numeric correlation map and strongest pairwise relationships across latency_ms, request_size_bytes, response_size_bytes, retry_count, and thread_id; (2) latency/retry drivers by status_code, error_type, and root_cause; (3) environment and region effects on failure patterns and recovery success; (4) log-level and resolution_action associations with root_cause and retry outcomes; (5) missingness/data-quality scan on key categorical fields that may bias the analysis. Use the actual columns in the dataset, keep everything deterministic, and provide compact outputs that could be turned into an analysis_summary.json.
```

### 1035. D7_k984345_zh (domain=D7, difficulty=7)

```
请基于文件 niladriroy0__failure-cascades-in-cloud-cost-optimization__failure_cascades_cloud_cost_optimization.csv 做一次面向 IT 运维 / 日志与事故分析的深度排查，重点围绕“排名与集中度”展开：我想知道哪些 system_regime、哪些高成本/高故障样本、以及哪些参数组合最集中地贡献了累计失败请求、成本超支和客户流失风险。请把分析拆成 4-6 个彼此独立的分析轨道，适合并行给不同子任务做。请至少覆盖：1）按 system_regime 的样本占比、失败请求占比、cost_overrun_debt 占比；2）按累计失败请求/成本超支/客户流失风险的 Top-N 记录及其集中度（Top 5、Top 10 之类）；3）“高风险”阈值下（例如累计失败请求或 customer_churn_risk 的高分位）各 regime 的集中情况；4）关键运维变量（如 spot_instance_fraction、traffic_spike_intensity、warm_instance_pool、billing_signal_latency）与高风险样本的关系；5）按参数分桶后查看风险是否呈现 Pareto/少数桶贡献多数损失的模式。请输出一份结构化的 analysis_summary.json。务必基于真实数据，不要臆造任何数值。
```

### 1036. D7_k984442_zh (domain=D7, difficulty=7)

```
请基于文件 kartikjaspal__server-logs-suspicious__CIDDS-001-external-week1.csv 做一版面向 IT 运维 / 日志与事件分析的深度分析，重点围绕“数值字段之间的相关性与驱动因素”展开：先判断 Duration、Packets、Bytes、Flows、Src Pt、Dst Pt、Tos 这些数值字段谁和谁移动最一致，再找出最强的正/负相关对，并结合 class、Proto、Flags、attackType 的分布解释这些关联在正常/unknown/suspicious 记录里是否不同。希望输出能直接支持告警规则和排查优先级，包括：整体相关矩阵、按 class 分组后的相关性差异、关键端口/协议/标志位组合与高流量/长持续时间的关系，以及哪些字段最适合作为异常流量的驱动指标。请把结论拆成可并行处理的几个分析块，最后汇总成一份可交付的分析摘要。
```

### 1037. D7_k984697_en (domain=D7, difficulty=7)

```
Analyze the file supplejade__rt-iot2022real-time-internet-of-things__RT_IOT2022.csv for IT ops / logs and incident analytics, with the main focus on temporal or sequence-based trend behavior using the sequence/index field no as the ordering proxy. I want a multi-part review of how attack types, protocol/service mix, traffic rates, and packet/header patterns change over the sequence, including period-over-period shifts, concentration changes, and any notable spikes or regime changes. Please break the work into independent tracks so separate analysts can work in parallel, and summarize the findings in analysis_summary.json using the real columns such as no, proto, service, flow_duration, fwd_pkts_per_sec, bwd_pkts_per_sec, flow_pkts_per_sec, down_up_ratio, packet/header counts, and Attack_type.
```

### 1038. D7_k984724_zh (domain=D7, difficulty=7)

```
请基于文件 djaouadnm__nasa-website-data__nasa_aug95_c.csv 做一份面向 IT 运维/日志与事件分析的分层阈值分析，重点围绕访问量分布、业务阈值 cohort、分位数组、以及不同区间的流量占比来做。数据列包括 requesting_host、datetime、request、status、response_size。我要你重点回答：1）不同响应大小阈值下的请求分布和占比；2）按日与按小时的高流量 cohort 识别；3）状态码在各阈值 cohort 中的混合占比；4）请求路径类型在不同分位数组中的差异；5）高响应/低响应请求对总体流量的贡献；6）找出最值得关注的异常集中区间。请把结果整理成可直接给管理层看的分析摘要。请按独立分析轨道拆分，方便不同子任务并行处理。
```

### 1039. D7_k984750_zh (domain=D7, difficulty=7)

```
请基于文件 djaouadnm__nasa-website-data__nasa_aug95_c.csv 做一份面向 IT 运维 / 日志与事件分析的深入诊断，重点放在“相关性与驱动因素分析”上：找出哪些数值字段彼此一起变化、哪些状态码与响应大小/访问时间存在关联，以及不同主机、时间段和请求类型是否会影响这些关系。请结合真实列 requesting_host、datetime、request、status、response_size，输出一份可直接给运维/事故响应团队使用的分析结论。希望你把任务拆成 4-6 个彼此独立的分析轨道，便于分工并行执行；每个轨道都要能回答一个明确问题，比如：1）整体数值字段相关性与最强关联对；2）按状态码分组的响应大小差异及异常状态；3）按小时/日期切片观察请求量、平均响应大小与状态码之间的联动；4）按主机维度识别高流量主机与其响应大小/状态分布；5）按请求路径类别（如图片、HTML、脚本/下载等）分析驱动响应大小变化的主要因素；6）识别可能的异常组合（例如高响应大小但错误状态、或某些主机对特定状态码贡献过高）。请最终给出一份可供复核的 analysis_summary.json，并附上可重复执行的核验问题答案。
```

### 1040. D8_g1087_zh (domain=D8, difficulty=7)

```
我需要你基于以下输入文件做一次知识库审计，包括识别过期内容、检查覆盖缺口、结合工单和现有缺口候选给出优先修补建议。输入文件：articles.csv、coverage_requirements.xlsx、ticket_topics.csv、tickets.xlsx、gaps.xlsx。输出三份报告：report_summary.md（一页审计结论和方向）、report_metrics.csv（聚合指标和排名，行数尽量少）、report_actions.json（建议动作，含归属团队和理由）。不要输出原始行级明细。
```

### 1041. D8_g1140_zh (domain=D8, difficulty=7)

```
我需要你基于以下文件做一次知識庫審計，找出過期、覆蓋缺口、關聯異常和高關注度的條目，並給出修復優先級建議：

- inputs/articles.csv
- inputs/reviews.xlsx
- inputs/tickets.xlsx
- inputs/escalations.csv
- inputs/access_log.csv

審計基準日設為2026-04-15，需要判斷stale文章、review過期、ticket和escalation中的異常引用，以及access_log中指定文章的片段統計。完成後輸出兩個文件：

1. findings.md – 中文分析簡報，內容要包含「發現概覽」「跨源一致性/衝突說明」「建議的修復優先級」
2. evidence_table.csv – 小型證據表（5–15行），記錄關鍵文章、異常和日誌命中點及其來源

請把工作拆成幾條可並行的分析線，最後整合成一份報告，不要只是各文件結論的堆砌。
```

### 1042. D8_g1260_en (domain=D8, difficulty=7)

```
Run a comprehensive audit of the knowledge base using the files in the inputs folder: articles.xlsx, product_versions.xlsx, topic_master.xlsx, article_conflicts.xlsx. I need a single ranked recommendation brief (recommendation_brief.md) that synthesizes your analyses on article staleness, coverage gaps, and conflicts into actionable steps. Keep it concise, about 2 pages.
```

### 1043. D8_g1428_zh (domain=D8, difficulty=7)

```
麻烦帮我把这批知识库审计材料过一遍，重点不是逐条抄表，而是做一份能直接给我和业务 owner 讨论的分析简报。请基于 inputs/kb_articles.csv、inputs/kb_snapshots.xlsx、inputs/incident_tickets.xlsx、inputs/coverage_map.xlsx 这四份材料，输出一份 findings.md，再附一个很小的证据表 evidence_table.csv。

我最关心的是这几件事：
- 先把知识库现状摸清：总量、已发布/草稿/弃用各有多少，哪些内容已经该复核但还没处理。
- 结合工单看风险：把“陈旧”定义为“status 属于 Published 或 Draft，且 next_review_date 早于 2025-04-20；或者 last_reviewed_at 距 updated_at 超过 120 天”。再找出其中有高优先级未结工单（severity >= 8）的文章，给我一个关键风险清单。
- 做跨源核对：对照两套快照，凡是 article_id 在 status、updated_at、last_reviewed_at、next_review_date 任一字段不一致，就算冲突；请把冲突数量和需要优先核对的前几个 ID 写出来。
- 看知识缺口：coverage_map 里只要 coverage_state 不是 Covered，或者 depth 不是 full，就算缺口；请按现状给出缺口总数，并顺手看一下缺口主要集中在哪类覆盖状态和深度。
- 顺便把未关闭工单按 issue_category 做个简单排行，另外告诉我“陈旧文章里工单最多的 owner_team 是谁”。

输出里请保留跨来源对账说明：如果某个来源和另一个来源口径不一致，要明确写出你最后采用的口径，以及为什么。证据表里只保留少量最关键的行，不要把整张表都贴进去。
```

### 1044. D8_g918_zh (domain=D8, difficulty=7)

```
对知识库审计数据做可汇报级梳理，识别过期内容、治理缺口，给出优先整改建议。使用 inputs/kb_articles.csv、kb_audit_issues.csv、kb_usage_daily.csv、kb_remediation_candidates.xlsx 和 kb_audit.sqlite（任选其一）。输出一份中文 Markdown 摘要报告和一份机器可读的 JSON 汇总文件（含标准统计结果），可选附一页表格补充说明。
```

### 1045. D8_g936_zh (domain=D8, difficulty=7)

```
用 inputs/kb_articles.csv、inputs/kb_events.xlsx、inputs/kb_owners.xlsx 和 inputs/kb_taxonomy.xlsx 完成知识库审计、过期识别和主题缺口补全，出一份给管理层和内容 Owner 的简报。最终交付三份文件：一份带所有关键指标和异常摘要的 JSON 汇总，一份按 traffic_score 降序列出前 20 篇需重审文章的 CSV，以及一份报告。
```

### 1046. D8_g980603_zh (domain=D8, difficulty=7)

```
我需要你基于这三份输入文件做一次知识库盘点和补洞分析：kb_audit_pack.xlsx、kb_feedback_rollup.csv、kb_audit_meta.json。请把结果整理成一份单一的中文汇总报告，直接给我可交付版本，不要拆成多个文件。重点要覆盖四块：一是知识库条目的新鲜度和缺口，二是反馈日志里的异常和重复情况，三是哪些主题最值得优先补充或改写，四是给出一份可执行的整改优先级建议。我希望你把口径统一好：过期是按 last_reviewed 加 review_cycle_days 之后仍早于报告日；日志去重只按完全相同的记录去重；带有 Helpful 和 Unhelpful 两类反馈的文章要单独识别；同时要把缺少 owner 的条目、指向不存在 article_id 的日志、以及 remediation 里高优先级高影响项都明确列出来。报告里最好有一个总览页，再加一页明细或一个简洁的汇总表就够了，重点是把结论讲清楚。如果你发现数据里有重复、孤立引用或者字段缺失，请按上面的口径处理，并在报告中说明对结论的影响。
```

### 1047. D8_g980687_en (domain=D8, difficulty=7)

```
I need a decision brief on the KB audit using kb_audit_pack.xlsx, kb_review_log.jsonl, and remediation_scorecard.xlsx.
Please turn this into a ranked recommendation for what we should remediate first.
- Call out the biggest staleness and duplication problems.
- Identify where the open gap backlog is weakest on ownership or due dates.
- Use the remediation scorecard to estimate the highest-priority work and summarize the workload.
- Tie the log file back to the audit with any meaningful blocking or repeated review patterns.
- Finish with a concise recommendation table and a clear first/second/third priority order.
```

### 1048. D8_g980768_zh (domain=D8, difficulty=7)

```
知识库最近被抱怨过期内容多、重复记录也开始影响检索结果，我需要一次完整的审计和修复优先级判断。请基于 inputs/kb_articles_audit.xlsx、inputs/kb_usage_feedback.xlsx、inputs/kb_gap_register.xlsx，输出一份精简的综合报告，说明当前知识库的健康状况、主要失效点、需要优先处理的内容，以及哪些条目最适合先做修订或下线。报告里请同时把数据异常、重复记录和内容陈旧问题说清楚，方便我直接分发给相关负责人。
```

### 1049. D8_g980962_zh (domain=D8, difficulty=7)

```
请基于 kb_change_log.xlsx、kb_articles.xlsx 和 kb_feedback.xlsx 做一版知识库审计与缺口修复汇总，重点看重复变更、删除事件、文章时效性、反馈缺口和责任人分布。我只需要一份整合后的简报文件，把异常、优先级和建议动作都写清楚；PDF 里的说明也一起参考。
```

### 1050. D8_g981133_zh (domain=D8, difficulty=7)

```
请根据 inputs/kb_inventory.xlsx、inputs/remediation_tickets.xlsx、inputs/usage_log.xlsx 和 inputs/knowledge_audit_brief.pdf 做一份知识库审计汇总，重点看陈旧内容、缺失责任人、重复标题、工单积压和高流量低满意条目。我只要一份合并后的中文报告文件，里面放关键汇总、异常清单和可执行的补齐建议。
```

### 1051. D8_g981175_en (domain=D8, difficulty=7)

```
Please audit the knowledge base bundle in kb_audit_bundle.xlsx and use the glossary/scope files alongside it.
- Summarize staleness, coverage gaps, duplicate clusters, and any status mix issues.
- Call out the real seed records that appear in the workbook and include their exact titles/questions where relevant.
- I need one compact report file with the key findings, counts, and recommended remediation priorities.
- Make sure the report is easy to review by leadership and can support follow-up cleanup work.
```

### 1052. D8_g981192_zh (domain=D8, difficulty=7)

```
请基于 inputs/knowledge_base_inventory.xlsx、inputs/support_ticket_feedback.xlsx 和 inputs/remediation_actions.pdf，给我一份单文件汇总，说明这批知识库的审计结果、主要缺口、优先修复项和反馈效果。重点把重复、缺失负责人、陈旧内容、未映射引用和高频问题都汇总清楚，输出成一份可直接转给管理层的报告。
```

### 1053. D8_g981304_zh (domain=D8, difficulty=7)

```
我需要你结合 inputs 里的 kb_articles.xlsx、kb_usage_logs.xlsx、kb_audit_tracker.xlsx 和 kb_governance_memo.pdf，做一份简短的决策简报，帮我判断 KB 治理这轮该先处理哪些条目、先补什么缺口，以及为什么。重点把过期但还被频繁访问、访问异常、审计逾期和未发布内容访问这些情况合在一起看，最后给我一份可直接发给负责人看的结论。
```

### 1054. D8_g981324_zh (domain=D8, difficulty=7)

```
我需要一份知识库审计报告，使用提供的三个文件：kb_articles.xlsx（文章库）、qa_pairs.xlsx（问答对）、reference_ontology.pdf（参考标准）。请进行过时性、质量、差距和重复分析，并输出一份决策简报，按照优先级给出改进建议。只需一份汇总文件。
```

### 1055. D8_g981329_en (domain=D8, difficulty=7)

```
We need a clear decision on how to fix our knowledge base issues before the next leadership review. Please review inputs/kb_audit_inventory.xlsx, inputs/support_tickets.xlsx, and inputs/audit_event_log.xlsx. I need a concise recommendation that ranks the best remediation path and explains the numbers behind it, including which content is stale or drifting, what the incident and ticket data show, which vendor option is the strongest backup, and whether the compliance timing gives us any urgency. Please put the result in one brief file.
```

### 1056. D8_g981416_en (domain=D8, difficulty=7)

```
I need a compact knowledge-base audit pack based on kb_audit_pack.xlsx. Please review the workbook and produce one consolidated report for me.
- Identify stale or outdated articles and show the highest-risk items first.
- Call out coverage gaps where important topics have no usable article or where article freshness is missing.
- Check the embedded issue records for patterns that explain the staleness or missing coverage.
- Summarize the business impact using the article metadata, issue queue, and review feedback.
- Include a short remediation plan with the biggest fixes to tackle first.
```

### 1057. D8_g981453_zh (domain=D8, difficulty=7)

```
我需要你帮我做一次知识库盘点和修复方案汇总，输入是 4 个文件：kb_articles.xlsx、kb_feedback_log.csv、kb_qa_cases.xlsx、kb_governance_memo.pdf。请把这次审计做成一个单一的汇总交付件，重点看三件事：哪些文章明显过期、哪些条目存在版本或来源冲突、以及哪些高频问题在现有知识库里没有被覆盖或覆盖不充分。我希望最后只产出一个紧凑的报告文件，内容里同时包含审计结论、优先修复清单、以及建议的后续动作。
```

### 1058. D8_g981584_zh (domain=D8, difficulty=7)

```
请基于 kb_audit_data.xlsx、kb_gap_glossary.xlsx、kb_remediation_tickets.xlsx 和 kb_audit_memo.pdf，给我一份知识库审计与补缺决策简报。
我想快速看懂现在该先修什么、为什么、以及建议的优先级排序。
- 先把内容陈旧、术语缺口、重复项、负责人异常和工单异常梳理清楚
- 再按影响和紧急度给出一个明确的优先级排序
- 简报里要带上关键数字、风险判断和建议动作
- 最后给出一个可以直接发给管理层的短版结论
```

### 1059. D8_g981614_zh (domain=D8, difficulty=7)

```
我需要你把这四个文件一起看一下：kb_articles.xlsx、gap_register.xlsx、usage_logs.xlsx、feedback_samples.xlsx，再结合 kb_audit_memo.pdf，帮我做一份知识库审计决策简报。重点是找出应该优先修复、重写或下线的内容，最后给我一个有排序的建议结论，写成 decision_brief.md，里面要带上支撑这个判断的关键数字。
```

### 1060. D8_g981883_en (domain=D8, difficulty=7)

```
You are responsible for auditing the company's knowledge base. The data is provided in inputs/kb_articles.csv and inputs/audit_summary.pdf. Analyze the articles and identify any anomalies, inconsistencies, or compliance gaps. Deliverables: (1) a detailed audit report in PDF, (2) a spreadsheet of all issues found, (3) a summary of compliance recommendations. Use any tools you need; your final answer should include the three deliverables.
```

### 1061. D8_g982056_zh (domain=D8, difficulty=7)

```
请基于 inputs/knowledge_issues.xlsx、inputs/kb_articles.xlsx 和 inputs/kb_activity_log.txt，做一次知识库审计并输出一个汇总报告文件 knowledge_audit_report.xlsx。我要看到过期内容、覆盖缺口、需要更新的条目，以及高风险工单/搜索行为的归因结论。
```

### 1062. D8_g982193_en (domain=D8, difficulty=7)

```
I need a KB audit and remediation decision brief for the April 8 NexCloud incident. Please review kb_articles.xlsx, kb_topic_demand.xlsx, and incident_and_compliance.pdf, then give me a ranked recommendation on what to fix first.

- Identify the most urgent staleness and gap issues in the knowledge base
- Call out any data quality problems in the inventory that affect the audit
- Use the incident evidence and compliance note to explain what should be prioritized for remediation
- Estimate the business impact using the ticket and views data
- Return one concise decision brief with the ranked actions and the supporting numbers
```

### 1063. D8_k982095_zh (domain=D8, difficulty=7)

```
请基于文件 suraj520__customer-support-ticket-dataset__customer_support_tickets.csv 做一次面向知识/客服工单的异常与离群分析，重点围绕显式数值规则来找出“异常工单”和“异常客户/产品模式”。请你直接用数据里的真实字段分析，不要编造值。重点看这些列：Ticket ID、Customer Age、Product Purchased、Date of Purchase、Ticket Type、Ticket Subject、Ticket Status、Resolution、Ticket Priority、Ticket Channel、First Response Time、Time to Resolution、Customer Satisfaction Rating。我要的是一份可交付给业务团队的分析摘要：先定义清晰的异常规则（例如年龄极端值、满意度极低、响应/解决时长极端值、稀有类别、组合异常等），再按这些规则拆成几个独立分析轨道，最后汇总出最值得人工复核的工单特征、涉及的渠道/优先级/产品，以及异常是否集中在某些类别上。请特别注意：要把阈值写清楚，并用可复现的方式计算；如果某些字段缺失，也要把缺失本身当作一种异常信号一起看。最终输出适合业务沟通的结论和可执行排查建议。
```

### 1064. D8_k982100_en (domain=D8, difficulty=7)

```
Using the file tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv, analyze the support-ticket dataset with a strong focus on temporal/sequence behavior in the tickets. I need a compact but rigorous readout of how ticket volume and composition change over the sequence of records, including period-over-period shifts in the main labels (type, queue, priority, language) and any notable changes in text/tag structure that might explain the trend. Please break the work into independent tracks so different analysts can work in parallel, and ground everything in the actual columns in the file: subject, body, answer, type, queue, priority, language, tag_1 through tag_8. I’m especially interested in whether the early, middle, and late parts of the dataset look different, whether the mix of ticket categories drifts over time, and whether missing tags or specific tags become more common in later records.
```

### 1065. D8_k982262_zh (domain=D8, difficulty=7)

```
请基于文件 tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv 做一份面向知识库/客服支持的复杂分群分析报告，重点比较不同分类群体之间的差异，尤其是各组的占比、均值和最大的差距。请围绕 columns（subject、body、answer、type、queue、priority、language、tag_1 到 tag_8）做分析，不要只看总体，要找出不同 type、queue、priority、language 之间在票量、响应长度、标签分布和缺失情况上的显著分段差异，并解释哪些组合最值得优先关注。请把结论整理成 analysis_summary.json，要求可直接给管理层阅读，突出“哪个细分群体更高频、哪几个群体最异常、哪些字段缺失最影响分群判断”。
```

### 1066. D8_k982550_zh (domain=D8, difficulty=7)

```
请基于文件 tobaisbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv 做一版支持工单异常/离群分析，重点放在“显式数值规则”上：比如用 IQR、极端频率、稀有类别、缺失模式、以及跨字段组合规则去找异常工单。我需要你先从数据质量和业务风险两条线一起看，尽量找出那些明显不正常、非常少见、或者在某些字段组合下极不协调的记录。请结合这些字段：subject、body、answer、type、queue、priority、language、tag_1 到 tag_8。希望输出能直接用于我向团队汇报，因此请把分析拆成 4-6 个彼此独立的子任务，分别覆盖：1）数值/规则型异常定义与总体异常率；2）语言、队列、优先级的稀有类别与极端分布；3）标签字段的缺失、重复、长尾与离群标签组合；4）按工单长度（subject/body/answer 字符数）做 IQR 异常检测；5）按类型/队列/语言交叉后的极小组与异常集中；6）把最值得人工复核的异常样本按规则列出来。请最后给我一个可直接落地的 analysis_summary.json 结论草案，并确保所有判断都基于明确阈值、计数或频次规则，而不是主观描述。
```

### 1067. D8_k982717_en (domain=D8, difficulty=7)

```
Using the file tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv and the columns subject, body, answer, type, queue, priority, language, version, tag_1 through tag_8, build a support-ticket analytics summary focused mainly on segment comparison across categorical groups. I need a realistic breakdown of which ticket segments differ most in volume and response characteristics, especially by queue, type, priority, language, and version. Please also flag any notable missing-tag patterns and whether the biggest gaps are consistent across languages or concentrated in specific ticket classes. I want this organized as a compact analysis package I can share internally.
```

### 1068. D8_k982993_zh (domain=D8, difficulty=7)

```
请基于文件 tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv 做一份面向知识库/支持工单运营的深度分析，重点围绕“相关性与驱动因素”展开：看哪些数值字段会一起变化、哪些业务标签/队列/语言更容易和高优先级或特定版本关联、以及这些关系是否在不同类型工单中稳定。请直接使用现有列 subject、body、answer、type、queue、priority、language、version 以及 tag_1 到 tag_8，不要假设任何额外字段。我要一个可执行的分析方案，最好能拆成几个彼此独立的子任务，分别输出：1）整体数值字段相关性矩阵与最强正/负相关对；2）version 与工单特征的单调/线性关联；3）priority/queue/type 对版本、语言分布和标签稀疏度的驱动差异；4）关键标签与高优先级/高版本的联合关联；5）缺失模式是否与队列、语言或优先级相关。最后请给我一个简洁的可汇总结果，便于我直接转成一页分析摘要。
```

### 1069. D8_k983336_zh (domain=D8, difficulty=7)

```
请基于文件 tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv 做一份面向知识库/客服工单分析的复杂诊断报告，重点围绕“相关性与驱动因素分析”展开：先检查数据质量与字段可用性，再围绕 language、type、queue、priority、tag_1 到 tag_8 之间的关联关系做分析，找出哪些类别最常一起出现、哪些队列/优先级与某些语言或工单类型明显绑定，以及各字段的缺失模式是否会影响结论。请把结果拆成几个彼此独立的分析轨道，便于并行处理；每个轨道都要给出可复核的定量结论，并尽量使用 rounded correlations、top associations、交叉表占比和缺失统计来说明驱动关系。最后请输出一份可直接给业务方看的简短摘要，说明最值得关注的 3-5 个相关性/关联模式，以及这些模式可能意味着什么。请特别基于真实列名：subject, body, answer, type, queue, priority, language, tag_1 到 tag_8。
```

### 1070. D8_k983407_zh (domain=D8, difficulty=7)

```
请基于文件 tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv 做一份支持工单的多维分析，但重点要放在“排名与集中度”上：先找出哪些 type、queue、priority、language、version 和高频 tag 最集中，看看头部组别是否占了大部分工单量（例如 Top-N 占比、累计占比、Pareto 现象），再结合 subject/body 的文本特征判断这些高频工单是否有明显共性。请把结果拆成 4-6 个彼此独立的分析轨道，方便我让不同子任务并行跑；每条轨道都要输出可直接用于管理汇报的结论，尤其要说明头部类别、集中度、以及可能的资源配置含义。请同时注意这是多语言工单数据，language 和 version 也要纳入排名分析。最终请输出一份结构化 summary。
```

### 1071. D8_k983434_zh (domain=D8, difficulty=7)

```
请基于文件 tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv 做一版面向知识库/支持工单分析的深度诊断，重点围绕“相关性与驱动因素分析”：请先检查数值字段 version 是否与工单主题、队列、优先级、语言以及标签分布存在可解释的联动，再找出最强的成对关联和最值得关注的组合。我要的是能直接支持运营决策的结论，不要泛泛而谈。请把分析拆成几条互不依赖的线并行推进：一条做 version 与 type/queue/priority/language 的整体相关与分组对比，一条做 tag_1 到 tag_8 的共现与高关联标签对，一条做按语言/队列/优先级的交叉驱动分析，一条做缺失值与标签空白模式是否影响结果的检查。最后给我一个简洁的 summary，列出最强的关联、最异常的组合、以及你认为最可能驱动工单版本变化的因素。请尽量使用可复现的统计汇总，相关系数请四舍五入到 2 位小数。
```

### 1072. D8_k983465_zh (domain=D8, difficulty=7)

```
请直接基于文件 tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv 做一轮支持工单分析，重点看时间序列/趋势变化：先确认如果把记录顺序当作一个自然时间序列，不同维度（type、queue、priority、language、tag）在前后段是否有明显结构变化，再比较各类别在不同阶段的占比、增长/下降、以及与文本字段是否存在稳定关联。我要你把结果拆成几个互不依赖的分析轨道并行做，最后汇总成一个可交付的分析摘要，尽量回答：哪些类型/队列/优先级/语言在样本前后阶段变化最大，哪些标签在前后段最稳定或最波动，是否存在某些类别组合在后半段显著增多。列出你发现的关键趋势、变化幅度、以及最值得继续深挖的异常点。请明确引用数据里的 real columns：subject、body、answer、type、queue、priority、language、tag_1 到 tag_8。
```

### 1073. D8_k983500_zh (domain=D8, difficulty=7)

```
请基于文件 tobiasbueck__multilingual-customer-support-tickets__aa_dataset-tickets-multi-lang-5-2-50-version.csv 做一份面向知识/支持工单分析的综合报告，重点围绕 version 这个序列字段做时间/趋势分析：先看不同 version 下工单量、类型、队列、优先级、语言和标签的变化率与环比/阶段性波动，再结合 subject、body、answer 的文本特征做辅助解释。请把分析拆成几个相互独立的方向，方便分配给不同子任务：1) 全局趋势：按 version 看总工单量、Incident/Change/其他类型占比、high/medium/low 优先级占比变化；2) 队列趋势：按 version 看各 queue 的工单量和增长/下滑最快的队列；3) 语言趋势：按 version 看各 language 的占比和变化；4) 标签趋势：按 version 看 tag_1 到 tag_8 的高频标签及其随版本的变化；5) 响应内容趋势：按 version 看 answer 长度或缺失情况的变化，并检查是否与 priority 或 type 有关联；6) 异常点识别：找出某些 version 上明显偏离整体趋势的工单高峰或结构突变。请输出可执行的分析结论框架，并给出适合进一步深挖的指标清单。数据字段请显式使用 subject、body、answer、type、queue、priority、language、version、tag_1 到 tag_8。
```

### 1074. D8_k983504_zh (domain=D8, difficulty=7)

```
请基于文件 tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv（列包括 subject、body、answer、type、queue、priority、language、tag_1 到 tag_8）做一份面向知识/支持工单运营的多部分分析，重点围绕“相关性与驱动因素分析”：哪些类别变量与工单类型、队列、优先级最相关，哪些标签经常一起出现，哪些字段组合会推动高优先级、Incident 或某些队列的出现。请把分析拆成 4-6 个彼此独立的轨道，适合并行给不同子代理处理，并最终汇总成一份可交付的 analysis_summary.json。请特别关注：1) type/queue/priority/language 的分布与交叉关系；2) tag_1 到 tag_8 的共现与高频组合；3) 高优先级工单的驱动特征；4) 不同 queue 的显著差异；5) 语言与类型/优先级的关联；6) 任何可以用“rounded correlations / top associations”表达的稳定模式。
```

### 1075. D8_k983589_zh (domain=D8, difficulty=7)

```
请基于文件 `tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv` 做一份面向支持/知识库运营的多部分分析，重点围绕“排名与集中度”来展开：先找出哪些 `queue`、`type`、`priority`、`language`、以及高频 `tag_1` 到 `tag_8` 在工单中最集中，计算 Top-N 占比、头部集中度、以及是否存在明显的 Pareto 结构；同时结合 `subject`、`body`、`answer` 的文本和这些分类字段，分析头部类别在不同维度上的分布是否失衡、是否有某些组合（例如某些 queue+priority、language+queue）异常集中。请把结果拆成 4-6 个相互独立的分析轨道，适合并行给多个子分析代理去跑。最终只需要输出一份适合内部汇报的分析摘要（文件名 `analysis_summary.json`），并确保所有结论都严格基于数据本身。请尽量用清晰的排名、占比、累计占比、Top-N/Top-3/Top-5 这类指标来组织结论。
```

### 1076. D8_k983693_zh (domain=D8, difficulty=7)

```
请基于数据文件 tobiasbueck__helpdesk-github-tickets__github_issues_tickets.csv 做一版面向知识库/支持工单管理的深度分析，重点放在“相关性与驱动因素分析”：哪些数值字段会一起变化、哪些字段之间关联最强、哪些标签/状态/时间特征可能驱动工单热度与回复活跃度。请先给我一份可直接汇报的结论摘要，并把分析拆成 4-6 个彼此独立的部分，方便不同人并行推进。务必结合真实列名，比如 comments、reactions_total_count、reactions_plus_1、reactions_heart、reactions_hooray、reactions_rocket、reactions_minus_1、reactions_confused、reactions_eyes、created_at、closed_at、state、comments、labels_*、assignee_*、user_*、answers_* 等字段，做相关系数、Top 关联、分组对比和异常点检查。最终希望能回答：哪些工单特征最能解释互动量高低、哪些标签更容易产生高反应/高评论、关闭状态是否与互动强度相关、以及是否存在明显的“少数高热度工单”现象。
```

### 1077. D8_k983696_en (domain=D8, difficulty=7)

```
Using the file noopurbhatt__retail-ai-intelligence-knowledge-base__retail_ai_knowledge_base_100k.csv, run a knowledge/support-ticket style analysis of how the content changes over the sequence implied by knowledge_id and whether the mix of topics, categories, regions, and AI use cases shifts over time. I need a business-ready readout that focuses mainly on temporal trend analysis and period-over-period change: identify which segments are gaining or losing share in the later portion of the dataset, how the most common topics and use cases evolve from earlier to later records, and whether the associated retail problems, customer segments, and regions show meaningful drift. Please break it into independent workstreams so different analysts can work in parallel, and give me concise outputs suitable for an executive summary.
```

### 1078. D8_k983723_zh (domain=D8, difficulty=7)

```
请基于文件 samanemami__yeastcsv__yeast.csv 做一版面向知识/支持工单运营的分析，重点围绕“分布与阈值分层”：把 mcg、gvh、alm、mit、erl、pox、vac、nuc 这些数值字段当作工单特征指标，结合 name 作为结果标签，分析不同阈值/分位数下的样本规模、占比和标签结构。我要你输出一份可直接给业务看的 analysis_summary.json，核心要回答：1）每个字段在业务阈值下的高/低值样本有多少；2）按分位数分桶后，各桶的样本量与 name 构成如何；3）不同字段组合形成的高风险/低风险 cohorts 占比多大；4）name 在整体和各 cohorts 中的 mix share 是否明显偏移；5）找出最值得关注的阈值分层信号，并给出能落地的运营解释。请按字段真实数据分析，不要假设、不要编造。
```

### 1079. D8_k983728_zh (domain=D8, difficulty=7)

```
请基于文件 parthpatil256__it-support-ticket-data__IT Support Ticket Data.csv 做一份面向知识库/支持工单分析的深度诊断，重点围绕“相关性与驱动因素分析”展开：请先确认数据规模、字段分布与缺失情况，然后分析 Department、Priority、Body、Tags 之间哪些因素会一起变化、哪些标签/部门/优先级最容易共同出现、以及高优先级工单与特定主题标签之间的关联强弱。请把分析拆成几个可并行的部分，最后输出一份适合忙碌管理者快速阅读的结论摘要，说明哪些部门/标签组合最值得优先优化知识库、哪些工单特征最可能驱动更高优先级。请严格基于原始数据，不要臆造任何字段。
```

### 1080. D8_k983847_zh (domain=D8, difficulty=7)

```
请基于文件 tobiasbueck__helpdesk-github-tickets__github_issues_tickets.csv 做一份面向知识库/支持工单分析的深度诊断，重点放在“数值字段之间的相关性与驱动因素”上：帮我找出哪些 numeric 指标彼此一起变化、哪些字段对互动强度/生命周期最有解释力，并把相关系数做四舍五入后给出可读结论。请围绕真实工单字段（例如 comments、reactions_total_count、reactions_plus_1、reactions_heart、reactions_eyes、reactions_laugh、reactions_confused、created_at、closed_at、state、assignee、labels、repo_name、user_login、answers_* 等）展开，不要只做描述统计；我需要你把分析拆成几个彼此独立的工作流，便于并行推进：一条线做核心数值相关矩阵和 top associations，一条线做不同交互信号的驱动比较，一条线做工单生命周期与反应/评论的关系，一条线做按仓库/标签/状态的分层差异，必要时再补一条线检查缺失与数据质量是否会干扰相关性结论。最后输出可直接给团队看的结构化摘要，突出最强的正/负相关、可能的业务解释，以及需要注意的局限。
```

### 1081. D8_k983948_en (domain=D8, difficulty=7)

```
Using the file mirzayasirabdullah07__customer-support-tickets-dataset-200k-records__customer_support_tickets_200k.csv, do a support-ticket analytics deep dive focused mainly on temporal trend analysis. I need a concise but decision-ready readout on how ticket volume, SLA breaches, escalation, response speed, and resolution time changed over time, and how those trends differ by priority, channel, and region. Please use the date fields ticket_created_date and ticket_resolved_date, and also reference first_response_time_hours, resolution_time_hours, sla_breached, escalated, priority, channel, region, category, subscription_type, and customer_segment. Break the work into separate tracks so different people can handle them independently, and make sure the final output is a compact analysis_summary.json with practical findings, period-over-period changes, and any notable outlier periods.
```

### 1082. D8_k983956_zh (domain=D8, difficulty=7)

```
请基于文件 noopurbhatt__retail-ai-intelligence-knowledge-base__retail_ai_knowledge_base_100k.csv 做一份面向知识库/支持工单分析的分段对比报告，重点看不同分类群体之间的差异（按类别、地区、客户细分、AI 用例、源类型等分组后比较占比、均值和最大差距）。我最关心的是：哪些群体在 retail_problem / retail_insight / merchandising_strategy / tags 上呈现出明显不同的模式，哪些组合最容易出现某类问题，哪些段之间的差距最大，以及这些差异是否在不同 region 或 source_type 中仍然成立。请你把结果整理成可直接汇总给业务团队的结构化结论，包含：1）各主分类的样本量与占比；2）不同 customer_segment 的问题主题与 AI 用例分布对比；3）不同 region 的关键问题/策略差异；4）source_type 与 category 的交叉差异；5）找出最大的分段差距（例如某类在某组显著高于另一组）；6）输出一个可用于后续工单/知识运营行动的优先级建议。请严格使用表中的真实列：knowledge_id, category, topic, retail_problem, retail_insight, ai_use_case, customer_segment, merchandising_strategy, source_type, region, tags。
```

### 1083. D8_k984078_zh (domain=D8, difficulty=7)

```
请基于文件 mirzayasirabdullah07__customer-support-tickets-dataset-200k-records__customer_support_tickets_200k.csv 做一份以“相关性与驱动因素分析”为主的客户支持工单分析。重点帮我找出哪些数值字段彼此一起变化、哪些指标最能解释满意度、响应时长、解决时长和 SLA 是否违约。请尽量围绕现有字段做细分：比如 customer_satisfaction_score、first_response_time_hours、resolution_time_hours、customer_age、customer_tenure_months、previous_tickets、issue_complexity_score 之间的相关关系；再结合 priority、escalated、sla_breached、status、channel、region、subscription_type、customer_segment 等分类字段，看看不同人群/工单类型下这些数值指标的驱动差异。输出时请给我一个可直接交付的分析摘要（analysis_summary.json），并且把关键结论按独立分析轨道拆开，便于我分派给不同子任务并行验证。
```

### 1084. D8_k984164_zh (domain=D8, difficulty=7)

```
请基于文件 noopurbhatt__retail-ai-intelligence-knowledge-base__retail_ai_knowledge_base_100k.csv 做一份面向知识库/支持工单分析的业务诊断，重点围绕“分布与阈值分层”来展开：先看 category、topic、region、source_type、customer_segment、ai_use_case 这些字段的整体分布，再按业务阈值做 cohort 切分（例如每个 category/topic 的样本量是否高于整体中位数、是否落在四分位数分桶、头部/长尾占比、以及不同 region/segment 下的 mix share）。我需要你把结果拆成几条彼此独立的分析线并分别产出结论：1）知识条目在 category/topic 上的头部与长尾结构；2）按 region 与 customer_segment 的阈值分层差异；3）source_type 与 merchandising_strategy 的组合分布及其高低频 cohort；4）ai_use_case 的集中度、top 占比和低频项占比；5）tags 的复合标签模式是否存在明显的高频阈值簇；6）如果有必要，补充一个整体分布的异常点或不平衡提示。请直接给出适合管理层阅读的中文摘要，强调哪些维度明显超出/低于阈值、哪些 cohort 值得优先关注，以及各分层的 mix share 差异。
```

### 1085. D8_k984216_zh (domain=D8, difficulty=7)

```
请基于文件 noopurbhatt__retail-ai-intelligence-knowledge-base__retail_ai_knowledge_base_100k.csv 做一版面向“知识库 / 支持工单分析”的异常排查报告，重点围绕明确数值规则识别异常与离群点：比如极少见类别、IQR 口径下的长尾分布、明显低频的 region / source_type / customer_segment / topic 组合，以及 tags 的稀有模式。请先确认数据规模和缺失概况，然后按以下方向拆成多条独立分析线并输出可执行结论：1）用明确阈值找出超低频 category、topic、region、source_type、customer_segment；2）用 IQR 或其他分位数规则找出在各类目内异常偏高/偏低的知识条目出现集中度；3）识别最稀有的 tags 组合及其对应的业务主题；4）检查可能的异常关联组合（例如某些 region + source_type + ai_use_case 的超低频交叉项）；5）总结这些异常点对知识运营、支持工单分流和检索覆盖可能带来的风险，并给出优先级建议。请直接产出适合交付给业务方的结论框架，不要只做描述性统计。字段包括 knowledge_id、category、topic、retail_problem、retail_insight、ai_use_case、customer_segment、merchandising_strategy、source_type、region、tags。
```

### 1086. D8_k984229_zh (domain=D8, difficulty=7)

```
请基于文件 sevgisarac__temperature-change__FAOSTAT_data_en_11-1-2024.csv 做一份面向知识库/支持工单分析的深入诊断：我想把它当作“不同地区在不同月份的温度变化异常是否显著不同”的业务代理指标来分析，重点看各个分类组之间的均值/占比差异，以及最大差距出现在哪些分组。请结合真实列名（Domain Code、Domain、Area Code (M49)、Area、Element Code、Element、Months Code、Months、Year Code、Year、Unit、Value、Flag、Flag Description）输出可直接给管理层看的结论。请至少拆成 4-6 个彼此独立、可并行的分析轨道：1）按 Months / Months Code 比较不同月份的 Value 分布与均值差异；2）按 Area 比较国家/地区的平均温度变化并找出极端高低组；3）按 Flag / Flag Description 比较“Estimated value”等标记与非标记记录的 Value 差异和占比；4）按 Year 分析不同年份的整体趋势与峰值/低谷；5）按地区分组（例如按 Area 名称中的显著区域特征或直接按前 N 个高均值地区）找出最大分段差距；6）检查是否存在缺失值、重复组合或异常月份编码。请最终给我一个可汇总的 analysis_summary.json，并明确列出每个轨道的结论、最大 gap、以及可行动建议。所有结论必须严格基于数据，不要臆测。
```

### 1087. D8_k984382_zh (domain=D8, difficulty=7)

```
请基于文件 harshitstark__healthcare-documentation-database__Healthcare Documentation Database.csv 做一份面向知识/支持工单分析的多维诊断。这个数据里没有真实日期字段，所以请把 Serial No 当作记录进入顺序，重点做“按序列推进”的趋势分析：先看整体记录量在连续序号上的变化，再看不同 medical_specialty 的占比和增速变化，接着识别哪些 sample_name / description 主题在前后段出现频率变化最明显，并评估 cleaned_transcription 的文本长度是否随序号阶段发生系统性变化。最后给我一份可直接用于汇报的结论，突出异常波动、稳定增长/下降的主题，以及可能需要优先处理的专科和问题类型。请把结果整理成 analysis_summary.json，要求结论能分别对应到不同分析轨道，便于我分给不同分析师并行复核。
```

### 1088. D8_k984467_zh (domain=D8, difficulty=7)

```
请基于文件 aniketg11__supportticketsclassification__all_tickets.csv 做一份面向知识/支持工单的细分分析，重点看不同分类分组之间的差异（rates/means per group、最大差距、哪些组更“重”）。我希望你直接围绕现有列 title、body、ticket_type、category、sub_category1、sub_category2、business_service、urgency、impact 来分析，不要假设别的字段。请把结果整理成一份适合汇报给支持运营负责人的分析，重点回答：1）不同 category / business_service / urgency / impact 组合下的工单量和平均影响/紧急程度差异；2）哪些 sub_category1 或 sub_category2 在某些 category 中明显更集中；3）ticket_type 在不同分类中的结构差异；4）找出最大的不均衡或最异常的分组；5）如果要优先优化支持流程，应该先看哪些组。请把分析拆成多个彼此独立的小任务，便于分工并行处理。
```

### 1089. D8_k984496_zh (domain=D8, difficulty=7)

```
请基于文件 sudhanshu746__analyze-helpdesk-tickets__WA_Fn-UseC_-IT-Help-Desk.csv 做一份面向知识/支持工单管理的异常与离群点分析，重点围绕“显式数值规则”识别异常工单：例如用 daysOpen 的绝对阈值、IQR、极端分位数、以及 RequestorSeniority / FiledAgainst / TicketType / Severity / Priority / Satisfaction 中的稀有类别来发现值得关注的工单。请把分析拆成 4-6 个彼此独立的轨道，方便不同子任务并行推进，并最终输出一份能直接给支持运营团队看的总结。请同时关注 ticket、requestor、ITOwner、FiledAgainst、TicketType、Severity、Priority、daysOpen、Satisfaction 这些字段之间的异常组合：比如超长未结单、严重级别与低优先级不一致、满意度异常、以及少见类别集中出现的情况。希望你先识别异常定义，再量化异常工单规模、主要来源、责任人分布和最可疑的交叉组合。请用中文回答，内容要贴近真实业务场景。
```

### 1090. D8_k984536_en (domain=D8, difficulty=7)

```
Analyze the file theaimindset__customer-behavior-and-churn-simulation-dataset__synthetic_customer_behavior_and_churn.csv using the real columns in it, and focus the work on temporal / trend analysis over date or sequence fields, especially period-over-period changes. I need a customer behavior and support-ticket analytics readout that explains how churn risk evolves over tenure and recency, how support tickets and satisfaction move over time, and where the biggest shifts are across customer segments. Please split the work into independent tracks so different analysts can work in parallel: one track on churn and tenure trends, one on support-ticket and satisfaction trends, one on signup cohort / recency behavior, one on subscription and contract trend shifts, and one on regional or demographic trend differences. Please keep the findings grounded in the actual data and produce a concise analysis summary JSON.
```

### 1091. D8_k984552_zh (domain=D8, difficulty=7)

```
请基于文件 samyakrajbayar__python-questions-faq-dataset__python_faq_dataset.csv（字段包括 question、answer、source、score、tags、topic、q_length、a_length、quality_score、difficulty），帮我做一份面向知识库/支持工单分析的异常与离群点排查报告。重点围绕显式数值规则来找异常：例如 q_length、a_length、quality_score、score 的极端值，长度比失衡，低分高质或高分低质的反常样本，稀有 difficulty/topic/tags 组合，以及 source 或 topic 中的稀有类别。请把分析拆成可并行的几个部分，并最终输出一份适合汇总成 analysis_summary.json 的结论。我要的是能直接指导后续清洗、标注和路由策略的结果，不要泛泛而谈。
```

### 1092. D8_k984558_zh (domain=D8, difficulty=7)

```
请基于文件 deepakdeepu8978__drug-indications-drug-engineering-with-ai__drug_indications_database.csv 做一份面向知识/支持工单分析的分群对比分析，重点围绕不同类别之间的指标差异（rates/means per group、最大差距、异常分布）。我希望你先按可解释的分类维度梳理数据，再找出最值得关注的分段差异，并把结果整理成一个 analysis_summary.json。请至少覆盖这些字段：src_nm、drug_raw_name、cas_match、chebi_match、chemid_match、ctd_match、ind_raw、ind_agg、ind_raw_match、ind_umls_entry_term_match、ind_umls_in_term_match、ind_umls_pheno_flg、umls_sem_typ1。具体分析时请分成 4-6 条彼此独立的分析线：1）不同来源 src_nm 的匹配率与缺失率对比；2）不同指示词/用途大类 ind_agg 的匹配与语义类型分布；3）按 cas_match / chebi_match / chemid_match / ctd_match 的命中情况比较各分组差异；4）按 ind_umls_pheno_flg 和 ind_raw_match 看“症状/疾病”类工单与其他类工单的表现差异；5）找出匹配率最低和最高的前几个人工可解释分组；6）检查原始药名 drug_raw_name 中重复或高频名称是否集中在某些来源或指示类别。请用定量结果优先，最后给出一版适合交付给业务方的简洁结论，指出最大 gap 在哪里、可能对应什么数据质量问题，以及应该优先处理哪些来源或分组。
```

### 1093. D8_k984758_zh (domain=D8, difficulty=7)

```
请基于文件 danofer__texas-government-salaries__texas_salaries.csv 做一份面向知识/支持类工单分析的管理简报，重点围绕“排名与集中度”展开：先识别哪些机构、岗位和人员名称最集中、最占薪酬/记录量，再评估前N项是否呈现明显的帕累托特征。请结合真实列字段（如 AGENCY NAME、CLASS TITLE、GENDER、ETHNICITY、STATUS、HRLY RATE、HRS PER WK、MONTHLY、ANNUAL、EMPLOY DATE、multiple_full_time_jobs、combined_multiple_jobs、summed_annual_salary、hide_from_search）进行分析。需要你把工作拆成多个可并行的分析轨道，并输出一份可直接给负责人看的结构化结论：1）机构维度的记录数与年薪总额排名；2）岗位维度的集中度（前10岗位占比、累计占比）；3）员工姓名/人员维度的重复集中情况（同名同人）与是否存在多岗位/合并岗位标记；4）性别、族裔、状态维度的集中度与Top-N分布；5）新近入职 vs 老员工在年薪上的集中差异；6）对薪酬总额是否符合“前20%对象贡献大部分总额”的帕累托判断。请输出结论时尽量用百分比、Top-N、累计占比和少量关键数字，避免大表。数据文件名必须明确写入结果说明中。
```

### 1094. D8_k984960_en (domain=D8, difficulty=7)

```
Using alexandermeau__synthetic-it-support-tickets__itsm_ticket_corpus_flat.csv, analyze the support-ticket corpus with a focus on correlation and driver analysis: which numeric fields move together, the strongest rounded correlations, and the top associations that look operationally meaningful. Break it into independent workstreams so I can hand them to multiple analysts: one track should quantify field-level structure in the ticket payloads, another should examine how ticket status and record_type relate to the main numeric/ordinal signals, another should look at whether ticket complexity proxies line up with slower resolution outcomes, another should inspect frequency patterns in the correspondence/diagnostics text for recurring drivers, and another should summarize the most important correlated factors and edge cases. I need a concise analysis package that tells me what is most associated with delays, closure, and escalation risk, using only the real columns in the file.
```

### 1095. D8_k985003_zh (domain=D8, difficulty=7)

```
请基于文件 mdabbert__ultimate-ufc-dataset__ufc-master.csv 做一份面向“知识 / 支持工单分析”的数据审查，重点围绕“排行与集中度”展开：先找出最常出现、最能解释结果、以及最集中占比的群体，再看这些集中度是否在不同维度上存在结构性差异。请结合我关心的真实字段（如 Winner、weight_class、gender、finish、finish_details、country、location、R_odds/B_odds、total_fight_time_secs、title_bout、better_rank 等）输出可落地的结论，而不是只给描述性统计。我要你把分析拆成多个彼此独立的子任务，适合并行交给不同小助手执行；最后汇总成一份简洁的 analysis_summary.json。请特别关注 top-N、占比、累计占比、Pareto/80-20、以及各类结果在样本中的集中程度。
```

### 1096. D8_k985113_zh (domain=D8, difficulty=7)

```
请基于文件 mdabbert__ultimate-ufc-dataset__ufc-master.csv 做一份面向“知识/支持工单分析”场景的数据质量审计，重点围绕这个数据集里与工单/事件记录相似的字段做全面检查：缺失值、空字符串、'?'、重复记录、取值范围异常、类别值不一致、以及一些关键衍生字段是否自洽。请重点查看这些列：R_fighter、B_fighter、R_odds、B_odds、R_ev、B_ev、date、location、country、Winner、title_bout、weight_class、gender、no_of_rounds，以及各类统计字段（如 B_current_win_streak、B_avg_SIG_STR_landed、R_avg_TD_pct、height_dif、reach_dif、age_dif、sig_str_dif、avg_sub_att_dif、avg_td_dif、finish、finish_details、finish_round、finish_round_time、total_fight_time_secs、r_dec_odds、b_dec_odds、r_sub_odds、b_sub_odds、r_ko_odds、b_ko_odds 等）。我需要你把这份审计拆成 4-6 个互相独立的分析轨道，便于分给不同子任务并行跑；最后输出一份简洁的 analysis_summary.json。请给出每个问题的结论、对应异常样本的定位方式，以及必要时按 weight_class / gender / Winner / title_bout 分组的统计结果。请特别注意：不要假设数据是干净的，要明确检查空值、'?'、空白字符串、重复行、明显不合理的赔率/年龄/身高/回合数/时间值，以及分类字段是否存在未预期类别。
```

### 1097. D9_g114_zh (domain=D9, difficulty=7)

```
基于 inputs/asset_inventory.csv、inputs/findings.xlsx、inputs/remediation_actions.xlsx 和 inputs/sla_policy.json，做一次漏洞分诊与汇总，输出 2-3 个紧凑的管理层周会报告（JSON/CSV/MD），不要逐条明细。
```

### 1098. D9_g128_en (domain=D9, difficulty=7)

```
Analyze the files in inputs/: vulnerabilities.xlsx, assets.xlsx, exceptions_and_controls.xlsx, remediation_tickets.csv, and triage_snapshot.sqlite. Produce a concise analysis brief (findings.md) and a small evidence table (evidence_table.csv) that synthesize across several independent analysis tracks, include a top-10 urgent table, and highlight any cross-source conflicts.
```

### 1099. D9_g139_en (domain=D9, difficulty=7)

```
Run a triage on the four files in inputs/ (assets.xlsx, vulnerabilities.csv, finding_assignments.xlsx, exceptions.xlsx). Produce three aggregate reports in output/ (CSV/JSON/MD) showing: total unique actionable findings after dedup and invalid row exclusion; counts by severity (Critical/High/Medium/Low) and closed status (Open/In Progress/Deferred/Mitigated/Accepted Risk/Duplicate); findings with breached SLA (pinned rule); exempted by active exception; top 10 urgent using pinned risk formula; top 5 assets by max risk (ties by ascending asset_id); highest risk score; and count of invalid assignment rows excluded for unknown asset_id or cve_id.
```

### 1100. D9_g163_en (domain=D9, difficulty=7)

```
I have a security triage task covering the same control population across six input files: inputs/assets.xlsx, inputs/cve_catalog.xlsx, inputs/findings.csv, inputs/exceptions.json, inputs/scanner_evidence.log, and inputs/triage.db. I need you to produce one compact analysis brief in Markdown and one small evidence table (Markdown table or CSV snippet) of the top‑10 urgent findings. This is a research/synthesis effort: treat all inputs as evidence sources, run three to four independent analysis tracks in parallel, then reconcile them into a single brief with explicit cross‑source conflict notes. The four tracks are: 1) inventory/severity (from findings.csv + cve_catalog.xlsx + assets.xlsx), 2) SLA/age/risk (from findings.csv + assets.xlsx), 3) exception/conflict (from exceptions.json + findings.csv), and 4) evidence/log reconciliation (from scanner_evidence.log + findings.csv).

Here are the key definitions and formulas to use:

- **Universe**: all findings in findings.csv with status in {Open, In Progress, Accepted Risk, Deferred, Resolved}.  
- **Active findings**: status is Open or In Progress only.  
- **Severity buckets** (pinned by CVSS score from cve_catalog.xlsx or findings.csv): Critical ≥9.0, High ≥7.0 and <9.0, Medium ≥4.0 and <7.0, Low <4.0.  
- **SLA days**: Critical → 15, High → 30, Medium → 90, Low → 180.  
- **SLA breach**: age_days > sla_days, where age_days = 2025‑06‑01 minus detected_date (whole days).  
- **Risk score formula** (used only for ranking the urgent table):  
  `risk_score = CVSS base score + asset criticality adjustment (Tier1:+1.5, Tier2:+1.0, Tier3:+0.5) + internet exposed (Y:+1.5, N:0) + auth_required (Y:–0.5, N:0) + known_exploit (Y:+1.0, N:0) + min(2.0, max(0, age_days – sla_days) / 30)`. Round to two decimals.  
- **Urgent ranking** (for top‑10 table): sort by risk_score DESC, then CVSS DESC, then age_days DESC, then finding_id ASC.  
- **Dedup rule for evidence/log**: if the same asset_id + cve_id appears more than once in scanner_evidence.log or findings.csv, count it once for evidence notes and mention as a conflict.  
- **Exception handling**: count only exceptions whose finding_id exists in findings.csv as valid; orphan exceptions must be called out separately.

The brief should contain sections for summary, triage metrics, top risks, and cross‑source reconciliation notes. It must include the following metrics (all aggregated, no per‑finding details):

1. Total active findings count.  
2. Active counts by severity bucket (Critical, High, Medium, Low).  
3. Total active SLA‑breached findings.  
4. Active SLA‑breached rate as a percentage rounded to 1 decimal.  
5. Top‑3 urgent asset IDs by count of active findings (tie‑break by max risk_score DESC, then asset_id ASC).  
6. Top‑10 urgent findings table sorted by the risk formula above.  
7. Number of valid exceptions from exceptions.json that match a finding_id in findings.csv.  
8. Number of orphan exceptions in exceptions.json.  
9. Number of duplicate asset_id+cve_id pairs observed across findings.csv and scanner_evidence.log that require reconciliation.  
10. Number of active findings that are both internet‑exposed and have known_exploit=Y.  
11. Number of active findings on Tier1 assets.  
12. A short cross‑source conflict note listing the specific mismatches you found.

Keep the output compact and well under 40 rows total. Do not include a per‑finding remediation register. Use the exact input file names as listed.
```

### 1101. D9_g219_en (domain=D9, difficulty=7)

```
I need you to synthesize the four input files in inputs/ to produce compact aggregate reports—no per-finding register. Use exactly these files: `inputs/assets.csv`, `inputs/cves.csv`, `inputs/findings.xlsx`, `inputs/remediation_actions.xlsx`, `inputs/triage_policy.md`, `inputs/daily_security_scans.log`, and `inputs/triage_bundle.sqlite`.

Here are the pinned definitions and formulas:
- Severity buckets (CVSS v3): Critical >= 9.0, High >= 7.0 and < 9.0, Medium >= 4.0 and < 7.0, Low < 4.0.
- Status enum: exactly Open, In Progress, Mitigated, Accepted, Deferred.
- Evidence enum: exactly confirmed, suspected, false_positive.
- Dedup rule: count each finding_id once; if duplicates exist, keep the last row by file order from `findings.xlsx`.
- Risk score formula: round(cvss_v3 * (1 + 0.25*(asset_criticality-1)) * exposure_mult * evidence_mult, 2), where exposure_mult = 1.15 if internet_exposed=1 else 1.0, and evidence_mult = 1.10 if evidence_state=confirmed, 0.85 if evidence_state=false_positive, else 1.0.
- SLA breach rule: breached if status is Open or In Progress AND today (2025-06-09) is strictly later than due_date.

Produce exactly three compact files in the output directory (keep tables well under 40 rows total):
1. A CSV with the top‑10 urgent findings table (ordered by: breached first, then higher risk_score, then asset_id ascending).
2. A JSON summary containing:
   - Total unique findings after dedup.
   - Findings by severity bucket (Critical, High, Medium, Low).
   - Findings by triage status (Open, In Progress, Mitigated, Accepted, Deferred).
   - Total count of SLA-breached findings.
   - Top 5 assets by summed risk_score (tie‑break: breach_count descending, then asset_id ascending).
   - Count of Critical findings on internet‑exposed assets.
   - Count of findings with confirmed evidence.
   - Flagged asset IDs: the 5 assets with the highest summed risk_score.
3. A short Markdown note summarizing what the noisy log file (`daily_security_scans.log`) corroborates about the highest‑risk assets/CVEs, plus any triage caveats.

Do not produce a remediation register.
```

### 1102. D9_g367_zh (domain=D9, difficulty=7)

```
我们需要对几个来源的风险数据做一次整合分析，输出一份中文简报和一个小型证据表。输入文件：inputs/assets.csv、inputs/findings.csv、inputs/exceptions.xlsx、inputs/cve_mapping.xlsx、inputs/triage.sqlite。这些数据来自漏洞扫描、人工复核、例外审批和资产台账。请进行跨源汇总、去重、冲突说明和优先级排序。分析应覆盖资产风险、漏洞严重性分布、SLA逾期情况、例外影响以及来源间的一致性。最终输出findings.md和evidence_table.csv，证据表只列出少量关键行。简报中需说明去重后的唯一问题总数、各严重性数量、有效状态分布、逾期数量、TOP‑10紧急问题、最高风险项、需优先标记的资产，以及跨源冲突/异常项。
```

### 1103. D9_g368_en (domain=D9, difficulty=7)

```
I'm coordinating a security vulnerability triage exercise. I need you to synthesize the data from these inputs into 2-3 compact aggregate reports (CSV, JSON, or MD) — no per-finding register, total rows under 40.

- inputs/assets.xlsx
- inputs/findings_dedup.xlsx
- inputs/policy.md (use the policy definitions exactly as written)
- inputs/scanner_events.log (most lines are noise; only a few relevant alerts are buried inside)
- inputs/triage.db

Here's what I want from the analysis:

- A severity/status summary report showing total deduplicated findings (applying the asset_id+vuln_id dedup rule from policy.md), counts by severity bucket and by status, plus the count of findings open for action (Open + In Progress), the total number of SLA‑breached findings, and the overall breach rate.
- A top‑10 urgent findings report ranked by the risk score formula from policy.md, with asset_id, vuln_id, risk_score, severity_bucket, and status.
- A short asset‑flag summary listing only the few highest‑priority asset IDs, sorted by breach count, then critical count, then max risk score.
- A brief synthesis note explaining the most important remediation pattern based on the aggregates.

Please reference the exact input filenames in your reports (prose or headers). Keep everything compact — well under 40 rows total across all deliverables.
```

### 1104. D9_g449_zh (domain=D9, difficulty=7)

```
请基于以下输入文件帮我完成漏洞与整改triage决策简报：inputs/asset_inventory.csv、inputs/vulnerability_catalog.xlsx、inputs/findings_register.csv、inputs/asset_controls.xlsx、inputs/remediation_events.xlsx、inputs/triage.db。输出一个简短的decision_brief.md，按风险优先级给出整改建议和关键统计数字，按常规流程处理去重、状态过滤、risk_score计算及SLA breach判断即可。结果用简体中文，紧凑汇总。
```

### 1105. D9_g452_en (domain=D9, difficulty=7)

```
Synthesize the four input files — assets.xlsx, findings.xlsx, triage_exceptions.xlsx, and remediation_snapshots.xlsx — into a remediation triage summary. Produce a markdown analysis brief with sections for executive summary, cross‑source reconciliation notes, urgent top‑10 triage table, compact aggregate summary by severity and status, and a flagged asset list. Also deliver a small evidence table (CSV or markdown) containing the top‑10 urgent items with finding_id, asset_id, cve_id, severity, final_status, risk_score, due_date, sla_breached, and rationale.

Apply our standard methodology: severity buckets from CVSS, the pinned risk_score formula (cvss_base * 10 + exposure_rank * 6 + asset_criticality * 4 + internet_facing * 8 + exploit_known * 5), SLA due dates based on severity (7/30/90/180 days), and our cross‑source conflict and deduplication rules (triage_exceptions overrides status per approved_date, assets.xlsx is authoritative for asset attributes, deduplicate by finding_id with highest risk_score then latest published_date, etc.). Use current_date = 2025‑07‑31 for SLA breach checks. Exclude findings with null published_date from breach calculations but include them in severity totals. Round percentages and risk_score to one decimal; counts are integers. No row‑per‑source records, no full register — keep the evidence table under 20 rows.
```

### 1106. D9_g70_zh (domain=D9, difficulty=7)

```
请根据inputs/下的5个文件（assets.csv、cves.xlsx、findings.xlsx、exceptions.csv、incidents.xlsx）完成一份中文分析简报，输出findings.md和evidence.csv。我需要一份面向管理层的紧急处置摘要，综合漏洞严重性、资产重要性、整改状态、SLA逾期与例外信息。

分析过程：先对发现进行去重，统计去重后的发现总数。然后按Critical、High、Medium、Low四个严重等级分别统计数量，再按Open、In Progress、Mitigated、Accepted Risk、Deferred五个状态分别统计数量。接着，根据标准SLA规则（如不同严重等级的修复期限）计算逾期发现总数和逾期率。同时，计算所有发现中pinned risk_score字段的平均值（保留两位小数）。然后，按照固定的urgent_score公式计算每个发现的紧急得分，输出得分最高的前10个发现，表中至少包含finding_id、asset_id、cve_id、severity、status、risk_score和urgent_score。此外，识别出前5个需要重点关注的asset_id（基于风险优先级）。

在findings.md中，必须明确说明你使用的去重规则、严重性等级划分、SLA规则与risk_score的计算公式。同时，指出至少两处跨源数据不一致或异常记录，并说明你的处理方式。报告应包含“总体结论”、“发现分布”、“逾期与风险优先级”、“跨源冲突与异常处理”和“建议”五个部分，全部使用中文。evidence.csv只保留与Top-10紧急发现和Top-5重点资产直接相关的最小证据集，行数不超过15行。

这是一个汇总型分析，不要输出逐条修复台账，只需给出综合结论和优先级排序。
```

### 1107. D9_g75_zh (domain=D9, difficulty=7)

```
我需要你基于 inputs/ 下的 4 个源文件完成一次安全漏洞整改分诊与风险汇总分析，输出一份中文分析简报（findings.md）和一张简短证据表（evidence_table.csv）。目标是把多源材料合并后形成可供风险委员会直接使用的紧凑摘要，并明确写出跨来源冲突/不一致的处理结果。

必须使用的输入文件：
- inputs/assets.csv
- inputs/findings_raw.xlsx
- inputs/control_mapping.xlsx
- inputs/remediation_notes.csv

我这里直接给出处理规则，请你严格遵循：

严重性分桶只使用以下闭集：Critical, High, Medium, Low。CVSS 分桶阈值：Critical >= 9.0；High >= 7.0 且 < 9.0；Medium >= 4.0 且 < 7.0；Low < 4.0。

去重规则：按 duplicate_key 去重，保留 discovered_at 最早的那条；若时间相同，再保留 finding_id 字典序最小的那条。

status 只允许 Open, In Progress, Mitigated, Accepted Risk；任何其他值一律归一为 Open。

SLA 到期天数：Critical 15 天、High 30 天、Medium 60 天、Low 90 天。SLA 违约定义为：status 属于 Open 或 In Progress 且 as_of=2026-06-01 严格晚于 due_date。

pinned 风险分数公式：risk_score = round(cvss_base*10 + exposure*2 + asset_criticality*1.5 + internet_facing*4 + exploit_confirmed*8 + max(days_overdue,0)*1.2 + (duplicate_count-1)*3, 2)，其中 days_overdue = as_of - due_date 的整天数。

输出要求（全部体现在简报中，evidence_table 可辅助展示）：

1. 给出去重前记录总数、去重后唯一 finding 总数、以及因 duplicate_key 去除的重复数。
2. 给出按上述 CVSS 阈值分桶后的 Critical/High/Medium/Low 数量。
3. 给出按标准化 status 分组后的 Open / In Progress / Mitigated / Accepted Risk 数量。
4. 给出 SLA 已违约的唯一 finding 数量，以及当前仍处于 Open 或 In Progress 的唯一 finding 数量。
5. 给出按 pinned risk_score 排序的 TOP-10 紧急清单，字段只列 asset_id、cve_id、severity、status、risk_score。
6. 给出需要重点跟进的前 5 个资产 ID 列表（按受影响高危/严重且违约或暴露在公网的综合优先级选取）。
7. 给出平均 cvss_base（保留 2 位小数），并写出 2-3 条跨来源 reconciliation 结论，至少覆盖：重复项、状态归一化、严重性/备注冲突。
8. 给出 control_mapping.xlsx 参与到本次分析的 CWE 覆盖情况摘要：出现过的 CWE 数量，以及其中映射到控制项的 CWE 数量。

请把结论写成自然的中文业务简报，必须明确说明你如何处理了文件间冲突与异常值。
```

### 1108. D9_g981084_zh (domain=D9, difficulty=7)

```
请基于 cve_master.xlsx、asset_remediation_register.xlsx 和 triage_event_log.xlsx 这三份材料，输出一份单文件的中文分析简报 findings.md。我希望你把它写成一份面向安全治理评审的汇总，不要做成逐条清单式的修复登记。请同时看漏洞主数据、资产修复登记和事件日志三条线，做交叉核对，并在简报里明确写出来源之间是否一致、哪里有冲突、哪里需要人工复核。我最关心的是整体风险态势、按严重级别的总量、资产修复状态分布、最紧急的前十个资产，以及少量需要单独标记的资产 ID。请保持输出紧凑，结果以表格和小结为主，必要时补一两句解释即可。
```

### 1109. D9_g981310_zh (domain=D9, difficulty=7)

```
请基于我放在 inputs 里的三份材料，帮我做一份安全漏洞处置 triage 简报，输出成 findings.md。
- 主表是 vulnerability_triage_master.xlsx，另外还有 remediation_exceptions.csv 和 asset_context.json。
- 我要的是一页式分析摘要，不是逐条登记表。
- 重点看三类东西：整体风险分布、最紧急的前十项、以及需要我立刻盯住的资产。
- 记得把不同来源之间对不上、重复记录、例外状态不一致的地方单独写出来。
- 结果里请把关键数量、Top 10 表和冲突点都整理清楚，方便我拿去开会。
```

### 1110. D9_g981611_zh (domain=D9, difficulty=7)

```
请基于 inputs/vulnerability_findings.xlsx、inputs/owner_sla.csv 和 inputs/exceptions.json 做一版安全漏洞处置决策简报，重点是 triage、逾期风险和优先级排序。
- 先把被压制的重复/误报记录排除，再汇总整体态势：按严重性、状态和 SLA 逾期情况给出关键数量。
- 输出一个 Top 10 紧急资产表，按风险分从高到低排序，并标出最需要先处理的少量资产ID。
- 结合 owner 维度说明哪些团队最需要优先投入，并给出一页式结论，明确推荐先做什么、为什么。
- 最终只要一个简短的决策文件，内容要能直接拿给管理层看。
```

### 1111. D9_g981673_zh (domain=D9, difficulty=7)

```
请基于 inputs/findings.xlsx、inputs/remediation_register.xlsx、inputs/asset_inventory.xlsx、inputs/control_mapping.csv、inputs/exec_requirements.json 做一版安全漏洞/整改分诊决策简报。我要的是一份可直接拿去开周会的结论文件，重点是把当前整改面、逾期压力、最高风险优先级和需要点名的资产讲清楚。请输出一个简短的决策简报文件，里面要有结论排序、关键数字和建议处置顺序，不要展开成逐条漏洞清单。
```

### 1112. D9_g981785_zh (domain=D9, difficulty=7)

```
请基于 inputs/triage_rules.xlsx、inputs/findings_inventory.xlsx 和 inputs/triage_snapshot.xlsx，帮我整理一份面向管理层的漏洞处置汇总报告，重点看总体风险、严重度分布、处置状态、逾期情况，以及最紧急的 Top 10 清单和少量需要优先盯住的资产。
```

### 1113. D9_g981801_zh (domain=D9, difficulty=7)

```
这批漏洞和整改台账要尽快给管理层出一个决策简报，判断哪些资产和问题要优先推进、哪些可以暂缓。我放了三份材料在 inputs 里：vuln_triage_master.xlsx、remediation_register_snapshot.csv、sla_policy.json。请你把它们整理成一份简短的决策文件，重点告诉我总体风险分布、最紧急的前 10 条问题、哪些资产最值得先处理，以及需要特别标出来的少数资产；我还想看到去重后口径下的关键汇总，避免重复记录把判断带偏。
```

### 1114. D9_g981857_en (domain=D9, difficulty=7)

```
I need you to put together a quick decision brief from our vulnerability scan results. The scan file is inputs/vuln_scan_results.xlsx and there's an audit report in inputs/audit_report.pdf. I want a summary of the most critical findings, highlighting any differences between the two sources, and a top-10 prioritized list for remediation. Just a short markdown file with the key numbers and recommendations.
```

### 1115. D9_g981990_zh (domain=D9, difficulty=7)

```
我需要你把这三份材料——triage_findings_master.xlsx、remediation_overrides.csv、cve_reference.json——整理成一份中文的风险处置分析简报 findings.md。请按严重级别、状态、SLA 逾期、TOP 10 高风险工单、重点资产和跨文件冲突这几条线索分别看，再把结论合成一份能给管理层看的摘要，顺手把几处冲突说明清楚。
```

### 1116. D9_k982294_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全分析的复杂多阶段分析，重点围绕“排名与集中度”展开：先找出最主要的入侵/正常类别、最集中的协议/服务/标志组合，再看这些头部群体在流量与告警特征上是否形成明显的 Pareto 结构。请同时结合数值特征（如 src_bytes、dst_bytes、count、srv_count、serror_rate、same_srv_rate、diff_srv_rate）和类别特征（protocol_type、service、flag、class）做拆解，输出能支持安全运营优先级排序的结论。我要你把分析拆成 4-6 个彼此独立的分析轨道，适合分给不同子代理并行做；最后汇总成一个可落地的分析摘要文件 analysis_summary.json。请特别关注：1）class/协议/服务/flag 的 Top-N 频次与覆盖率；2）头部组是否贡献了大部分样本或大部分异常；3）异常样本中最集中的组合；4）不同头部群体的关键数值特征对比；5）是否存在少数高风险组合主导整体风险的现象。
```

### 1117. D9_k982331_en (domain=D9, difficulty=7)

```
Analyze subhajournal__iotintrusion__IoT_Intrusion.csv for security analytics with a strong focus on temporal/sequence behavior. Use the available flow-level sequence field(s) to study how intrusion patterns evolve over ordered records, especially period-over-period changes in rate-related features and whether certain attack labels become more or less bursty across the sequence. I need a concise but rigorous summary of what changes over time, which labels drive the shifts, and whether any protocol/flag combinations show stable vs spiking behavior. Please use the real columns such as flow_duration, Rate, Srate, Drate, the TCP/UDP/HTTP/HTTPS/DNS protocol indicators, the flag/count fields, and label. Split the work so different parts can be analyzed independently and then merged into one written summary plus a compact JSON output.
```

### 1118. D9_k982356_zh (domain=D9, difficulty=7)

```
请帮我对文件 sampadab17__network-intrusion-detection__Test_data.csv 做一版面向安全分析的综合数据解读，重点围绕“数值字段之间的相关性与驱动因素”展开：先找出哪些数值指标彼此最强相关、哪些指标和连接异常特征最可能共同变化，再结合协议/服务/标记等类别字段补充解释。请把结果整理成 analysis_summary.json，并且拆成 4-6 个彼此独立的分析轨道，方便不同同事并行处理。重点要回答：1）总体上最值得关注的强相关对有哪些；2）在攻击/异常迹象更明显的连接里，哪些数值特征最能区分；3）不同 protocol_type、service、flag 下关键数值指标是否有系统性差异；4）哪些字段看起来是“联动”而不是独立变化；5）请给出可复核的、四舍五入到 2 位小数的相关性/比例/均值结论。
```

### 1119. D9_k982386_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份安全分析，重点围绕“分布与阈值分层”：把流量按关键业务阈值分成高/低风险 cohorts，比较各 cohort 的占比、特征均值、中位数和协议/服务/标志组合构成，并找出异常集中出现的区间。请直接使用数据中的真实列来分析，尤其关注 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、logged_in、is_guest_login、protocol_type、service、flag，以及 dst_host_* 相关字段。我要一个可落地给安全运营团队的结论，输出面向阈值分层、分布偏态、组合占比和可疑模式识别的分析结果。
```

### 1120. D9_k982395_en (domain=D9, difficulty=7)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, do a security-analytics segmentation review of the test traffic with emphasis on categorical-group comparisons. I want a concise but thorough breakdown that compares protocol_type, service, and flag segments on key traffic-intensity and attack-indicator metrics, identifies the biggest gaps between groups, and flags any combinations that look unusually attack-like or benign-like. Please structure it so a small team could work independently: one track for protocol_type comparisons, one for service comparisons, one for flag comparisons, one for cross-segment interactions among protocol_type/service/flag, and one for outlier-style segment findings using the numeric rate fields and connection-volume fields. Use the real columns in the file, especially duration, src_bytes, dst_bytes, logged_in, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, and the destination-host rate/count fields.
```

### 1121. D9_k982419_en (domain=D9, difficulty=7)

```
Using the file sampadab17__network-intrusion-detection__Test_data.csv, please run a security-analytics review focused on correlation and driver analysis across the numeric fields. I need a concise but rigorous readout of which measures move together, which features are the strongest associations, and what that suggests about attack-style traffic in this test set. Please treat the dataset as fixed and use the real columns only, especially duration, src_bytes, dst_bytes, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, srv_diff_host_rate, dst_host_count, dst_host_srv_count, dst_host_same_srv_rate, dst_host_diff_srv_rate, dst_host_same_src_port_rate, dst_host_srv_diff_host_rate, dst_host_serror_rate, dst_host_srv_serror_rate, dst_host_rerror_rate, and dst_host_srv_rerror_rate. Decompose the work into independent tracks so separate analysts could handle them in parallel: (1) numeric correlation structure and the strongest positive/negative pairs, (2) driver analysis for the key rate variables, (3) byte-volume versus connection-volume relationships, (4) host-based versus service-based network-activity relationships, and (5) segmentation checks by protocol_type / flag to see whether the strongest correlations differ across slices. Please return the results in analysis_summary.json.
```

### 1122. D9_k982422_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的多部分诊断报告，重点围绕“时间/序列趋势”来展开：由于数据里没有显式日期，请把样本行顺序当作观测序列，分析前后段以及滚动窗口中的异常变化、攻击/正常流量信号的阶段性漂移、以及关键连接特征的变化。请务必结合这些真实字段：duration、protocol_type、service、flag、src_bytes、dst_bytes、logged_in、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、srv_diff_host_rate、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_same_src_port_rate、dst_host_srv_diff_host_rate、dst_host_serror_rate、dst_host_srv_serror_rate、dst_host_rerror_rate、dst_host_srv_rerror_rate。希望你把分析拆成几条彼此独立的轨道，分别回答：1) 序列前后两段的协议/状态分布是否发生显著漂移；2) 滚动窗口内最明显的异常峰值和拐点在哪里；3) 关键错误率和相似度指标是否存在持续上升/下降趋势；4) 不同 service 在序列中的阶段性暴露变化；5) 高风险连接模式（例如 S0、REJ、RSTO 等 flag）是否集中在某些序列区间；6) 给出一个可复核的紧凑结果摘要，方便我继续做后续调查。请只输出可直接核对的分析结论，不要画图，不要训练模型，不要做随机抽样。
```

### 1123. D9_k982429_en (domain=D9, difficulty=7)

```
Analyze sampadab17__network-intrusion-detection__Train_data.csv as a security analytics time/sequence study using the available connection-order in the file. I want a multi-part investigation centered on temporal trends and period-over-period change in intrusion behavior: track how anomaly vs normal rates evolve over the row sequence, identify the largest shifts in traffic volume and attack indicators across consecutive blocks, compare protocol/service/flag mixes before and after major changes, and summarize which features show the clearest trend breaks. Use the real columns in the file, especially duration, protocol_type, service, flag, src_bytes, dst_bytes, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, and class. Please produce a concise analysis summary for security analysts and highlight any periods where the intrusion signature changes materially.
```

### 1124. D9_k982524_en (domain=D9, difficulty=7)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, run a security analytics review focused mainly on correlation and driver analysis: identify which numeric network-traffic fields move together, surface the strongest rounded correlations, and explain the likely behavioral drivers behind those relationships. Please break it into independent workstreams so different people can work in parallel: one track on overall numeric correlation structure, one on protocol/service/flag segmentation of key drivers, one on high-traffic vs low-traffic behavior, one on error-rate and count-based alert patterns, and one on any suspicious extreme-value records that dominate the correlation picture. Use the real columns in the file, including duration, src_bytes, dst_bytes, land, wrong_fragment, urgent, hot, num_failed_logins, logged_in, num_compromised, root_shell, su_attempted, num_root, num_file_creations, num_shells, num_access_files, num_outbound_cmds, is_host_login, is_guest_login, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, and the dst_host_* features.
```

### 1125. D9_k982569_en (domain=D9, difficulty=7)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, analyze the test traffic with a focus on temporal/sequence behavior across the connection order in the file. I need a security-analytics readout that covers how attack-like signals evolve over the record sequence, especially changes in `count`, `srv_count`, the four error-rate fields (`serror_rate`, `srv_serror_rate`, `rerror_rate`, `srv_rerror_rate`), and the relationship to `flag`, `protocol_type`, and `service`. Please break it into independent workstreams so different analysts can work in parallel: one track on period-over-period changes by sequence segments, one on flag/service mix shifts, one on protocol-specific trend differences, one on high-risk burst detection using rolling windows, one on threshold-based escalation patterns, and one on correlation/association changes among the rate features over time. Summarize the findings in a concise JSON-style deliverable with actionable observations for intrusion monitoring.
```

### 1126. D9_k983103_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全运营的异常/离群分析，重点围绕“显式数值规则”来找可疑流量：例如对 duration、src_bytes、dst_bytes、count、srv_count 以及各类 rate 字段设置阈值、IQR 极值、以及 rare 类别（protocol_type/service/flag）的组合规则。请不要做建模预测，只做可审计、可复现的规则型分析，并把结果整理成一份适合给值班分析师看的摘要。希望你拆成 4-6 条彼此独立的分析线并并行完成，至少包括：1）极端数值/离群点统计；2）稀有协议/服务/标志组合；3）多字段规则命中的可疑样本画像；4）不同协议或服务下的异常密度对比；5）字段间相关性或共异常关系；6）给出最值得人工复核的样本索引清单。请严格基于表中真实列名进行分析。
```

### 1127. D9_k983213_en (domain=D9, difficulty=7)

```
Using subhajournal__iotintrusion__IoT_Intrusion.csv, run a security analytics review focused mainly on temporal/trend behavior across the sequence-like fields in the dataset (especially flow_duration, Duration, Rate, Srate, Drate, and the packet/flag counters). I need a multi-part assessment that tells me how attack behavior changes over the ordered records, where there are abrupt shifts in traffic intensity, and which labels show the clearest period-over-period changes. Please also connect the trend findings to protocol/flag patterns so I can understand whether bursts in rate align with specific intrusion types. Use the real columns in the file, including label, Protocol Type, TCP/UDP/HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC/DHCP/ARP, fin/syn/rst/psh/ack/ece/cwr flags, and the summary stats columns (Tot sum, Min, Max, AVG, Std, Tot size, IAT, Number, Magnitue, Radius, Covariance, Variance, Weight) where helpful. I want a concise but rigorous analyst-style output that is suitable for a security operations briefing.
```

### 1128. D9_k983234_zh (domain=D9, difficulty=7)

```
请基于数据文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一版面向安全运营的多维分析，重点放在“时间/序列趋势”上：把 flow_duration、Duration、Rate、Srate、Drate 当作流量随时间/会话推进的演化指标，结合 label（攻击类型）分析不同阶段的变化、峰值、增速和异常抬升。请输出可直接给管理层和 SOC 团队使用的结论，最好能指出哪些攻击在序列上最早爆发、哪些指标随序列增长最明显、以及不同协议/服务与攻击类型之间的趋势差异。除了趋势主线，也请兼顾协议分布、标志位行为、服务端口特征和统计特征之间的关系，但不要做机器学习建模。请基于真实列名分析：flow_duration、Header_Length、Protocol Type、Duration、Rate、Srate、Drate、fin_flag_number、syn_flag_number、rst_flag_number、psh_flag_number、ack_flag_number、ece_flag_number、cwr_flag_number、ack_count、syn_count、fin_count、urg_count、rst_count、HTTP、HTTPS、DNS、Telnet、SMTP、SSH、IRC、TCP、UDP、DHCP、ARP、ICMP、IPv、LLC、Tot sum、Min、Max、AVG、Std、Tot size、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight、label。请把结果整理成一份 analysis_summary.json。需要拆成 4-6 个彼此独立的分析轨道，便于不同子任务并行推进。
```

### 1129. D9_k983238_zh (domain=D9, difficulty=7)

```
请基于 `sampadab17__network-intrusion-detection__Test_data.csv` 做一份面向安全分析的多部分数据分析，重点放在**数值字段之间的相关性与驱动因素**：哪些指标高度同向/反向变化、哪些特征最能解释异常连接特征、以及不同协议/服务/标志下这些关系是否一致。请直接读取文件中的真实字段（例如 `duration`, `src_bytes`, `dst_bytes`, `count`, `srv_count`, `serror_rate`, `srv_serror_rate`, `rerror_rate`, `srv_rerror_rate`, `same_srv_rate`, `diff_srv_rate`, `dst_host_count`, `dst_host_srv_count`, `dst_host_same_srv_rate`, `dst_host_diff_srv_rate`, `dst_host_serror_rate`, `dst_host_rerror_rate` 等），不要假设标签或做建模。你需要拆成 4-6 个彼此独立的分析轨道：1) 全局相关性矩阵与最强正/负相关对；2) 与攻击迹象/异常会话特征最相关的数值驱动因素；3) 按 `protocol_type` 分组的相关结构对比；4) 按 `service` 或 `flag` 分组检验关键相关关系是否稳定；5) 对极端值/异常连接做一个小型剖析，看这些记录的相关模式是否偏离整体。最终输出一份适合安全分析师复核的 `analysis_summary.json` 风格结论摘要，包含可解释的要点、top 关联关系、以及需要进一步排查的特征组合。
```

### 1130. D9_k983416_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全运营的复杂分析，重点围绕“时间/序列趋势”展开：把样本按记录顺序当作一个代理时间轴，分析正常与异常流量在前后阶段、滚动窗口和变化率上的演变，找出最能体现攻击活跃度上升/下降的特征，以及哪些服务、协议和连接状态在序列中最先出现异常信号。除了趋势主线外，也请同时做一次行为画像和异常分层：按 protocol_type、service、flag 分组比较在不同序列阶段的异常占比变化，结合 src_bytes、dst_bytes、count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate 等字段，识别最值得关注的持续恶化模式。希望输出一份适合安全分析师汇报的结论，并附带可复核的关键统计。
```

### 1131. D9_k983483_zh (domain=D9, difficulty=7)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的多部分数据分析，重点围绕“相关性与驱动因素分析”展开：哪些数值字段彼此一起变化、哪些字段和 label 最相关、以及不同攻击类型的关键数值特征差异。请直接使用数据中的真实列名（例如 flow_duration、Header_Length、Protocol Type、Duration、Rate、Srate、Drate、ack_count、syn_count、fin_count、urg_count、rst_count、Tot sum、Min、Max、AVG、Std、Tot size、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight 等），不要改列名。希望你把结果拆成可并行处理的 4-6 个独立分析轨道，并输出一份可供安全团队复核的简洁结论，特别强调：1）整体数值相关矩阵中最强的正/负相关对；2）与 label 关系最强的驱动字段；3）按攻击类别比较关键特征的差异；4）识别可能存在冗余或共线性的字段组；5）给出面向检测规则设计的简短建议。
```

### 1132. D9_k983492_zh (domain=D9, difficulty=7)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的分布与阈值分层报告，重点围绕“业务阈值以上/以下的流量占比、分位数分桶后的攻击类型混合、以及不同协议/标志位组合在各阈值区间中的构成差异”展开。请直接使用表中的真实字段（例如 flow_duration、Header_Length、Rate、Srate、Drate、ack_count、syn_count、HTTP、HTTPS、DNS、Telnet、SMTP、SSH、IRC、TCP、UDP、DHCP、ARP、ICMP、IPv、LLC、Tot sum、Min、Max、AVG、Std、Tot size、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight、label），不要假设任何额外字段。请把工作拆成 4-6 个彼此独立的分析轨道，适合并行分给多个子分析员：1）核心连续变量的阈值分层与分位桶分布；2）label 在不同阈值/分桶中的构成与集中度；3）协议与标志位在高风险/低风险区间的混合特征；4）若干关键字段之间的相关性与极端值分布；5）针对业务可解释阈值的告警候选清单（例如高 Rate、高 Srate、高 Std、高 Covariance 等）；6）必要时对多重阈值交集做交叉统计。最后输出一份简洁的分析摘要 JSON，强调哪些区间最值得优先告警、哪些标签在高阈值区间占比最高，以及哪些字段最适合作为阈值规则的候选。
```

### 1133. D9_k983495_zh (domain=D9, difficulty=7)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一版面向安全运营的异常与离群分析，重点围绕“明确数值规则”的异常识别：例如按 IQR、分位数、极端值阈值、稀有类别和组合条件去找异常流量/样本。请直接读取数据并围绕这些字段开展分析：flow_duration、Header_Length、Protocol Type、Duration、Rate、Srate、Drate、各类 flag/count、HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC/TCP/UDP/DHCP/ARP/ICMP/IPv/LLC、以及 label。我要你输出一份简洁的 analysis_summary.json，里面要能回答：1）整体异常值分布有多严重；2）按 label 看哪些类别最容易触发极端规则；3）哪些字段最容易出现离群点；4）是否存在稀有协议/标签的高风险组合；5）按 explicit thresholds 定义的异常样本数量和占比；6）如果把这些规则叠加，哪些样本会被判为“高风险异常”。请把分析拆成多个彼此独立的轨道，便于并行核查，最后合并成结论和可执行检查清单。
```

### 1134. D9_k983644_en (domain=D9, difficulty=7)

```
Using `inputs/sampadab17__network-intrusion-detection__Train_data.csv`, please run a security-analytics deep dive focused mainly on correlation and driver analysis: identify which numeric fields move together, report the strongest rounded correlations, and explain which traffic features appear to co-vary with `class` and with each other. Break this into independent workstreams so a small team can work in parallel: (1) overall numeric correlation structure, (2) correlations with `class` / anomaly vs normal separation, (3) high-activity and byte-volume drivers (`src_bytes`, `dst_bytes`, `count`, `srv_count`), (4) error-rate and service-state drivers (`serror_rate`, `srv_serror_rate`, `rerror_rate`, `srv_rerror_rate`, `same_srv_rate`, `diff_srv_rate`), (5) protocol/service/flag comparisons for the biggest correlation patterns, and (6) a concise security interpretation of the top co-moving variables and any likely redundancies.
```

### 1135. D9_k983731_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一版面向安全运营的复杂分析，重点围绕“时间/序列趋势”来判断攻击流量是否在训练样本中呈现出阶段性变化、爆发、回落或结构切换。这个数据没有真实日期字段，所以请把样本行顺序当作观测序列来分析，并把前半段/后半段、前 10%/后 10%、滚动窗口变化、以及连续区间内的异常占比变化都纳入考虑。请你结合真实列名（例如 duration、protocol_type、service、flag、src_bytes、dst_bytes、count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate、dst_host_count、dst_host_srv_count、dst_host_serror_rate、dst_host_rerror_rate、class 等）做一份可交付给安全分析师的结论摘要。

我希望你把工作拆成 4-6 条彼此独立的分析线，便于不同子任务并行推进：
1) 序列前后段的异常率与关键指标趋势对比；
2) 攻击/正常样本在序列位置上的持续性和爆发点识别；
3) 不同 protocol_type / service / flag 在前后段的结构变化；
4) 与攻击最相关的一组行为指标在序列上的变化（例如 count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate、dst_host_*）；
5) 找出最典型的前后段类别迁移或占比翻转现象；
6) 给出适合安全运营复核的异常窗口与重点观察字段清单。

请输出一份结构化 summary，并确保所有判断都基于该 CSV 的真实数据，不要臆造任何数值。
```

### 1136. D9_k983910_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的多部分数据分析，重点围绕“数值特征之间的相关性与驱动因素”展开：先确认哪些数值字段在攻击/异常行为下会一起变化，再找出最强的正负相关组合和高联动特征组，最后结合协议类型、服务、flag 和登录/流量特征解释这些关联是否具有安全含义。请只用这份数据里真实存在的字段（例如 duration、src_bytes、dst_bytes、logged_in、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、srv_diff_host_rate、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_same_src_port_rate、dst_host_srv_diff_host_rate、dst_host_serror_rate、dst_host_srv_serror_rate、dst_host_rerror_rate、dst_host_srv_rerror_rate 等），输出可直接给安全团队看的结论、可核查的统计结果和对应的驱动解释。任务要拆成 4-6 个彼此独立的分析轨道，方便并行推进。
```

### 1137. D9_k983989_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全分析的入侵流量分布与阈值分层分析。重点不要只看整体均值，而要围绕“业务阈值/分位数分层/高风险占比”展开：例如 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate 这些字段，在正常(normal)与异常(anomaly)之间的分布差异、阈值以上/以下的样本占比、分位数桶中的异常混合率、以及不同协议/服务/flag 组合在这些阈值层中的风险构成。请输出可直接给安全运营团队使用的结论摘要，并将结果整理成 analysis_summary.json。希望拆成 4-6 个彼此独立的分析轨道，便于并行处理：一条做整体分布与阈值命中率，一条做按 class 的阈值混合率，一条做按 protocol_type/service/flag 的风险结构，一条做关键数值字段的分位数桶比较，一条做高风险记录画像（多阈值同时命中），如有余力再补一条检查缺失值/异常值与字段一致性。
```

### 1138. D9_k983991_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份安全分析，重点放在“按类别分组后的差异对比”上。请直接读取并分析这些真实字段：protocol_type、service、flag、duration、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、logged_in、is_guest_login、land、urgent、hot、num_failed_logins、num_compromised、root_shell、su_attempted、num_root、num_file_creations、num_shells、num_access_files、is_host_login、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_same_src_port_rate、dst_host_srv_diff_host_rate、dst_host_serror_rate、dst_host_srv_serror_rate、dst_host_rerror_rate、dst_host_srv_rerror_rate。请把分析拆成 4-6 条彼此独立的轨道，适合并行给多个子代理分别做。核心任务是比较不同类别分组之间的均值/比例/中位数差异，找出差异最大的 segment，并结合安全语义解释哪些分组更像可疑流量、拒绝型流量、正常交互或扫描/探测型模式。请至少覆盖：1) protocol_type 分组差异；2) service 分组差异；3) flag 分组差异；4) 登录/权限/异常交互特征在不同分组中的对比；5) 连接强度与主机级统计在不同分组中的对比；6) 找出各类指标上差异最大的前若干组。最终输出一份可执行的分析摘要文件 analysis_summary.json。
```

### 1139. D9_k983996_zh (domain=D9, difficulty=7)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一版面向安全分析的分布与阈值分层分析，重点围绕“阈值以上/以下的流量占比、分位数分桶、以及不同攻击标签的混合占比”来展开。请直接读取 df 中的真实字段（例如 flow_duration、Header_Length、Protocol Type、Duration、Rate、Srate、Drate、ack_count、syn_count、HTTP、HTTPS、DNS、Telnet、SMTP、SSH、IRC、TCP、UDP、DHCP、ARP、ICMP、IPv、LLC、Tot sum、Min、Max、AVG、Std、Tot size、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight、label），不要做建模，重点做可落地的阈值 cohort 分析。请把结果整理成 analysis_summary.json，要求能回答：1）哪些指标在业务阈值之上/之下的样本占比最高；2）按分位数切桶后各桶的样本数和攻击标签混合情况；3）不同标签在关键阈值 cohort 中的分布差异；4）哪些协议/标志位组合最常出现在高风险 cohort；5）从统计上识别最值得关注的异常分布段，并给出可复核的数值。请把分析拆成多个彼此独立的子任务，便于分别并行处理。
```

### 1140. D9_k984025_en (domain=D9, difficulty=7)

```
Using sampadab17__network-intrusion-detection__Train_data.csv, build a security analytics memo focused mainly on temporal / trend behavior over the sequence of records (treat row order as the observation sequence since there is no timestamp). I need you to split the work into independent tracks: (1) overall anomaly rate trends across the dataset in rolling/period buckets, (2) how key traffic volume features like src_bytes, dst_bytes, count, and srv_count evolve between early vs late records and quarter segments, (3) whether protocol_type, service, and flag mixes shift over the sequence and how those shifts relate to anomaly prevalence, (4) whether the rate-based intrusion indicators (serror_rate, rerror_rate, same_srv_rate, diff_srv_rate and related fields) change materially over time, (5) identify the biggest step-changes or period-over-period changes in suspicious behavior using simple deterministic bucketed comparisons, and (6) summarize any notable class-conditioned differences that help explain the observed trends. Please use the real columns in the file, keep all values fixed, and produce a concise analysis_summary.json with clear findings and supporting metrics.
```

### 1141. D9_k984055_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全运营的异常/离群检测分析，重点不要做建模，而是用明确、可复核的数值规则来找可疑流量：比如对 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate 以及若干离散字段（protocol_type、service、flag）设置阈值、IQR、极端值、稀有类别规则，识别异常样本、分层统计、规则冲突和误报风险。请输出一个可直接给 SOC/威胁分析同事看的结论摘要，说明哪些规则最敏感、哪些组合最可疑、正常/异常标签在这些规则下的差异，以及需要进一步人工复核的样本类型。请同时覆盖 4-6 个彼此独立的分析轨道，例如：1）单变量极端值与 IQR 离群；2）按类别字段的稀有类别与异常占比；3）多规则命中交集与冲突；4）按 class 的规则命中率对比；5）关键数值字段的相关性/联动异常；6）可解释的高风险样本画像。
```

### 1142. D9_k984151_en (domain=D9, difficulty=7)

```
Analyze the file sampadab17__network-intrusion-detection__Train_data.csv for a security-analytics review focused mainly on temporal / trend analysis over the sequence fields available in the data. Treat the observations as ordered in file order and look for period-over-period shifts in attack mix, protocol/service behavior, and intrusion indicators. Please break the work into independent tracks for: (1) overall anomaly-vs-normal trend by row blocks, (2) changes in protocol_type/service/flag composition over time, (3) trend shifts in traffic volume and connection-count features such as duration, src_bytes, dst_bytes, count, and srv_count, (4) trend shifts in error/scan indicators like serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, and diff_srv_rate, and (5) any concrete security takeaways about which block(s) look most suspicious and why. Use only the actual columns in the CSV and keep conclusions grounded in deterministic aggregates from the data.
```

### 1143. D9_k984192_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的分层阈值审计：我想重点看这批网络连接样本在不同业务阈值下的分布、桶分布和占比结构，判断哪些特征更像正常流量、哪些更像异常或高风险会话。请围绕以下列做分析：duration、src_bytes、dst_bytes、count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate、protocol_type、service、flag，以及必要时结合 land、logged_in、is_guest_login、hot、num_failed_logins、num_compromised、root_shell、su_attempted、num_root、num_file_creations、num_shells、num_access_files、is_host_login、num_outbound_cmds。请输出可直接给管理层看的分析结论，但不要画图。重点按阈值做分群：例如 0、低值、较高值、极高值；按分位数做桶；按协议/服务/标志位做混合占比。请把分析拆成若干互相独立的子任务，方便并行处理，并给出最终的阈值分布摘要和可疑组合特征。
```

### 1144. D9_k984267_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的多维关联诊断，重点围绕“哪些数值字段会一起变化、哪些组合最能驱动异常流量特征”展开。请直接使用表中的真实列（例如 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate，以及 dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_same_src_port_rate、dst_host_srv_diff_host_rate、dst_host_serror_rate、dst_host_srv_serror_rate、dst_host_rerror_rate、dst_host_srv_rerror_rate 等）。我需要一份可落地的分析结论，不要泛泛而谈，优先给出：1）数值字段相关性矩阵里的最强正/负相关对；2）围绕攻击/异常征兆的驱动变量排序；3）按协议、服务、flag 分层后这些相关关系是否稳定；4）高风险特征组合的频次与典型模式；5）对 count / srv_count 以及各类 error rate、same/diff rate 的联动解读。请把结果整理成 analysis_summary.json 可直接汇总给管理层。
```

### 1145. D9_k984298_en (domain=D9, difficulty=7)

```
Analyze `inputs/sampadab17__network-intrusion-detection__Train_data.csv` for security-analytics trends in intrusion behavior, focusing mainly on temporal/sequence-style change patterns using the available observation order as the sequence. I need a compact but rigorous analysis that tracks how anomaly/normal behavior changes across the dataset, especially shifts in attack signatures, protocol/service usage, and key rate features over successive rows. Please break it into independent workstreams so different analysts can work in parallel: one on anomaly prevalence over sequence windows, one on protocol/service/flag mix changes over the sequence, one on feature-rate drift for the core traffic metrics, one on identifying abrupt transition points between normal and anomaly blocks, and one on summarizing the most informative class-separated differences in the sequence slices. Use the real columns in the file, including `class`, `protocol_type`, `service`, `flag`, `count`, `srv_count`, `serror_rate`, `srv_serror_rate`, `rerror_rate`, `srv_rerror_rate`, `same_srv_rate`, `diff_srv_rate`, and the host-rate fields. Deliver a single analysis summary JSON with concise findings and any notable sequence-based change points.
```

### 1146. D9_k984320_zh (domain=D9, difficulty=7)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的多部分数据分析，重点放在“按类别分组后的指标对比”和“不同攻击/协议/方向之间的差异”上。请围绕 label、Protocol Type、TCP/UDP/DHCP/ARP/HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC 这些类别变量，以及 flow_duration、Duration、Rate、Srate、Drate、Header_Length、ack_count、syn_count、fin_count、rst_count、urg_count、Tot sum、Min、Max、AVG、Std、Tot size、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight 等数值特征，找出：1）不同 label 之间哪些流量指标差异最大，2）不同协议类型在速率/时延/统计特征上的分布差异，3）TCP/UDP/DHCP/ARP 等标志位组合对应的典型画像，4）哪些攻击类别最偏离全局均值，5）类别之间是否存在明显的不平衡或重叠风险。请输出可直接给安全团队看的结论，并尽量用分组均值、中位数、占比和最大差异来表达，避免泛泛而谈。
```

### 1147. D9_k984326_en (domain=D9, difficulty=7)

```
Using subhajournal__iotintrusion__IoT_Intrusion.csv, build a security-analytics review focused mainly on temporal / trend behavior across the sequence of flow observations. I want a concise but rigorous readout that breaks the dataset into 4-6 independent workstreams a small team could do in parallel: (1) overall label trend over the observation order, including whether attack mix shifts early vs late; (2) per-label changes in traffic intensity over time using flow_duration, Duration, Rate, and Srate; (3) period-over-period shifts in protocol / service mix using the protocol and port-like indicator columns (TCP, UDP, HTTP, HTTPS, DNS, Telnet, SMTP, SSH, IRC, DHCP, ARP); (4) flag-pattern evolution over time using the TCP flag/count columns; (5) any monotonic or step-change signals in the numeric burst/size fields like Header_Length, Tot sum, Tot size, Magnitue, Radius, Covariance, Variance, Weight; and (6) a compact anomaly-oriented comparison of early vs late windows to identify which labels and features change the most. Please ground everything in the actual file and columns, and return the findings in a structured analysis summary.
```

### 1148. D9_k984390_en (domain=D9, difficulty=7)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, build a security analytics brief that focuses on segment comparison across categorical groups. I want you to compare rates and means across protocol_type, service, and flag, then surface the biggest gaps between segments that look most operationally meaningful. Break the work into independent tracks so different analysts can work in parallel: one track on protocol_type segment differences, one on service-level differences, one on flag-level differences, one on interaction patterns between protocol_type/service/flag, and one on identifying high-risk vs low-risk network behavior using the numeric rate fields and count/srv_count fields. Please keep the output practical for an incident-response or SOC audience and prioritize the largest segment gaps over generic summary stats.
```

### 1149. D9_k984396_en (domain=D9, difficulty=7)

```
Using sampadab17__network-intrusion-detection__Test_data.csv, do a security analytics review focused mainly on temporal/sequence behavior in the test set. Treat the row order as the observed sequence and analyze how attack-like indicators evolve over time/sequence positions. I need a concise but rigorous summary for operations: identify where the sequence shifts, what protocol/service/flag patterns change before and after those shifts, and which host/network features move the most. Please split the work into independent tracks so it can be handled in parallel: (1) sequence trend and change-point style analysis on the numeric rate/count features across row order, (2) protocol/service/flag composition changes over early vs late portions of the sequence, (3) attack-intensity segmentation using logged_in, serror/rerror rates, and count/srv_count behavior, (4) feature drift comparison for the host-based metrics between the first and second halves, and (5) a short anomaly inventory of the most extreme rows in the sequence with their categorical context. Save the final output as analysis_summary.json and make sure every claim is backed by exact counts/averages from the data.
```

### 1150. D9_k984494_en (domain=D9, difficulty=7)

```
Analyze subhajournal__iotintrusion__IoT_Intrusion.csv for a security-analytics review focused mainly on temporal/trend behavior over the available sequence fields. I need a compact but rigorous assessment of how attack patterns evolve across the dataset, especially changes in flow_duration, Duration, Rate, Srate, Drate, and the packet-flag/count features, and how those trends differ by label. Please structure the work so multiple analysts can work independently: one track should quantify overall time/row-order trend shifts and rate-of-change patterns, another should compare early vs late segments of the dataset, another should examine label-wise temporal concentration and drift, another should inspect correlation changes among traffic-rate features over the sequence, and another should identify any abrupt regime changes using rolling-window summaries. Use the real columns in the file, including label and the numeric traffic features. I want the final output to be suitable for a concise security briefing with clear findings, segment comparisons, and notable anomalies.
```

### 1151. D9_k984503_zh (domain=D9, difficulty=7)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的异常/离群检测排查报告，重点围绕“显式数值规则”来找可疑流量：比如用分位数/IQR 设阈值、识别极端值、稀有类别和规则命中的组合异常。请先按攻击标签和关键协议/标志位做分层，再结合流量时长、速率、包标志计数、以及 HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC/TCP/UDP/DHCP/ARP 等离散特征，找出最异常的样本群体与最可疑字段。我要的是可直接交付给安全团队的结论摘要，不需要建模或画图，但需要清楚说明哪些规则最能区分异常流量，哪些标签更容易出现极端值，以及有哪些稀有协议/组合值得重点人工复核。
```

### 1152. D9_k984534_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全分析的入侵流量复盘，重点围绕“排名与集中度”来展开：我想知道哪些协议、服务、连接标志和流量特征最集中地贡献了样本中的连接记录，以及这些头部类别是否在可疑行为指标上更极端。请把分析拆成若干彼此独立的子任务，分别覆盖：1）协议/服务/flag 的频次排名与集中度（Top-N、累计占比、Pareto）；2）不同协议下关键攻击迹象指标的集中与异常分布；3）Top 服务与 Top flag 组合的占比、以及它们对应的高风险特征画像；4）按 src_bytes、dst_bytes、count、srv_count 等指标做分位排名，识别最“重”的连接群体；5）基于若干二元/比例特征（如 logged_in、is_guest_login、serror_rate、rerror_rate 等）比较头部组与尾部组的差异；6）输出可直接给管理层看的浓缩结论，强调头部集中度、长尾和最值得优先盯防的类别。请尽量给出能落地的结论，并且所有结论都要能从数据里直接复核。
```

### 1153. D9_k984561_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全运营的复杂分析，重点放在数值字段之间的相关性与驱动因素分析：先识别哪些数值特征彼此强相关、哪些指标可能共同上升或下降，再结合连接行为特征判断哪些变量最能解释异常流量模式。请直接围绕现有列分析，不要假设标签列不存在；我更关心可操作的结论，比如：常见协议/服务/flag 组合下，哪些数值指标最容易一起变化，哪些 host 侧与 connection 侧指标高度相关，是否存在明显的“攻击式”行为簇。请输出适合给安全团队的结论、关键相关对、以及可以复核的统计结果。
```

### 1154. D9_k984565_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全分析的分群对比报告，重点围绕“不同类别分组之间的指标差异”展开，帮助我快速找出最可疑的流量段。请直接用数据里的真实列名分析，不要做建模或预测。重点看 class、protocol_type、service、flag 这几个分类维度，以及它们与 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate、dst_host_diff_srv_rate、dst_host_same_src_port_rate、dst_host_srv_diff_host_rate、dst_host_serror_rate、dst_host_srv_serror_rate、dst_host_rerror_rate、dst_host_srv_rerror_rate 等指标之间的关系。请输出一份结构化结论，明确指出各分组的占比、均值/中位数差异、异常占比最高的类别、以及各分类维度下差异最大的细分组。我要的是能直接给安全运营/威胁分析团队看的结果，而不是泛泛描述。
```

### 1155. D9_k984669_en (domain=D9, difficulty=7)

```
Analyze the file sampadab17__network-intrusion-detection__Test_data.csv for a security-analytics review focused mainly on temporal / trend behavior over the available sequence of connection records (treat row order as the sequence since there is no date column). I need a compact but rigorous investigation of how attack-like indicators and traffic patterns evolve over the record sequence, including period-over-period shifts, spikes, and changes in service/protocol mix. Please also connect the trend work to behavior differences in the connection metadata columns like protocol_type, service, flag, src_bytes, dst_bytes, logged_in, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, and the host-based rate features. Break this into independent workstreams that could be handled in parallel, then summarize the findings in one analysis_summary.json deliverable.
```

### 1156. D9_k984676_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Train_data.csv 做一份面向安全分析的多部分深度分析报告，重点围绕“序列/时间趋势”来展开：虽然数据里没有真实日期，但 `duration`、`count`、`srv_count`、`dst_host_count`、`dst_host_srv_count` 等字段可视作连接序列中的行为轨迹，请重点分析不同连接模式在攻击与正常流量中的变化趋势、异常率的阶段性差异、以及高风险协议/服务/标志位在序列上的聚集特征。请把分析拆成彼此独立、便于并行推进的 4-6 个子任务，并最终输出一个 `analysis_summary.json`，里面至少包括：1）总体趋势结论；2）按序列分段/分位数的异常占比变化；3）不同 `protocol_type`、`service`、`flag` 在序列上的风险差异；4）关键数值特征随序列变化的统计摘要；5）对安全运营可落地的监控建议。请务必使用文件中的真实列名，不要虚构任何字段或数值。
```

### 1157. D9_k984681_zh (domain=D9, difficulty=7)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一次面向安全运营的流量分布与集中度分析，重点看“谁占了大头、头部有多集中、是否存在明显长尾”。请围绕 protocol_type、service、flag 以及关键数值字段 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、rerror_rate、same_srv_rate、diff_srv_rate、dst_host_count、dst_host_srv_count、dst_host_same_srv_rate 等列展开，给出可落地的安全解读。希望你把工作拆成几个互相独立的分析轨道：1）协议/服务/标志位的频率排名与 Top-N 占比；2）关键数值特征的头部样本与贡献集中度（例如 src_bytes、dst_bytes、duration 的 Pareto/Top 分位）；3）按 service 或 protocol_type 分组后对 count、srv_count、错误率的集中度比较；4）识别最常见组合模式（protocol_type + service + flag）及其覆盖率；5）检查是否存在少数类别主导的高风险模式，并结合 seror/rerror 及 same/diff_srv_rate 做解释；6）输出一个适合汇报的简短结论，说明最值得优先关注的头部类别与原因。请给出结构化结果，尽量用表格/JSON 风格总结，并明确每个结论对应的数据支撑。
```

### 1158. D9_k984799_zh (domain=D9, difficulty=7)

```
请基于文件 piyushrumao__malware-executable-detection__uci_malware_detection.csv 做一份面向安全分析的复杂数据分析报告，重点围绕“相关性与驱动因素分析”：哪些数值特征彼此同向/反向变化、哪些字段之间的相关性最强、哪些特征组合可能在区分 Label 上最有信息量。数据里有 Label 和大量数值特征 F_1 到 F_433（以实际文件为准）。我需要你把分析拆成几个相互独立的轨道并并行推进，最后输出一个可交付的 summary JSON。请至少覆盖：1）整体数据质量与字段概览；2）Label 分布与按 Label 的特征差异；3）全局相关性矩阵与 Top 正/负相关特征对；4）围绕若干关键字段做局部驱动分析（例如与最强相关特征、与 Label 差异最大的特征）；5）特征冗余/共线性风险提示；6）把能直接支持安全检测解释性的发现整理成简明结论。请注意不要做建模、不要画图、不要随机抽样，所有结论都必须来自可复现的确定性统计。最终请给我一个结构化结果，便于我再交给安全团队复核。
```

### 1159. D9_k984858_zh (domain=D9, difficulty=7)

```
请基于文件 nkongolo__ugransome-dataset__final(2).csv 做一份面向安全分析的多部分研究，重点围绕时间序列/趋势变化来展开。数据里有 Time、Protcol、Flag、Family、Clusters、SeddAddress、ExpAddress、BTC、USD、Netflow_Bytes、IPaddress、Threats、Port、Prediction 等字段。请帮我从“随时间变化的攻击/流量特征”这个主线出发，拆成几个可以并行推进的分析轨道，最后输出一份结构化结论，最好能覆盖：1）按 Time 的威胁与预测标签趋势；2）不同协议/Flag 在时间上的变化与异常峰值；3）主要恶意 Family 的时间分布与对应指标变化；4）流量/金额类指标（BTC、USD、Netflow_Bytes）在不同时间段的变化；5）不同 Threats、Port、IPaddress 的时间活跃度与集中度；6）把时间趋势和 Clusters/SeddAddress/ExpAddress 结合，看是否存在阶段性聚集或迁移模式。请先给我可执行的分析框架和结论方向，再给出关键统计结果。
```

### 1160. D9_k984908_en (domain=D9, difficulty=7)

```
Analyze the dataset in subhajournal__iotintrusion__IoT_Intrusion.csv for security analytics, with the main focus on segment comparison across categorical groups. I need a practical breakdown that compares rates, means, and class composition across segments so we can see which traffic families differ most. Please organize the work into 4-6 independent tracks so a sub-agent team can split it up cleanly: (1) label distribution and class imbalance, (2) protocol/transport segment comparisons using columns like Protocol Type, TCP, UDP, HTTP, HTTPS, DNS, Telnet, SMTP, SSH, IRC, DHCP, and ARP, (3) flag and count behavior comparisons using fin_flag_number, syn_flag_number, rst_flag_number, psh_flag_number, ack_flag_number, ece_flag_number, cwr_flag_number plus the corresponding *_count columns, (4) traffic-intensity comparisons using flow_duration, Duration, Rate, Srate, Drate, Header_Length, and Tot size, (5) identify the biggest mean gaps between attack labels for the most informative numeric features, and (6) a compact summary of the strongest segment-level separation patterns that a defender could use to prioritize rule tuning or monitoring.
```

### 1161. D9_k984922_zh (domain=D9, difficulty=7)

```
请基于文件 mryanm__luflow-network-intrusion-detection-data-set__2020.06.22.csv 做一份面向安全分析的分组对比报告，重点围绕不同类别之间的指标差异（均值、占比、最大差距）来找出可疑模式。请直接使用这些真实字段：avg_ipt、bytes_in、bytes_out、dest_ip、dest_port、entropy、num_pkts_out、num_pkts_in、proto、src_ip、src_port、time_end、time_start、total_entropy、label、duration。我要你把分析拆成几个彼此独立的小任务，最后合并成一份简洁结论，最好能指出 benign 和 malicious 在哪些特征上差异最大、哪些端口/协议/地址段最值得关注、以及是否存在明显的通信方向或持续时间模式。请同时给出可复核的统计结果。
```

### 1162. D9_k984941_zh (domain=D9, difficulty=7)

```
请基于文件 danielfernandon__web-page-phishing-dataset__web-page-phishing.csv 做一次面向安全分析的深度数据分析，重点围绕“分布与阈值分层（业务阈值以上/以下、分位数分桶、占比结构）”展开。数据里只有这些列：url_length、n_dots、n_hypens、n_underline、n_slash、n_questionmark、n_equal、n_at、n_and、n_exclamation、n_space、n_tilde、n_comma、n_plus、n_asterisk、n_hastag、n_dollar、n_percent、n_redirection、phishing。我要你把分析拆成几个彼此独立的轨道，方便并行给不同子代理分别做：1）先按 phishing 标签看各核心特征的分布差异，重点做业务阈值分层（比如 URL 长度、点号数、斜杠数、下划线数、问号数、等号数、百分号数等），输出各阈值以上/以下的样本占比；2）再做分位数分桶分析，找出哪些桶里钓鱼样本占比最高，以及各桶样本数结构；3）做符号类型组合的混合结构分析，关注常见“多符号共现”模式及其在钓鱼/非钓鱼中的占比；4）检查强异常 URL 的长尾情况，识别极端值对整体分布的贡献；5）做标签条件下的统计摘要与相关性对比，找出哪些变量与 phishing 的单调关联最强。最终请给我一份简洁的 analysis_summary.json 风格结果，重点是阈值 cohorts、分位数 cohorts、mix shares、长尾和标签差异，不要训练模型，不要画图。
```

### 1163. D9_k985026_zh (domain=D9, difficulty=7)

```
请基于文件 mryanm__luflow-network-intrusion-detection-data-set__2020.06.22.csv 做一份面向安全运营的时序分析，重点围绕 time_start、time_end、duration 以及按 proto / dest_port / label 划分的流量趋势变化，帮我判断哪些时间段、哪些端口、哪些协议的行为最异常，以及这些变化和 malicious 标签之间的关系。请直接输出一份可交付的分析摘要，最好能支持我快速定位需要进一步排查的时段和端口范围。数据列包括 avg_ipt, bytes_in, bytes_out, dest_ip, dest_port, entropy, num_pkts_out, num_pkts_in, proto, src_ip, src_port, time_end, time_start, total_entropy, label, duration。
```

### 1164. D11_k984256_zh (domain=D11, difficulty=8)

```
请基于文件 itssuru__loan-data__loan_data.csv 做一份面向信贷风控与放款策略的深度分析，重点围绕“按序列/时间趋势”展开：虽然数据里没有明确日期列，但请把贷款利率 int.rate 视为风险环境的序列分组基准，分析不同利率区间下的违约/逾期表现是否存在单调变化、拐点或阶段性波动，并结合 credit.policy、fico、dti、inq.last.6mths、revol.util、purpose 等字段解释原因。我要的是可直接给管理层看的结论，最好能输出一份 analysis_summary.json。请把工作拆成互相独立的 4-6 条分析线：1）按利率分箱的违约趋势与环比变化；2）不同 purpose 在利率序列上的风险迁移；3）信用评分 fico 与利率/违约率的联动；4）credit.policy 批准与不批准样本在各利率阶段的表现差异；5）高查询次数、较高债务负担、较高循环额度利用率人群在利率序列中的违约放大效应；6）如有必要，再补充对 days.with.cr.line 或 revol.bal 的稳定性分析。请输出可执行的分组、对比和结论摘要，不要写成泛泛而谈。
```

### 1165. D12_g981822_zh (domain=D12, difficulty=8)

```
请用 people_training_enablement_q1_data.xlsx、people_training_enablement_q2_data.xlsx、people_training_enablement_q3_data.xlsx 做一份合并简报，重点看招聘评分、绩效校准、技能矩阵和入职缺口。我要一个汇总文件，能直接给 HRBP 和培训负责人看，里面把跨源匹配情况、主要不一致原因、各团队的技能覆盖缺口、以及需要优先补训的人群都收好。
```

### 1166. D12_k984165_zh (domain=D12, difficulty=8)

```
请基于文件 pavansubhasht__ibm-hr-analytics-attrition-dataset__WA_Fn-UseC_-HR-Employee-Attrition.csv 做一份面向管理层的离职趋势分析，重点围绕“随时间/序列变化”的角度展开：把 YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager、TotalWorkingYears、NumCompaniesWorked 这些序列字段当作员工职业阶段或任职过程的时间线，分析离职风险如何在不同阶段变化，并结合 Attrition、OverTime、BusinessTravel、Department、JobRole、MaritalStatus、Age、MonthlyIncome、JobSatisfaction、EnvironmentSatisfaction、WorkLifeBalance、StockOptionLevel 等字段解释原因。请输出一份可直接给 HR 负责人看的结论摘要，并拆成 4-6 个可并行的分析轨道：1) 任职年限/晋升滞后与离职的阶段性变化；2) 关键人群（部门、岗位、婚姻状态、加班）在不同任职阶段的离职趋势；3) 近似“时间序列”的员工职业路径分层对比（如 TotalWorkingYears、NumCompaniesWorked 分组）；4) 满意度与薪酬在各阶段的变化及其与离职的关系；5) 结合年龄和司龄的交叉趋势，识别最脆弱的人群；6) 给出可执行的人才保留建议。请注意，这是一份真实数据分析，不要虚构任何字段或数值，只基于文件中的实际列进行分析。
```

### 1167. D12_k985163_zh (domain=D12, difficulty=8)

```
请基于文件 thedevastator__jobs-dataset-from-glassdoor__glassdoor_jobs.csv 做一份面向人力/招聘分析的深度诊断，重点围绕“数值字段之间的相关性与驱动因素”展开，帮我找出哪些特征最可能一起变化、哪些字段最强相关、以及不同公司/岗位画像下这些关系是否有明显差异。请直接使用现有列：Rating、Founded、Salary Estimate、Size、Revenue、Sector、Industry、Location、Headquarters、Type of ownership、Competitors、Job Title、Job Description、Company Name。这个任务需要拆成多个彼此独立的分析轨道，便于并行推进：1）薪资估算与公司评分/成立年份之间的相关性和方向性；2）公司规模、营收、成立年份与评分的关联强弱；3）不同 Sector / Industry 下相关性的分层对比；4）高薪岗位与岗位标题关键词、地点的联合特征；5）竞争对手数量、公司类型与评分/营收的关系；6）缺失值和数据质量对相关性结论的影响。请最终输出可供管理层快速阅读的结论摘要，同时保留可复算的统计结果。所有结果尽量用四舍五入到 2 位小数的相关系数、计数或均值来呈现。
```

### 1168. D13_k984995_zh (domain=D13, difficulty=8)

```
请基于文件 yasserh__amazon-product-reviews-dataset__7817_1.csv 做一份面向产品分析的多维驱动分析，重点放在“哪些数值字段彼此相关、哪些字段是核心驱动因子、以及这些关联在不同产品/评价维度上是否一致”。我需要你先把数据做一次严谨的质量检查，再围绕相关性与驱动关系拆成若干独立分析轨道，最后汇总成可给业务看的结论。请重点使用这些真实字段：reviews.rating、reviews.numHelpful、ean、upc、sizes、reviews.doRecommend，以及 prices（注意它是字符串/JSON文本，必要时先提取可用数值）。请不要臆测字段含义，所有结论都必须来自数据本身。输出里请至少覆盖：1）数据完整性与有效样本规模；2）数值字段之间的相关性矩阵与最强正/负相关对；3）评分与 helpfulness、recommend 的驱动关系；4）价格相关指标与评分/推荐的关系；5）按品牌或类别分组后的差异；6）识别异常或极端值对相关性的影响。请把结论写得像真实分析给业务负责人看的简报。需要能拆给 4-6 个独立子任务并行做。
```

### 1169. D3_k982485_zh (domain=D3, difficulty=8)

```
请基于文件 open-source-sports__professional-hockey-database__Scoring.csv 做一份面向业务汇报的分层分析，重点围绕时间序列/趋势变化来展开：按 year 观察球员进攻产出、罚时和特殊球队表现的长期变化，并识别赛季之间的结构性变化、位置差异以及季后赛表现的演进。请直接使用表里的真实字段（如 playerID、year、stint、tmID、lgID、pos、GP、G、A、Pts、PIM、+/−、PPG、PPA、SHG、SHA、GWG、GTG、SOG、PostGP、PostG、PostA、PostPts、PostPIM、Post+/−、PostPPG、PostPPA、PostSHG、PostSHA、PostGWG）完成分析，不要编造口径。请把工作拆成多个相互独立的分析轨道：1）按赛季的整体趋势；2）按位置（pos）的趋势对比；3）高产球员/高罚时球员的年代变化；4）常规赛与季后赛的联动；5）赛季间增速或增幅最大的年份切片；6）数据完整性与缺失模式对趋势分析的影响。最后输出一份适合管理层阅读的结论摘要，并给出可复核的关键数字。
```

### 1170. D3_k983812_zh (domain=D3, difficulty=8)

```
请基于文件 mohamedsaqibshouqi__2023-2024-nba-player-stats-playoffs__NBA Stats 202324 All Stats  NBA Player Props Tool (4).csv 做一份面向 BI/分析汇报的深入分析，重点围绕“相关性与驱动因素分析”：先找出各数值字段之间哪些指标最强正相关/负相关，再识别哪些统计维度最能解释得分、效率、球权和综合产出。请结合真实字段（如 MPG、USG%、TO%、FTA、FT%、2PA、2P%、3PA、3P%、eFG%、TS%、PPG、RPG、APG、SPG、BPG、TPG、P+R、P+A、P+R+A、VI、ORtg、DRtg）输出可落地结论，并说明不同位置/球队中这些关系是否存在差异。请拆成独立分析轨道并分别产出可核查结果，不要只给总览。
```

### 1171. D3_k984396_zh (domain=D3, difficulty=8)

```
请基于文件 ruthgn__bank-marketing-data-set__bank-direct-marketing-campaigns.csv 做一份面向业务决策的多维分析，重点围绕时间/序列维度展开。请把分析拆成多个彼此独立的子任务，方便不同分析同学并行完成。核心要回答：不同月份、星期几、以及历史触达序列（如 campaign、pdays、previous、poutcome）变化时，客户转化率 y 的趋势、拐点和组合差异是什么；同时结合 age、job、contact、education、housing、loan、default、以及宏观变量 emp.var.rate / cons.price.idx / cons.conf.idx / euribor3m / nr.employed 做业务解释。请输出一份可直接给管理层的分析摘要，说明哪些时间段/序列特征更容易促成转化，哪些组合需要重点优化触达策略，并给出可以落地的行动建议。
```

### 1172. D4_k984225_zh (domain=D4, difficulty=8)

```
请基于文件 stackoverflow__stack-overflow-2023-developers-survey__survey_results_public.csv 做一份面向内容/编辑选题的分析，重点放在“相关性与驱动因素”上：哪些数值字段、分组变量与收入/经验/工作方式更相关，哪些组合更值得做内容专题。请直接围绕这份数据里的真实列来做，不要泛泛而谈，最好能把结果转成可执行的选题建议。请至少覆盖这些方面：1）薪资与经验/工作形态/地区之间的相关性和分层差异；2）编程语言、数据库、云平台、Web 框架与收入的关联强弱；3）学习方式、学历、在线学习/课程认证与经验或收入的关系；4）AI 工具使用、职业技术栈与收入/经验的关联；5）从高相关字段里筛出最值得内容团队深挖的 top 关联组合，并说明这些组合为什么适合做专题。输出时请尽量给出可复用的结论表述，方便编辑直接拿去定选题。
```

### 1173. D4_k984361_zh (domain=D4, difficulty=8)

```
请基于文件 stackoverflow__stack-overflow-2023-developers-survey__survey_results_public.csv 做一份面向内容/编辑分析的调研报告，重点围绕“时间/序列变化”来分析开发者内容消费与工具使用的变化趋势。请结合真实列字段（如 YearsCode、YearsCodePro、LearnCodeOnline、LearnCodeCoursesCert、SOVisitFreq、SOAccount、SOPartFreq、SOComm、AISelect、AISent、AIAcc、AIBen、AIDevHaveWorkedWith、AIDevWantToWorkWith、AISearchHaveWorkedWith、AISearchWantToWorkWith、TimeSearching、TimeAnswering、SurveyLength、SurveyEase、Country、EdLevel、MainBranch、Employment、RemoteWork、DevType、LanguageHaveWorkedWith、LanguageWantToWorkWith 等）做一份能直接支持内容选题和编辑排期决策的分析。请把任务拆成 4-6 个彼此独立的分析轨道：例如按经验阶段的内容偏好演变、AI 工具采用与态度变化、学习渠道/课程证书随职业阶段的变化、社区参与频率的序列差异、搜索/答疑时间与内容需求关系、以及不同国家/岗位/远程工作状态下的趋势差异。最终输出需要能回答：哪些内容主题正在上升、哪些人群最值得优先触达、以及哪些指标可作为后续月度追踪基线。
```

### 1174. D5_g203_en (domain=D5, difficulty=8)

```
I need you to do a multi-track audit on the project files in the inputs/ folder. Use these files: app_core_cache_utils.py, app_api_handlers.py, config_production.py, requirements.txt, audit_scope.md, test_log.jsonl, event_counts.xlsx, runtime_audit.log, and audit.sqlite. Produce three reports: audit_summary.json, findings_by_track.md, and validation_plan.csv. The audit should cover static code review, security/config review, dependency audit, test triage, large-log audit, event-count audit, and SQLite health check. Then synthesize a prioritized fix plan with the top 5 items using the labels code-hardening, config-lockdown, dependency-pinning, test-stabilization, runtime-remediation, and db-reliability.
```

### 1175. D5_g434_en (domain=D5, difficulty=8)

```
We’re auditing a small multi‑module Python codebase and need a consolidated picture from all sources. I’ve got these files to work with: inputs/parser.py, inputs/auth.py, inputs/config.json, inputs/runbook.md, inputs/pytest.log, inputs/junit.xml, and inputs/audit.sqlite.

Run four independent analysis tracks: static code review, security/config review, test triage, and dependency/risk audit. Then synthesize everything into three compact deliverables:

- one JSON executive summary
- one CSV findings matrix
- one Markdown validation plan

The final report should reconcile the four tracks into a prioritized fix‑and‑validation plan. Use the usual closed‑set audit patterns for each track (don’t mark anything outside those patterns). Keep each report file small – no per‑record dumps.
```

### 1176. D5_g980783_zh (domain=D5, difficulty=8)

```
我需要你帮我做一次代码库和日志的联合审计，目标是把这几个文件 static_audit.xlsx、config_audit.xlsx、test_logs.xlsx、dependencies.xlsx、issue_log.xlsx 串起来，整理成一份紧凑的总报告，给我明确的修复优先级和验证结论。
```

### 1177. D5_g981430_zh (domain=D5, difficulty=8)

```
请审计 inputs/api_gateway.py、inputs/report_utils.py、inputs/job_runner.py、inputs/data_transform.py，再结合 inputs/runtime_audit_log.csv、inputs/test_results.xlsx 和 inputs/config_audit.xlsx 做一次完整的代码+日志+配置联审。我需要你输出一份决策简报，按风险和影响排序，说明先改哪些点、为什么，以及验证时要盯哪些指标。
```

### 1178. D5_g981637_zh (domain=D5, difficulty=8)

```
我需要你把这套小项目做一次完整的代码库与日志联查审计，输入是 inputs/modules.xlsx、inputs/code_audit.xlsx、inputs/test_runs.log、inputs/dependencies.json 和 inputs/releases.sql。请把代码风险、测试失败模式、依赖与生产配置问题，还有它们之间的交叉影响合并成一份简洁的结论报告，最后给出优先级排序和一个可执行的修复与验证计划。
```

### 1179. D5_g982475_zh (domain=D5, difficulty=8)

```
请基于 inputs/project_audit.xlsx、inputs/service_logs.txt、inputs/dependency_snapshot.json 做一次 代码库/日志联合审计，输出一个汇总版报告文件 audit_report.xlsx。
我需要你把模块代码审查、日志故障排查、测试失败归因、配置与依赖检查合并成一份结论，标出问题清单、影响面和修复优先级。
```

### 1180. D5_g983215_en (domain=D5, difficulty=8)

```
You are auditing a small Python service using three spreadsheets: codebase_audit.xlsx, runtime_logs.xlsx, and qa_and_config.xlsx.

Your job is to synthesize findings across code, logs, tests, and configuration.

Deliverables:
1. A concise risk summary identifying the highest-priority issues and which modules/configs are implicated.
2. A table or bullet list of concrete evidence with counts/examples drawn from the spreadsheets.
3. A short remediation plan sorted by priority.

Use the provided files only. Do not invent missing data.
```

### 1181. D5_g983457_zh (domain=D5, difficulty=8)

```
请基于 inputs/module_inventory.xlsx、inputs/app_runtime.log、inputs/test_results.xlsx 以及 inputs/project/app/ 下的代码文件，做一次合并审计并输出一个完整的结论文件。我要你把四条并行线一起收敛：静态代码审查、风险/安全审查、测试失败归因、以及配置/依赖核查；最后给出一个统一的修复优先级和验证计划。输出只要一个汇总报告文件，内容要能直接给研发和测试一起用，不要拆成多个报告。
```

### 1182. D6_g282_zh (domain=D6, difficulty=8)

```
基于 `inputs/agreements.csv`、`inputs/contract_clauses.xlsx`、`inputs/invoices.xlsx`、`inputs/receipts.xlsx`、`inputs/operational_events.xlsx`、`inputs/termination_notices.xlsx` 和 `inputs/memos.xlsx`，帮我做一份中文综合分析简报，输出 `findings.md` 和一张证据表 `evidence_table.csv`。需要把多份合同、政策、发票、收款、运营表格和备忘录整合起来，得出供业务负责人阅读的综合结论，同时处理跨来源的冲突、重复、异常值和口径问题。具体分析要涵盖合同主数据、条款冲突、发票与收款对账、运营事件、终止通知合规性、跨源联动，并标出至少3个需要业务复核的异常点。结果要紧凑，不是原始数据导出。
```

### 1183. D6_g364_en (domain=D6, difficulty=8)

```
Please reconcile the audit data from the files in inputs/: contracts_master.xlsx, policy_exceptions.xlsx, clause_extract_log.xlsx, reference_notes.md, and contracts_review.sqlite. Output a JSON summary with metrics and top/bottom lists, a CSV of contract-level flags for matched contracts, and a Markdown report with narrative bullets and an anomalies appendix.
```

### 1184. D6_g980801_zh (domain=D6, difficulty=8)

```
我需要你把这四个文件——`clause_extraction.xlsx`、`policy_register.xlsx`、`case_reviews.xlsx`、`review_txns.xlsx`——合成一份可直接给管理层看的简报，重点是把合同条款、政策登记、案例问答和交易记录串起来，顺手把需要人工复核的异常也标出来。
```

### 1185. D7_g351_zh (domain=D7, difficulty=8)

```
我需要你基于这次事故的调查数据，写成一份可以直接发给管理层的决策简报。数据在 inputs/ 目录下，包括 incidents.csv、tickets.xlsx、api_calls.xlsx、comms_log.xlsx、ticket_events.xlsx、ops_config.csv 和 ops_bundle.sqlite。这些文件记录了事故清单、工单流转、API 调用日志、沟通记录、工单事件时间线和当前运营配置。数据里混了一些异常值、重复记录和时间顺序问题，你处理时注意。

目标不是出流水账，而是先重建事故影响和时间线，再核对 Owner 和沟通覆盖情况，最后按优先级给出处置建议。把关键数值作为依据，最终只输出一个简短文件 decision_brief.md，内容面向业务。如果数据之间有冲突，在简报里说明你采用了什么规则（比如重复行怎么处理、异常值怎么剔除、时间边界怎么定）。
```

### 1186. D7_g361_zh (domain=D7, difficulty=8)

```
我需要你根据以下文件做一次事故调查和决策简报：

- `inputs/alerts.csv`
- `inputs/config_history.xlsx`
- `inputs/api_gateway_logs.ndjson`
- `inputs/tickets.csv`
- `inputs/postmortem_notes.csv`
- `inputs/ops_workflow.db`

背景是5月21日上午payments-api在us-east-1出现明显失败，请你把告警、配置变更、日志、工单和沟通这五条线串起来，输出一个文件 `decision_brief.md`，给出排序后的决策建议，并引用关键数字支持结论。日志文件较大且包含少量异常记录，注意只分析相关部分。
```

### 1187. D7_g980523_en (domain=D7, difficulty=8)

```
I need a decision brief for the incident review. Use incident_ops_master.xlsx together with workflow_notes.csv and ticket_index.json to reconstruct what happened, assess customer impact, and decide where we should focus next.
- Reconcile the duplicate incident and ticket records, then summarize the clean incident picture.
- Rebuild the timeline of detection, triage, mitigation, resolution, and comms.
- Flag the main owner/comms gaps and the highest-risk configuration issues.
- End with a ranked recommendation on which integration area to prioritize next, with the key numbers cited.
```

### 1188. D7_g980992_zh (domain=D7, difficulty=8)

```
我这边要做一次事故复盘和对外说明准备，请帮我看一下 inputs/incidents_workbook.xlsx 和 inputs/comms_log.docx，整理成一个决策简报，最后给我一份 recommendation.json。我要的是能直接支持我判断这次事件怎么定责、怎么分优先级和怎么对外沟通的结果，最好把关键数字都带上。
```

### 1189. D7_k983505_zh (domain=D7, difficulty=8)

```
请基于文件 kanchana1990__global-superpower-and-geopolitical-risk-nexus__global_superpower_and_geopolitical_risk_nexus.csv 做一份面向 IT 运营 / 日志与事件分析 的多部分分析，重点围绕“排名与集中度（Top-N、头部占比、Pareto）”展开。请把数据里的主题词指标（如 BRICS_Views、Cyberwarfare_Views、Economic_sanctions_Views、Inflation_Views、NATO_Views、Nuclear_weapon_Views、OPEC_Views、Recession_Views、Semiconductor_Views、South_China_Sea_Views、Taiwan_Strait_Views、United_States_Armed_Forces_Views、Vladimir_Putin_Views、World_War_III_Views、Xi_Jinping_Views）当作事件/告警热度，把对应的 *_7D_Momentum 和 *_30D_Shock 当作变化与冲击信号；同时结合市场/资产列（如 000001.SS_Close、BA_Close、CL=F_Close、GC=F_Close、GD_Close、LMT_Close、NOC_Close、RTX_Close、URA_Close、ZW=F_Close、^GSPC_Close、^N225_Close、^FTSE_Close 等）做联动分析。请输出一份结构清晰的 analysis_summary.json，至少拆成 4-6 个彼此独立的分析轨道，例如：1) 主题词热度 Top-N 与集中度（Top 3/5/10 占比、HHI/帕累托），2) 时间切片上的头部主题更替与稳定性，3) 30D shock 最大的主题及其是否也在 views 中占优，4) 视图热度与动量/冲击的相关性排序，5) 资产端日线收盘价或波动的 Top-N 集中度，6) 主题词与资产之间的联动/同向关系排行。请明确指出哪些主题或资产长期占据大部分关注度，哪些是尾部但偶发冲击强，哪些更像系统性风险信号。所有结论都必须严格基于数据，不要臆测。
```

### 1190. D7_k983752_zh (domain=D7, difficulty=8)

```
请基于文件 mikhailhushchyn__dss-performance__ssd_random.csv 做一份面向 IT 运维/日志与事件分析的复杂诊断报告。重点围绕“时间/序列趋势”来分析：虽然没有显式时间戳，但可以把 id 作为采集批次/事件序列标识，先按 id 的自然顺序或按文件出现顺序做序列分析，再结合 block_size、n_jobs、iodepth、read_fraction、raid、device_type、n_disks、io_type、load_type、offset 等维度，找出 iops 与 lat 的阶段性变化、环比/前后窗口变化、不同配置在序列上的漂移，以及异常尖峰/低谷。请拆成几个互相独立的分析轨道并分别给结论：1) 整体 iops/lat 的序列趋势与变化率；2) 不同 block_size 和 iodepth 组合下的趋势对比；3) read_fraction、io_type、load_type 对性能时序的影响；4) raid、n_disks、device_type 的分组趋势与异常点；5) 识别性能突变最明显的前后片段并解释可能关联配置；6) 给出可操作的运维建议，指出哪些配置更容易引发延迟抖动或吞吐回落。请输出适合内部复盘的结构化结果，便于我直接转给团队。
```

### 1191. D7_k984403_zh (domain=D7, difficulty=8)

```
请基于文件 amineipad__telemetrydataset__balanced_augmented_dataset.csv 做一份面向 IT 运维 / 日志与事件分析的综合分析，重点围绕“按序列/时间趋势变化”来展开：虽然数据里没有显式时间戳，但可以把 segment 当作事件序列索引，把 train、sampling、duration、len 看作不同采样与窗口设置下的观测。请重点回答：1）异常率是否在 segment 序列上呈现阶段性上升/下降，是否存在明显的前后期差异；2）不同 sampling、duration、len 分层下，异常率与统计特征（mean、var、std、kurtosis、skew、n_peaks、diff_var、diff2_var、gaps_squared、len_weighted、var_div_duration、var_div_len）之间的关系是否随序列变化而变化；3）异常样本与正常样本在峰值、差分波动和分布形态上有哪些稳定差异；4）哪些 channel 更容易出现异常，以及这些 channel 的异常是否集中在特定 segment 区间；5）train 与非 train 数据在上述趋势上是否存在系统性偏移。请把分析拆成多个相互独立的子任务，便于并行处理，并最终输出可复核的结论、关键统计表和需要重点关注的风险段。请直接使用数据文件中真实列名，不要假设有任何额外字段。
```

### 1192. D8_g1217_en (domain=D8, difficulty=8)

```
I need you to audit the knowledge base using `kb_articles.csv`, `taxonomy.json`, and `expert_validations.xlsx`, then compile a prioritized remediation plan into a single JSON file named `audit_recommendation.json`. Cover staleness, gap analysis, quality/consistency, and cross-source reconciliation, and include a summary with key metrics plus ranked recommendations.
```

### 1193. D8_k982118_zh (domain=D8, difficulty=8)

```
请基于文件 tobiasbueck__multilingual-customer-support-tickets__dataset-tickets-multi-lang-4-20k.csv 做一份面向知识库/支持工单分析的深度诊断，重点围绕“相关性与驱动因素”展开：哪些字段之间的数值关系最强、哪些类别最容易一起出现、哪些标签/队列/优先级与结果更相关。请结合真实列 subject、body、answer、type、queue、priority、language、tag_1 到 tag_8，输出适合管理层直接看的结论，并尽量用可复核的统计结果支撑。我要你把任务拆成多个彼此独立的分析轨道，方便不同子代理并行处理；其中至少一条轨道专门做相关性矩阵与高关联对，至少一条轨道做标签/队列/优先级之间的联动，至少一条轨道做语言维度差异，至少一条轨道做文本长度或字段缺失对结果的驱动分析。请注意只基于这份真实数据，不要编造任何数值。最后给我一份结构化结论摘要，说明哪些因素最值得优化，以及可能的运营含义。
```

### 1194. D8_k984156_zh (domain=D8, difficulty=8)

```
请基于文件 mirzayasirabdullah07__customer-support-tickets-dataset-200k-records__customer_support_tickets_200k.csv 做一份面向知识/客服工单分析的深度结论，重点围绕“排名与集中度”（例如 Top-N、头部占比、Pareto 80/20）来判断资源应该优先投向哪里。请务必结合真实字段：category、product、priority、channel、region、customer_segment、status、escalated、sla_breached、customer_satisfaction_score、first_response_time_hours、resolution_time_hours、issue_complexity_score、customer_tenure_months、previous_tickets、subscription_type、customer_age、customer_gender、language、preferred_contact_time、operating_system、browser、payment_method 等。希望你拆成 4-6 条彼此独立的分析线并行推进：1）工单量/复杂度/升级风险的头部集中；2）不同 category/product 的 Top-N 与贡献占比；3）高优先级与 SLA 违约的集中度；4）按 region/channel/customer_segment 的资源压力与差异；5）客户满意度、响应/解决时长与集中度之间的关系；6）输出可以直接用于管理层汇报的结论和优先级建议。请最后给我一个适合落地的分析摘要文件结构建议（analysis_summary.json）与可复核的关键统计结果。
```

### 1195. D8_k984784_zh (domain=D8, difficulty=8)

```
请基于文件 danofer__texas-government-salaries__texas_salaries.csv 做一份面向“知识/支持工单分析”的数据质量审计与使用可行性评估，重点围绕数据质量问题展开：先核查缺失值、空字符串、问号/占位符、重复记录、数值范围异常、类别字段不一致，以及关键字段（如 AGY、AGENCY NAME、CLASS CODE、CLASS TITLE、ETHNICITY、GENDER、STATUS、EMPLOY DATE、HRLY RATE、HRS PER WK、MONTHLY、ANNUAL、STATE NUMBER、duplicated、multiple_full_time_jobs、combined_multiple_jobs、summed_annual_salary、hide_from_search）的完整性和一致性；再从支持工单分析的角度，判断哪些字段可用于工单分群、优先级识别、员工信息匹配、薪酬核验和异常案例排查。请把结果拆成多个独立分析轨道：字段级质量、行级异常、重复/冲突记录、类别标准化、薪酬与工时合理性、以及对支持工单场景的可用性建议。最终给我一个可以直接交给业务方的审计摘要。
```

### 1196. D9_g117_en (domain=D9, difficulty=8)

```
Use `inputs/assets.csv`, `inputs/scanner_findings.xlsx`, `inputs/appsec_reviews.xlsx`, `inputs/exceptions.xlsx`, and `inputs/asset_control_map.sqlite` to produce 2–3 compact report files (JSON summary, CSV top‑10 urgent table, MD notes) for executive triage. This is a unified risk rollup across scanner findings, appsec reviews, and exceptions—not a per‑finding register. Apply our standard severity mapping from CVSS (Critical ≥9.0, High 7.0–<9.0, Medium 4.0–<7.0, Low <4.0; exclude invalid scores), closed status sets, and date handling (YYYY‑MM‑DD; current date fixed at 2025‑06‑01). Join on asset_id; flag unmatched assets. Dedup by (asset_id, cve_id, source_table) keeping latest valid date. Use the pinned SLA‑breach rule (Critical/High, non‑terminal status, past due or no date) and the weighted risk score formula. Deliver the 10 highest‑risk unified records sorted by risk score and severity, plus aggregate counts (total records, severity buckets, SLA breaches, unmatched assets, invalid statuses, distinct assets/CVEs, top‑5 SLA‑breached assets, exception decisions). Keep everything internally consistent and compact.
```

### 1197. D9_g982054_zh (domain=D9, difficulty=8)

```
我需要你基于这几个输入文件做一次漏洞处置决策简报：inputs/vulnerability_findings.xlsx、inputs/asset_inventory.xlsx、inputs/control_mapping.xlsx 和 inputs/risk_exception_memo.pdf。请把四个来源交叉起来看，先把重复发现按资产与CVE组合去重，再按严重性、SLA、资产关键性和审批例外做汇总，最后输出一个简短的决策文件，告诉我应该优先推进哪些资产、哪些漏洞类别最急、以及当前风险例外是否已经超出可接受范围。我只要一个精简的决策简报，不要逐条漏洞清单。请把结论里必须出现的内容写清楚：按 Critical/High/Medium/Low 的数量汇总，总数，SLA 逾期数量，正式例外数量，风险最高的前 10 个资产排序表，以及需要重点盯防的少量资产 ID。
```

### 1198. D9_k982520_zh (domain=D9, difficulty=8)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的多部分深度分析，重点围绕时间/序列趋势来展开（把 flow_duration、Duration、Rate、Srate、Drate 以及各类计数/标志位视为序列中的变化特征，做环比/阶段性变化、趋势分层、突变与异常模式分析）。我希望你把结果整理成 analysis_summary.json，重点回答：不同攻击标签在时长与速率上的变化规律是什么，哪些攻击更像突发型/持续型流量，哪些协议/端口与速率变化更相关，哪些特征组合最能区分不同攻击的演化阶段，以及各标签在前后序列阶段的分布是否显著不同。请拆成多个互相独立的分析轨道，方便并行处理；不要做建模预测，先做严谨的描述统计、分组对比和趋势切片。
```

### 1199. D9_k982968_zh (domain=D9, difficulty=8)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全运营的多阶段分析报告，重点围绕“序列/趋势变化”来判断网络流量是否存在逐步升级的攻击迹象。请把数据按记录顺序视为时间序列（该文件没有显式时间戳，就按行号/窗口顺序分析），重点比较前后窗口、相邻分段和速率变化，识别可疑的阶段性跃迁、协议/服务/标志位的结构变化，以及典型入侵信号在序列中的漂移。请结合真实列名（如 duration、protocol_type、service、flag、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate、dst_host_* 等）输出可执行的分析结论，并在结论里明确指出哪些变化更像扫描、拒绝服务、探测或成功登录后的横向活动。请拆成多个独立分析轨道，便于不同小组并行处理。
```

### 1200. D9_k983957_zh (domain=D9, difficulty=8)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的异常/离群检测分析，重点围绕“显式数值规则”来识别可疑流量：例如对 flow_duration、Header_Length、Rate、Srate、Drate、Duration、ack_count、syn_count、rst_count、HTTP/HTTPS/DNS/Telnet/SMTP/SSH/IRC/TCP/UDP/DHCP/ARP/ICMP/IPv/LLC 以及 Tot sum、Min、Max、AVG、Std、Tot size、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight 等字段，使用 IQR、极端值阈值、稀有类别、零值/近零值、以及跨标签对比分布等方式，找出最异常的样本、最可疑的攻击类型、以及异常指标之间的关联。请把工作拆成多个彼此独立的分析轨道，方便并行处理：1）整体异常值概览；2）按 label 的离群行为对比；3）端口/协议与稀有类别检测；4）阈值规则命中分析；5）多指标联合异常样本定位；6）输出可直接复核的统计摘要。请重点给出可执行的规则、命中数量、最极端的样本/类别，并明确说明哪些异常更像噪声、哪些更像真实攻击特征。
```

### 1201. D9_k984207_zh (domain=D9, difficulty=8)

```
请基于文件 sampadab17__network-intrusion-detection__Test_data.csv 做一份面向安全运营的时序/趋势分析，重点看“按记录顺序”形成的流量与攻击迹象变化，而不是单点统计。请把数据按原始行顺序视为一个会话序列，围绕 duration、src_bytes、dst_bytes、count、srv_count、serror_rate、srv_serror_rate、rerror_rate、srv_rerror_rate、same_srv_rate、diff_srv_rate，以及 protocol_type、service、flag 这些字段，分析：1）整体趋势是否存在阶段性升高或恶化；2）不同协议/服务/标志位在序列前后期的变化；3）高失败/高拒绝特征是否在时间上聚集；4）可疑模式在相邻窗口中的跃迁与集中度；5）哪些服务或 flag 的变化最能解释趋势拐点。请输出可直接给管理层和检测规则工程师看的结论，并附上 analysis_summary.json。
```

### 1202. D9_k984524_zh (domain=D9, difficulty=8)

```
请基于文件 subhajournal__iotintrusion__IoT_Intrusion.csv 做一份面向安全分析的异常/离群值排查报告，重点围绕“显式数值规则”来识别可疑流量：例如对 flow_duration、Header_Length、Rate、Srate、Drate、Duration、ack_count、syn_count、rst_count、Tot sum、Max、AVG、Std、IAT、Number、Magnitue、Radius、Covariance、Variance、Weight 等连续字段，结合 IQR、极端分位数、零值/近零值、以及协议/标志位/服务类别的稀有组合来判断异常；同时把 label 作为结果解释的参考但不要做建模。请把工作拆成多个彼此独立的分析轨道：1）整体异常值规模与极端阈值；2）按 label 的异常分布对比；3）按协议类型和服务/端口特征找稀有高风险组合；4）按 TCP 标志位与计数字段找规则型异常；5）按相关性与一致性找不合逻辑的数值组合；6）输出可执行的排查优先级建议。请给我能直接交付给安全团队的结论和依据，尽量明确阈值、计数、占比和最异常样本的特征。
```

