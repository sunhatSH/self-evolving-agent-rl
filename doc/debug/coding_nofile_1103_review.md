# Coding 无文件产出型任务审查清单（1103 条）

来源：`datasets/train_cl_backup.parquet`（旧 12800）中 bucket=coding、record_id 为 generated_tasks D_id、`has_inputs=False` 的任务。

这些任务 query 不引用输入文件，要求 agent **从零产出**代码（app.py/tests/README 等），沙箱无需注入文件。

## 统计

- 总数：1103
- 难度分布：{'5': 2, '6': 104, '7': 997}
- 域分布：{'D11': 192, 'D13': 112, 'D3': 201, 'D5': 454, 'D7': 144}

## 任务清单

### 1. D11_s982792_en (domain=D11, difficulty=5)

```
Build a from-scratch finance ops exception tool in Python for budget variance and invoice/expense review. I want `app.py`, `exceptions.py`, `rules.py`, `cli.py`, `tests/`, and a short `README.md` that explains how to run it. It should detect over-budget spend, duplicate invoices, missing PO/reference, weekend submissions, and unusual category spikes, then print a clean exceptions report from hardcoded sample data in the code.
```

### 2. D5_s982776_en (domain=D5, difficulty=5)

```
Build a small Python tool from scratch that parses application logs, groups repeated errors, and flags likely regressions from the last 24 hours. I want `logtriage.py`, `tests/test_logtriage.py`, and a short `README.md` with install/run examples and the log format assumptions you used.
```

### 3. D11_s982407_en (domain=D11, difficulty=6)

```
I need you to build a small from-scratch finance ops tool that flags budget variance and invoice/expense exceptions for a monthly close workflow. It should let a user load or paste transactions, compare them to a simple budget rule set, and output a clean exceptions report with categories like over-budget, duplicate invoice, missing PO, bad tax code, and out-of-policy expense. Please create the code, a short README, and whatever tests or sample usage files you think are needed, and make it practical enough that a finance team could actually run it locally.
```

### 4. D11_s982527_en (domain=D11, difficulty=6)

```
Build a small budget-variance and invoice-exception review tool from scratch for finance ops. I want a Python backend plus a simple CLI in app.py and README.md that can flag over-budget POs, duplicate invoices, and missing-approval expense claims, with configurable rules and a clean summary report. Use current best practices for a lightweight local app and document any libraries or patterns you choose.
```

### 5. D11_s982625_en (domain=D11, difficulty=6)

```
Build a small Python service for budget variance and invoice/expense exception handling from scratch. I want a FastAPI app with a rule engine, a JSON config for thresholds/coding rules, and endpoints to flag anomalies, explain exceptions, and export a review queue. Put the code in app.py, tests in tests/test_app.py, and a README.md with setup/run instructions.
```

### 6. D11_s982630_zh (domain=D11, difficulty=6)

```
我们财务团队现在最头疼的是预算偏差和发票/报销异常处理太分散：同样一笔费用，预算超支、重复提交、税率不一致、附件缺失、供应商信息不完整这些问题要靠人一条条看，效率很低，也容易漏掉高风险单据。我想从零做一个内部工具，专门帮我们把这些异常先自动筛出来，让财务和业务负责人能快速看到该优先处理什么。

请你直接帮我做一个可运行的代码工具，不要依赖我提供任何现成文件。你需要先自己查一下当前常见的做法、适合的开源库和实现方式，再从头搭一个简洁但实用的版本。这个工具最好能支持：输入一笔预算和一组费用/发票记录后，自动识别预算偏差、重复报销、超阈值、字段缺失、日期异常、供应商名称疑似不一致等情况；给每条记录一个风险等级和原因；最后输出一份便于财务复核的结果。

我希望交付的是完整的代码文件和一个简单的说明文档，最好再带上基本测试，方便我们后面自己接到内部系统里。你可以自己决定用命令行、简单 API，或者两者都做，但要尽量让这个工具能直接跑起来、好维护、也方便以后扩展规则。请把实现思路、主要功能和使用方法都整理好。
```

### 7. D11_s982655_en (domain=D11, difficulty=6)

```
I want a small internal tool for finance ops that helps us catch budget variance and invoice/expense exceptions before they hit AP review.
- Build it from scratch as a working Python app with a simple command-line workflow and a clean core rules engine.
- Let it compare a planned budget against actual spend by category, flag unusual variance, and label likely exception types like duplicate invoice, out-of-policy expense, or missing approval.
- Include a way to ingest mock records from hardcoded sample data in the code, since I’m not providing files.
- Add a short README with setup/run instructions and a few examples of how the checks work.
- Make the logic configurable so thresholds, approval rules, and exception categories can be adjusted without rewriting the whole app.
```

### 8. D11_s983067_en (domain=D11, difficulty=6)

```
Build a small invoice-exception and budget-variance workflow service from scratch in Python. I need the code in app.py plus tests in tests/test_app.py and a README.md with setup/run instructions. Make it handle submitted invoices, detect approval-required exceptions, and generate department budget variance summaries with a simple API and CLI.
```

### 9. D11_s983069_en (domain=D11, difficulty=6)

```
Build a small Python tool from scratch for budget variance and invoice/expense exception handling. I want `app.py` plus `README.md`: include a rules engine for flagging over-budget spend, duplicate invoices, missing PO matches, and policy exceptions, with a simple CLI and JSON output. Use current docs for a couple of relevant libraries if needed, and make it easy to extend with new exception rules.
```

### 10. D11_s983176_en (domain=D11, difficulty=6)

```
Build a from-scratch Python tool for budget variance and invoice/expense exception handling. I need a CLI plus a small library that can ingest records from JSON, calculate variance against budget, flag duplicates/out-of-policy expenses, and export a review queue with reason codes and severity. Create the code, tests, and README in separate files; no input data files, just the implementation.
```

### 11. D11_s983273_en (domain=D11, difficulty=6)

```
Build a small Python tool from scratch for finance ops that flags budget variances and invoice/expense exceptions, with a simple CLI and a JSON report output. Research current best-practice library choices for parsing, validation, and terminal output, then wire the implementation, tests, and README together in separate files.
```

### 12. D11_s983355_en (domain=D11, difficulty=6)

```
Build a from-scratch Python tool for finance ops that flags budget variances and invoice/expense exceptions, with a small CLI and JSON output. I want app.py, exceptions.py, rules.py, tests/, and README.md; no input files, just implement the feature and document how to run it.
```

### 13. D11_s983392_en (domain=D11, difficulty=6)

```
Build a from-scratch Python tool for finance ops that flags invoice and expense exceptions against budget rules, with a small CLI and JSON output. Put the code in app.py, tests in tests/test_app.py, and a short README.md with setup and usage. I need it to support vendor duplicate detection, policy-threshold checks, budget-variance alerts, and a compact exception report.
```

### 14. D11_s983428_en (domain=D11, difficulty=6)

```
Build a small Python app from scratch for budget variance and invoice/expense exception handling. I need a command-line tool plus a simple JSON-based rules engine that flags over-budget spend, duplicate invoices, missing approvals, and out-of-policy expenses, and outputs a clean exception report. Put the code in app.py, add tests, and include a README.md with setup and usage.
```

### 15. D11_s983479_en (domain=D11, difficulty=6)

```
I need you to build a small finance-ops tool from scratch that helps a team review budget variance and flag invoice/expense exceptions before they hit accounting. Please create the code, tests, and a short README for a CLI app that lets me load budget lines and transactions I paste in as JSON, compares actuals to budget, detects over-budget items and common exception patterns like duplicate invoices, missing PO numbers, weekend expense claims, and amounts just under approval thresholds, then outputs a clean exception report and a summary by cost center. Use current best practices and a couple of real Python libraries if they make sense, but don’t rely on any starter data or input files.
```

### 16. D11_s983584_en (domain=D11, difficulty=6)

```
Build a small budget-variance and invoice-exception service from scratch. I want a Python backend with `app.py`, `exception_rules.py`, and `README.md` that ingests in-memory sample transactions, flags budget overruns, duplicate invoices, missing PO numbers, and out-of-policy expenses, then exposes the results through a simple CLI and JSON API. Use current best-practice research for the stack and library choices, and make it production-leaning enough that Finance Ops could extend it later.
```

### 17. D11_s984236_en (domain=D11, difficulty=6)

```
Build a small from-scratch finance ops tool in Python that flags budget variances and invoice/expense exceptions, with a CLI and a simple rules engine. I want app.py, rules.py, tests/, and README.md; use current best-practice libraries only if needed and document the setup.
```

### 18. D11_s984585_en (domain=D11, difficulty=6)

```
Build a small Python tool from scratch for finance ops that flags budget variance and invoice/expense exceptions, with a simple rule engine and a CLI. I want app.py, rules.py, tests/, and a short README.md showing how to run it and how the exception logic works.

Please research a couple of current open-source Python libs or best-practice patterns first so the design is sensible, then implement the code and tests without using any input files or sample datasets.
```

### 19. D13_s981240_en (domain=D13, difficulty=6)

```
Build a from-scratch Python tool for product analytics readouts: implement experiment A/B summary stats, funnel conversion, and cohort retention from event streams, with a small CLI and a test suite. I want app.py, analytics.py, cli.py, tests/, and a short README.md with usage and assumptions.
```

### 20. D13_s982683_en (domain=D13, difficulty=6)

```
Build me a small product-analytics experiment readout tool from scratch. I want a Python CLI that can ingest in-memory event definitions and emit A/B readouts, funnel conversion tables, and cohort retention summaries in Markdown and JSON. Put the code in `src/`, add tests in `tests/`, and include a short `README.md` with usage examples.
```

### 21. D13_s983826_en (domain=D13, difficulty=6)

```
Build a small product-analytics experimentation service from scratch: a Python backend with an API for A/B test readouts, funnel conversion, and cohort retention, plus a minimal README. I want files like `app.py`, `analytics.py`, `experiments.py`, `README.md`, and tests; no input data files, just the code and docs.
```

### 22. D13_s984039_en (domain=D13, difficulty=6)

```
Build a from-scratch Python CLI for product analytics experiment readouts: `experiment_readout.py` plus `README.md`. It should compute A/B test lift, confidence intervals, funnel conversion by step, and cohort retention summaries from events you generate in code, no input files. Use current best practices for stats libraries and CLI UX, and document the design choices in the README.
```

### 23. D13_s984616_en (domain=D13, difficulty=6)

```
Build a small Python analytics service from scratch for experiment readouts: reusable modules for A/B significance, funnel conversion, and cohort retention, plus a FastAPI endpoint and a CLI. I want app.py, analytics.py, tests/test_analytics.py, and README.md; no input files, just implement the code and docs.
```

### 24. D3_s981748_en (domain=D3, difficulty=6)

```
I need you to build a small from-scratch data quality toolkit for internal ops that can clean messy event logs, flag anomalies, and generate a KPI dashboard summary from in-memory sample data. Please create the code, tests, and a short README, and make it work as a real reusable package with a CLI or simple API. There are no input files — use synthetic data you generate in the code for demos and tests, and make sure the design follows current best practices for Python data tooling and visualization libraries.
```

### 25. D3_s982178_en (domain=D3, difficulty=6)

```
Build a from-scratch Python tool for warehouse KPI monitoring: create `kpi_engine.py`, `anomaly_rules.py`, `dashboard.py`, and `README.md`. It should clean time-series operational data, compute KPIs like on-time rate, defect rate, throughput, and alert on anomalies with a small Streamlit dashboard.
```

### 26. D3_s982240_en (domain=D3, difficulty=6)

```
I need you to build a small Python tool from scratch that can clean messy KPI/event data, detect anomalies, and generate a simple dashboard-ready summary for a retail ops team. Please create the code and README only, with no input files assumed — the tool should accept raw JSON/CSV pasted in or generated sample data, normalize timestamps and categories, flag outliers in key metrics, and export a cleaned dataset plus a KPI summary report and basic charts. Use current best practices and a couple of appropriate open-source libraries, but make sure the implementation is self-contained and easy to run locally.
```

### 27. D3_s982356_en (domain=D3, difficulty=6)

```
Build a from-scratch Python tool for cleaning and monitoring KPI streams: I want `kpi_guard.py`, a small CLI dashboard, and `README.md`. It should ingest synthetic or pasted JSON event batches, clean bad records, detect anomalies, and print/export KPI summaries for ops usage.
```

### 28. D3_s982428_en (domain=D3, difficulty=6)

```
Build a small Python project from scratch for our ops team: a KPI dashboard engine that cleans event data, flags anomalies, and renders a Streamlit web app with trend charts and alert summaries. I need the code in app.py plus a short README.md with run steps and config notes; no input files, just code that can ingest a CSV or API JSON later.

Use current best practices for Streamlit, pandas, and anomaly detection, and make the architecture easy to extend for new KPIs and data sources.
```

### 29. D3_s982500_en (domain=D3, difficulty=6)

```
Build a small Python data-quality tool from scratch for a SaaS ops dashboard: I need a cleaning + anomaly-detection + KPI pipeline that can be plugged into a BI report later. Create the code, not a sample analysis, and make it work with synthetic records generated in code. Include a CLI, a reusable library module, and a minimal dashboard output file.
```

### 30. D3_s982548_en (domain=D3, difficulty=6)

```
Build a small Python tool from scratch for ops KPI monitoring: ingest raw JSON/CSV logs, clean and normalize timestamps, detect anomalies in daily metrics, and generate an HTML dashboard plus a Markdown summary. Put the code in app.py, tests in tests/, and a short README.md with install/run instructions. Use current best-practice library choices where needed and keep it dependency-light.
```

### 31. D3_s982579_en (domain=D3, difficulty=6)

```
We need a small internal tool to help our operations team spot bad customer and sales data before it reaches our weekly KPI dashboard, because right now we keep finding broken records too late and the numbers look wrong. Build a clean, from-scratch code tool that can take in plain records, clean obvious issues, flag strange values, and calculate a simple KPI summary we can review quickly. I do not have any starter files for this, so please create the code and the basic documentation from scratch. I want something practical that can be reused by the team, with a way to run it from the command line and a simple visual summary output if that makes sense.
```

### 32. D3_s982818_en (domain=D3, difficulty=6)

```
We need a small internal tool to help our operations team catch data issues before they hit our weekly KPI dashboard. Please build a from-scratch Python app that can take in live-looking event records we generate inside the code, clean the data, flag suspicious spikes or gaps, and show a simple KPI summary and chart so non-technical managers can review it. I do not have any input files for this — please create the sample data generator, the processing logic, the anomaly detection, and the visualization yourself. I also want a short README that explains how to run it and how the checks work, plus a few tests so we can trust it before we use it in demos.
```

### 33. D3_s982850_en (domain=D3, difficulty=6)

```
Build a small Python tool from scratch for log quality monitoring: parse newline-delimited JSON app logs, clean/normalize fields, detect anomalies in request volume, error rate, and latency, and compute a daily KPI summary. I want the code in app.py plus a README.md with setup, usage, and examples; no input files, generate sample data in code for demos. Make it usable from the command line and easy to extend.
```

### 34. D3_s983478_en (domain=D3, difficulty=6)

```
I need you to build a small from-scratch Python tool for cleaning messy time-series ops data and turning it into KPI and anomaly reports: one module for ingesting raw records from in-memory JSON/dicts, one for normalization and validation, one for anomaly detection, and one for exporting a simple dashboard-style HTML report plus a CLI entry point. Please include the code files, a README, and tests, and make it handle missing values, duplicate timestamps, schema drift, and alert-style KPI summaries without relying on any input files.
```

### 35. D5_s980459_en (domain=D5, difficulty=6)

```
I want a small but realistic internal tool to help debug flaky CI failures in our GitHub Actions pipeline.

- Build it from scratch as a Python package with a CLI that ingests raw GitHub Actions job logs pasted in as text and turns them into a structured failure summary.
- It should detect common failure patterns like test assertion failures, timeout-like hangs, dependency/install errors, and environment/setup issues, then emit a clean JSON report plus a human-readable Markdown summary.
- Include a simple rules engine so we can add or tweak log signatures without rewriting the core parser.
- Add a test suite with representative synthetic logs you create yourself, plus a README showing how to run it locally and extend the rules.
- Please research current best practices and any relevant library choices first, especially around log parsing, CLI design, and Python testing/packaging, then build the code and docs.
```

### 36. D5_s980501_en (domain=D5, difficulty=6)

```
Build a small Python log-triage tool from scratch and put it in app.py plus README.md. It should watch a local log directory, parse rotating app logs, detect error spikes and repeated stack traces, and print a ranked incident summary with suggested next checks. Use a real library choice for file watching and pattern matching, and include a few example commands in the README.
```

### 37. D5_s980576_en (domain=D5, difficulty=6)

```
Build a small Python log-triage tool from scratch: parser, anomaly detector, and CLI for Kubernetes pod logs and app server logs. I want app.py, logtriage.py, tests/, and a short README.md with setup and usage.
```

### 38. D5_s980609_en (domain=D5, difficulty=6)

```
Build a Python CLI tool 'log_analyzer.py' that parses Apache/NGINX access logs, outputs a summary of error types (4xx, 5xx), identifies the slowest 10 requests, and generates a test plan (suggested load test scenarios) based on peak traffic patterns. Also write unit tests in 'test_log_analyzer.py' and a 'README.md' with usage. Research best practices for log parsing (e.g., pyparsing, regex) and anomaly detection heuristics online. Deliverables: log_analyzer.py, test_log_analyzer.py, README.md.
```

### 39. D5_s980662_en (domain=D5, difficulty=6)

```
Our team spends too much time manually sifting through scattered log files from different microservices when debugging failures. I need a CLI tool that can take a log file (or multiple files), automatically identify error types (like 500 errors, connection timeouts, stack traces), count how often each occurs, and output a clean summary report. Build this from scratch – no starter code. Please research common log formats (e.g., Apache, syslog, custom JSON logs) and best practices for regex-based parsing and CLI design in Python. The tool should be easy to extend later. Deliver the code and a README.
```

### 40. D5_s980667_en (domain=D5, difficulty=6)

```
Hey, I need a CLI log analyzer tool built from scratch in Python. It should parse multiple log formats like Apache combined and syslog, filter by a time range (ISO datetime), and output summary statistics (line count, error level breakdown, top IPs). Deliverables: log_analyzer.py, test_log_analyzer.py, README.md. Make it modular, testable, and handle malformed lines gracefully. Research common log formats online to design the parsers. Keep dependencies minimal (stdlib + maybe dateutil). Go.
```

### 41. D5_s980715_en (domain=D5, difficulty=6)

```
We need a small internal troubleshooting tool because our support team keeps losing time when customer incidents come in and nobody can quickly tell whether a failure is a bad deploy, a dependency issue, or just noisy logs. I want you to build this from scratch as a real working code project, not a mockup. It should include a command-line tool that can ingest plain text log output pasted into stdin, detect the most common error patterns, group repeated messages, and produce a short incident summary with likely severity and next-step suggestions. Please also add a simple way to run it in a test mode so we can verify the parser and detection logic. I need the actual code files, plus a short README that explains how to install and use it. Use current best practices and, where helpful, look up the right Python libraries or approaches for log parsing, CLI design, and testing before building it.
```

### 42. D5_s980717_en (domain=D5, difficulty=6)

```
I need a small internal troubleshooting tool built from scratch for our engineering team to analyze service logs and catch recurring failure patterns.
- Build a CLI utility that ingests pasted log text from stdin, groups related errors by signature, and highlights probable root causes.
- Make it useful for real incident reviews: include timestamp parsing, stack-trace clustering, severity bucketing, and a compact summary report.
- Use current best practices and a lightweight Python stack; check modern libraries and logging-analysis patterns online before you implement.
- Include a test suite with realistic synthetic log cases, plus a short README explaining how to run it and how the grouping logic works.
- Deliver the finished code and docs, not a mockup.
```

### 43. D5_s980720_en (domain=D5, difficulty=6)

```
Build a small Python tool from scratch for incident log triage: parse mixed app logs from stdin, detect repeated error bursts, correlate stack traces by fingerprint, and output a human-readable summary plus JSON. Put the code in triage.py and add tests in tests/test_triage.py; include a short README.md with usage examples and assumptions.
```

### 44. D5_s980766_en (domain=D5, difficulty=6)

```
I need you to build a command-line tool for analyzing server logs. It should parse common log formats (Apache, Nginx, Syslog), compute summary stats like request counts per IP, status code distribution, and detect simple anomalies like spikes in 4xx errors. I want the tool to be self-contained in Python, using only the standard library plus maybe one lightweight third-party library if needed. Also include unit tests and a README. No input files provided – I'll run it on my own logs later.
```

### 45. D5_s980822_zh (domain=D5, difficulty=6)

```
我们现在每天要盯着几套线上服务的日志和告警，靠人工翻看很费时间，也容易漏掉真正需要处理的问题。我想从零做一个轻量的日志诊断工具，先能把常见的错误模式自动归类，再把高风险问题用更清楚的方式提示出来，最后方便我们后面接到现有的运维流程里。

请你直接帮我做成代码，不要用现成模板凑合。先自己调研一下适合这个场景的实现方式、常用库和最佳做法，然后从头写出一个可运行的小工具：它要能读取一段结构化日志文本，识别常见异常、重复报错、超时、连接失败这几类问题，输出一份适合值班同事快速看的诊断结果；最好还能带一个简单的命令行入口，方便本地直接跑。你再补一份测试方案和基础测试，保证这个工具不是只有演示效果。

如果你觉得有必要，也可以把架构拆得更合理一点，比如核心解析、规则判断、结果汇总、命令行和测试分开做。最终请把完整代码和说明一起给我。
```

### 46. D5_s980852_en (domain=D5, difficulty=6)

```
Build a small Python CLI called logtriage for debugging production logs from scratch. I need logtriage.py, tests/test_logtriage.py, and a README.md that explains setup and usage; include parsing for JSONL and common nginx-style text logs, grouping by error signature, top-N summaries, and a simple anomaly flagger. Use current best practices/libraries you verify online before coding.
```

### 47. D5_s980889_en (domain=D5, difficulty=6)

```
Build a from-scratch Python tool that ingests plain-text application logs and diagnoses common failure patterns in CI jobs and microservices. I want `logtriage.py` plus `README.md`, with a CLI that outputs a ranked incident summary, probable root-cause categories, and suggested next checks; no input files, just code and docs.
```

### 48. D5_s980980_en (domain=D5, difficulty=6)

```
I need a from-scratch internal tool for debugging incident logs from our Kubernetes services.
- Build a small Python app that ingests plain-text logs pasted into stdin or a file and turns them into a structured incident summary.
- I want it to detect common patterns like repeated errors, first-seen timestamps, probable root-cause lines, and a simple timeline of notable events.
- Please include a command-line interface, a reusable parsing module, and a test suite with realistic synthetic log examples.
- Also add a short README explaining how to run it and how the detection logic works.
```

### 49. D5_s981038_en (domain=D5, difficulty=6)

```
We need to reduce the time our support team spends digging through service logs when customers report incidents, so I want a small internal tool built from scratch that can scan plain text logs, flag likely error patterns, and produce a clean incident summary our team can use in Slack and Jira. Please research the best lightweight approach for parsing and matching log lines in Python, then build the tool as working code with a simple command-line interface, clear error handling, and tests. I want the final deliverable to include the code files and a short README explaining how to run it and what kinds of logs it can analyze. There are no input files to start from; use realistic sample logs inside the tests and examples.
```

### 50. D5_s981213_en (domain=D5, difficulty=6)

```
Build a from-scratch Python 3.11 log triage tool for Sentry-style application logs: create `logtriage.py` and `README.md` that detect crash signatures, group duplicate stack traces, and generate a concise incident summary from pasted logs. I want it to support stdin or a `--log-file` path, output JSON and human-readable modes, and include a small test suite with realistic sample logs generated in-code. Use current best practices for parsing regex-heavy logs and CLI design.
```

### 51. D5_s981312_en (domain=D5, difficulty=6)

```
I need you to build a small Python log-debugging tool from scratch that helps me diagnose flaky CI failures by parsing plain-text build logs, grouping repeated error patterns, and generating a short triage report with likely root-cause categories. Please create the code and a README, and use current docs or examples from the web for the logging/parser libraries and CLI best practices so the design is solid.
```

### 52. D5_s981478_en (domain=D5, difficulty=6)

```
Build a from-scratch Python tool for analyzing Kubernetes container logs and debugging crash loops: include a parser, anomaly detection rules, and a CLI that outputs a concise incident summary plus recommended next steps. Use current best practices for log formatting and Kubernetes event fields, and write the code into app.py with tests in test_app.py and a short README.md.
```

### 53. D5_s981504_en (domain=D5, difficulty=6)

```
I need you to build a small Python log-triage tool from scratch that helps debug failed CI runs: it should read plain-text logs from stdin, detect common failure patterns across Python, Node, and Docker builds, cluster repeated errors, and print a concise summary with suggested next checks. Please give me the code files and a short README, and make sure the implementation is based on current best practices for log parsing and CLI design.
```

### 54. D5_s981525_en (domain=D5, difficulty=6)

```
Build a from-scratch Python log-triage tool for our Kubernetes services: create `logtriage.py` and `README.md` for a CLI that ingests plain text app logs from stdin, detects common failure patterns, groups related stack traces, and prints a prioritized incident summary with probable root-cause hints. Research best-practice approaches for Python log parsing and CLI design, then implement it cleanly with tests and no external input files.
```

### 55. D5_s981573_en (domain=D5, difficulty=6)

```
Build a from-scratch Python log triage tool for our Kubernetes services: core parser, anomaly scoring, and a CLI that summarizes suspicious spikes from structured JSON logs. I want app.py, tests/test_app.py, and README.md, with a short section in the README on how the scoring works and how to run it.

Use current best practices from web research for Python logging/JSON parsing and CLI design, then implement everything from scratch.
```

### 56. D5_s981584_en (domain=D5, difficulty=6)

```
Build a small Python log-triage tool from scratch for Kubernetes-style app logs. I want app.py, parser.py, report.py, and README.md that can parse mixed JSON/text logs, detect error bursts, group repeated stack traces, and print a concise incident summary to stdout. Use current best practices from web docs for Python logging, regex parsing, and CLI design, then wire in a few focused tests.
```

### 57. D5_s981620_en (domain=D5, difficulty=6)

```
Build a small Python CLI tool from scratch for debugging flaky CI logs. I want `ci-log-triage.py` plus `README.md` that can ingest pasted GitHub Actions or CircleCI logs from stdin, detect the likely failure category, and print a short root-cause summary with suggested next steps. Please research current log formats, common failure patterns, and any useful library choices before implementing it.
```

### 58. D5_s981675_en (domain=D5, difficulty=6)

```
We need a small internal tool to make incident debugging and log review faster for our support team. Right now we spend too much time guessing whether a service issue is a real outage, a bad deploy, or just noisy logs from a known pattern. Please build a from-scratch command-line utility that reads plain text logs from standard input, groups related messages into incidents, flags likely error spikes, and produces a short human-readable summary plus a machine-friendly JSON output. It should be practical for day-to-day use, easy to run locally, and include a clear test plan so we can trust it before sharing it with the wider team. I want the code, tests, and a short README explaining how to use it.
```

### 59. D5_s981697_en (domain=D5, difficulty=6)

```
I need you to build a small log-triage tool from scratch for our on-call workflow: a Python CLI that reads plain text app logs from stdin or a file, detects likely error bursts and repeated stack traces, groups related incidents, and prints a compact incident summary with timestamps, error signatures, and probable root-cause hints. Please research a couple of practical Python logging/parsing patterns and any good libraries or best practices first, then implement the code, tests, and a short README showing how to run it and what the output means.
```

### 60. D5_s981721_en (domain=D5, difficulty=6)

```
I need you to build a small Python tool from scratch that parses application logs, detects a few common failure patterns, and produces a human-readable incident summary plus a machine-readable JSON report. Please make it a real code deliverable with the core library, a CLI, tests, and a short README, and use web research where needed to pick a sensible log format/parser approach and any best practices for CLI/testing. There are no input files to start from — just build the tool and its docs.
```

### 61. D5_s981744_en (domain=D5, difficulty=6)

```
I need you to build a small log-triage tool from scratch in a few files: a Python CLI that reads plain text app logs from stdin or a file, detects common failure patterns with timestamps, groups related errors into incidents, and outputs a concise incident summary plus a JSON report. Use current best practices and existing library docs where helpful, especially for robust regex handling, structured logging, and CLI design, and make sure the code is clean enough to extend later.
```

### 62. D5_s981766_en (domain=D5, difficulty=6)

```
Build a small Python 3.12 log-triage tool from scratch for incident debugging. I want a CLI in `triage.py`, a parser/analyzer package, and a short `README.md` showing how to use it on pasted stdin logs. Make it detect common failure patterns in structured and plain-text logs, group related errors, and emit a concise incident summary with likely root-cause hints.
```

### 63. D5_s981788_en (domain=D5, difficulty=6)

```
Build a small Python tool from scratch for debugging production logs: `logtriage.py` plus `README.md`. It should ingest plain-text app logs from stdin or a file path, detect error clusters by stack-trace similarity, summarize top failure signatures, and export a Markdown incident report with timelines and candidate root causes. Use current best practices from the web for Python log parsing, Levenshtein/sequence matching, and CLI design.
```

### 64. D5_s981809_en (domain=D5, difficulty=6)

```
Build a small Python log-debugging tool from scratch: `logtriage.py`, `parser.py`, `rules.py`, `report.py`, and `README.md`. It should ingest raw text logs from stdin or `--log-file`, detect common failure patterns, group repeated stack traces, and print a ranked incident summary with likely root-cause hints and next steps.
```

### 65. D5_s981927_en (domain=D5, difficulty=6)

```
Build a small Python CLI called logtriage from scratch and put it in app.py plus README.md. It should ingest a stream of plain-text app logs from stdin or a file path, detect common failure patterns, cluster repeated incidents, and print a concise incident summary with likely root-cause hints and next-step checks. Use current best practices and library choices from the web, then implement and test it without any input data files.
```

### 66. D5_s981934_en (domain=D5, difficulty=6)

```
I need a small internal tool built from scratch because our support team keeps losing time when a service outage happens and the logs are noisy. What I want is a lightweight Python command-line tool that can read plain-text application logs, spot common error patterns, group related lines into incidents, and produce a short incident summary that a non-engineer can understand. Please design and build the code, plus clear setup notes and tests, so we can run it locally without any external services or input files.
```

### 67. D5_s981958_en (domain=D5, difficulty=6)

```
We need a lightweight internal incident-log tool because our support team keeps losing time when Kubernetes jobs fail and the messages are spread across too many logs. Build a small from-scratch utility that can collect log snippets from a pasted text blob, detect common failure patterns, and turn them into a short incident summary with suggested next checks. I want the code and a short README explaining how to run it. Please research current best practices for log parsing and incident summaries, then build something practical rather than a demo.
```

### 68. D5_s982059_en (domain=D5, difficulty=6)

```
I need you to build a small Python log-triage tool from scratch that ingests plain text service logs, spots likely incident patterns, and outputs a concise summary with severity, probable root-cause hints, and a few suggested next checks. Please include the code files, a README with setup/run instructions, and a test suite; I also want the design to follow current best practices for log parsing and CLI tools, so use web research to choose a sensible library stack and structure before you implement it.
```

### 69. D5_s982182_en (domain=D5, difficulty=6)

```
I want a small but real incident-debugging tool built from scratch for our backend team.
- Build a Python CLI that ingests raw application logs from stdin and turns them into a clean incident timeline with grouped errors, request IDs, and probable root-cause hints.
- Research current best practices and a couple of real libraries/APIs for parsing timestamps, structured logs, and pretty terminal output before you implement it.
- Include a compact test suite that covers noisy log formats, malformed lines, and duplicate event grouping.
- Add a README with install/run examples and a short section on how to extend the parser for new log formats.
- I want the final code files and docs, not a report.
```

### 70. D5_s982190_en (domain=D5, difficulty=6)

```
I need you to build a small from-scratch log triage tool for Kubernetes incidents: make a Python CLI that reads plain text logs from stdin, groups repeated errors, spots likely root-cause patterns, and outputs a readable incident summary plus a JSON report. It should be usable on live terminal output, include a handful of built-in parsing rules for common Python/Node/Go stack traces and timeout/auth errors, and ship with tests and a short README showing how to run it and extend the rules.
```

### 71. D5_s982294_en (domain=D5, difficulty=6)

```
Build me a small Python 3.12 tool for debugging Kubernetes app logs: parse plain-text logs from stdin or a file, detect error bursts and probable root causes, and print a compact incident summary plus a JSON mode. Put the code in app.py, tests in tests/test_app.py, and usage notes in README.md. Use current best practices for log parsing/CLI design and keep it dependency-light if possible.
```

### 72. D5_s982324_en (domain=D5, difficulty=6)

```
We need a small internal debugging tool because our support team keeps losing time chasing down errors from a few different services, and I want one place that turns raw logs into a clear incident summary. Build a from-scratch Python tool that can read pasted log text from standard input or a file path, detect likely error bursts, group related lines into one incident, and output a clean summary with the first error, last error, service name if present, and the most likely root-cause pattern. I also want a simple command-line interface, a few sane tests, and a short README that explains how to run it and how the grouping logic works. Please research current best practices for Python log parsing, CLI design, and any standard libraries or lightweight packages that would make sense before building it.
```

### 73. D5_s982443_en (domain=D5, difficulty=6)

```
I need you to build a small log-analysis tool from scratch for debugging Kubernetes-style app logs: parse JSON lines and plain text, detect error spikes, group repeated stack traces, and output a clear incident summary plus a CSV export. Use current best practices for Python logging and a lightweight CLI framework, and check the docs for the standard library and a couple of popular libraries before you code. I want the finished code files and a short README that explains how to run it and how the detection works.
```

### 74. D5_s982463_en (domain=D5, difficulty=6)

```
Build a small Python tool from scratch for SRE log triage: a CLI that ingests plain-text service logs from stdin, classifies likely root causes from error patterns, and emits a compact incident summary plus a JSON report. I want app.py, tests/, and README.md; use current best practices and whichever library/API docs you need to research first.
```

### 75. D5_s982491_en (domain=D5, difficulty=6)

```
I need you to build a small Python log-analysis tool from scratch that helps debug flaky CI runs: it should read plain-text build logs, detect common failure patterns like timeouts, retry storms, dependency install errors, and test flakiness, then output a structured summary plus a human-readable report. Please research a couple of good Python parsing/reporting libraries and logging best practices first, then create the code, tests, and a README that explains how to run it and extend the detectors.
```

### 76. D5_s982524_en (domain=D5, difficulty=6)

```
Build a small Python tool from scratch that tails application logs, parses structured and unstructured lines, and flags likely incident patterns in real time. I want app.py, tests, and a README.md that explains the CLI, the detection rules, and how to run it locally. Use current best practices for Python logging/regex/parsing and reference any relevant library docs you need while designing it.
```

### 77. D5_s982553_en (domain=D5, difficulty=6)

```
We need a small internal tool because our support team keeps losing time when customer incidents come in with broken logs and no clear next step. I want you to build a from-scratch log triage utility that can take pasted incident notes, identify likely failure patterns, and produce a plain-English summary plus suggested debugging checks for our engineers. Please make it realistic for use in a team workflow: I want a working command-line tool with a clean output format, clear error handling, and enough tests that we can trust it. Use current best practices and any relevant libraries or approaches you need to research, then build the code and a short README so another engineer can run it and understand how it works. There are no input files to start from; you should design the whole thing yourself.
```

### 78. D5_s982571_en (domain=D5, difficulty=6)

```
Build a small Python tool from scratch for debugging log spikes in a microservice: parse one service’s structured JSON logs from stdin, detect bursts and top error signatures, and output a concise incident report plus a CSV summary. Name the main files app.py, analyzer.py, and README.md, and include a minimal test suite.
```

### 79. D5_s982623_en (domain=D5, difficulty=6)

```
I need you to build a small Python log-triage tool from scratch that can ingest app logs pasted into stdin or a text blob, detect common failure patterns, and spit out a short incident report with likely root-cause clues, grouped errors, and a timestamped timeline. Please research a couple of current Python logging/parsing best practices and any useful standard-library or lightweight library options before you code it, then give me the finished code and a README showing how to run it and a few example commands.
```

### 80. D5_s982695_en (domain=D5, difficulty=6)

```
I need you to build a small log-triage tool from scratch for Node.js that helps debug flaky CI jobs by parsing plain-text build logs, detecting common failure patterns, and outputting a concise incident summary plus a suggested next-step checklist. Please create the code files and a short README, and make sure the design follows current best practices for log parsing, CLI structure, and testable error handling.
```

### 81. D5_s982711_en (domain=D5, difficulty=6)

```
I want a small from-scratch developer tool that helps on-call engineers debug services faster from logs and traces.
- Build a Python CLI that ingests plain-text app logs from stdin and flags likely incident patterns, then prints a concise triage summary.
- Include pattern detection for retries, auth failures, timeout storms, and sudden error-rate spikes, with sensible defaults and a config file option.
- Research current best practices and any relevant Python libraries for CLI parsing, log parsing, and text highlighting before you code, then implement the tool cleanly from scratch.
- Add a test suite that covers the main detectors, edge cases, and the CLI behavior.
- Write a short README with usage examples and a section explaining how the heuristics work and when they can fail.
```

### 82. D5_s982816_en (domain=D5, difficulty=6)

```
We need a small internal troubleshooting tool because our support team keeps losing time when customer incidents come in with vague logs, and I want a real working prototype rather than another spreadsheet. Build a from-scratch Python utility that takes pasted log text, groups related lines into incidents, highlights likely error patterns, and produces a short plain-English summary plus a simple test plan for what to check next. I want the built code and a short README so our team can run it locally and understand how it works. Please design it using current best practices and check the latest options for a lightweight parser and command-line handling before you build it.
```

### 83. D5_s982878_en (domain=D5, difficulty=6)

```
I want a from-scratch internal tool for debugging and log analysis around flaky jobs in our CI/CD pipeline.
- Build a small Python service or CLI that ingests plain-text logs, extracts errors/warnings, groups repeated failures, and outputs a concise triage summary.
- Include a lightweight rules engine so I can define patterns like known exceptions, retryable network failures, and timeout signatures without editing code.
- Add a simple test plan with representative synthetic logs and unit tests that prove the parser, grouping, and summary logic work.
- Use current best practices and a couple of real libraries where they make sense, but implement the core behavior yourself.
- Deliver the built code and a short README explaining how to run it and extend the rules.
```

### 84. D5_s982942_zh (domain=D5, difficulty=6)

```
帮我从零做一个可落地的日志故障排查小工具，做成 Python 项目，生成 `app.py`、`pyproject.toml`、`README.md` 和 `tests/`。功能要包括：读取并解析本地日志文本、按时间/级别/关键字过滤、检测常见异常模式、输出带上下文的诊断摘要，顺手给出一个命令行入口和基础测试。顺带查一下 Python 标准库和 `logging`/`re`/`argparse` 的最佳实践，再按你查到的推荐方式实现。
```

### 85. D5_s982961_en (domain=D5, difficulty=6)

```
We need a small internal tool because our incident reviews keep wasting time on scattered logs and inconsistent triage notes, and I want something our support and engineering teams can actually use during outages. Build a from-scratch command-line tool that takes pasted log text or stdin, spots likely error patterns, groups repeated messages, highlights timestamps and request IDs when present, and produces a short incident summary with suggested next checks. Please research a few current Python libraries and best practices first, then build the tool, add tests, and write a short README explaining how to run it and what it can and cannot do. No input files are provided — the tool should work from pasted text or standard input.
```

### 86. D5_s983194_en (domain=D5, difficulty=6)

```
Build a from-scratch Python tool for log triage that ingests raw service logs from stdin, flags likely incidents, and outputs a concise Markdown report plus JSON summary. Put the code in app.py, tests in tests/test_app.py, and a short README.md with run examples and assumptions.
```

### 87. D5_s983342_en (domain=D5, difficulty=6)

```
I need you to build a small log-correlation tool from scratch for incident debugging: a CLI that takes a few service log lines pasted in as text, normalizes timestamps, groups related events into a timeline, flags likely root-cause clues, and exports a clean markdown incident summary. Please use current best practices for Python logging and CLI design, and check the docs for any libraries you rely on before coding. I want the finished code files plus a short README that shows how to run it and a couple of example commands.
```

### 88. D5_s983351_zh (domain=D5, difficulty=6)

```
帮我从零写一个 Python 3.12 的日志故障排查小工具，支持解析 JSON/纯文本日志、按时间窗和关键字过滤、聚合错误分布、输出可读报告，并提供命令行入口和基础测试。把代码拆成多个文件，顺手补一份 README.md 说明安装、用法和已知限制。
```

### 89. D5_s983356_zh (domain=D5, difficulty=6)

```
我们最近在排查线上服务偶发超时和重试风暴的问题，手工看日志太慢，也很难快速判断是哪个接口、哪类错误、还是哪个时间段最值得先处理。我想从零做一个轻量的日志诊断工具，最好能直接帮工程和运维同事把一批文本日志整理成可读的故障摘要、按严重程度分组、找出高频错误模式，并给出简单的排查建议。请你先做必要的网页查证，参考一些常见日志格式、Python 生态里适合处理文本和命令行工具的做法，再从头实现这个工具，给我完整的代码和说明。不要用现成的输入文件；直接把工具本身做出来，后面我会自己接日志源。
```

### 90. D5_s983357_en (domain=D5, difficulty=6)

```
We keep losing time when production incidents happen because the logs are noisy and the team has to manually hunt for the real error pattern. I want a small internal tool built from scratch that can read plain text application logs, detect likely incident windows, group related errors, and generate a short investigation summary I can hand to engineering. Please build the code for this, not a data report. It should include a simple command-line interface, a reusable core library, and clear tests so we can trust the results. I don’t have any input files to provide — the tool should be designed to work with logs pasted in or read from a file path we pass in. Use whatever modern approach makes sense, but please research current best practices and existing libraries first so the design is sensible. I want the finished code files and a short README that explains how to run it and what it does.
```

### 91. D5_s983363_en (domain=D5, difficulty=6)

```
Build a small Python tool from scratch that ingests app logs from stdin or a pasted string, detects likely root causes for incidents, and prints a human-readable incident summary plus a JSON summary. I want app.py, tests, and README.md; make it work for real mixed logs from Python/Node services and include a few sample log patterns in the docs. Use current best practices for Python logging, regex parsing, and CLI design.
```

### 92. D5_s983403_en (domain=D5, difficulty=6)

```
I need you to build a small command-line log triage tool from scratch for Python that can take a directory of app logs, detect common failure patterns, and spit out a concise incident summary plus a machine-readable JSON report. Please include the code files, tests, and a README, and use real web research to pick a good log parsing approach and any libraries or best practices before you implement it.
```

### 93. D5_s983483_en (domain=D5, difficulty=6)

```
Build a from-scratch Python log triage tool called `logtriage` with `src/logtriage.py`, `tests/test_logtriage.py`, and `README.md`. It should parse mixed JSON/text app logs, detect error spikes and common failure signatures, and print a concise incident summary plus suggested next checks.
```

### 94. D5_s983494_en (domain=D5, difficulty=6)

```
Build a from-scratch Python log triage tool for Kubernetes incident debugging. I want `logtriage.py` plus `README.md`: it should ingest plain-text container logs from stdin or a file, detect common failure patterns (OOMKill, CrashLoopBackOff, connection timeouts, TLS errors, DNS failures), group repeated messages, and print a concise incident summary with severity scores and suggested next checks. Use current best practices from Python stdlib/argparse/logging and Kubernetes docs or common incident-debugging guides as needed.
```

### 95. D5_s983518_en (domain=D5, difficulty=6)

```
Build a from-scratch Python tool for Kubernetes log debugging that can ingest live or pasted logs, detect common crash-loop/root-cause patterns, and output a concise incident report plus suggested next checks. Create the code in `logtriage.py`, tests in `test_logtriage.py`, and a short `README.md` with usage examples and assumptions.
```

### 96. D5_s983531_en (domain=D5, difficulty=6)

```
Build a from-scratch Python tool for postmortem debugging that ingests application logs from stdin or a pasted string, groups repeated errors by fingerprint, and prints a concise incident summary with top suspects and timeline spikes. I want `logtriage.py`, `tests/test_logtriage.py`, and `README.md`; use whatever standard libraries or a small third-party parser you research, but no starter files or input fixtures.
```

### 97. D5_s983632_en (domain=D5, difficulty=6)

```
We need a small internal tool that helps our ops team investigate incidents faster, because right now we lose time jumping between logs, guessing likely causes, and writing repeat notes by hand. Please build it from scratch as a lightweight command-line app that can read plain text logs from standard input or a pasted log string, detect likely error patterns, group related lines into incidents, and produce a short incident summary with probable root-cause hints and follow-up questions for support. I want the code, tests, and a short README for how to run it. Please use current best practices and look up any useful Python libraries or approaches for log parsing, pattern matching, and testing before you build it.
```

### 98. D5_s983688_en (domain=D5, difficulty=6)

```
Build a from-scratch Python tool for debugging and log analysis that tails Docker/container logs, detects common failure patterns in real time, and outputs a concise incident summary plus remediation hints. Put the code in `logwatcher.py`, add tests in `tests/test_logwatcher.py`, and include a short `README.md` with install/run examples.
```

### 99. D5_s983954_en (domain=D5, difficulty=6)

```
Build a from-scratch Python tool that ingests raw application logs from stdin, detects error bursts and probable root causes, and prints both a concise terminal summary and a JSON report. Include a CLI in `main.py`, core parsing/anomaly logic in `log_analyzer.py`, and tests in `tests/test_log_analyzer.py`; also add a short `README.md` with usage and assumptions.
```

### 100. D5_s984110_en (domain=D5, difficulty=6)

```
Build a fresh log-triage tool for our Node.js services: create the code for a CLI that ingests raw text logs from stdin, detects error clusters, and prints a concise incident summary with probable root-cause hints. Make it from scratch, include a small test suite, and add a README with install/run examples; no input files, just code and docs.
```

### 101. D5_s984348_en (domain=D5, difficulty=6)

```
Build a from-scratch Python tool that tails application logs, detects common failure patterns, and outputs a concise incident summary plus suggested next steps. I want `logdoctor.py` and `README.md`, with a CLI that can read from stdin or a file, support regex-based rules, and print JSON and human-readable modes.
```

### 102. D5_s984464_en (domain=D5, difficulty=6)

```
I want a small but realistic debugging/log-analysis utility built from scratch for our engineering workflow.
- Make it a command-line tool that can ingest app logs from stdin or a file and flag likely root causes from common patterns like retries, timeouts, rate limits, and deploy regressions.
- Use current best practices for parsing and terminal output, and check the latest docs for a few Python libraries or standard-library options before you code.
- Include a compact test suite with realistic synthetic log cases, plus a README that explains usage and how to extend the rule set.
- Keep it practical: I want the built code files, not a mockup or pseudocode, and it should run locally without any external services.
- If there are tradeoffs between libraries or approaches, document the choice briefly in comments or the README.
```

### 103. D5_s984654_en (domain=D5, difficulty=6)

```
We need a small internal tool that helps our support team make sense of messy application logs when customers report incidents, because right now people are copying snippets into chat and we lose time figuring out what happened. Build a from-scratch command-line log triage utility in Python that can take pasted log text from stdin or a string argument, detect likely error patterns, group related lines into incidents, and output a clean summary with timestamps, severity, probable root-cause hints, and a short timeline. Please research a sensible approach to parsing and classifying logs with standard Python libraries or lightweight packages, then implement the tool, tests, and a short README explaining how to use it. I do not have any files to start from, so please create everything needed yourself and make it work as a real, runnable utility.
```

### 104. D7_s982048_en (domain=D7, difficulty=6)

```
Build a from-scratch incident workflow CLI in Python: `incidentctl` with commands for create, update, timeline, and postmortem draft. It should store incidents locally in SQLite, generate a Markdown postmortem template, and support exporting a Slack-ready incident summary. Put the code in `incidentctl.py` and the usage docs in `README.md`.
```

### 105. D7_s983319_en (domain=D7, difficulty=6)

```
Build a small Python service from scratch for incident automation: it should accept a raw incident timeline and produce a postmortem draft plus a Slack-ready incident summary. I want the code in `app.py`, `postmortem.py`, `templates/`, and `tests/`, plus a short `README.md` with setup and usage. Use current best-practice guidance for incident response/postmortems and any relevant Python libraries you need.
```

### 106. D7_s983554_en (domain=D7, difficulty=6)

```
Build a small but real incident-ops automation tool from scratch for a modern SRE workflow. I want a working Python project that can generate consistent incident timelines, draft a postmortem skeleton, and kick off follow-up tasks from a simple incident event payload.

- Use current best practices from public docs for at least one incident or workflow API, and cite the sources you used in the README.
- Build the core logic, a CLI, and a small HTTP API so I can feed in incident events and get a structured timeline/postmortem plan back.
- Include support for severity levels, owner assignment, timestamps, and action-item extraction from free-text notes.
- Add tests for the parsing and workflow logic, plus a clear README with setup and example usage.
- Keep it self-contained: no input files, no starter dataset, just code and docs I can run locally.
```

### 107. D11_s982256_zh (domain=D11, difficulty=7)

```
帮我从零做一个财务运营的小工具，重点是预算偏差和发票/报销异常处理，要求能直接落地给财务团队用。

- 做一个可运行的命令行工具或轻量服务，用来录入预算、实际支出、发票和报销申请，并自动标记异常。
- 异常规则要支持几类常见场景：超预算、同一供应商重复报销、发票金额与申请金额不一致、缺少必填字段、日期超出周期。
- 需要把规则设计成可配置的，不要把逻辑写死在一个函数里；最好能支持以后继续扩展。
- 顺手补一份简短的使用说明和示例交互，说明怎么安装、怎么运行、怎么加新规则。
- 最后把代码、测试和说明文档都整理好，我希望拿到的是一套完整的项目文件，而不是一段示例代码。
```

### 108. D11_s982269_zh (domain=D11, difficulty=7)

```
帮我从零做一个用于财务运营的“预算偏差 + 发票/费用异常”小工具，目标是让财务和业务运营同事能快速识别异常并生成可执行的处理清单。

- 做一个可运行的命令行工具，支持导入我之后手动提供的 CSV/JSON 交易数据，输出预算偏差分析、异常发票/报销标记和汇总报告。
- 规则要能配置，比如预算阈值、重复发票识别、超标准费用、缺失字段、拆单嫌疑、供应商白名单/黑名单等。
- 需要有一个清晰的报告格式：控制台摘要 + 结果文件（Markdown 或 HTML 都可以），里面要列出异常原因、影响金额、建议后续动作。
- 顺手把代码结构、使用说明、示例配置、以及最少一套自动化测试一起补齐，方便后面直接接到内部流程里。
- 另外帮我参考一下目前常见的 Python 数据校验/命令行/报表库，选一个合适的技术方案再开始写，不要直接拍脑袋实现。
```

### 109. D11_s982296_zh (domain=D11, difficulty=7)

```
帮我从零做一个预算偏差和发票/报销异常处理的小工具，代码要直接能跑，优先给 Python 实现。我要你同时产出一个可用的命令行程序和一套单元测试，文件名你自己定，但要把核心规则、异常分类、阈值配置都写清楚。先查一下常见费用管理/发票校验的最佳实践和相关 Python 库，再开始实现，不要用任何现成模板或示例数据文件。
```

### 110. D11_s982304_zh (domain=D11, difficulty=7)

```
我要从零做一个给财务运营团队用的轻量工具，解决预算偏差和发票/报销异常的日常处理。

- 用 Python 做成一个可运行的命令行工具，能录入预算、实际支出、发票和报销单，自动找出超预算、重复报销、税率/金额不一致、缺字段等异常。
- 设计一套清晰的数据模型和规则引擎，支持后续扩展不同部门、不同审批阈值和不同异常规则。
- 需要把结果输出成可读的摘要报告，最好同时有 JSON/CSV 风格的导出接口，方便接到后续系统里。
- 你先做一次必要的网页调研，看看 Python 里适合做命令行参数、表格输出、数据校验和测试的主流库，以及财务异常检测/内控方面常见的实现做法。
- 最后给我完整代码、README 和测试，保证我克隆后可以直接跑起来。
```

### 111. D11_s982308_zh (domain=D11, difficulty=7)

```
帮我从零写一个“预算偏差 + 发票/报销异常”审核工具，做成可运行的 Python 项目，核心代码、CLI、测试和 README 都要有。我要你先查一下常见费用报销/发票校验做法，再实现一个命令行工具，能根据我后面手工填的预算、实际支出和发票规则，自动标记超预算、重复报销、税率异常、抬头不一致、金额拆分规避审批这几类异常。
```

### 112. D11_s982320_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for finance ops that flags budget variance and invoice/expense exceptions, with a small FastAPI service and a CLI. I want the code in app/ plus a README.md, using current best-practice guidance for invoice validation, duplicate detection, and approval workflow patterns. No input files — generate a few sample scenarios in code and include tests.
```

### 113. D11_s982334_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for finance ops that flags invoice and expense exceptions and explains budget variances. I need a small CLI plus a reusable library: src/exception_detector.py, src/variance_explainer.py, and a README.md with setup and usage. Use current best-practice research for Python libraries and any relevant finance-ops workflows, but do not rely on any input files; generate all sample data and rules in code.
```

### 114. D11_s982344_en (domain=D11, difficulty=7)

```
Build a small finance ops tool from scratch for budget variance and invoice/expense exception handling. I need a web-backed research brief on best practices and a working Python app that flags overruns, duplicate invoices, missing PO links, and out-of-policy expenses, with a simple CLI and test suite. Put the code in app.py, tests in test_app.py, and include a README.md with setup and usage.
```

### 115. D11_s982368_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for finance ops that flags budget variance and invoice/expense exceptions, with a small CLI and a JSON report output. Use web research to pick current Python libraries and best-practice rules for OCR-free invoice validation, anomaly thresholds, and export formats, then implement the code in app.py, tests/, and README.md. No input files — generate sample data inside the tests and include a few realistic exception scenarios.
```

### 116. D11_s982375_en (domain=D11, difficulty=7)

```
We need a small internal tool for Finance Ops because we keep losing time on budget variance reviews and invoice/expense exceptions, and the team needs one place to see what needs follow-up before month end. Build it from scratch as a working code project, not a spreadsheet or analysis of any uploaded file. I want a simple web app where someone can enter budget lines, actuals, invoices, and expenses, then the tool flags exceptions like over-budget spend, missing approvals, duplicate-looking invoices, and unusual expense amounts, and gives a clear review list with reasons. Please include the code, a short README on how to run it, and basic tests. Use current best-practice libraries and patterns you find online so the setup is sensible and realistic for a small finance team.
```

### 117. D11_s982399_en (domain=D11, difficulty=7)

```
I need a small internal tool that helps us catch budget overruns and invoice/expense exceptions before they turn into month-end surprises. Please build it from scratch for a finance team: something we can use to compare planned spend against actuals, flag unusual invoices or expense claims, and produce a clear summary of what needs review. I want the code files and a short README so my team can run it themselves. Use current best practices for a simple web-based or command-line tool, and if you need to choose libraries or patterns, research what is sensible and lightweight for this kind of finance ops workflow.
```

### 118. D11_s982405_en (domain=D11, difficulty=7)

```
Build a small finance ops tool from scratch for budget variance and invoice/expense exceptions. I want a working Python service with a REST API, a rules engine for variance thresholds and duplicate/over-limit invoice flags, plus a CLI to run checks and export a summary report. Include tests and a README with setup and usage.
```

### 119. D11_s982408_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that helps AP/accounting teams review budget variance and flag invoice/expense exceptions before they hit approval. Make it a real code project with a clean CLI or simple local web app, plus a short README, and use web research to pick sensible libraries and follow current best practices for things like CSV/JSON handling, date parsing, and rule-based exception checks. The app should let me load transaction data, define budget lines and validation rules, run the checks, and export a summary of variances and exceptions for review.
```

### 120. D11_s982414_en (domain=D11, difficulty=7)

```
I need a small internal tool for Finance and Business Ops that helps us catch budget variance and invoice or expense exceptions faster, because right now the review process is too manual and issues are slipping through until month-end close. Build the tool from scratch so a reviewer can enter a department, budget, actual spend, invoice amount, vendor name, and a short note, then see whether it should be flagged, what kind of exception it is, and a plain-English explanation of why. I also want a simple way to export the results and a short README that explains how to run it and how the rules work. Please do the research you need first so the design follows current best practices for rule-based validation, basic finance controls, and a practical Python package or framework choice, then build the code and supporting files.
```

### 121. D11_s982438_en (domain=D11, difficulty=7)

```
We need a small internal tool to help Finance and Operations catch budget variances and invoice or expense exceptions before they hit month-end close. Please build it from scratch so our team can review exceptions in one place, flag anything over budget, and clearly show why an invoice or expense should be held, approved, or sent back. I want a working tool we can run locally, with the code files and a short README explaining how to use it. Please research a sensible approach first, including any lightweight libraries or patterns that fit a simple finance workflow, then implement the tool in a clean way without relying on any existing starter files or input data.
```

### 122. D11_s982460_en (domain=D11, difficulty=7)

```
I need you to build a small from-scratch finance ops tool that helps AP/FP&A teams flag budget variance and invoice/expense exceptions before they hit month-end close. Please design and implement the codebase, with a simple API or CLI plus a rules engine, so it can ingest basic transaction records, compare them to budget thresholds, and surface anomalies like duplicate invoices, missing cost centers, out-of-policy spend, and large variances with human-readable reasons. Use web research to pick a practical stack and any useful validation/formatting libraries, then put the finished code and README together.
```

### 123. D11_s982475_en (domain=D11, difficulty=7)

```
Build a small finance-ops tool from scratch that helps our team catch budget variance and invoice/expense exceptions before they hit accounting. I want a working codebase, not a mockup.

- Create a rule-based engine that flags suspicious invoices and expenses against configurable policy thresholds, vendor limits, and department budgets.
- Include a simple API or CLI for loading records, running checks, and exporting an exceptions report.
- Add clear tests for the core validation logic, especially around duplicate invoices, out-of-policy spend, and budget overages.
- Use current best practices and a sensible library stack for Python/service design, so please research the right approach before coding.
- Ship concise docs showing how to run it locally and how to extend the rules later.
```

### 124. D11_s982480_zh (domain=D11, difficulty=7)

```
帮我从零做一个预算差异和发票/费用异常处理的小工具，先用 Web 查一下业界常见做法和可用的 Python 库，然后直接实现成可运行代码。我要你交付 `app.py`、`exceptions.py`、`rules.py`、`README.md` 和 `tests/`，支持我手工录入预算、发票、报销记录后自动标出超预算、重复报销、缺少审批、税率异常和币种不一致，并给出可解释的原因。
```

### 125. D11_s982495_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch for budget variance and invoice/expense exceptions: something that lets a user define cost centers, monthly budgets, and imported transactions, then flags over-budget items, missing approvals, duplicate invoices, out-of-policy expenses, and builds a clean exception report with basic drill-down. Please research a sensible stack and any useful libraries or patterns first, then implement the app code and README; no input files are provided, so create the data model and sample config yourself and make it runnable end to end.
```

### 126. D11_s982497_en (domain=D11, difficulty=7)

```
We need a small internal tool that helps Finance quickly spot budget overruns and invoice or expense exceptions before month-end close. I want something practical for our team to use, not a spreadsheet exercise: build a simple code-based tool from scratch that lets a user enter a budget amount, actual spend, invoice lines, and expense items, then flags cases like over-budget departments, duplicate invoices, missing approvals, out-of-policy expenses, and unusual spikes compared with recent spend. It should produce a clear summary for Finance Ops and export a review-ready report we can share with department managers. Please research the best lightweight way to build this, then create the code and any supporting files needed to run it and understand it.
```

### 127. D11_s982505_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for finance ops that detects invoice and expense exceptions and computes budget variance flags by department/vendor. I want a CLI plus a small library in app.py, with tests in tests/, and a README.md explaining setup and usage. Design it around current best-practice Python packages and a simple rules engine, not a data-analysis notebook.
```

### 128. D11_s982523_en (domain=D11, difficulty=7)

```
I need a small internal tool for finance ops that helps us catch budget variance and invoice/expense exceptions before they hit the ERP.
- Build it from scratch as a working Python app with a simple command-line workflow and a lightweight local storage layer.
- It should support creating rules for budget thresholds, duplicate invoices, missing PO checks, and out-of-policy expenses.
- I want a clear exception report view, plus the ability to export results for review.
- Use current best-practice libraries and patterns where appropriate, and make the structure easy to extend later.
- Include tests and enough documentation so another engineer can run it and understand the design.
```

### 129. D11_s982539_en (domain=D11, difficulty=7)

```
Build a small finance ops tool from scratch for invoice and expense exception handling. I want `app.py`, `exceptions.py`, `storage.py`, and `README.md` that implement a rule-based budget variance checker and an invoice/expense exception workflow with a local CLI and JSON output. Use current best practices/library choices from the web, then wire it up so I can run it locally and review flagged items, approvals, and audit history.
```

### 130. D11_s982545_en (domain=D11, difficulty=7)

```
We need a small internal tool for our finance team because invoice and expense exceptions are slowing month-end close and people are chasing the same issues in email. I want a from-scratch app that helps us flag budget variances, questionable invoices, and out-of-policy expenses, then gives a simple review queue with reasons and status so Finance, AP, and budget owners can work the exceptions in one place.

Please build the code for a lightweight web app or command-line app, whichever is more practical, but it should feel ready for a real business team to pilot. It should let us set up basic rules for common exceptions, create a few sample records inside the app itself, and show a clean summary of what needs review, what is approved, and what is blocked. If it makes sense, include an easy way to export the exceptions list for follow-up. Use current best practices for the stack you choose, and research any libraries or approaches you need before building. Deliver the code files and a short README explaining how to run it and what it does.
```

### 131. D11_s982564_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for budget variance and invoice/expense exception handling: generate a rules engine, a small REST API, and a CLI that flags anomalies, route exceptions, and exports review-ready summaries. Put the code in `app.py`, the tests in `test_app.py`, and a short setup/run guide in `README.md`.
```

### 132. D11_s982566_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch for budget variance and invoice/expense exceptions: a web app or CLI that lets an AP/FP&A user enter budgets, actuals, invoices, and employee expenses, then flags over-budget lines, duplicate or suspicious invoices, missing cost centers, and policy exceptions, with a clean summary report and exportable results. Please use current best practices and any relevant open-source libraries or API docs you need, but don’t rely on any input files — make the whole thing self-contained and ready to run.
```

### 133. D11_s982571_zh (domain=D11, difficulty=7)

```
想从零做一个给财务运营用的异常处理小工具，目标是帮团队快速抓出预算偏差、发票异常和报销异常，并能生成可直接给业务看的结果。
- 做成一个可本地运行的命令行工具，支持输入一段我自己写的交易/预算/报销样例数据，然后输出异常清单和汇总统计
- 需要有规则引擎：比如预算超支、同供应商重复发票、金额与审批级别不匹配、报销日期超窗、缺少必要字段这几类都要能识别
- 结果最好带一个简洁的 HTML 报告页，能按异常类型、部门、严重级别查看，并显示每条异常的原因
- 代码要从头写，附上清晰的 README 和测试，方便以后接到真实 ERP / AP 系统时扩展
- 先帮我把方案、代码结构和核心实现都设计好，尽量用现在常见、靠谱的 Python 工具链
```

### 134. D11_s982587_zh (domain=D11, difficulty=7)

```
帮我从零做一个预算偏差+发票/费用异常处理工具，先实现成一个可运行的 Python 3.11 小项目，代码放到 `app/`，测试放到 `tests/`，再补 `README.md` 和 `ARCHITECTURE.md`。我需要它支持：录入预算、实际支出、发票和报销单，自动算预算偏差、抓常见异常（重复报销、超预算、税号/币种不一致、缺少审批链），并提供一个命令行入口可以生成异常清单和汇总报告。要先调研一下现成的做法和相关库，再直接开写，不要给我空泛方案。 
```

### 135. D11_s982594_en (domain=D11, difficulty=7)

```
I need a small internal tool built from scratch because our finance team keeps losing time on budget variance checks and invoice/expense exceptions. The goal is to help managers quickly spot where a month’s spend is off plan, and to flag invoices or employee expenses that look wrong before they get approved.

Please build the code for a simple web app or command-line tool, with clear instructions to run it. It should let someone enter budgeted vs. actual numbers by category, show the biggest variances, and also review a batch of invoices or expenses for common exception patterns like duplicates, amounts over a threshold, missing approvals, odd dates, or mismatched vendor names. I do not have any source files to start from, so create the whole thing yourself.

Use your judgment on the best structure and libraries, but please research current best practices and any useful open-source options first so the design is sensible and realistic. I want the finished code, tests, and a short README that explains what it does and how to use it.
```

### 136. D11_s982611_zh (domain=D11, difficulty=7)

```
从零做一个可直接跑的预算异常与发票/费用例外处理工具，后端用 Python，输出代码到 app.py、tests/ 和 README.md。我要一个命令行工具：能录入预算、实际支出、发票与报销单，自动标记预算偏差、重复发票、超阈值审批、缺失税号/PO 等异常，并生成月度例外摘要。先调研并采用一个合适的 CLI/数据校验/表格输出方案，再把核心规则引擎、命令行、测试和文档一次做完。
```

### 137. D11_s982623_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for budget variance and invoice/expense exception handling. I want `app.py`, `budget_rules.py`, `exceptions.py`, `storage.py`, `cli.py`, and `README.md`, plus a small test suite; no input files, generate sample data in code. Use real web research for current Python libraries/patterns and include a clear CLI for creating budgets, flagging over-budget items, and routing invoice/expense exceptions.
```

### 138. D11_s982627_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that helps flag budget variances and invoice/expense exceptions for a monthly close workflow. Please research a sensible stack and any relevant library choices first, then deliver the code and a short README. The app should let someone define budget lines, load invoice or expense entries, compare actuals to budget, and flag issues like over-budget spend, duplicate-looking invoices, missing approvals, and out-of-policy expenses. Keep it practical for a real internal ops team, with a clean CLI or lightweight web API, validation, and a few example commands or requests in the docs.
```

### 139. D11_s982636_zh (domain=D11, difficulty=7)

```
帮我从零实现一个“预算差异 + 发票/报销异常”管理工具，直接输出可运行代码和 README。我要一个本地可运行的 Python 项目，包含规则引擎、异常分类、统计汇总和一个简单 CLI，文件名你自己定，但要结构清楚。
```

### 140. D11_s982639_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch for budget variance and invoice/expense exception handling. Make it a working codebase, not an analysis on a spreadsheet: I want a web-researched design and implementation that can ingest simple JSON records, flag over-budget spend and invoice anomalies, and generate a clean exception report with a CLI plus a tiny API. Please use current best practices and suitable open-source libraries you verify online, then give me the finished code and README.
```

### 141. D11_s982652_zh (domain=D11, difficulty=7)

```
我需要你从零做一个给财务运营用的预算差异和发票/费用异常处理小工具，最好做成一个可运行的后端服务加一个简单命令行入口：能创建预算、录入实际支出、自动标记超预算和重复发票/异常报销，支持按部门和月份出汇总，还要把规则、API 说明和示例都写清楚；这个任务里没有现成数据文件，代码、测试和文档都要你自己搭起来，顺便帮我查一下适合这种场景的 Python 库、FastAPI/SQLite 的最佳实践，以及常见的费用异常规则怎么设计。
```

### 142. D11_s982664_zh (domain=D11, difficulty=7)

```
我需要你从零搭一个面向财务运营的“预算偏差 + 发票/报销异常”小工具，最好做成一个可直接运行的 Web 应用或命令行工具，支持手工录入预算、实际支出、发票和费用报销记录，然后自动识别超预算、重复报销、金额不一致、缺失审批、异常供应商这类情况，给出简洁的异常清单、原因说明和处理建议；同时帮我把代码、测试和 README 都写好，能本地启动。
```

### 143. D11_s982683_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for finance ops that ingests invoices, expenses, and monthly budget plans, then flags budget variances and exception cases with a rules engine. I want `app.py`, `rules.py`, `schemas.py`, `tests/`, and a `README.md` with setup and usage, plus a small CLI for running checks and exporting exception summaries. Research current best-practice libraries for CLI, validation, and report output before coding.
```

### 144. D11_s982689_en (domain=D11, difficulty=7)

```
We need a small internal tool because our finance team is wasting time chasing budget overruns and messy invoice or expense exceptions by email. I want a from-scratch web app that lets us flag a transaction, classify the reason, assign it to the right owner, and track whether it was resolved, so managers can see what is driving variance and what is still open.

Please build the code for a simple but real-budget variance and exception handling tool for Finance & Business Ops. It should let us create exception cases manually, list them, filter by status and department, add notes, change ownership, and show a basic dashboard of open exceptions, aging, and top reasons. I also want an export option for a clean CSV of the current cases, plus a short README that explains how to run it locally.

Use current best practices for the stack and any libraries you think fit, but please research a sensible modern approach before coding. There are no input files; everything should be built from scratch, with sample records generated in the app so it feels realistic. Deliver the code files and README, not just an explanation.
```

### 145. D11_s982691_en (domain=D11, difficulty=7)

```
Build me a small finance ops tool from scratch that helps me flag invoice and expense exceptions before they hit month-end close.

- I want a runnable app with a simple CLI or local web UI, plus the core logic for spotting budget variances and suspicious invoices/expenses.
- Include a few practical exception rules I can toggle on/off, like duplicate invoice detection, threshold-based budget overruns, missing PO checks, and merchant/category anomalies.
- Please use current best practices or widely used libraries where it makes sense, and do a quick web-backed design check on comparable tools, invoice data formats, and any relevant Python/TypeScript libraries before building.
- Add tests and a short README so someone on finance ops could install it, run it, and understand the outputs.
- No input files are provided; build it to work with sample records created in code or entered interactively.
```

### 146. D11_s982698_zh (domain=D11, difficulty=7)

```
请你从零做一个面向财务运营的异常处理小工具，最好能直接跑起来：要有一个用于预算偏差、发票/报销异常的规则引擎和一个小型 Web 界面或 CLI，能让用户手动录入一笔费用/发票记录后立刻看到是否命中异常、异常原因和建议下一步处理；同时把常见规则做成可配置的 JSON/YAML，支持阈值、重复报销、超预算、缺少审批、发票抬头不一致这几类场景。代码、测试、README 都一起给我，最好再补一个简短的设计说明，说明你参考了哪些现成做法和库。不要依赖任何输入文件，直接从代码里构建出来就行。
```

### 147. D11_s982699_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variances and invoice/expense exceptions, with a simple API or CLI plus a clean README. Use current web research to pick the right libraries and check best practices for parsing, validation, and report generation, then implement the code and tests so it can ingest sample budget, invoice, and expense records, compare them against rules, and output exception summaries for finance review. No input files are provided — please create the structure, logic, and example data in the codebase yourself.
```

### 148. D11_s982707_en (domain=D11, difficulty=7)

```
Build a small from-scratch budget variance and invoice exception review tool for finance ops: generate the code for a CLI and a lightweight web dashboard that lets users create budget lines, enter invoice/expense records, flag over-budget items, and route exceptions for approval with comments. Put the main app in app.py, shared logic in finance_ops.py, tests in tests/, and a README.md with setup and usage.
```

### 149. D11_s982719_en (domain=D11, difficulty=7)

```
Build a small finance ops tool from scratch for budget variance and invoice/expense exceptions. I want a Python app with CLI plus a simple FastAPI service, using a rules engine to flag over-budget spend, duplicate invoices, missing PO references, and out-of-policy expense lines. Add a clear README, tests, and a few example scenarios in code — no input files, just implement the feature set cleanly.
```

### 150. D11_s982745_en (domain=D11, difficulty=7)

```
Build a small Python service from scratch for budget variance and invoice/expense exception handling. I want the core engine, a FastAPI API, and a CLI in separate files, plus tests and a README. Use current best-practice docs for FastAPI/Pydantic/SQLite patterns and any relevant finance ops reference material you need.
```

### 151. D11_s982748_zh (domain=D11, difficulty=7)

```
我需要你从零写一个面向财务运营的异常处理工具，场景是预算差异和发票/报销异常：做成一个可运行的 Python 项目，能让财务人员输入一笔费用或发票记录后，自动判断是否超预算、是否重复报销、是否缺少必填字段，并把结果按规则输出成可读报告和告警清单；同时给我一个命令行入口、配置文件样例、单元测试和 README。实现前先查一下业界常见做法、相关 Python 库和财务控制最佳实践，再把代码、测试和文档一起搭好，不要用现成模板或示例数据，直接从零开始做。
```

### 152. D11_s982771_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variance and invoice/expense exceptions for monthly close. Please make it a real code project, not a data analysis, with a simple web or CLI interface, a rules engine for exception detection, and a clean README. Use web research to pick a practical stack and check a couple of current libraries or patterns before coding, then produce the finished files and tests.
```

### 153. D11_s982794_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that helps AP/FP&A teams track budget variance and flag invoice/expense exceptions, with a simple web API plus a command-line way to run it locally. Please research a few current Python libraries and API patterns first, then implement the code, tests, and a short README so I can use it to load sample transactions, compare them to budget rules, and generate exception reports for over-budget spend, duplicate invoices, missing PO numbers, and out-of-policy expenses. No input files are provided — just create the app, sample fixtures, and the docs from scratch.
```

### 154. D11_s982800_en (domain=D11, difficulty=7)

```
I want a small but realistic internal tool for finance ops that flags budget variance and invoice/expense exceptions before they hit month-end close.
- Build it from scratch as a working code project, not a notebook or analysis on sample files.
- Use current web research to choose a practical stack and any relevant library/API patterns for CSV parsing, rules/config handling, and generating exception reports.
- Include the core rules engine, a simple CLI, and a clean way to define thresholds and exception categories in config.
- Add a lightweight HTML or Markdown report output that summarizes variances, duplicate invoices, missing PO references, and suspicious expense patterns.
- Package it with tests and a README so another analyst could run it locally and adapt the rules.
```

### 155. D11_s982806_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variances and invoice/expense exceptions for a monthly close workflow. Make it a working Python app with a simple API or CLI, plus tests and a README, and use web research to pick a sensible stack and any best-practice patterns for rules, validation, and reporting. There are no input files for this — just create the codebase, define the data shapes, and make the tool able to ingest sample records, detect exceptions, summarize variance reasons, and export a clean report for finance reviewers.
```

### 156. D11_s982809_zh (domain=D11, difficulty=7)

```
我现在需要把财务运营里“预算偏差 + 发票/费用异常”这件事做成一个可落地的内部工具，因为我们每个月都在人工追催：预算超支、重复报销、缺少审批、金额和供应商不一致，这些问题发现得太晚，处理也太分散。我要你从零开始做一个小型可用的代码工具，最好能帮我们把这些异常规则先固化下来，后面财务和业务都能直接用。

请你先帮我做一版完整的实现方案并直接把代码文件建出来，不要用现成模板凑数。这个工具最好支持：
1）录入预算、部门、项目、发票/费用记录；
2）自动检查预算偏差和常见异常；
3）输出一份清楚的异常清单和汇总；
4）能在命令行里直接运行，后面方便我们接到内部系统里。

我不提供任何输入文件；请你自己设计数据结构、校验逻辑和展示方式。你可以参考现在常见的财务/报销系统做法，选合适的技术栈和实现方式，但要保证是从零开发出来的可运行版本。最后把你生成的代码文件和说明一起给我。
```

### 157. D11_s982831_zh (domain=D11, difficulty=7)

```
我需要你从零做一个财务运营的小工具，专门用来处理预算偏差、发票/报销异常的规则校验和预警，最好做成一个可本地运行的命令行加一个简单 API 的 Python 项目，顺手把 README、测试和示例配置也一起补齐。这个工具要能让我们自己配置阈值、异常类型、审批链和提醒规则，输入直接写在代码里的示例数据就行，不要依赖外部文件数据；你先把实现和项目文件都搭好，再说明怎么运行和怎么扩展。
```

### 158. D11_s982845_zh (domain=D11, difficulty=7)

```
我们现在每个月都要手工盯预算偏差、发票异常和员工报销异常，靠表格和邮件来回核对，太慢也容易漏掉问题。我想从零做一个小工具，帮助财务和业务运营在收到一笔费用或发票后，自动判断它是不是有问题，并把可疑项按优先级列出来，方便团队先处理最影响现金流和合规的部分。

请你直接帮我设计并写出这个工具的代码方案，最好是一个可以本地运行的命令行小应用，或者一个很轻量的 Web 小页面也可以。它至少要支持：录入一笔费用/发票/预算申请的基本信息，自动做几类常见检查，比如超预算、重复报销、供应商信息不完整、金额与政策不一致、审批链缺失、日期异常，然后输出一个清楚的异常结果和建议下一步处理动作。我要的是从头写出来的成品代码和必要的说明，不是分析现成数据。

如果你觉得有必要，请先查一下现在常见的做法、适合的开源库、以及财务异常规则引擎/校验框架怎么搭会更稳妥，再开始实现。最后请把代码、测试和运行说明一起给我。
```

### 159. D11_s982846_en (domain=D11, difficulty=7)

```
We need a small internal tool because our monthly budget reviews are slowing down and we keep missing invoice and expense issues until they hit the close process. Build a lightweight finance ops app from scratch that lets our team enter a budget, record actual spend, and flag variances and exceptions like duplicate invoices, over-budget lines, missing PO numbers, and expenses above policy limits. I want the code and a short README so we can run it locally and see a simple working demo. Please research the best-fit stack and any useful libraries first, then build the app cleanly with sensible defaults, validation, and basic tests.
```

### 160. D11_s982878_zh (domain=D11, difficulty=7)

```
我需要你从零做一个给财务运营用的“预算偏差 + 发票/费用异常”小工具，最好做成可直接跑的 Python 项目：能录入一批部门预算、实际支出和发票/报销记录，自动找出超预算、重复报销、供应商名称不一致、金额接近审批阈值这些异常，并输出一个可读的报告和一个简单的命令行界面；项目里顺手把规则配置、测试和 README 也一起补齐，我要的是完整可交付的代码文件，不是分析现成数据。 
```

### 161. D11_s982880_zh (domain=D11, difficulty=7)

```
我需要你从零做一个用于财务和业务运营的轻量工具，专门处理预算偏差、发票/报销异常和审批提醒：做成一个可运行的后端服务，带一个最小命令行入口或简单API，支持录入预算、费用、发票和审批规则，自动识别超预算、重复报销、缺少凭证、供应商/成本中心不匹配这几类异常，并输出一份可读的异常清单和汇总报表；同时把项目结构、安装运行方式、接口说明和测试都补齐。
```

### 162. D11_s982889_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool called `expense_variance_guard` that flags budget variance and invoice/expense exceptions for AP and finance ops. I want `app.py`, `variance_engine.py`, `exceptions.py`, `cli.py`, `tests/`, and a short `README.md` with setup/run examples. Use current web research for best-practice checks and any relevant Python libraries/APIs, then implement the whole thing with no starter data or input files.
```

### 163. D11_s982891_en (domain=D11, difficulty=7)

```
I need you to build a small finance-ops tool from scratch that flags budget variance and invoice/expense exceptions for a monthly close workflow. It should include the code, a simple CLI or API, tests, and a short README so a finance team can run it locally and see exceptions like over-budget spend, duplicate invoices, missing PO numbers, and out-of-policy expense claims. Please research current best-practice patterns for the libraries and approach before implementing, then produce the finished files.
```

### 164. D11_s982896_en (domain=D11, difficulty=7)

```
Build a small finance-ops tool from scratch that helps AP/FP&A teams flag invoice and expense exceptions before they hit month-end close.

- I want a working app/service that can score uploaded transactions for common issues like duplicate invoices, split expense risk, missing PO reference, over-budget spend, and vendor mismatch.
- Please research a few current implementation options first so the design uses realistic libraries and best practices for validation, rule engines, and a simple web API/UI.
- The deliverable should be production-minded code with clear setup docs, not a demo notebook. No input files are provided; generate your own sample data and test cases in the repo.
- Include a rules-based core, an API or CLI for running checks, and a concise explanation of how finance users would interpret each exception.
- I also want tests that cover the main exception paths and a short README showing how to run it locally.
```

### 165. D11_s982906_en (domain=D11, difficulty=7)

```
We need a small internal tool because our month-end close is getting slowed down by budget surprises and invoice exceptions, and finance keeps having to chase people for explanations in email threads. I want a simple app built from scratch that lets us enter or paste budget line items, actual spend, and invoice/expense exceptions, then flags the items that look off, groups them by reason, and generates a clear summary for managers. Please build the code for the tool and include whatever files are needed so someone can run it locally and review the results. I do not have any input files to give you, so make sensible assumptions about the data entry and how the workflow should work, and lean on your own research for the best approach.
```

### 166. D11_s982919_en (domain=D11, difficulty=7)

```
Build a small internal finance ops tool from scratch for budget variance and invoice/expense exceptions handling.
- I want a working codebase that can ingest manually entered transaction records, compare them against budget lines, and flag overspend, duplicate invoices, missing PO, and out-of-policy expenses.
- Include a simple web API plus a basic UI or CLI so a finance analyst can review exceptions, add comments, and mark items as resolved.
- Use current best-practice libraries and patterns where helpful, and research a realistic approach for rules, data modeling, and lightweight persistence before coding.
- Please deliver the built code and a short README with setup, usage, and examples of the exception types it handles.
```

### 167. D11_s982943_en (domain=D11, difficulty=7)

```
Build a small from-scratch finance ops tool that helps a team review budget variances and invoice/expense exceptions before month-end close.
- I want a web-backed design pass first, then the actual code for the tool with no starter files.
- Make it work as a local app/CLI that can flag suspicious transactions, explain why they were flagged, and summarize budget vs. actuals by department.
- Use current best practices and realistic library choices by researching how teams handle rule-based exception detection, CSV import/export, and simple reporting.
- Include a clear README with setup, usage, and a few example workflows for AP/FP&A users.
- Add tests for the exception logic and the reporting outputs, and make sure the project is organized enough for a small finance ops team to extend.
```

### 168. D11_s982963_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that helps flag budget variance and invoice/expense exceptions for a mid-size team, with a simple API or CLI, clear README, and tests. It should let me define budgets by department or project, ingest manually entered transactions, compare actuals to budget, and flag things like duplicate invoices, out-of-policy expenses, and big month-over-month spikes; please also include the code files needed to run it and any docs the app needs.
```

### 169. D11_s982985_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for finance ops that flags budget variance and invoice/expense exceptions, with a small CLI and a clean HTML report. Research current best-practice rules for invoice validation, duplicate detection, and budget overrun thresholds, then implement the logic in the codebase with no starter data.
```

### 170. D11_s982987_en (domain=D11, difficulty=7)

```
I need you to build a small finance-ops tool from scratch that flags budget variance and invoice/expense exceptions for our AP team. Make it a working app with a simple API and command-line entry point, plus tests and a short README. It should support uploading raw invoice/expense records, compare them to a budget or policy config we define in code, and output exception reports with reasons like over-budget, duplicate invoice, missing PO, out-of-policy merchant, and suspicious rounding. Please research a few current Python libraries and best practices for validation, CLI/API structure, and testing before you implement it.
```

### 171. D11_s982997_en (domain=D11, difficulty=7)

```
Build a from-scratch invoice exception manager for finance ops in Python. I want `app.py`, `rules.py`, `storage.py`, `cli.py`, and `README.md` that handle invoice/expense exceptions like duplicate invoices, out-of-policy spend, missing PO, and budget variance alerts, with a small SQLite-backed workflow and a CLI to review/resolve cases. Use current web research for good practices and any useful library choices, then implement it cleanly with tests.
```

### 172. D11_s983042_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for our finance ops team that flags budget variance and invoice/expense exceptions across monthly close workflows. I want a small but production-shaped package with a rules engine for variance thresholds, duplicate invoice detection, policy checks for expenses, and a command-line interface that can ingest JSON payloads passed on stdin or as inline literals. Use current best practices and existing open-source patterns where relevant, but do the implementation from scratch. Please research and base the design on realistic accounting controls, common exception codes, and a sane CLI/library layout before coding. Deliver the built code plus a README that explains setup, usage, and the exception model.
```

### 173. D11_s983050_en (domain=D11, difficulty=7)

```
We need a small internal tool because finance keeps losing time chasing budget overruns and messy invoice/expense exceptions in different systems. I want you to build a simple from-scratch app that lets us flag variance issues, capture exception reasons, and produce a clear summary for month-end review. Please design and build the code for a lightweight web app or command-line tool that can create exception cases, categorize them, track status, and generate a clean report for Finance and Operations. Use current best practices and look up a sensible stack and libraries before you build it. I do not have any input files to give you, so please include sample data creation inside the app or tests. Deliver the code and a short README explaining how to run it.
```

### 174. D11_s983052_en (domain=D11, difficulty=7)

```
Build a small finance-ops tool from scratch that helps AP/FP&A teams catch and explain budget variances and invoice/expense exceptions before they hit month-end close.
- I want a usable command-line app with a simple rule engine for flagging over-budget spend, duplicate invoices, unusual expense patterns, and missing required fields.
- Please research current best practices and a couple of relevant open-source libraries/APIs for validation, CLI parsing, and report export, then choose a practical stack and justify it in the docs.
- The app should generate a concise exception report and a CSV/JSON export, plus a short README with install and usage examples.
- Include solid automated tests for the core rules and a few realistic edge cases, and make the code easy to extend with new checks later.
- No input files are provided; create the project structure and sample in-memory/demo data yourself so the tool can run end-to-end.
```

### 175. D11_s983056_zh (domain=D11, difficulty=7)

```
帮我从零写一个“预算偏差 + 发票/报销异常”小工具，代码放在 `app/`，再给一份 `README.md` 说明怎么跑。要求支持导入手工录入的预算、实际支出、发票和报销记录，自动标出超预算、重复发票、缺审批、金额不匹配、币种不一致这些异常，并输出一份可读的汇总报告。顺手查一下现在常用的实现方案/库/最佳实践，别用现成模板，自己搭出来。
```

### 176. D11_s983064_zh (domain=D11, difficulty=7)

```
请从零做一个用于财务运营的“预算偏差 + 发票/费用异常”小工具，目标是让财务团队能快速发现超预算、重复报销、缺失审批和供应商异常。
- 用 Python 从零实现一个可运行的命令行工具或轻量服务，不要依赖任何现成业务模板。
- 需要先调研一下适合的库/做法：比如金额处理、规则引擎、CSV/JSON 导入、命令行参数、报表输出和测试框架，尽量选成熟、轻量、易维护的方案。
- 功能上要支持预算汇总、预算实际对比、发票/费用异常规则检测、按部门/项目输出结果，并能生成可读的摘要报告。
- 希望你把核心计算、输入校验、异常规则、测试和使用说明都一并做好，代码要能直接运行。
- 如果你觉得有必要，可以顺手加一个简单的可扩展规则配置方式，方便后续再接更多异常类型。
```

### 177. D11_s983072_zh (domain=D11, difficulty=7)

```
我需要你从零开发一个给财务运营用的预算差异和发票/费用异常处理工具，做成一个可运行的命令行小项目，顺手带上一个简短的 README 和测试。这个工具要能让团队手动录入预算、实际支出、发票和报销单，自动找出超预算、重复报销、金额不一致、缺少审批这些异常，并输出一份可读的检查报告；另外希望你先查一下几个常见 Python 方案里怎么做命令行参数、表格输出、日期处理和规则校验更稳妥，再决定实现方式。最后直接把代码、测试和说明文档都给我，别用现成模板，自己搭出来。
```

### 178. D11_s983084_zh (domain=D11, difficulty=7)

```
我需要你从零搭一个用于财务和业务运营的“预算偏差 + 发票/费用异常”小工具，给财务团队做日常排查用，不要依赖任何输入文件，直接把代码和说明文档一起写出来。工具要能手动录入预算、实际支出、发票与报销记录，然后自动标出超预算、重复报销、异常日期、供应商信息不一致、税率/金额不匹配这些常见问题；最好做成一个可以本地跑的 Web 服务或命令行程序，带基础测试和 README，方便我后面接到公司内部系统里。
```

### 179. D11_s983085_en (domain=D11, difficulty=7)

```
We keep getting budget surprises because invoice mismatches and expense exceptions are only caught late, and I want a small internal tool built from scratch to help the finance team catch them earlier. Please create a simple but real budget-variance and invoice/expense exception checker that can be used by our ops team to flag issues, explain why something was flagged in plain English, and export a clean review list we can send to managers. I do not have any input files to give you, so please build the tool, sample rules, and a few demo records yourself. I want the code and a short README that shows how to run it and what it does. Please use up-to-date best practices and check a few current Python libraries or approaches before building so the design is sensible for a real team.
```

### 180. D11_s983089_en (domain=D11, difficulty=7)

```
I want you to build a small finance operations tool from scratch for budget variance and invoice/expense exception handling. I am not giving you any input files; instead, I want the codebase itself to define the data model, business rules, and a usable workflow. The core idea is a lightweight internal app that finance operations teams could use to review spend against budget, flag exceptions, and generate an approval-ready summary.

Please design and implement a realistic solution that includes both the calculation engine and a usable interface. I want the application to support these business concepts precisely:

- A budget is defined by cost center, fiscal month, and category.
- An actual spend item is an invoice or expense line with an amount, vendor/payee, date, category, cost center, and optional invoice ID.
- Variance is actual minus budget for the same cost center/month/category combination.
- Overspend exception: actual exceeds budget by more than 5% or by more than a fixed threshold of 500 in currency units, whichever is lower in absolute terms? No — use this exact rule: flag if actual is greater than budget + max(500, 5% of budget). Treat a zero-budget line as automatically exceptional if actual > 0.
- Missing coding exception: flag any spend item that has an empty cost center or category.
- Duplicate invoice exception: flag any two spend items with the same invoice ID and vendor/payee, unless one is explicitly marked as a reversal/credit memo and the net amount becomes zero.
- Date exception: flag any spend item dated outside the fiscal month it is assigned to.
- Budget coverage rule: when multiple spend items map to the same budget line, the tool should aggregate them before comparing to budget.
- Exception severity should be tiered: critical for duplicate invoice and missing coding, high for overspend, medium for date mismatch, low for variance within 5% of budget but nonzero.

I want the implementation to include a small data store layer using either SQLite or a simple JSON-backed repository, but the app should be able to run without external services. I need a clear separation between domain logic, persistence, and presentation.

The interface should be practical for finance ops work. At minimum, provide a CLI that can:

- create or load a budget set,
- ingest spend items entered in code or via a simple structured JSON string passed on the command line,
- compute budget variance and exceptions,
- print a concise summary by cost center and category,
- print a detailed exception report sorted by severity then amount descending,
- export the result as JSON.

If a web API is a better design choice, include it too, but the CLI is mandatory. I also want tests that cover the key rule logic and the main CLI paths.

Before coding, do web research on current best practices for lightweight finance data modeling, CLI structure, and any standard libraries you would reasonably choose for this build in the target language, then implement the system from scratch based on that research. Do not use a starter project or input files; define the sample budget/spend data in the code or accept it as inline JSON only.
```

### 181. D11_s983105_zh (domain=D11, difficulty=7)

```
帮我从零写一个“预算偏差 + 发票/报销异常”小工具，输出代码和 README，做成一个可本地运行的 Python 服务。我要它支持：导入/录入预算、实际花费、发票/报销单，自动算预算偏差、标记超预算/重复报销/缺少审批/税额异常，并提供一个简单的 API 和命令行入口。请顺手把目录结构、核心模块、测试和示例用法都补齐，别用现成模板直接拼。
```

### 182. D11_s983127_en (domain=D11, difficulty=7)

```
Build a small finance-ops exception engine from scratch for budget variance and invoice/expense approvals. I want a working Python app with a CLI and a simple FastAPI endpoint that flags over-budget spend, duplicate invoices, split transactions, missing PO references, and policy threshold breaches, plus a README and tests. Use current web research for the recommended libraries and any best-practice rules you need, then implement everything cleanly in code files.
```

### 183. D11_s983129_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for finance ops that flags budget variances and invoice/expense exceptions, with a CLI plus a small HTTP API. Put the core logic in budget_rules.py, the API in app.py, the CLI in cli.py, and tests in tests/. Make it support configurable thresholds, duplicate invoice detection, policy-based exception tagging, and a summary report export.
```

### 184. D11_s983144_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variance and invoice/expense exceptions for monthly close. Make it a real code project with a simple backend API and a command-line workflow, plus a short README so someone on finance ops can run it locally. Since there’s no input data file, generate your own sample records in code and make the logic handle things like over-budget spend, duplicate invoices, missing PO numbers, weekend expenses, and suspicious vendor names. Please do a bit of web research first on a sensible Python stack, any lightweight libraries for CLI/API validation, and common invoice/expense exception rules, then implement the app and tests.
```

### 185. D11_s983160_en (domain=D11, difficulty=7)

```
Build a small internal finance operations tool from scratch for budget variance and invoice/expense exception handling.
- I want a working app that lets a finance ops user enter budgets, actuals, invoices, and expense claims, then flags over-budget lines and common exception cases.
- Use current best practices and a modern, lightweight stack you research first; include a short design note on any libraries or patterns you choose.
- The app should support a simple UI or command-line workflow, plus exportable outputs for exception summaries.
- Include rules for things like duplicate invoice numbers, missing cost centers, amounts over approval limits, and budget variance thresholds.
- Ship the code, tests, and a README with setup/run instructions and a few example scenarios I can try manually.
```

### 186. D11_s983164_zh (domain=D11, difficulty=7)

```
帮我从零写一个用于财务运营的“预算偏差 + 发票/报销异常”小工具，做成可运行的 Python 项目，输出 `app.py`、`README.md` 和测试。要支持命令行录入规则、生成异常告警、按部门/供应商/项目汇总预算偏差，并能导出 Markdown 报告。
```

### 187. D11_s983170_zh (domain=D11, difficulty=7)

```
我们现在每个月都要手工处理预算偏差和发票/报销异常，邮件、Excel、审批记录分散在各处，财务和业务同学来回追问特别耗时间。我想从零做一个小工具，帮我们把这些异常先自动整理出来，减少人工排查。

请你直接帮我设计并写出这个工具的代码，最好能做成一个可运行的命令行程序，再附上简单说明文档。它要能让我输入一段预算和费用规则配置，然后自动生成异常清单，比如超预算、重复发票、金额不一致、缺少审批、费用类别不匹配这些情况；同时把结果按部门、项目、供应商分组，输出成一个清晰的报告。希望你先参考一下现在常见的开源做法和相关库，再从头实现，不要依赖现成的成品系统。

如果你觉得有必要，也可以顺手加上基本测试和示例用法，方便我们后面交给运营同事试用。
```

### 188. D11_s983220_zh (domain=D11, difficulty=7)

```
想做一个从零开始的内部财务运营小工具，重点解决预算偏差和发票/报销异常这两类问题。
- 做一个可运行的代码项目，最好包含一个轻量 Web 界面或命令行界面，能让财务/业务同事手动录入预算、实际支出、发票和报销记录。
- 需要支持常见异常识别：超预算、重复报销、缺少审批、币种/税率不一致、金额临界波动、供应商名称疑似重复等，并给出可解释的规则提示。
- 希望有一个简单的规则配置方式，方便后续按部门、成本中心、项目切换阈值和校验逻辑，不要写死在代码里。
- 最终请把核心代码、说明文档和测试一起交付出来，能本地运行，最好附上示例数据生成或示例输入方式，但不要依赖现成数据文件。
- 如果需要选技术栈，先基于现有生态和最佳实践做一下快速调研，再开始实现。
```

### 189. D11_s983221_en (domain=D11, difficulty=7)

```
I want you to build a small but realistic finance operations tool from scratch for budget variance and invoice/expense exceptions, without using any input files. The deliverable should be a working codebase that I can run locally, plus a short README that explains how to use it.

The tool should help a finance or accounting ops team review budget-to-actual variance and flag invoice/expense exceptions before they get paid or booked. I want it to be based on real-world best practices rather than a toy example, so please research current approaches and relevant libraries/APIs before implementing.

Please design and implement a command-line or lightweight local web app that does all of the following:

1) Budget variance logic
- Let me define a budget plan in code or via a simple JSON/YAML config embedded in the repo, with fields like cost center, department, month, budgeted amount, actual amount, and variance thresholds.
- Compute variance amount and variance percentage.
- Classify each variance into buckets such as under budget, within tolerance, or over budget exception.
- Support both absolute threshold and percentage threshold rules, because finance teams often care about both.
- Handle edge cases cleanly: zero budget, negative budget/credit memo scenarios, missing actuals, and rounding to two decimals.

2) Invoice/expense exception detection
- Build rule-based exception checks for invoice/expense items such as duplicate invoice numbers, amount exceeds approved budget, missing cost center, weekend submission, merchant outside allowed category, tax amount inconsistencies, and currency mismatch.
- Each exception should produce a clear reason code and human-readable explanation.
- The rule engine should be extensible so new checks can be added without rewriting the whole system.
- Include a severity model, at minimum low/medium/high, and explain how the severity is assigned.

3) Review queue and output
- Aggregate all flagged items into a review queue that can be sorted or filtered by severity, department, cost center, and exception type.
- Provide a summary dashboard view in text form if it is a CLI app, or a simple local HTML view if it is a web app.
- Show totals for flagged items, total over-budget amount, and counts by exception category.

4) Data model and usability
- Since there are no input files, create a realistic seed dataset directly in the code or as fixtures in the repository that simulates several departments and multiple months of activity.
- Include enough variety to exercise the edge cases above.
- Make the tool easy to extend with new budget lines, new vendors/merchants, and new rule checks.

5) Engineering expectations
- Research current Python/TypeScript/Node or similar libraries that would be appropriate for formatting output, validating data models, and testing, then pick one stack and implement it cleanly.
- I need the code to be organized into logical modules, not one giant file.
- Add tests for the core calculation logic and exception rules.
- Document any assumptions and any limitations clearly in the README.

Please keep this as a genuine build-from-scratch task, not a data analysis exercise. There are no input files to inspect, so the implementation should create its own sample data and focus on the tool itself.
```

### 190. D11_s983237_en (domain=D11, difficulty=7)

```
Build a small Python tool from scratch for finance ops that flags budget variance and invoice/expense exceptions, with a CLI and a reusable library. I want `app.py`, `exceptions.py`, `budget_rules.py`, `tests/`, and `README.md` wired up so I can run it locally and extend the rules later.

Use current web research to pick a practical stack and reference a few real accounting/AP rule patterns, then implement the checker, a simple report output, and tests.
```

### 191. D11_s983247_en (domain=D11, difficulty=7)

```
Build a small finance-ops exception engine from scratch: a Python service that flags budget variance anomalies plus invoice/expense exceptions, with a REST API, a CLI, and a rules config file. Research current best practices and libraries first, then implement the code and tests in `src/`, `tests/`, and `README.md` — no input data files, just synthetic examples generated in code.
```

### 192. D11_s983248_zh (domain=D11, difficulty=7)

```
帮我从零做一个预算偏差和发票/报销异常的规则引擎工具，直接产出代码文件和 README。我要一个可运行的 Python 项目：支持导入预算、实际支出、发票/报销记录，自动做预算偏差预警、重复报销、超标、缺票、异常备注分类，并生成汇总报告和明细导出。
```

### 193. D11_s983251_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variance and invoice/expense exceptions for a monthly close workflow. It should include the code, tests, and a short README, and I want it designed for a realistic workflow with configurable thresholds, duplicate invoice detection, missing PO checks, out-of-policy expense rules, and a simple summary view for finance managers. Please use web research where useful to choose a solid stack and any libraries or best practices, then implement the whole thing from scratch.
```

### 194. D11_s983284_zh (domain=D11, difficulty=7)

```
帮我从零做一个预算偏差与发票/费用异常处理工具，直接输出可运行代码和README。我要一个Python项目：支持录入预算、实际支出、发票和报销单，自动标记超预算、重复报销、缺少审批、币种不一致和阈值异常，并生成一页HTML/Markdown汇总报表。
```

### 195. D11_s983288_zh (domain=D11, difficulty=7)

```
我需要你从零做一个财务运营的小工具，专门处理预算偏差和发票/报销异常：做成一个可运行的 Python 项目，能生成一套模拟的企业预算与费用数据、自动识别超预算和异常单据、把结果汇总成一份 HTML 报告和命令行输出，最好还能支持按部门/成本中心筛选、导出 CSV，以及给每条异常打上原因标签。你先把项目代码、README 和测试都搭好，别用现成模板，尽量按现在常见的 Python 工具链来设计。
```

### 196. D11_s983301_en (domain=D11, difficulty=7)

```
I need a small finance operations tool built from scratch because our team keeps missing budget overruns and invoice issues until month-end, and that’s creating surprise spend and delayed approvals. Build a simple internal app that lets us enter budget lines, expense/invoice exceptions, and then flags cases where actuals are drifting too far from plan or where an invoice looks like it needs review. I want the code and a short README that explains how to run it and what it does. Please use a sensible stack, but research current best practices and a couple of good libraries first so the design is modern and practical. I do not have any input files to provide.
```

### 197. D11_s983308_zh (domain=D11, difficulty=7)

```
帮我从零做一个预算偏差和发票/费用异常处理的小工具，给财务运营用，要求有一个可运行的命令行程序和一份 README。功能要能录入预算、实际支出、发票/报销单，自动找出超预算、重复报销、金额不一致、缺字段这些异常，并输出汇总报表。代码里请顺手把规则、错误码、示例命令和测试都补齐，别依赖任何现成数据文件。
```

### 198. D11_s983320_zh (domain=D11, difficulty=7)

```
帮我从零写一个“预算偏差 + 发票/报销异常”处理工具，做成一个可运行的命令行小项目，重点是规则引擎、异常分类、告警摘要和测试。不要用现成模板；直接产出代码、README 和测试，文件名你自己定，但要能本地跑起来。
```

### 199. D11_s983321_en (domain=D11, difficulty=7)

```
Build a from-scratch budget-variance and invoice/expense-exception tool for Finance Ops: I want a small Python service with a rules engine that flags over-budget spend, duplicate invoices, missing PO matches, and stale approvals. Use the latest docs for a few realistic libraries/APIs you’d choose, then implement the app and wire a simple CLI plus JSON output in app.py and README.md.
```

### 200. D11_s983323_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that helps flag budget variance and invoice/expense exceptions for a monthly close workflow, with a simple command-line interface and a lightweight rules engine. Use current best practices and library docs you look up on the web for things like CLI structure, validation, and report formatting, but don’t rely on any input files or starter data — just create the code, tests, and README from scratch so I can run it against sample records I enter by hand.
```

### 201. D11_s983331_en (domain=D11, difficulty=7)

```
Build a small finance ops tool from scratch for budget variance and invoice/expense exceptions. I need src/, tests/, and a README.md for a Python CLI that ingests no sample data but can validate CSV/JSON inputs, flag over-budget spend, duplicate invoices, missing PO numbers, and out-of-policy expenses, then export a summary report. Research a couple of current Python libraries for CLI, validation, and report output before you code, and make the design fit real AP/FP&A workflows.
```

### 202. D11_s983364_zh (domain=D11, difficulty=7)

```
帮我从零做一个财务运营里的“预算偏差 + 发票/报销异常”检查工具，目标是给财务和业务运营团队日常用的，不是做数据分析报告。
- 用 Python 做一个可运行的命令行工具，能录入/读取我后面自己填的预算、实际花费、发票明细和报销单明细，并输出异常清单和汇总。
- 重点要支持几类常见异常：预算超支、同一供应商重复开票、发票金额和报销金额不一致、缺少审批/附件、日期跨期或明显不合理。
- 希望你先调研一下现在常用的开源库/最佳实践，比如命令行参数、数据校验、报表输出、单元测试这些怎么选更稳妥，然后直接把代码和说明文档搭好。
- 结果最好能直接运行，带一个清晰的 README，说明怎么输入样例数据、怎么跑检查、怎么读输出结果。
- 如果你觉得有必要，也可以顺手加一个简单的规则配置文件，让我后面能自己改阈值和异常规则。
```

### 203. D11_s983381_zh (domain=D11, difficulty=7)

```
帮我从零做一个预算差异和发票/费用异常处理的小工具，最好是可直接运行的 Python 项目，输出 app.py、README.md 和 tests/。我要它支持：导入一笔一笔的预算、实际支出、发票和报销记录，自动找出超预算、重复发票、金额不一致、缺少审批这几类异常，并生成一份可读的 HTML/Markdown 汇总报告。顺手查一下适合用的开源库和最佳实践，再把代码、测试和使用说明一起给我。
```

### 204. D11_s983403_en (domain=D11, difficulty=7)

```
Build a small Python service from scratch for finance ops: a budget-variance and invoice/expense exception engine with a REST API and CLI. I want the code in app.py, tests in tests/test_app.py, and a short README.md with setup/run steps. Include rules for flagging overspend, duplicate invoices, missing PO, out-of-policy expenses, and manager approval routing.
```

### 205. D11_s983404_zh (domain=D11, difficulty=7)

```
从零做一个本地可运行的财务异常处理工具，输出 `app.py`、`rules/` 和 `README.md`：支持导入发票/报销/预算差异的记录，按可配置规则识别重复报销、超预算、缺少审批、税码异常和供应商黑名单，并生成异常清单与汇总统计。先查一下 Python 里适合做规则引擎、CLI、JSON/YAML 配置和表格导出的成熟库，再把实现补全并附上最小可用测试。
```

### 206. D11_s983420_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that helps a team catch budget variance and invoice/expense exceptions before they hit the ERP. Make it a usable command-line app with a rule engine for flagging over-budget spend, duplicate invoices, missing PO numbers, and out-of-policy expenses, plus a simple report output so someone can review exceptions quickly. Please research the best-fit Python libraries and any relevant accounting/AP best practices first, then implement the code and tests from scratch with no starter files.
```

### 207. D11_s983424_en (domain=D11, difficulty=7)

```
Build a small internal finance-ops tool from scratch for budget variance review and invoice/expense exception handling.

- I want a working app that lets me create cost centers, monthly budgets, invoice/expense entries, and flag exceptions when spend is over budget or missing required fields.
- Include a simple rules engine for common finance checks like duplicate invoice number, missing PO, out-of-policy amount thresholds, and category-to-cost-center mismatches.
- Provide a CLI or lightweight web API for adding records, running variance checks, and exporting an exceptions report.
- Use current best-practice libraries and patterns for the chosen stack, and research a sensible approach to validation, persistence, and test structure before coding.
- Deliver the built code plus a short README explaining how to run it and how the exception logic works.
```

### 208. D11_s983430_en (domain=D11, difficulty=7)

```
I need you to build a small from-scratch finance ops tool that flags budget variances and invoice/expense exceptions for monthly close. Make it a real codebase, not a data analysis notebook: I want a working CLI or tiny service with clear rules for over-budget spend, duplicate invoices, missing PO references, out-of-policy expenses, and approval-chain gaps, plus a short README showing how to run it. Please do the design research with the web first so the rules and any library choices line up with common finance ops practice, then implement the code and tests from scratch.
```

### 209. D11_s983439_zh (domain=D11, difficulty=7)

```
帮我从零做一个预算偏差和发票/费用异常处理的小工具，最好是一个可运行的 Python 项目，核心逻辑、命令行入口、测试和 README 都补齐。要求它能录入预算、实际支出、发票/报销单，自动算偏差并把异常单据按规则分级、输出待处理清单。
```

### 210. D11_s983446_en (domain=D11, difficulty=7)

```
We need a small internal tool because finance keeps losing time on budget checks and invoice exceptions. I want something that can flag unusual spend, catch invoices that don’t line up with the expected budget or approval path, and explain the issue in plain English so operations can act on it quickly. Build the tool from scratch, with a simple web-based screen or command line if that’s easier, and include clear output for things like budget variance alerts, duplicate or suspicious invoices, missing approvals, and out-of-policy expenses. Please research good approaches and any useful libraries or API patterns before you build, then give me the finished code and a short README so my team can run it and understand how it works. There are no input files to start with, so create the logic, sample rules, and a way to enter test cases yourself.
```

### 211. D11_s983477_en (domain=D11, difficulty=7)

```
Build a small Python service from scratch for budget variance and invoice/expense exception handling. I want app.py, exception_rules.yaml, and README.md, with a simple API or CLI to flag over-budget lines, missing PO/invoice mismatches, duplicate expenses, and stale approvals. Use a real current library stack and best-practice patterns—check the web for a good rules-engine/library choice and modern FastAPI/Pydantic setup before coding.
```

### 212. D11_s983483_zh (domain=D11, difficulty=7)

```
我想从零做一个面向财务运营的小工具，专门处理预算偏差和发票/报销异常，先做一个可运行的命令行版本。
- 需要能录入预算、实际支出、发票和报销单，自动识别超预算、重复报销、金额不一致、缺少审批等异常。
- 希望有一个清晰的规则引擎，后续能方便加新规则；最好把规则配置和核心计算逻辑分开。
- 要提供命令行命令：导入一组示例交易、运行检查、输出异常汇总和按部门/项目的偏差报告。
- 需要写好测试，覆盖正常路径和典型异常场景，并给出 README，说明怎么安装、运行、扩展规则。
- 开发前请先查一下常见的 Python 库选择、CLI 设计和财务异常检测的最佳实践，然后直接把代码和文档搭起来。
```

### 213. D11_s983495_zh (domain=D11, difficulty=7)

```
帮我从零实现一个面向财务/业务运营的“预算偏差与发票/报销异常处理”小工具，最好是一个可直接跑起来的命令行或轻量 API 项目。

- 需要能录入/配置预算科目、预算周期、实际支出、发票金额、报销金额、审批状态等，并自动做预算偏差和异常检测
- 异常规则要支持可配置，比如超预算、同一供应商短期重复报销、发票金额和报销金额不一致、缺少审批、超阈值拆单等
- 希望给出一个可扩展的规则引擎设计，后续能方便加新规则，并把异常结果输出成结构化报告
- 需要带上测试、示例数据生成、以及一份简明的使用说明，能说明如何运行、如何新增规则、如何查看结果
- 如果有合适的开源库、最佳实践或类似工具设计，可以参考一下，但最终代码要从头写，不要用现成成品直接拼装
```

### 214. D11_s983505_en (domain=D11, difficulty=7)

```
We need a small internal tool because our month-end close keeps getting slowed down by invoice exceptions, missing receipts, and budget overruns that only show up after finance has already spent time chasing people. Build a from-scratch expense and invoice exception tracker for our ops team that can flag unusual items, show budget variance by department and project, and generate a simple review list for finance and managers. I do not have any input files for you — please design the whole thing yourself and build the code and whatever supporting files are needed. I want a practical solution that could be run locally by our team, with clear instructions, sensible defaults, and a way to add or review exceptions without needing a spreadsheet. Please research current best practices and any lightweight libraries or APIs that would make this easier, then implement the tool from scratch and include the finished code files and a short README.
```

### 215. D11_s983529_en (domain=D11, difficulty=7)

```
We need a small internal tool because our finance team keeps losing time reconciling budget overruns, duplicate invoices, and out-of-policy expenses by hand. I want a from-scratch app that lets us enter or paste budget lines, invoices, and expense claims, then flags exceptions like over-budget spend, duplicate invoice numbers, missing approvals, and receipts that do not match policy. Please build the code for it, not just a description, and make it something we can actually run locally. I’m happy for you to choose the best stack, but please research current good options first and use a simple setup that a business team could extend later. Include a short README so someone non-technical can understand how to run it and what it does.
```

### 216. D11_s983544_en (domain=D11, difficulty=7)

```
I need a small internal tool for finance ops to flag budget variance and invoice/expense exceptions before they hit month-end close.
- Build it from scratch as a working command-line app with a simple config file and generated sample data, since I don’t have any source files to provide.
- Include rules for over-budget spend, duplicate invoices, missing PO/reference fields, and suspicious merchant/amount patterns.
- Make it easy to run locally, explain how to configure thresholds, and include a few realistic example commands in the README.
- Use current web research to pick a practical implementation stack and any libraries or patterns that fit a lightweight finance workflow tool.
- Deliver the code, tests, and documentation, not just a concept writeup.
```

### 217. D11_s983553_en (domain=D11, difficulty=7)

```
I need a small internal tool for finance ops so our team can catch budget variances and invoice or expense exceptions faster instead of doing it all by hand in spreadsheets. Please build the code from scratch for a practical web app or command-line tool that lets someone set a budget by department and month, load invoices or expenses one at a time, flag anything that looks over budget or inconsistent, and produce a clear exception summary we can share with managers. I want it to be realistic for a finance team, with sensible statuses, notes, and review actions, and I need the final code and a short README so my team can run it and understand how to use it.
```

### 218. D11_s983578_en (domain=D11, difficulty=7)

```
We keep getting burned by budget surprises and invoice exceptions, and I want a small internal tool built from scratch that helps Finance Ops spot the issues before they turn into month-end problems. The tool should let us enter a department budget, actual spend, open commitments, and invoice/expense exception details, then flag the cases that need follow-up, explain why they were flagged in plain English, and export a simple review summary for managers. Please build the code and any supporting files needed to run it, with a clean way to add more rules later. Use current best practices and reasonable open-source libraries where helpful, but don’t rely on any sample data files — I want the app itself created from scratch.
```

### 219. D11_s983583_zh (domain=D11, difficulty=7)

```
帮我从零做一个预算差异与发票/费用异常处理的小工具，先输出可运行代码和 README，文件名你自己定。我要一个能接收手工输入的规则引擎 + 一个轻量 API/CLI，用来标记超预算、重复报销、缺票据、税率异常这几类问题，并生成可导出的异常清单。
```

### 220. D11_s983596_zh (domain=D11, difficulty=7)

```
帮我从零写一个“预算偏差 + 发票/费用异常”处理小工具，先调研 NetSuite、SAP Concur、QuickBooks 这类系统的常见异常字段和处理方式，再自己实现一个可跑的 Python 代码库。我要你直接产出 `app.py`、`rules.py`、`exceptions.py`、`README.md` 和 `tests/`，支持导入我后面会自己接的 JSON 记录，做规则校验、异常分类、汇总报表和命令行输出。
```

### 221. D11_s983620_zh (domain=D11, difficulty=7)

```
给我从零搭一个“预算偏差 + 发票/报销异常”的小工具，直接交付代码和 README。我要一个可运行的 Python 服务，能接收手工录入的预算、实际支出、发票/报销记录，自动标出超预算、重复报销、缺少审批、币种不一致和时间窗异常，并输出 JSON 报告。顺手把规则配置、命令行入口、单元测试和一个最小 API 都补齐，文件就按你觉得合理拆分。
```

### 222. D11_s983645_zh (domain=D11, difficulty=7)

```
帮我从零实现一个“预算偏差 + 发票/报销异常”处理小工具，做成可运行的 Python 项目，代码放在 app.py、exceptions.py、rules.py、cli.py、tests/ 里，顺手补一份 README.md。要支持预算对比、异常规则配置、发票/报销数据校验、导出异常清单和简单统计，别用现成模板，自己搭结构。
```

### 223. D11_s983669_en (domain=D11, difficulty=7)

```
Build a small Python service from scratch for invoice and expense exception handling. I need an API with rules for budget variance alerts, duplicate invoice detection, approval routing, and a simple HTML dashboard; put the code in app.py, tests in tests/test_app.py, and setup notes in README.md. Use current web research for the best-fit libraries and any relevant API patterns before you code.
```

### 224. D11_s983685_en (domain=D11, difficulty=7)

```
Our finance team keeps losing time on budget variance follow-ups and invoice/expense exceptions, and I want a small internal tool that helps us catch the most common problems early instead of sorting through them manually. Build a from-scratch app for our month-end ops workflow that can compare budget vs. actuals, flag unusual variances, and track invoice or expense items that look inconsistent or need review. I don’t have any files to give you, so please create the whole thing yourself with sensible sample data or demo records where needed. I want the actual code and a short README so our team can run it and understand how it works. Please use current best-practice guidance for the libraries and approach you choose, and make sure the result is practical for a real finance operations team.
```

### 225. D11_s983693_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for invoice and expense exception handling in finance ops: budget-variance detection, duplicate invoice checks, approval-rule validation, and a small CLI to review exceptions. Use current best practices and pick any solid libraries after checking docs online; no input files are provided, so include sample data generation and tests yourself. Deliver app code plus a README.
```

### 226. D11_s983697_en (domain=D11, difficulty=7)

```
I need a small internal tool we can use to flag budget variances and invoice or expense exceptions before they turn into month-end cleanup. Please build it from scratch so our finance team can enter a budget, log invoices or expenses, and immediately see anything that looks over budget, duplicated, outside policy, or missing approval. I want it to be practical for a real business ops workflow, not just a demo, and I need the code plus a short README that explains how to run it and how the exception checks work. Please research a sensible stack and any good practices for handling invoice/expense validation, then implement the tool cleanly.
```

### 227. D11_s983716_en (domain=D11, difficulty=7)

```
Build me a small finance ops tool from scratch for budget variance and invoice/expense exceptions. I want a working CLI + lightweight API in Python, with rules for flagging over-budget spend, duplicate invoices, missing PO/approver, and unusual expense spikes; include README.md and tests. Research current best practices for budget variance workflows and a couple of relevant Python libraries before you code, then wire it all together with no input files assumed.
```

### 228. D11_s983727_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch for budget variance and invoice/expense exceptions, with the code and a short README. It should let a team enter monthly budget vs actuals, flag overspend and unusual variance, track invoice/expense exceptions like duplicates, missing PO, and out-of-policy amounts, and export a clean exception report. Please use current web research for good Python libraries and any relevant accounting/expense-management best practices, then implement it as a working app with tests and clear setup instructions.
```

### 229. D11_s983745_zh (domain=D11, difficulty=7)

```
帮我从零写一个可直接跑的 Python 工具：做预算偏差和发票/报销异常检测，支持规则配置、生成汇总报告、导出异常清单。把代码放在 `app.py`、`rules.yaml`、`README.md` 和 `tests/` 里，顺手加一个命令行入口，能对示例数据跑通并输出结果。
```

### 230. D11_s983852_en (domain=D11, difficulty=7)

```
Build a small finance ops tool from scratch for budget variance and invoice/expense exception handling. I want the code in `app/` plus a `README.md` that explains setup and usage; no sample data files, generate your own fixtures in code. Include the core rules engine, a minimal API or CLI, and a short config format for thresholds, approval routing, and exception reasons.
```

### 231. D11_s983892_en (domain=D11, difficulty=7)

```
I need you to build a small finance-ops exception manager from scratch: a backend service plus a simple CLI or web UI that lets teams log budget variance cases and invoice/expense exceptions, route them through statuses, add notes, and export a clean report for finance review. Please use current best practices and a practical stack choice after checking modern library/docs options online, then deliver the code and README with setup/run instructions.
```

### 232. D11_s983953_en (domain=D11, difficulty=7)

```
We keep losing time every month on budget variance follow-up and invoice/expense exceptions, and I want a small internal tool that helps finance and ops spot problems early and route them to the right owner. Build it from scratch as a working code project, not a spreadsheet or analysis on existing files. I want a simple web app or command-line tool that lets someone enter a budget line, an actual spend, and an exception type, then shows a clear variance summary, flags likely issues, and tracks exception status through review, approved, rejected, or needs more info. It should also have a way to import a few sample records you create yourself for demo/testing, plus a short README explaining how to run it and what business problem it solves. Please use current best-practice libraries and patterns, and make sure the code is structured so we could extend it later for invoice and expense workflows, role-based review, and audit history.
```

### 233. D11_s983972_zh (domain=D11, difficulty=7)

```
帮我从零实现一个“预算偏差 + 发票/报销异常”小工具，输出完整代码和 README，文件名就按你设计来。我要它能录入预算、实际支出、发票/报销记录，自动识别超预算、重复报销、缺票、金额不一致这几类异常，并给出一页可运行的本地演示界面或命令行。
```

### 234. D11_s983986_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variances and invoice/expense exceptions for a monthly close workflow, with a clean CLI and a minimal local API or library interface. Please research a couple of current Python options for parsing CSV/JSON, CLI handling, and optional report output, then implement the code, tests, and README in separate files—no input data files, just the app itself and a few generated sample cases in tests or fixtures.
```

### 235. D11_s984022_zh (domain=D11, difficulty=7)

```
我需要你从零做一个用于财务运营的异常管理小工具，重点是预算偏差和发票/费用报销异常：做成一个可运行的 Python 项目，能让用户手动录入或通过接口传入预算、实际支出、发票和报销数据，然后自动识别超预算、重复报销、缺少审批、税率异常、金额拆分规避阈值这几类问题，并生成一份清晰的异常清单和汇总报告。你先帮我把项目代码、README 和测试都搭起来，顺便参考一些现成的做法和库选型，但不要依赖任何输入文件，全部功能都要从头实现。
```

### 236. D11_s984032_zh (domain=D11, difficulty=7)

```
帮我从零写一个预算差异与发票/费用异常处理工具，要求输出完整代码到 app.py、exceptions.py、rules.py、cli.py、tests/test_app.py 和 README.md。功能要支持：导入我手工在代码里定义的预算、实际发生和发票/报销记录，自动找出超预算、重复报销、缺少审批、供应商名称不一致、发票日期异常，并生成可导出的异常清单。
```

### 237. D11_s984059_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variance and invoice/expense exceptions for monthly close. Make it a real runnable app, not a mockup: a backend service with rules for over-budget spend, duplicate invoices, out-of-policy expenses, and missing approvals, plus a simple command-line or API interface to submit transactions and get exception results. Please use current best-practice patterns and relevant library choices after checking the web, and include the code, tests, and a short README showing how to run it.
```

### 238. D11_s984120_en (domain=D11, difficulty=7)

```
I need you to build a small Finance & Business Ops tool from scratch that flags budget variance and invoice/expense exceptions for a monthly close workflow. Please create the code, tests, and a short README for a local app that lets someone enter budget, actual spend, invoice, and expense records, then produces exception flags, variance summaries, and an exportable review queue for AP/FP&A follow-up. I don’t have any input files for you — design the data model and rules yourself, but make it realistic for a mid-sized company and use current best practices for how these checks should work.
```

### 239. D11_s984131_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variances and invoice/expense exceptions for a monthly close workflow, with a simple API plus CLI and a clean README. Please research a sensible stack and any relevant best practices first, then implement the code, tests, and docs so I can run it locally and use it with sample records I provide later.
```

### 240. D11_s984181_en (domain=D11, difficulty=7)

```
We’re spending too much time chasing down budget overruns and messy invoice or expense exceptions after the fact, and I want a small internal tool that helps us catch them earlier and explain them clearly to finance and department managers. Build a lightweight web app from scratch that lets a user enter a budget, actual spend, invoice details, and expense claims, then flags exceptions like over-budget lines, duplicate invoices, missing approval, date mismatches, and out-of-policy expenses. I want it to show a simple dashboard with the exception list, a plain-English reason for each flag, and a way to export the results as a CSV or JSON file. Please also include clear setup instructions and make the app easy to run locally.
```

### 241. D11_s984188_zh (domain=D11, difficulty=7)

```
帮我从零做一个“预算偏差 + 发票/报销异常”审查工具，直接产出代码，不要依赖任何输入数据文件。我要一个可运行的 Python 包，能根据我在代码里定义的预算、实际支出和发票记录，自动找出超预算、重复报销、缺少审批、税号/抬头不一致、金额拆分规避阈值等异常，并生成一份 HTML/Markdown 审核报告。顺手把命令行入口、单元测试和 README 也一起补齐，文件名你来定。
```

### 242. D11_s984223_zh (domain=D11, difficulty=7)

```
帮我从零写一个“发票/费用异常 + 预算差异”检查工具，做成可复用的 Python 包和一个命令行入口，文件就放在 `finance_ops/`、`tests/`、`README.md`。功能要能配置部门预算、规则阈值、发票/报销异常类型，并输出异常清单和汇总报表，先别接任何现成数据源。顺手把你查到的最佳实践整理进 README，代码、测试和示例都一起给我。
```

### 243. D11_s984284_en (domain=D11, difficulty=7)

```
Build a small internal finance ops tool from scratch for budget variance and invoice/expense exceptions. I want the code in app.py with supporting modules plus README.md, and make it support rule-based flagging for budget overruns, duplicate invoices, missing PO numbers, and suspicious expense categories. Use current docs/best practices for a lightweight Python stack and package it cleanly.
```

### 244. D11_s984289_en (domain=D11, difficulty=7)

```
We keep losing time on budget follow-up because invoice and expense exceptions are getting flagged too late, and managers only see the problem after the month is basically closed. I want a small internal tool built from scratch that helps finance and ops teams catch the common exceptions earlier and explain them clearly: budget variances, duplicate-looking invoices, missing approvals, out-of-policy expenses, and spend that needs manager review. Please build the code for a simple web app or internal tool that lets a user enter or paste invoice and expense details, runs the checks, and shows a clean exception summary with reasons and priority. I also want a short setup guide and a few realistic example scenarios so we can demo it to stakeholders. No input files from me — please create the tool and any sample data yourself.
```

### 245. D11_s984296_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for finance ops that flags budget variances and invoice/expense exceptions, with a small CLI and reusable library. I want the code in src/, tests/, and a README.md, and it should be designed around a realistic AP/FP&A workflow, not a toy demo.
```

### 246. D11_s984369_zh (domain=D11, difficulty=7)

```
帮我从零做一个 Python 工具，处理预算偏差和发票/报销异常：要能导入我以后接上的明细数据，自动标记超预算、重复发票、缺少审批、税额不一致和异常供应商。请直接产出代码文件、测试和 README，放到一个可运行的小项目里，顺手把规则配置和示例用法也写好。
```

### 247. D11_s984453_en (domain=D11, difficulty=7)

```
Build a small finance-ops exception engine from scratch: `budget_variance_alerts.py` plus `README.md`. It should ingest manually entered budget vs actuals and invoice/expense exception rules, then generate a clean exceptions report with configurable thresholds, reason codes, and CSV/JSON output.

Use web research to choose a sensible Python stack and validate best practices for CLI parsing, tabular output, and tests before you code.
```

### 248. D11_s984531_en (domain=D11, difficulty=7)

```
Build a small internal finance ops tool from scratch for budget variance and invoice/expense exceptions.

- I want a working app, not a spreadsheet or data analysis on files.
- Make it help a finance team flag overspend, duplicate invoices, out-of-policy expenses, and missing approval cases.
- Use current, real-world guidance or library/API research where it helps the design, then implement the feature set cleanly in code.
- Include a simple UI or API plus sensible validation, audit logging, and a clear way to review exceptions.
- Deliver the code and a short README so another engineer can run it and extend it.
```

### 249. D11_s984537_en (domain=D11, difficulty=7)

```
Build a from-scratch finance ops tool for budget-variance and invoice/expense exception triage. I want a small Python app with a CLI plus a lightweight FastAPI service, and a README that explains setup and usage; no input files, just implement the tool and its tests. Base the design on current best practices for invoice validation, duplicate detection, approval thresholds, and budget variance handling, using web research for APIs/libraries if needed.
```

### 250. D11_s984551_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch for budget variance and invoice/expense exception handling: a CLI app that lets a team upload or type in monthly budget and actual spend entries, flags variances above configurable thresholds, catches invoice/expense anomalies like duplicates, missing cost centers, out-of-policy amounts, and mismatched vendor names, and exports a clean exceptions report plus a summary dashboard file. Please research a couple of sensible implementation choices first so the design matches current best practices, then produce the code, tests, and a README for running it locally—no input files are provided, so the app should work with sample data you generate in code and with new records entered by the user.
```

### 251. D11_s984565_en (domain=D11, difficulty=7)

```
I need a small internal tool that helps Finance spot budget overruns and invoice or expense exceptions before they hit month-end close. We keep getting surprise variances because people are checking things manually, and I want a clean workflow that flags the problem cases, explains why they were flagged, and gives the team a simple way to review them. Build it from scratch as working code, with a simple interface and clear documentation, so we can use it as a prototype for our ops team. No input files are being provided — just create the tool and the sample data it needs yourself, and make sure it’s practical enough that a finance analyst could actually test it.
```

### 252. D11_s984692_zh (domain=D11, difficulty=7)

```
帮我从零做一个“预算偏差 + 发票/报销异常”审查工具，输出 `app.py`、`rules.py`、`README.md` 和 `tests/`。我要一个可运行的 Python CLI：支持输入预算和单据的 JSON 配置，自动算预算偏差、识别发票重复/拆单/超阈值/缺字段/日期异常，并生成一份审查报告。顺手调研一下常见的 Python CLI、数据校验和金额处理最佳实践，再按调研结果实现，不要依赖任何现成模板。
```

### 253. D11_s984736_zh (domain=D11, difficulty=7)

```
帮我从零搭一个用于财务运营的“预算偏差 + 发票/费用异常”小工具，最好能直接跑起来。

- 核心功能：输入预算、实际支出、发票/报销明细后，自动识别超预算、重复报销、异常金额、缺失审批、供应商名称不一致等情况。
- 形态：做成一个可本地运行的命令行工具，最好再带一个简单的 HTTP API，方便以后接到内部系统。
- 规则：请把异常规则设计成可配置的，不要写死；同时给出默认规则集和示例配置。
- 工程化：代码要模块化，包含单元测试、基本日志、错误处理和一份 README，说明如何安装、运行和扩展。
- 交付物：请直接产出完整代码文件和必要的文档，不要只给思路。

```

### 254. D11_s984838_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variance and invoice/expense exceptions for a monthly close workflow. Make it a real codebase, not a data analysis notebook: I want a working app with the core rules engine, a simple API or CLI to submit transactions and budgets, exception classifications, and a short README explaining how to run it. Please research a few current best-practice options for the stack and any relevant libraries or patterns before coding, then implement the whole thing cleanly with tests.
```

### 255. D11_s984863_zh (domain=D11, difficulty=7)

```
我需要你从零写一个面向财务运营的小工具，专门处理预算差异和发票/报销异常：做成一个可直接运行的 Python 项目，支持导入我后面自己补的交易明细后，自动识别超预算、重复报销、缺少审批、税率不一致和供应商名称不规范这些问题，并输出一份可读的异常报告和一个命令行入口。你先把代码、测试和 README 一起搭好，顺手把你查到的适合用的开源库、文件格式和财务异常规则也考虑进去，最后给我一套能跑起来的项目文件。
```

### 256. D11_s984864_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variance and invoice/expense exceptions for a monthly close workflow. Please create the code, tests, and a short README for a local app that lets a user define budgets by department/cost center, ingest invoices and expenses entered manually or via JSON, and then surface exceptions like overspend, duplicate invoices, missing PO numbers, and unusual spend spikes. Use current best practices and a sensible library choice after checking the web for lightweight Python tools that fit this use case.
```

### 257. D11_s984964_zh (domain=D11, difficulty=7)

```
请从零实现一个适合财务运营团队使用的小工具，用来自动处理预算差异和发票/报销异常，最好能直接跑起来。

- 做一个可配置的规则引擎，能识别预算超支、重复报销、金额不一致、缺少审批、超阈值等异常类型，并输出清晰的异常原因
- 提供一个命令行入口，支持导入我后续提供的 JSON/CSV 数据、运行校验、生成异常报告和汇总统计
- 设计一套合理的数据模型和结果格式，方便以后接到 ERP/财务系统里
- 写上必要的单元测试和集成测试，保证规则、解析和报告输出都稳定
- 补一份简短说明，讲清楚如何安装、运行、扩展规则，以及推荐的目录结构
- 如果需要选技术方案，请先查一下 Python 里适合做规则校验、表格处理和命令行工具的常见库，再决定实现方式
```

### 258. D11_s984978_zh (domain=D11, difficulty=7)

```
请从零实现一个用于财务运营的“预算差异与发票/费用异常处理”小工具，目标是让财务共享服务中心（FSSC）和业务财务能快速筛查月度预算偏差、重复报销、超阈值审批缺失、发票字段不一致等异常，并输出可直接落地的处理结果。

我不提供任何输入文件；请你直接搭建完整代码项目并给出可运行的实现。建议做成一个本地可运行的 Python 工具，核心能力至少包括：
1）定义一套可配置的规则引擎，用来判断预算差异异常和 invoice/expense exceptions；
2）支持读取 JSON/CSV 形式的交易、预算和报销记录（自行设计 schema，不依赖现成样本）；
3）输出异常分层结果：严重/中等/轻微，并给出可审计的原因码；
4）提供命令行入口，支持跑一次批处理、导出异常清单、生成汇总统计；
5）内置单元测试和最少量示例数据构造，确保能端到端跑通；
6）附带一份简洁 README，说明配置方式、规则扩展方式和使用示例。

实现时请参考当前主流 Python 生态里适合做规则配置、CSV/JSON 解析、CLI 和测试的库与最佳实践，必要时查一下这些库的推荐用法和当前稳定接口，再从头搭建，不要套用现成业务模板。交付物请直接给出代码文件和说明文件，要求能在本地复现运行。
```

### 259. D11_s984981_en (domain=D11, difficulty=7)

```
Build a small finance-ops tool from scratch for invoice and expense exception handling. I want a rules engine plus a simple API and CLI that flags budget variance, duplicate invoices, out-of-policy expenses, and missing approvals; put the code in app.py, with tests in tests/test_app.py and a README.md. Use current web research for best-practice choices on Python libraries and API patterns, then implement the feature set cleanly with no starter data.
```

### 260. D11_s985008_en (domain=D11, difficulty=7)

```
I need you to build a small finance-ops tool from scratch that flags budget variances and invoice/expense exceptions for a month-end close workflow. Make it a real code deliverable, not a data analysis: I want a runnable app plus tests and a short README, with the logic designed around common ERP/AP controls and exception handling best practices. Use web research where useful to sanity-check approaches, common invoice exception rules, and any lightweight library choices, then implement the whole thing cleanly from scratch with no input files or starter data.
```

### 261. D11_s985016_en (domain=D11, difficulty=7)

```
Build a from-scratch invoice and expense exception manager for finance ops. I need a small web app plus API that flags duplicate invoices, out-of-policy expenses, and budget variance alerts, with a rules engine I can configure in code and a clean dashboard for reviewers. Use current best practices and existing library docs where helpful, then deliver the code, tests, and a short README in app.py, rules.py, tests/, and README.md.
```

### 262. D11_s985041_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for finance ops that flags budget variance and invoice/expense exceptions, with a small CLI and a JSON report export. I want app.py, rules.py, and README.md; use current best-practice research for the design and pick a practical library stack before coding.
```

### 263. D11_s985065_en (domain=D11, difficulty=7)

```
Build a small finance ops exception tool from scratch for budget variance and invoice/expense review. I want a web research-backed implementation plan and the code in app.py plus README.md for a local CLI that flags overspend, duplicate invoices, and out-of-policy expenses, with configurable thresholds and exportable exception reports. Use current best-practice libraries/APIs where relevant, but do not rely on any input files or sample datasets.
```

### 264. D11_s985067_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that helps spot budget variance and invoice/expense exceptions, with a simple web API and a command-line entry point for uploading records and getting flagged anomalies back. Please use current best practices and real Python libraries, and do a bit of web research first so the design lines up with how people actually handle validation, rules, and audit-friendly outputs today. I want the code, tests, and a short README in the final deliverable, with no input files provided up front.
```

### 265. D11_s985075_zh (domain=D11, difficulty=7)

```
帮我从零做一个“预算差异 + 发票/报销异常”管理工具，直接产出可运行代码和 README，文件名你自己定，但要把核心逻辑、接口和测试都写全。我要能录入预算、实际支出、发票和报销单，自动算超支/节省、找出重复报销、缺少发票、税额不一致、超审批阈值这些异常，并输出一个简洁的 Web API + 命令行入口。
```

### 266. D11_s985103_zh (domain=D11, difficulty=7)

```
我需要你从零搭一个用于财务运营的“预算偏差与发票/费用异常管理”小工具，最好是一个可本地运行的 Web 应用，能手动录入预算、实际支出、发票和报销记录，自动识别超预算、重复报销、金额不一致、缺少审批人这些异常，并把结果按部门和项目汇总成一个简洁报表；同时把代码、README 和基本测试一起给我，方便我直接跑起来看效果。
```

### 267. D11_s985175_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that flags budget variance and invoice/expense exceptions for a monthly close workflow, with a simple API/CLI and clear docs. Please research a couple of current Python libraries and any best-practice patterns for validation, reporting, and rule-based exception handling, then implement the code, tests, and README in a clean repo structure. No input files — just generate the app and any sample config/data it needs.
```

### 268. D11_s985179_en (domain=D11, difficulty=7)

```
I want a small internal tool for finance ops that flags budget variances and invoice/expense exceptions before they hit AP review.

- Build it from scratch as a working codebase, not a spreadsheet or data-analysis notebook.
- Include a rules engine for common exception cases like duplicate invoices, out-of-policy expenses, missing PO, and budget overrun alerts.
- Add a simple API or CLI so a user can submit invoice/expense records and get back structured exception results.
- Use current best practices for validation, logging, and error handling, and research any libraries or patterns you pick.
- Make it testable with a clear test suite and a short README explaining how to run it and extend the rules.
```

### 269. D11_s985191_en (domain=D11, difficulty=7)

```
I want a small internal tool for Finance Ops that flags budget variance and invoice/expense exceptions before they hit review. Please build it from scratch as a working code project, not a data analysis notebook.

- Include a rules engine that can compare planned vs. actual spend and flag anomalies like over-threshold variance, duplicate invoice numbers, split expenses, weekend-dated receipts, and missing cost centers.
- Expose it through a simple API or CLI so someone can submit a batch of transactions and get back a structured exceptions report.
- Add a basic config layer so thresholds and exception rules can be changed without editing code.
- Include tests for the main rule paths and edge cases, plus a short README explaining how to run it.
- Use current best-practice research on a lightweight Python framework/library choice and any validation/testing patterns that fit this use case.

```

### 270. D11_s985216_en (domain=D11, difficulty=7)

```
I need a small internal finance ops tool built from scratch for handling budget variance and invoice/expense exceptions.

- Build a working app that lets a user create a monthly budget, log actuals, and flag over/under variance by department and category.
- Add an exceptions workflow for invoices/expenses with rules like duplicate invoice checks, amount threshold alerts, missing PO/vendor fields, and approval status tracking.
- Include a simple API or CLI plus a lightweight UI if practical, and make the data model easy to extend.
- Use current best practices and pick sensible libraries/frameworks after checking the web for up-to-date options and docs.
- Deliver the code, tests, and a short README explaining setup, key features, and how the exception rules work.
```

### 271. D11_s985247_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch for budget variance and invoice/expense exceptions: make it take transaction records entered in code, flag over-budget spend, duplicate invoices, missing PO references, and out-of-policy expenses, then generate a clean exception report and a simple CLI to review and export the results. Please put the code and a short README together, and use current web research on a few practical libraries or patterns for CLI parsing, table output, and validation so the implementation is solid and realistic.
```

### 272. D11_s985254_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for our finance ops team that flags budget variance and invoice/expense exceptions across monthly spend workflows. I want a small but production-minded package with a CLI and a simple local API so analysts can load ledger entries, vendor invoices, and expense claims from in-memory data structures or JSON payloads, then generate exception findings with reason codes. The feature set should include: configurable variance thresholds by cost center and vendor, duplicate invoice detection, amount/date/tax mismatches, missing PO references, and a summary of budget vs actuals by period. Use current best practices and existing open-source patterns for CLI design, validation, and lightweight API serving, but implement the logic and data models entirely from scratch. Deliver the code files plus a concise README describing how to run it and how the exception rules work. No input files are provided; the build should stand on its own and include representative test fixtures created in code.
```

### 273. D11_s985262_en (domain=D11, difficulty=7)

```
I need a small internal tool for Finance and Business Ops that helps us catch budget variance issues and invoice or expense exceptions before they turn into month-end surprises. The tool should be built from scratch, not based on any existing file, and I want a practical prototype I can hand to our ops team. Please research a sensible approach using current web resources first, then build the code and basic documentation. It should let a user enter budget lines and actual spend, flag unusual variances with clear reasons, and also review invoice or expense records for common exceptions like duplicate amounts, missing approvals, out-of-policy categories, or mismatched dates. I want the deliverable to be the built code files plus a short README that explains how to run it and what it does.
```

### 274. D11_s985307_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that helps our team flag budget variances and invoice/expense exceptions before they hit accounting. Make it a real working code project, not a data analysis thing: I want a runnable app with a rules engine for thresholds and approval logic, a simple API or CLI to enter transactions and exceptions, and a way to generate an exception report and audit trail. Use current best-practice research on a couple of relevant Python libraries and any common patterns for validation, logging, and export so the design is sensible, then implement the code and basic tests from scratch. No input files are provided, so create your own sample scenarios in the code or test fixtures. Please deliver the built code files and a short README.
```

### 275. D11_s985331_en (domain=D11, difficulty=7)

```
I need you to build a small finance ops tool from scratch that helps our team flag budget variance and invoice/expense exceptions before they hit accounting. Please create the code for a lightweight web app or CLI service that lets a user enter a budget amount, actuals, invoice lines, and expense claims, then automatically highlights over-budget items, duplicate invoices, missing PO numbers, out-of-policy expenses, and threshold breaches with a clear exception summary. Use real-world best practices for how finance teams structure approvals, validations, and exception statuses, and make sure the design is based on current libraries and patterns you look up online. No input files are needed — just build the tool, tests, and a short README explaining how to run it and how the exception rules work.
```

### 276. D11_s985337_en (domain=D11, difficulty=7)

```
Build me a small but real finance-ops exception handling tool from scratch for budget variance review and invoice/expense exceptions. I do not have any input files for you to work from, so please create the whole feature set yourself, including the data model, validation logic, and a usable interface. I want it designed for an operations team that reviews monthly budget variance flags, duplicate or suspicious invoices, and out-of-policy employee expenses.

The tool should be practical rather than toy-like. It needs to support at least these concepts: departments, cost centers, budgets by month, actual spend, approved purchase commitments, invoices, and expenses. I want rules that identify exceptions such as over-budget spend, missing approval, duplicate invoice risk, weekend or holiday expense, category mismatches, and split transactions that may evade approval thresholds. Please define reasonable default thresholds and explain them in the implementation so they can be configured later.

Please build it as a real code project from scratch with a clean structure rather than a single script. I want a small core engine that computes variance and flags exceptions, plus a user-facing interface that can inspect a handful of example transactions I can edit in code. Since there are no input files, please seed the app with a few hardcoded sample records representing multiple departments and scenarios, but keep the logic generic so it works on arbitrary records.

I want the output to be usable by a finance or business-ops team. At minimum, the tool should be able to:
- calculate budget variance at the month, department, and cost-center level;
- flag invoices and expenses for rule-based exceptions;
- produce a concise exception summary with severity levels and recommended next actions;
- allow a reviewer to mark an exception as approved, rejected, or resolved;
- export the current exception list to a simple machine-readable format such as JSON or CSV;
- include tests for the core rules and edge cases.

Please make the exception logic specific and realistic. For budget variance, treat variance as actual minus budget and compute both amount and percentage. For invoices, consider a duplicate-risk rule if invoice number, vendor, amount, and invoice date are suspiciously similar to another entry. For expenses, consider whether the transaction is outside policy when it exceeds category thresholds, occurs on a weekend, lacks a receipt over a configured amount, or is outside the employee’s cost center. If you include any ML or scoring heuristics, keep them lightweight and explainable; deterministic rules are preferred.

I also want a simple way to inspect the results locally, such as a CLI or a minimal web API. I do not need a full frontend, but I do want a usable interface for a reviewer to list exceptions, filter by status or severity, and update status. Please organize the code so it would be reasonable to extend later with a database or real payroll/AP system integration.

Please do some web research first if helpful to choose appropriate libraries, current best practices for date handling, JSON serialization, command-line interfaces, and lightweight API frameworks, but the implementation itself should be built from scratch. Use the research to make sensible choices about architecture and testing. I want the final deliverable to be the code files and a short README explaining how to run it and what rules it implements.
```

### 277. D11_s985347_en (domain=D11, difficulty=7)

```
I need a small internal tool for finance ops that helps us flag budget variances and invoice/expense exceptions before they hit monthly close. Build it from scratch as a real app, not a mockup.

- Create a backend service and simple CLI or web API for entering budgets, actuals, invoices, and expense claims, then returning exception flags and a concise explanation.
- Support a rules-based exception engine for common cases like over-budget spend, duplicate invoice risk, missing PO, weekend/after-hours submissions, and unusual vendor patterns.
- Use current best-practice libraries and patterns for validation, date handling, logging, and test structure; do a bit of web research first so the design matches what’s commonly used now.
- Include tests, sample usage, and short docs so another engineer can run it and extend the rules later.
- Keep it implementable without any input datasets; everything needed should be generated in code or via example payloads.

```

### 278. D11_s985399_en (domain=D11, difficulty=7)

```
Build a from-scratch finance ops exception tool for budget variance and invoice/expense anomalies. I want a small Python app with a CLI and a FastAPI service that flags overspend, duplicate invoices, missing PO matches, and out-of-policy expenses, plus a compact rules engine and sample synthetic data generator. Use current docs for the chosen libraries and keep it clean enough to drop into our internal ops workflow.
```

### 279. D11_s985423_en (domain=D11, difficulty=7)

```
Build a from-scratch Python tool for finance ops that flags budget variance and invoice/expense exceptions, with a small CLI and a reusable rules engine. I want the code in app.py, tests in tests/test_app.py, and a README.md that explains setup and usage. Use current web research for the best-fit libraries and any relevant accounting/expense-validation conventions before you code.
```

### 280. D11_s985430_en (domain=D11, difficulty=7)

```
I need a small internal tool for our finance team that helps us catch budget overruns and invoice or expense exceptions before they become month-end surprises. It should be built from scratch, not based on any existing template, and I want something we can actually use and extend later.

Please create the code for a simple budget variance and exception-review app that lets a user set a monthly budget by department, add planned spend and actual spend, and flag items that are over threshold or missing required details. I’d also like a way to review invoice and expense exceptions in one place, with basic filtering, status updates, and a clear summary of what needs attention. Use sensible defaults and make the experience straightforward for non-technical finance users.

Please research current best practices and suitable libraries or frameworks for a lightweight app and validation layer, then build the tool from scratch with proper tests and setup instructions. I want the code files and a short README so my team can run it locally and understand how it works.
```

### 281. D11_s985437_zh (domain=D11, difficulty=7)

```
帮我从零开发一个“预算偏差 + 发票/费用异常”审核工具，直接给出可运行代码和README。我要一个命令行优先的Python项目，能配置部门预算、导入发票/报销记录、自动识别超预算、重复报销、缺少审批、异常税率和供应商黑名单，并输出审计报告。顺手把核心规则、命令行参数、测试和示例配置都补齐，文件名你自己定。
```

### 282. D13_s981169_en (domain=D13, difficulty=7)

```
Build a from-scratch Python tool for product analytics experimentation readouts: `experiment_readout.py` plus `README.md`. I want it to compute A/B test summaries, funnel conversion comparisons, and cohort retention tables from event streams, with a small CLI for ingesting CSV events and printing the readout. Do the design against current best practices and libraries you verify from the web, then implement the code and tests.
```

### 283. D13_s981316_en (domain=D13, difficulty=7)

```
I need you to build a small from-scratch product analytics toolkit for A/B readouts, funnels, and cohorts. Please create the code and a short README so I can run it locally on sample event streams I generate later. It should include a clean core engine for metric definitions, experiment readouts, funnel conversion, and cohort retention, plus a simple CLI or local API to run analyses and export results. Make sure the design follows current best practices from real analytics libraries and experiment-analysis docs, but don’t rely on any input files or existing starter project.
```

### 284. D13_s981337_en (domain=D13, difficulty=7)

```
Build a from-scratch Python package for experiment readouts: `experiments/` with modules for A/B significance, funnel conversion, and cohort retention, plus a small CLI in `main.py` and a `README.md` with usage examples. Use current best practices from web research on stats libraries and command-line app structure, but don’t rely on any input files or starter project—just create the code and tests from scratch.
```

### 285. D13_s981362_en (domain=D13, difficulty=7)

```
Build a from-scratch Python toolkit for product analytics experimentation called `exp_readout`. I need `exp_readout.py`, `tests/`, and a short `README.md` that explains how to use it. It should support A/B readouts, funnel conversion analysis, and cohort retention summaries from event logs, with a small CLI for running analyses and exporting JSON/CSV.
```

### 286. D13_s981393_en (domain=D13, difficulty=7)

```
Build a from-scratch Python package for product analytics experimentation called `expreadout` with `README.md`, `pyproject.toml`, and the main package files. It should compute A/B test readouts, funnel conversion summaries, and cohort retention curves from event-level data, with a small CLI and a simple local HTTP API. Use current best practices from existing tools/docs where useful, and keep the code self-contained.
```

### 287. D13_s981432_zh (domain=D13, difficulty=7)

```
给我从零构建一个产品分析工具包，包括A/B测试读数、漏斗分析和队列分析。用Python写，核心模块放product_analytics/core.py，统计函数放stats_utils.py，命令行接口放cli.py，单元测试在tests/下，文档用README.md。工具要能处理用户从标准输入或参数传入的数据并输出统计结果。直接生成文件结构和代码。
```

### 288. D13_s981456_en (domain=D13, difficulty=7)

```
I need you to build a small from-scratch product analytics toolkit for A/B readouts, funnels, and cohorts, with a clean CLI or API, so our team can plug in events later and use it for experiment reviews. Please research a sensible Python stack and patterns first, then implement the code, tests, and a short README explaining how to run it and how the core metrics are computed. There are no input files for this — I want the actual tool built from scratch, not a data analysis on existing data.
```

### 289. D13_s981473_zh (domain=D13, difficulty=7)

```
我需要你帮我从零构建一个Python工具包，专注于产品分析中的实验解读、漏斗分析和同期群分析。具体来说，这个工具应该是一个命令行程序，能接受用户提供的实验数据（CSV格式），自动计算A/B测试的统计显著性（比如p值、置信区间），还能做多步骤漏斗的转化率计算，以及基于时间的同期群留存分析。所有代码要自己写，不能依赖现有的数据文件。请包括完整的单元测试和README文档，方便后续维护和扩展。可以用scipy等开源库。最终给我一个可运行的脚本和配套文档。
```

### 290. D13_s981489_zh (domain=D13, difficulty=7)

```
帮我从头构建一个产品实验分析工具（Python命令行），主要做三个功能：1) A/B测试结果读取与统计显著性计算（支持两样本t检验和贝叶斯方法）；2) 漏斗分析（自定义步骤，计算每一步转化率与流失率）；3) 同期群分析（按周/月计算留存率并输出热力图）。

具体要求：
- 所有数据由工具自动生成随机实验数据，不依赖外部文件，用户只需指定参数（比如样本量、转化率、步骤数等）；
- 输出一份包含图表和表格的HTML报告（用matplotlib和pandas生成，嵌入base64图片）；
- 支持两个实验变体（控制组 vs 实验组），漏斗步骤最多10个，同期群最多24个周期；
- 提供CLI接口，支持 `python analytics.py ab --size 1000 --rate 0.1` 等命令；
- 代码结构清晰，模块化，附带单元测试（覆盖核心统计函数、数据生成、报告生成）；
- 最终交付物：一个可运行的 `analytics.py` 文件和配套的 `README.md` 说明。
```

### 291. D13_s981495_en (domain=D13, difficulty=7)

```
We need a small internal product analytics tool built from scratch because our team is spending too much time manually pulling A/B readouts, funnel performance, and cohort retention summaries for launch reviews. Please build the code for a lightweight web app or CLI tool that lets us define an experiment or product metric question, then calculates and displays the key readouts in a clear, business-friendly way. It should support basic A/B comparison, funnel step conversion, and cohort retention views, with sensible defaults and guardrails so non-technical teammates can use it safely. Please research current best practices and a practical open-source stack before building, then deliver the working code and a short README explaining how to run it and what it does. No input files will be provided; the tool should work with synthetic/demo data you generate in the code or with data pasted in a simple format the app accepts.
```

### 292. D13_s981581_en (domain=D13, difficulty=7)

```
I want a small product-analytics tool built from scratch that helps me read A/B tests and usage behavior without relying on spreadsheets.
- Build a CLI or lightweight app that can ingest event logs and produce experiment readouts: conversion, lift, confidence intervals, and basic significance checks.
- Add funnel analysis and cohort retention views so I can compare steps, drop-off, and week-over-week retention by experiment variant.
- Make the tool support a simple event schema, filtering by date, variant, and user segment, and output clean tables plus a JSON summary.
- Research a couple of current best-practice approaches for A/B readouts and Python libraries for stats/output formatting, then implement the core logic yourself.
- Include tests and a short README with usage examples so another analyst can run it locally.
```

### 293. D13_s981790_en (domain=D13, difficulty=7)

```
Build a small Python app from scratch for experiment readouts: it should compute A/B test lift with confidence intervals, support funnel conversion by step, and basic cohort retention tables. Put the code in app.py with a CLI and add tests in tests/test_app.py, plus a short README.md. Use current best practices for stats and CLI design, and do the necessary web research before implementing.
```

### 294. D13_s981908_en (domain=D13, difficulty=7)

```
Build a small open-source Python tool from scratch for product analytics experiment readouts: `experiment_readout/` with a CLI that ingests event logs, computes A/B test summary stats, funnel conversion by step, and cohort retention tables, plus a clean Markdown report export. Name the main files `experiment_readout.py`, `report.py`, `tests/`, and `README.md`; don’t use any starter dataset.
```

### 295. D13_s981932_en (domain=D13, difficulty=7)

```
Build a from-scratch Python 3 tool for product analytics experimentation: a small CLI app that ingests event JSON from stdin, computes A/B readouts, funnels, and weekly cohorts, and prints a compact markdown report. I want app.py, analytics.py, tests/, and README.md; use real-world library choices and current best practices, and check the docs/API behavior before you code.
```

### 296. D13_s981968_en (domain=D13, difficulty=7)

```
Build a from-scratch product analytics experimentation service in Python: a small FastAPI app plus a core library that computes A/B readouts, funnel conversion, and cohort retention from event streams, with an endpoint and CLI for running experiments. Include a README and tests; no starter data, just the code and a synthetic example generator.
```

### 297. D13_s981970_en (domain=D13, difficulty=7)

```
Build a from-scratch Python service for product analytics experimentation readouts: it should ingest event streams, compute A/B test lift with guardrails, funnel conversion, and cohort retention, then expose results through a small FastAPI app and CLI. Put the code in app/, tests in tests/, and write a short README.md with setup and usage.
```

### 298. D13_s981973_en (domain=D13, difficulty=7)

```
I need you to build a small but real product analytics toolkit from scratch that can do A/B experiment readouts, funnel conversion analysis, and cohort retention summaries from event data, with a simple CLI or local API and clear docs. Please research a couple of current Python libraries/best practices for stats, CLI design, and event-schema handling first, then implement the code, tests, and README in separate files so I can run it locally and use it on my own event logs later. No input files from me — just make the tool itself and the supporting docs.
```

### 299. D13_s982006_zh (domain=D13, difficulty=7)

```
从零做一个可本地运行的产品分析读数工具，重点支持 A/B 实验读数、漏斗和 cohort 分析。请直接交付代码文件：main.py、analytics.py、storage.py、cli.py、tests/test_analytics.py、README.md，做成一个 Python 包，CLI 能创建实验、录入事件、生成实验 readout 和漏斗/cohort 汇总报表。
```

### 300. D13_s982078_en (domain=D13, difficulty=7)

```
Build a from-scratch product analytics experiment readout tool in Python that can ingest event streams, compute A/B test lift, funnels, and cohort retention, and expose it as a small CLI plus library. I want app.py, analytics/ modules, tests/, and a README.md with usage examples; no starter data, just the code.
```

### 301. D13_s982119_en (domain=D13, difficulty=7)

```
We need a lightweight internal product analytics tool because our team keeps losing time every week waiting for ad hoc A/B readouts, funnel drop-off checks, and cohort retention summaries. Please build this from scratch as a small, practical codebase that can take event data we define ourselves and produce clear experiment and product metrics in a way a PM or analyst could use without spreadsheets.

What I want:
- A simple core engine that can calculate A/B experiment readouts, funnel conversion steps, and cohort retention from event-level records.
- A clean command-line or small local app interface so someone can run one report at a time and get readable output.
- A few example scenarios built into the code so we can demo it immediately.
- Basic tests so we know the main calculations and edge cases behave correctly.
- Documentation that explains how to run it and what each report means.

Please research current best practices and a few solid library choices before building, especially for Python analytics tooling, CLI structure, and how teams usually present experiment readouts and funnels. Then implement the code from scratch and organize it so different parts can be built in parallel.
```

### 302. D13_s982145_en (domain=D13, difficulty=7)

```
Build a small from-scratch product analytics experimentation tool for internal use that can read an event stream, calculate A/B test readouts, and support basic funnel and cohort analysis.
- I want a working codebase, not a mockup, with a clear CLI or simple API to run analyses on synthetic event data generated inside the app.
- Include experiment readout for a variant vs control, funnel conversion tracking across configurable steps, and cohort retention by signup week.
- Use current best practices for stats and product analytics tooling, and research a couple of relevant open-source libraries/APIs before implementing so the design is grounded.
- Add tests and a short README that explains how to run it and what assumptions it makes.
- Keep it dependency-light and practical enough that a product analyst or engineer could actually use it as a local prototype.
```

### 303. D13_s982156_en (domain=D13, difficulty=7)

```
Build a small, production-style product analytics experiment readout tool from scratch for A/B tests, funnels, and cohorts. I want the code, not a mockup, and there are no input files — please create the whole implementation and supporting docs/tests yourself.

- Make it able to ingest a simple event stream schema and compute A/B readouts with significance checks, funnel conversion by step, and cohort retention tables.
- Include a clean CLI or lightweight local API so I can run a readout on synthetic/example data and export results as JSON/CSV.
- Research current best practices for experiment analysis libraries and statistical methods before implementing, then build the solution from scratch.
- Add automated tests for the core analytics logic and edge cases, plus a short README explaining how to run it.
- Keep the design modular so the analytics engine, CLI/API layer, and test suite are separable and easy to extend.

```

### 304. D13_s982220_en (domain=D13, difficulty=7)

```
Build a from-scratch Python 3.12 package for product analytics experimentation: a small local service that ingests event JSON, defines funnels/cohorts, and generates A/B readouts with significance and guardrails. I want `src/`, `tests/`, `README.md`, and a working CLI entrypoint with examples; no input files, just code.
```

### 305. D13_s982227_en (domain=D13, difficulty=7)

```
We need a lightweight internal product analytics tool because our team keeps making experiment decisions too slowly and the current reports are too manual. Please build a small from-scratch app that lets us define an A/B test, track the key events for a funnel, and view a simple cohort retention readout so product managers can answer basic questions without waiting on analysts.

I want the code and a short README, not a slide deck. Please make it practical for a startup: one backend service, a simple UI or command-line way to create and inspect experiments, and clear guidance on how to run it locally. Use current best practices for whatever libraries you choose, and check the web for realistic choices and patterns before building. There are no input files; the app should start with sample data generated in code or created on the fly.
```

### 306. D13_s982246_en (domain=D13, difficulty=7)

```
Build a from-scratch Python service for product analytics experimentation: a small A/B readout engine with funnel and cohort support, exposed as a CLI plus a minimal FastAPI endpoint. I need app.py, analytics/core.py, analytics/funnels.py, analytics/cohorts.py, api.py, tests/, and README.md; use current best-practice libraries and document any API choices you make. No input files — generate your own example fixtures in code and make the tool runnable end to end.
```

### 307. D13_s982259_en (domain=D13, difficulty=7)

```
I need you to build a small from-scratch product analytics toolkit for experiment readouts, funnels, and cohorts: give me the code for a local Python package plus a CLI that can ingest event logs, run A/B test readouts with guardrail checks, compute funnel drop-off, and build basic cohort retention tables. Please research a couple of current Python libraries and best practices first so the implementation is realistic, then produce the app code, tests, and a README showing how to run it. There are no input files yet, so make the whole thing work with sample event data generated in code.
```

### 308. D13_s982309_en (domain=D13, difficulty=7)

```
I need you to build a small product-analytics experimentation toolkit from scratch for our team: a CLI plus a lightweight HTTP API that can take event logs we generate, compute A/B test readouts, funnel conversion, and cohort retention, and return a clean markdown/JSON report. Please include the code, tests, and a README showing how to run it. I want it to support sequential comparison of two variants, basic guardrails for bad event data, and a couple of example commands so I can try it locally.
```

### 309. D13_s982340_en (domain=D13, difficulty=7)

```
Build a from-scratch Python tool for A/B readout, funnels, and cohort retention that can ingest event streams, compute experiment lift with confidence intervals, and generate a plain-English markdown report. I want the code in app.py plus tests in test_app.py and a short README.md with usage examples and assumptions.
```

### 310. D13_s982354_en (domain=D13, difficulty=7)

```
Build a from-scratch lightweight experiment readout tool for product analytics: implement a small Python package + CLI that ingests event streams, computes A/B test readouts, funnels, and cohort retention from scratch, and exports a markdown report. Use current docs/best practices from Statsig, Optimizely, and Amplitude for metric/readout conventions before coding, but do not use any starter data. Put the code in app.py, analytics_core.py, and README.md.
```

### 311. D13_s982376_en (domain=D13, difficulty=7)

```
Build a from-scratch experiment analytics service for product metrics readouts. I want a small Python app with a typed core library, FastAPI endpoints, and a CLI that computes A/B test lift, funnel conversion, and cohort retention from event logs; include README.md and tests. Use current best-practice library choices and document any APIs or packages you pick.
```

### 312. D13_s982380_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics toolkit from scratch for A/B readouts, funnels, and cohorts, with a clean CLI and a minimal web dashboard. Please create the code and docs in a few files so I can run it locally against synthetic events, and make sure it can summarize experiment results, compute funnel drop-off, and generate cohort retention views without relying on any starter dataset.
```

### 313. D13_s982416_en (domain=D13, difficulty=7)

```
I need you to build a small product-analytics experimentation toolkit from scratch for A/B readouts, funnels, and cohort tracking — think a lightweight internal service I could use to define events, compute experiment lift with guardrails, and generate funnel/cohort summaries from event streams. Please research a couple of current Python libs and best practices for stats and reporting first, then produce the code, tests, and a short README for how to run it locally; there are no input files, just the codebase.
```

### 314. D13_s982439_zh (domain=D13, difficulty=7)

```
我需要你从零做一个产品分析和实验读数的小工具，最好是一个可运行的后端服务加命令行入口，支持 A/B 实验读数、漏斗转化和 cohort 留存的基础计算，并且能把结果以 JSON 和简单 Markdown 报告输出；你先自己查一下现在适合 Python 的实现方式和常用库，再直接把代码、测试和 README 一起搭出来，别依赖任何现成数据文件，样例数据你可以在代码里造出来。
```

### 315. D13_s982450_en (domain=D13, difficulty=7)

```
Build a from-scratch Python tool for product analytics experimentation readouts: `experiment_readout.py` with a small CLI that ingests event logs and outputs A/B test results, funnel conversion, and cohort retention summaries. Include `README.md` and unit tests; use current best-practice libraries/APIs after checking the web, and don’t rely on any starter dataset.
```

### 316. D13_s982504_en (domain=D13, difficulty=7)

```
I need a small but production-minded product analytics toolkit built from scratch for experiment readouts. Please implement the code and supporting docs, not a data analysis on any uploaded files.
- Build a Python package/CLI that can ingest event logs, define funnels and cohorts, and produce A/B experiment readouts with guardrails for sample ratio mismatch and basic statistical significance.
- Research and pick sensible open-source libraries/APIs for command-line UX, table output, and stats utilities, then justify those choices in the docs.
- Include a way to compare two variants over configurable date windows, compute funnel conversion by step, and segment results by cohort.
- Add tests that cover the core analytics logic and the CLI end-to-end, plus a short README with usage examples.
- Keep it self-contained and buildable from scratch; no starter dataset will be provided.
```

### 317. D13_s982510_en (domain=D13, difficulty=7)

```
Build a small product-analytics experiment readout tool from scratch in Python: a FastAPI backend plus a lightweight CLI that computes A/B test readouts, funnel conversion, and cohort retention from in-memory event JSON. Use current best-practice references for stats and API design, and include a README plus tests. Name the files app.py, analytics.py, cli.py, tests/test_analytics.py, and README.md.
```

### 318. D13_s982552_en (domain=D13, difficulty=7)

```
I need a small but real analytics tool I can use for product experimentation work. Build it from scratch so I can run A/B readouts, funnel checks, and basic cohort views against event data.
- Make it a local Python package or app with a clean command-line interface for ingesting events, defining experiments, and producing readouts.
- Include support for A/B metrics like conversion rate, uplift, confidence intervals, and a simple sequential guardrail so it’s usable for weekly experiment reviews.
- Add funnel analysis and cohort retention views from the same event model, with documented event schema assumptions.
- Use current best practices and a couple of appropriate open-source libraries only after checking the web for up-to-date API details and common patterns.
- Ship the implementation code, tests, and a short README with example commands so another analyst can run it without a starter dataset.

```

### 319. D13_s982568_en (domain=D13, difficulty=7)

```
Build a from-scratch Python package for product analytics experimentation: a CLI + library that generates A/B readouts, funnel reports, and simple cohort retention tables from event streams. I want src/, tests/, and a README.md, with no starter data files; include a small synthetic demo generator inside the code so it runs end-to-end. Do a quick web-backed design pass first on best practices and commonly used approaches for experiment readouts, funnel definitions, and cohort retention output formats before implementing.
```

### 320. D13_s982580_zh (domain=D13, difficulty=7)

```
帮我从零做一个产品分析实验平台的核心服务，支持 A/B readout、漏斗和 cohort 计算：先调研现成方案/最佳实践（如 Statsig、LaunchDarkly、Amplitude、Mixpanel、OpenTelemetry 里和实验/分析相关的做法），然后实现一个可运行的 Python 包和命令行工具。代码里要有事件模型、实验分流结果汇总、漏斗转化计算、cohort 留存计算、以及输出一份 README.md 说明怎么用。不要用任何现成分析 SDK 直接替代核心逻辑，自己实现。
```

### 321. D13_s982647_zh (domain=D13, difficulty=7)

```
帮我从零做一个产品分析实验读数工具：支持 A/B 实验的显著性读数、漏斗转化、分 cohort 留存三块，做成一个可运行的 Python 项目，包含核心计算库、命令行入口和最小 API。把代码放在 app/、tests/、README.md，顺手把指标口径和边界条件写清楚。别用现成分析平台，自己实现。
```

### 322. D13_s982659_en (domain=D13, difficulty=7)

```
Build a from-scratch experiment analytics service for product teams: implement an A/B readout engine with funnel conversion, cohort retention, and segment breakdowns, plus a small CLI to run reads against in-memory event data and print a results report. Put the code in app.py, tests in test_app.py, and a short README.md with usage and assumptions.
```

### 323. D13_s982708_en (domain=D13, difficulty=7)

```
Build a small Python service for product analytics experimentation: compute A/B test readouts, funnel conversion, and cohort retention from event streams, with a minimal FastAPI API and CLI in src/. Use current best practices and pick the right open-source libs after checking their docs first; also include a README with setup and example requests. No input data files — generate sample events in tests and examples.
```

### 324. D13_s982724_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics experimentation tool from scratch for A/B readouts, funnels, and cohorts. Please design the code so I can run it locally, with a clean CLI or simple web app, and include the core reporting logic, a few realistic example event schemas, and a README that explains how to use it for experiment readouts and cohort analysis. No input files are provided, so it should generate or accept sample events itself and be ready to demo.
```

### 325. D13_s982726_en (domain=D13, difficulty=7)

```
We need a small internal analytics tool for our product team because we keep losing time every week stitching together A/B test results, funnel drop-off, and cohort retention in spreadsheets. Please build the code from scratch for a lightweight web app that lets a PM define an experiment, view a clean readout for two variants, explore a simple funnel, and see cohort retention trends without needing any input data files. I want the deliverable to be the working codebase and a short README so engineering can run it locally and extend it. Please use current best practices and check what libraries or patterns are sensible before you start, since I care more about something reliable and practical than a flashy demo.
```

### 326. D13_s982749_en (domain=D13, difficulty=7)

```
We need to ship a small internal analytics tool that product managers can use to read out A/B tests without waiting on an analyst. It should help answer three things in one place: how each variant performed, where users drop off in the funnel, and how behavior changes over time in cohorts after signup. Build the tool from scratch and give me the code files plus a short README so our team can run it locally and extend it. Please base the design on current best practices and existing libraries if that helps, but do not use any input data files — it should work with synthetic example data you generate in the code. I want something practical enough that a real product team could actually use as a starting point.
```

### 327. D13_s982768_en (domain=D13, difficulty=7)

```
Build a small from-scratch product analytics service for A/B readouts, funnels, and cohort retention. I want a backend in Python plus a minimal CLI and HTTP API; name the files and wire it up so I can run local experiments without any input datasets. Also include a README with setup and example commands.
```

### 328. D13_s982877_zh (domain=D13, difficulty=7)

```
帮我从零写一个产品分析实验平台原型，重点是 A/B readout、漏斗分析、cohort 留存三块。给我代码和 README，要求有命令行或小型 Web 服务都行，但要能直接运行，别用现成样例数据；你自己生成一套示例事件流并把核心逻辑实现出来。顺手把常见实验统计口径、漏斗定义、留存 cohort 的实现方案做一下技术选型，文件名和目录结构你来定。
```

### 329. D13_s982880_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics toolkit from scratch for A/B readouts, funnels, and cohorts, with a clean CLI or lightweight web app plus solid docs and tests. It should let me define events, run experiment readouts with significance/guardrail checks, compute funnel conversion by step, and generate cohort retention tables, and I want you to research a couple of current open-source libraries or best-practice approaches first so the design is sensible. No input files are provided — just build the code, tests, and a short README for how to use it.
```

### 330. D13_s982899_zh (domain=D13, difficulty=7)

```
从零实现一个面向 Product Analytics & Experimentation 的轻量级实验读数工具，目标是支持 A/B readout、漏斗转化和 cohort 留存的统一计算与输出。不要依赖任何现成埋点数据或输入文件；请直接把代码、测试和使用说明一起搭出来。我们标准是：事件模型以用户级事件流为核心，支持 experiment assignment、conversion event、funnel step、cohort anchor 四类概念；结果层要能输出实验分组的指标汇总、漏斗各步转化率、以及按周/月 cohort 留存矩阵。希望你先基于当前主流实现方式做一次简短 Web research，确认 Python 生态里适合做这类工具的库和最佳实践（例如 pandas/polars、typer/click、pydantic、统计检验/置信区间实现方式），再从零实现一个可运行的命令行工具和核心计算库。最终交付我希望看到：核心计算模块、CLI、单元测试、README，以及一个最小可运行示例入口；如果你认为更合适，也可以附一个简短设计说明，解释指标口径、边界条件和统计假设。
```

### 331. D13_s982913_zh (domain=D13, difficulty=7)

```
帮我从零做一个产品分析实验读数工具，支持 A/B 实验结果判定、漏斗转化和 cohort 留存分析，代码和 README 都要齐。优先给我一个可直接跑的命令行工具或小型服务，文件名你自己定，但要把核心计算、输入校验、输出格式、示例用法都补全。
```

### 332. D13_s982926_en (domain=D13, difficulty=7)

```
Build a from-scratch product analytics experimentation tool: a small TypeScript app that reads event streams, computes A/B test readouts, funnels, and cohort retention, and exposes them through a simple CLI plus JSON output. I want `README.md`, `src/`, and tests; use current best practices from the web for stats and analytics library choices, but don’t use any starter dataset.
```

### 333. D13_s982932_en (domain=D13, difficulty=7)

```
I need a small from-scratch product analytics tool that I can actually use for experiment readouts and funnel/cohort checks.
- Build a web app or CLI that lets me define an A/B test, compute basic readouts, and compare variants with clear summaries and charts.
- Include funnel analysis and cohort retention views so I can inspect drop-off and repeat usage by variant or segment.
- Make it work without any sample input files; use synthetic/demo data generation inside the app so I can try it immediately.
- Research current best practices and a couple of modern libraries/APIs for stats, charting, and data handling before you build it.
- Deliver the finished code and a short README with how to run it, plus tests for the core analytics logic.
```

### 334. D13_s982985_en (domain=D13, difficulty=7)

```
Build a from-scratch Python 3.12 package for A/B readouts, funnels, and cohorts. I want `src/`, `tests/`, `pyproject.toml`, and a `README.md` that shows how to run it; no input data files. Make it support event-level datasets in pandas, compute experiment readouts with guardrails, funnel conversion/drop-off, and retention cohorts, plus a small CLI for running each report.
```

### 335. D13_s982989_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics experimentation toolkit from scratch for A/B readouts, funnel analysis, and cohort retention, with a clean CLI or lightweight API plus docs and tests. Please research current best practices and a few relevant open-source libraries first, then implement the code and make sure it can generate experiment summaries, funnel conversion breakdowns, and cohort tables from event data without relying on any starter files.
```

### 336. D13_s983008_zh (domain=D13, difficulty=7)

```
帮我从零做一个产品分析实验平台的小工具，重点是 A/B 实验读数、漏斗和 cohort 看板：先调研一下现成做法和相关库，然后直接实现一个可运行的 Python 包和命令行工具。我要它能定义事件 schema、加载内存样本数据、算实验分组指标、漏斗转化、留存 cohort，并输出一份 demo 报告；代码放到 analytics_tool/，再写 README.md 和最少一组测试。
```

### 337. D13_s983020_en (domain=D13, difficulty=7)

```
Build a from-scratch Python service for product analytics experimentation: an A/B readout engine that ingests event JSON, computes funnel conversion by variant, cohort retention, and basic significance/readout summaries. I want app.py, analytics/core.py, analytics/funnels.py, analytics/cohorts.py, and README.md, plus tests. Use current best-practice sources for experiment stats and Python library choices before coding.
```

### 338. D13_s983034_en (domain=D13, difficulty=7)

```
Build a small Python product-analytics service from scratch for A/B readouts, funnels, and cohorts: expose a CLI plus a FastAPI API in app.py, and include README.md with setup and usage. I want it to accept event streams, compute experiment readouts, funnel conversions, and cohort retention without any input files.
```

### 339. D13_s983071_zh (domain=D13, difficulty=7)

```
我需要你从零搭一个给产品分析和实验平台用的轻量工具：能录入一批事件级数据，然后生成 A/B 实验读数、漏斗转化和 cohort 留存的结果，最好做成一个可直接运行的命令行小项目，顺手给我一份 README 和基础测试。设计上别照搬现成 BI 工具，核心是把实验分流校验、指标汇总、漏斗路径、留存分组这些能力做扎实一点，输出格式要适合分析师直接看，也方便后面接到 API 或仪表盘里。
```

### 340. D13_s983082_en (domain=D13, difficulty=7)

```
Build me a small analytics service from scratch for product experiments: I want a FastAPI backend plus a tiny CLI that can compute A/B readouts, funnel conversion, and cohort retention from event streams. Use current best-practice Python libs and docs you verify on the web, and include clear examples in README.md. No input files — generate a synthetic demo dataset in code and make the whole thing runnable locally.
```

### 341. D13_s983124_en (domain=D13, difficulty=7)

```
Build a small but production-minded product analytics toolkit from scratch for A/B readouts, funnels, and cohorts. I want the codebase, not a mockup, and I’m not providing any input files.
- Create a Python package that accepts event logs in memory or via JSONL/CSV and computes experiment readouts, funnel conversion, and cohort retention.
- Include a clean CLI for running analyses, plus a minimal HTTP API so the same engine can be used by tools or scripts.
- Make the statistical choices sane for product analytics and document them clearly, especially around A/B comparisons, guardrails, and missing data handling.
- Add tests for the core analytics logic and a few end-to-end command paths.
- Use web research to check current best practices and a couple of real libraries/APIs for inspiration before implementing.
```

### 342. D13_s983203_zh (domain=D13, difficulty=7)

```
我需要你从零做一个产品分析和实验读数的小工具，最好是一个可运行的 Python 项目：能接收我手动定义的事件数据结构，生成 A/B 实验读数、漏斗转化和 cohort 留存的结果，还要有一个简单的命令行入口和一份 README，方便我本地直接跑起来。你先帮我把实现方案、依赖选型和最佳实践查清楚，再把代码和测试一起做出来，别依赖任何现成数据文件。
```

### 343. D13_s983212_en (domain=D13, difficulty=7)

```
Build a small Python service for product analytics experiment readouts: `experiment_readout.py` plus `README.md`. I want it to compute A/B test summary stats, funnel conversion comparisons, and cohort retention tables from event streams, with a tiny FastAPI endpoint and a CLI. Research the best-practice formulas and any lightweight libraries you’d use, then implement it from scratch.
```

### 344. D13_s983230_en (domain=D13, difficulty=7)

```
We need a small internal product analytics tool because our teams keep arguing about experiment results, funnel drop-offs, and whether cohort retention is actually moving in the right direction. Build the code for a lightweight web app that can ingest event data, define an A/B test readout, show a simple funnel view, and display cohort retention over time so a product manager can answer basic questions without waiting on engineering. I do not have any input files for this — please build it from scratch, choose a sensible stack, and include clear setup instructions plus a few example data generators or sample events so it can be run right away. I want the finished code files, not a written report.
```

### 345. D13_s983278_en (domain=D13, difficulty=7)

```
We need a small internal analytics tool because our product team keeps asking the same questions after every experiment: did the change move the main metric, where are users dropping in the funnel, and are newer cohorts behaving differently over time? I want a real code build from scratch that gives us a simple way to answer those questions without depending on spreadsheets. Please design and build a lightweight experiment readout app that can ingest basic event data, calculate A/B test results, show funnel drop-off, and compare cohorts over time. Use current best practices and look up a few good libraries or patterns before you build it. I want the finished codebase and a short README that explains how to run it, how the logic works, and how to extend it later.
```

### 346. D13_s983298_en (domain=D13, difficulty=7)

```
Build a small from-scratch experiment analytics service in Python for product teams: implement A/B readout, funnel conversion, and cohort retention APIs in src/ and a simple CLI in cli.py. Use current best-practice research for experiment analysis libraries, confidence interval handling, and funnel/cohort definitions, then document the design in README.md.
```

### 347. D13_s983334_en (domain=D13, difficulty=7)

```
Build a small product-analytics experimentation service from scratch for A/B readouts, funnels, and cohorts. I want the code in app.py plus tests.py and a short README.md, with a CLI and a tiny HTTP API for creating experiments, ingesting events, and generating readouts. Use current best-practice libraries and patterns after checking the web for a lightweight Python stack that fits this use case.
```

### 348. D13_s983356_en (domain=D13, difficulty=7)

```
Build a from-scratch experiment readout tool for product analytics: a small TypeScript app that computes A/B test lift, funnels, and cohort retention from event streams, with a clean CLI and a minimal HTTP API. Create src/, tests/, README.md, and package.json; include sane defaults, sample generated demo data, and no external datasets.
```

### 349. D13_s983370_en (domain=D13, difficulty=7)

```
Build a from-scratch Python analytics tool for product experimentation readouts: a small FastAPI service plus core library that computes A/B test results, funnel conversion, and cohort retention from event streams. I want app.py, analytics.py, tests/, and README.md; use current best practices and library choices you verify with web research before coding.
```

### 350. D13_s983381_zh (domain=D13, difficulty=7)

```
帮我从零做一个产品分析实验平台的最小可用实现：支持 A/B readout、漏斗和 cohort 分析，最好做成一个可运行的后端服务 + CLI。请输出代码到 app.py、analytics.py、README.md 和 tests/，并把你选型时参考到的 Web API/库说明写进 README 里；不要依赖现成数据文件，自己生成示例事件数据和演示流程。
```

### 351. D13_s983416_en (domain=D13, difficulty=7)

```
Build a from-scratch Python tool for experiment readouts: a small FastAPI service plus CLI that computes A/B test summaries, funnel conversion, and cohort retention from event-style data generated in code. I want app.py, analytics.py, tests/, and README.md, with sane defaults, confidence intervals, and clear endpoints/commands for product analytics use.
```

### 352. D13_s983500_en (domain=D13, difficulty=7)

```
Build a small Python product-analytics toolkit from scratch for A/B readouts, funnels, and cohort retention. I want the code in app.py plus README.md, with a simple CLI that can take event data from stdin and output experiment stats, funnel conversion, and cohort tables. Research the right statistical approach and any libraries you’d use before you code, then implement it cleanly with tests.
```

### 353. D13_s983564_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics experimentation tool from scratch: a Python service that lets me define events, compute A/B test readouts, build funnel and cohort summaries, and expose it through a simple CLI plus a tiny local API. Please include the core code, tests, and a README showing how to run it; use current best-practice libraries and patterns for stats and table output, and make sure the design is based on real-world tooling choices rather than guesswork.
```

### 354. D13_s983610_en (domain=D13, difficulty=7)

```
Build a small Python service from scratch for product analytics experimentation. I want an HTTP API with readout endpoints for A/B tests, funnel conversion, and cohort retention, plus a minimal README and tests. Research a couple of current open-source Python web/metrics libraries and best-practice patterns before you code, then implement the service in app.py and tests in tests/test_app.py.
```

### 355. D13_s983621_zh (domain=D13, difficulty=7)

```
从零做一个用于产品分析和实验读数的 Python 工具包，支持 A/B 实验读数、漏斗和 cohort 分析，外加一个最小 CLI。把核心库、CLI、单元测试和 README 分开写，文件名你自己定，但要能直接跑起来。先去查一下现成库的 API/最佳实践，再按你的设计实现，不要依赖任何输入数据文件。
```

### 356. D13_s983647_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics experimentation toolkit from scratch that can power A/B readouts, funnel conversion analysis, and cohort retention views for an internal team. Please use current best practices and a few modern open-source libraries after checking the web for what’s standard right now, then deliver the code and a short README showing how to run it. No input files are provided — just create the tool, with a clean API/CLI and sensible defaults.
```

### 357. D13_s983655_en (domain=D13, difficulty=7)

```
Build a production-grade Python package from scratch for product analytics experimentation readouts. I need a small but realistic internal toolkit that can compute A/B test readouts, funnel conversion metrics, and cohort retention summaries from event-level product telemetry, with a clean CLI and importable library API.

Use current best practices by researching the relevant ecosystem first: compare at least two modern Python data/CLI libraries and verify any statistical methodology choices against up-to-date references before implementing. I do not have any input data files; generate a small synthetic dataset in-code for examples and tests.

Deliver the codebase as a complete repo with an importable core module, a CLI entrypoint, unit tests, and a README that explains usage and methodology. The implementation should include: metric definitions, experiment assignment handling, significance/readout output for binary conversion and continuous metrics, funnel step aggregation, cohort retention tables, and a way to serialize results as JSON.

Keep it modular enough that different parts can be owned independently and then integrated cleanly.
```

### 358. D13_s983710_en (domain=D13, difficulty=7)

```
Our product team needs a small internal analytics tool because we keep arguing about whether experiments are really moving the right customer behavior, and we want something we can use for quick readouts without waiting on a data scientist every time. Please build the code for a lightweight experiment analysis app from scratch that can show A/B test readouts, basic funnel performance, and simple cohort retention views for our product team. I want it to be usable as a local tool with clear instructions, and I want the implementation to follow current best practices for whatever stack you choose, so please research the right libraries and patterns first. Deliver the built code files and a short README explaining how to run it and what it does. There are no input files; the tool should work with sample data generation or built-in demo datasets that you create yourself.
```

### 359. D13_s983714_en (domain=D13, difficulty=7)

```
Build a small but production-minded product analytics experimentation toolkit from scratch for A/B readouts, funnel analysis, and cohort retention. I want this as real code, not a notebook and not a data-analysis writeup. There are no input files to start from; please design and implement the whole thing from scratch, including the data model, query/aggregation logic, and a usable interface.

The tool should let me define events with a canonical schema, ingest synthetic or user-provided event streams, and then compute the kinds of metrics I would use in product experimentation: experiment readouts with conversion lift and confidence intervals, funnel step conversion rates with drop-off, and cohort retention by signup date or first-event date. I care about practical definitions, so please make the behavior explicit: an exposure event should assign a user to variant A or B, a conversion event should count only after exposure when relevant, and funnels should deduplicate repeated events per user per step unless otherwise specified. For readouts, include at least absolute lift, relative lift, standard error or a confidence interval, and a clear way to handle zero denominators and missing groups. For cohorts, define a time-bucketed retention matrix based on first seen date, with week- or day-level buckets and a clear interpretation of “retained.”

I want the code to be structured so it can be extended later. Please include a clean core library for computing the metrics, plus a command-line interface or small API wrapper that exposes the main operations in a practical way. The interface should support running an experiment readout from a defined assignment mapping, computing a funnel from a list of ordered steps, and generating a cohort retention table from event timestamps. Since there are no input files, create a minimal synthetic data generator inside the project so the tool can be demonstrated immediately. Use widely accepted Python libraries where appropriate, but do the design research first so the implementation follows current best practices for statistical intervals, funnel semantics, and CLI/API ergonomics.

Please also include tests that cover the hard cases: users missing exposure, users who convert before assignment, multiple exposures for the same user, repeated funnel steps, empty cohorts, and bucket boundaries at day/week transitions. I want the final deliverable to be the built code files themselves, plus a short README explaining how to run the tool and what each metric means. Do not assume any starter repo; create everything needed from scratch.
```

### 360. D13_s983731_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics toolkit from scratch for A/B readouts, funnels, and cohorts, with a simple CLI and a reusable library I can drop into a Python project. Please research the best-fit open-source pieces and patterns first, then implement the code, tests, and a short README showing how to use it with synthetic event data only—no input files, just generated examples. I want something that can calculate experiment readouts, funnel conversion steps, and cohort retention, and expose those through a clean command-line interface.
```

### 361. D13_s983755_en (domain=D13, difficulty=7)

```
I need you to build a small from-scratch product analytics toolkit for A/B readouts, funnels, and cohorts that I can run locally from the command line, with a clean README and basic tests. Please research a few current best-practice libraries/APIs first, then implement the core logic, a simple CLI, and example outputs so I can use it on event streams later without any input files. The goal is a realistic internal tool for experiment analysis, not a one-off script.
```

### 362. D13_s983791_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics toolkit from scratch for experiment readouts: a service that can take event data, compute A/B test summaries, funnel conversion, and cohort retention, and expose it through a simple CLI plus a lightweight API. Please research current best practices and any useful open-source libraries for stats and time-series handling before coding, then produce the code, tests, and a short README showing how to run it. There are no input files — just build the tool and include a few synthetic examples in the repo so the endpoints and commands can be demonstrated.
```

### 363. D13_s983830_en (domain=D13, difficulty=7)

```
We need a lightweight product analytics tool for our team so we can understand how experiments are performing without waiting on a data team. Build a small web app from scratch that lets me define an A/B test, load sample event data through the app, and then see a plain-English readout with funnel conversion, cohort retention, and basic experiment results side by side. Please also make it possible to compare two segments and export the summary as a downloadable report. I want the code, setup instructions, and a short README so someone on the team can run it locally and use it right away.
```

### 364. D13_s983844_en (domain=D13, difficulty=7)

```
I want a small but realistic product analytics tool built from scratch for experiment readouts.
- Build a command-line app that lets me define an A/B test, record event counts, and generate a readout with uplift, confidence intervals, and basic significance checks.
- Include funnel and cohort views so I can compare step conversion and retention between variants.
- Use a sensible stack and whatever libraries are best supported right now, but verify design choices with current docs or examples first.
- Keep it self-contained with no input data files; ship the code, tests, and a short README showing how to run it.
- Make sure the design is production-minded enough to extend later to a web API.
```

### 365. D13_s983959_zh (domain=D13, difficulty=7)

```
我需要你从零搭一个面向产品分析和实验读数的轻量工具，最好先做成一个可运行的命令行小项目：能输入一段事件定义和实验配置，自动产出 A/B 读数、漏斗转化和分群留存的汇总结果，还要带上基础校验、异常检测和一份使用说明。代码、测试和文档都要一起给我，项目结构尽量清晰，后面我可以直接接到真实埋点数据上用。
```

### 366. D13_s983980_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics readout tool from scratch: give me the code for a CLI app that can compute A/B experiment summaries, basic funnel conversion, and simple cohort retention from event logs, plus a short README showing how to run it. Please make it realistic for a modern stack, use current best practices for experiment stats and package choices, and don’t assume any starter data — just build the tool and its tests.
```

### 367. D13_s984028_en (domain=D13, difficulty=7)

```
Build a from-scratch Python tool for product analytics readouts: a small local service that takes event specs in code, computes experiment A/B stats, funnels, and cohort retention, and exposes them through a CLI plus a minimal HTTP API. I want app.py, analytics.py, tests/, and README.md; use current best practices and whatever libraries you confirm are appropriate via web research, but don’t use any input files or sample datasets.
```

### 368. D13_s984045_en (domain=D13, difficulty=7)

```
We need a small internal product analytics tool because our team keeps debating experiment results by hand, and we need something that can quickly show A/B readouts, funnel drop-off, and simple cohort retention without relying on spreadsheets. Please build the code for a lightweight web app from scratch that lets a user define an experiment, paste event names and dates, and then see a clear readout for experiment comparison, funnel conversion, and cohort retention in one place. I want the app code, a short README, and basic tests so we can hand it to engineering for review. Please use current best practices for the stack and data visualization approach, and research any good lightweight libraries or patterns before you build it.
```

### 369. D13_s984050_zh (domain=D13, difficulty=7)

```
帮我从零做一个产品分析实验读数工具：做成一个本地可运行的 Python 包和 CLI，支持 A/B 实验读数、漏斗分析、分群 cohort、以及最基本的显著性判断。先用 web 查一下现在常用的实现方式、推荐库和业界实践，再开始写代码；不要用现成分析文件，直接从零搭框架、核心逻辑、测试和文档。输出 `app.py`、`analytics/` 目录、`tests/` 和 `README.md`，能直接本地跑起来。
```

### 370. D13_s984058_en (domain=D13, difficulty=7)

```
Build a small open-source experimentation analytics tool from scratch for product teams, focused on A/B readouts, funnel analysis, and cohort retention. I want the code, a short README, and enough tests that someone could actually run it locally.
- Make it ingest event-level JSON or CSV data and compute experiment lift/readout, funnel conversion, and cohort retention.
- Include a simple CLI or local API so a PM can run a report without notebooks.
- Use web research first to choose a sensible stack and borrow current best practices for experiment stats, funnel semantics, and cohort definitions.
- Keep it modular so the core analytics engine, interface, and tests can be worked on separately and then integrated.
- Document how to use it with a small synthetic example dataset generated in code, since no input files are provided.
```

### 371. D13_s984166_en (domain=D13, difficulty=7)

```
I want a small product-analytics experimentation service built from scratch, not a notebook or analysis on a CSV.
- Build an A/B experiment readout engine that can take event definitions and compute lift, funnel conversion, and cohort retention for variants.
- Expose it as a simple local API or CLI so I can point it at synthetic in-memory data and get a readable result.
- Make the design realistic: use an actual Python analytics stack and follow current best practices for stats, event modeling, and testability.
- Include clear docs for how the engine works, how to run it, and how to extend it with new metrics.
- I also want a compact test suite that covers the main experiment scenarios and edge cases.
```

### 372. D13_s984305_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics toolkit from scratch for A/B readouts, funnels, and cohorts, with a simple CLI or web API that can ingest event streams, define experiments and conversion windows, and spit out a readable experiment summary plus funnel and cohort reports. Please research a couple of current Python libraries and best practices first, then implement the code, tests, and a short README so I can run it locally without any starter data.
```

### 373. D13_s984374_zh (domain=D13, difficulty=7)

```
从零构建一个产品分析工具，支持A/B测试显著性检验、漏斗转化分析和同期群留存计算。工具直接解析用户提供的CSV数据（从标准输入或文件路径读取），无需任何内置数据文件。用Python实现，包含命令行界面和单元测试。需要支持至少三种A/B检验方法（卡方检验、Fisher精确检验、贝叶斯A/B测试），漏斗转换支持多步骤，同期群留存支持按周/月配置。输出格式为ASCII表格。所有代码放在单个文件product_analytics_tool.py中，附带README.md。
```

### 374. D13_s984544_zh (domain=D13, difficulty=7)

```
我需要一个轻量级的Python工具，支持A/B测试统计显著性检验、漏斗转化率分析和同期群留存计算。请从零开始构建：核心模块（src/product_analytics/）、CLI（使用Click）、单元测试和README文档。直接给出所有代码文件，并用web搜索最新的scipy用法和Click最佳实践。
```

### 375. D13_s984663_en (domain=D13, difficulty=7)

```
Build a from-scratch product analytics experiment readout tool for A/B tests with funnels and cohorts. I want a small Python app with a CLI and a minimal web UI that can define events, calculate conversion/readout metrics, compare variants, and export a JSON summary; include README.md and tests. Use current best practices and a couple of relevant open-source libraries only if they fit.
```

### 376. D13_s984741_en (domain=D13, difficulty=7)

```
We need a small internal product analytics tool we can use for A/B test readouts, funnel checks, and cohort retention without waiting on a data team. Please build it from scratch as working code, because the goal is to give product managers a simple way to define an experiment, see the result summary, and compare funnel drop-off and retention over time. I want a lightweight web app or command-line tool that lets us enter events by hand or through a simple JSON API, then automatically shows experiment readouts, funnel conversion, and cohort views in a clear format. Please also include the setup instructions and a short README so our team can run it locally and understand how to use it.
```

### 377. D13_s984860_zh (domain=D13, difficulty=7)

```
我们现在要把产品团队每周看板里最费时间的部分自动化：围绕 A/B 实验的结果解读、漏斗转化和 cohort 留存，做一个从零开始的内部分析工具。它不要依赖任何现成报表，也不要用外部样例数据；我希望你直接帮我搭一个可运行的代码项目，能让分析同事输入一份事件定义和实验信息后，自动生成一份清晰的读数结果，包括实验组对照组对比、漏斗每一步转化、以及按周/按首访日期分组的 cohort 留存。请你先查一下适合的开源库、常见做法和最佳实践，再把功能设计成一个简单但专业的命令行或轻量服务。最后请把代码、说明和基础测试一起给我，方便我们后面接真实埋点数据接入。
```

### 378. D13_s984897_en (domain=D13, difficulty=7)

```
We need a small internal analytics tool for our product team so we can understand A/B test results, funnel drop-off, and cohort retention without waiting on the data team every time. Please build the code from scratch for a lightweight web app or command-line tool that lets us define an experiment, compare two variants, inspect a funnel, and view simple cohort retention summaries. I want something practical that we could actually use to review launch decisions, with a clean interface, sensible defaults, and clear output we can share with leadership. Please research the best current open-source libraries or patterns for the implementation before you build it, then deliver the working code and a short README that explains how to run it and what it does.
```

### 379. D13_s984964_en (domain=D13, difficulty=7)

```
Build a from-scratch Python tool called `experiment_readout` for product analytics that takes event-level experiment data and outputs A/B readouts, funnel conversion summaries, and cohort retention tables. I need `README.md`, `src/experiment_readout.py`, and a small test suite; include a CLI and a minimal JSON report export.
```

### 380. D13_s985059_en (domain=D13, difficulty=7)

```
Build a from-scratch Python tool called `experiment_readout.py` plus `README.md` that computes A/B experiment readouts, funnel conversion, and basic cohort retention from event-level data, with a small CLI for running analyses and exporting JSON/CSV summaries. Use current best-practice libraries and patterns you verify online before coding, then implement everything yourself—no starter code or data files.
```

### 381. D13_s985085_en (domain=D13, difficulty=7)

```
I need you to build a small product analytics toolkit from scratch for A/B readouts, funnels, and cohorts — something I can actually run locally to summarize experiment results and basic retention without any input files. Please research a sensible Python stack and a couple of modern analytics libraries or design patterns first, then implement the code, tests, and a short README. The tool should let me define events, users, experiments, and date ranges in code, and it should output clean readout tables and charts for experiment lifts, funnel conversion, and cohort retention.
```

### 382. D13_s985285_en (domain=D13, difficulty=7)

```
Build a from-scratch internal experimentation analytics tool for product teams that can evaluate A/B test readouts, funnel performance, and simple cohort retention without relying on any input datasets. I want a small but production-shaped implementation that includes: a core metrics engine, a configurable event-schema model, a command-line interface for running analyses on synthetic in-memory event streams generated by the tool, and a concise README with usage examples and design notes. Use current best practices for statistical readouts and experiment guardrails, and research a couple of relevant Python libraries or implementation patterns before coding so the design matches modern conventions. The output should be the code files and README, ready to run locally.
```

### 383. D13_s985301_en (domain=D13, difficulty=7)

```
I need you to build a small from-scratch product analytics toolkit for experiment readouts, funnels, and cohorts — something I can run locally on synthetic event data to compare A/B variants, inspect funnel drop-off, and view cohort retention. Please research a couple of good open-source patterns or libraries first, then implement the code, tests, and a short README so it’s usable without any input files.
```

### 384. D13_s985407_zh (domain=D13, difficulty=7)

```
帮我从零写一个可发布的产品分析实验读数工具，支持 A/B 实验结果判定、漏斗转化、以及 cohort 留存分析，代码和 README 都要补齐。优先用 Python 做成一个可安装的小工具/库，文件结构你自己定，但要有清晰的核心模块、命令行入口、单元测试和示例用法。
```

### 385. D13_s985412_zh (domain=D13, difficulty=7)

```
我们现在要把产品分析做得更自动化，方便我和增长团队每天看 A/B 测试结果、漏斗转化和用户留存，不用再手工拼表。请从零做一个可运行的分析小工具，最好能在本地先跑起来：它要能接收我们自己生成或手动输入的事件数据，支持按实验分组做 A/B 读数、做基础漏斗分析、做简单 cohort 留存查看，并输出一份清楚的结果页面或报告。你来决定合适的技术方案，但希望代码结构清晰、后面好扩展，也把关键计算逻辑和展示层分开。请顺手把你参考过的实现思路、适合用的库、以及你为什么这么设计，整理成简短说明一起给我。不要依赖现成的数据文件，直接从头实现。
```

### 386. D13_s985686_en (domain=D13, difficulty=7)

```
I need you to build a small from-scratch product analytics toolkit for A/B readouts, funnels, and cohorts that I can run locally on synthetic event data, with a clean Python package plus a simple CLI or demo app and a README. Please make it feel like a real internal experimentation tool: support event ingestion, experiment assignment, metric readouts, funnel conversion, cohort retention, and a basic report export, and use current best practices from existing analytics libraries/docs where useful.
```

### 387. D13_s985756_en (domain=D13, difficulty=7)

```
Build a from-scratch Python tool for product analytics experimentation: a small A/B readout engine that computes experiment summaries, funnel conversion, and cohort retention from in-memory event streams, with a CLI and a JSON output mode. Use modern best practices from current docs for pandas/statistics/CLI design, and include README.md plus tests.
```

### 388. D13_s985792_en (domain=D13, difficulty=7)

```
Build a from-scratch lightweight experimentation readout service for product analytics: I want a small Python app with an API and CLI that can compute A/B test readouts, funnel conversion, and simple cohort retention from event streams, then export results as JSON and Markdown. Use FastAPI, pandas or polars, and add a clean README plus tests; name the main files app.py, analytics.py, cli.py, and tests/.
```

### 389. D3_s981531_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team that can clean messy KPI data, flag unusual spikes or drops, and show a simple dashboard so managers can quickly see what changed day to day. Please build the code from scratch, not using any sample files, so we can plug in our own data later. I want a working app with a clear way to define columns like date, team, metric value, and status, plus a clean view that highlights anomalies and basic KPI summaries. Please use current best practices for the stack and pick libraries that are well supported today. Deliver the code and a short README that explains how to run it and what it does.
```

### 390. D3_s981556_zh (domain=D3, difficulty=7)

```
我要做一个从零开始的工程化小工具，不要基于任何现成数据文件，目标是帮助运营团队做日常数据质检和指标看板。

- 请实现一个 Python 项目：支持对一批“手工传入的指标记录”做清洗、异常检测和 KPI 汇总，并输出可视化报表。
- 重点要有一个可复用的核心库，再加上命令行入口；我希望能直接运行本地命令生成 HTML 报告和 JSON 结果。
- 清洗规则、异常检测方法、KPI 口径、图表方案请先做一次简短调研后再设计，尽量参考业界常用做法和成熟库的最佳实践。
- 代码要能独立运行，附带单元测试、基本文档和示例用法；不要依赖外部数据源，示例数据请在代码里构造。
- 这个任务请按模块拆分，方便并行开发后再集成，最后给我完整可运行的代码仓库内容。
```

### 391. D3_s981569_en (domain=D3, difficulty=7)

```
Build a small from-scratch Python tool for a data ops team that cleans event-like records, flags anomalies, and outputs KPI summaries plus a simple visualization. I want it to be usable as a local utility, not a notebook.
- Include a core library that can normalize messy timestamps, deduplicate rows, standardize category fields, and handle missing values in a configurable way.
- Add anomaly detection for time-series KPIs and record-level outliers, with a reasonable default approach based on current best practices from modern Python libraries.
- Expose it through a CLI that can ingest JSON/CSV-like records from stdin or generated sample data, then print a KPI report and optionally save a chart.
- Add tests and a short README showing installation, usage, and a couple of example commands.
- Use web research to choose the right libraries/patterns for plotting, CLI design, and anomaly detection before implementing it from scratch.
```

### 392. D3_s981595_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for cleaning and monitoring operational KPI streams in a retail analytics workflow. I need a small but production-minded package that ingests synthetic in-memory event records only, standardizes messy fields, detects anomalies in daily KPI aggregates, and renders a browser-based dashboard with trend lines, control limits, and a data-quality panel. Use current best practices for anomaly detection and plotting libraries after checking up-to-date docs/examples for pandas, scikit-learn or statsmodels, and a modern visualization stack such as Plotly or Altair. Do not rely on any input files; generate representative test data inside the code and expose a clean public API plus a CLI entrypoint. Deliver the built code and a concise README explaining architecture, assumptions, and how to run the demo.
```

### 393. D3_s981614_zh (domain=D3, difficulty=7)

```
我需要做一个面向运营团队的异常数据处理和看板小工具，解决我们每天看关键指标时要手工清洗、排查异常、再汇总成 KPI 的问题。希望你从零开发一个可运行的 Python 工具，能让用户输入几列原始数值后自动完成清洗、异常点识别、基础 KPI 计算，并生成一个简单的可视化报表页面或图表文件，方便给管理层看。这个工具最好支持命令行启动，能保存结果，也要把每一步处理说清楚，便于以后扩展到真实业务数据。请你自己先查一下适合的开源库、图表方案和异常检测做法，再按你判断的最佳方式实现，最后把代码和说明文档一起给我。
```

### 394. D3_s981615_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team that can turn messy monthly business metrics into something we can trust and act on. Right now, our KPI numbers are being checked by hand in spreadsheets, and that’s too slow and too easy to miss bad data. Please build a clean, from-scratch Python tool that lets us define a set of KPIs, validate incoming records, flag anomalies, and generate a simple visual summary dashboard we can share with management. I do not have any input files for you — please build the tool itself, with sensible sample/demo data if needed to show it working. Please research current Python libraries and best practices first so the solution uses a practical approach for data cleaning, anomaly detection, and charting. Deliver the code and a short README that explains how to run it and what it does.
```

### 395. D3_s981620_zh (domain=D3, difficulty=7)

```
帮我从零做一个 Python 工具：`kpi_guard/`，用于生成和监控数据处理 KPI 仪表盘，包含数据清洗、异常检测和指标计算三部分。需要你先查清楚可用的库和最佳实践，再直接写代码、测试和 README，别用现成模板。输出 `src/`、`tests/`、`README.md` 和一个可运行的命令行入口，能本地生成 HTML 报表。
```

### 396. D3_s981623_zh (domain=D3, difficulty=7)

```
我需要你从零做一个数据处理和可视化的小工具，面向运营看板用：用 Python 做一个命令行 + 本地 Web 页面应用，支持手工生成模拟指标数据、清洗缺失值和重复值、做简单异常检测、自动汇总核心 KPI，并把结果画成时间序列图和告警列表。不要给我现成数据文件，直接把代码、README 和测试都写出来，最好还能让我一键运行；如果需要选库、选图表方案、异常检测做法，就先去查一下现在主流做法和相关库文档再定。
```

### 397. D3_s981627_en (domain=D3, difficulty=7)

```
I need a small internal tool for our operations team that turns messy daily service metrics into something we can trust and act on. The goal is to clean incoming records, flag unusual spikes or drops before we send the report, and produce a simple KPI dashboard view we can share with managers. Build it from scratch as working code, not a mockup. Please include the code files and a short README explaining how to run it. I’m not giving you any source files, so the tool should generate its own sample data for demonstration and include the cleaning, anomaly detection, and KPI summaries in one flow.
```

### 398. D3_s981640_en (domain=D3, difficulty=7)

```
I want a small but real from-scratch tool for data quality monitoring and KPI reporting. Build a Python app that lets me define a schema, clean incoming event records, flag anomalies, and generate a simple dashboard-ready summary.
- Include a CLI for loading JSON/CSV event streams, running validation/cleaning, and exporting KPI summaries.
- Add anomaly detection for both missing-value spikes and metric outliers, with configurable thresholds.
- Produce an HTML or markdown report with key KPIs, detected anomalies, and a short explanation of the cleaning steps taken.
- Use current best-practice libraries and patterns for data validation, time-series aggregation, and lightweight visualization, and briefly justify the choices.
- Ship the code, tests, and a README with setup and usage examples; no input files are provided, so create your own sample data generator or fixtures in the project.
```

### 399. D3_s981646_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for our ops team called DataPulse: it should clean messy event data, flag anomalies, and generate KPI summaries plus a simple HTML dashboard. I want the code in app.py, tests in tests/, and a README.md with setup and usage; no input files, generate your own sample data in code for demos. Use current best-practice libraries/APIs where useful and make it runnable locally.
```

### 400. D3_s981670_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for product KPI monitoring: `kpi_monitor/` with anomaly detection on streaming metrics, a small FastAPI service, and a Plotly-based HTML dashboard. I want `README.md`, `app.py`, and the core package files; no input files, synthesize demo data inside the code and make the pipeline configurable.
```

### 401. D3_s981673_zh (domain=D3, difficulty=7)

```
帮我从零写一个可运行的 Python 工具：做日志/指标数据清洗、异常检测和 KPI 看板，支持命令行跑本地计算并输出 HTML 报告。请直接给出代码文件和 README，别假设有现成数据；需要你自己设计示例数据生成、规则配置和可视化。
```

### 402. D3_s981675_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool for an internal ops dashboard that ingests raw service metrics, cleans and normalizes them, flags anomalies, and computes a few KPIs with a simple visual report. There are no input files yet, so please create the code, CLI, and a sample synthetic-data generator yourself, and make it flexible enough to plug into CSV or JSON later. I want the finished code files plus a README that explains how to run it, what the anomaly logic does, and how the KPI summary and charts are generated.
```

### 403. D3_s981692_zh (domain=D3, difficulty=7)

```
帮我从零设计并实现一个可本地运行的“数据质量与KPI监控”小工具，面向团队每周看板使用，不要依赖任何现成输入文件。请做成一个能直接跑的代码项目，重点是清洗、异常检测和KPI可视化。

- 需要支持我在代码里定义一份示例数据源配置，然后程序自己生成/处理数据并输出结果，不要要求我上传 CSV。
- 需要包含数据清洗流程、异常检测规则、KPI 计算，以及一个简洁的图表/仪表盘输出方式。
- 希望你顺便把命令行入口、配置方式、单元测试和使用说明都一起补齐。
- 如果需要选库或设计方案，请先查一下当前 Python 生态里常用做法，再定实现。
- 最终给我代码文件和 README，能让我按步骤运行、验证和扩展。
```

### 404. D3_s981704_zh (domain=D3, difficulty=7)

```
请从零做一个可落地的 Python 数据处理与可视化小工具，目标是把“原始运营指标”清洗、检测异常并输出可视化 KPI 报告，适合内部周报/日报使用。
- 需要支持命令行运行，能读取用户指定的 CSV/JSON 数据源，自动做字段标准化、缺失值处理、重复记录去重和基础校验。
- 需要实现一套通用的异常检测逻辑（比如对时间序列指标的突增/突降、缺失、重复、波动异常做标记），并能生成可解释的异常摘要。
- 需要输出 KPI 面板图和异常明细图，最好能导出为 HTML 报告或静态图片，方便直接分享给业务同事。
- 需要附带一份 README，说明安装、运行方式、参数含义、数据格式要求和典型使用场景。
- 请你直接交付代码文件和必要文档，不要假设我已经有现成数据；代码里可以带一个可运行的示例数据生成器或 demo 流程。
```

### 405. D3_s981711_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch for our ops team that ingests live CSV/JSON exports from our internal event pipeline, cleans and standardizes the fields, flags anomalies, and outputs a KPI dashboard summary plus a simple web chart view. There are no starter files — just create the code, tests, and a README, and use web research where needed to pick sensible libraries and patterns for streaming-friendly cleaning, anomaly detection, and lightweight visualization.
```

### 406. D3_s981715_en (domain=D3, difficulty=7)

```
Our ops team needs a small internal tool for cleaning messy KPI data, spotting unusual spikes or drops, and turning it into a simple dashboard we can use in weekly reviews. I want this built from scratch as code, not based on any uploaded sample data, and I want the solution to be practical enough that a non-data person can run it locally and get a clear view of the numbers. Please research a sensible open-source stack first, then build the tool with a clean way to define metrics, run data checks, flag anomalies, and show the results in a visual report. I’d like the finished code and a short README so someone else on the team can install it, run it, and understand what it does.
```

### 407. D3_s981722_en (domain=D3, difficulty=7)

```
Build a small Python toolkit for real-time ops data quality monitoring: ingest JSON events, clean and normalize fields, detect spikes/anomalies, and compute KPI summaries for latency, error rate, and throughput. I want the code in src/ plus a CLI, a FastAPI endpoint for triggering runs, tests, and a README.md with setup and examples—no input files, just implement it from scratch.
```

### 408. D3_s981728_en (domain=D3, difficulty=7)

```
I want a small from-scratch Python tool for product ops that can clean event logs, flag anomalies, and surface KPIs in a lightweight dashboard.
- Build it as a real reusable package, not a notebook or one-off script.
- Include a CLI that can generate synthetic demo data, run the pipeline, and export results.
- I need a simple web dashboard or local HTML report showing KPI trends, anomaly markers, and data-quality issues.
- Use current best-practice libraries for validation, plotting, and anomaly detection, chosen after quick web research.
- Add tests and concise setup instructions so someone can run it locally with no input files.
```

### 409. D3_s981737_zh (domain=D3, difficulty=7)

```
我需要你从零搭一个用于“数据清洗 + 异常检测 + KPI看板”的小工具，面向电商日常运营数据：支持把实时/批量 CSV 或 JSON 记录清洗、去重、统一时间格式，按规则识别异常波动，并生成一个可在本地打开的交互式 KPI 仪表盘页面。请把代码、基础测试和 README 一起做出来，最好顺手把配置文件也补上；实现时你需要先查一下适合前端图表、数据校验和异常检测的主流 Python 库与最佳实践，再决定技术方案。不要用任何现成数据文件，我不提供输入样本，代码里自己生成演示数据和默认配置即可。
```

### 410. D3_s981768_zh (domain=D3, difficulty=7)

```
帮我从零实现一个可本地运行的“数据质量监控与KPI仪表盘”工具，支持手动生成模拟业务数据、做清洗/异常检测、计算关键KPI，并输出一个可交互的HTML报表。把代码拆成清晰模块，至少包含数据生成、清洗规则、异常检测、KPI汇总、可视化和命令行入口，顺手补一版README和单元测试。
```

### 411. D3_s981787_zh (domain=D3, difficulty=7)

```
我们现在要把每天零散的运营数据变成一个能直接给管理层看的工具，重点是尽早发现异常、自动算出核心 KPI，并且让非技术同事也能一眼看懂趋势。我要你从零开始做一个可运行的小型数据处理与可视化工具，不要依赖任何现成数据文件，也不要假设我已经有模板；请你自己设计一套合理的示例数据结构、清洗规则、异常检测逻辑和仪表盘展示方式。这个工具最好能支持我以后接入门店销售、订单、库存这类常见业务数据：先把脏数据清理掉，再自动标出异常点，最后生成一页清晰的 KPI 和图表页面。请直接交付完整代码和说明文档，方便我后面让团队继续接入真实数据源。
```

### 412. D3_s981800_en (domain=D3, difficulty=7)

```
Build a small from-scratch data quality and KPI monitoring tool for a SaaS operations team, with a simple local dashboard and a CLI. I want it to ingest synthetic or user-provided CSVs, clean common issues, detect anomalies, and compute business KPIs without relying on any starter dataset.

- Use web research to pick sane library choices and best practices for a Python implementation of cleaning, anomaly detection, and lightweight visualization.
- Implement the core engine, a CLI, and a local dashboard that shows data quality issues, KPI trends, and anomaly flags.
- Include a rule-based cleaning pipeline plus one statistical anomaly detector, both configurable.
- Add a short README with setup/run instructions and design notes.
- Make sure it works on synthetic data generated inside the tool so there are no input files required to get started.
```

### 413. D3_s981818_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for cleaning operational metrics, detecting anomalies, and generating KPI summaries for a SaaS support dashboard. I want app.py, kpi_engine.py, anomaly_detector.py, and README.md; include a small CLI plus a simple HTML report output with charts, but do not use any input files or starter dataset. Research best-practice libraries/APIs for time-series anomaly detection and plotting before you implement it.
```

### 414. D3_s981825_zh (domain=D3, difficulty=7)

```
帮我从零做一个面向运营数据的“小型数据质量与 KPI 监控工具”，不要依赖任何现成输入文件，代码里自己造一套可运行的示例数据和演示流程。
- 要能做基础清洗：字段标准化、缺失值处理、重复记录识别、异常值标记。
- 要能做异常检测和 KPI 汇总：比如按日/周生成转化率、活跃度、客单价等指标，并对突增突降给出告警。
- 要提供一个可视化界面或可交互图表，能看到清洗前后、KPI 趋势和异常点；最好支持导出一份报告。
- 技术方案请结合一下当前主流 Python 生态，必要时查一下 pandas / polars、plotly / streamlit、以及异常检测相关的最佳实践，再决定实现方式。
- 最终请直接给我可运行的项目代码和 README，包含启动方式、功能说明、以及如何扩展规则的说明。
```

### 415. D3_s981828_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for warehouse KPI monitoring that cleans raw event logs, flags anomalies in throughput/latency, and renders a small dashboard with trend lines and alert summaries. Create app.py, dashboard.py, and tests/ covering the whole pipeline; I want the code and a short README.md with run instructions. Use current library patterns and recommended approaches for anomaly detection and plotting, but there are no input files — generate the sample data in code.
```

### 416. D3_s981840_en (domain=D3, difficulty=7)

```
Build a small Python package from scratch for cleaning streaming event data, flagging anomalies, and computing KPI summaries for a product analytics dashboard. I want `src/`, `tests/`, `pyproject.toml`, and a `README.md` with usage examples; include a minimal CLI and a JSON output mode. Use current best-practice Python libraries and patterns, but no input dataset — generate sample data in code for demos and tests.
```

### 417. D3_s981860_en (domain=D3, difficulty=7)

```
I want a small but real internal tool for our ops team: build a from-scratch Python dashboard that ingests live KPI data from a few REST endpoints, cleans it, flags anomalies, and shows the results in a browser.
- Use current web research to pick practical libraries and patterns for a lightweight data pipeline, anomaly detection, and a simple web UI.
- The app should support configurable KPI definitions, data cleaning rules, rolling-window anomaly detection, and a summary view with charts and alert status.
- Include a CLI to run the pipeline on demand, plus a local web server for the dashboard.
- I want the actual code/files, plus a short README explaining how to run it and extend it.
- No input files will be provided; create the project from scratch with synthetic/example configuration and tests.
```

### 418. D3_s981867_zh (domain=D3, difficulty=7)

```
我需要你从零做一个用于“数据清洗 + 异常检测 + KPI 看板”的小工具，目标是给中小团队用来把原始指标数据标准化、自动标记异常、再生成一个可交互的本地仪表盘。请直接产出可运行代码和 README，建议做成 Python 项目，最好包含一个命令行入口、核心处理模块、一个轻量可视化页面（例如 Streamlit 或 Plotly Dash），并把清洗规则、异常检测逻辑和 KPI 口径都写清楚；项目里不要依赖现成数据文件，初始化后应能用你自己生成的示例数据跑通并展示效果。
```

### 419. D3_s981918_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team to keep an eye on daily metrics without waiting for an analyst. The goal is to build a clean, from-scratch dashboard app that can take in raw KPI numbers we paste in, clean up messy entries, flag unusual changes, and show the results in a simple visual view so managers can spot problems fast. Please build the code for the app and include clear setup instructions. I do not have any input files to provide — this should work with pasted data or sample data generated by the app itself. Please use modern, practical approaches for data cleaning, anomaly detection, and charting, and make sure the design reflects current best practices from the web.
```

### 420. D3_s981924_en (domain=D3, difficulty=7)

```
Build me a small Python tool for KPI monitoring: clean streaming-ish event logs, flag anomalies, and render a simple KPI dashboard. I want the code in app.py plus a README.md with setup and usage, and I want it to be built from scratch with no starter data files. Use current best practices for anomaly detection and charting libraries; look up what’s reasonable before you code.
```

### 421. D3_s981926_en (domain=D3, difficulty=7)

```
Build a Python tool from scratch for cleaning, anomaly detection, and KPI reporting on operational event data. I want `kpi_cleaner.py`, `dashboard.py`, and `README.md` with a CLI that ingests newline-delimited JSON from stdin, normalizes timestamps/units, flags anomalies, and outputs a KPI summary plus an HTML chart. Use current best practices for pandas/plotly/typer, and check any relevant library docs before coding.
```

### 422. D3_s981927_zh (domain=D3, difficulty=7)

```
我需要你从零做一个用于数据清洗、异常检测和KPI展示的小工具，最好做成一个可直接运行的 Python 项目：能接受命令行参数，生成一组模拟业务数据（比如订单、转化率、收入、缺失值和异常波动），再自动做清洗、识别异常、计算几个常见KPI，并把结果输出成一个带图表的HTML报告和一个简洁的CLI摘要；你可以顺手把项目结构、核心代码、测试和README都补齐，尽量用现在常见、靠谱的库和实现方式。
```

### 423. D3_s981939_zh (domain=D3, difficulty=7)

```
我需要你从零做一个数据处理与可视化的小工具，目标是给电商/运营团队用来做清洗、异常检测和 KPI 看板：用 Python 直接搭一个可运行的命令行或小型 Web 应用，能接收用户手动粘贴的 JSON/CSV 字符串或在界面里直接输入模拟数据，自动做字段清洗、重复/缺失处理、基础异常检测，并生成日、周、月维度的核心 KPI 和可视化图表；同时把项目结构、安装运行方式、核心逻辑和示例用法一起写清楚，最好顺手把代码、测试和 README 都补齐。不要依赖现成模板，代码和界面都要自己实现。
```

### 424. D3_s981962_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for weekly SaaS KPI monitoring: ingest raw events from stdin or a pasted JSON blob, clean duplicates/missing timestamps, detect anomalies in usage/revenue metrics, and render a small HTML dashboard with charts and KPI cards. I want the code in app.py, tests in tests/test_app.py, and a short README.md with setup and usage.
```

### 425. D3_s981963_zh (domain=D3, difficulty=7)

```
我需要你从零做一个数据处理和可视化小工具，目标是把一堆订单/运营指标的原始记录清洗、自动找异常、算关键 KPI，然后在本地生成一个可交互的仪表盘和导出的报告文件。你直接帮我把代码、测试、README 和示例配置都写出来，最好用 Python 做成一个可运行的项目，支持命令行跑批、输出 HTML 图表和 Markdown 摘要，不要依赖现成数据文件，自己用模拟数据也要把流程搭完整。帮我顺手把清洗规则、异常检测方案、图表库和打包方式都定下来，保证别人拉下来就能跑。
```

### 426. D3_s981964_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool for data processing and visualization that can ingest CSV or JSON event data, clean it up, flag anomalies, and generate a KPI dashboard-style HTML report with charts and summary metrics. Please make it practical for ops/finance style time series data, include a simple CLI, and add tests plus a README so someone can run it locally. No input files are being provided, so design the schema, sample data generator, and the whole workflow yourself.
```

### 427. D3_s981966_en (domain=D3, difficulty=7)

```
I need a small internal tool that helps us catch bad operational data before it reaches our weekly KPI dashboard. We keep seeing missing values, duplicate records, sudden spikes, and weird metric changes, and I want something we can run on our own systems without uploading any files anywhere. Please build the code from scratch for a lightweight data-quality and anomaly-checking app that can take a CSV or a pasted table, clean the data, flag suspicious rows, and show a simple KPI summary with charts. I want the finished code files plus a short README that explains how to run it, what checks it performs, and how to customize the thresholds. Please use current best practices and choose the most practical open-source libraries after checking what’s available now.
```

### 428. D3_s981996_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for cleaning and KPI monitoring of operational event streams: I want a small library plus CLI in `src/` that ingests synthetic JSON events, deduplicates them, detects anomalies in rolling KPIs, and renders an HTML dashboard with charts. Research and pick a solid stack for charting, CLI parsing, and anomaly detection first, then implement it and include tests and a README with usage examples.
```

### 429. D3_s982001_zh (domain=D3, difficulty=7)

```
我需要你从零做一个数据处理和可视化的小工具，目标是把一组销售/运营事件流数据清洗、自动识别异常、算出几个核心 KPI，然后生成一个能直接打开看的交互式仪表盘；不要假设有现成数据文件，代码里自己造一份可重复的示例数据并提供可复用的数据管道。最好把代码拆成清晰的模块，前端可视化用你查到的成熟方案来选型，另外补一份 README 说明怎么运行、怎么扩展规则和指标。最后把完整可运行的代码文件都给我。
```

### 430. D3_s982014_en (domain=D3, difficulty=7)

```
We need a small internal tool for our ops team that can take in fresh daily sales and store performance data later, but for now it should be built from scratch with no starter files so we can wire it into our pipeline ourselves. The main goal is to clean messy records, flag unusual spikes or drops, and show a simple KPI dashboard so managers can spot problems fast without digging through spreadsheets. Please build the code and supporting files from scratch, using sensible libraries and current best practices you research first, and make it easy to run locally with clear instructions. I want the result to include the working application code, the anomaly detection and data cleaning logic, and enough tests and documentation that another developer can pick it up and extend it.
```

### 431. D3_s982034_zh (domain=D3, difficulty=7)

```
帮我从零做一个 Python 项目：把“数据质量监控 + 异常检测 + KPI 看板”做成一个可复用的本地工具，包含核心库、CLI 和一个 Streamlit 可视化页面，代码直接放到指定文件里。不要用现成模板或示例数据文件，自己在代码里生成演示数据；实现清洗规则、异常检测、KPI 计算、图表展示和基础测试。
```

### 432. D3_s982037_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch data quality monitoring tool for an e-commerce dashboard: it should ingest JSON events from stdin or a file, clean and normalize the records, detect obvious anomalies in key metrics like orders, revenue, and conversion rate, and generate a simple HTML/Markdown KPI report with charts and an alert summary. Please include the code files, tests, and a README with setup and usage, and use current best-practice libraries or patterns only after checking the web for what’s appropriate.
```

### 433. D3_s982039_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team that can clean messy daily KPI data, flag unusual spikes or drops, and turn it into a simple dashboard so managers can spot issues fast. Build it from scratch as a real code project, not a notebook or a one-off analysis. I want the finished code files plus a short README, and I need you to research the best lightweight Python libraries and current practices for validation, anomaly detection, and charting before you build it. The tool should work without any input files included in the request, so create it to accept pasted CSV or JSON data at runtime, normalize the fields, calculate a few core KPIs, detect suspicious values, and show the results in a clean web page or local app.
```

### 434. D3_s982070_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for an internal ops dashboard that cleans messy event logs, flags anomalies, and computes daily KPIs. I want the code in app.py plus a short README.md with run steps and examples; no input files, generate sample data in code for demos and tests. Research a sensible anomaly detection approach and plotting stack first, then implement the pipeline, CLI, and outputs.
```

### 435. D3_s982092_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for cleaning event-stream data and generating KPI/anomaly dashboards for a SaaS ops team. I want app.py, kpi_engine.py, anomaly_detector.py, charts.py, and README.md, with a CLI that can ingest JSON lines from stdin, compute rolling KPIs, flag anomalies, and export an HTML report plus PNG charts. Use current best-practice Python libraries after checking docs online, and wire it so I can run it locally with no starter data.
```

### 436. D3_s982096_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch data quality and KPI monitoring tool for ecommerce orders, with a CLI plus a simple dashboard that can clean messy records, detect anomalies in daily metrics, and flag broken KPIs before they hit a report. Please include the code files, tests, and a short README, and use current library/API docs where needed so the design is based on real, modern practices rather than guesses.
```

### 437. D3_s982108_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch for operational data quality monitoring: it should clean messy event records, detect anomalies in daily KPI streams, and render a simple dashboard/report from generated sample data with no input files required. Please research a couple of good open-source approaches for anomaly detection and plotting before coding, then give me the code files plus a short README with how to run it.
```

### 438. D3_s982128_en (domain=D3, difficulty=7)

```
Build a small Python app from scratch for cleaning event-stream data, flagging anomalies, and computing KPI summaries for a SaaS ops dashboard. I want app.py, kpi_rules.py, anomaly_engine.py, and README.md, plus a simple CLI that prints a markdown report and a JSON output. Do a quick web-backed design pass first on good Python libraries and anomaly-detection approaches, then implement it without any input files.
```

### 439. D3_s982129_zh (domain=D3, difficulty=7)

```
帮我从零做一个 Python 小工具，做数据清洗 + 异常检测 + KPI 看板，直接输出代码文件和 README。要支持生成一份可交互的本地 HTML 报告，包含清洗规则、异常点标记和 KPI 汇总卡片；不要依赖任何现成数据文件，默认用内置示例数据和随机模拟数据演示。顺手把常用库方案、图表方案和异常检测方法研究一下，按你查到的最佳实践来定实现。
```

### 440. D3_s982130_en (domain=D3, difficulty=7)

```
Build a from-scratch Python package for a retail ops KPI monitor: ingest CSV/JSON logs, clean messy timestamps and missing values, detect anomalies in daily revenue/order counts, and generate a small HTML dashboard plus CLI output. Make the core logic, CLI, tests, and docs in separate files; no input data files, just the code.
```

### 441. D3_s982173_zh (domain=D3, difficulty=7)

```
帮我从零做一个用于“数据处理与可视化”的小工具，目标是把一批原始业务指标记录清洗、异常检测并自动生成 KPI 仪表盘和周报摘要。

- 需要从零实现，不要假设我已经有现成数据文件；你可以自己定义示例输入格式和少量演示数据，重点是把处理流程、规则和输出做出来。
- 希望包含数据清洗、缺失值处理、异常值识别、KPI 计算和可视化渲染，最好能支持导出 HTML 报告或静态图表。
- 请顺手查一下适合这个场景的 Python/前端库和最佳实践，再决定技术方案；我希望代码结构清晰，后面能继续扩展。
- 最终交付我一套可运行的代码和 README，说明怎么安装、怎么运行、支持哪些输入字段、有哪些异常规则和 KPI。
- 如果你认为有必要，也可以补一个命令行入口或简单 API，但核心是把这套“清洗 + 异常检测 + KPI 看板”的工具真正做出来。
```

### 442. D3_s982177_zh (domain=D3, difficulty=7)

```
帮我从零做一个 Python 工具，做一个面向日志/指标数据的清洗 + 异常检测 + KPI 汇总 + 可视化仪表盘。直接产出代码文件和 README，要求能本地跑起来，别依赖现成数据文件，内置一套可模拟数据生成器和示例配置。
```

### 443. D3_s982183_zh (domain=D3, difficulty=7)

```
我们现在要把运营报表里的日常数据检查、异常提醒和核心指标看板做成一个能直接交付给业务团队用的工具，目的是减少人工盯数和漏报。请从零开发一个可运行的小工具：它要能接收一段手工粘贴的数据文本（比如 CSV 风格的表格内容，直接粘贴到界面里，不需要上传文件），自动做清洗、识别明显异常、计算几个常用 KPI，并把结果用一个简单的网页看板展示出来。希望它能支持至少 3 类常见问题，比如空值、重复记录、数值格式混乱；异常提醒要能解释为什么被标记；KPI 至少包括总量、环比变化、转化率这类业务常用指标。请你自己调研适合的前端图表、数据处理和异常检测实现方式，按最稳妥的方案从头搭建完整代码、测试和使用说明，最终交付可运行的代码文件和说明文档。
```

### 444. D3_s982189_zh (domain=D3, difficulty=7)

```
帮我从零写一个用于运营指标监控的 Python 小工具，别用现成模板。我要一个可运行的命令行项目，支持清洗日志/指标数据、异常检测、KPI 计算和生成一份简单的可视化报告；代码放到 `src/`，入口是 `main.py`，再补 `README.md` 和 `tests/`。实现时顺手查一下 pandas、polars、plotly、typer 这几类库的最佳实践，选一套最合适的方案直接落地。
```

### 445. D3_s982216_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch for cleaning and monitoring event data, with a simple dashboard that shows data quality KPIs and flags anomalies in volume, null spikes, and duplicate rates. Please create the code, tests, and a README, and use current web research to choose the right libraries and best-practice approach for charts, alert thresholds, and lightweight anomaly detection. There are no input files — the tool should generate or accept sample records at runtime so it can be run immediately and demonstrated end to end.
```

### 446. D3_s982228_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch for cleaning and monitoring operational data: it should expose a CLI plus a lightweight local dashboard that can load JSON/CSV records, normalize messy fields, flag anomalies in KPIs like counts and rates, and generate a clear summary report with charts and alerts. Please include the code files, tests, and a README, and do a quick web check first for good choices around pandas/polars, anomaly detection, and a simple plotting/dashboard library so the design is sensible.
```

### 447. D3_s982230_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team that can spot data issues early and give us a clean KPI dashboard without relying on spreadsheets. Build it from scratch so we can enter or generate records directly in the app, clean messy values, flag unusual spikes or drops, and show a few simple business KPIs in a web page we can share with leadership. Please make the code, a short README, and include basic tests so we can trust it before rollout. I want you to research the best lightweight approach for this, pick sensible open-source libraries, and build the whole thing so it can run locally with no external data files.
```

### 448. D3_s982236_en (domain=D3, difficulty=7)

```
Build me a from-scratch Python tool for cleaning and monitoring product-order data, with anomaly detection and KPI charts, and put the code in `src/`, `tests/`, and `README.md`. I want a small CLI plus a reusable library, not a notebook, and no sample input files — synthesize any demo data in code. Use current best-practice libraries only after checking the web, then wire up the implementation, tests, and docs.
```

### 449. D3_s982248_en (domain=D3, difficulty=7)

```
Build a small Python data-quality and KPI dashboard tool from scratch for Shopify-style order data: create `app.py`, `kpis.py`, `anomaly.py`, `transform.py`, `dashboard.py`, and `README.md`. It should clean messy tabular records, compute revenue/order/customer KPIs, detect anomalies in daily metrics, and render a simple local HTML dashboard with charts. Use web research to choose sensible open-source libraries and current best practices, but do not rely on any input files or sample dataset.
```

### 450. D3_s982262_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for ops KPI monitoring that cleans messy event logs, detects anomalies, and renders a compact dashboard summary. I want app.py, kpi_engine.py, visualization.py, tests/test_kpi_engine.py, and README.md with a CLI that can ingest JSONL/CSV, compute daily KPIs, flag anomalies, and output an HTML report.
```

### 451. D3_s982280_en (domain=D3, difficulty=7)

```
I need a small but real analytics utility I can ship internally for ops and finance teams.
- Build a from-scratch Python app that cleans event/transaction records, flags anomalies, and computes a few business KPIs with a simple dashboard.
- Make it work on generated sample data only — no input files — so the repo includes synthetic data generation, not a dataset dependency.
- Please use current best practices from the web for a lightweight stack (for example Streamlit or Plotly, plus a testing setup) and design the architecture around reusable modules.
- I want the built code/files, plus a short README that explains how to run it and what each component does.
- Include a clear path to extend the rules later for new KPIs or anomaly checks.
```

### 452. D3_s982294_en (domain=D3, difficulty=7)

```
Build me a small but real data-quality monitoring tool from scratch for a business dashboard use case. I want a Python 3.11 project that can ingest event metrics from a simple in-memory structure or JSON payload passed at runtime, clean the data, detect anomalies, and compute KPI summaries for visualization. There are no input files to start from, so please create the whole codebase yourself.

The core idea is that I have a stream or batch of daily operational metrics, such as orders, revenue, conversion rate, latency, and error rate, and I need a reusable library plus a command-line interface that can do three things reliably: normalize messy metric records, flag anomalies, and emit dashboard-ready KPI outputs. Please implement it in a way that would be realistic for a production analytics team, not a toy script.

I need the cleaning layer to handle missing values, duplicated records, mixed timestamp formats, negative values where they are invalid, and out-of-range percentages. Please define clear rules for how records are standardized, how conflicts are resolved, and how invalid records are rejected or repaired. For anomaly detection, I want at least two methods: a robust statistical baseline method using median and MAD or z-score variants, and a time-series change detector based on rolling windows or day-over-day deltas. Please make the methods configurable per metric, because some metrics are seasonal and some are not. For KPI computation, I want the project to derive totals, means, medians, rolling averages, conversion rate, error rate, and a simple health score that combines severity-weighted anomaly counts with metric thresholds. The health score should be easy to explain and reproducible.

Please also include a lightweight visualization export layer that can generate a JSON structure suitable for charts, with series, labels, anomaly markers, and KPI summaries, so that a front-end team could plug it into a dashboard later. I do not need a graphical UI, but I do need the output schema to be practical and documented.

I want the final deliverable to be the built code files plus a README that explains how to run the tool, what assumptions it makes, the cleaning rules, the anomaly algorithms, and example CLI invocations. Please include tests that cover the main edge cases and prove the core functionality works. If you need to research current best practices for Python data validation, anomaly detection libraries or statistical formulas, and JSON visualization payload conventions, do that first with web sources and then implement from scratch rather than depending on a prebuilt app.

Please keep the architecture modular so this can realistically be split across a team: one part for the core cleaning and normalization engine, one for anomaly detection and KPI computation, one for the CLI and JSON export format, and one for the tests and documentation. The implementation should be complete enough that I can run it locally and use it as the basis for a real monitoring workflow.
```

### 453. D3_s982301_zh (domain=D3, difficulty=7)

```
我需要你从零做一个数据处理和可视化的小工具：写一个本地可运行的 Python 项目，能把零散的业务指标数据清洗、做异常检测、计算核心 KPI，并生成一个可交互的仪表盘页面和命令行入口；你要顺手把项目结构、测试和使用说明也一起补齐，最后给我完整代码文件和 README，方便我直接跑起来。
```

### 454. D3_s982308_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for KPI monitoring on streaming CSV logs: ingest raw event data, clean timestamps/nulls/duplicates, detect anomalies on key KPIs, and generate an HTML dashboard plus a CLI. Use current best-practice libraries only after checking their docs and recent usage examples online, then implement the code and tests. Put the code in app.py, tests in test_app.py, and usage notes in README.md; no input files, just the codebase.
```

### 455. D3_s982314_en (domain=D3, difficulty=7)

```
Our operations team needs a small internal tool we can use to clean messy sales activity data, flag unusual spikes or drops, and turn it into a simple KPI dashboard we can trust every week. Build it from scratch as a working code project, not a writeup, and do not rely on any input files being provided — it should create its own sample demo data and be able to run end to end on that. I want the code to include data cleaning, anomaly detection, and a few core KPI summaries with a basic visualization layer, plus clear instructions so another team member can run it locally. Please research sensible Python libraries and current best practices first, then implement the app, tests, and documentation as a complete package.
```

### 456. D3_s982315_zh (domain=D3, difficulty=7)

```
我们现在想把客服和运营每天手工盯报表的事情自动化掉，重点是让团队能更快发现异常波动、看懂关键指标、少花时间在整理数据上。请你从零做一个可运行的小工具，专门用于数据清洗、异常检测和 KPI 可视化：它要能接收我们后续自己填入的数据，自动完成字段标准化、缺失值和重复值处理、识别异常点，并输出一张清晰的仪表盘页面，让业务同事能直接看日趋势、周趋势、异常告警和关键指标摘要。实现方案请你自己设计，尽量选成熟、轻量、好维护的技术栈，并把代码、使用说明和必要的测试一起交付出来。
```

### 457. D3_s982316_en (domain=D3, difficulty=7)

```
I need a small but real prototype for a data-quality and KPI monitoring tool I can demo internally. Build it from scratch, with no input files, and make it feel production-minded rather than a notebook.

- Create a Python package/CLI that can ingest a small in-memory dataset schema, clean common issues, detect anomalies, and compute a few KPI summaries.
- Include a simple visualization layer that outputs charts or an HTML report for data quality and KPI trends.
- Use current best practices and a sensible library stack after checking up-to-date docs and examples online, especially for visualization and anomaly detection.
- I want the final code, tests, and a short README with run instructions and design notes.
- Keep it modular so different parts can be built and tested independently, then integrated cleanly.
```

### 458. D3_s982332_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for SaaS ops KPI monitoring: an anomaly detector and daily KPI digest generator for event/metric streams, with a clean CLI and a small HTML dashboard. I want app.py, kpi_engine.py, detector.py, dashboard.py, tests/, and README.md — no input files, just the code and docs.
```

### 459. D3_s982336_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch data quality tool for a warehouse ops team: it should ingest CSV/JSON event logs, clean and normalize messy fields, flag anomalies, and compute a handful of KPIs with a simple visualization dashboard or HTML report. Please research a couple of lightweight Python libraries and best practices first, then produce the code, tests, and a README so I can run it locally with no sample input files included.
```

### 460. D3_s982345_zh (domain=D3, difficulty=7)

```
帮我从零做一个 Python 工具，做“数据清洗 + 异常检测 + KPI 监控”一体化的小型命令行应用，文件就按你自己定，核心代码、测试和 README 一起给我。不要用现成模板项目，直接搭建一个可运行的 repo，最好还能导出一个简单的 HTML/CSV 报告。
```

### 461. D3_s982348_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool that can clean messy event data, flag anomalies, and generate KPI summaries with a simple HTML dashboard. There are no input files to start with, so please create the code, a config-driven pipeline, sample synthetic data generation for demo/testing, and a README that explains how to run it. Please use web research where it helps to pick solid libraries and patterns for data cleaning, anomaly detection, and lightweight visualization, and make sure the final deliverable is the codebase itself, not a report.
```

### 462. D3_s982350_en (domain=D3, difficulty=7)

```
I need a small internal tool for our operations team that helps us clean up messy daily sales exports, flag unusual spikes or drops, and show a simple KPI dashboard so managers can see what changed without opening a spreadsheet. Build the code from scratch, with no input files provided, and make it practical enough that we can later point it at CSV exports from our systems. I want the finished code files and a short README explaining how to run it. Please figure out the best lightweight stack and sensible defaults yourself, and use web research where needed so the approach matches current good practice for data cleaning, anomaly detection, and visualization.
```

### 463. D3_s982360_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch for ops analytics that reads event data, cleans it, flags anomalies, and outputs a KPI dashboard summary as Markdown plus a simple local web chart page. There are no input files to start with, so make the tool generate a realistic synthetic dataset for demo mode, and design it so I can later point it at CSV/JSON logs. Please include the code files, tests, and a short README showing how to run it, and use current web research to pick a sensible stack and best-practice approach for anomaly detection and visualization.
```

### 464. D3_s982386_en (domain=D3, difficulty=7)

```
We need to build a small internal tool for our operations team that can clean messy daily metrics, flag unusual numbers, and show a simple KPI dashboard so managers can spot problems fast. I want this built from scratch as working code, not a write-up, and there are no starter files or data. Please research the best lightweight Python libraries and patterns to use for data cleaning, anomaly detection, and dashboarding, then build the tool with a clean command-line workflow and a basic visual report. It should take pasted or generated sample records inside the app, not from uploaded files, because the point is to ship the tool itself. Please include the code files and a short README explaining how to run it and what it does.
```

### 465. D3_s982401_zh (domain=D3, difficulty=7)

```
我想从零做一个可运行的小工具，用来清洗和监控业务指标数据，并且能自动做异常检测和可视化。

- 做一个 Python 项目，核心是一个“指标清洗 + 异常检测 + KPI 仪表盘”工具，数据源先假设为程序生成的示例数据，不要依赖现成输入文件。
- 需要提供命令行入口，能一键生成样例数据、执行清洗、跑异常检测、输出 KPI 汇总，并把图表导出成静态文件。
- 希望你参考现有开源库/最佳实践来选型和设计，例如数据清洗、时间序列异常检测、图表展示、CLI 结构这些部分，但代码必须是从头实现的，不要照搬模板工程。
- 代码要拆成清晰模块，最好再补一份简短 README，说明安装、运行方式、参数含义和输出结果。
- 如果可以，也顺手加上单元测试，覆盖关键清洗规则、异常检测边界情况和 CLI 的基本流程。
```

### 466. D3_s982406_en (domain=D3, difficulty=7)

```
Build a small Python app from scratch for KPI monitoring: ingest live metrics from a few public HTTP APIs, clean and normalize the records, flag anomalies, and render a simple dashboard HTML report. Use current library guidance from the web, and give me `app.py`, `kpi_engine.py`, `dashboard.html`, and `README.md`.
```

### 467. D3_s982418_en (domain=D3, difficulty=7)

```
Build a small Python package from scratch for a retail KPI monitoring tool: clean incoming order/returns events, detect anomalies in daily revenue and refund rate, and generate a simple HTML dashboard with charts. Create app.py, kpi_monitor/ modules, and README.md; no input files, just code and docs.
```

### 468. D3_s982432_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch data quality and KPI dashboard tool for a SaaS ops team: it should ingest CSV or JSON logs we define in the code, clean and normalize fields, detect anomalies in metrics like revenue, signups, and error rate, and render a simple web dashboard with trend charts, KPI cards, and anomaly flags. Please create the actual code files, plus a short README and tests, and use web research to pick sensible libraries and best practices for anomaly detection, charting, and CSV/JSON handling before implementing.
```

### 469. D3_s982456_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch for our ops team that cleans messy event logs, flags anomalies, and produces a few KPI summaries plus a simple chart-ready output for dashboards. Please create the code and a README, with no input files assumed, so it can generate a synthetic demo dataset and also accept CSV/JSON later via the CLI. I want it to be practical enough to wire into a real workflow, using a sensible library stack and best practices you verify with web research.
```

### 470. D3_s982465_zh (domain=D3, difficulty=7)

```
帮我从零做一个 Python 小工具，做一套“交易/运营指标数据清洗 + 异常检测 + KPI 仪表盘”的命令行应用，直接输出 `app.py`、`metrics.py`、`anomaly.py`、`dashboard.py`、`README.md`。我不提供任何输入文件，你要自己设计可运行的数据结构、示例生成器和默认演示流程，并把清洗规则、异常阈值、KPI 计算和图表都做完整。顺便调研一下适合的 Python 可视化和异常检测方案，按你查到的最佳实践来实现。
```

### 471. D3_s982466_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for cleaning and monitoring operational metrics called `kpi_guard`. I want `src/`, `tests/`, `pyproject.toml`, and a `README.md` that shows how to use it from the CLI and as a library. The tool should ingest plain dictionaries or JSON lines, normalize messy KPI records, flag anomalies with configurable rules, and render a simple terminal dashboard plus an optional HTML report.
```

### 472. D3_s982476_en (domain=D3, difficulty=7)

```
Build a fresh Python tool for our ops dashboard: `kpi_guard/` with a Streamlit app and a small library that computes cleaning, anomaly detection, and KPI summaries for live business metrics. Pull in current best-practice references for Streamlit, pandas, and a lightweight anomaly detector before you code, then implement the whole thing from scratch with no starter data. Include `README.md`, `app.py`, `kpi_guard.py`, and tests; make the dashboard show data quality checks, flagged anomalies, and KPI tiles from synthetic sample data generated in code.
```

### 473. D3_s982479_zh (domain=D3, difficulty=7)

```
我需要你从零做一个数据处理和可视化的小工具，专门用来清洗一批业务指标数据、做异常检测、算常见 KPI，然后生成一个可交互的本地仪表盘。不要依赖现成模板或示例数据，代码要自己搭起来；你可以自己设计一套数据结构、配置方式和输出格式。最好把结果拆成几个文件，比如核心处理模块、命令行入口、可视化页面、测试和 README，一起交付成一个能直接跑的项目。
```

### 474. D3_s982482_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team that can turn messy daily business metrics into something we can trust quickly. I want you to build it from scratch, not analyze any existing file: a local app that lets us paste or type in raw KPI rows, cleans up obvious issues, flags unusual values, and shows a simple dashboard so non-technical people can spot problems fast. It should handle things like duplicate rows, missing values, inconsistent date formats, and sudden spikes or drops, then summarize the results in a clear way for management. Please research the best lightweight Python libraries and patterns for this kind of data cleaning, anomaly detection, and visualization before building it, then deliver the working code and a short README that explains how to run it and what it does.
```

### 475. D3_s982483_zh (domain=D3, difficulty=7)

```
我们现在要给运营团队做一个“每天自动看数据”的轻量工具，目的是尽早发现订单、退款和库存里的异常，别等到月底才发现问题。我要你从零做一个可运行的代码项目，不是分析现成表格，而是帮我搭一个可以以后接入真实业务数据的基础工具。

请做一个面向数据处理和可视化的小应用，要求能自己生成示例数据、完成清洗、自动找异常、算关键指标，并把结果做成一个本地可打开的页面看板。页面里至少要有总览指标、异常列表、趋势图和可以按日期/类型筛选的功能。最好再带一个简单的命令行入口，方便我们定时跑。

我希望你先自己查一下现在常用、稳妥的实现方式和相关库的最佳实践，再开始搭建。最后交付完整代码和使用说明，能在本地直接运行起来。不要依赖我提供任何输入文件，因为这次就是从零把工具搭出来，示例数据也请你在代码里生成。
```

### 476. D3_s982492_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch for our ops team that can clean incoming KPI snapshots, flag anomalies, and render a simple dashboard view without relying on any sample data files. It should include the code, tests, and a README, and I want it designed around a realistic retail-metrics workflow with metrics like orders, revenue, refund rate, and conversion rate. Please research a sensible approach to anomaly detection and lightweight visualization libraries first, then implement the actual package and a CLI so someone can point it at JSON or CSV they already have and get cleaned output plus a KPI summary and chart export.
```

### 477. D3_s982493_zh (domain=D3, difficulty=7)

```
我需要你从零开发一个面向中小团队的“数据质量与KPI监控”小工具，最好能直接跑起来：把清洗、异常检测和KPI看板串成一个完整的本地应用，支持我手动输入几组示例指标（比如订单数、转化率、客单价、缺失率），自动做字段清洗、规则校验、异常点标记和日/周KPI汇总，并把结果渲染成一个简单的网页仪表盘或命令行报告；代码要包含清晰的目录结构、README、必要的测试和一个可扩展的配置方案，别依赖现成数据文件，所有示例数据和演示流程都要在代码里生成出来。
```

### 478. D3_s982494_en (domain=D3, difficulty=7)

```
We need a small internal tool to help our operations team spot bad data and track daily service quality before it turns into reporting mistakes. Please build the code from scratch for a lightweight dashboard that can clean incoming operational metrics, flag anomalies, and show a few simple KPIs in a clear visual view. It should not depend on any input files because I want the tool itself, not an analysis of a specific dataset. Use current best practices and look up a few good libraries or patterns for data validation, anomaly detection, and plotting so the implementation is solid. I want the built code files plus a short README that explains how to run it, what it does, and how to extend it.
```

### 479. D3_s982504_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch that helps a product team clean messy event data, flag anomalies, and generate a KPI summary dashboard from whatever CSV they export from their app logs. There are no input files to start with, so please create the code, tests, and a short README that shows how to run it on any CSV with timestamp/user/event/value columns. I want the tool to infer basic data quality issues, detect suspicious spikes or drops, compute a few common KPIs, and output both a cleaned CSV and a simple HTML/JSON report.
```

### 480. D3_s982507_zh (domain=D3, difficulty=7)

```
我们现在需要做一个给运营和财务都能直接用的轻量工具，解决每天看数据时最头疼的几个问题：数据里经常有空值、重复值、异常波动，报表口径又容易不一致，最后大家看到的 KPI 也不稳定。我希望你从零开发一个本地可运行的小工具，用来自动清洗一份原始业务数据、识别异常、计算几个核心 KPI，并把结果做成一个简单的可视化页面或交互式报告，方便我直接打开看。

这不是让我上传现成数据去分析，而是请你自己先设计并实现整个功能：包括数据清洗规则、异常检测方法、KPI 计算逻辑、以及一个能展示趋势和异常点的界面。你需要自己决定技术方案，但要尽量贴近真实业务场景，考虑可配置、可复用、可扩展。最好支持命令行一键运行，也能输出结果文件。

请你先查一些当前常用的开源方案和最佳实践，再开始搭建代码。最终我希望拿到完整代码和说明文档，能让我本地直接跑起来验证。
```

### 481. D3_s982532_en (domain=D3, difficulty=7)

```
I want a small but real Python tool built from scratch for operational data quality monitoring.

- Build a CLI app that ingests a synthetic JSON event stream you generate in code, cleans it, detects anomalies, and computes KPI summaries.
- Include a simple dashboard output (HTML or terminal-based) that shows trends, anomaly flags, and key metrics like volume, error rate, and latency.
- Make the detection logic configurable and document the chosen approach with references to current best practices or library docs.
- Add solid tests and a README so another engineer can run it and extend it.
- Use current web research to choose a lightweight stack and verify the recommended patterns for plotting, CLI design, and anomaly detection.
```

### 482. D3_s982539_zh (domain=D3, difficulty=7)

```
我需要你从零做一个用于业务数据处理和可视化的 Python 工具，目标是把零散的 KPI 事件数据清洗后自动做异常检测，并生成一页可直接给管理层看的 HTML 报表和 PNG 图表；请把代码、README 和必要的测试文件一起产出，重点是要有一个可复用的核心库、命令行入口、以及带趋势图/异常点标注的可视化页面，技术选型和实现细节你可以先查一下现成库的最佳实践再开工。
```

### 483. D3_s982542_en (domain=D3, difficulty=7)

```
Our operations team needs a small internal tool we can use to keep an eye on daily sales and support numbers without waiting for an analyst. Please build a from-scratch Python app that can take simple pasted data, clean it up, flag suspicious spikes or drops, calculate a few clear KPIs, and show the results in a dashboard we can open in a browser. I want it to feel practical for a business user: easy to run locally, easy to understand, and able to explain why something was flagged. Use current best practices for the libraries and patterns you choose, and research the most sensible way to do this before coding. Please deliver the built code files and a short README with setup and use instructions — there are no input files, so please design the whole thing from scratch.
```

### 484. D3_s982550_en (domain=D3, difficulty=7)

```
Build a Python 3.12 command-line tool for my ops team that ingests raw event logs we generate internally, cleans them, flags anomalies, and prints a KPI summary with a tiny ASCII dashboard. I want `src/`, `tests/`, `pyproject.toml`, and `README.md`; make it runnable with one command and include a sample synthetic generator in the code, but no input files. Use a solid stats/anomaly approach and keep the CLI dead simple.
```

### 485. D3_s982552_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch data quality and KPI monitoring tool in Python for a SaaS dashboard team — no input files, just the code and README. It should clean incoming event records, detect obvious anomalies and missing-data spikes, and generate a simple KPI summary plus a lightweight HTML/CSV report I can run locally on synthetic or streamed JSON events. Please make it practical enough to plug into a real pipeline, with clear config, tests, and documentation.
```

### 486. D3_s982563_en (domain=D3, difficulty=7)

```
I need you to build a from-scratch Python tool for cleaning time-series business metrics, spotting anomalies, and generating a KPI summary dashboard with both a CLI and a small web UI. There are no input files for this task, so please create the whole project structure, code, tests, and docs yourself, including sensible sample data generation for demos. I want the code to be production-minded, with a clean module for outlier detection, configurable KPI calculations, and a simple chart-based report page that shows trends, anomalies, and alert thresholds.
```

### 487. D3_s982587_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool for cleaning time-series business data, flagging anomalies, and generating KPI summaries with a simple interactive dashboard. Please create the codebase and docs for a CLI app plus a lightweight web dashboard that can ingest pasted CSV text or synthetic sample data generated in-app, normalize messy dates/currencies/missing values, detect outliers and sudden KPI drops, and render a clean summary table plus charts; there are no input files to start from, so the app should include its own sample-data generator and clear README instructions for running it.
```

### 488. D3_s982611_zh (domain=D3, difficulty=7)

```
我需要你从零搭一个用于数据处理和可视化的小工具，目标是给运营/分析团队做“日报数据清洗 + 异常检测 + KPI 看板”。不要用现成模板，直接输出可运行代码和说明文档；项目里要包含一个核心处理模块、一个命令行入口、一个简单的本地可视化页面，以及测试。这个工具要支持接收我后续自己提供的 CSV/JSON 数据源，能自动做字段清洗、缺失值和重复值处理、按规则识别异常波动，并生成可视化 KPI（比如趋势、环比、分组对比和异常标记），最好还能把结果导出成新的 CSV 和一份 HTML 报告。
```

### 489. D3_s982622_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for daily sales KPI monitoring: clean incoming event data, detect anomalies in conversion rate / revenue / traffic, and render an HTML dashboard with trend charts and alert summaries. Use FastAPI for the API, SQLite for persistence, and add a small CLI for ingesting synthetic sample events and generating the report; put the code in app.py, dashboard.py, and tests/.
```

### 490. D3_s982623_zh (domain=D3, difficulty=7)

```
我需要你从零做一个用于数据处理与可视化的小工具，目标是把零散的业务指标数据清洗、做异常检测、算核心 KPI，然后生成一个能直接看趋势和异常点的交互式仪表盘。不要依赖现成模板或输入文件，代码里自己构造示例数据和测试数据，最好顺手把数据清洗规则、异常判定方式和 KPI 口径写成可配置的。最后把项目代码、说明文档和基本测试一起整理好，方便我后面直接接到真实数据源上。
```

### 491. D3_s982659_zh (domain=D3, difficulty=7)

```
我需要你从零搭一个面向运营数据的 Python 工具，做“清洗 + 异常检测 + KPI 看板”一体化处理：代码里自己生成示例数据，不要依赖任何输入文件，最后给我可直接运行的项目文件（比如主程序、测试和 README）。这个工具要能接收一段原始事件流/指标数据，自动做字段清洗、缺失值处理、重复记录去重、异常值标记，还要输出一份简洁的 KPI 汇总和一张可交互的可视化图表；另外希望你顺手查一下适合这种场景的现成库和最佳实践，别用过时方案。请把项目结构、核心逻辑、命令行入口、测试都一起做出来。
```

### 492. D3_s982660_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch that generates a data quality and KPI dashboard for arbitrary CSV exports from our ops team. There are no input files included, so create the code, CLI, and a sample synthetic dataset generator yourself. The tool should clean messy fields, flag anomalies, compute a few core KPIs, and render an HTML dashboard plus a JSON summary; please also include a short README with setup and usage. Make sure the design is based on current best practices for Python data processing, anomaly detection, and lightweight dashboarding, so research the right libraries and patterns before coding.
```

### 493. D3_s982674_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team because the current spreadsheet checks are too slow and we keep missing odd spikes in daily order volume, refunds, and failed payments. Please build a from-scratch data processing and visualization app that can clean messy event data, flag unusual changes, and show a few simple KPI charts so managers can spot problems fast. I do not have any input files for you — create the tool and its sample/demo data yourself. I want the actual code files, plus a short README that explains how to run it and how the anomaly checks work in plain language.
```

### 494. D3_s982704_en (domain=D3, difficulty=7)

```
Build a small Python package from scratch for cleaning and monitoring operational KPI time series, with anomaly detection and a Streamlit dashboard. I need `src/` code, `tests/`, `README.md`, and an example config; no input data files, generate your own demo data in code. Use current best-practice libraries and patterns you verify online, and make the design support multiple KPI streams, outlier handling, rolling baselines, and exportable summary metrics.
```

### 495. D3_s982721_zh (domain=D3, difficulty=7)

```
我需要你从零搭一个用于运营数据清洗、异常检测和 KPI 可视化的小工具，目标是给电商/订阅类团队日常盯数用的，不要任何输入文件，直接把代码和说明文档做出来。你可以参考现成库和最佳实践，但实现要自己写：要支持接收一小段内置样例数据、自动清洗缺失值和重复值、做简单的异常检测、计算几个常见 KPI（比如转化率、留存率、客单价之类），再输出一个可交互的仪表盘或可视化页面；另外把启动方式、配置方式、以及怎么扩展指标写清楚。最后请把完整代码、测试和 README 一起整理好。
```

### 496. D3_s982724_en (domain=D3, difficulty=7)

```
I want a from-scratch Python tool for operational data quality monitoring and KPI reporting. Build a small library plus a runnable CLI that can ingest raw event records, clean them, flag anomalies, and generate a simple KPI dashboard output.

- The tool should define a configurable schema for rows, normalize messy values, and handle missing/duplicate/out-of-range data gracefully.
- It should implement at least two anomaly-detection approaches that are practical for time-series or event-stream metrics, and expose them through the library and CLI.
- It should compute a few common KPIs from the processed records and export a visualization-ready summary, ideally as JSON plus a lightweight HTML or SVG report.
- Use current best practices and a couple of well-known Python libraries where appropriate, but the core feature set should be built from scratch.
- Please also include tests and a short README showing how to run it and extend the rules.
```

### 497. D3_s982734_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team because we keep missing bad numbers in daily partner reports, and it takes too long to clean them up by hand before we share anything with leadership. Please build a from-scratch web app that lets a user paste in raw KPI data, cleans obvious issues, flags unusual values, and shows a simple dashboard with trends and alerts. I want the app code and a short README so another person can run it locally. Please use current best practices for the stack and any charting or validation libraries you choose, but do the implementation yourself.
```

### 498. D3_s982738_en (domain=D3, difficulty=7)

```
I need you to build a small but real Python tool from scratch for data processing and visualization that can clean messy event data, flag anomalies, and calculate a few operational KPIs, with a simple local web dashboard for charting the results. There are no input files — please create the code, tests, and a short README, and use current web research to pick the right libraries and best practices for things like anomaly detection, CSV/JSON handling, and lightweight plotting.
```

### 499. D3_s982741_zh (domain=D3, difficulty=7)

```
帮我从零做一个面向制造业数据质量的 Python 小工具，重点不是分析现成数据，而是把“清洗 + 异常检测 + KPI 计算 + 可视化”做成可复用的代码库。

- 先调研并选型 2-3 个合适的开源库/做法，用来实现时序数据清洗、异常检测和图表输出，说明为什么选它们。
- 代码要能生成一份演示用的合成传感器数据，并对它做缺失值处理、离群点识别、指标计算和趋势图/告警图输出。
- 提供一个命令行入口，能一键运行生成结果；最好再给一个简单的配置文件，方便改阈值和 KPI 口径。
- 需要把核心处理逻辑、CLI、测试、文档分开做，最后能直接运行并通过测试。
- 最终请交付完整代码和 README，说明安装、运行方式、关键设计和你参考的网页资料。
```

### 500. D3_s982747_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool that lets me define business KPIs, clean messy event data, flag anomalies, and generate a simple HTML dashboard with charts and summary cards. There are no input files to start from, so please make it work with sample data generated inside the app or via a demo mode, and include the code, tests, and a short README showing how to run it. Please also check current best practices for the plotting/library choices and any lightweight anomaly-detection options before you implement it.
```

### 501. D3_s982755_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool that generates a live KPI dashboard for ecommerce ops: ingest raw event streams, clean bad records, detect traffic/order anomalies, and render a small web UI with charts. I want the code in app.py, a test suite, and a short README.md with setup and run commands.
```

### 502. D3_s982755_zh (domain=D3, difficulty=7)

```
我需要你从零做一个数据处理与可视化小工具，目标是给电商/运营团队用来做日常指标清洗、异常检测和 KPI 看板，不要用任何现成数据文件，直接自己把代码和项目结构搭起来。希望你参考一下现在常见的 Python 可视化和数据校验方案，最后交付可运行的代码和 README，包含一个命令行入口、一个能生成示例仪表盘的本地网页、以及一套单元测试，方便我后面接真实 API 或数据库数据。
```

### 503. D3_s982770_zh (domain=D3, difficulty=7)

```
帮我从零写一个 Python 数据处理与可视化小工具，做“事件流清洗 + 异常检测 + KPI 看板”三件事，代码放到 `src/`、测试放到 `tests/`、说明写到 `README.md`。不要用现成模板项目；需要你先查一下适合的库和最佳实践，再直接把可运行代码搭出来。
```

### 504. D3_s982772_en (domain=D3, difficulty=7)

```
Our operations team needs a small internal tool that can clean messy daily sales and inventory numbers, flag unusual spikes or drops, and show a simple KPI dashboard so managers can spot problems fast. I want you to build the code from scratch, not analyze any provided data, and make it work on synthetic sample data generated by the app itself so we can demo it right away. Please research the best lightweight Python libraries and current practices for data cleaning, anomaly detection, and dashboarding, then build the tool and include clear run instructions. I want the final code files and a short README.
```

### 505. D3_s982773_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool that cleans messy event logs, flags anomalies, and computes a few business KPIs, then renders a simple HTML dashboard from generated sample data so I can demo the workflow without any input files. Please include the code files, tests, and a short README; use current best practices for the library choices and any plotting/dashboard approach, and make sure the tool can be run locally from the command line.
```

### 506. D3_s982779_en (domain=D3, difficulty=7)

```
Build a small Python tool from scratch for operational data quality: it should clean noisy event streams, flag anomalies, and compute KPI summaries, with a simple CLI and a JSON/HTML report. Use current best practices and library choices you verify with web research; I want the code, tests, and README, but no input files or sample datasets.
```

### 507. D3_s982779_zh (domain=D3, difficulty=7)

```
我需要你从零做一个可运行的小工具，目标是给电商运营用的“订单数据清洗 + 异常检测 + KPI 看板”框架，代码要自己实现，不用任何现成数据文件。希望你把项目拆成多个文件，至少包含核心清洗与异常检测模块、一个命令行入口、一个能把结果导出成 HTML/Markdown 看板的可视化层，以及单元测试和 README。这个工具要支持我以后直接接入自己的 CSV/JSON 订单流，能自动做字段标准化、缺失值处理、重复记录识别、异常订单标记，并输出像订单量、客单价、退款率、转化率这类 KPI 的汇总页面；如果需要参考现成的 Python 库、CLI 设计或可视化最佳实践，先用 web 查一下再动手实现。
```

### 508. D3_s982788_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for streaming log-quality monitoring: it should ingest synthetic event records generated in code, clean noisy fields, detect anomalies in near-real time, and compute KPI summaries with a small dashboard export. Use current best practices for pandas/plotly/duckdb or alternatives if they make more sense, and write the implementation in app.py plus README.md. No input files — generate the sample data inside the app and make the tool runnable end-to-end.
```

### 509. D3_s982800_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for operations KPI monitoring: `kpi_cleaner.py`, `anomaly_detector.py`, `dashboard.py`, and `README.md`. It should ingest JSON/CSV event streams from stdout or files, clean timestamps and missing values, detect anomalies with configurable rules plus z-score/rolling baselines, and render a small web dashboard with trend charts and KPI cards.
```

### 510. D3_s982804_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch data quality and KPI monitoring tool for CSV logs, with a clean Python core, a simple CLI, and a dashboard that flags anomalies and shows trends; please research a couple of good Python libraries and design patterns first so the implementation is sane, then deliver the code files and a short README. There are no input files — the tool should generate sample data if needed and work on any CSV I drop in.
```

### 511. D3_s982807_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool for cleaning messy event data and flagging anomalies before it goes into our KPI dashboard. Make it a real usable package with code files, a CLI, and a simple summary report output that can run on synthetic JSON records I’ll generate later, not any input files. I want it to normalize dates and categories, detect spikes and missing-data gaps, calculate a few operational KPIs, and render a basic chart or text-based summary so an analyst can spot problems fast.
```

### 512. D3_s982827_zh (domain=D3, difficulty=7)

```
我需要你从零做一个本地可运行的 Python 小工具，专门处理日志/指标数据的清洗、异常检测和 KPI 看板：输入不是现成文件，而是你自己先设计一套可生成测试数据的模块，再做一个命令行程序把原始事件流清洗、聚合成日/周 KPI、标出异常点，并输出一个静态 HTML 可视化页面和一份 README。希望你顺手把目录结构、核心算法、交互命令、测试和文档都补齐，做成一个能直接交付的代码仓库。
```

### 513. D3_s982830_en (domain=D3, difficulty=7)

```
We need a small internal tool that helps our operations team clean up messy daily order and shipment data, flag weird records before they hit reporting, and show a simple KPI dashboard for on-time delivery and exceptions. I don’t have any source files to give you — please build the tool from scratch as working code, not just an explanation. Please research a sensible approach and current best practices for data validation, anomaly detection, and a lightweight dashboard stack, then create the code files and a short README so our team can run it locally. Keep it practical for a business team: it should be easy to point at incoming CSV or JSON data later, but for now just build the app, the cleaning rules, the anomaly checks, and the KPI view from scratch.
```

### 514. D3_s982836_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for cleaning transaction streams, anomaly detection, and KPI dashboards for retail sales ops. I want the code in `app.py` plus `README.md`, with a CLI that ingests JSON/CSV input from stdin or a file path, computes daily KPIs, flags anomalies, and exports an HTML report with charts.
Use current best practices and a few real library choices after checking the web; no starter dataset is needed, just the code and docs.
```

### 515. D3_s982840_zh (domain=D3, difficulty=7)

```
帮我从零实现一个 Python 数据处理与可视化小工具，做门店日销数据的清洗、异常检测和 KPI 仪表盘输出；代码放到 app.py、kpi.py、anomaly.py、viz.py、tests/ 里，顺手补 README.md。先用 web 搜一下 pandas、plotly、statsmodels/ sklearn 里适合做时间序列异常检测和 KPI 计算的最佳实践，再按那个思路实现，别依赖任何输入文件，代码里自己生成示例数据并能直接跑起来。
```

### 516. D3_s982854_zh (domain=D3, difficulty=7)

```
我需要你帮我从零开始构建一个数据处理与可视化工具，专门用于时间序列数据的清洗、异常检测和KPI计算。没有输入文件，你自己生成模拟数据。工具要提供命令行CLI接口和可选Web界面（比如Flask），核心算法自己实现，但可以参考pandas、numpy、scikit-learn、plotly等库的最佳实践。交付物包括：app.py（主程序）、cli.py（CLI入口）、anomaly_detector.py、kpi_calculator.py、test_all.py（单元测试）、README.md。代码要整洁、有注释，测试覆盖主要功能。
```

### 517. D3_s982864_zh (domain=D3, difficulty=7)

```
帮我从零做一个 Python 的数据处理+可视化工具，做“销售指标清洗、异常检测、KPI 仪表盘”这三件事，直接交付代码。请输出 app.py、dashboard.py、tests/ 和 README.md，支持命令行运行和本地网页看板，不要依赖现成数据文件，自己内置一份模拟数据生成器。
```

### 518. D3_s982873_zh (domain=D3, difficulty=7)

```
帮我从零写一个 Python 工具，做“数据清洗 + 异常检测 + KPI 监控”的小型仪表盘，代码放在 app.py、kpi.py、anomaly.py、viz.py、tests/ 里。不要用现成模板；需要你先查一下 Streamlit/Plotly/Pandas 的最佳实践，再把 CLI 和 Web 界面都做出来，最后给一份简短 README.md。
```

### 519. D3_s982874_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for monitoring SaaS product telemetry in real time: clean incoming event streams, detect anomalies in daily KPIs, and render a compact HTML dashboard with charts and status badges. Use current best-practice libraries/APIs you research first, and give me the code plus a README that explains how to run it with synthetic demo data generated in the app.
```

### 520. D3_s982877_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool that cleans event/log data, flags anomalies, and generates a KPI dashboard report with charts and a compact summary. There are no input files for this task, so design the whole thing yourself: pick a realistic schema, add synthetic data generation for demos/tests, then implement the core processing, anomaly detection, and visualization output as code files I can run locally. Also include a README with setup and usage, and make sure the implementation uses a sensible modern library stack after checking current best practices and a couple of relevant libraries online.
```

### 521. D3_s982882_zh (domain=D3, difficulty=7)

```
帮我从零做一个“数据质量与KPI监控”小工具，面向日常运营数据流，不依赖任何输入文件，直接实现可运行的代码和说明。
- 需要先调研并选型：Python 里适合做流式清洗、异常检测和可视化的开源库，最好参考一些主流实践和文档。
- 核心功能要能接收模拟数据事件，自动做字段清洗、缺失值处理、重复检测、异常值标记，并生成几个常用 KPI（比如到达量、转化率、延迟、错误率一类）。
- 要有一个可用的结果展示层：至少支持命令行输出摘要，最好再带一个轻量的本地可视化页面或生成 HTML 报告。
- 代码要从零实现，不要依赖现成模板；同时补齐单元测试和基本的使用说明，保证我拿到后能直接跑起来。
- 最后给我一套清晰的项目结构和 README，说明怎么启动、怎么验证、怎么扩展规则。
```

### 522. D3_s982892_en (domain=D3, difficulty=7)

```
I want a small but real analytics tool built from scratch for our operations team.
- Create a Python app that ingests event records we generate in-memory or via pasted JSON, cleans common data issues, flags anomalies, and outputs KPI summaries.
- Add a simple dashboard or report view that shows trends, anomaly counts, and a few operational KPIs over time.
- Make the cleaning and anomaly rules configurable so we can tune thresholds without changing code.
- Include tests for the main pipeline and edge cases, plus a clear README with how to run it.
- Use current best practices for Python plotting/data validation and pick libraries after checking the web.
```

### 523. D3_s982912_en (domain=D3, difficulty=7)

```
I need you to build a small but solid Python tool from scratch for cleaning and monitoring operational data streams in a logistics dashboard: it should normalize messy timestamp/number fields, detect anomalies in KPI series, and render a simple web-based visualization with summary cards and trend charts. Please research the best-fitting open-source libraries and current best practices first, then produce the code files and a README so I can run it locally and extend it later. There are no input files for you to work from — design the sample data generator and the whole feature set yourself.
```

### 524. D3_s982919_en (domain=D3, difficulty=7)

```
I want a from-scratch Python tool for cleaning and monitoring operational metrics in a small SaaS product. Build a lightweight package that ingests event logs from an API or in-memory stream, cleans the data, detects anomalies, and computes KPIs with a simple dashboard output.
- Make it work without any input files by generating a realistic demo stream and letting me plug in my own JSON events later.
- Include a reusable core library for cleaning rules, anomaly detection, and KPI calculations, plus a CLI to run it end-to-end.
- Add a minimal web dashboard or exportable HTML report that shows trends, anomalies, and KPI summaries.
- Write tests for the main logic and edge cases, and include setup/run instructions.
- Use current best practices for the chosen Python libraries and data-visualization stack, and keep the code organized so it can be extended later.
```

### 525. D3_s982926_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team that can clean up messy daily order-performance data, flag unusual spikes or drops, and show the key numbers in a simple dashboard so managers can spot problems fast. I want this built from scratch as working code, not a report, with no input files assumed — the tool should include sample synthetic data generation so it can run on its own. Please research a sensible modern stack and best practices for data cleaning, anomaly detection, and KPI visualizations, then build the app, add tests, and include clear setup and run instructions. I need the final code files delivered.
```

### 526. D3_s982958_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for streaming data quality monitoring: a cleaning engine, anomaly detection on KPIs, and a small dashboard/API for viewing trends. Use current best practices for pandas, scipy/statsmodels, and a lightweight web UI; write the code in app.py, detector.py, cleaning.py, and README.md, with no input files. 
```

### 527. D3_s982960_en (domain=D3, difficulty=7)

```
I need you to build a small data-quality and KPI monitoring tool from scratch for a SaaS ops team: it should generate sample event data internally, clean it, detect anomalies in daily conversion/latency/error-rate KPIs, and expose both a CLI and a simple dashboard so someone can inspect trends and alerts without any input files. Please use current best practices and library choices where useful, and include the built code plus a short README that explains how to run it.
```

### 528. D3_s982982_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for cleaning and validating event-stream data, detecting anomalies, and calculating KPIs for a SaaS funnel dashboard. I want the code in app.py plus tests in tests/, with a small README that explains setup, usage, and the anomaly rules.
```

### 529. D3_s983020_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for real-time log KPI monitoring: ingest a stream of JSON events, clean/normalize them, detect anomalies on rolling metrics, and render a dashboard plus alert summary. I want the code in app.py, modules/, and README.md; no input files, generate synthetic demo events inside the app for local runs.
```

### 530. D3_s983031_zh (domain=D3, difficulty=7)

```
帮我从零做一个 Python 项目：做一个“运营指标清洗 + 异常检测 + KPI 仪表盘”小工具，包含命令行和一个本地网页可视化界面。代码里不要依赖现成样例数据，自己生成一套可配置的模拟业务数据，并实现缺失值处理、重复记录去重、异常值检测、KPI 计算和图表展示。顺手把你选用的库、接口设计和最佳实践查一下，最后给我 app.py、pipeline.py、dashboard.py、tests/、README.md。
```

### 531. D3_s983059_en (domain=D3, difficulty=7)

```
I need you to build a command-line tool from scratch that cleans a CSV dataset, detects anomalies, and computes key KPIs. The tool should be called `datacleaner` and should accept a CSV file as input, with options to specify cleaning rules (e.g., remove duplicates, fill missing values with median or mean), anomaly detection method (IQR or Z-score with configurable threshold), and a list of KPI columns to summarize (mean, median, std, missing percentage). It must output a cleaned CSV, a CSV of flagged anomalies, and a JSON report of KPIs. No starter data – we'll write the entire Python package from scratch. Please include unit tests, a CLI using argparse or click, and a README with usage examples. You can research libraries like pandas, numpy, scipy, and click for best practices. I want the final deliverable as a zip of the project folder with all source files.
```

### 532. D3_s983107_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch data quality and KPI monitoring tool for a SaaS dashboard: it should clean incoming event records, flag anomalies in daily metrics, and render a simple web dashboard with KPI cards and trend charts. Please implement the code and basic docs in a few files, with no starter data or input files — generate your own demo data in the app/tests. I want it to use a sensible Python stack and follow current best practices for anomaly detection, charting, and structuring the code.
```

### 533. D3_s983118_en (domain=D3, difficulty=7)

```
I need you to build a Python package called 'dataclean-kpi' from scratch. It must provide a command-line tool that can read CSV or JSON data (from a file or stdin), perform data cleaning (handle missing values, detect and treat outliers), detect anomalies using at least two different statistical methods (like Z-score and IQR), and compute key KPIs (mean, median, standard deviation, percentiles). The output should be in JSON format, with separate sections for cleaning actions taken, anomalies flagged, and computed KPIs. No input files will be given — you design the architecture and implement everything yourself. Use web research to find the most robust algorithms, suitable Python libraries (avoiding heavy dependencies beyond numpy/scipy), and best practices for CLI design and error handling. The final deliverable is the full package (including setup.py, code, tests, and a README with examples).
```

### 534. D3_s983178_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool for cleaning event telemetry, flagging anomalies, and computing KPI summaries, with a simple charting/report output. There are no input files — just create the code, tests, and README so I can run it on generated or streamed records later. Use current web research where it helps for choosing the best Python libraries and patterns for validation, anomaly detection, and plotting, then implement the actual app from scratch. Please make it feel like a real internal ops tool, not a toy.
```

### 535. D3_s983188_en (domain=D3, difficulty=7)

```
Build a Python CLI tool for data cleaning, anomaly detection, and KPI computation from CSV/JSON inputs. Name the main script 'datacleaner.py', include a design doc 'design.md'. Research libraries like pandas, scipy, and anomaly detection algorithms (e.g., isolation forest) to decide on implementation. I want the tool to have subcommands: clean, detect, kpi, and a help command.
```

### 536. D3_s983223_en (domain=D3, difficulty=7)

```
Build a CLI Python tool called 'datacleaner' that reads CSV or JSON from stdin or a file, performs configurable data cleaning (missing value imputation, duplicate removal, outlier capping), detects anomalies using multiple methods (Z-score, IsolationForest, moving average), calculates key KPIs (rolling mean, std, count), and generates a summary report with visualizations (histograms, time series anomaly highlights). Use Click for CLI, pandas for data handling, matplotlib/seaborn for plots, scikit-learn for IsolationForest. Write from scratch with no provided input data. Include a tests.py suite and a README.md with usage and examples.
```

### 537. D3_s983283_zh (domain=D3, difficulty=7)

```
帮我写一个数据处理工具，从零实现数据清洗、异常检测和KPI计算功能。要求用Python，命令行接口，输出清洗后的数据和报告。项目文件包括app.py, utils.py, test_app.py, README.md。我需要设计参考，查一下最佳实践和常用算法。快点搞定。
```

### 538. D3_s983309_zh (domain=D3, difficulty=7)

```
我需要你帮我从零开始写一个Python工具，用来做数据清洗、异常检测和KPI计算。这个工具要能处理用户提供的CSV时序数据文件（没有输入文件给到你，工具本身要能接受用户输入）。清洗部分包括处理缺失值（删除或填充）、删除重复行；异常检测支持IQR和Z-score两种方法，可调阈值；KPI要算均值、标准差、最小值、最大值，还有线性趋势斜率。另外要有命令行界面，比如用click或者argparse，支持clean、detect、kpi、plot四个子命令，plot能生成带异常标记的折线图并保存为PNG。单元测试要用pytest写，覆盖各个模块。还要写一个README，说明怎么安装和用。你帮我分解成几个独立的部分，然后分别实现，最后整合在一起。
```

### 539. D3_s983374_zh (domain=D3, difficulty=7)

```
帮我从零开始构建一个 Python 命令行工具，用于数据清洗、异常检测和 KPI 计算。这个工具不需要依赖任何预先提供的数据文件，而是设计成用户通过命令行传入 CSV 文件路径来使用。我希望最终交付一个完整的项目，包括核心代码、CLI 接口、单元测试和文档。具体要求如下：
- 核心功能：支持常见数据清洗操作（如缺失值填充、重复行删除、列类型转换），至少两种异常检测方法（Z-score 和 IQR），并能计算关键 KPI（如均值、标准差、缺失率、异常占比）。
- CLI 接口：提供三个子命令：clean、detect、kpi，并处理输入错误（比如文件不存在、参数无效）。
- 测试：用 pytest 编写单元测试，覆盖所有主要功能，测试覆盖率建议 80% 以上。
- 文档：一个 README.md，包含安装说明、使用示例和参数说明。
过程中你需要搜索相关库（如 pandas、numpy、scikit-learn）的最佳实践、CLI 框架（如 argparse 或 click）的使用方法，以及异常检测算法的实现细节。由于任务模块独立，请并行推进：一个子代理负责核心算法模块，另一个负责 CLI 层，再一个负责测试，最后一个负责文档，最后整合在一起。
```

### 540. D3_s983402_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for cleaning event telemetry, flagging anomalies, and generating KPI dashboards for a SaaS product. I want a CLI plus a small FastAPI service, with the code in app/, tests/, and a short README.md. Use current best-practice libraries and patterns you verify online, and make sure the anomaly rules, KPI calculations, and chart outputs are all implemented in code with no input files provided.
```

### 541. D3_s983480_en (domain=D3, difficulty=7)

```
We need a small internal tool that helps our operations team clean up daily sales data, flag suspicious spikes or drops, and show a simple KPI dashboard without relying on spreadsheets. I want the code built from scratch, not based on an existing template or sample dataset, so our team can drop in their own data later. Please research the best current Python libraries for data cleaning, anomaly detection, and dashboard-style visualization, then build the app and include a clear README so a non-technical manager can run it. The finished deliverable should be the source code files and documentation, with no input files included.
```

### 542. D3_s983495_zh (domain=D3, difficulty=7)

```
帮我从零做一个面向运维/数据平台的“日志质量与异常监控”小工具，目标是把原始事件流清洗、聚合，并生成可视化 KPI 面板。
- 需要你直接产出可运行的代码，不要依赖任何现成数据文件；自己在代码里生成一套模拟日志事件用于演示。
- 希望包含日志清洗、字段标准化、异常检测（比如突增、空值、重复、延迟异常）和核心 KPI 计算（吞吐、错误率、P95 延迟、数据完整性等）。
- 最好做成一个小型 Web 仪表盘或本地可视化页面，能切换时间窗口、查看异常列表和趋势图。
- 请顺手把项目结构、运行方式、配置项和关键设计写清楚，方便我后续扩展到真实数据源。
- 你需要先做一些 Web 调研，参考合适的 Python/前端可视化库和异常检测实践，再开始实现。
```

### 543. D3_s983499_en (domain=D3, difficulty=7)

```
Build me a from-scratch Python tool for warehouse ops that cleans time-series sensor logs, flags anomalies, and outputs daily KPIs as a terminal dashboard plus CSV/JSON export. Make it use no input files by default: generate synthetic demo data in code, but also support pasted JSONL on stdin and a simple HTTP ingest endpoint in the same repo. I want the core module, CLI/API, tests, and README in separate files.
```

### 544. D3_s983554_en (domain=D3, difficulty=7)

```
I want a small but real dashboard tool that can clean messy operational data, flag anomalies, and surface KPIs in a way a product or ops team could actually use.

- Build a from-scratch Python app that accepts pasted CSV text or generated sample records at runtime, cleans the data, detects anomalies, and computes a few KPIs.
- Include a lightweight visualization layer with charts for trend, outliers, and KPI summary; make it usable from either a CLI or a tiny local web app.
- Research a practical stack first so the implementation follows current best practices for Python data visualization and anomaly detection libraries.
- Add tests for the cleaning rules, anomaly detection logic, and KPI calculations, plus a short README with setup and usage.
- Keep it self-contained with no input files required; the app should create or accept its own data at runtime.
```

### 545. D3_s983588_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team that can clean messy daily shipment records, flag suspicious outliers, and show the KPIs leadership asks for every morning without anyone having to do spreadsheet work by hand. I want the code built from scratch as a simple web app or local dashboard that lets us paste in raw records, automatically standardizes the fields, detects unusual rows, and displays a few clear charts and summary numbers. Please use current best practices and look up a sensible open-source stack for the implementation, then build the tool, tests, and a short README so my team can run it ourselves. There are no input files to start from; the app should include a small synthetic sample dataset generator so we can test it immediately.
```

### 546. D3_s983620_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for our ops team that validates streaming sales KPIs, flags anomalies, and renders a simple dashboard. I need app.py, kpi_rules.py, anomaly_engine.py, dashboard.py, and README.md; no input files, generate synthetic demo data in code and make it runnable locally. Use current best practices for the charting/CLI stack and document any library choices you make.
```

### 547. D3_s983660_en (domain=D3, difficulty=7)

```
We need a small internal tool that helps our operations team keep an eye on daily sales and inventory health without waiting on a data analyst every time. I want you to build it from scratch so it can take raw numbers we paste in later, clean them up, flag anything suspicious, and show a simple dashboard with the main KPIs and warnings. Please design and implement the code for the tool, not a write-up. It should include a way to define the key metrics, detect odd spikes or drops in a practical way, and render a clear visual summary we can use in a browser. Since we don’t have any starting files for you, build the whole thing yourself and make sensible choices after checking current best practices for a lightweight Python dashboard/data-processing stack. Deliver the code files and a short README with how to run it.
```

### 548. D3_s983672_en (domain=D3, difficulty=7)

```
We need a small internal tool that helps our ops team clean up messy sales, support, and fulfillment numbers before leadership meetings, and then surface the weird spikes or drops that need a human review. Please build the code from scratch for a lightweight KPI monitoring app that can ingest pasted CSV text, standardize column names and date formats, flag missing or duplicated rows, detect obvious anomalies in daily metrics, and show a simple dashboard with trend lines and alerts. I want the finished code files and a short README so our team can run it locally and understand how it works. Please research the best lightweight Python plotting and anomaly-detection approach first, then implement the tool with a clean structure and tests.
```

### 549. D3_s983682_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool for internal ops that can clean messy event logs, flag anomalies, and compute a few KPI summaries, then render a simple dashboard report from generated sample data so I can demo it without any input files. Please include the code files, tests, and a README that explains how to run it and what the outputs mean. Use web research where it helps for picking a lightweight plotting/library stack and for following current best practices for anomaly detection and data-cleaning patterns.
```

### 550. D3_s983693_en (domain=D3, difficulty=7)

```
I need you to build a small but real Python tool from scratch that turns raw event logs into a clean KPI dashboard with anomaly detection, like a mini ops-monitoring package. Please create the code, tests, and a short README for a package that can ingest JSON/CSV log records, clean and normalize timestamps and fields, calculate a few operational KPIs, flag anomalies with explainable rules, and render a simple HTML/terminal summary. Use web research where it helps to choose good libraries and follow current best practices for parsing, validation, time handling, and charting, but don’t rely on any starter dataset — the tool should work on data I provide later.
```

### 551. D3_s983721_en (domain=D3, difficulty=7)

```
We need a small internal tool to help our operations team spot bad data earlier and keep our daily KPI dashboard trustworthy. Right now, our team has no consistent way to clean incoming event records, flag unusual spikes or drops, and generate a simple KPI summary we can share with managers. Please build the tool from scratch as real code, not a mockup, with no input files required — it should generate or accept sample records inside the app and show the full flow from cleaning to anomaly checks to KPI output. I want something practical I can run locally: a clear command-line workflow, a reusable processing module, and a simple chart or HTML report showing the results. Please research current Python libraries and best practices for data cleaning, anomaly detection, and lightweight visualization before you code, then implement the solution and include whatever files are needed to run it and understand it.
```

### 552. D3_s983810_en (domain=D3, difficulty=7)

```
Build a small Python package for KPI monitoring called `kpi_guard` from scratch. I want `src/kpi_guard/` with the core data-cleaning, anomaly detection, and KPI calculation modules, plus a CLI entrypoint and a minimal demo dashboard script; no input files, generate synthetic sample data in code. Use current best practices and choose the stack after checking recent docs for pandas/numpy, a lightweight anomaly library or pure-Python approach, and a simple charting option like Plotly or Altair.
```

### 553. D3_s983882_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool that computes cleaning, anomaly-detection, and KPI summaries for streaming event telemetry, then renders a small dashboard and CLI in app.py and README.md. Use web research to pick a solid stack and best practices for the plotting + anomaly layer, but do not rely on any input files or starter data; generate synthetic sample data in code and make the whole thing runnable end to end.
```

### 554. D3_s983884_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for ops KPI monitoring: create `kpi_guard/` with a data-cleaning pipeline, anomaly detection on time-series KPIs, and a small dashboard/API to visualize alerts and trends. I want `README.md`, `pyproject.toml`, and the full source code, with no input files required—generate synthetic demo data in the app and make the whole thing runnable locally.
```

### 555. D3_s983888_en (domain=D3, difficulty=7)

```
We need a small internal tool that helps our operations team clean up messy daily sales numbers, flag odd spikes or drops, and show a simple KPI dashboard without depending on a spreadsheet. Please build the code from scratch so we can run it locally and later plug it into our reporting flow. I want a working app, not a write-up, and it should include a way to enter sample records manually, clean common data issues, detect anomalies, and show key metrics and charts in a browser. Please use current best practices for the libraries and implementation choices, and make sure the code is structured so we can maintain it easily.
```

### 556. D3_s983942_zh (domain=D3, difficulty=7)

```
帮我从零做一个“数据健康检查 + 异常检测 + KPI 仪表盘”小工具，写成可直接运行的代码，主要用于运营数据每天落地后的自动清洗、指标汇总和可视化输出。请分别产出核心库、命令行入口、测试和 README，文件名你自己定，但要能一键跑起来。
```

### 557. D3_s983987_en (domain=D3, difficulty=7)

```
I want a small but real internal tool built from scratch for our ops team: a Python service that ingests event records from a mock API, cleans and standardizes them, flags anomalies, and computes a few KPI summaries with charts.

- Use current best-practice choices for the stack, and check modern library docs or patterns where it helps.
- Build the core processing engine, a simple API/CLI to run it, and a dashboard or report output for the KPIs.
- Include tests for the cleaning rules, anomaly detection, and KPI calculations.
- Make the output easy to run locally and document the setup clearly.
- No input files are provided; generate or simulate any sample data inside the app itself.
```

### 558. D3_s984020_en (domain=D3, difficulty=7)

```
I need a small internal tool that our ops team can use to clean messy daily sales numbers, flag unusual spikes or drops, and show a simple KPI dashboard so we can spot problems before the morning meeting. Build it from scratch as a working code project, not a report, and make it usable without any input files by generating sample data inside the app. I want the finished code and a short README that explains how to run it and what it does. Please use current, reliable web research for the best lightweight library choices and any good practices for anomaly detection and dashboard design, then implement the tool cleanly.
```

### 559. D3_s984031_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch for our ops team that ingests live event records we paste in JSONL, cleans and normalizes them, flags anomalies in near real time, and outputs a KPI summary plus a simple dashboard view. Please use current best practices and a couple of real Python libraries after checking the web for what’s recommended, then give me the finished code files and a short README. There are no input files — the tool should include its own sample data generator and clear CLI commands so we can demo cleaning, anomaly detection, and KPI reporting locally.
```

### 560. D3_s984039_en (domain=D3, difficulty=7)

```
Build a small Python package for KPI data cleaning, anomaly detection, and dashboard-ready summaries from scratch. I need `src/` code for a reusable `kpi_pipeline` module, a `cli.py`, and a `README.md` that explains setup and usage with no sample input files. Use current best practices for Pandas, SciPy/Statsmodels-style anomaly detection, and Plotly or Altair for visualization, and research the API choices before you code.
```

### 561. D3_s984041_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool for ops teams that ingests live KPI text or JSON they paste in, cleans messy fields, flags anomalies, and renders a simple dashboard with trend charts and status colors. Please include the code files, a short README, and make sure it works as a local CLI plus a minimal web UI. No input files are provided, so design the data model and sample fixtures yourself, and research a couple of good Python libraries and best practices first so the implementation is current.
```

### 562. D3_s984098_zh (domain=D3, difficulty=7)

```
帮我从零写一个可直接运行的 Python 工具，做运营指标数据的清洗、异常检测和 KPI 可视化，代码放到 app.py、kpi.py、anomaly.py、viz.py、tests/ 里，顺手补一份 README.md。不要任何输入文件，自己生成一组演示数据并支持命令行跑通；接口设计、库选型和指标口径请参考公开文档后再实现。最后把安装、运行、测试命令都写清楚。
```

### 563. D3_s984162_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool that monitors service KPIs, cleans incoming event data, flags anomalies, and renders a simple dashboard view for ops use. There are no input files — just create the code and supporting docs from scratch, using current best practices and a few web checks for library choices and dashboard patterns. I want the finished code files plus a short README that explains how to run it, what it does, and how the anomaly rules work.
```

### 564. D3_s984164_en (domain=D3, difficulty=7)

```
We need a lightweight internal tool for our operations team to clean messy event data, flag unusual spikes or drops, and turn it into a simple KPI dashboard we can share in meetings. Please build the code from scratch, not a report. There are no source files to start from. I want something that can take a small pasted JSON or CSV payload, standardize the fields, detect obvious anomalies in the daily numbers, calculate a few basic KPIs, and show the results in a simple web page. Please use sensible current practices and check modern options for a Python backend and a small charting library before you build it. I want the finished code files plus a short README so our team can run it locally.
```

### 565. D3_s984170_zh (domain=D3, difficulty=7)

```
帮我从零实现一个 Python 小工具：做一套本地数据质量处理 + 异常检测 + KPI 仪表板，支持读入 CSV/JSON、自动清洗、规则校验、异常点检测，并输出一份可交互的 HTML 报告和命令行结果。代码放到 `src/`，入口是 `main.py`，再给我 `README.md` 和最小可运行示例（自己在代码里造测试数据即可，不要任何外部输入文件）。
```

### 566. D3_s984188_en (domain=D3, difficulty=7)

```
Our ops team keeps asking for a simple way to turn messy event logs into clean daily KPI charts, and we need something we can actually use internally without relying on spreadsheets. I want you to build a small from-scratch data processing and visualization tool that takes raw text or JSON event records entered directly in the app, cleans them up, flags obvious anomalies, and shows a few business KPIs like daily counts, error rate, and unusual spikes in a dashboard. It should be a real working code deliverable, not a mockup, and it should include a clear way to run it locally plus enough guidance that our team can reuse it for new event types later. Please research a sensible lightweight stack and best-practice approach first, then implement the code, tests, and short documentation.
```

### 567. D3_s984197_en (domain=D3, difficulty=7)

```
I need you to build a small Python tool from scratch for our ops team that can clean messy event metrics, flag anomalies, and generate a KPI summary dashboard from live API data — no input files, just code. The tool should pull from a real public endpoint we can wire in later, normalize timestamps and missing fields, detect spikes/drops in a sensible way, and render a simple HTML/PNG report with trend charts and top-line KPIs. Please also include the README and tests, and make the design choices match current best practices for the libraries and APIs you pick.
```

### 568. D3_s984246_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool for cleaning event logs, flagging anomalies, and generating KPI dashboards from raw app metrics. There are no input files yet, so please design the codebase, CLI, core processing pipeline, and visual output files yourself, using current best-practice libraries and patterns you check with web research. I want the finished code files plus a short README, and the tool should be usable on synthetic sample data it generates internally for demos and tests.
```

### 569. D3_s984257_zh (domain=D3, difficulty=7)

```
我需要你从零做一个用于运营数据清洗、异常检测和 KPI 看板的小工具，别用现成模板，直接给我可运行的代码和 README。功能上要能手动生成一组模拟订单/流量指标数据，做缺失值处理、重复值去重、异常点标记，然后输出日报级 KPI 汇总，并用一个简单的网页图表把趋势和异常高亮出来；如果有合适的 Python 库、前端图表方案或异常检测做法，先查一下再定实现。最后把代码、测试和使用说明一起整理好，方便我本地直接跑起来。
```

### 570. D3_s984342_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool for ops dashboards that cleans messy event metrics, flags anomalies, and computes a few KPIs, with a simple web UI to visualize the results. Please make it production-ish: include the core library code, a CLI to run it on generated sample data, and a lightweight dashboard page that shows the cleaned series, anomaly markers, and KPI cards. Do the research you need on a good Python stack for charting, data validation, and anomaly detection, then implement the code and README with setup/run instructions.
```

### 571. D3_s984362_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for cleaning event-stream data, detecting anomalies, and calculating KPIs, with a small web dashboard for results. I want app.py, kpi_rules.py, anomaly.py, and README.md, plus tests. Use current best practices and whichever libraries make sense; no input files are provided, so generate synthetic demo data in the code.
```

### 572. D3_s984368_en (domain=D3, difficulty=7)

```
We need a small internal tool for our operations team that can spot bad daily numbers before they go out to leadership. Build it from scratch as a data-processing and visualization app that cleans incoming event metrics, flags anomalies, and shows a simple KPI dashboard for the last 30 days. I do not have any source files to give you, so please create the whole thing yourself, including the data model, the anomaly detection approach, the dashboard views, and a basic way to run it locally. Use current best practices for the stack and any libraries you choose, and research the most practical options before you build. I want the final code files and a short README with setup and run steps.
```

### 573. D3_s984374_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for cleaning time-series KPI data, anomaly detection, and a simple interactive dashboard. I need app.py, kpi_engine.py, and README.md, plus tests. Use web research for best-practice choices on libraries and anomaly methods, but don’t rely on any input files — generate sample data in code and make the tool work end-to-end.
```

### 574. D3_s984388_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for a customer-support ops dashboard: it should ingest JSONL event streams, clean messy timestamps/status codes, detect anomalies in daily ticket volume and first-response time, and compute KPIs with a small CLI plus a Plotly HTML report. Use current best-practice libraries and patterns, and write the code in app.py, kpi.py, anomalies.py, and report.py with a short README.md.
```

### 575. D3_s984414_en (domain=D3, difficulty=7)

```
I need you to build a small from-scratch Python tool for cleaning messy operational metrics, flagging anomalies, and generating KPI summaries with a simple chart output. Please create the code and a short README for how to run it, with no input dataset provided — the tool should just work on data I pass in later and include sensible defaults. I want it to feel like a real internal utility, not a toy script, and I want you to research the best lightweight library choices and patterns first so the implementation is solid.
```

### 576. D3_s984422_en (domain=D3, difficulty=7)

```
Build a from-scratch Python tool for warehouse KPI monitoring: include a data cleaning pipeline, anomaly detection for daily metrics, and a small dashboard that shows trends and flags issues. Research the current best-practice Python libs and plotting patterns first, then implement it in app.py, tests/, and README.md with no input files required.
```

### 577. D3_s984453_en (domain=D3, difficulty=7)

```
We need a small internal tool that helps us spot bad data before it hits our dashboards and weekly KPI reports. Please build it from scratch for our operations team: a lightweight app that can clean incoming records, flag obvious anomalies, and summarize the health of a dataset with simple KPI-style checks. It should include a clear screen or report showing counts, error rates, anomaly flags, and a few trend indicators, and it should be usable without any uploaded sample file because the tool should generate or accept demo data on its own for testing. Please use current best practices for the chosen stack, and give me the code files plus a short README so my team can run it and understand what it does.
```

### 578. D3_s984476_en (domain=D3, difficulty=7)

```
I need a small internal tool for our operations team that can take live or pasted service metrics and turn them into a clean daily health view. The goal is to cut down on manual spreadsheet work and give us an easy way to spot bad data, sudden spikes, and whether our key numbers are on track. Please build the code from scratch with a simple interface, clear documentation, and tests. I do not have any input files to give you — please design the tool and its sample/demo data yourself. I’d like the solution to use current best practices for Python data handling and visualization, and if you need to make decisions about libraries or chart patterns, research them first. Deliver the built code and a short README so someone on the team can run it and understand what it does.
```

### 579. D5_s980340_zh (domain=D5, difficulty=7)

```
帮我从零开发一个用于排查线上故障的轻量级日志分析工具，目标是能在本地快速定位 API 服务异常的根因。
- 需要支持读取标准输出日志、按时间范围/请求 ID/关键词过滤，并自动聚合常见错误模式
- 希望做成命令行工具，带清晰的子命令和帮助文档，最好能输出 JSON 和人类可读报告
- 要包含一套可运行的测试计划，覆盖日志解析、过滤逻辑、聚合统计和异常输入处理
- 请参考现成工具和最佳实践，选一个合适的实现语言/库，但代码要从零写，不要直接套模板
- 最后给我完整代码、README 和测试说明，方便我直接跑起来验证
```

### 580. D5_s980357_zh (domain=D5, difficulty=7)

```
从零做一个 Python 诊断工具，能读取应用日志/JSON 日志，自动识别常见错误模式（重试风暴、超时链路、异常激增、日志噪声），输出一份可读的 HTML + Markdown 诊断报告。代码放在 `src/`，测试放在 `tests/`，再补一个 `README.md` 说明安装、使用和设计思路；不要用现成同类项目直接套壳，核心分析逻辑自己实现。
```

### 581. D5_s980368_zh (domain=D5, difficulty=7)

```
帮我从零写一个 Go 版日志异常排查小工具，做成一个可直接运行的命令行项目，重点是解析结构化/半结构化日志、按规则聚合错误、输出可读的诊断报告。需要你顺手把 README、测试和示例用法一起补齐，另外先查一下现在 Go 里做 CLI 参数解析、日志切分和表格输出的主流做法，再决定实现方案。
```

### 582. D5_s980369_en (domain=D5, difficulty=7)

```
Build a fresh Python tool called `logshift` for debugging and log analysis: parse mixed JSON/NDJSON and plain-text app logs, detect likely error spikes and repeated stack traces, and generate a concise incident summary from the command line. Use current best practices for Python logging/CLI/test tooling, and write `README.md`, `pyproject.toml`, `src/logshift/`, and `tests/` from scratch.
```

### 583. D5_s980374_en (domain=D5, difficulty=7)

```
We keep losing time whenever a production job fails and the only thing we get back is a messy chunk of logs. I want a small internal troubleshooting tool built from scratch that can take raw application logs, spot likely root causes, group repeated errors, and produce a clear incident summary that our support team can use without reading every line. Please build the code and include a short README that explains how to run it and what it detects. I want it to be practical for our current stack, so please research a couple of common logging patterns and best practices first, then implement the tool in a clean way with tests.
```

### 584. D5_s980388_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool that helps engineers debug flaky test runs from CI logs. I want a small but real utility that can ingest raw text pasted from GitHub Actions, GitLab CI, or Jenkins logs and turn it into a structured failure summary.

- Identify likely root-cause categories like timeout, assertion failure, network error, dependency/install failure, and environment/configuration issue.
- Extract useful signals from noisy logs: failing test name, error line, stack trace tail, first failure point, and repeated retries.
- Include a simple CLI with a few subcommands so I can summarize a log, inspect one failure in detail, and export JSON.
- Add solid tests for the parser and classifier, plus a short README showing how to use it on real CI output.
- Research current best practices or relevant library choices before implementing, especially for Python log parsing, CLI ergonomics, and how GitHub Actions/GitLab/Jenkins logs are typically formatted.
```

### 585. D5_s980392_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called logdoctor that parses raw Kubernetes pod logs plus Python app stack traces, groups repeated failures, and produces a root-cause summary with recommended next actions. I want app.py, log parser/core modules, and a README.md with setup, usage, and examples.
```

### 586. D5_s980406_en (domain=D5, difficulty=7)

```
I need you to build a small Python debugging tool from scratch that watches app logs, detects common failure patterns, and turns them into a clean incident summary with likely root-cause hints. Please make it a real usable command-line utility with a parser for plain text logs, a rules engine for matching stack traces and timeout/retry patterns, an output report in Markdown, and a solid test suite. Use web research where it helps for current best practices and library choices, then implement the code and README yourself — no starter files, no input dataset, just the tool and tests.
```

### 587. D5_s980448_zh (domain=D5, difficulty=7)

```
我想从零做一个面向工程排障的本地工具，重点是分析服务日志、快速定位错误模式，并能生成可执行的排查建议。
- 先帮我调研并选型 2-3 个适合的 Python 方案/库，重点看标准库、Rich/typer、以及日志解析/文本模式匹配的最佳实践。
- 然后直接实现一个命令行工具：支持读入本地日志文本、按时间窗口和关键词过滤、聚合错误类型、输出摘要报告，还要能对常见异常模式给出建议。
- 需要把核心解析引擎、CLI、测试、以及使用说明分开做好，代码要能直接运行，测试要覆盖主要逻辑和边界情况。
- 最后给我一份简短的设计说明，说明你为什么这样选型、有哪些限制、后续怎么扩展到 JSON 日志或多服务日志。
```

### 588. D5_s980453_zh (domain=D5, difficulty=7)

```
帮我从零做一个本地日志排障工具，支持读取 Nginx / Python / Docker 容器日志，自动按时间线聚合、提取错误模式、给出可能根因和修复建议。请直接产出代码和文档：main.py、parser.py、analyzer.py、cli.py、tests/、README.md，要求命令行可用，别用现成大框架。
```

### 589. D5_s980456_en (domain=D5, difficulty=7)

```
I need you to build a small but real Python tool from scratch that helps debug flaky services by parsing app logs, grouping repeated errors, and generating a clean incident summary with likely root-cause hints. Please make it a proper repo with the core parser/analyzer, a CLI, a few focused tests, and a README that explains how to use it with sample log snippets (no input files from me — create your own examples in the docs/tests). Use web research to check current best practices and library choices for Python log parsing, CLI design, and testing, then implement the code and files directly.
```

### 590. D5_s980479_en (domain=D5, difficulty=7)

```
I need you to build a small log-debugging toolkit from scratch for incident triage: parse plain text app logs, detect repeated error patterns, summarize likely root causes, and generate a clean markdown report plus a CLI to run it. Please research current best-practice Python libraries for parsing/regex/reporting and any recommended approaches for structured log handling before you code, then produce the full codebase with tests and a README. No input files are provided — the tool should work on logs pasted in or read from stdin.
```

### 591. D5_s980496_zh (domain=D5, difficulty=7)

```
我想从零做一个用于排查线上故障的命令行工具，目标是帮工程师快速分析应用日志里的异常线索。
- 先帮我做一份可落地的实现方案，并直接把工具代码写出来，不要依赖现成模板工程。
- 工具要支持读取多种日志格式（至少包含常见的 JSON 日志和纯文本日志），能按时间、级别、关键字筛选。
- 希望它能自动提取错误聚类、统计高频异常，并输出一个适合排障的摘要报告。
- 需要补上测试计划和单元测试，覆盖解析、过滤、聚合和边界情况。
- 最后给我一个简洁的 README，说明安装、用法和常见故障排查场景。
```

### 592. D5_s980531_en (domain=D5, difficulty=7)

```
I want a small but real developer tool built from scratch for debugging service logs and catching regressions before they hit production.

- Build a CLI in Python that can ingest plain text or JSONL logs and summarize errors, warnings, top exception types, and slow requests.
- Add a rules engine for alert-style checks, like repeated error bursts, missing correlation IDs, and latency spikes, with a clean exit code for CI use.
- Include a test plan and a solid automated test suite covering parsing edge cases, rule evaluation, and CLI behavior.
- Research a few current Python libraries and best practices first so the design is sane and lightweight, then implement the tool and document how to use it.
- I want the deliverable as the built code plus a short README explaining architecture, commands, and example outputs.
```

### 593. D5_s980541_zh (domain=D5, difficulty=7)

```
我们最近在排查线上接口偶发超时和错误率波动，但现在每次只能靠人工翻日志，效率太低。我想从零做一个轻量工具，专门用来分析服务日志，自动找出失败请求、超时、慢请求和可疑的错误峰值，并把结果整理成一份适合给开发和运维看的报告。你帮我直接设计并实现这个工具，最好同时带上命令行入口、可配置的规则、基础测试和一份简单说明，方便我们后面接到 CI 里。

我希望你先参考一下现在常见的日志处理方式和 Python 里适合做这类事情的库，确认一下命令行参数、输出格式、测试习惯这些怎么设计更稳妥，然后再从头把代码做出来。工具本身不要依赖现成的数据文件，代码里要能接收我们以后自己提供的日志文本或日志目录。最后给我可以直接运行的代码和说明文档，能看得出怎么安装、怎么用、怎么扩展规则。
```

### 594. D5_s980544_en (domain=D5, difficulty=7)

```
I want a small but real debugging/observability tool built from scratch for Kubernetes logs and test failures.

- Build a Python CLI that can ingest plain-text app logs from stdin or a file and flag likely root causes using rules you design.
- Add a log-pattern library for common issues like connection timeouts, auth failures, retries, and out-of-memory events, with a clear explanation output.
- Include a compact test plan plus automated tests that cover the main detection paths and edge cases.
- I also want a short README with install/run examples and a section on how the heuristics were chosen from current best practices.
- Do a bit of web research first on modern logging/debugging guidance for Python/Kubernetes so the patterns and output format are realistic, then implement everything from scratch.
```

### 595. D5_s980546_en (domain=D5, difficulty=7)

```
Build a from-scratch Python 3.12 incident-log triage tool for our on-call workflow that turns raw application logs into an actionable debugging brief. I need a small library plus CLI that can ingest pasted log text from stdin or a string argument, normalize common timestamp formats, cluster repeated exceptions by stack-trace fingerprint, extract request/correlation IDs, detect probable root-cause candidates from known patterns (timeouts, auth failures, connection resets, OOM, schema mismatch), and emit a structured JSON report plus a human-readable summary. Use current best practices for CLI design, log parsing, and Python packaging; research the relevant standard-library and any lightweight parsing libraries on the web before implementing. Deliver the code, tests, and a concise README with usage examples and output schema.
```

### 596. D5_s980548_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for Kubernetes incident debugging: a CLI that ingests live text from stdin, detects common failure patterns across app logs, and outputs a ranked incident summary with probable causes and next-step checks. Put the code in `triage.py`, tests in `test_triage.py`, and a short `README.md`; use current best-practice references for Python logging/regex/CLI design before you code.
```

### 597. D5_s980564_zh (domain=D5, difficulty=7)

```
我需要你从零搭一个用于排查线上事故的日志分析小工具，最好先做成一个可运行的命令行程序，能读取标准输入里的文本日志，按时间窗口聚合错误、提取高频异常堆栈、按 request_id 串起一次请求的完整链路，还能输出适合排障的摘要和 JSON 报告；同时把项目结构、用法说明、测试计划和你选用的日志解析/命令行库一起整理好，代码、README 和测试都要能直接跑起来，不要依赖我提供任何输入文件。
```

### 598. D5_s980595_zh (domain=D5, difficulty=7)

```
我们现在要把客服和运维一起用的故障排查效率提上来，尤其是线上日志一多，大家经常要手工翻半天，定位慢、还容易漏线索。我想从零做一个小工具，能把一段服务日志粘进去后，自动帮我找出错误、按时间线整理关键事件、给出可能的根因线索，并且把重复报错、超时、重试这些模式单独拎出来，方便给值班同事看。你帮我直接做成一个可运行的命令行工具，最好还能顺手带一个简单的本地网页预览界面，方便复制日志后直接看结果。实现前先自己查一下现在常见的日志解析和命令行工具写法，选一个合适的方案，不要照搬模板。最后把代码、测试和使用说明一起给我，确保我拿到后能直接跑起来。整个项目不要依赖任何现成输入文件，我会自己把日志贴进去测试。
```

### 599. D5_s980597_zh (domain=D5, difficulty=7)

```
我想从零做一个面向工程团队的日志排障小工具，重点是把分散的服务日志快速归类成“异常爆发 / 依赖超时 / 配置错误 / 部署回滚后遗留问题”这几类，并输出可读的诊断报告。
- 需要你先做一点 Web 调研，选一个合适的 Python 日志解析/CLI 方案，确认常用库的最佳实践，再开始设计实现。
- 帮我从零实现一个可运行的命令行工具，支持读取文本日志、正则/模板匹配、规则打分、聚合统计和导出 Markdown 报告。
- 希望把核心解析引擎、CLI 参数层、规则系统、测试、文档分成独立模块一起做，最后能整合成一个完整项目。
- 需要补上单元测试和一份简洁的使用说明，确保别人拿到仓库就能直接跑起来验证效果。
- 如果你觉得有必要，也可以顺手加上一个最小的 demo 日志生成器，方便演示和回归测试。

```

### 600. D5_s980599_en (domain=D5, difficulty=7)

```
Build a from-scratch Python 3.12 incident-log triage tool for our SRE workflow: a CLI that ingests raw application log text from stdin or a pasted multiline string, detects likely root-cause signals using configurable regex rules plus a small baseline anomaly scorer, groups related events into incident candidates, and emits a structured JSON summary plus a human-readable report. I need you to research current best practices for Python CLI packaging, log parsing, and JSON output conventions before implementing, and include a short README with usage and design notes. No input files are provided; design the parser, scoring, and report generation yourself.
```

### 601. D5_s980613_zh (domain=D5, difficulty=7)

```
我们团队经常需要手动检查服务器日志来定位 bug，非常耗时。我想请你构建一个命令行工具，能自动读取日志文件，识别常见的错误模式（比如 404、500、内存溢出、段错误、超时等），然后输出一份结构化的错误摘要和对应的调试测试计划。工具要能处理至少三种日志格式，比如 Apache access log、Python traceback、syslog。我不需要你分析已有的数据，而是要你从零开始编写这个工具。请确保它可以直接在终端运行，并且附带清晰的说明文档。最终交付物是工具代码和 README。
```

### 602. D5_s980614_zh (domain=D5, difficulty=7)

```
我们团队每天要分析大量服务器日志来定位错误，但手动查找太慢，还容易漏掉关键信息。我需要你帮我从零开发一个轻量级的日志分析工具，能自动解析常见格式的日志（比如Nginx、Java异常堆栈、系统syslog），提取错误级别、时间戳、错误消息和堆栈摘要，并输出清晰的结构化报告（比如按错误频率排序的前10个错误，或者按时间线展示）。这个工具要能通过命令行使用，支持自定义正则解析规则（比如用户新增一种日志格式时能自己配置）。另外，考虑以后扩展，最好模块化设计，单元测试覆盖核心逻辑。做完后给我一个完整的Python脚本和一个简单的使用说明文档。你先上网查一下当前主流的日志解析库和最佳实践，确保设计合理。
```

### 603. D5_s980615_zh (domain=D5, difficulty=7)

```
我需要你从零搭一个用于排查日志问题的小工具，目标是做一个命令行程序，能读入一段服务日志后自动按错误类型聚类、提取关键上下文、给出可能的根因提示，还能生成一份适合发给值班同事的排障摘要；同时把你参考过的开源做法、日志解析相关的最佳实践和你选型的原因写进 README.md，最后把核心代码、测试和使用说明都整理好给我。
```

### 604. D5_s980616_zh (domain=D5, difficulty=7)

```
我需要你从零写一个用于排查线上问题的“日志事件关联与根因提示”小工具，目标是把多服务的 JSON 日志按 request_id / trace_id 关联起来，自动重建一次请求的关键调用链、标出异常与超时、并输出一个可读的诊断报告和一个简单的命令行界面。代码、测试和 README 都一起给我，最好顺手把你选用的 Python 日志解析、结构化输出和命令行库的最佳实践也查一下，避免我后面踩坑；不要依赖任何现成数据文件，直接把工具和示例用例都从头写出来。
```

### 605. D5_s980619_en (domain=D5, difficulty=7)

```
We need to cut down the time it takes our ops team to find and explain incidents from logs, because right now every outage turns into a manual grep exercise. Build a small but real log triage tool from scratch that can read plain-text application logs and help a support engineer answer: what happened, when did it start, which requests were affected, and what looks most likely to be the root cause. I want a usable command-line tool, a short README, and tests. Please choose a sensible stack, research any common log parsing or CLI libraries you think fit, and make the tool robust enough for messy real-world logs, not just one perfect format. There are no input files provided; the tool should work with logs pasted in or read from standard input.
```

### 606. D5_s980629_en (domain=D5, difficulty=7)

```
I need you to build a small log-triage tool from scratch that helps debug flaky CI jobs by ingesting plain-text build logs and turning them into a structured failure summary with probable root causes, repeated error clustering, and a timeline of the last 200 lines. Please research the best-fit Python libraries and any current guidance for parsing large logs, then implement the tool, tests, and a short README. I want the code files and docs, not a writeup.
```

### 607. D5_s980632_en (domain=D5, difficulty=7)

```
I want a from-scratch debugging tool for our backend logs that actually helps triage incidents instead of just dumping text.
- Build a small Python 3.11 command-line app that ingests raw JSON logs from stdin and turns them into incident summaries, suspected root-cause buckets, and a human-readable timeline.
- Make it smart enough to detect common patterns like retries, timeouts, auth failures, and dependency errors, then group related events into a single incident with a confidence score.
- Add a real test plan and automated tests for the parser, grouping logic, and edge cases like malformed lines, out-of-order timestamps, and duplicate events.
- Use web research to choose a practical stack and follow best practices for log handling and CLI UX, then implement the code and docs from scratch.
- I want the final deliverables to be the working code plus a README that explains usage, design choices, and how to run the tests.
```

### 608. D5_s980637_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called logtriage that ingests raw app logs from stdin, clusters repeated error signatures, and outputs a ranked incident report with probable root-cause hints. I want logtriage.py plus README.md, and use current Python stdlib/logging best practices plus any useful libraries or patterns you research first.
```

### 609. D5_s980637_zh (domain=D5, difficulty=7)

```
我们团队平时要分析大量服务器日志来排查线上问题，但人工翻日志太慢了，而且容易漏掉关键异常。我想让你从头帮我开发一个命令行工具，专门用来分析日志文件。这个工具不需要任何输入文件，它本身就是一个可执行的脚本，用户只需要在终端里指定日志文件路径，它就能自动识别日志格式（比如JSON、CSV、纯文本），统计不同日志级别的数量，检测常见的异常模式（例如空指针、超时、连接失败），并生成一份简洁的总结报告。另外，工具还得有清晰的帮助命令和错误提示。我需要你把核心代码、命令行界面、单元测试和一份使用说明全部写好。你可以先用网络查一下主流的日志解析库和命令行框架的最佳实践，然后直接编码。最终给我一个可以直接运行的Python脚本和README文档就行。
```

### 610. D5_s980660_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called logtriage for debugging production logs. I want app.py, parser.py, heuristics.py, and README.md, plus a small test suite that exercises real log patterns and failure modes. Make it detect error spikes, group repeated stack traces, and output a short triage summary from raw text logs; use current best practices/docs from Python logging, regex handling, and any useful open-source log-analysis libraries as research references before implementing.
```

### 611. D5_s980682_zh (domain=D5, difficulty=7)

```
我需要你从零开发一个命令行日志分析工具，专门用来解析和总结服务器错误日志。工具要能自动识别常见的错误模式（比如OOM、连接超时、权限拒绝等），并输出一个带有统计信息和样本行的摘要报告。请包括：核心解析引擎（支持流式读取大文件）、CLI接口（支持-f输入、-o输出、--mode快速/详细等选项）、单元测试，以及一份清晰的README。在开始编码前，先做一下网络调研，看看有哪些成熟的日志解析库（比如Python的logparser、re、pandas等）以及最佳实践，确保方案合理。最后交付一个可以直接运行的脚本和一个README文档。
```

### 612. D5_s980685_en (domain=D5, difficulty=7)

```
Our support team is drowning in production logs. Every incident requires hours of manual digging to find root causes. I need you to build a command-line tool from scratch that can parse common log formats (JSON, syslog, Apache combined logs), automatically detect stack traces and error patterns, aggregate error frequencies, and output a structured summary report with possible root cause categories. The tool must be extensible to new log formats, include a clean CLI with subcommands (parse, analyze, report), and come with a comprehensive test suite. Research best practices and existing libraries (like Python's logging, regex, pyparsing) before you start coding. Deliver the full source code, unit tests, and a README with usage examples.
```

### 613. D5_s980690_en (domain=D5, difficulty=7)

```
We need a small internal troubleshooting tool because our support team keeps losing time sifting through messy application logs when customers report outages. Please build a from-scratch log investigation utility that can take plain-text log lines pasted into it, detect likely error patterns, group related events into a short incident summary, and produce a clean report the team can share with engineering. I want you to design the whole thing and deliver the code and a short README. Please research a few current best-practice approaches for parsing logs, grouping repeated errors, and writing a simple command-line tool before you build it, since I want this to be practical and not just a toy.
```

### 614. D5_s980712_zh (domain=D5, difficulty=7)

```
请帮我开发一个从零开始的日志分析工具，用于调试和生成测试计划。我希望它是一个命令行工具，能够解析常见的日志格式（比如 Apache 访问日志、syslog 和自定义 JSON 日志），检测异常模式（比如错误突增、响应时间异常），然后自动生成对应的测试用例计划。具体要求：
- 工具必须是纯 Python 实现，无需任何外部数据文件，用户通过命令行传入日志文件路径。
- 支持至少三种不同日志格式的解析，每种格式需要不同的正则表达式或解析逻辑。
- 异常检测应基于滚动统计（比如平均值和标准差），并输出异常时间段和可能的根因。
- 测试计划输出为 CSV 文件，每个测试用例包含描述、预期行为、优先级。
- 命令行接口要友好，有子命令（parse、analyze、plan），并且处理错误输入。
- 附带完整的单元测试和清晰的 README 文档。
```

### 615. D5_s980714_zh (domain=D5, difficulty=7)

```
我们最近在排查线上告警时，最耗时间的不是修代码，而是每次都要人工翻日志、对时间线、猜根因。我想做一个从零开始的小工具，帮我们把一段服务日志自动整理成可读的故障分析结果，至少能看出异常开始时间、相关错误链路、可能的根因线索，以及给出下一步排查建议。你先帮我调研一下适合的日志解析和时间线归纳做法，然后直接把工具做出来。希望它是一个命令行工具，能接收标准输入的日志内容，输出结构化分析结果；最好再带一个简单的测试计划和使用说明。不要依赖现成的样例文件，工具本身要从头写，方便我们后面接到内部服务里用。
```

### 616. D5_s980731_en (domain=D5, difficulty=7)

```
I need a log analysis CLI tool that I can use to debug issues. It should parse JSON log files or plain text with timestamps and let me filter by level, time range, or keywords; compute basic stats like error count per minute; and detect anomaly spikes in error rates. Build it from scratch in Python, no input files given. Make sure it's well-tested with unit tests and has a clear README. Use web research to decide on efficient parsing and anomaly detection methods.
```

### 617. D5_s980732_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for debugging log spikes in a Kubernetes service: `log-spike-analyzer.py` plus `README.md`. It should ingest raw text logs from stdin or a path, detect bursty error patterns, cluster related stack traces, and output a concise incident summary with timestamps, top fingerprints, and suspected root-cause hints. Research current best practices for log fingerprinting, regex-based stack-trace collapsing, and CLI UX from real Python tooling docs before implementing.
```

### 618. D5_s980742_zh (domain=D5, difficulty=7)

```
帮我从头写一个命令行日志异常检测工具，用来分析Nginx/Apache的combined格式访问日志，自动识别异常（比如突然大量404、响应时间飙升、错误率超过阈值），输出一份摘要报告和异常列表。需要用Python实现，代码要有模块化结构、单元测试和文档。你先调研一下Apache combined日志格式的具体字段定义、常用的异常检测算法（移动平均、Z分数之类的），以及用哪个CLI库（比如click或argparse）最合适，然后开始写。最终给我一个可以直接跑的脚本log_anomaly_detector.py、README.md和requirements.txt。
```

### 619. D5_s980746_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for debugging Kubernetes app logs: implement a CLI that tails logs, filters by pod/namespace/time window, detects common error patterns, and outputs a compact incident summary with suggested next checks. I want the code in app.py, tests in tests/, and a short README.md with install/run examples.
```

### 620. D5_s980747_zh (domain=D5, difficulty=7)

```
我需要你从零做一个面向 SRE/后端排障的日志分析小工具，重点是把一堆杂乱的 JSON/文本日志里和请求链路相关的字段抽出来，按 trace_id/request_id 关联成可读的故障时间线，还要顺手做异常模式统计和一个简单的命令行界面。希望你先调研一下 Python 里做日志解析、正则/结构化输出、CLI 参数和测试的常见做法，再直接把代码、README 和测试都写好；不用我给任何输入文件，工具本身要能处理我之后丢进去的日志内容。
```

### 621. D5_s980753_zh (domain=D5, difficulty=7)

```
帮我从零做一个面向 SRE/后端排障的日志诊断小工具，目标是把一段服务日志快速归类、提炼异常模式，并输出可读的排障报告。

- 我想要一个可运行的命令行工具，支持读取标准输入或本地文本日志，自动识别常见错误模式、请求链路 ID、时间窗口和高频异常。
- 先做一轮 Web 资料调研：对比 2-3 个常见日志处理库/方案（比如 Python 里的正则、argparse、rich、loguru 或类似工具），并参考一些业界日志规范和最佳实践，确定实现方式。
- 功能上希望包含：日志解析、规则匹配、聚类/归因、输出 Markdown 报告，以及一个最基本的测试计划和单元测试。
- 最终交付希望是完整代码和说明文档，能直接在本地运行、测试、演示；如果你觉得合适，也可以顺手补一个示例日志生成器用于自测，但不要依赖外部输入文件。
- 这个工具要尽量贴近真实生产排障场景，能处理混合格式日志、时间戳缺失、重复报错、堆栈跟踪这些常见问题。
```

### 622. D5_s980759_zh (domain=D5, difficulty=7)

```
我需要你从零做一个面向工程排障的日志分析小工具，最好用 Python 实现，目标是把一批服务端日志里的错误、超时和重试链路自动归类，输出一份可读的故障摘要和时间线；你直接把代码和 README 写好，顺手加上单元测试和一个简单 CLI，重点是要能在本地跑起来，支持常见的 JSON/文本日志输入、规则配置、以及生成 Markdown 报告。
```

### 623. D5_s980771_en (domain=D5, difficulty=7)

```
I need you to build a small log-triage tool from scratch for a Node.js service: a CLI that reads plain-text app logs, groups repeated errors, detects probable root causes from stack traces and correlated log lines, and outputs a compact incident summary plus JSON. Please include the code files, tests, and a short README, and use current best-practice guidance for parsing/CLI libraries and structured logging patterns so the design is solid.
```

### 624. D5_s980774_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering teams spot problems faster from log files and incident notes. Please build it from scratch as a command-line utility that can read raw application logs, detect common error patterns, group related messages into incidents, and produce a short plain-English summary of what likely went wrong and what to check next. I want the code, a short README, and tests. Please also check current best practices for log parsing and CLI packaging before you build it, because I want this to be something we could realistically hand to an engineer to extend later.
```

### 625. D5_s980784_en (domain=D5, difficulty=7)

```
I need you to build a small log-debugging tool from scratch for our SRE team: a Python CLI that tails a live application log, recognizes common failure patterns, groups related stack traces, and outputs a readable incident summary with likely root-cause hints. Please use web research to pick a sensible parsing/logging approach and any lightweight library choices, then deliver the code files plus a short README with setup and usage. There are no input files to start from.
```

### 626. D5_s980789_zh (domain=D5, difficulty=7)

```
帮我从零搭一个可直接跑的命令行工具，用来做“日志 + 测试失败”的自动排障。
- 目标是把一份程序运行日志和一份测试输出（都直接作为命令行文本输入）解析后，自动归类常见问题：依赖缺失、断言失败、超时、端口冲突、配置错误、网络错误、异常堆栈等。
- 希望它能给出一个结构化诊断结果：问题类型、命中证据、可能根因、建议下一步排查动作。
- 需要同时提供一个 CLI 和一个可复用的 Python 库接口，便于后面嵌到 CI 里。
- 还要补一套测试计划和单元测试，重点覆盖真实日志格式的边界情况、误报/漏报风险，以及输出稳定性。
- 如果需要参考现成最佳实践、Python 标准库用法、日志解析/测试失败分类思路，可以先做一轮 web 调研再开工；最后把代码、README 和测试都整理好。
```

### 627. D5_s980803_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for our incident-response workflow that ingests raw application logs from stdin or a string literal, detects duplicate root-cause signatures, clusters related errors by stack-trace similarity, and emits a concise triage report plus a machine-readable JSON summary. I want a small but production-minded package with a CLI, reusable library API, and a test suite. Research current best practices and library choices first — especially Python log parsing, stack-trace normalization, approximate string matching, and CLI ergonomics — using web sources like the Python docs, RapidFuzz docs, click/typer docs, and any relevant logging/debugging guidance. Then implement the tool from scratch with no starter files.

Concretely, the tool should: parse unstructured log lines with timestamps/severity/module fields when present; normalize Python traceback blocks; deduplicate recurring errors by signature; group related incidents into clusters; and produce both a human-readable summary and a JSON output mode. Include a minimal CLI with flags for input source, output format, similarity threshold, and top-N clusters. The final deliverable should be the built code files and README/test artifacts, not a report.
```

### 628. D5_s980830_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for a containerized service: create `logtriage.py`, `tests/`, and `README.md`. It should parse mixed JSON and text logs, detect error spikes, cluster similar stack traces, and output a compact incident summary with likely root-cause hints. Use current best practices from the web for Python logging, regex/stack-trace parsing, and CLI UX before implementing.
```

### 629. D5_s980837_en (domain=D5, difficulty=7)

```
I need a from-scratch internal debugging tool for our engineering team that turns raw application logs into a compact incident timeline and a suggested triage plan.

- Build a small command-line app that ingests plain text logs from stdin, groups related events into sessions, and highlights likely root-cause signals.
- Include a rules engine for parsing common web/app patterns like retries, timeouts, auth failures, rate limits, and stack traces.
- Add a short report mode that summarizes what happened, when it started, and the top suspected failure modes.
- Make it easy to run locally with clear usage instructions, and include tests that cover the parsing and grouping logic.
- Use current best practices for log parsing and CLI design, and base the implementation on up-to-date research into Python libraries and command-line conventions.
```

### 630. D5_s980846_zh (domain=D5, difficulty=7)

```
我们现在要把线上故障排查做得更快一点，尤其是客服和运维经常要从零散日志里找出同一次请求的完整链路，但手工翻日志太慢了。请你从零开始做一个小工具，能把应用日志里的请求、错误和耗时信息自动串起来，帮助我们快速定位问题。

我希望你先做调研，看看常见日志格式、Python 里适合做日志解析和命令行工具的库，以及业界常用的输出和排查方式，然后再直接把工具做出来。这个工具最好能：
- 支持命令行运行，输入一段日志文本或从标准输入读取都可以
- 自动识别时间、级别、请求ID、用户ID、接口路径、错误信息、耗时这些字段（尽量兼容几种常见写法）
- 按请求ID把同一条链路的日志聚合出来，输出成便于排查的摘要
- 能标出疑似异常，比如报错、超时、明显慢请求、重复失败
- 顺手给我一个简单的使用说明和测试方案，方便后面交给别的同事用

如果你觉得有必要，也可以给我一个很基础的 Web 接口，但不是必须；重点是要把这个日志分析小工具本身做扎实。最后请直接给我代码和说明，最好能让我拿来就能跑。
```

### 631. D5_s980884_zh (domain=D5, difficulty=7)

```
帮我从零开发一个面向 SRE/平台工程的“日志异常 triage”小工具，目标是把一段服务日志快速归类成可能的故障类型，并给出可执行的排查建议。
- 这个工具要能在本地命令行运行，支持粘贴日志或从 stdin 输入，输出结构化结果（JSON 或清晰表格都可以）。
- 需要内置一套可维护的规则/模式库，至少覆盖超时、连接失败、认证失败、限流、OOM、配置错误这几类常见问题。
- 希望你把核心分析引擎、CLI、测试、文档分开设计并实现，最后给我可直接运行的代码和 README。
- 需要参考一下现成的日志分析/CLI 设计最佳实践，选用合适的 Python 库或标准库方案，但实现必须是你从头写。
- 重点是要考虑误报、重叠匹配、置信度排序和可扩展性，别只是简单的关键词匹配。
```

### 632. D5_s980885_en (domain=D5, difficulty=7)

```
I want a small but real log-debugging tool built from scratch for our SRE workflow.
- Make it a command-line app that can ingest plain-text application logs, detect recurring error patterns, and summarize likely root causes.
- Include a rule-based parser plus a simple anomaly detector for spikes in error frequency, with a clear explanation of how each works.
- Add a few useful commands like scanning a log file, viewing grouped incidents, and exporting a compact incident report.
- Write tests for the parser, pattern grouping, and anomaly detection, and include a short README with setup and usage.
- Use current best practices for Python CLI tooling and logging libraries, and research any library choices before coding.
```

### 633. D5_s980931_zh (domain=D5, difficulty=7)

```
我们现在要把线上故障排查这件事做得更快一点，减少工程师在日志里手工翻来翻去的时间。我希望你从零做一个可运行的小工具，专门帮我们分析应用日志里的报错和异常模式，最好能直接看出最近哪些错误在变多、哪些请求链路最容易失败、以及同一类问题是不是反复出现。你可以自己决定最合适的实现方式，但要做成真正能用的代码，不是只写思路。请你先查一下现在常见的日志解析、异常分组、命令行工具和测试做法，再基于这些资料设计并实现这个工具。最终请交付完整代码、使用说明和测试方案，尽量考虑真实团队会怎么用它来做日常排障。
```

### 634. D5_s980944_en (domain=D5, difficulty=7)

```
I need a from-scratch Python tool that helps debug flaky CI jobs by analyzing build logs and test output, then suggesting the most likely root-cause patterns.
- Build a small CLI that can ingest pasted text logs, auto-detect common failure classes, and summarize the evidence with timestamps/line references.
- Include a rules-based parser for noisy logs from GitHub Actions, pytest, and JavaScript test runners like Jest or Playwright.
- Add a confidence-scored report that distinguishes infrastructure issues, assertion failures, timeout patterns, and environment/setup problems.
- Generate a short Markdown summary plus a machine-readable JSON result.
- Research a few current best practices and library choices for log parsing, CLI design, and terminal output formatting before implementing.
```

### 635. D5_s980951_en (domain=D5, difficulty=7)

```
I need you to build a small log-triage tool from scratch for debugging incidents in Kubernetes apps: it should watch a live stream of logs, detect likely error patterns, group related lines into incidents, and print a concise root-cause summary with confidence notes. Please research a couple of current Python log parsing / CLI libraries and best practices first, then implement the code, tests, and a short README; I want the finished files, not a writeup. There are no input files for this one — just build the tool and make it runnable from the command line.
```

### 636. D5_s980960_zh (domain=D5, difficulty=7)

```
给我从零写一个 Go 语言的日志异常检测小工具，支持读取 stdin 或文件、按规则匹配错误模式、输出 JSON 报告和退出码。顺手补一份 README.md、测试用例和一个最小 CLI，代码要能直接跑。去查一下现在常用的 Go 标准库/第三方库怎么做日志解析、CLI 参数和 JSON 输出，再按查到的最佳实践实现。
```

### 637. D5_s980971_en (domain=D5, difficulty=7)

```
Build a from-scratch Python 3.12 command-line tool for postmortem log triage that ingests one or more plain-text application logs from stdin, classifies incidents by error signature, and emits a concise diagnostic report with clustering, top stack traces, and probable root-cause hints. I want this to be designed against current best practices for Python logging, structured exception parsing, and CLI ergonomics, so do web research first on relevant libraries and conventions (for example: Python stdlib logging patterns, Typer/Click CLI usage, regex/stack-trace parsing approaches, and any modern log deduplication or similarity techniques worth borrowing). Build the tool from scratch with no starter files or sample inputs, and include a small test suite and usage docs. Deliver the code files and README, not just an explanation.
```

### 638. D5_s980973_en (domain=D5, difficulty=7)

```
Build a from-scratch Python incident-log triage tool for our GitHub Actions runs: one core module that parses logs, classifies failure patterns, and produces a root-cause summary; one CLI with "scan", "explain", and "report" commands; and a README with setup and usage. Research the current best practices for GitHub Actions log access, Python regex/log parsing, and CLI design before you implement it.
```

### 639. D5_s981001_zh (domain=D5, difficulty=7)

```
我需要你从零做一个面向工程排障的日志分析小工具，目标是给一组服务端应用的结构化日志和纯文本日志做统一解析、按请求链路串起来、自动标出错误根因和可疑时间窗口，并提供一个本地 CLI 可以直接跑。请把代码、README 和一套可运行的测试一起交付出来；实现前先查一下当前常见日志格式处理库、CLI 参数设计和 Python 里做高亮输出的最佳实践，避免自己重复造轮子。最后希望工具能支持常见的 JSON 日志、logfmt 和普通文本三种输入方式，输出一份可读的故障摘要。
```

### 640. D5_s981033_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for on-call log triage that detects repeating error patterns, groups them into incident candidates, and generates a concise markdown summary with likely root-cause clues. I want the code in app.py plus a README.md with setup, usage, and a few example invocations; no input files, it should read logs from stdin or a live tail command.
```

### 641. D5_s981053_en (domain=D5, difficulty=7)

```
I want a small but real developer tool built from scratch for debugging production logs.
- Build a CLI that ingests plain-text application logs from stdin or a file path and flags likely incident signatures like error bursts, request timeouts, retry storms, and sudden latency spikes.
- Make it configurable with a simple YAML or JSON config for patterns, thresholds, and severity levels, and include a sane default ruleset.
- Add a compact report mode that prints a human-readable summary plus a machine-readable JSON output for use in CI or on-call workflows.
- Include a focused test suite covering parsing, detection logic, config loading, and edge cases like malformed lines and empty input.
- Before coding, do quick web research on current best practices for CLI ergonomics, Python log parsing libraries or standard-library options, and any relevant guidance for structured output and config handling.
- Deliver the code and a README with install, usage, and examples.
```

### 642. D5_s981065_en (domain=D5, difficulty=7)

```
I want a small but real observability tool built from scratch for incident debugging.
- Build a Python CLI that ingests application logs from stdin and groups related errors into incident-style summaries.
- Include support for stack-trace collapsing, repeated-message clustering, and a simple "most likely root cause" heuristic.
- Add a compact local web dashboard or HTML report so I can review the grouped incidents after a run.
- Use current best practices from the ecosystem for log parsing and CLI design, and check a couple of relevant libraries or docs before implementing.
- Make sure it ships with tests and a short README showing how to run it and what the output looks like.
```

### 643. D5_s981068_en (domain=D5, difficulty=7)

```
Build a fresh Python 3.12 log-triage tool from scratch: `logtriage.py` plus `README.md`. It should parse mixed JSON/text app logs, detect error spikes, cluster repeated stack traces, and generate a concise incident summary with likely root-cause clues and example queries for follow-up. Use current best practices from the web for log parsing and anomaly detection, then implement it cleanly with tests and a CLI.
```

### 644. D5_s981071_en (domain=D5, difficulty=7)

```
I need you to build a small incident-log triage tool from scratch that parses plain-text service logs, detects likely root-cause patterns, and spits out a ranked debugging summary with suggested next checks. Please make it a real code deliverable with a CLI, a core analysis module, tests, and a short README explaining how to use it; there are no input files, so just implement the tool and include a few representative sample log strings inside the tests or examples. Please research a couple of good Python parsing/logging libraries and CLI patterns first so the design is solid, then build the project cleanly and keep it easy to extend.
```

### 645. D5_s981108_zh (domain=D5, difficulty=7)

```
我需要你从零做一个可直接运行的日志故障诊断小工具，目标是给 SRE/后端排查用：支持把多种常见服务日志（像 Nginx、Python/Java 应用、Docker 容器日志）的文本贴进去后，自动识别错误模式、按时间线聚合、输出可读的根因线索和排障建议；最好顺手带一个命令行入口、一个简单的本地 Web 页面，以及一套单元测试和使用说明，代码和文档都一起给我。
```

### 646. D5_s981133_zh (domain=D5, difficulty=7)

```
我需要你从零搭一个用于排查后端日志的命令行工具，最好先做一个小型但可扩展的 MVP：能读取本地文本日志，按时间范围、级别、请求 ID 和关键词过滤，自动把重复错误聚合出来，还能输出一份简洁的故障摘要报告。你把代码、README 和测试都一起做出来，顺手查一下 Python 里适合做日志解析、命令行参数和表格输出的主流库，选型别拍脑袋，最后把实现写得能直接跑。不要用现成项目骨架，直接从零开始。
```

### 647. D5_s981137_zh (domain=D5, difficulty=7)

```
帮我从零做一个面向运维/后端团队的日志排障小工具，目标是把分散的应用日志快速变成可读的故障线索。
- 需要做成一个可直接运行的命令行工具，支持读取标准输入或本地文本日志，按时间范围、级别、请求ID/traceID 过滤。
- 需要做日志解析、事件聚合和简单的异常模式识别，比如同类错误合并、重复报错折叠、按根因候选分组。
- 希望输出两种结果：终端摘要和一份结构化报告（JSON 或 Markdown 都可以），方便接到 CI 或排障流程里。
- 请同时补上单元测试和一份简短 README，说明支持的日志格式、典型用法、已知限制。
- 先做一个可用的最小版本，但设计上要留出后续扩展到多格式日志和更多规则的空间。
```

### 648. D5_s981147_en (domain=D5, difficulty=7)

```
We need a small internal log-triage tool because our engineers are wasting time reading noisy Kubernetes and application logs by hand when incidents happen. Build a from-scratch command-line utility that can read plain text logs pasted into stdin or passed as a file path, detect likely error patterns, group related lines into incidents, and produce a short human-readable summary of what happened and what to check next. I want it to feel practical for a support team: include a clear CLI, sensible defaults, and output that is easy to scan during an outage. Please research current best practices for Python CLI tools, structured logging, and log parsing libraries before you build it, then implement the tool, tests, and a short README explaining how to use it.
```

### 649. D5_s981172_en (domain=D5, difficulty=7)

```
I want a small but real log-analysis tool built from scratch for our incident-response workflow.

- Build a Python CLI that ingests live/service logs from stdin or a file path and flags likely root-cause patterns like error bursts, retries, timeouts, and cascading failures.
- Include a simple rule engine with configurable thresholds and a few built-in detectors, plus a clean JSON output mode for piping into other tools.
- Add a test suite that covers the parsing logic, detector behavior, and CLI edge cases, with enough cases to catch regressions.
- Research a couple of current Python logging/CLI best practices and any standard libraries or lightweight packages that would make sense here, then base the implementation on that research.
- Deliver the code and a short README with usage examples, install steps, and a brief note on how to extend the detectors.
```

### 650. D5_s981173_en (domain=D5, difficulty=7)

```
I need a small debugging utility built from scratch for our engineering team to help us triage flaky services faster.
- Build a CLI tool that tails logs, detects repeating error patterns, and groups related events into incident summaries.
- Make it configurable for common log formats like JSON logs and plain text with timestamps, and include sensible defaults.
- Add a compact report/export mode so we can dump a summary to markdown or JSON for sharing in tickets.
- Include automated tests for parsing, pattern grouping, and a couple of end-to-end CLI flows.
- Keep the code self-contained and production-minded, with a README that explains usage and edge cases.
```

### 651. D5_s981201_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for Kubernetes incidents: a small CLI that ingests pasted logs from stdin, classifies likely root causes, and outputs a concise incident summary plus suggested next checks. Use FastAPI for an optional local HTTP endpoint if that helps, and include a README plus tests.
```

### 652. D5_s981230_zh (domain=D5, difficulty=7)

```
我们现在要把值班排障效率提上来，减少工程师在深夜翻日志、看告警和手工定位问题的时间。请你从零做一个小工具，帮我们把服务日志和告警信息整理成可读的故障时间线，并自动给出可能的根因线索。

我希望你直接交付可运行的代码和简单说明，不要只写思路。这个工具最好能本地跑，不依赖外部服务，输入就是我们手动复制进去的一段日志文本和几条告警文本，输出要能看懂：按时间排序、自动分组同一条问题、标出错误峰值、提取关键异常、并生成一份简短的排障摘要。

你帮我调研一下现成的做法和常见库，看看 Python 里做日志解析、时间线整理、文本聚类、命令行交互有哪些靠谱选择，然后从头实现一个轻量版本。最后请把代码、测试和使用说明一起给我，确保别人拿去就能在本机跑起来并验证效果。不要依赖任何现成输入文件，我会把日志直接贴到命令里或标准输入里。最好把功能拆开做，这样以后我们也方便继续加规则和接入别的日志格式。
```

### 653. D5_s981237_en (domain=D5, difficulty=7)

```
Build a small Python log-triage tool from scratch for Kubernetes services: parse JSON and plain-text logs, detect error spikes, group repeated stack traces, and emit a compact incident summary. I want `logtriage.py`, `tests/`, and a short `README.md`; use current best practices and libraries you verify online before coding.
```

### 654. D5_s981245_en (domain=D5, difficulty=7)

```
Build a small Python troubleshooting tool from scratch for SRE work that turns raw application logs into an incident-style summary.
- I want a command-line app that can read pasted log text or stdin, detect likely error clusters, and produce a concise timeline plus top suspects.
- Please research current best-practice Python libraries for parsing timestamps, colorized CLI output, and lightweight anomaly grouping before you code.
- Include a core library, a CLI interface, and a few realistic sample log scenarios embedded in tests so I can verify behavior end to end.
- The output should be something I could use during an outage: grouped errors, repeated stack traces, spike detection, and a short human-readable summary.
- Deliver the built code and a README with usage examples and design notes.
```

### 655. D5_s981248_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called logtriage for parsing mixed JSON/text service logs, clustering repeated errors, and generating a root-cause summary report. I want the code in app.py plus a short README.md with install/run instructions and one example command; no input files, just code and docs.
```

### 656. D5_s981250_en (domain=D5, difficulty=7)

```
Build a from-scratch log triage tool for Kubernetes incidents: ship a small Python package with a CLI that ingests pasted logs from stdin, detects error bursts, groups them by likely root cause, and outputs a ranked incident summary plus suggested next checks. Include a README.md with usage and a sample workflow, and add tests for the parser, grouping logic, and CLI output.
```

### 657. D5_s981273_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for Postgres log debugging: `pglog_inspector.py` plus `README.md`. It should parse Postgres CSV/text logs, cluster repeated errors, summarize slow queries and auth failures, and emit a terminal report and JSON output. Use current Postgres logging docs and one or two mature Python log parsing/CLI library references to shape the design, then implement it cleanly from scratch with tests.
```

### 658. D5_s981295_en (domain=D5, difficulty=7)

```
Build a small but production-grade Python troubleshooting tool from scratch that ingests live application logs from stdin, detects repeated exception patterns and log-volume anomalies, and emits a concise incident triage report plus a machine-readable JSON summary. I want this designed around current best practices for Python logging, regex parsing, and lightweight anomaly detection, so please research the standard library docs and a couple of widely used logging/CLI patterns before implementing. Deliver the finished codebase, not a prototype: include the core library, a CLI entrypoint, unit tests, and a README with usage examples. The tool should support at least JSON and plain-text logs, allow configurable window size and severity thresholds, and surface likely root causes by grouping repeated stack traces and adjacent error bursts.
```

### 659. D5_s981313_en (domain=D5, difficulty=7)

```
I need you to build a small from-scratch log investigation tool for a production support workflow: implement a Python CLI that can ingest raw application logs from stdin or a pasted string, detect suspicious error bursts, correlate repeated stack traces, and generate a concise incident summary with recommendations. Please make it work with common JSON and plain-text logs, include a few realistic sample log lines in the README, and add tests plus a short design note explaining how you chose the parsing and grouping logic. Use current best-practice guidance from the web for Python logging, regex stack-trace handling, and CLI ergonomics, then build the code and docs from scratch.
```

### 660. D5_s981327_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering team cut through messy logs faster when customers report issues in our API. I want you to build it from scratch so we can paste in a log snippet, automatically detect likely error patterns, and get a plain-English summary with suggested next checks. It should be practical enough for real use, not a toy: handle mixed log formats, group repeated errors, pull out timestamps and request IDs when present, and make it easy to run locally from the command line. Please design and build the code, plus a short README that explains how to use it and what it can and cannot do. If helpful, research a couple of well-supported libraries or best practices first so the structure is sensible.
```

### 661. D5_s981331_en (domain=D5, difficulty=7)

```
Build a from-scratch incident log triage tool in Python for our on-call workflow. The tool should ingest plain-text application logs from stdin or a pasted string, detect likely error spikes and recurring exception signatures, and emit a concise incident summary with top suspects, timeline clustering, and suggested next checks. I want a small but production-minded codebase with a CLI, a library module, and tests. Use web research to confirm current best practices for Python CLI UX, regex/log parsing approaches, and any lightweight libraries worth adopting for colored terminal output or structured summaries, then implement the tool without relying on any starter data or sample files. Deliver the code and a README that documents usage, design choices, and limitations.
```

### 662. D5_s981335_en (domain=D5, difficulty=7)

```
I need you to build a small from-scratch log triage tool for incidents: it should ingest plain text app/server logs, detect common failure patterns, group related lines into incidents, and generate a short root-cause-style summary plus a confidence score. Please use current docs or best practices for Python regex/log parsing, structured logging, and CLI design where helpful, then give me the finished code and README in a couple of files.
```

### 663. D5_s981341_en (domain=D5, difficulty=7)

```
I want a from-scratch tool for debugging production logs and finding likely root causes faster.

- Build a small Python command-line app that ingests raw text logs, groups repeated error patterns, and surfaces suspicious spikes or new exceptions.
- Research a couple of current options for parsing and fuzzy grouping in Python first, then choose a sensible approach and implement it cleanly.
- Include a minimal report format for humans, plus a JSON output mode that could feed a dashboard later.
- Add unit tests around the log parsing, clustering/grouping, and anomaly detection behavior.
- Make the code easy to extend, with a short README explaining how to run it and how the detection logic works.
```

### 664. D5_s981353_en (domain=D5, difficulty=7)

```
Build a from-scratch incident-log triage tool for Kubernetes workloads that helps SREs turn noisy pod logs into a clear debug report.

- I want a small Python CLI that tails or ingests raw logs, detects likely error patterns, groups duplicates, and highlights probable root causes.
- Research current best practices and relevant libraries for log parsing, regex-based extraction, clustering/similarity, and terminal-friendly output before implementing.
- Include a test plan and automated tests that cover parsing, deduplication, ranking, and failure cases.
- Add a short README that explains how to run it, what the heuristics do, and how to extend the rule set.
- Keep it self-contained, with no input data files required; the tool should work on logs pasted in or piped from stdin.
```

### 665. D5_s981368_zh (domain=D5, difficulty=7)

```
帮我从零做一个 Python 的日志告警工具，文件直接给我 `main.py`、`alert_rules.py`、`tests/` 和 `README.md`。要支持读取应用 stdout 日志，按规则检测错误爆发、超时、重复报错和请求失败率，并输出带时间窗口的告警摘要；命令行要能本地跑，顺手把边界条件和示例用法都补上。
```

### 666. D5_s981372_zh (domain=D5, difficulty=7)

```
我需要你从零做一个小工具，帮我们排查微服务日志里的请求链路和错误根因：做一个可运行的命令行程序，能读取一段结构化日志文本，按 trace_id/请求 ID 还原一次请求的完整路径，标出异常、超时和重试，并输出一份清晰的诊断报告；另外把核心解析逻辑、CLI 入口、测试、以及使用说明都一起补齐，最好再顺手对照一下当前常见日志格式、Python 标准库和常用命令行参数写法，避免接口设计过时。
```

### 667. D5_s981392_zh (domain=D5, difficulty=7)

```
帮我从零做一个 Python 调试工具，做成可直接跑的 CLI：给一段服务日志，自动解析请求链路、聚合错误模式、按时间窗口输出告警摘要，并生成一份 Markdown 排障报告。代码里要有清晰的模块划分、单元测试和 README，别用现成模板直接拼。
```

### 668. D5_s981393_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called logtriage for debugging service incidents from raw application logs. I need a core parser, anomaly detection for error bursts and latency spikes, a CLI that can ingest pasted logs from stdin, and a small test suite plus README.md with usage examples. Use web research for current best practices around Python log parsing, argparse/typer-style CLI design, and testing patterns before implementing.
```

### 669. D5_s981422_zh (domain=D5, difficulty=7)

```
我们最近在排查线上问题时，日志很多、告警也很多，但真正能快速看懂“哪个请求先坏、哪里开始变慢、是不是同一类错误重复出现”的工具还没有。我要你从零做一个可用的小工具，用来把应用日志里的请求链路和错误线索整理出来，帮助值班同事更快定位问题。

我希望你先查一查目前常见的日志结构化做法、Python 里适合做这类解析和汇总的库、以及命令行工具怎么设计更顺手，然后直接实现出来。这个工具不要依赖现成输入文件作为题目材料；你自己在代码里把解析规则、汇总逻辑、测试和示例都搭起来。

最后请交付可运行的代码和简短说明文档，最好还能顺手加上几组单元测试。工具至少要能：读取文本日志、识别时间、级别、请求ID或类似链路标识、错误类型，输出按请求和错误分类的汇总，并能把最常见的问题单独列出来，方便做排障总结。
```

### 670. D5_s981423_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support team make sense of messy service logs and quickly spot the likely root cause when customers report an outage. Build it from scratch so a non-technical person can paste in raw log text, choose a few simple options, and get a clear summary of errors, repeated patterns, likely incident windows, and a short action list. I want the finished code and a short README so our team can run it locally, and I want you to use current web research to pick a sensible stack and logging/test approach before you build it.
```

### 671. D5_s981437_en (domain=D5, difficulty=7)

```
I need a small but realistic observability tool built from scratch for a Node.js service that helps with debugging flaky failures in production logs.

- Build a CLI that tails JSON logs, groups repeated errors, and surfaces the top exception signatures with context lines.
- Add a parser/resolver for common Node stack traces so file/line links are clickable in terminal output.
- Include a config format and a few sensible defaults for filtering noise like health checks and retry storms.
- Write tests for the parser, grouping logic, and CLI behavior, plus a short README with usage examples.
- Use current best practices and existing library conventions where useful, but implement the actual tool yourself.

```

### 672. D5_s981456_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上日志的命令行工具，目标是把一堆服务日志里的报错自动归类、提取关键上下文，并生成一份可读的故障摘要。请直接给我实现代码和 README，最好还能带上测试；技术选型你可以自己定，但要先查一下 Python 里常用的日志解析、结构化输出和 CLI 设计做法，再开始写。最后希望这个工具能支持按时间范围、错误级别、关键字过滤，并输出 JSON 和 Markdown 两种报告。
```

### 673. D5_s981458_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps us figure out why our weekly job runs are failing before they become a bigger issue. I want a from-scratch log triage utility that can read plain text application logs, spot common failure patterns, group related errors together, and produce a short incident summary with likely causes and next steps. Please build the code and the basic usage notes for it, not a mockup. I’m especially interested in something that can be run from the command line, because our ops team would want to point it at a pasted log file or a log export and get a clear report quickly. Please do the research you need on good Python libraries and current best practices for log parsing, pattern matching, and test setup, then implement it cleanly with tests and a simple way to extend the failure rules later.
```

### 674. D5_s981471_zh (domain=D5, difficulty=7)

```
我们现在要把线上服务的故障排查做得更快一些，减少工程师在日志里手工翻找的时间，所以我想做一个从零开始的小工具，帮我们把一段应用日志自动整理成可读的故障分析结果。你直接帮我设计并实现这个工具：它要能读取文本日志，识别常见的错误、告警、请求链路和时间线，输出一份结构化摘要，还要能给出可能的根因线索和下一步排查建议。工具最好有命令行入口，方便我和同事本地直接跑；也请把测试一起做好，保证后面接到我们自己的日志格式时不会轻易坏掉。实现时请你先参考一下现成的日志解析、命令行参数处理和测试组织方式，再从头写代码，不要依赖现成样例数据。最后把代码和使用说明一起交付给我。
```

### 675. D5_s981473_zh (domain=D5, difficulty=7)

```
帮我从零实现一个面向工程排障的日志告警小工具，目标是给一组服务日志做实时规则检测并输出可读的诊断报告。
- 需要先调研一下当前常见的日志处理方案和最佳实践，比如 Python 里适合做流式解析、正则匹配和命令行分发的库，以及日志结构化输出的推荐方式。
- 核心功能要支持自定义规则：按关键字、正则、时间窗口、重复次数阈值来触发告警，并能把同一类问题聚合成事件。
- 希望你直接交付可运行的代码和测试，不要依赖任何现成输入文件；你自己在代码里构造示例日志和测试样例。
- 还要有一个简洁 CLI，可以指定规则配置、输入来源和输出格式，最好再加一个 JSON 报告模式，便于后续接到别的系统里。
- 最后写一份 README，说明设计思路、运行方式、规则示例和已知边界条件。
```

### 676. D5_s981481_en (domain=D5, difficulty=7)

```
I need you to build a small log-diagnostics tool from scratch for our SRE workflow: a Python package plus CLI that can ingest JSON and plain-text application logs, detect common failure patterns, cluster related errors by stack trace signature, and emit a concise incident summary with suggested next checks. Make it realistic enough to use on real service logs, include tests, and add a short README showing how to run it and what the output looks like. Please research current best practices for Python logging parsing, CLI design, and any useful libraries or patterns before implementing it.
```

### 677. D5_s981483_en (domain=D5, difficulty=7)

```
Our support team keeps losing time when customer issues come in with vague app logs, and I want a small internal tool that helps us spot the most likely root cause faster. Please build a from-scratch log troubleshooting utility for our engineering team that can take pasted logs from common web app services, detect error patterns, group related lines, and produce a clear incident summary with likely causes and suggested next checks. It should be something we can run locally from the command line, and I want the code plus a short README that explains how to use it and how the pattern logic works. Please research current best practices for Python log parsing and command-line tooling so the design is sensible, then implement it cleanly with tests.
```

### 678. D5_s981489_en (domain=D5, difficulty=7)

```
Build a from-scratch Go tool called logtriage that parses app logs from stdin, detects common failure patterns, and prints a ranked incident summary plus suggested next checks. I want app.go, parser.go, detector.go, and README.md, and it needs to support JSONL and plain text logs, configurable regex rules, and a --watch mode for tail-like streaming.
```

### 679. D5_s981490_zh (domain=D5, difficulty=7)

```
给我从零做一个 Go 版的 Kubernetes 容器日志故障排查小工具，先查资料再实现。我要一个命令行程序和 README：支持按 pod/container 名称筛选、按时间窗口过滤、识别常见错误模式（OOMKilled、CrashLoopBackOff、panic、connection refused），输出一份可读的诊断摘要。再补上单元测试和一个最小的示例用法。
```

### 680. D5_s981503_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上故障的日志分析小工具，目标是把应用日志里的错误、慢请求和关键告警自动归类成一份可读的排障报告。你直接给我实现代码和 README 就行，最好是一个可运行的 CLI，支持解析文本日志、输出摘要、按时间线聚合相关事件，还能导出 JSON 和 Markdown 报告；实现前先查一下现成的 Python 日志解析、终端表格输出和时间戳处理的最佳实践，别照搬模板，要自己设计出一套合理的数据结构和规则。
```

### 681. D5_s981507_zh (domain=D5, difficulty=7)

```
我们现在需要尽快做一个内部排障工具的原型，帮助客服和工程师在一堆日志里快速定位“为什么这次请求失败了”。我希望你从零开始做一个可运行的小工具，不用任何现成输入文件，自己先设计数据结构和演示样例，再把功能做出来。这个工具最好能把日志按请求 ID 串起来，识别常见错误模式，给出一段简短的排查结论，还能生成一个简单的测试方案，方便我们后面接进真实系统。请你先查一下现在比较常用的 Python 日志处理和命令行工具写法，再决定最合适的实现方式，然后直接把代码、说明和测试都做出来。我们更看重可用性和清晰的排障结果，不需要很花哨，但要真的能跑。
```

### 682. D5_s981518_en (domain=D5, difficulty=7)

```
Our support team keeps losing time when a deployment goes bad because the logs are too noisy and the same error shows up in slightly different ways. I want a small internal tool built from scratch that can take raw application logs pasted in by an engineer, group the repeated failures into clear incident clusters, and produce a plain-English summary with the most likely root-cause patterns, first-seen timestamps, and example log lines. Please build the code and include a simple command-line way to run it, plus tests and a short README so someone else can use it without guessing. Use current best practices for log parsing and text clustering, and check the web for any practical Python libraries or techniques that would make this reliable and easy to maintain.
```

### 683. D5_s981524_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called logtriage with a CLI in src/logtriage/ and README.md. It should parse mixed JSON/text application logs, detect probable root-cause patterns, and output a concise incident summary plus a machine-readable report. Research current best practices for Python CLI design, structured logging, and log parsing libraries before you code.
```

### 684. D5_s981534_en (domain=D5, difficulty=7)

```
I want you to build a small but production-style log triage tool from scratch for investigating flaky CI failures in GitHub Actions. I do not want a notebook or a one-off analysis; I want actual code I can run locally against logs that I paste in or stream into the tool. Please implement a command-line utility that reads raw GitHub Actions job logs from standard input or from a pasted multiline string, parses the logs into structured events, detects likely failure signatures, and produces a concise triage report that highlights probable root causes, repeated patterns, and suspicious timing anomalies.

The tool should be designed around real GitHub Actions log conventions, so please research the current GitHub Actions logging commands, annotation format, grouping syntax, error markers, and any documented quirks in how logs are emitted. I expect you to look up current best practices and any stable patterns worth supporting, rather than guessing. In particular, I want the parser to recognize step boundaries, grouped sections, warning/error annotations, masked values, and common shell failure patterns from bash, PowerShell, and Node-based actions. If there are existing libraries that help with ANSI stripping, timestamp parsing, or command-line UX, please research them first and choose deliberately.

Functionally, I want the tool to accept raw log text and generate a structured summary with these sections: detected job/step names, all error and warning entries, a grouped list of repeated failure signatures, a timeline of notable events if timestamps are present, and a final “most likely cause” section that ranks causes by confidence. The ranking logic should be deterministic and explainable. I want it to rely on observable signals such as exact exception text, repeated retry messages, package install failures, test assertion failures, missing secret/permission messages, and abrupt termination patterns, not on any opaque ML. If the same signature appears multiple times, the report should collapse duplicates and show counts. If logs include GitHub Actions annotations like `::error file=...,line=...::message`, those should be parsed as first-class structured findings.

I also want a small test suite with realistic inline fixtures embedded directly in the tests, since there are no external input files. The tests should cover at least these cases: a clean successful job log, a log with one obvious failing step, a log with grouped output and annotations, and a log with mixed shell output where the parser must avoid false positives from benign lines that merely contain the word “error”. Please include at least one regression test for edge cases around multiline messages, ANSI color escape sequences, and duplicated failure lines. The tests should be deterministic and runnable without network access.

Please build the code in a clean, modular way. I expect separate concerns for parsing, normalization, signature detection, ranking/scoring, and report rendering. I also want a small CLI entry point that supports either reading from stdin or a literal string argument, plus an option to emit JSON instead of the human-readable report. Make the CLI usage clear and ensure invalid arguments fail gracefully. If you choose a language ecosystem like Python, Node, or Go, please justify that choice based on current library support and idiomatic CLI patterns, using web research to inform the decision.

Please produce the actual source files and a README that explains installation, examples, and the heuristics used for failure detection. The README should also document limitations clearly, such as what the tool cannot infer from logs alone and where manual review is still needed. I want the final implementation to feel like something a developer could reasonably use during incident response on CI failures, not just a toy parser.
```

### 685. D5_s981538_zh (domain=D5, difficulty=7)

```
给我从零做一个 Python 工具，专门解析服务日志里的请求链路并生成故障排查报告。要支持 JSONL/纯文本两种日志格式，输出一个可直接运行的 CLI（含 help、子命令、退出码）和一份 README.md，代码里顺手加上单元测试。顺便帮我查一下 Python 里做日志解析、命令行参数和颜色输出的最佳实践，选一个稳妥的方案实现。
```

### 686. D5_s981562_zh (domain=D5, difficulty=7)

```
给我从零做一个 Python 诊断工具，专门解析 Kubernetes / Docker / Nginx 的日志，自动归类常见报错并给出排查建议。把代码放在 `app.py`、`diagnostics.py`、`cli.py`、`tests/` 和 `README.md`，顺手补一个 `docs/architecture.md` 说明设计。功能要包含：日志输入、规则匹配、摘要统计、置信度、以及可扩展的插件接口。
```

### 687. D5_s981600_en (domain=D5, difficulty=7)

```
I need you to build a small Python troubleshooting tool from scratch that tails application logs, detects a few common failure patterns, and turns them into a readable incident summary with suggested next checks. Please make it a real little code project with the core parser/alerting logic, a CLI, tests, and a short README, and use web research where needed to check current best practices for Python log parsing, argparse/typer-style CLI design, and how similar tools format structured diagnostics.
```

### 688. D5_s981624_en (domain=D5, difficulty=7)

```
I need you to build a small log-debugging tool from scratch for our Python services: a local CLI that tails JSON logs, detects a few common failure patterns, and prints a concise incident summary with likely root-cause hints and a suggested test plan. Please use current best practices from the web for Python logging, JSON line parsing, and CLI UX, then deliver the code, tests, and a short README showing how to run it and what kinds of logs it can inspect. 
```

### 689. D5_s981626_zh (domain=D5, difficulty=7)

```
我们现在要把线上故障排查做得更快一些，减少值班同事来回翻日志、手工拼时间线的时间。请从零设计并实现一个可在本地运行的日志排障小工具：它能接收多种常见服务日志文本，自动识别时间戳、级别、请求 ID、异常堆栈，把同一次请求的相关日志串起来，输出一份可读的故障时间线和简短结论；同时再给一个命令行入口，方便工程同学直接用。你需要自己决定合适的技术方案、数据结构和交互方式，但要把代码、基础说明和测试一起做好，最好能直接跑起来。实现前请查一些当前常见日志解析和命令行工具的做法，避免我这边拍脑袋定方案。最后请交付完整代码和使用说明，不要依赖任何我提供的输入文件。
```

### 690. D5_s981627_en (domain=D5, difficulty=7)

```
I need a small internal log-checking tool for our ops team because we keep losing time triaging the same kinds of failures across services. Build it from scratch so it can scan plain text logs, flag likely incidents, group repeated errors, and produce a clean summary we can hand to engineers after an outage. Please research the best current Python libraries and practices for log parsing, pattern matching, and terminal reporting before you build it, then implement the tool and include clear instructions for running it. I want the finished code files, not a report.
```

### 691. D5_s981647_zh (domain=D5, difficulty=7)

```
我需要你从零做一个面向工程排障的日志分析小工具，目标是把一组服务日志里常见的报错模式自动归类、给出时间线和可执行的排查建议，最好做成一个命令行程序，另外把设计思路、使用方法和测试说明也写清楚。你可以先查一下现在常用的 Python 日志解析、正则/结构化日志处理和 CLI 设计最佳实践，再开始实现代码和文档；我这边不提供任何输入文件，你要自己把功能、接口和示例都搭出来。最后把可运行的代码、测试和 README 一起给我。
```

### 692. D5_s981671_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上故障的日志分析小工具，目标是把一组应用日志里的错误、慢请求和异常堆栈自动归类，输出一份可读的诊断报告，并带一个命令行入口和一套可跑的测试。你先查一下 Python 里适合做日志解析、时间窗口聚合和终端报告输出的现成最佳实践/库，然后直接把代码、测试和 README 一起写出来，文件尽量清楚些，比如核心模块、CLI、测试和说明文档都分开。
```

### 693. D5_s981711_zh (domain=D5, difficulty=7)

```
我们的工程团队最近在排查线上告警和发布后回归问题，日志分散在不同服务里，人工翻看太慢，导致定位根因和复盘都拖时间。我想从零做一个轻量的日志排障工具，先能把一组文本日志里的错误、重复告警、时间线和疑似根因自动整理出来，方便支持工程师快速看。请你直接帮我把这个工具做出来，代码、测试和使用说明都一起给我，不要依赖任何现成的输入文件；你自己设计一个合理的示例日志和测试方案。实现前请先查一下现在常见的 Python 日志解析、命令行参数和输出格式的最佳实践，再决定用什么库和结构。最后给我能直接运行的代码文件、测试文件和 README，要求以后我可以继续扩展到更多服务日志。
```

### 694. D5_s981716_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for debugging Kubernetes pod logs that can detect crash-loop patterns, correlate them with recent deploys, and generate a concise incident summary. I want app.py, tests/, and README.md; include a CLI, structured log parsing, a simple rule engine, and a JSON report output.
```

### 695. D5_s981727_en (domain=D5, difficulty=7)

```
Build a from-scratch Rust tool that tails container logs and emits structured incident signals for our on-call workflow. I want a small but production-minded CLI that can ingest stdout/stderr text streams, detect a configurable set of failure patterns, correlate repeated stack traces, suppress noisy duplicates with a sliding window, and output JSON events plus a human-readable summary. Use web research before coding to validate current best practices and library choices for log streaming, regex matching, CLI ergonomics, and JSON serialization in Rust, and check any relevant crate docs/issues for tradeoffs. Deliver the finished codebase with tests and a README that explains usage, configuration, and the detection model. No input files are provided; implement the functionality from scratch.
```

### 696. D5_s981734_en (domain=D5, difficulty=7)

```
We need a small internal troubleshooting tool for our support team because our engineers keep losing time digging through messy app logs when customers report broken checkouts. Please build it from scratch as a real working utility, not a mockup, so it can take raw log lines pasted in by a person and quickly flag likely failure points, group related events, and produce a short incident summary that a support agent can hand to engineering. I want the code and a short README that explains how to run it locally, what it does, and how to verify it with tests. Please use current best practices and look up any useful libraries or patterns you need before building it.
```

### 697. D5_s981737_zh (domain=D5, difficulty=7)

```
我想从零做一个面向 SRE/后端团队的日志排障小工具，目标是把分散的服务日志快速整理成可读的故障时间线。
- 先帮我调研几类常见日志格式和现成 Python 库的取舍，优先看看结构化日志、正则解析、时间线聚合这几块的最佳实践
- 然后直接实现一个命令行工具：输入多段原始日志字符串或从 stdin 读入，输出按时间排序的事件摘要、可疑错误聚类和简单的根因线索
- 希望支持至少 2-3 种常见格式的自动识别，包含时间戳、级别、服务名、trace/request id 的提取
- 需要补上比较完整的单元测试和一份简短的 README，说明怎么安装、怎么跑、支持哪些日志样例
- 如果你觉得合适，也可以顺手加一个小的 JSON 导出模式，方便后续接入别的工具
```

### 698. D5_s981740_en (domain=D5, difficulty=7)

```
Build a small Python incident-debugging tool from scratch: `logtriage.py` plus `README.md`. It should ingest mixed application logs from stdin or a file, cluster likely related errors, extract correlation IDs/request IDs, and generate a concise incident timeline with probable root-cause hints. Use current best practices from the web for Python log parsing, ANSI-safe CLI output, and traceback handling, then implement it cleanly with tests.
```

### 699. D5_s981749_en (domain=D5, difficulty=7)

```
I need a small but real developer tool built from scratch for investigating flaky services and noisy logs in CI.
- Build a Python command-line utility that ingests plain text logs and flags likely failure signatures, retry storms, and timeout cascades.
- Include a couple of useful analysis modes like grouping repeated exceptions, summarizing error bursts by time window, and highlighting probable root-cause lines.
- Add a clean CLI, readable output, and a test suite that covers edge cases and a few realistic log patterns.
- Research the best lightweight Python libraries and any current recommendations for CLI parsing, colored output, and regex/log processing before you implement it.
```

### 700. D5_s981765_en (domain=D5, difficulty=7)

```
Build a from-scratch Python CLI called logtriage for debugging and log analysis of Python services. I want src/logtriage.py, tests/, and README.md with install/run examples; include an interactive mode, regex-based filters, severity extraction, and a JSON/Markdown report export. Do a quick web pass first on Python logging best practices and a couple of similar CLI tool patterns, then implement it cleanly with tests.
```

### 701. D5_s981769_en (domain=D5, difficulty=7)

```
I need you to build a small but real Python debugging tool from scratch: a CLI that watches a local app log stream, detects common failure patterns like stack traces, retry storms, timeout bursts, and repeated 5xx errors, then groups them into incidents and prints a concise triage summary with probable root-cause hints. Please research current best practices and a couple of solid libraries/APIs for log parsing and terminal output before coding, then give me the finished code, tests, and a short README explaining how to run it and how the detection rules work.
```

### 702. D5_s981781_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-triage tool from scratch that watches a stream of app logs, flags likely incident patterns, and spits out a short debugging summary plus a test plan I can hand to the team. Make it practical for Kubernetes-style JSON logs and plain text logs, add a CLI, a library module, and solid tests, and use current docs for a couple of real log/regex/python packages so the design matches what people actually use today.
```

### 703. D5_s981797_zh (domain=D5, difficulty=7)

```
我想从零实现一个面向工程排障的日志分析小工具，目标是能把多服务日志里的同一条请求串起来，快速定位异常链路。
- 先调研一下当前主流做法，重点看看 OpenTelemetry trace/span 语义、JSON 日志结构化字段、以及 Python 里做流式日志处理比较稳妥的库或实现方式。
- 帮我直接设计并实现一个命令行工具，能读取我手动喂给它的日志文本，识别 request_id / trace_id / span_id 之类字段，把跨服务调用按时间线整理出来。
- 需要支持基础的告警规则：比如按错误级别、超时关键字、重复重试次数来标记可疑链路，并输出一份可读的排障摘要。
- 最终给我完整代码、必要的测试、以及一份简短 README，说明怎么运行、怎么扩展规则、以及它适合哪些排障场景。
```

### 704. D5_s981798_en (domain=D5, difficulty=7)

```
I need you to build a small incident-log triage tool from scratch for our SRE team: make a Python CLI that ingests plain text or JSON logs from stdin, detects error bursts, groups repeated stack traces, and outputs a compact incident summary with likely root-cause hints and a severity score. I also want a simple README and a solid test suite, and please research a couple of current Python libraries and logging best practices first so the design isn’t guesswork.
```

### 705. D5_s981802_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering teams quickly make sense of service outages and weird production logs without waiting for someone to manually stitch together clues. I want you to build it from scratch as a working command-line utility for our team to use locally: it should ingest pasted log text, identify likely error patterns, group related lines into incidents, and generate a short plain-English summary with timestamps and possible root causes. Please research current best practices and a couple of suitable open-source Python libraries for parsing logs and terminal output first, then implement the tool, add tests, and include clear usage notes so our team can run it and trust the results. No input files are being provided; design the whole thing yourself and deliver the code.
```

### 706. D5_s981807_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for Kubernetes incident debugging. I want `incident_triage.py` plus `README.md`: it should ingest raw pod/container logs from stdin or pasted text, detect common failure patterns, and output a ranked incident summary with suspected root cause, correlated timestamps, and suggested next checks. Use current best practices from the web for regex/log parsing, timestamp handling, and CLI UX.
```

### 707. D5_s981813_zh (domain=D5, difficulty=7)

```
我们现在要把客服和运维排障这件事做得更快一些，因为最近线上出问题时，大家常常要在一堆日志里手工找线索，来回切换工具也很慢。我希望你从零做一个“日志排障助手”小工具，最好能直接在本地跑，用来分析应用日志、自动提取常见错误模式、按时间线整理关键事件，并给出一个简单的排查建议。

你先自己查一下现成做法和常用库，看看大家通常怎么做日志解析、模式匹配、时间线归并、以及命令行工具的交互设计；但最后实现要你自己从头写，不要直接套现成项目。这个工具不需要接任何输入文件，直接把代码和必要的说明文档给我就行。

我希望它至少支持：读取一段日志文本、识别不同级别的日志行、把同一次故障相关的片段聚类到一起、输出可读的摘要、并提供一个简单的测试计划，说明怎样验证它在常见异常日志上的表现。尽量做得像一个真正能交给团队使用的内部工具，而不是演示样例。若你觉得有必要，可以顺带做一个命令行接口，方便大家把日志复制进去就能分析。
```

### 708. D5_s981815_zh (domain=D5, difficulty=7)

```
我想从零做一个用于排查服务异常的命令行工具，目标是把多份应用日志快速聚合成一份可读的故障分析报告。

- 先帮我调研一下适合 Python 的日志解析、颜色输出和表格展示方案，优先选维护活跃、文档清晰的库；如果有更适合做 CLI 的设计最佳实践也一起参考。
- 需要你直接实现一个可运行的 CLI 工具，支持读取多行文本日志、按时间窗口和级别过滤、聚合相同错误模式，并输出摘要、Top 错误、以及带上下文的片段。
- 再补上单元测试和集成测试，覆盖常见日志格式、空输入、异常字段、以及命令参数错误等情况。
- 最后写一份简短的使用说明，告诉我怎么安装、怎么跑、以及这个工具适合排查什么类型的问题。
- 我不需要你分析我现有文件；请直接从零设计并交付代码和说明。
```

### 709. D5_s981820_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for Kubernetes-style JSON logs. I want `logtriage.py`, `tests/`, and a short `README.md`; make it detect error clusters, summarize likely root causes, and flag suspicious retries/timeouts from mixed stdout logs. Use current best practices for Python logging/JSON parsing and CLI design, and pull any needed research from the web before you code.
```

### 710. D5_s981832_zh (domain=D5, difficulty=7)

```
帮我从零做一个 Python 工具，输出 `logtriage/` 代码和 `README.md`：它要能解析 Nginx / Python / Node 三类日志，自动提取异常模式、按时间线聚合、生成可读的排障摘要，并支持 `--format json|md` 和 `--top-n`。先查一下现成日志解析/文本聚类/异常检测的最佳实践和合适的开源库，再自己实现核心逻辑、CLI、测试和示例用法。
```

### 711. D5_s981834_zh (domain=D5, difficulty=7)

```
我需要你从零做一个 Python 的日志排障小工具，最好是一个可直接运行的命令行项目，能把应用日志里的错误自动归类、提取关键上下文、按时间线整理成一份排障报告，还要顺手加上几个常见格式的解析器（比如 Python logging、JSON logs、nginx 风格 access log）和一些基础测试。你先查一下现成库和最佳实践，确定我们该怎么设计解析、分组和输出格式，然后直接把代码、测试和 README 一起写出来；最后给我一份可用的项目文件清单，能在本地跑起来那种。
```

### 712. D5_s981838_en (domain=D5, difficulty=7)

```
We need a small internal tool to help our support and operations team make sense of messy application logs when something goes wrong. The goal is to let someone point it at a log file, get a clean incident summary, and quickly see the likely error patterns, the services involved, and a short timeline of what happened. I want you to build this from scratch as a real usable command-line utility, not a mockup. Please use current best practices for Python logging and CLI design, and research any standard libraries or lightweight packages that make sense before you implement it. I’d like the finished code files and a short README that explains how to run it, what it does, and how to test it.
```

### 713. D5_s981847_zh (domain=D5, difficulty=7)

```
我需要你从零做一个面向工程排障的日志分析小工具，目标是帮我们把一堆服务日志里的异常堆栈、告警和关联请求串起来，最后能输出一份可读的故障摘要和时间线。你直接交付代码和 README 就行，最好做成一个可本地运行的 Python 命令行工具，支持配置日志格式、关键字规则、时间窗口和输出 JSON/Markdown 报告；实现前先查一下 Python 标准库、常用日志解析/时间处理库、以及业界在日志聚合和错误归因上的做法，别用现成的整套平台，功能要自己写。
```

### 714. D5_s981852_en (domain=D5, difficulty=7)

```
I want a small but real log-triage tool I can actually use in our Python services.

- Build a from-scratch Python CLI that ingests app logs from stdin or a file and flags likely root causes for common failures like timeouts, retries, connection errors, and bad payloads.
- Add a lightweight rules engine with confidence scores, grouped incident summaries, and a clean human-readable report mode plus JSON output.
- Research current best practices for Python log parsing and CLI design so the implementation uses sensible libraries and patterns, not a toy approach.
- Include tests, sample usage in the README, and enough structure that I can extend the rules later without rewriting the core.
- I don’t have any input files for you; just build the tool and the supporting docs/tests from scratch.
```

### 715. D5_s981880_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool in `logtriage/` that ingests raw application logs from stdin or a pasted string and outputs a ranked incident summary with probable root-cause categories, duplicate-clustered errors, and suggested next debugging steps. I need `main.py`, `analyzer.py`, `cli.py`, `tests/`, and a short `README.md`; use current best-practice guidance from web docs for regex/log parsing, Python CLI design, and log-level classification. No input files — just ship the code and tests.
```

### 716. D5_s981887_en (domain=D5, difficulty=7)

```
I want a small but real internal debugging tool built from scratch for our Node.js services.
- Build a CLI that ingests application logs from stdin, detects likely root causes for crashes/timeouts, and outputs a concise incident summary.
- Research the best fit for parsing structured logs and command-line UX in the current Node ecosystem before you implement it.
- Include a few detector rules for common failure patterns like unhandled promise rejections, database connection exhaustion, and upstream 5xx cascades.
- Make the tool easy to extend with new detectors, and include solid tests and a short README with usage examples.
- Deliver the working code files plus the docs and tests; no input files will be provided.
```

### 717. D5_s981910_zh (domain=D5, difficulty=7)

```
我们现在要把线上故障排查做得更快一点。每次服务一出问题，值班同事都要手工翻很多日志，效率很低，也容易漏掉关键线索。我想从零做一个小工具，专门用来分析服务日志里的报错、按时间线把相关事件串起来，并且能快速给出一个可读的排查摘要，方便值班和研发直接看。

请你直接帮我设计并实现这个工具，最好做成一个可以本地运行的命令行程序，支持从标准输入或日志文本里读取内容，自动识别常见错误级别、请求 ID、时间戳和重复告警，输出一份结构清晰的分析结果。这个工具还要有一些基础测试，确保在常见日志格式下不会乱掉。

如果你需要参考现成做法，可以自己去查一下 Python 标准库里适合做日志解析、命令行参数和时间处理的最佳实践，再决定用什么方式实现。最后把代码和说明一起给我，方便我们内部直接试用和以后继续改。
```

### 718. D5_s981911_zh (domain=D5, difficulty=7)

```
帮我从零做一个“日志异常定位”小工具，面向 SRE/后端排障场景，用来把一批应用日志里的报错自动归类、提取关键上下文，并生成可读的排障摘要。

- 先做一个能直接运行的命令行工具，支持读取标准输入或本地日志文件，按时间窗口聚合同类异常。
- 希望你参考一下现在主流 Python 生态里做日志解析、CLI 参数、结构化输出和测试的最佳实践，再决定技术选型。
- 工具要能识别常见错误栈、重复报错、超时/连接失败/断言失败这几类模式，并输出一份简洁的诊断报告。
- 需要把核心逻辑、命令行入口、测试用例、以及使用说明都一起做出来，最后能让我直接跑起来验证。
- 如果你觉得合适，也可以顺手加一个 JSON 输出模式，方便后面接到别的自动化流程里。
```

### 719. D5_s981915_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called logtriage that analyzes mixed application logs and test-run output, clusters recurring failure signatures, and generates a debugging summary with likely root-cause candidates. I need app.py, tests, and a README that shows how to run it on pasted logs; also wire in a small CLI so I can point it at a log file or stdin and get a JSON report plus a human-readable summary.
```

### 720. D5_s981920_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-triage tool from scratch that helps debug flaky CI failures: it should parse mixed app/CI logs, group repeated errors, detect probable root-cause lines, and produce both a CLI report and a JSON summary. Please include the code files, a short README, and a solid test suite, and do a quick web-backed design pass first so you can choose a sensible parser and any lightweight libraries that fit current best practices.
```

### 721. D5_s981923_en (domain=D5, difficulty=7)

```
I want a small from-scratch incident-debugging tool I can actually use in a backend service workflow.
- Build a Python package that ingests raw application logs from stdin or a string and detects likely error clusters, request IDs, and timing anomalies.
- Include a CLI that can summarize a log stream, filter by severity, and emit a compact incident report in markdown or JSON.
- Use current best practices and a modern, lightweight parsing library if one is clearly better than rolling everything by hand, but keep the implementation self-contained.
- Add a solid test plan with unit tests for parsing, clustering, and CLI behavior, plus a few realistic sample log snippets embedded in the tests.
- Before coding, do a quick web-backed check of relevant Python log-parsing / CLI-library options and any recommended patterns for structured logging and human-readable incident summaries.
- Deliver the built code files and a short README with usage examples and design notes.
```

### 722. D5_s981938_en (domain=D5, difficulty=7)

```
Build a from-scratch internal observability tool in Python that ingests application logs from stdin or a file path, detects common failure patterns, and produces a structured triage report for debugging and incident review. The tool should implement log parsing for JSON and plain-text formats, severity bucketing, stack-trace grouping, regex-based signature extraction, and a CLI with subcommands for summarize, top-errors, and export. Use current best practices from the Python ecosystem for CLI design, structured logging, and packaging; research appropriate libraries and patterns with web sources before implementation. Deliver the built code, tests, and a concise README that explains installation, usage, and the debugging heuristics used. No input files are provided; create the implementation and tests from scratch.
```

### 723. D5_s981943_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上问题的日志分析小工具，目标是把 Nginx access log 和应用错误日志合并解析后，输出按时间线聚合的故障摘要、可疑请求链路和 Top 错误模式；你先基于 Web 查一下 Python 里适合做日志解析、命令行参数、时间处理和测试的主流库和最佳实践，然后直接把工具代码、测试和 README 一起写出来，要求命令行能接收日志文件路径、时间窗口和输出格式，支持 JSON/表格两种结果，并能对缺失字段、乱序时间戳和大文件做稳健处理。
```

### 724. D5_s981948_en (domain=D5, difficulty=7)

```
I want a small but realistic log-triage tool built from scratch for our on-call workflow.

- Build a CLI that can ingest plain-text app logs from stdin, detect common error patterns, and summarize likely root causes plus next-step checks.
- Use current best practices by researching a couple of well-known Python libraries for parsing/colorized output and one or two logging guidance sources before you implement it.
- Include a compact test suite that covers parsing edge cases, grouping, ranking of probable issues, and CLI behavior.
- Add a short README with usage examples, configuration options, and how the heuristics were chosen.
- Keep it dependency-light and practical for Linux/macOS terminals; no input files are provided, so everything should work with pasted log text or piped input.
```

### 725. D5_s981966_zh (domain=D5, difficulty=7)

```
我需要你从零做一个 Python 命令行工具，用来分析应用日志里的错误和告警，自动按时间线聚合相同异常、提取关键信息、给出可读的排查建议，并顺手生成一份 Markdown 报告和测试计划；代码要能直接跑，别依赖现成样例数据，自己设计一套合理的日志解析规则和输出格式，同时参考一下当前 Python 标准库、Click/Typer、Rich 这类库的最佳实践再决定实现方式，最后把代码、README 和测试都一起补齐。
```

### 726. D5_s981969_zh (domain=D5, difficulty=7)

```
我们最近在排查线上接口偶发超时和日志里大量重复报错的问题，管理层希望尽快有一个可以直接用的排障工具，帮助工程师把散落的服务日志、请求链路和错误信息串起来看清楚。请你从零做一个本地可运行的命令行工具，专门用于分析开发/测试环境里的日志文本，自动识别同一请求的关联片段、提取错误类型、统计高频异常，并输出一份适合排障的汇总结果。工具要尽量贴近真实工程使用，参数设计、输出格式和日志解析思路都请你自己定，但要方便工程师日常使用。

我不提供任何输入文件，你需要自己设计实现方案、代码结构和测试方式。请先做一些必要的线上资料调研，看看常见日志格式、CLI 设计习惯、Python 现成库或标准库能怎么配合使用，然后从头实现这个工具。最终请交付可运行的代码和说明文档，最好还能带上测试，确保别人拿到就能跑起来验证效果。
```

### 727. D5_s981972_en (domain=D5, difficulty=7)

```
I want a small but production-minded log analysis tool built from scratch for Python services.

- Build a CLI that can ingest structured application logs, group repeated errors by fingerprint, and summarize likely root causes from stack traces and message patterns.
- Include a dry-run mode, JSON output, and a human-readable terminal report so it’s useful in incident response.
- Use current best practices for Python packaging and CLI design, and research any relevant libraries or standard-library approaches before implementing.
- Add a solid test suite with fixtures you create yourself, plus a short README that explains how to run it and what the output means.
- I want the code files and docs, not a notebook or any input dataset.
```

### 728. D5_s981981_zh (domain=D5, difficulty=7)

```
我们最近在排查线上接口偶发超时和错误重试失控的问题，业务上已经开始影响订单处理和客服工单，所以我想从零做一个小工具，帮助工程团队以后能更快看懂日志、定位问题、并把排障步骤标准化。请你直接帮我实现一个可运行的命令行工具：它能读取我们自己贴进去的服务日志文本，自动识别错误类型、把同一次请求的关键日志串起来、找出最可能的异常模式，并生成一份适合给技术团队看的排障报告。最好还能支持导出成 Markdown 报告，方便发到群里和工单里。

我不提供任何现成文件，你需要自己把工具、解析逻辑、报告输出和测试一起从头做出来。请在实现前自己查一下现在常见的日志处理、异常分类和命令行工具写法，尽量用成熟、可靠的做法。最后把完整代码和使用说明一起给我。
```

### 729. D5_s981994_zh (domain=D5, difficulty=7)

```
给我从零做一个 Go 语言的日志故障排查小工具，文件就按你自己定，至少要有核心库、CLI、测试和 README。目标是：把多服务日志里的同一个请求链路串起来，支持按 trace_id / request_id 搜索、按时间窗口过滤、输出简版调用链和异常摘要。
```

### 730. D5_s981996_en (domain=D5, difficulty=7)

```
Build a fresh Python tool called logpulse that tails a service log stream, detects error spikes and repeated stack traces, and outputs a concise incident summary plus recommended next checks. I want app.py, tests/, and README.md; make it usable as a CLI with a config file and JSON output, and include a small synthetic demo mode so I can run it without any input files.
```

### 731. D5_s982005_en (domain=D5, difficulty=7)

```
Build a from-scratch Python 3.12 command-line tool called `logtriage` for debugging and incident response. It should ingest plain-text application logs from stdin or a file path, detect common failure signatures using rule-based parsing plus lightweight heuristics, and emit a ranked triage summary with probable root-cause categories, correlated timestamps, and recommended next investigative steps. I want a working codebase, not a report: package layout, CLI entrypoint, core parser/ranker, a small rules engine, and tests. Use current best practices for `argparse`/`rich`/`pyyaml` only if the research supports them; verify any external library APIs or patterns with web sources before implementing. Also include a concise README with usage examples and a troubleshooting section. No input files are provided; generate any fixtures/tests needed from scratch.
```

### 732. D5_s982022_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上问题的命令行工具，目标是给一组应用日志快速生成“异常时间线 + 可能根因提示 + 测试复现建议”的报告，最好直接产出可运行代码和 README。这个工具要支持读取本地文本日志、按时间/级别/请求 ID 聚合，识别错误爆发、超时链路和重试风暴，并把结果导出成 Markdown；实现前先查一下 Python 里适合做日志解析、命令行参数和时间序列聚合的现成库，以及常见的日志分析最佳实践，再开始写代码。请把核心分析引擎、CLI 接口、测试、文档和集成分别做完整。
```

### 733. D5_s982023_en (domain=D5, difficulty=7)

```
I need you to build a small log-triage tool from scratch that takes pasted app logs from stdin or a text box and turns them into a ranked incident summary with probable root-cause hints, timeline grouping, and next-step suggestions. Please research a few current parsing/reporting libraries and best practices first, then implement the code, tests, and a short README. I want the finished files, not a writeup of the process.
```

### 734. D5_s982026_en (domain=D5, difficulty=7)

```
I want a small but real log-debugging tool built from scratch for our engineering team.
- Build a Python CLI that can ingest application logs from stdin or a file, normalize timestamps, and detect common failure patterns like retries, timeouts, and cascading errors.
- Use current best practices from the web for Python logging, ANSI-safe terminal output, and at least one lightweight parsing library or standard-library approach that fits this use case.
- Include a concise report mode that summarizes likely root causes, repeated exceptions, and the top correlated log lines in a readable table.
- Add solid tests for parsing edge cases, malformed lines, time-zone handling, and the pattern-detection logic.
- Package it with a README that explains install, usage, and a few example commands.

```

### 735. D5_s982032_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for debugging flaky CI jobs from logs: write the core parser/analyzer, a CLI, and a small HTML report generator. Use web research to confirm best practices and current library choices for parsing timestamps, ANSI logs, and generating portable reports; then implement everything in app.py, cli.py, and report.py with tests and a README.
```

### 736. D5_s982033_zh (domain=D5, difficulty=7)

```
我需要你从零做一个给 SRE/后端排障用的日志分析小工具，目标是把一段 HTTP 服务日志里的请求链路、错误分布和慢请求自动整理出来，并能直接输出一份可读的 Markdown 排障报告。请你自己研究一下适合的 Python 标准库/第三方库、日志解析和结构化输出的最佳实践，然后把代码、测试和使用说明一起做出来；不要依赖现成的样例数据，代码里要自己定义清晰的日志格式和示例用法，最后希望能有一个可运行的命令行工具、核心解析模块、测试集和 README。
```

### 737. D5_s982036_zh (domain=D5, difficulty=7)

```
我们现在要把线上服务的故障排查做得更快一些，减少日志里来回翻找的时间。我想从零做一个小工具，能把一段应用日志自动整理成可读的排查报告，最好还能把常见错误按时间线和严重程度归类，方便值班同事直接看。请你帮我设计并实现这个工具，产出可直接运行的代码和说明文档；如果你认为有必要，可以顺手加一个简单的命令行入口。希望它能支持常见的文本日志格式，能从日志里识别错误、警告、重复报错、异常堆栈和关键时间点，并生成一份结构清楚的总结。你先查一下现在比较通用的日志解析和命令行工具做法，再从头搭建实现，不要依赖现成的成品系统。最后把代码、测试和使用说明一起给我。
```

### 738. D5_s982044_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for Kubernetes incidents. I want a CLI in `triage.py`, a small `triage/` package, and `README.md` with setup, usage, and examples; no input files, just code. Research current best practices for parsing JSON logs, regex-based stack trace extraction, and recommended CLI patterns before you build it.
```

### 739. D5_s982047_zh (domain=D5, difficulty=7)

```
我需要你从零做一个给 SRE/后端排障用的小工具：围绕 Kubernetes Pod 日志里的错误堆栈和告警文本，做一个命令行加 Python 库的“日志归因助手”，它能把常见报错模式归类、提取关键字段、给出可能根因和下一步排查建议，并输出 JSON 和 Markdown 报告；你先帮我把方案、代码、测试和 README 都写出来，目录结构你自己定，但要是能直接跑的完整项目。
```

### 740. D5_s982050_zh (domain=D5, difficulty=7)

```
帮我从零做一个可落地的日志排障小工具，目标是让工程师把服务日志贴进去后，快速看出错误模式、时间线和可能根因。
- 做成一个本地可运行的命令行工具，支持 stdin/文件输入、按时间排序、按级别聚合、提取关联请求 ID。
- 需要有一个规则引擎：能识别常见 Java/Python/Go 服务日志里的异常、重试、超时、连接失败，并输出简短诊断摘要。
- 加一个测试计划和单元测试，覆盖典型日志、乱序日志、缺字段日志、以及误报/漏报场景。
- 再补一份 README，说明安装方式、命令示例、输出格式和已知限制。
- 你可以参考现成生态里日志解析/命令行参数/测试的最佳实践，但代码本身要从头实现，不要直接套现成项目。
```

### 741. D5_s982058_zh (domain=D5, difficulty=7)

```
我需要你从零搭一个给 SRE/后端排障用的命令行工具，专门分析 Nginx 和应用日志里的错误链路、自动归类常见异常、并生成一份可直接发给团队的排障摘要。你先自己查一下当前比较合适的 Python 日志解析/彩色输出/命令行参数库的最佳实践，然后直接产出代码和 README，最好把核心解析器、CLI、测试、示例用法都补齐，项目里不要依赖任何现成输入文件，代码要能直接运行并用你自己写的测试覆盖主要场景。
```

### 742. D5_s982071_zh (domain=D5, difficulty=7)

```
我需要你从零做一个小型的日志排障工具，目标是帮我们把一堆分散的应用日志快速汇总成一份可读的故障分析报告：你先做一个命令行程序，支持读取本地目录里的多份文本日志，自动提取时间线、错误栈、重复告警和高频关键字，然后输出 Markdown 报告和结构化 JSON；再补一份 README 说明安装、用法和示例命令，并加上单元测试和一个最小可运行的 demo。实现前先查一下 Python 里适合做日志解析、正则抽取、终端输出和 Markdown 生成的常用库/最佳实践，尽量选成熟方案，但代码本身要你从头实现，不要依赖现成的日志分析成品。
```

### 743. D5_s982074_zh (domain=D5, difficulty=7)

```
帮我从零做一个用于排查线上问题的日志分析小工具，目标是把一堆服务日志快速变成可读的故障线索。
- 我希望你先调研一下当前常见的日志格式处理方案、Python 里适合做流式解析/聚合的库，以及终端报表输出的最佳实践。
- 然后直接从零实现一个可运行的命令行工具，支持按时间范围、级别、关键字过滤，并能自动聚合高频错误、慢请求、异常堆栈模式。
- 工具最好能输出一份结构化的诊断报告，既能看终端摘要，也能导出成 Markdown。
- 还要补上单元测试和一份简短的使用说明，保证我拿到代码后可以直接跑起来验证。
- 不要依赖现成样例数据；代码里用测试构造日志样本即可。
```

### 744. D5_s982082_en (domain=D5, difficulty=7)

```
I need you to build a small Python incident-debugging tool from scratch that tails app logs, detects common failure patterns, and turns them into a readable root-cause report with suggested next checks. Please include the code files, a short README, and a test suite; don’t use any starter project. I want it to support plain text and JSON logs, configurable regex rules, and a CLI that can print a summary or write the report to a file.
```

### 745. D5_s982094_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上日志问题的 Python 小工具，目标是把零散的 JSON/文本日志流按 trace_id / request_id 关联起来，自动生成一份可读的故障摘要、时间线和高频异常统计；你帮我直接产出代码和 README，支持命令行读取 stdin 或指定日志文件、输出 Markdown 报告，还要顺手把常见的 Python 日志格式、结构化日志最佳实践和现成库选型调研一下再决定实现方案。
```

### 746. D5_s982106_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上问题的小工具：写一个 Python 命令行应用，专门把应用日志里的 request_id、耗时、状态码、异常栈和慢请求自动整理成可读的故障摘要，并且支持按时间窗口过滤、按 request_id 追踪一条请求链路、输出 JSON/Markdown 两种报告格式。代码、测试、README 都要一起给我，另外最好把你查到的 Python 日志解析、CLI 设计和报告生成的做法也顺手整理进文档里，方便我后面直接接到 CI 里用。
```

### 747. D5_s982113_en (domain=D5, difficulty=7)

```
Build a small but production-credible Python incident-log triage tool from scratch for our SRE workflow. It should ingest plain-text application logs from stdin, correlate request IDs across lines, detect common failure signatures (timeouts, retries exhausted, upstream 5xx cascades, JSON parse errors, auth failures), and emit a ranked diagnosis summary plus a compact timeline for the top incident. Use current best practices for Python logging, regex parsing, and CLI design, and research any library/API choices with web sources before implementing. I want the full codebase plus a README with usage examples and a short test plan; no input files will be provided, so include self-contained fixtures/tests in the repo and make the tool work on pasted log snippets or piped input.
```

### 748. D5_s982118_zh (domain=D5, difficulty=7)

```
我需要你从零搭一个小工具：做一个面向生产排障的日志分析器，用来解析一组服务端应用日志，自动提取错误模式、按时间聚合告警、给出可操作的排障建议，并支持命令行运行和一份简短的使用说明。代码和文档都要一起产出，最好把核心解析、规则引擎、CLI、测试和 README 分开处理，方便最后集成成一个可直接跑的项目。
```

### 749. D5_s982120_en (domain=D5, difficulty=7)

```
We need a small internal troubleshooting tool because our support team keeps losing time when customer systems fail and the only thing we get is a pile of logs. I want a from-scratch command-line utility that can read plain-text application logs, detect common failure patterns, group related lines into one incident, and produce a clean summary that a non-engineer can understand. It should also let us quickly spot the most likely root cause, the first bad event, and any repeated error bursts. Please research the best Python libraries and current logging best practices first, then build the tool and include tests and short usage instructions. No input files will be provided in advance; the tool should work on logs we paste or pass in later.
```

### 750. D5_s982122_en (domain=D5, difficulty=7)

```
I want a small from-scratch Python tool for debugging and log analysis that I can use on real services.
- Build a CLI that ingests text logs from stdin or a file, detects likely failure patterns, and groups related events into incidents.
- Include rules for common issues like retries, timeouts, connection resets, and exception chains, plus a simple plugin-style way to add more patterns later.
- Add a summary report mode that prints the top incidents, probable root-cause signals, and a timeline view for a chosen incident.
- I want solid tests, clear usage docs, and a short design note explaining the parsing approach and any tradeoffs.
- Please research current best practices and library options for CLI parsing, regex/log parsing, and test structure before building it.
```

### 751. D5_s982123_zh (domain=D5, difficulty=7)

```
帮我从零做一个用于排查线上故障的日志分析小工具，最好能直接跑在本地命令行里。
- 目标是把一段应用日志里的错误、告警和关键上下文自动聚合出来，按时间线和同一请求链路整理，方便值班时快速定位问题
- 希望支持至少两种常见日志格式，并能通过配置扩展字段映射；遇到解析失败的行不要崩，要有清晰的错误统计
- 需要给出一个可执行的 CLI，能输入日志文本/文件、输出摘要报告，还要带一个简单的测试计划和单元测试
- 另外帮我补一份 README，说明设计思路、依赖选择、使用方法，以及怎么把它接到 CI 里
- 如果你在设计时需要参考现成库、CLI 设计习惯、日志格式最佳实践，就自己去查资料，但实现必须是你从头写出来的
```

### 752. D5_s982133_en (domain=D5, difficulty=7)

```
We need a small internal incident-debugging tool because our support team keeps losing time when logs from our app, the API gateway, and the worker queue all use different formats and it’s hard to spot the real failure chain. Please build a from-scratch command-line utility that can ingest plain text logs we paste in, normalize the entries, group related events by request or trace ID when present, flag likely root-cause patterns, and produce a clean summary that a non-engineer can read. I want the code, a short README, and a basic test suite so we can hand it to engineering for review. Please research the best lightweight Python libraries and any current logging format conventions before you build it, and make sensible choices on structure and output.
```

### 753. D5_s982146_zh (domain=D5, difficulty=7)

```
帮我从零做一个本地可运行的日志排障工具，重点是把分散的服务日志快速定位到可疑根因。
- 目标是一个命令行工具，支持读取一组文本日志，按时间线聚合、按错误链路分组，并输出可读的排障摘要。
- 需要先做一点在线调研，参考 Python 标准库、常见日志格式、以及现成 CLI 设计最佳实践，避免自己拍脑袋定接口。
- 希望实现核心解析、聚合与根因提示逻辑，再配一个干净的 CLI 和基础测试。
- 最后给我完整代码、使用说明，以及一组能验证关键行为的单元测试。
- 不要依赖外部数据文件，直接把示例和测试样例写进代码或测试里。
```

### 754. D5_s982165_en (domain=D5, difficulty=7)

```
I need you to build a small log-analysis tool from scratch in Python that can ingest application logs from stdin or a pasted string, detect recurring error patterns, group related stack traces, and output a concise incident summary plus a machine-readable JSON report. Please include the code files, a README, and a solid test suite, and use web research to pick a practical parsing approach and any libraries or best practices worth borrowing for structured logging and traceback grouping.
```

### 755. D5_s982180_en (domain=D5, difficulty=7)

```
We need a small internal debugging tool because our engineers keep losing time when a service fails and the logs are too noisy to tell what happened first. I want you to build a from-scratch log triage utility for our on-call team that can take pasted log text, spot the likely root-cause sequence, and generate a short incident summary with the most important warnings, errors, and timestamps. Please use current best practices and research a practical Python approach before building it. I want the actual code/files, not just an explanation, and it should be something we can run locally from the command line and also reuse in a script.
```

### 756. D5_s982187_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for our Kubernetes services: create `logtriage.py` plus `README.md` that can ingest raw multiline logs from stdin, detect common failure patterns, cluster similar incidents, and print a concise incident report with likely root-cause hints. I want the implementation based on current best practices from Python logging, regex parsing, and standard CLI UX, so check the web for up-to-date guidance before coding.
```

### 757. D5_s982194_en (domain=D5, difficulty=7)

```
I want a small but real Python tool that helps me debug flaky services from logs.

- Build a from-scratch CLI that ingests plain-text application logs and flags likely incident patterns, like bursts of errors, repeated restarts, and latency spikes.
- Include a simple rules engine so I can add or tweak detection patterns without changing core code.
- Add a concise JSON output mode plus a human-readable terminal summary for quick triage.
- Make sure it has solid tests, especially for edge cases like out-of-order timestamps and mixed log formats.
- Use current best practices for Python packaging, logging, and CLI design, and research any useful libraries or patterns before implementing.
```

### 758. D5_s982195_en (domain=D5, difficulty=7)

```
I want a small but production-worthy log debugging tool I can actually use in CI and during incident triage.
- Build it from scratch as a Python CLI that can ingest mixed log lines, detect likely root-cause patterns, and print a ranked incident summary.
- Use current best practices and a couple of real libraries/APIs you look up first for log parsing, CLI ergonomics, and test strategy.
- Make it support timestamps, severity normalization, deduping repeated errors, and clustering related stack traces or messages.
- Include a clear README with install/run examples and a few realistic usage scenarios.
- Add a solid test plan and automated tests that cover parsing edge cases, ranking logic, and CLI behavior.
```

### 759. D5_s982240_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps us make sense of production log noise faster, because our support team keeps losing time when incidents happen and we need a simple way to turn raw service logs into a clearer incident summary. Build it from scratch as a real code project, not a mockup: a command-line utility that can read logs from stdin or a file, detect common error patterns, group repeated messages, flag likely root causes, and output a clean incident report in both plain text and JSON. Please research current best practices and any useful open-source libraries for log parsing, pattern matching, and CLI design before you build it, then implement the tool, tests, and a short README so another engineer can run it and understand the output.
```

### 760. D5_s982243_zh (domain=D5, difficulty=7)

```
帮我从零做一个用于排查生产问题的日志分析小工具，目标是把零散的应用日志变成可读的故障诊断报告。
- 需要先调研并选定一个合适的实现方案：比如 Python 里常用的日志解析、时间窗口聚合、异常模式识别库/做法，最好参考官方文档和最佳实践。
- 最终要交付一套可直接运行的代码，支持命令行输入一段日志文本，自动提取错误类型、时间线、关键上下文和重复告警，并输出结构化结果。
- 希望它能识别常见的格式：纯文本日志、JSON 日志、带时间戳的异常堆栈，并且对脏数据、缺字段、乱序日志有基本容错。
- 还要带上完整测试计划和单元测试，覆盖正常样例、边界情况、以及一些容易误判的日志片段。
- 最后整理一份简短的 README，说明设计思路、使用方法、已知限制，以及后续可以怎么扩展成更完整的排障工具。
```

### 761. D5_s982259_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for our Kubernetes services: give me `logtriage.py`, `tests/`, and a short `README.md`. It should ingest plain-text app logs from stdin or a file, detect error patterns, cluster repeated stack traces, and print a ranked incident summary with likely root-cause hints. Use current best practices from Python stdlib + any lightweight parsing approach you research first.
```

### 762. D5_s982270_en (domain=D5, difficulty=7)

```
Build a Python CLI called `logtriage` from scratch for debugging service incidents from application logs. I want `logtriage.py`, `parser.py`, `detector.py`, `report.py`, and `README.md` with install/run examples, plus tests under `tests/`. It should ingest plain-text logs from stdin or a file path, detect common incident patterns, cluster related lines into timelines, and print a concise incident report with likely root-cause hints.
```

### 763. D5_s982277_zh (domain=D5, difficulty=7)

```
我们现在要把线上服务的排障能力补起来，核心原因是客服和工程同事每次看日志都要手工翻很多文件，定位慢、容易漏线索。请你从零做一个可直接运行的日志排障小工具：它能读取一段服务日志，自动识别常见错误模式，按时间线整理出可疑事件，给出一份清晰的排障报告，并尽量把“可能的根因、关联请求、影响范围”讲明白。希望你先自己查一下现成的做法和合适的库，选一个靠谱的实现方案，然后把工具本身、命令行入口、测试和使用说明一起做出来。不要依赖我提供任何输入文件，代码里自己准备示例用法或内置演示日志即可；最后请把能直接交付的代码文件和说明文件给我。
```

### 764. D5_s982299_en (domain=D5, difficulty=7)

```
I need you to build a small Python tool from scratch that ingests plain-text service logs, detects likely incident patterns, and spits out a clean incident summary with the suspected root cause, first-seen timestamp, error spikes, and a suggested next-step checklist. Please research a couple of good Python libraries and current best practices for log parsing, structured output, and CLI design before coding, then give me the finished code files plus a short README with how to run it and example usage. No input files will be provided; make the tool work on text pasted in or read from stdin.
```

### 765. D5_s982303_en (domain=D5, difficulty=7)

```
I want a small but real incident-debugging tool built from scratch for our backend team.
- Build a CLI utility that ingests application logs from stdin or a pasted string and identifies likely root-cause patterns for common failure modes like timeout cascades, retry storms, and noisy neighbor spikes.
- Include a lightweight rules engine or scoring model, plus a clear explanation output that points to the strongest signals in the log text.
- Research a couple of current, well-supported Python libraries for CLI parsing, log parsing, and test tooling before you implement, then pick sensible defaults and justify them in the README.
- Add a solid test suite with representative synthetic log cases, edge cases, and regression coverage for the detection logic.
- Package it cleanly with usage examples and a short design note so another engineer can extend the rules later.
```

### 766. D5_s982321_en (domain=D5, difficulty=7)

```
I need you to build a small log-diagnostics tool from scratch for our SRE workflow: a Python package plus a CLI that reads plain-text app logs from stdin, detects common failure patterns, groups related stack traces, and prints a concise incident summary with severity, likely root cause, and next-step suggestions. Please include the code files, a README with usage examples, and a test suite; I want it to be based on current best practices and real Python logging/parsing library guidance, so research any useful libraries or patterns first and then implement it cleanly.
```

### 767. D5_s982326_en (domain=D5, difficulty=7)

```
Build a small incident-debugging toolkit from scratch for our on-call team. I want a working codebase, not a writeup.
- Make a CLI that tails a log file, detects likely root-cause patterns, and groups related events into incident timelines.
- Use current best practices for structured logging and regex/pattern matching; check the docs for Python’s logging, argparse, pathlib, and any lightweight libraries you think are worth using.
- Include a simple local web dashboard or terminal report that shows the grouped incidents, top error signatures, and a short summary of probable causes.
- Add tests for the parser, grouping logic, and CLI behavior, plus a short README with setup and usage.
- Keep it self-contained and implement everything from scratch; no input datasets, just the code and tests.
```

### 768. D5_s982327_zh (domain=D5, difficulty=7)

```
我想从零做一个面向 SRE/后端排障的日志告警小工具，目标是能直接拿来给团队用。
- 先帮我调研一下现成做法，重点看 Python 生态里日志解析、规则匹配、CLI 输出和测试这几块，最好参考几个真实项目/库的最佳实践。
- 然后从零实现一个命令行工具，能读取多行日志文本，按我定义的规则检测异常模式、做聚合统计，并输出可读的排障摘要。
- 需要支持常见场景：正则/关键字匹配、按时间窗口聚合、按严重级别分组、以及生成一份结构化 JSON 报告。
- 希望代码、测试和 README 都齐全，能直接运行、能直接改规则配置继续用。
- 如果你觉得有必要，可以顺手补一个简单的扩展点设计，方便后面接入更多规则类型或导出格式。
```

### 769. D5_s982346_zh (domain=D5, difficulty=7)

```
我需要你从零做一个可直接跑的日志排障小工具，目标是给我们内部用来分析应用启动失败和接口超时的日志：先用 Web 查一下现在常见的 Python 日志结构化方案、CLI 参数解析和日志高亮/过滤的最佳实践，然后实现一个基于 Python 的命令行工具，支持按时间范围、级别、关键词、trace_id 过滤，能把多行异常堆栈聚合成一条事件，还要输出一份简短的使用说明和测试计划；代码和文档都自己写，不要依赖我给任何输入文件，直接把项目骨架、核心逻辑、命令行入口、测试和 README 一起做出来。
```

### 770. D5_s982370_zh (domain=D5, difficulty=7)

```
我需要你从零做一个给 SRE/后端排障用的小工具，目标是把一份系统日志里的错误自动聚类成几类常见故障，并生成一份可读的排障报告；你直接给我完整代码和 README 就行。这个工具要支持命令行输入本地日志文本、按时间范围过滤、抽取异常堆栈和关键错误码、输出 JSON 和 Markdown 两种报告，还要带测试和一套基础的日志解析规则。实现前先查一下 Python 标准库、常用日志解析/正则处理的最佳实践，以及类似工具在 CLI 设计上的做法，确保方案靠谱。
```

### 771. D5_s982372_zh (domain=D5, difficulty=7)

```
我们最近在做线上服务稳定性提升，最需要的是把日志排查这件事做快、做准，不然每次出故障都要靠人肉翻日志，响应太慢。我想从零做一个小工具，专门用来分析服务日志里的报错和告警，帮我快速看出异常模式、常见错误、时间分布和可疑关联。你不用给我现成方案，按你认为最合适的方法设计并实现出来。

请直接交付完整代码和说明文档，做成一个可以本地运行的小项目。这个工具最好支持：
1）读取一段文本日志并提取关键字段；
2）自动归类错误类型，找出高频问题；
3）按时间线输出异常峰值和可能的连锁影响；
4）生成一份给排障同事看的简明报告；
5）附带一套测试，说明它在常见和边界情况下都能正常工作。

如果你需要参考最佳实践、现成库的用法、日志分析和测试设计思路，可以自己上网查一下再决定实现方式。重点是要从零把工具做出来，不要依赖我提供任何输入文件。
```

### 772. D5_s982392_zh (domain=D5, difficulty=7)

```
帮我从零做一个 Python 诊断工具，目录结构你来定，最终给我代码和 README。这个工具要能读应用日志，按错误模式聚类，自动生成一份排障报告；同时带一个 CLI，可以指定日志目录、时间窗口和输出格式。先调研一下现在常用的 Python 日志解析/匹配方案和 CLI 最佳实践，再开始实现。
```

### 773. D5_s982398_en (domain=D5, difficulty=7)

```
I want a from-scratch internal debugging tool for our Node.js services that can turn raw app logs into a usable incident timeline and quick triage summary.
- Build a small CLI in TypeScript that ingests plain-text logs from stdin or a file and groups events by request ID / trace ID.
- Detect common failure patterns like uncaught exceptions, timeout cascades, retry storms, and dependency errors, then rank the likely root cause.
- Add a compact JSON output mode for machines and a human-readable mode for on-call engineers.
- Include solid tests and a short README with setup, usage, and a few real example commands.
- Use current best-practice libraries for parsing, CLI flags, and timestamp handling after checking the web, but implement the actual analyzer yourself from scratch.
```

### 774. D5_s982406_en (domain=D5, difficulty=7)

```
I need you to build a small log-analyzer tool from scratch in Python that helps debug production incidents by parsing app logs, grouping repeated errors, and flagging suspicious spikes in error rate. Make it usable from the command line, with a clean JSON output mode and a human-readable summary, and include unit tests plus a short README. Please research a couple of current Python log-parsing/testing libraries and CLI best practices before coding so the design isn’t guesswork.
```

### 775. D5_s982407_zh (domain=D5, difficulty=7)

```
我需要你从零做一个 Python 小工具，专门给线上服务的日志排障用：输入一段原始日志文本后，能自动识别错误模式、按时间线聚合相关事件、给出可能根因和排查建议，还要提供一个简单的命令行接口和一组可运行的单元测试。你先帮我查一下适合这类日志分析的现成库、Python 标准库的最佳做法，以及类似工具的常见输出格式，然后直接把代码和 README 一起写出来，别依赖任何现成样例数据。
```

### 776. D5_s982408_en (domain=D5, difficulty=7)

```
We keep getting burned when production incidents happen because the logs are too noisy, the root cause is hard to spot, and our engineers waste time stitching together clues by hand. I want a small but solid command-line tool we can use internally to analyze application logs, flag likely error bursts, and generate a short incident summary that a non-expert can hand to engineering. Build it from scratch and make it practical for real logs, not a toy demo. Please use current best practices and check a couple of modern Python libraries or approaches before you implement, so we don’t end up with something fragile. I want the code files, a short README, and tests that show it works on messy log text and edge cases.
```

### 777. D5_s982416_zh (domain=D5, difficulty=7)

```
帮我从零做一个本地可运行的日志故障排查工具，针对 Kubernetes / Docker 容器日志，能自动归类常见错误、提取关键上下文、给出可执行的排查建议。请直接产出代码和文档，至少包含核心解析器、CLI、测试、示例用法和 README。
```

### 778. D5_s982417_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-triage tool from scratch that helps debug backend incidents by parsing structured app logs, detecting common error patterns, and generating a short incident summary plus a test plan. It should expose a CLI, include a reusable library module, and ship with tests and a README. Please research current best practices and a couple of solid Python libraries for JSON log parsing, CLI handling, and terminal output before you implement it, then build the codebase and the docs.
```

### 779. D5_s982419_en (domain=D5, difficulty=7)

```
I need you to build a small from-scratch log investigation tool for our engineering team: a Python app that can ingest plain-text application logs, detect common failure patterns, cluster related incidents by fingerprint, and output a clean summary report plus a CLI for ad hoc analysis. Please research a few current Python libraries and best practices first, then implement the code, tests, and a short README with usage examples; no input files are provided, so the tool should work with logs pasted in or piped from stdin.
```

### 780. D5_s982424_zh (domain=D5, difficulty=7)

```
请帮我从零开发一个命令行工具，叫做 `trace-to-testplan`。它的输入是一个 Python 追溯（traceback）文本（支持从文件读取或管道传入），输出是一个结构化的测试计划（markdown 或纯文本），帮助开发人员理解并重现那个 bug。不需要给任何预先准备好的数据文件——用户会自己提供追溯文本作为参数。我需要这个工具能处理真实的 Python 追溯，包括多行堆栈、自定义异常、缺少源代码行（仅显示 'None'）、以及跨文件调用的情况。还要考虑追溯可能来自压缩过的日志（gzip 格式，通过标志指定）。输出格式要求：测试计划至少包含以下章节：‘错误摘要’（异常类型和消息, 堆栈顶部）、‘重现步骤’（模拟触发条件的命令或脚本骨架）、‘相关代码位置’（列出堆栈中的文件名和行号，并尝试提取附近源码，如果本地可访问）、‘可能根因分析’（基于常见错误模式给出提示，比如 AttributeError 可能是拼写、NoneType 等；这一部分需要联网搜索 Python 官方文档或常见陷阱，以给出权威参考）、‘测试用例建议’（至少三个自动生成的 pytest 风格的测试函数骨架，覆盖正常场景、边界和异常）。工具需要支持子命令：`parse`（核心解析并输出）、`reconstruct`（尝试根据追溯信息从本地文件系统恢复代码上下文）、`help` 和 `version`。所有子命令要有基本的参数校验（如缺少输入文件时报错）。请确保代码完全从零写起，不要依赖外部解析库（如 traceback 标准库可以用，但不要用现成的第三方追溯解析器）。此外，请编写一套完整的 pytest 单元测试，覆盖：标准追溯、多行消息、缺少行号、gzip 输入、无效文件、以及预期输出格式的关键字段。最后，提供一份清晰的 README.md，包含安装、用法示例、支持格式说明和开发指南。所有代码文件（工具主程序 `trace_to_testplan.py`、测试文件 `test_trace_to_testplan.py`、以及 `README.md`）都需要作为交付物。注意：开发过程中，你需要通过网页搜索确认 Python 追溯的官方规范（PEP 3134、PEP 409 等），以及 pytest 对参数化测试的最佳实践，并在报告中引用这些资料。
```

### 781. D5_s982432_zh (domain=D5, difficulty=7)

```
我们现在要把线上服务的排障和日志检查做得更可靠一些，减少团队每次靠人工翻日志找问题的时间。请从零做一个小工具，专门用来分析服务日志里的错误、自动归类常见故障，并给出一份可执行的排查建议。这个工具最好能直接在命令行里用，能读标准输入或本地日志文本，支持按时间范围、错误级别和关键词筛选，输出一份清晰的摘要和“下一步怎么查”的建议。请你自己先查一下现成的做法和合适的 Python 库/实现方式，再把代码、测试和使用说明一起做出来；如果你觉得更适合用别的语言也可以，但要从头实现，不要依赖现成的日志平台。最后请把可运行的代码和 README 一起给我。
```

### 782. D5_s982456_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering teams debug incident spikes faster. I want you to build it from scratch, because right now people are piecing things together by hand in spreadsheets and chat threads, and it’s slowing down response time. The tool should take plain log text pasted into it, find the most likely error patterns, group related lines into incident clusters, and produce a short summary that a manager can read quickly. It should also let an engineer drill into the exact lines that triggered each cluster and flag repeated failures over time.

Please research the best current approach for doing this in a lightweight way with Python, including a sensible log parsing library, a simple clustering or pattern-matching approach, and a straightforward way to package it so it can run locally. Then build the code, tests, and a short README. I do not have any input files for you — please design the tool and its behavior yourself, and make reasonable choices based on current best practices.
```

### 783. D5_s982479_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上日志问题的小工具，目标是把一段服务日志解析、归类、做基础统计，然后生成一份可读的故障摘要和诊断建议，最好能直接跑在本地命令行里，支持输入文本日志并输出 Markdown 报告；你顺手把实现代码、测试、README 和一个简单的使用示例都补齐。另外先帮我查一下 Python 里适合做流式日志解析、正则分组、CLI 参数处理和 Markdown 生成的主流库/最佳实践，再决定实现方案。
```

### 784. D5_s982511_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for debugging flaky CI logs: add a log parser, failure-pattern detector, and a report generator in `src/`, plus a small CLI in `cli.py`. Use current best practices from the web for Python log parsing, structured logging, and regex-safe pattern handling, then wire in tests and a short `README.md`.
```

### 785. D5_s982513_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查服务日志问题的命令行工具，目标是把一组应用日志里的错误自动归类、提取关键上下文，并生成一份可读的排障摘要；请直接给我完整代码和 README，最好用 Python 实现，支持读取本地文本日志、按时间范围和级别过滤、识别常见异常堆栈、输出 Markdown 报告，还要带上单元测试和一个最小可运行示例。
```

### 786. D5_s982514_en (domain=D5, difficulty=7)

```
I need you to build a small but real incident-log triage tool from scratch in Python that watches a folder of app logs, detects common failure patterns, and prints a concise root-cause summary plus suggested next checks. Please include the code, a README, and tests, and use current docs for a few real logging/parsing libraries or standard-library best practices so the design is solid. Make it work as a CLI with configurable rules, severity levels, and a JSON report output.
```

### 787. D5_s982515_zh (domain=D5, difficulty=7)

```
我需要你从零搭一个给 SRE 用的日志/故障排查小工具，最好是一个 Python 命令行项目：能读入应用的文本日志，按时间窗做聚合，自动识别常见错误模式（比如超时、重试风暴、连接池耗尽、5xx 激增），输出一份可读的排障报告，还要带一个简单的本地 Web 页面或 Markdown 报告导出。请把代码、测试和 README 一起做出来，顺手研究一下现成日志处理库、CLI 框架和 Python 测试最佳实践后再定方案。
```

### 788. D5_s982516_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and operations teams make sense of server incidents faster. Right now the logs from our app, Nginx, and worker jobs are all over the place, and people waste time manually searching them when an outage happens. I want you to build a from-scratch command-line tool that can read plain-text logs, detect likely incident windows, group related errors, and produce a clean summary we can use during debugging and postmortems. Please research current best practices for log parsing, time-window grouping, and incident-style output formats, then build the tool and include clear instructions for running it. I do not have any input files to give you — design the tool with sample logs generated in code or tests, and deliver the finished code files plus a short README.
```

### 789. D5_s982528_zh (domain=D5, difficulty=7)

```
我们现在要把客服和运维每天收到的错误日志，做成一个能直接用的排查小工具，减少人工翻日志的时间。请你从零设计并实现一个本地可运行的命令行工具，专门用于分析应用日志里的报错、按时间和错误类型做归类、找出重复出现的高频问题，并输出一份适合团队排查的摘要报告。希望它不是一个简单脚本，而是一个比较完整的小工具：能读标准输入或本地日志文本，支持常见日志格式，能识别时间戳、级别、错误信息和堆栈片段，最后生成可读性强的结果。你先自己查一下适合这个场景的 Python 日志解析、命令行参数设计和测试实践，再把工具完整做出来；如果有合适的开源做法或库，可以参考思路，但代码要自己写，不能依赖现成成品。请把最终代码、测试和使用说明都一起交付出来，方便我直接拿去给工程团队试用。
```

### 790. D5_s982558_en (domain=D5, difficulty=7)

```
Build a small Python 3.12 CLI called logtriage for debugging Kubernetes app incidents from scratch. I want src/, tests/, pyproject.toml, and README.md; include a parser for JSON logs and plain text logs, severity grouping, error signature clustering, and a concise incident summary report. Use current best practices from Python logging/argparse and any relevant open-source libraries you need to verify via web research first.
```

### 791. D5_s982563_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-debugging tool from scratch that watches a live app log stream, detects common failure patterns, and generates a compact incident summary with likely root-cause hints and a test plan. Please research current best practices for structured logging and log-pattern detection with web sources, then implement the tool, CLI, tests, and a short README. There are no input files — the tool should work on pasted log text or stdin and be usable right away.
```

### 792. D5_s982572_zh (domain=D5, difficulty=7)

```
帮我从零做一个 Python 诊断工具：解析应用日志、自动聚类常见错误、生成故障排查摘要，并提供一个 CLI（支持 ingest/analyze/report 三个子命令）和一组单元测试。请直接产出代码文件和 README.md，顺手把你查到的相关日志结构、Python 日志解析/聚类最佳实践也融进去。
```

### 793. D5_s982574_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上日志问题的小工具，目标是写成一个可直接跑的命令行项目：它能读取多行应用日志，按时间窗口聚合错误、按请求 ID 追踪链路、识别常见异常模式，并输出一份带结论的诊断报告和可读的摘要。请你顺手把项目代码、测试和 README 一起补齐，尽量参考一下现成的日志格式最佳实践、Python 标准库里适合做解析/时间处理/命令行参数的写法，以及业界常见的日志告警和根因分析思路；我不提供输入文件，你自己在代码里把解析规则、示例日志和测试用例都设计好。
```

### 794. D5_s982585_en (domain=D5, difficulty=7)

```
I need you to build a small open-source-friendly log triage tool from scratch in Python that watches a stream of application logs, detects common failure patterns with rule-based matching plus a simple anomaly score, and outputs a clear incident summary with likely root causes and suggested next checks. Please research current best practices and a couple of lightweight libraries for streaming/log parsing and CLI ergonomics, then implement the code, tests, and a README for how to run it and extend the rules. No input files are needed — just create the project files and make it work end to end.
```

### 795. D5_s982589_zh (domain=D5, difficulty=7)

```
我们现在想把线上故障排查做得更快一点，因为客服和工程团队每次看日志都要来回切换，定位慢、漏线索也多。我希望你从零做一个小工具，把我们常见的服务日志和错误堆栈整理成一套可用的“排障助手”，最好能直接在本地跑起来，帮助人快速看出异常、按时间线串起来，并给出一些基础判断。你可以自己决定最合适的实现方式，但要把核心功能做扎实，别只是一个简单脚本。

具体希望你完成这些内容：
1. 做一个可运行的命令行工具，能够读取一份标准格式的日志文本，自动识别常见级别、错误、请求ID、时间戳和重复告警。
2. 输出一份结构化的排障摘要，至少包括：最常见错误、首次出现时间、可能相关的前后日志、以及你认为值得继续查的异常点。
3. 增加一个“时间线模式”，把同一个请求或同一类错误按顺序串起来，方便人肉排查。
4. 提供一个简单的测试方案和自动化测试，让人能验证它在几种典型日志场景下确实可用。
5. 顺手把使用说明、输入格式示例和局限性写清楚，避免别人接手后不知道怎么用。

我不需要你先给我分析思路，直接把这个工具从头做出来，包含代码、测试和说明文档。实现时如果需要参考现成日志处理、命令行参数、文本解析或测试方面的最佳做法，你自己去查最合适的方案，然后按我们的需求落地。
```

### 796. D5_s982590_en (domain=D5, difficulty=7)

```
I need a small but real developer tool built from scratch for diagnosing flaky services from logs and test runs.

- Build a Python CLI that ingests raw text logs pasted into stdin and flags likely root causes for failures.
- Include pattern-based detection for common issues like timeouts, retries, port conflicts, dependency outages, and assertion failures, with a clear explanation for each match.
- Add a compact HTML or Markdown report output that summarizes the findings, shows evidence snippets, and groups related events into a timeline.
- Please research current best practices and relevant library choices first, especially for CLI design, log parsing, and test-friendly output formatting.
- Deliver the finished code and a short README with usage examples and how to run the tests.
```

### 797. D5_s982598_zh (domain=D5, difficulty=7)

```
我需要你从零做一个可用的日志排障小工具：把它做成一个 Python 命令行程序，能读取应用日志并自动识别错误模式、按时间聚合异常、给出可能的根因建议，还要支持输出 Markdown 报告和 JSON 结果，另外顺手把单元测试和使用说明一起补上。实现前先查一下常见日志解析、Python 标准库/第三方库选型、以及业界对日志字段和错误分类的最佳实践，再开始写代码；最后把项目代码、测试和 README 都整理好给我。
```

### 798. D5_s982603_zh (domain=D5, difficulty=7)

```
帮我从零做一个可落地的日志排障小工具，面向 Kubernetes / 微服务场景，目标是把分散的应用日志和错误信息快速归因。
- 我希望它能从标准输入或本地日志文件读取文本日志，自动抽取时间、级别、服务名、trace_id、错误栈，并生成一份可读的排障摘要。
- 需要支持一个命令行工具，至少包含“解析日志”“按 trace 聚合”“输出 Markdown 报告”这几类能力，方便我在 CI 或本地直接跑。
- 请顺手查一下 Python 里适合做日志解析、命令行参数、富文本输出/报告生成的成熟方案和最佳实践，但最终实现要自己从头写，不要依赖现成的整套日志分析产品。
- 我还想要一套最基本但有质量的测试计划和单元测试，能覆盖正常日志、缺字段日志、混合格式日志、以及错误输入处理。
- 最后把代码、简要使用说明、以及测试一起给我，确保我拿到就能运行和扩展。
```

### 799. D5_s982620_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for debugging and log analysis that ingests plain-text app logs, detects recurring failure patterns, and generates a concise incident report plus a timeline. Research the best-fit parsing/CLI/testing approach first, then implement the code and tests in app.py, parser.py, analyzer.py, cli.py, and tests/.


```

### 800. D5_s982638_zh (domain=D5, difficulty=7)

```
帮我从零做一个用于排查线上故障的小工具，面向 Python 微服务日志。希望你输出可直接运行的代码和说明。
- 这个工具要能读取一段文本日志，自动识别常见错误模式，比如超时、重试风暴、连接池耗尽、请求链路里某个环节的 5xx 激增。
- 希望它同时支持命令行模式和一个简单的 HTTP API，方便本地脚本和服务集成。
- 你需要先做一点 Web 调研，参考现成日志格式、常见可观测性实践和合适的 Python 库，再开始设计实现。
- 代码要包含测试计划和单元测试，最好再补一个最小可用的 README，说明怎么跑、怎么接入、怎么看输出。
- 我不要你分析任何现成数据文件；请直接从零实现这个诊断工具的代码、测试和文档。
```

### 801. D5_s982642_en (domain=D5, difficulty=7)

```
Build a small Python log-triage tool from scratch for Kubernetes-style app logs: `logtriage.py` plus `README.md`. It should parse newline-delimited JSON and plain-text logs, detect error spikes, cluster likely duplicate incidents, and emit a concise incident summary with probable root-cause hints. Use web research for current best practices on log parsing, clustering, and CLI design before you code.
```

### 802. D5_s982646_en (domain=D5, difficulty=7)

```
I need you to build a small log-triage tool from scratch for our on-call workflow: read live or pasted Kubernetes app logs, detect likely error patterns, cluster repeated stack traces, and output a concise incident summary plus suggested next debugging steps. Please use current best practices from the web for log parsing and terminal UX, then deliver the code and a short README with setup and usage examples.
```

### 803. D5_s982649_zh (domain=D5, difficulty=7)

```
我们团队最近在排查生产环境里偶发的接口超时和日志噪音问题，运维和研发来回沟通很慢，我想做一个从零开始的小工具，把这类日志快速整理成可读的诊断结果，帮助我们更快定位是超时、重试风暴、还是下游依赖异常。请你直接帮我开发这个工具，不要给我现成思路清单，尽量把方法和实现都一起做出来。

我希望你做一个可在本地运行的命令行工具，能够读取一段或多段服务日志，自动识别常见问题模式，输出一份简洁的故障分析报告。它至少要支持：
1）按时间顺序整理日志并去重；
2）识别超时、重试、HTTP 5xx、连接失败、限流这几类信号；
3）把同一条请求链路里分散的日志尽量串起来；
4）给出“可能原因 + 证据片段 + 建议下一步排查”的结果；
5）可以导出成 Markdown 报告；
6）附带一套能自己跑的测试，覆盖正常、缺字段、乱序、重复日志这些情况。

实现方式你来定，但要尽量做得像真的能交给运维和研发一起用的工具。请你在开发前先查一下 Python 里适合做日志解析、时间处理、命令行和测试的常用库和最佳实践，再开始从零实现。最后把代码、测试和使用说明一起给我，方便我直接落地。
```

### 804. D5_s982657_zh (domain=D5, difficulty=7)

```
我需要你从零做一个给 SRE/开发排障用的日志分析小工具，目标是能把一堆应用日志里按 request_id 串起来，还能自动识别常见错误模式、输出一份可读的排障报告。你先帮我调研一下现在适合做这类工具的 Python 库和最佳实践（比如日志解析、命令行参数、结构化输出、测试框架），然后直接把代码、测试和 README 都写出来；不要依赖现成输入文件，代码里自己定义一套示例日志格式和演示样例，最后给我一个能本地运行的完整项目。
```

### 805. D5_s982660_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering teams debug incidents faster without manually digging through scattered logs. Please build it from scratch as a real working utility that can take raw application logs pasted into it or loaded from a local text file, then identify likely error clusters, summarize the top recurring failure patterns, and flag suspicious bursts by time window. I want the result to be something we can actually run locally as a command-line tool, with clear output that a non-engineer can read and a mode that produces a more detailed engineer view. Please research current best practices for Python log parsing, CLI design, and lightweight anomaly detection so the implementation is sensible and not overcomplicated. Deliver the code files and a short README explaining how to run it, plus tests that show the main behaviors work.
```

### 806. D5_s982666_zh (domain=D5, difficulty=7)

```
帮我从零写一个 Python 命令行工具，叫 logtriage，用来解析应用日志、自动按错误模式聚类、生成排障摘要，并支持 dry-run 和 JSON 输出。把代码放到 app.py，测试放到 tests/，再写一份 README.md 说明安装、用法和典型排障流程；我还要一个简短的设计说明，解释你选的日志解析和聚类方案。
```

### 807. D5_s982683_zh (domain=D5, difficulty=7)

```
我需要你从零做一个面向 SRE/后端排障的小工具，目标是把一段服务日志输入后，自动提取关键错误、做基本聚类和时间线梳理，并输出一份可读的诊断报告，还要带一个命令行入口和单元测试。你先自己查一下现在常用的 Python 日志解析、文本聚类、命令行参数和测试实践，再直接把代码、README 和测试都写出来；不要用现成的数据文件，代码里自己造一小段示例日志来演示就行。
```

### 808. D5_s982690_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for Kubernetes incident debugging: CLI + library that ingests pasted logs from stdin, detects common failure patterns, groups related events by request ID/pod, and outputs a ranked incident summary with suggested next checks. Create `triage.py`, `triage_rules.yaml`, `tests/test_triage.py`, and `README.md`; use current best practices from the web for Python logging, YAML schema handling, and Kubernetes log conventions.
```

### 809. D5_s982692_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called logtriage for debugging Kubernetes-style service logs: parse mixed JSON/text logs, detect error bursts, group likely root-cause spans, and emit a concise incident summary plus a timestamped timeline. I need app.py, tests/, and README.md; use current best practices for Python logging/CLI libs and include a few examples of real log formats to support.
```

### 810. D5_s982693_en (domain=D5, difficulty=7)

```
I need you to build a small log-debugging tool from scratch for a Node.js service: a CLI that reads plain-text app logs, groups repeated stack traces, spots likely root causes from error patterns, and spits out a concise incident report plus a few suggested next-step checks. Please research a couple of current libraries and best-practice approaches first, then create the code, tests, and a short README with how to run it and what the output means.
```

### 811. D5_s982709_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering teams spot recurring problems faster in server logs, because right now people are manually scanning text and missing patterns until customers complain. Please build the tool from scratch and give me the code and a short README for how to run it. I want something practical, not a demo: it should accept raw log text pasted in or read from stdin, group similar errors together, highlight likely root causes, and produce a clear summary we can share in Slack. Please research current best practices for log parsing and lightweight text clustering first, then design and implement the solution in a way that fits a normal Python workflow.
```

### 812. D5_s982716_en (domain=D5, difficulty=7)

```
Build a from-scratch Python 3.12 tool called logscope that parses mixed application logs, groups exceptions by probable root cause, and outputs a compact triage report plus JSON. I need the code in logscope.py, tests in tests/test_logscope.py, and a short README.md with usage examples. Use current best practices from the web for Python logging, regex performance, and CLI design before you implement it.
```

### 813. D5_s982722_en (domain=D5, difficulty=7)

```
I want a from-scratch observability tool for debugging our Node.js services in Kubernetes.
- Build a small log-triage CLI that ingests plain text logs, detects likely root-cause patterns, and groups related lines into incidents.
- Include support for common Kubernetes and Node.js signals like OOMKilled, crash loops, uncaught exceptions, and timeout spikes.
- Research a couple of current libraries or best practices for CLI parsing, log colorization, and terminal tables before you implement it.
- Ship the working code, a clean README, and a test suite that covers the main parsing and grouping behavior.
- Keep it self-contained, with no sample input files required; the tool should run on pasted logs or stdin.
```

### 814. D5_s982728_zh (domain=D5, difficulty=7)

```
帮我从零实现一个 Python 命令行工具，名字叫 logtriage，目标是把一组服务日志里的异常先做聚类、再按严重度打标签，最后输出一份可读的调查摘要。代码放在 `logtriage/`，入口脚本 `main.py`，再给我 `README.md`、`pyproject.toml` 和 `tests/`。先去查一下 Python 里做日志解析、文本聚类、CLI 参数设计的最佳实践和常用库，然后直接按你的调研结果开写。
```

### 815. D5_s982731_en (domain=D5, difficulty=7)

```
I need you to build a small from-scratch Python tool that helps debug Kubernetes microservices by parsing container logs and turning them into a readable incident report: it should detect repeated errors, group related stack traces, spot likely root-cause services, and output both a CLI summary and a JSON report. Please research a couple of current Python log-parsing libraries and best practices for structured logging and stack-trace grouping before you implement it, then deliver the code and a short README with how to run it.
```

### 816. D5_s982732_zh (domain=D5, difficulty=7)

```
我们现在要把客户支持团队的日志排查效率提上去，尤其是每次线上出问题后，大家都得手工翻服务日志、应用日志和告警记录，耗时很大。请从零做一个可直接运行的排障小工具，帮助我们把一段日志里最关键的异常、时间线和可能的根因自动整理出来。你先自己查一下当前比较稳妥的实现方式和现成库的最佳实践，再动手开发，不要依赖我提供任何输入文件。我要的是完整的代码和说明，最好能直接在本地跑起来。

这个工具需要支持：把多行日志文本贴进去后，自动识别错误级别、重复异常、关键时间点和可能关联的上下文；能输出一份结构化摘要；最好还能生成一份便于发给工程师的排障报告。请你自己决定合理的技术方案，但要做到稳定、好维护、便于以后接到我们现有的监控系统里。完成后请把代码、使用说明和测试都一起给我，尽量做成一个我可以直接试用的版本。
```

### 817. D5_s982744_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support team make sense of messy server logs and catch recurring errors before customers complain. I want it built from scratch, not as a write-up, because the team needs something we can actually use and extend. Please create a Python-based command-line tool that can ingest plain-text application logs, detect common error patterns, group related lines into incidents, and produce a short summary that a non-technical manager could read. It should also flag likely root causes based on the log context, and include a simple test plan so we know it works on real-looking examples. Please research current best practices for Python log parsing, CLI structure, and any useful standard libraries or lightweight packages before you build it, then deliver the code and brief README so we can run it ourselves.
```

### 818. D5_s982756_zh (domain=D5, difficulty=7)

```
我们现在每周都要排查线上服务的故障，日志分散在不同格式里，工程师靠手工翻日志太慢了，出问题时也很难快速判断是哪个时间段、哪类错误、哪条链路先坏的。我想从零做一个小工具，专门用来把一段原始应用日志整理成可读的故障排查报告，最好能直接帮助定位异常高发时间、错误类型分布、疑似关联的请求链路，并输出给团队使用。

请你自己先做一点网页调研，看看现在常见的日志结构化、时间窗口统计、错误聚类、命令行工具设计和 Python/Node 里适合做这类事情的做法，然后帮我把这个工具真正做出来，不要依赖任何现成输入文件，直接从代码开始实现。希望最终交付的是可运行的代码和说明文档，最好还能带上测试，方便我们以后继续扩展。
```

### 819. D5_s982780_en (domain=D5, difficulty=7)

```
We need a small internal debugging tool because our support team keeps losing time when production incidents happen and the logs are too scattered to compare by hand. Build a from-scratch command-line utility that can read plain text application logs, detect likely incident windows, group related errors, and generate a clear investigation summary we can hand to engineers. Please research the best lightweight Python libraries and current practices for parsing logs, fuzzy grouping similar messages, and building a reliable CLI, then implement the tool, tests, and a short README. I do not have any input files for you; create everything needed from scratch and make the tool usable on synthetic logs you generate in the code or tests.
```

### 820. D5_s982783_zh (domain=D5, difficulty=7)

```
帮我从零搭一个用于排查线上问题的小工具，目标是把服务日志里的关键错误自动归类，并给出可执行的排障建议。
- 需要先做一点网页调研，看看 Python 里适合做日志解析、规则匹配和 CLI 的主流库，以及它们的最佳实践。
- 最终交付要包含可运行的代码、命令行入口、以及一份简短的使用说明，能直接在本地对日志文本进行分析。
- 工具要支持我手动输入一段日志或读取粘贴到标准输入的内容，输出按错误类型聚合的摘要、相关上下文、和建议下一步该查什么。
- 希望你把核心解析、规则引擎、CLI、测试和文档分开实现，尽量按模块组织，方便后面扩展到更多日志格式。
- 重点不是做数据分析报告，而是做一个真实可用的、从零实现的排障辅助工具。
```

### 821. D5_s982786_zh (domain=D5, difficulty=7)

```
帮我从零写一个 Python 工具，做 Kubernetes 容器崩溃排障：能解析 `kubectl logs` / `kubectl describe pod` / `kubectl get events` 的文本输出，自动归因常见问题（OOMKilled、探针失败、镜像拉取失败、CrashLoopBackOff、配置缺失、权限不足），并生成一份结构化诊断报告。请把代码放到 `k8s_pod_triage.py`，再给我 `README.md`、`tests/` 里的单测和一份 `report.md` 示例输出。先查一下 kubectl 输出格式、常见事件字段和 Python 文本解析/CLI 最佳实践，再开始实现。
```

### 822. D5_s982789_en (domain=D5, difficulty=7)

```
I need you to build a small log triage tool from scratch for Kubernetes-style JSON logs: one Python package plus a CLI that can ingest a stream from stdin, detect likely incident patterns from timestamps/levels/message fields, group related events into a timeline, and output a compact human-readable report and a machine-readable JSON summary. Please research a couple of current Python logging/parsing best practices and any useful standard-library or lightweight library choices before coding, then give me the finished code files and a short README with how to run it.
```

### 823. D5_s982801_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查日志和回放故障的命令行小工具，目标是给我们内部 SRE/后端排障用：它要能读取结构化日志文本，按时间窗口、服务名、trace_id 过滤，自动聚合错误类型和请求链路，并生成一份适合发给工程师的故障摘要报告；同时要支持一个交互式的“回放”模式，把同一条请求的关键事件按时间顺序打印出来，方便定位异常。请你把代码和说明文档一起做出来，最好顺手把测试也补齐，最后给我可以直接运行的项目文件。
```

### 824. D5_s982815_zh (domain=D5, difficulty=7)

```
我需要你从零搭一个可直接用的“服务日志排障助手”：做成一个本地 CLI 工具，能接收多种格式的应用日志（比如 JSON lines、纯文本、带时间戳的错误栈），自动解析、按时间线归并、识别常见异常模式、生成一份可读的故障分析报告，还要带上单元测试和一份简短使用说明。你先自己查一下 Python 里适合做日志解析/结构化输出/命令行参数的现成库和最佳实践，然后把代码、测试和 README 一起给我，目标是让我能在本地直接跑起来做日志分析和排障。
```

### 825. D5_s982818_en (domain=D5, difficulty=7)

```
I need a small but real observability tool built from scratch for our engineering team.
- Make a log triage utility that ingests raw application logs from stdin or a pasted string and classifies likely causes like auth failures, timeouts, rate limiting, and dependency errors.
- Include a lightweight rules engine plus a summary report that groups repeated errors, highlights unusual spikes, and suggests next debugging steps.
- Add a CLI with a couple of practical commands, plus a library interface we can reuse in tests or scripts.
- Use current best practices and existing Python libraries only where they make sense; do a bit of web research first so the design matches modern logging and CLI patterns.
- Ship the actual code, tests, and a short README with usage examples and limitations.
```

### 826. D5_s982828_en (domain=D5, difficulty=7)

```
We keep losing time when production issues happen because the logs are too hard to read and our on-call people need a faster way to spot patterns, errors, and likely root causes. I want a small internal tool built from scratch that can take raw application logs and turn them into something useful for debugging: group similar errors together, highlight important fields, and produce a clear summary we can hand to engineering and support. Please design and build the code for it, including the command-line workflow, the core log-processing logic, and enough tests that we can trust it in day-to-day use. If you need to choose libraries or approaches, research current best practices first and then implement the tool cleanly.
```

### 827. D5_s982833_en (domain=D5, difficulty=7)

```
Build a from-scratch Python incident-log triage toolkit for our on-call workflow that parses application logs, clusters repeated errors, flags probable root causes, and emits a concise triage report plus a small CLI. I want the implementation to be grounded in current best practices, so research the relevant Python logging/regex/testing guidance and any lightweight text-clustering or anomaly-scoring library options before coding. Deliver the built code and a README. The tool should accept raw log text pasted via stdin or a string argument, not files, and it should support: timestamp normalization, severity extraction, error fingerprinting, grouping by stack trace signature, and a summary of the top suspected incidents with counts and first/last-seen times. Keep it dependency-light, but if you choose a library for clustering or parsing, justify it in the README and pin the version. Include a focused test suite and make sure the CLI behaves deterministically for the same input.
```

### 828. D5_s982851_zh (domain=D5, difficulty=7)

```
我需要你从零做一个给 SRE/后端工程师用的日志排障小工具，目标是把一组服务日志里的错误串起来，自动识别同一次请求里的关联事件，输出一份可读的故障摘要和时间线。你直接把代码和说明文档都写出来，最好做成一个可运行的 CLI 工具，支持从标准输入读日志、按 trace_id/request_id 关联、按错误级别聚合、并生成 Markdown 报告；另外我还希望你补一套测试和一些示例用法，方便我以后自己接到 CI 里。这个项目需要你先查一下 Python 里做日志解析、CLI 参数、Markdown 生成和测试的常用库/最佳实践，再从头实现，不要依赖现成的日志样例文件。
```

### 829. D5_s982861_en (domain=D5, difficulty=7)

```
I need you to build a small log-diagnostics tool from scratch that watches a service log stream, detects a few common failure patterns in real time, and produces a readable incident summary with suggested next checks. Use current best practices and the latest docs for a couple of Python logging/CLI libraries and whatever stream-processing or regex utilities make sense, then implement the code, tests, and a short README. No input files — just the codebase and docs.
```

### 830. D5_s982877_zh (domain=D5, difficulty=7)

```
我们现在每天都要看服务故障排查和发布后的日志，靠人工翻日志太慢，出问题时很难第一时间判断是哪个环节坏了。我想从零做一个小工具，帮团队把常见错误日志自动归类、提炼时间线，并生成一份能直接给工程同事看的排障摘要。请你直接帮我设计并实现这个工具的代码，最好是一个能本地运行的命令行程序，输入是一段原始日志文本，输出是结构化的故障报告和简短结论；如果你觉得更合适，也可以顺手加一个简单的 Web 接口。实现时请你先自己查一下现成日志处理库、命令行框架和写测试的最佳做法，再从头搭建，不要依赖我提供任何输入文件。最后把代码、测试和使用说明一起给我，确保别人拿到就能跑起来并复现结果。
```

### 831. D5_s982897_en (domain=D5, difficulty=7)

```
I need you to build a from-scratch log triage tool for our backend team: make a small CLI app that reads plain text service logs, spots likely error patterns, groups related lines into incidents, and prints a short summary with severity, first/last seen timestamps, and probable root-cause hints. It should include the core parsing/deduping logic, a command-line interface, good unit tests, and a README with how to run it and what kinds of logs it handles. Please research a couple of current Python libraries and best practices for log parsing, CLI design, and timestamp handling before you implement it.
```

### 832. D5_s982904_en (domain=D5, difficulty=7)

```
I want you to build a from-scratch Python troubleshooting tool for our engineering team that helps us debug production incidents from application logs and test them locally without relying on any pre-existing dataset. The goal is to produce a small but real command-line utility that can ingest plain-text logs, normalize common timestamp formats, detect repeated error signatures, cluster related stack traces, and generate an incident summary with likely root-cause candidates and recommended next debugging steps.

Please design and implement it as a clean, self-contained project using only code you write from scratch. I do not want a notebook, and I do not want a mock/demo that depends on files I provide. Assume the inputs are raw text pasted on stdin or passed as a file path at runtime, but the repository itself starts empty. The tool should be useful on real logs from Python services, especially logs that include exception traces, request IDs, service names, log levels, and timestamps in more than one common format.

The core behavior I need is this: parse lines into structured events; identify multi-line stack traces and attach them to the originating error event; group events into incident clusters using a configurable similarity rule that treats variable tokens such as UUIDs, hex addresses, numeric IDs, and timestamps as placeholders; rank clusters by frequency and recency; and emit a human-readable summary plus a machine-readable JSON report. I also want a small rules engine for common debugging heuristics, such as: repeated database connection failures, import/module resolution errors, timeout bursts, JSON parse errors, and syntax errors in startup logs. The summary should explain why each cluster matters, what evidence was seen, and what the likely next action is.

I care about edge cases, so please handle at least these explicitly: empty input; logs that interleave unrelated request traces; lines that are continuation lines but not stack traces; exceptions whose tracebacks are truncated; timestamps in ISO 8601, RFC 3339, and common Python logging formats; lines without timestamps; and malformed or partial lines. If two stack traces are essentially the same except for dynamic values, they should cluster together. If a line looks like a stack trace but is actually a pasted code block, it should not be over-aggressively merged unless the surrounding context supports it.

I also want a compact test suite that proves the parser and clustering logic are working on representative synthetic examples created in the tests themselves. Please include tests for the normalization rules, stack-trace extraction, cluster grouping, heuristic classification, and the CLI output format. The code should be documented enough that another engineer can extend the heuristics later.

Before implementing, use web research to check current best practices and relevant library behavior for Python log parsing, timestamp handling, and CLI design. I want you to verify what is reasonable to do with the standard library versus what should be done manually, and to look up any relevant guidance for parsing exceptions and timestamps robustly. Base the design on that research, but write the actual tool from scratch rather than copying an existing package.

Please produce the completed code project itself, with the main application file(s), tests, and a README that explains usage, design decisions, supported log formats, and how the clustering heuristic works. I want the result to feel like a real utility a teammate could run locally for debugging production logs.
```

### 833. D5_s982911_en (domain=D5, difficulty=7)

```
I need you to build a small incident-log debugging tool from scratch for our on-call workflow: a Python CLI that can read plain-text app logs, detect likely crash patterns, group related events into timelines, and print a short incident report with the probable root cause, top symptoms, and the most relevant log lines. Please make it usable from the command line, include a couple of sample commands in the README, and add tests so we can trust the parsing and grouping behavior. You’ll probably need to look up a few current Python libraries and best practices for log parsing/CLI UX before coding it.
```

### 834. D5_s982918_zh (domain=D5, difficulty=7)

```
给我从零做一个 Python 调试工具，专门针对 Docker/Kubernetes 里的服务日志和崩溃堆栈：先查一下现成方案里像 OpenTelemetry、Sentry CLI、py-spy、structlog 的最佳实践，再自己实现一个命令行工具。我要这些文件：app.py、parser.py、diagnostics.py、tests/、README.md，能输入一段日志文本就自动识别常见异常模式、按严重级别聚类、输出修复建议和最小复现步骤草案。
```

### 835. D5_s982921_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-triage tool from scratch that can ingest plain-text app logs, detect likely incident patterns, and spit out a compact debugging report with severity, timeline, and root-cause hints. Make it realistic: use current best practices for structured logging, parsing, and testability, and do a quick web check on good Python libraries/patterns before coding. I want the finished code files plus a README, with solid tests and a simple CLI so I can run it locally on arbitrary log text.
```

### 836. D5_s982930_en (domain=D5, difficulty=7)

```
Build a from-scratch Python incident-log triage tool for our Kubernetes services: parse app logs and generate a ranked root-cause report with timestamps, error clustering, and probable service owners. I need the code in app.py plus tests in tests/, and a short README.md with run instructions; no input files, just make it work against pasted logs or stdin.
```

### 837. D5_s982936_zh (domain=D5, difficulty=7)

```
我们现在需要把线上问题排查这件事做得更快一些。最近客服、运维和开发经常在不同系统里来回翻日志，定位一次故障太慢，也很难统一复盘。我想从零做一个轻量的“日志故障分析工具”，能把一批文本日志里常见的错误模式自动归类，按时间线串起来，并输出一份适合给团队看的排查摘要。

我不需要你直接给我讲方案，我更希望你先做出可以运行的代码和说明文档。这个工具要尽量实用，能处理常见的服务端日志格式，支持命令行使用，最好还能给出简单的测试方法和一个示例运行说明。请你自己调研一下现在常见的做法和适合的开源库，再从头实现，不要只拼接现成脚本。最后把代码、测试和使用说明一起交付给我。
```

### 838. D5_s982941_en (domain=D5, difficulty=7)

```
Build a from-scratch log triage utility in Python for our internal incident-response workflow, targeting Kubernetes-era microservices. I want a small but production-shaped tool that ingests plain-text container logs from stdin or a file, classifies common failure patterns (for example OOMKill, readiness probe flaps, DB connection exhaustion, TLS handshake errors, timeout cascades), extracts the salient fields into structured JSON, and emits a ranked incident summary plus suggested next investigative steps. Include a CLI, a reusable library layer, and a compact test suite. Use current best practices from the Python standard library and any well-supported parsing/CLI libraries only if they materially improve the implementation; research the current APIs and recommended patterns first. Deliver the built code and a README with usage, design notes, and operational caveats. No input files are provided.
```

### 839. D5_s982945_zh (domain=D5, difficulty=7)

```
我需要你从零做一个“服务端日志异常排查助手”，目标是给运维/后端工程师用的：它要能解析一段文本日志，自动识别常见错误模式（比如超时、重试风暴、连接池耗尽、5xx 激增），输出一份结构化诊断报告，并带一个命令行工具和最小可运行的 Python 包。你先查一下 Python 标准库、`argparse`、`re`、`dataclasses`、`logging` 以及常见日志分析最佳实践，再直接把代码、测试和 README 一起写出来；不要用现成日志分析框架，核心解析和规则引擎要自己实现，代码文件、测试文件和文档都要完整。 
```

### 840. D5_s982949_en (domain=D5, difficulty=7)

```
We need a small internal tool to help our support and ops team make sense of production incidents faster. Right now, when something breaks, people paste random logs into chats and we lose time figuring out what happened, what changed, and what to try next. I want you to build this from scratch as a working code tool, not a write-up: a local command-line utility that can take pasted log text from stdin, detect the most likely error pattern, cluster related lines, and produce a plain-English incident summary with likely root-cause categories and next-step suggestions. Please research current best practices for log parsing, pattern matching, and CLI design before you build it, and use that to choose a sensible implementation approach and library stack. I want the finished code files plus a short README with how to run it and how the logic works.
```

### 841. D5_s982956_en (domain=D5, difficulty=7)

```
Build a from-scratch Python 3.12 log-anomaly CLI called `logguard` with `src/`, `tests/`, and `README.md`. It should parse mixed JSON and plain-text application logs, flag likely issues using configurable rules, and emit both a human summary and JSON report. Use web research to pick current best-practice libraries for parsing/CLI/config/testing and document the choices in the README.
```

### 842. D5_s982958_en (domain=D5, difficulty=7)

```
I need you to build a small incident-diagnostics tool from scratch that helps us parse application logs, detect likely root causes, and spit out a concise triage summary for on-call use. Please make it a real code deliverable with the core parser/analyzer, a CLI, and a test suite, plus a short README that explains how to run it. Do a bit of web research first so the design follows current best practices for CLI tooling, structured logging, and log parsing in the Python ecosystem, then implement the tool without using any starter files or input datasets.
```

### 843. D5_s982980_en (domain=D5, difficulty=7)

```
Build a Python log-triage tool from scratch for Kubernetes-style incident debugging: a CLI that ingests live app logs from stdin, detects crash loops/timeouts/4xx-5xx spikes, groups repeated stack traces, and outputs a ranked incident summary plus suggested next checks. Research current best practices for log parsing, stack-trace fingerprinting, and CLI libraries first, then implement the tool and write README.md and tests.
```

### 844. D5_s982982_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-analysis tool from scratch that helps debug flaky CI jobs: it should read plain-text build logs, detect common failure patterns like timeout, OOM, network errors, flaky test retries, and missing dependencies, then output a ranked diagnosis with suggested next steps. Please create the code files, a short README, and a solid test suite; also check current best practices and a couple of well-known Python libraries/docs online so the pattern rules and CLI design are realistic.
```

### 845. D5_s982990_zh (domain=D5, difficulty=7)

```
帮我从零做一个可运行的 Python 命令行工具，项目名就叫 logguard，目标是把应用日志里的报错自动归类、提炼时间线，并输出一份可读的排障报告。请直接给我完整代码和 README.md，最好还能带上单元测试；实现前先查一下 Python 标准库/现成库里做日志解析、颜色输出和 CLI 参数处理的最佳实践。要能支持从 stdin 读日志，按异常类型和请求 ID 聚合，输出 JSON 和 Markdown 两种格式。
```

### 846. D5_s983003_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called logtriage for parsing and triaging mixed application logs from stdout/stderr. I want cli.py, core parser/analyzer modules, and a README.md that documents usage, config, and examples. Add a small test suite too, but no input files — generate any sample logs in code.
```

### 847. D5_s983015_zh (domain=D5, difficulty=7)

```
给我从零写一个 Python 工具，做 K8s 应用日志和事件的故障排查：支持接收一段文本日志/事件流，自动归类常见错误模式、提取关键时间线、输出根因候选和修复建议。请直接交付代码和 README.md，再补一份 tests/ 的单测。
```

### 848. D5_s983019_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-debugging tool from scratch for Kubernetes services: it should read plain-text app logs from stdin or a file, detect common error patterns, group repeated stack traces, summarize likely root causes, and output both a human-readable report and JSON. Please use current best practices and the right libraries by checking the web first, then implement the code, tests, and a short README; there are no input files, just the code you create.
```

### 849. D5_s983028_en (domain=D5, difficulty=7)

```
Build a small Python 3 tool from scratch called logtriage. I want a CLI plus a reusable library that ingests live service logs from stdin or a file, detects error spikes and repeated stack traces, and prints a compact incident summary with likely root-cause clusters. Use current best practices from the web for Python logging parsing and anomaly detection, then implement it cleanly in app.py, triage.py, and README.md. Also include tests for the parser, clustering, and CLI output.
```

### 850. D5_s983042_en (domain=D5, difficulty=7)

```
I need you to build a small open-source-style log triage tool from scratch that watches a folder of application logs, detects error bursts and repeated stack traces, and then produces a clear summary report plus a CLI for running it locally. Make it work like a real utility: include the core parser/analyzer, a command-line interface, sensible defaults, and tests. Please research current best practices for Python log parsing and CLI design before coding, and use that to shape the implementation and README.
```

### 851. D5_s983051_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for diagnosing CI failures from raw logs: emit a root-cause summary, cluster repeated errors, and generate a test plan with likely flaky tests vs real regressions. Use Click for the CLI and make the output human-readable plus JSON, with code in src/ and tests/ plus a README.md. No input files — the tool should accept pasted logs from stdin and I want the full implementation.
```

### 852. D5_s983053_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上问题的日志分析小工具，目标是把一堆服务日志里的错误和异常请求自动归类，输出一份可读的诊断报告，并且最好能顺手生成一个最小可用的命令行程序。你帮我把代码、测试和说明文档一起做出来，文件名你来定；实现前先查一下常见日志格式解析、结构化输出和 Python CLI 的最佳实践，别依赖任何现成输入文件，直接把核心功能从头写出来。
```

### 853. D5_s983069_en (domain=D5, difficulty=7)

```
We need to cut down the time our support team spends chasing down flaky deployment issues in our Kubernetes-based service, because every missed signal costs us customer confidence. Build a small from-scratch debugging tool that ingests plain text logs, spots likely failure patterns, and produces a clear human-readable incident summary plus a short test plan we can use before the next release. I want the actual code files for the tool and a README that explains how to run it, what it detects, and how to extend it. Please research the best current Python libraries and log-processing practices first, then build it so it is practical for a real internal workflow.
```

### 854. D5_s983078_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-analysis tool from scratch that can read plain-text Kubernetes app logs from stdin or a file, detect common failure patterns like retries, timeouts, and stack traces, and generate a clean incident summary with root-cause hints and a confidence score. Please research a couple of current best-practice Python libraries or parsing approaches first, then implement the tool, add tests, and include a short README with usage examples and design notes. No input files are needed from me — just build the code and the docs.
```

### 855. D5_s983086_en (domain=D5, difficulty=7)

```
Build a Python log-triage tool from scratch for Kubernetes incidents. I want `logtriage.py`, `triage_rules.yaml`, `tests/`, and a short `README.md` that shows how to use it on pasted logs and live tail output. It should detect likely root causes from mixed app/container logs, group repeated errors, flag deploy-related regressions, and print a concise incident summary plus suggested next checks.
```

### 856. D5_s983102_zh (domain=D5, difficulty=7)

```
我需要你从零做一个小型的日志排障工具，目标是给一个 Python 微服务项目用：它要能读本地应用日志，自动识别常见错误模式、按时间线聚合关联日志、生成一份可读的故障摘要，还要带一个命令行入口和一套测试。请你顺手查一下现在比较稳妥的 Python 日志解析/正则/CLI 方案和最佳实践，最后把代码、README、测试都补齐，最好还能说明怎么扩展到 JSON 日志和多文件日志。
```

### 857. D5_s983110_en (domain=D5, difficulty=7)

```
Build me a from-scratch Python log triage tool for Kubernetes incident debugging. I want a CLI that ingests plain text logs from stdin or a file, clusters repeated errors, detects likely root-cause patterns, and emits a concise incident summary plus a JSON report. Put the code in app.py, tests in test_app.py, and a short README.md with usage examples.
```

### 858. D5_s983115_en (domain=D5, difficulty=7)

```
I need you to build a small Python tool from scratch that helps debug production logs: it should parse mixed JSON/text logs, detect common error patterns, correlate repeated stack traces, and produce a compact incident summary plus a CLI for filtering by time, service, and severity. Please research a couple of good Python libraries and current best practices for log parsing/CLI design before coding, then give me the finished code files and a short README with usage examples.
```

### 859. D5_s983128_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering teams make sense of API incidents faster. Right now, people paste logs into chat and waste time guessing whether a failure is a real outage, a client mistake, or a retry storm. I want you to build this from scratch as a lightweight command-line utility that can read raw logs we paste into it, group the related events, and produce a clear incident summary with likely root-cause hints, timing, and suggested next steps. Please research current best practices for log parsing and incident triage, and base the design on sensible, modern Python libraries or approaches. I want the finished code and a short README so another engineer can run it and understand it without help.
```

### 860. D5_s983151_en (domain=D5, difficulty=7)

```
I need you to build a small log-debugging tool from scratch that can take raw application logs pasted into stdin, detect common failure patterns, group related lines into incidents, and print a clean triage summary with probable root-cause hints. Make it a real CLI package with the source code, tests, and a short README, and research a couple of solid Python parsing/logging best practices plus one or two existing libraries so the design is sensible before you implement it.
```

### 861. D5_s983158_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for our Kubernetes services: implement `logtriage.py`, `anomaly_rules.py`, `tests/`, and a short `README.md`. It should parse multiline JSON and plain-text logs, detect spikes in error rate, deduplicate repeated stack traces, and emit a ranked incident summary plus a machine-readable JSON report. Use current best practices from real logging/regex/argparse docs and common incident-analysis guidance.
```

### 862. D5_s983166_en (domain=D5, difficulty=7)

```
I want you to build a from-scratch Python tool for debugging and log analysis that helps a team triage flaky CI failures in GitHub Actions.
- Create a CLI that ingests plain-text job logs pasted into stdin and extracts the failing step, the first error line, and a short root-cause summary.
- Add a small rules engine for common patterns like timeout, dependency install failure, test assertion failure, and permission/auth errors, with clear confidence scoring.
- Include a test plan and automated tests for the parser, pattern matching, and CLI behavior.
- Research current best practices for GitHub Actions logs, Python CLI packaging, and robust regex/log parsing, then implement the tool from scratch with no starter files.
- Deliver the code and a concise README explaining how to run it, extend the rules, and interpret the output.
```

### 863. D5_s983173_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上问题的日志分析小工具，目标是给一组服务日志自动提取错误模式、按时间线聚合、生成可读的排障摘要，并提供一个命令行入口和一套可跑的测试。项目里不要依赖现成数据文件，自己把示例日志和测试用例构造出来；实现前先查一下当前比较稳妥的 Python 日志解析、CLI 参数处理和测试最佳实践，再开始写代码。最后把完整代码、README 和测试都补齐。
```

### 864. D5_s983179_en (domain=D5, difficulty=7)

```
I need a small but real debugging/log-analysis tool built from scratch for our on-call workflow.

- Build a Python CLI that ingests application logs from stdin or a pasted text block and surfaces the most likely root-cause events with timestamps, severity, and surrounding context.
- Include support for a few common log formats we actually see: plain text, JSON lines, and Python-style stack traces; it should group related lines into one incident and rank candidates by confidence.
- Add a test suite with realistic synthetic logs, plus edge cases for malformed lines, multiline exceptions, and mixed formats.
- Use current best practices from existing libraries/docs where helpful, but implement the parsing, grouping, and ranking logic yourself from scratch.
- Also include a short README with usage examples and a note on how to extend the parser for a new format.

```

### 865. D5_s983188_zh (domain=D5, difficulty=7)

```
我们现在要把客服和线上事故排查做得更快一些，减少工程师来回翻日志、手动对时间线的情况。我需要你从零开发一个小工具，专门帮助我们把一段服务日志自动整理成可读的故障时间线，并且能指出可疑的错误链路。请你先自己查一下常见的日志解析和命令行工具最佳实践，选一个合适的实现方案，然后直接把代码、测试和使用说明都做出来。

我希望这个工具是命令行程序，能接收标准输入里的日志文本，按时间排序后输出事件摘要；如果日志里有请求 ID、级别、服务名、错误信息，也要尽量识别出来，合并成一条清晰的排障记录。最好还能支持一个简单的“过滤关键字”和“只看错误/警告”的模式，方便值班同学快速缩小范围。请你把核心解析逻辑、命令行接口、测试用例和 README 都一起做好，保证别人拿到后可以直接跑起来用。

另外，这个任务不要依赖现成的样例文件；你需要从零设计日志格式兼容性和测试策略，自己决定实现细节，但要尽量考虑真实线上日志常见的几种写法。最后把能运行的代码和说明文件交给我。
```

### 866. D5_s983193_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool that turns application logs into incident-ready debugging artifacts. I want a small CLI that ingests plain-text logs from stdin or a file path, detects common failure patterns across structured and unstructured lines, groups related events into incidents, and emits a JSON summary plus a human-readable Markdown report. The implementation should include a configurable parser for JSON logs and classic text logs, timestamp normalization, stack-trace stitching, severity classification, duplicate suppression, and basic root-cause hints based on pattern rules. Use current best practices for log parsing and CLI design, and verify any library/API choices with web research before coding. Deliver the built code and a README with usage examples, design notes, and test instructions.
```

### 867. D5_s983198_en (domain=D5, difficulty=7)

```
I need you to build a small Python log triage tool from scratch for debugging Kubernetes-style app logs: it should parse JSON and plain-text lines, detect common error patterns, group repeated exceptions, and print a concise incident summary with likely root-cause hints and a severity score. Please put the code and a short README in the repo, and use web research to pick the best lightweight parsing/logging libraries and follow current best practices for CLI UX and structured logging.
```

### 868. D5_s983201_zh (domain=D5, difficulty=7)

```
我们现在要把线上事故排查做得更快一些：每次服务出问题，日志、错误堆栈和时间线都散在各个地方，工程师要手工翻很久。我想从零做一个轻量的命令行工具，专门用来读取本地日志文本，自动帮我们整理出可读的故障摘要、按时间顺序串起关键事件、提取重复报错，并给出一个简单的排查建议。你帮我把这个工具直接做出来，最好顺手把用法说明和测试也一起补齐；如果你觉得合适，也可以查一下现成的 Python 标准库/常用库怎么做日志解析、命令行参数和输出格式最稳妥，但最终代码要我们自己完整实现，不要依赖现成成品工具。我要的是能交付的代码文件和说明文档，而不是只给我思路。
```

### 869. D5_s983213_en (domain=D5, difficulty=7)

```
We need a small internal troubleshooting tool that helps our support team turn messy application logs into clear incident notes fast, because right now they spend too long guessing what went wrong and writing updates by hand. Please build it from scratch as a real working command-line tool that can scan logs, spot likely error patterns, group related lines into a single incident, and produce a clean summary with likely root causes and next steps. I want the finished code and a short README so another engineer can run it and understand how it works. Please also check current best practices for log parsing, pattern matching, and command-line tool design before building it.
```

### 870. D5_s983226_zh (domain=D5, difficulty=7)

```
帮我从零实现一个用于排查微服务日志问题的小工具，目标是把一组文本日志快速整理成可读的故障分析结果。
- 希望支持常见日志格式（比如带时间戳、级别、服务名、trace_id 的行），能按时间窗口聚合相关日志。
- 需要能识别并高亮几类典型异常：错误堆栈、超时、重试风暴、请求链路中断、同一 trace_id 的跨服务关联。
- 最好做成一个命令行工具，输入原始日志文本或从 stdin 读取，输出一份结构化摘要和可读报告。
- 请顺手补上单元测试和一份简短的 README，说明如何安装、运行、以及它适合解决什么问题。
- 设计时参考一下现成日志解析和 CLI 方面的最佳实践，但实现必须是你从头写的，不要依赖现成成品直接替代核心逻辑。
```

### 871. D5_s983232_zh (domain=D5, difficulty=7)

```
帮我从零做一个 Python 诊断工具，文件名先按 `log_triage.py` 和 `README.md` 来。目标是给 SRE/后端排障用：它要能读一段服务日志，自动识别常见异常模式、聚合相邻错误、按严重级别输出摘要，并给出可执行的排查建议。你先查一下 Python 标准库/常用日志处理最佳实践，再直接实现代码、测试和使用说明，别留空壳。
```

### 872. D5_s983255_zh (domain=D5, difficulty=7)

```
给我从零做一个 Python 命令行工具，专门做生产日志/报错的“根因定位助手”：输入一段服务日志或一条 stack trace，自动提取关键信号、归类常见异常模式、给出排查建议，并输出 JSON 和人类可读摘要。把代码放在 `src/`，补齐 `tests/`、`README.md`，顺手写一个 `examples/` 里的最小用例。先查一下现成库和最佳实践再设计实现，但代码本身要自己写，不要依赖现成同类工具直接拼装。
```

### 873. D5_s983257_en (domain=D5, difficulty=7)

```
I need you to build a small incident-log triage tool from scratch for Kubernetes workloads: something that can ingest raw container logs, detect common crash-loop and timeout patterns, correlate them with recent pod events, and output a short diagnosis summary plus suggested next steps. Please research current best practices and any relevant Python libraries or Kubernetes APIs first, then produce the code and a README for running it locally; no input files are provided, so include a clean sample-data generator or fixtures in the repo.
```

### 874. D5_s983261_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering teams make sense of flaky production incidents faster. I want you to build it from scratch so we can paste in app logs from a deployment or outage and get a clean incident report with probable error clusters, timeline, and a short summary of what changed. Please research the best practical approach first using current docs for a couple of modern Python log parsing / text clustering libraries and any good guidance on handling time-based log timelines, then implement the tool yourself. I want the finished code and a short README with how to run it locally, plus tests so we can trust it. No input files should be required; the tool should work from pasted log text or standard input.
```

### 875. D5_s983267_zh (domain=D5, difficulty=7)

```
给我从零做一个 Node.js 的日志告警小工具，文件名就按你定：先实现核心库、命令行入口和测试，再补一个 README。它要能解析结构化/非结构化日志，按规则做错误聚合、去重、速率统计和阈值告警，最好顺手支持 tail/follow 模式。
```

### 876. D5_s983273_en (domain=D5, difficulty=7)

```
We need to cut down the time our support team spends chasing down server issues, so I want a small tool built from scratch that turns messy application logs into a simple incident summary. Please create a real working utility for our engineering team that can read plain-text logs, detect common error patterns, group related events into one incident, and produce a clear summary with timestamps, likely root-cause clues, and a short timeline. I also want a command-line version people can run locally, plus a small test suite so we can trust it before rolling it out. Please use current best practices and check existing Python libraries or approaches for log parsing and CLI design before you build it, then deliver the code and the README.
```

### 877. D5_s983285_zh (domain=D5, difficulty=7)

```
我们最近在排查生产环境里的接口超时和偶发错误，团队每次都要手工翻日志，效率很低，也很难统一判断问题优先级。我想从零做一个小工具，帮助我们把一段服务日志快速整理成可读的故障摘要，能自动识别常见错误类型、按时间线串起来、标出可疑的异常峰值，并给出下一步排查建议。你先帮我调研一下适合在本地运行的实现方式和常见库的最佳实践，然后直接把这个工具做出来。

我希望最终交付的是一套可直接运行的代码，而不是写方案。工具最好有命令行入口，支持输入一段文本日志或从标准输入读取，输出一份结构清楚的分析结果；如果你觉得有必要，也可以补一个简单的本地 API。请把核心分析、日志解析、错误分类、测试和使用说明都一起做好，保证别人拿到就能跑、能测、能改。
```

### 878. D5_s983296_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps us triage production incidents faster by turning raw service logs into a readable incident summary and a suggested next step. I want you to design and build it from scratch, because our team keeps losing time scrolling through logs during outages. Please make it a real, usable command-line tool for engineers, with a clear setup guide and tests. Use current best practices and check the latest guidance for any libraries or patterns you choose, because I want this to be something we could actually adopt. Deliver the built code and a README, and make sure it can run locally without any input files by accepting logs from standard input or a pasted string.
```

### 879. D5_s983317_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-triage tool from scratch for our backend team: read streamed app logs from stdin, detect likely incidents, group related lines by request/session, and output a clean incident summary plus a CLI we can use locally. Please research the best lightweight Python libraries and current patterns for CLI parsing, structured logging, and regex-based parsing before coding, then give me the finished code and a short README that explains how to run it, tune the rules, and interpret the output.
```

### 880. D5_s983320_en (domain=D5, difficulty=7)

```
We keep losing time when production incidents happen because the logs are messy, the team has no quick way to trace one request across services, and our current scripts are too brittle to trust. I want a small internal tool built from scratch that helps us debug incidents faster by reading plain text application logs, grouping events by request ID, flagging likely errors, and producing a clear summary we can share in Slack or a ticket. Please design and build the code for it, with a simple command-line interface, solid tests, and a short README that explains how to run it and how the logic works. I do not have any input files for you — please create the solution from scratch and use your judgment on the best approach.
```

### 881. D5_s983327_zh (domain=D5, difficulty=7)

```
给我从零做一个 Go 的日志故障排查小工具，代码和 README 一起交付，文件名就叫 `logtriage.go` 和 `README.md`。它要能同时解析多行 JSON 和纯文本日志，按时间线聚合错误、提取关联 request_id/trace_id，并输出一份可读的排障摘要，还要附带一个最小化的测试方案说明。
```

### 882. D5_s983329_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上问题的小工具：做成一个本地可运行的 Python 命令行程序，能把应用日志里的异常栈、请求 ID、时间线和关键错误自动串起来，输出一份可读的故障摘要，并支持按服务名、级别、时间范围过滤；同时给我一份 README 说明安装、用法和排障思路。这个项目不要依赖现成样例数据，代码和测试都要你自己写，最好参考一下现有的日志解析和 CLI 设计最佳实践，再决定用哪些标准库或第三方库。请直接把最终代码文件和文档文件整理好。
```

### 883. D5_s983332_zh (domain=D5, difficulty=7)

```
我们最近在排查线上故障时，日志太散、告警太多，排查时间经常拖很久，影响客户问题恢复。我想从零做一个轻量的内部工具，帮我们把应用日志和告警事件快速归类、定位异常链路、并生成一份适合值班同事直接看的排障摘要。请你自己先做一点网页调研，看看现在常见的日志结构化、异常聚类、时间线拼接和命令行工具设计有哪些成熟做法，再基于这些思路从头实现一个可运行的小工具，不要依赖现成模板或我提供的数据文件。最终请直接交付代码和说明文档，最好能让我在本地一条命令跑起来验证。工具里希望至少能支持：读取标准输入或指定文本日志，识别错误/警告/超时等关键事件，按请求ID或时间窗口把相关日志串起来，输出简洁的故障摘要，并给出可操作的排查建议。另请把测试计划和核心测试也一并做好，确保后续我们能扩展到接入更多日志格式。
```

### 884. D5_s983352_en (domain=D5, difficulty=7)

```
Build a small Python log-triage tool from scratch for Kubernetes and NGINX incident debugging. I want `log_triage.py`, `tests/`, and a short `README.md` that explains how to use it against pasted logs, with no input files required. Use current best practices from the web for log parsing, regex safety, and CLI design, then implement a CLI that classifies errors, groups repeated stack traces, and suggests likely causes.
```

### 885. D5_s983383_en (domain=D5, difficulty=7)

```
Build a from-scratch log triage tool for our engineering team that can ingest raw app logs, detect likely incident patterns, and produce a readable summary for debugging.

- I want a small Python package plus a CLI I can run locally against pasted log text or stdin.
- Include pattern detection for common failure modes like stack traces, repeated error bursts, timeouts, auth failures, and dependency outages.
- Add a concise report format with severity, likely root-cause hints, and a timeline of notable events.
- Use current best practices from the web for Python CLI design and log parsing libraries, but implement the core logic ourselves.
- Include tests and a short README with usage examples and extension points.
```

### 886. D5_s983389_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上服务日志的 Python 小工具，目标是把一段原始文本日志解析成结构化结果，支持按时间范围、级别、request_id 和关键词过滤，还能自动把异常栈、重复错误和慢请求汇总成一份排障报告。你直接把代码和说明文件都写出来，最好做成一个可安装运行的命令行工具，顺手补上测试、示例用法和 README；实现前先查一下 Python 标准库/常用日志解析和命令行库的最佳实践，避免我后面再返工。
```

### 887. D5_s983410_en (domain=D5, difficulty=7)

```
Build a small Python log-triage tool from scratch: `logtriage.py` plus `README.md`. It should ingest raw app logs from stdin or a pasted string, detect common failure patterns, cluster repeated stack traces, and emit a concise incident summary with likely root-cause hints and top error signatures. Use web research for best-practice log parsing/stack-trace normalization and any lightweight libraries you’d recommend before coding.
```

### 888. D5_s983435_en (domain=D5, difficulty=7)

```
Build a from-scratch log triage tool for our SRE workflow: create a Python CLI called `logtriage` with `src/`, `tests/`, and `README.md`. It should ingest plain-text app logs from stdin or a file path, parse common formats, detect error clusters, and output a concise incident summary plus suggested next checks. Use web research for Python logging/parsing best practices and any library choices, then implement it cleanly with tests.
```

### 889. D5_s983441_zh (domain=D5, difficulty=7)

```
我们现在想把线上故障排查变得更快一些，减少客服和工程师来回找日志的时间，所以我希望你从零做一个轻量的“日志检索与故障定位”小工具。它要能把一段服务日志里的报错、请求链路和关键上下文整理出来，支持按时间范围、错误级别、请求ID去筛选，并且能输出一份便于排查的摘要。请你先查一下现在常见的做法和合适的开源库，再直接把这个工具做出来，最好带上使用说明和测试。不要依赖现成的数据文件，全部从代码开始搭建；如果你觉得有必要，可以顺手把命令行界面和核心逻辑分开，方便以后接到别的系统里。最后把代码、测试和简短说明一起给我。 
```

### 890. D5_s983446_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called `logsentinel` for debugging and log analysis of Kubernetes-style JSON logs. I need `logsentinel.py`, `tests/`, and a short `README.md` showing install and usage. Research current best practices for structured logging, severity parsing, and regex-safe anomaly detection before you code, then implement the tool with a CLI that can summarize logs, flag likely root-cause candidates, and export a test plan report.
```

### 891. D5_s983455_en (domain=D5, difficulty=7)

```
I want a small but real developer tool built from scratch for debugging and log analysis.
- Build a command-line log triage utility for Kubernetes-style JSON logs that can detect repeated errors, noisy spikes, and probable root-cause chains across related entries.
- Use current best practices and a couple of existing libraries/docs only as design references, then implement the tool yourself with no starter code or input files.
- Include a clear CLI, sensible defaults, and an output mode for both human-readable summaries and machine-readable JSON.
- Add solid tests for parsing, grouping, ranking, and edge cases, plus a short README with usage examples and design notes.
- I need the actual code files, not just a description.
```

### 892. D5_s983463_en (domain=D5, difficulty=7)

```
I need you to build a small log-diagnostic tool from scratch for Kubernetes-style app logs: a Python package plus a CLI that can ingest plain text log lines, detect common failure patterns, cluster related errors, and generate a short incident summary with likely root-cause hints. Please research a couple of current Python libraries or approaches for parsing logs and CLI ergonomics before coding, then implement the tool, add tests, and include a README with usage examples. There are no input files — just create the code and docs.
```

### 893. D5_s983481_en (domain=D5, difficulty=7)

```
Build a from-scratch Python 3.12 troubleshooting toolkit for our on-call workflow that ingests application logs from stdin or a pasted multiline string, normalizes timestamps from common formats, clusters related error lines into incidents, and generates a concise incident summary with probable root-cause signals and recommended next debugging steps. I want a real working codebase, not a prototype: include the core parser/clusterer, a small CLI, and a regression test suite. Use current best practices for log parsing and CLI ergonomics, and research any useful libraries or standard-library approaches before coding. No input files are provided; design the system and implement it from scratch. Deliver the code files and a README.
```

### 894. D5_s983486_en (domain=D5, difficulty=7)

```
I need you to build a small Python command-line tool from scratch that helps me debug service logs by grouping related events into incidents, spotting likely root-cause lines, and generating a clean markdown report I can share with the team. Please include the code, a short README, and tests, and use current best-practice docs for any logging/parsing libraries or CLI patterns you choose so the design is sensible and up to date.
```

### 895. D5_s983491_en (domain=D5, difficulty=7)

```
I want a from-scratch internal tool for debugging our service logs and building test plans around failures.

- Build a small CLI app that can ingest raw application logs from stdin or a pasted string, group related errors, and summarize likely root causes.
- Include a rule-based parser for timestamps, levels, request IDs, stack traces, and retry patterns, plus a few heuristics for spotting noisy duplicates and cascading failures.
- Add a mode that turns the analysis into a concise incident report and a separate mode that generates a test plan with edge cases and regression checks.
- Research a couple of current Python libraries and logging best practices first, then implement the tool from scratch with no starter files.
- I want the code, tests, and README delivered in a small repo layout that I can run locally.
```

### 896. D5_s983495_zh (domain=D5, difficulty=7)

```
帮我从零做一个 Python 3.12 的日志/故障排查工具，文件就按 `logtriage.py`、`tests/` 和 `README.md` 来写。它要能把一段服务日志做结构化解析、按错误类型聚类、输出可读的排障摘要，并支持 CLI：`scan`、`group`、`explain`、`export` 四个子命令。顺手查一下 `argparse`、`rich`、`orjson` 和常见 Python 日志格式/最佳实践，按查到的方案实现，不要用现成项目骨架。
```

### 897. D5_s983506_zh (domain=D5, difficulty=7)

```
从零做一个 Python 诊断工具，项目里输出这些文件：app.py、log_triage.py、README.md、tests/test_app.py。工具要能解析应用日志里的异常栈、按错误模式聚类、给出可能根因和排查顺序，顺手提供一个 CLI，支持输入日志文本、设定时间窗口、导出 Markdown 报告。先查一下 Python 标准库/现成库里做日志解析、栈追踪提取、相似度分组和 CLI 参数解析的最佳实践，再开始实现。
```

### 898. D5_s983527_zh (domain=D5, difficulty=7)

```
我想从零做一个用于排查生产问题的日志分析小工具，最好能直接在本地跑起来。
- 用 Python 做一个命令行工具，支持按时间窗口、级别、服务名、request_id 过滤日志，并把相关事件串成一条可读的故障时间线。
- 需要支持常见日志格式：纯文本、JSON line、以及带堆栈信息的多行异常；输出里要能提取关键信息、聚合重复错误、给出初步根因线索。
- 请先调研一下 Python 里适合做日志解析/命令行/表格输出的主流库和最佳实践，再决定实现方案，但最终代码要自己从头写，不要套现成项目。
- 希望你把代码、测试和使用说明一起交付，最好还有一份简短的设计说明，解释解析策略、边界情况和如何扩展。
- 如果你觉得有必要，也可以顺手补一个最小的示例命令和几组单元测试，方便我直接验证。
```

### 899. D5_s983532_zh (domain=D5, difficulty=7)

```
从零写一个 Python 3.12 的日志诊断工具，做成 CLI：能读 stdout/stderr 文本流，自动识别常见错误模式（Python traceback、Java stack trace、nginx/Go/TLS/timeout/oom 之类），输出带严重级别的摘要、聚类后的重复告警、以及一份可直接贴到工单里的诊断建议。请生成 app.py、tests/、README.md，顺手把参数设计、输出格式和边界行为都定好。别用示例输入文件，直接把工具和测试都写出来。
```

### 900. D5_s983536_en (domain=D5, difficulty=7)

```
We keep losing time every time an incident comes in because the logs are spread across services and the team has to piece together what happened by hand. I want a small internal tool we can actually use to turn raw application logs into a readable incident timeline, highlight likely errors, and generate a short debugging summary for non-specialists. Please build it from scratch as a real code project, not a mockup, and make it something we can run locally with a simple command. I also want you to research the best lightweight libraries and current logging patterns first, then use that to design the tool properly. Deliver the code and a short README that explains how to run it and what it does.
```

### 901. D5_s983539_en (domain=D5, difficulty=7)

```
I want a small but real internal developer tool built from scratch for debugging production logs and flaky tests.
- Build a command-line app that can ingest raw text logs pasted into stdin and flag likely root causes using rules you design.
- Include a compact rules engine so I can add patterns for retries, timeouts, rate limits, null pointers, and dependency failures without editing code.
- Add a test runner helper that summarizes flaky-test signals from log snippets and exits with a useful status code for CI.
- Research a couple of current Python libraries or standard approaches for CLI parsing, pattern matching, and colored terminal output before you implement.
- Ship the code plus a short README with usage examples, design notes, and how to extend the rules.
```

### 902. D5_s983551_en (domain=D5, difficulty=7)

```
I want a from-scratch build for an internal observability/debugging tool that helps engineers analyze application logs and catch regression patterns before release.

- Build a small Python 3 command-line app that can ingest plain-text logs, detect common error spikes/anomalies, and summarize likely root-cause signals.
- Include a sensible rules engine for parsing timestamps, levels, request IDs, and repeated exceptions, plus a report that highlights the top suspicious sequences.
- Add a test suite and a few example commands so I can run it locally and validate the behavior end to end.
- Use current best practices and existing Python libraries where helpful, but implement the core analysis logic yourself.
- Make the output practical for engineers: clear CLI help, readable summaries, and a compact JSON export for automation.
```

### 903. D5_s983555_en (domain=D5, difficulty=7)

```
Build a from-scratch log triage tool for Kubernetes incidents: I want a Python CLI named `klogtriage` with `parse`, `summarize`, `detect`, and `export` commands, plus a small `README.md` and `tests/` suite. Use web research for the current best practices around Kubernetes JSON logs, Python logging/parsing libraries, and CLI packaging, then implement the code in `src/` with no starter files.
```

### 904. D5_s983562_en (domain=D5, difficulty=7)

```
I want a small from-scratch observability tool for debugging flaky services in Python.
- Build a log-anomaly CLI that reads live or pasted logs, groups repeated stack traces, and flags new error signatures.
- Use current best practices from the Python logging ecosystem and a few relevant libraries/APIs after checking the web.
- Include a lightweight rule engine for severity scoring plus a human-readable summary report.
- I need the actual code, tests, and a short README with install/run examples.
- Please make it easy to extend later for JSON logs and plain-text logs.
```

### 905. D5_s983570_en (domain=D5, difficulty=7)

```
I need you to build a small Python debugging tool from scratch that scans application logs and flags likely root-cause patterns for failed jobs, then ships with a CLI, a test suite, and a short README. Make it work on plain text logs with timestamps, levels, request IDs, stack traces, and retry messages; I want it to group related lines into incidents, infer common failure signatures, and print a concise summary plus a JSON report. Please research the best-fit Python libraries and log-format handling first, then create the code files and tests.
```

### 906. D5_s983585_zh (domain=D5, difficulty=7)

```
我们最近要把线上服务的排障效率提上来，尤其是接口变慢、错误率升高、日志里信息太散的时候，值班同事现在很难快速判断“先看哪里、怎么定位、要不要升级处理”。我希望你从零做一个小工具，专门帮我们把应用日志里的关键线索整理成清晰的排障结论，最好能直接用于团队日常值班。

请你直接做出这个工具的代码，不要用现成模板。这个工具需要支持命令行运行：可以读取一段原始日志文本，自动识别常见问题类型（比如超时、重试过多、数据库连接异常、外部接口失败、权限错误），输出一份结构化的排障摘要；同时要能生成一份简短的测试方案，说明它有哪些典型日志场景、怎么验证结果对不对。最好再补一份 README，写清楚怎么安装、怎么运行、有哪些限制。

我不提供任何输入文件，你需要自己把处理逻辑、错误处理、测试和文档都搭起来。实现前请你查一下现在常见的 Python 日志处理和命令行工具写法，选一个稳妥的方案再开始做。
```

### 907. D5_s983598_zh (domain=D5, difficulty=7)

```
帮我从零做一个用于排查线上问题的日志分析工具，目标是把一段原始应用日志快速整理成“可读的故障摘要”。
- 要支持常见的 Java / Python / Node.js 风格日志格式，能识别时间、级别、线程/进程、请求 ID、异常堆栈和重复报错。
- 希望提供一个命令行工具，能读 stdin 或本地日志文件，输出按时间排序的事件流、错误聚类、Top N 异常，以及一份适合贴到工单里的简明报告。
- 需要你顺手补上单元测试和一份 README，说明安装、用法、支持的日志模式和已知限制。
- 如果你觉得更合适，也可以设计成一个小型 Python 包，但核心解析、聚类和报告生成都要自己实现，不要依赖现成的日志分析平台。
- 先做一些必要的 web 调研再开工，看看 Python 标准库/常用库里有哪些适合做日志解析、命令行参数和 ANSI 彩色输出的最佳实践。
```

### 908. D5_s983604_zh (domain=D5, difficulty=7)

```
从零做一个 Python 工具，帮我们定位线上服务日志里的“超时/重试风暴”根因。请产出 `logtriage.py`、`README.md` 和一套最小但完整的 `tests/`，支持解析多行日志、按请求链路聚合、识别异常峰值、输出可读报告。顺手查一下 Python 标准库/常用库里适合做 CLI、日志解析和时间窗口统计的最佳实践，再把你采用的方案写进 README。
```

### 909. D5_s983615_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for our on-call workflow: create `logtriage/` plus `pyproject.toml`, `README.md`, and tests. I need a CLI that ingests plain-text app logs from stdin or a file, detects common failure patterns, groups related lines into incidents, and prints a ranked summary with timestamps, signatures, and suggested next checks.

Use web research first for current best practices and library choices, then implement it cleanly with no starter data or files.
```

### 910. D5_s983618_zh (domain=D5, difficulty=7)

```
我需要你从零做一个面向工程排障的“小型日志诊断工具”，目标是能读取应用运行日志后自动识别常见故障模式（比如超时、重试风暴、数据库连接耗尽、Nginx 5xx 激增），输出一份结构化诊断报告，并附带一个可本地运行的命令行工具和测试集。你先做设计和实现，代码文件、README 和测试都要给我；如果需要选型，就自己查一下 Python 标准库、click/typer、regex、JSON 输出格式、以及日志分析最佳实践后再定方案。
```

### 911. D5_s983627_zh (domain=D5, difficulty=7)

```
从零做一个 Python 命令行工具，叫 logtriage，用来分析服务日志、自动聚类错误、定位疑似根因并输出排障建议。请直接给我完整代码和 README.md，包含可运行的 CLI、日志解析器、聚类/规则引擎、测试和示例用法；不要用任何现成项目骨架。
```

### 912. D5_s983639_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for Kubernetes incidents: parse mixed JSON/plaintext app logs, detect error bursts and correlated trace IDs, and generate a ranked incident summary plus recommended next checks. Put the code in `src/`, tests in `tests/`, and a short `README.md` with usage and design notes; no input files, just ship the code.
```

### 913. D5_s983643_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-triage tool from scratch that helps debug flaky test runs by parsing raw CI logs, spotting common failure patterns, and generating a concise incident summary with suggested next steps. Please include the code files, a README, and a solid test suite; there are no input files to start from, so make it self-contained. Use web research where helpful to check current best practices for Python log parsing, regex handling, and CLI design, then implement the actual tool from scratch.
```

### 914. D5_s983645_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering teams make sense of messy app logs when a customer reports an outage. I want a from-scratch command-line utility that can read plain text logs, detect likely error spikes, group related messages, and produce a short human-readable incident summary we can paste into Slack. Please build the code and supporting files, and make it practical enough that a non-engineer could run it with a simple command and get a useful report. Use web research first to choose a good lightweight parsing library and a sensible approach for log pattern matching and timestamp handling, then implement it cleanly from scratch with tests and brief usage notes.
```

### 915. D5_s983647_zh (domain=D5, difficulty=7)

```
我想从零做一个用于工程排障的命令行工具，重点是分析应用日志、快速定位错误模式，并生成可执行的排查建议。
- 先帮我调研并选型：Python 里适合做日志解析、模式匹配和高亮输出的主流库/做法，最好结合官方文档和近年的最佳实践。
- 直接实现一个可运行的 CLI 工具，支持读取本地日志文本，识别常见问题类型（如异常堆栈、超时、重试风暴、5xx 激增、连接失败），并输出结构化摘要。
- 需要有一个“规则引擎”模块，后面方便继续扩展新规则；同时给出清晰的模块划分和注释。
- 帮我补一套测试方案并实现关键单测，覆盖正常日志、混合日志、乱码/空行、无匹配、以及多种错误同时出现的情况。
- 最后整理一份简短 README，说明安装、用法、输出格式和设计思路，最好也提一下你参考了哪些文档或库。
```

### 916. D5_s983654_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上故障的小工具，最好是一个 Python 3.11 的命令行项目，能把服务日志里的错误堆栈和关联请求串起来，自动提取时间线、按 trace_id/request_id 聚合、输出可读报告，并且带一套可跑的测试和使用说明；你先自己查一下现成库和最佳实践，选合适的方案后直接把代码、测试和 README 一起做出来。
```

### 917. D5_s983665_en (domain=D5, difficulty=7)

```
I need you to build a small from-scratch Python troubleshooting tool for log analysis and incident debugging that can take raw app logs pasted into stdin or a string and turn them into a structured incident summary, with anomaly detection, error clustering, and a short triage report. Please research current best practices and a couple of solid Python libraries or approaches for parsing timestamps, fuzzy matching stack traces, and output formatting, then implement the code, a CLI, and tests in separate files, plus a README that explains how to run it and how the detection logic works. There are no input files — just build the tool and make it usable on real logs from modern Python services.
```

### 918. D5_s983674_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called `logtriage` for debugging production logs: it should ingest raw text logs from stdin or a file, detect common incident patterns, cluster similar errors, and emit a ranked triage report plus JSON output. I want `logtriage.py`, `tests/`, and a short `README.md` with usage examples and assumptions.

Research the best-fit parsing/clustering libraries and current Python logging best practices first, then implement the tool cleanly.
```

### 919. D5_s983681_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering teams make sense of incident logs faster. Build it from scratch so we can paste in raw logs, flag likely error patterns, and generate a short triage summary with next-step suggestions. It should be practical enough for our team to run locally, not a demo. Please research the best lightweight Python libraries for parsing logs and making a simple command-line workflow, then build the tool and include clear setup and use instructions. I want the finished code files and a short README, with tests that show it works on a few realistic log examples.
```

### 920. D5_s983702_en (domain=D5, difficulty=7)

```
I need you to build a small but real log-debugging tool from scratch that can ingest plain-text app logs, detect likely root causes from common crash patterns, and output a concise incident summary plus a recommended next-check list. Please implement the code, a CLI, and tests, and include a short README showing how to run it. I want it to be useful for modern Python services and to follow current best practices for parsing, structured logging, and error classification.
```

### 921. D5_s983708_en (domain=D5, difficulty=7)

```
I want a small but real incident-debugging tool built from scratch for a Kubernetes-based service.
- Build a command-line app that can ingest app and cluster logs, detect likely root-cause patterns, and produce a readable incident summary.
- Include support for at least a few common failure modes like crash loops, readiness probe failures, OOM kills, and upstream timeout patterns.
- Add a test suite with representative synthetic logs and edge cases, plus a short README showing how to run it locally.
- Use current best-practice docs for log parsing, CLI design, and any relevant Python or Go libraries, then implement the code yourself.
- I only want the code/files and docs, not a conceptual writeup.
```

### 922. D5_s983720_en (domain=D5, difficulty=7)

```
I want a small but real internal debugging tool built from scratch for our incident-response workflow.

- Build a command-line utility that parses application logs, groups repeated stack traces, and highlights likely root-cause patterns.
- Include a lightweight rules engine for detecting common issues like connection pool exhaustion, timeout storms, and memory pressure from text logs.
- Add a test suite with realistic synthetic log examples and edge cases so we can trust the grouping and detection behavior.
- Document how to run it locally, how the detection rules work, and how to extend it with new patterns.
- Use current best practices and a sensible Python library choice for log parsing / CLI / testing after checking the web first.
```

### 923. D5_s983729_zh (domain=D5, difficulty=7)

```
我需要你从零做一个小工具：给 Sentry / OpenTelemetry / 普通应用日志都能用的“错误日志聚类与排障助手”，要求你直接产出可运行的代码和 README，不要用现成模板。这个工具要能读一段 JSON Lines 日志，自动把同类报错聚成组，抽取关键信息（异常类型、消息、堆栈首尾行、服务名、请求路径、版本号），再生成一份可读的排障摘要，还要带一个命令行入口、一个最小的 HTTP 接口，以及一套完整测试。实现前请先查一下 Python 里做日志解析、文本相似度/聚类、CLI 框架和测试的常见最佳实践，优先用成熟库但核心逻辑自己写。最后给我代码文件、测试、README 和一个示例输出说明。
```

### 924. D5_s983790_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and engineering teams make sense of production logs faster, because right now every incident turns into a manual hunt through messy text. I want you to build a from-scratch log triage utility that can take pasted log lines, spot the most likely error patterns, group repeated messages, flag unusual spikes, and produce a short incident summary that a non-engineer can read. Please research a sensible approach first using current best practices and any relevant Python libraries or patterns for parsing, grouping, and summarizing logs, then build the tool from scratch with a clean command-line interface and clear usage notes. I do not have any input files for you; just create the code, tests, and a short README. The end result should be something we can run locally to analyze logs copied into stdin or passed as plain text.
```

### 925. D5_s983814_en (domain=D5, difficulty=7)

```
We need a small internal tool that helps our support and operations team make sense of service logs faster, because right now they waste too much time jumping between raw text, timestamps, and error codes. I want you to build this from scratch as a working command-line utility that can read pasted log text, spot likely incidents, group related lines, and produce a clear summary of what happened, the most common error patterns, and a short timeline. Please research the best current Python libraries and approaches first so the tool is sensible and easy to maintain, then implement the code, tests, and a short README explaining how to run it. There are no input files to start from; just build the tool and its docs.
```

### 926. D5_s983816_en (domain=D5, difficulty=7)

```
I want a from-scratch internal debugging tool for our Node.js services that turns application logs into an actionable incident report.
- Build a small CLI that ingests plain text logs, groups related errors, and highlights likely root-cause chains.
- Research a couple of good-fit parsing and terminal formatting libraries first, then pick one approach and justify it in the README.
- Include a compact rules engine for detecting retries, timeouts, dependency failures, and repeated stack traces.
- Add a test plan with realistic sample log scenarios and enough unit tests to prove the grouping and classification logic works.
- Deliver the code plus clear setup docs so another engineer can run it locally and extend it.
```

### 927. D5_s983833_zh (domain=D5, difficulty=7)

```
帮我从零写一个 Python 命令行工具，文件就放在 `logguard/` 里，核心是分析 Web 服务日志里的错误模式，输出可执行的排障建议。我要 `README.md`、`pyproject.toml`、`logguard/__main__.py`、`logguard/core.py`、`tests/`，并把依赖、CLI 参数、异常处理和测试都补齐。顺手查一下当前 `typer` / `rich` / `pydantic` 的最佳实践，再设计成能直接 `python -m logguard` 跑起来。别用示例数据文件，所有示例和测试数据都在代码里生成。
```

### 928. D5_s983986_en (domain=D5, difficulty=7)

```
I want a from-scratch Python tool that helps me debug production incidents by turning raw application logs into a concise incident timeline and an actionable triage summary. I am not asking for a notebook, a data-analysis report, or anything that depends on input files; I want the codebase itself built from scratch, with no starter dataset. The tool should accept pasted log text from stdin or a string argument, parse common structured and semi-structured formats, normalize timestamps and severity levels, group repeated messages into clusters, detect likely error bursts, and produce both a human-readable summary and a machine-readable JSON output.

Please design it as a small but real command-line utility with a clean library layer underneath it. I want the parser to handle at least these log shapes: RFC 3339 timestamps, ISO-8601 timestamps with timezone offsets, and timestamp-less lines that should be attached to the most recent timestamped entry when they are clearly stack-trace continuation lines or indented continuation lines. The severity detector should recognize standard levels such as DEBUG, INFO, WARN, WARNING, ERROR, FATAL, TRACE, and should gracefully mark unknown levels as UNK. Repeated identical messages within a short rolling window should be deduplicated into clusters with a count, first-seen time, last-seen time, and example line. Error bursts should be detected using a configurable sliding window and threshold, and the output should distinguish between ordinary repeated warnings and actual high-severity spikes.

I also want a compact incident timeline that preserves chronological ordering after timezone normalization, and a triage summary that highlights the top suspects: most frequent error signatures, earliest fatal/error event, highest burst window, and any lines that look like stack traces. The output should include stable message signatures computed from the normalized message text, ignoring volatile tokens like UUIDs, hex memory addresses, request IDs, and numeric counters where appropriate. I want that normalization strategy documented because I need deterministic grouping for tests and for later integration into alerting.

The CLI should support at least three commands: one that prints a plain-text summary, one that prints JSON, and one that runs a self-check or validation mode that verifies the parser on embedded examples and reports whether the core heuristics are behaving as expected. I also want explicit exit codes for success, parse warnings, and fatal failures. If you think a lightweight dependency is justified, keep it minimal and explain why in the docs, but I want the implementation itself to be fully built out, not a stub.

Please make sure the project is production-minded: include unit tests for parsing, normalization, clustering, burst detection, and CLI behavior; include a small README with usage examples and design notes; and include a short test plan that explains edge cases such as multi-line stack traces, mixed timezone offsets, malformed timestamps, repeated identical errors, and logs with no severity labels. I care about correctness and debuggability more than raw performance, but the code should still handle reasonably large pasted log blobs without quadratic behavior. I need the final deliverable to be the built code files and documentation, not a prose-only answer.
```

### 929. D5_s984006_en (domain=D5, difficulty=7)

```
We keep losing time when incidents happen because engineers have to jump between logs, metrics, and Slack just to figure out what failed and what changed. I want a small internal tool built from scratch that helps us quickly summarize a production incident from raw application logs and gives a clear, readable troubleshooting report. Please research the best practical approach first, then build the code and the basic docs.

What I need:
- A command-line tool that accepts pasted log text or stdin and turns it into an incident summary.
- It should detect the most common error patterns, group repeated messages, pull out timestamps, request IDs, and likely root-cause clues.
- It should generate a human-friendly report with sections like what happened, when it started, top error types, affected services, and suggested next checks.
- I want the tool to be configurable for different log formats we use across Node.js, Python, and Nginx.
- Please include a few realistic sample log snippets inside the code for testing and demonstration, but no separate input files.
- Also include tests so we can trust the output formatting and the main detection logic.

Please use web research where useful to choose a sensible implementation approach and any lightweight libraries that help with parsing or CLI behavior, then build the tool from scratch and give me the code files.
```

### 930. D5_s984016_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-triage tool from scratch that helps debug flaky CI runs: it should read plain-text or JSONL logs, detect likely failure signatures, cluster repeated errors, and generate a short incident summary with the most probable root-cause hints. Please make it a real reusable package with the core analyzer, a CLI, and a README, and use web research to check current best practices and APIs for the Python logging/parsing libraries and any useful log-dedup approaches before you implement it.
```

### 931. D5_s984038_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for debugging and log analysis that tails live app logs, detects common failure patterns, and generates a concise incident summary with likely root-cause hints. I want `app.py`, `patterns.yaml`, `tests/`, and `README.md`; research the best-fit logging/parser libraries and any current guidance on structured logging and regex performance before you code.
```

### 932. D5_s984044_en (domain=D5, difficulty=7)

```
I need a small but real debugging and log-analysis utility built from scratch for our engineering team.

- Build a CLI tool that ingests plain-text application logs and pinpoints likely root causes for repeated failures, timeouts, and retries.
- Add a rules-based detector for common patterns like stack traces, HTTP 5xx bursts, malformed JSON messages, and exponential backoff loops.
- Include a clean test suite with realistic sample cases you generate yourself, plus a short README that explains how to run it and how the heuristics work.
- Use current best practices for Python CLI tooling and log parsing, and research any standard libraries or lightweight dependencies before you code.
- I want the actual code files and tests, not just an explanation.
```

### 933. D5_s984056_en (domain=D5, difficulty=7)

```
I want a small but real debugging tool built from scratch for our engineering team.

- Build a CLI that can ingest plain text app logs and summarize likely error clusters, noisy repeats, and first-seen failure signatures.
- Include a compact report mode that highlights probable root-cause patterns and links repeated stack traces together.
- Make it easy to run locally on Linux/macOS, with clear install/use instructions and sensible defaults.
- Add a test suite with realistic synthetic log cases so we can validate parsing, clustering, and edge cases.
- Please do a bit of web research first so the design follows current best practices for Python CLI apps, log parsing, and approximate string matching libraries.
- Deliver the code and README, not just an explanation.
```

### 934. D5_s984097_zh (domain=D5, difficulty=7)

```
帮我从零做一个 Python 诊断工具，名字就叫 logtriage。要能解析多种格式的应用日志（至少支持 JSON 行和常见 text logs），自动归类错误、提取时间线、去重堆栈，并输出一份可读的故障摘要。请直接给出代码文件和 README，顺手把单元测试也写好；实现前先查一下 Click/Typer、Rich、structlog 或类似库的当前最佳实践。然后把核心解析、CLI、测试、文档分开做，最后整合成可运行项目。
```

### 935. D5_s984116_en (domain=D5, difficulty=7)

```
I want a from-scratch Python tool that helps us debug flaky service outages from logs and test runs.
- Build a small CLI that ingests raw text logs and CI test output pasted in by the user, then groups likely related errors into incidents.
- Add a compact HTML or Markdown report with timelines, deduped stack traces, and a short "what changed" summary for each incident.
- Include a configuration file format for tuning rules like time-window size, regex patterns, and severity mapping.
- Make it realistic by using current best practices from the web for structured logging, log parsing, and CLI design, and call out any library choices you make.
- Ship the code, tests, and a README with setup and usage examples.
```

### 936. D5_s984137_zh (domain=D5, difficulty=7)

```
我需要你从零写一个小型故障排查工具，目标是给 Python 服务的结构化日志做分析，自动找出最近一次异常高峰前后的关键错误链路，并输出一个可直接运行的命令行程序和说明文档。你先自己查一下 Python 标准库里和常见第三方库在日志解析、时间窗口统计、TUI/CLI 参数处理方面的最佳实践，再把代码、测试和 README 一起做出来；不要用现成项目当模板，文件名你来定，但要能直接跑起来。最好把工作拆成几个互不依赖的部分并行做，最后再集成成完整工具。
```

### 937. D5_s984140_en (domain=D5, difficulty=7)

```
I want a from-scratch internal debugging tool for a Kubernetes-based service, focused on log analysis and incident triage.
- Build a small Python service that ingests raw app logs and turns them into searchable incident summaries with severity scoring and likely-root-cause hints.
- Include a CLI and a tiny HTTP API so engineers can run it locally or hook it into a workflow.
- Use current best-practice choices for log parsing, structured logging, and lightweight local persistence; please research the most suitable libraries and patterns first.
- Add solid tests and a short setup guide so the tool is actually usable by the team.
- Keep it self-contained: no input files, no external datasets, just code and docs created from scratch.
```

### 938. D5_s984144_en (domain=D5, difficulty=7)

```
Build me a from-scratch Python tool that tails app logs, detects error spikes and repeated stack traces, and outputs a short triage report plus a JSON summary. Put the code in `src/`, add a CLI in `main.py`, and include `tests/` plus a `README.md` with usage and examples. No input files — just build the tool and the docs.
```

### 939. D5_s984156_en (domain=D5, difficulty=7)

```
Build a from-scratch Python log triage tool for Kubernetes app incidents: parse mixed JSON/plaintext logs, detect error clusters, correlate them with recent deploy markers, and output a short incident summary plus a machine-readable report. Use the latest best practices from the Python logging ecosystem and Kubernetes log/label conventions, and write the code in app.py with tests in test_app.py and a README.md that explains usage and the detection heuristics.
```

### 940. D5_s984195_zh (domain=D5, difficulty=7)

```
我需要你从零搭一个用于排查线上故障的日志分析小工具，目标是做成一个可直接运行的命令行程序和配套文档，支持读取多行文本日志、按时间窗口聚合错误、识别常见异常模式（比如超时、重试风暴、5xx、连接池耗尽），再输出一份适合值班排障看的总结报告和可选的 JSON 结果；你先自己查一下 Python 标准库里适合做日志解析和时间处理的最佳实践，以及现成库（如果真有必要）该怎么选，再把代码、测试和 README 一起做出来，文件名你自己定，但要能直接运行和验证。
```

### 941. D5_s984213_zh (domain=D5, difficulty=7)

```
帮我从零做一个可落地的日志排障工具，目标是把 Kubernetes / Docker / 应用日志里的报错快速归因并给出下一步排查建议。
- 先做一个 Python 版本的命令行工具，能读取文本日志，识别常见异常模式（比如超时、连接拒绝、OOM、DNS 失败、认证失败），并输出结构化摘要。
- 希望它支持按时间窗口聚合、按错误类型分组、自动提取关键上下文行，还能生成一份适合 on-call 使用的排障报告。
- 需要你参考现有生态里常见做法，决定用哪些库更稳妥，比如日志解析、模式匹配、命令行参数、颜色输出、表格展示这些部分。
- 请把代码、测试和使用说明一起给我，最好再补一个简短的设计说明，解释你的识别规则和误报控制思路。
- 代码要能直接运行，测试要覆盖核心解析逻辑和至少几个典型错误场景。
```

### 942. D5_s984231_zh (domain=D5, difficulty=7)

```
我需要你从零搭一个用于排查微服务日志问题的小工具，目标是做一个本地可运行的 CLI：它能读取我后面会自己喂进去的多服务日志文本，自动按 trace/request 关联、提取错误链路、识别常见异常模式，还能输出一份适合值班排障的摘要报告和测试用例说明。你先把代码、README 和测试都写好，尽量参考现成日志解析、CLI 参数设计和 Python 标准库/第三方库的最佳实践来选型，但不要依赖任何现成模板或输入文件；如果需要，你可以自己设计示例日志格式和内置规则集。请把成品文件直接给我。
```

### 943. D5_s984242_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for debugging Kubernetes pod logs and crash loops: `logtriage.py` plus `README.md`. It should ingest raw text from stdin or a pasted log string, detect common failure patterns, cluster related lines, and emit a concise triage report with likely root cause, severity, and next-step actions. Use current best practices and any relevant library/API docs you need to research first, then implement and test it.
```

### 944. D5_s984248_en (domain=D5, difficulty=7)

```
I want a small but real observability tool built from scratch for incident triage.

- Build a log parser and anomaly detector for Kubernetes-style application logs that can spot bursts, repeated error signatures, and sudden latency spikes.
- Expose it as a command-line tool with a clean summary report plus JSON output for automation.
- Include solid unit tests and a few sample log scenarios generated in code so it can be exercised without any input files.
- Use current best practices from existing logging/CLI libraries and any relevant docs you need to check online before coding.
- Keep the implementation lightweight, but make the architecture clear enough that I could extend it later into a daemon or API service.
```

### 945. D5_s984257_zh (domain=D5, difficulty=7)

```
我需要你从零做一个用于排查线上问题的小工具：给我实现一个 Python 的命令行日志分析器，能读取多种格式的应用日志（比如 JSON 行、普通文本、带时间戳的错误堆栈），自动识别错误类型、聚合高频异常、按时间窗口统计告警，并输出一份可直接给值班同学看的诊断报告和终端摘要。代码、测试、README 都要一起交付；如果需要的话，先查一下现成库怎么处理日志解析、正则提取、命令行参数和表格输出，再自己从头搭起来，不要依赖现成样例数据。
```

### 946. D5_s984314_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for debugging log spikes: parse mixed app/server logs, cluster recurring error patterns, and generate a short incident report with likely root causes and next-step checks. I want `logtriage.py`, `tests/`, and `README.md`; make it a real CLI with `--input`, `--since`, `--top`, and `--json` output, plus a small demo in the README. Use current best practices for Python logging, regex parsing, and CLI UX.
```

### 947. D5_s984333_zh (domain=D5, difficulty=7)

```
我想从零做一个面向 SRE/开发者的日志与故障排查小工具，重点是把零散日志变成可操作的诊断结果。
- 做一个本地可运行的命令行工具，支持读取标准输入或文本日志，自动识别错误模式、异常堆栈、重复告警和关键事件时间线
- 参考一下现成方案里常见的做法，先查一查 Python 生态里适合做日志解析、结构化输出和命令行交互的库，以及可借鉴的最佳实践
- 代码要从头实现，不要依赖现成的日志分析成品；希望有清晰的模块划分、可测试的核心逻辑和比较完整的单元测试
- 最终给我一套能直接跑的代码和简短说明，最好包含用法示例、测试方法，以及遇到未知日志格式时的降级策略
```

### 948. D5_s984340_en (domain=D5, difficulty=7)

```
I need you to build a small from-scratch log triage tool for Kubernetes incidents: a Python CLI that can ingest raw text logs from stdin or a file, detect common crash-loop and probe-failure patterns, cluster repeated stack traces, and emit a concise incident summary plus recommended next debug steps. Please include the code, a README, and enough tests to show it works; use current best practices and look up any relevant log-parsing or CLI library choices before you implement it.
```

### 949. D5_s984363_zh (domain=D5, difficulty=7)

```
我需要你从零做一个给 SRE/后端排障用的小工具：做成一个本地可运行的日志诊断器，能读我手动贴进去的 Docker/Kubernetes/应用日志字符串，自动识别常见错误模式（比如超时、重试风暴、OOM、连接池耗尽、JSON 解析失败），给出事件时间线、可疑根因排序、以及一份可导出的 Markdown 报告；再顺手带上一个简单的命令行入口和单元测试。你先查一下 Python 里适合做日志解析、模式匹配、CLI 和测试的现成最佳实践/库，再把核心逻辑、命令行、测试和文档都从头实现出来，最后把代码文件和 README 一起给我。
```

### 950. D5_s984426_en (domain=D5, difficulty=7)

```
We need a small internal incident-triage tool because our support team keeps losing time when customer-facing services fail and the logs are too noisy to read quickly. I want you to build it from scratch as a real code project, not a mockup, so it can take a stream of plain-text log lines and flag likely root causes, repeated failures, and the most important alerts for an on-call person. Please research any good current Python libraries or standard approaches for parsing logs, pattern matching, and building a simple command-line tool, then use that to design and implement the solution cleanly. I want the finished code plus a short README that explains how to run it and how the detection works. There are no input files to start from; please create the code, tests, and any supporting documentation yourself.
```

### 951. D5_s984478_en (domain=D5, difficulty=7)

```
Build a from-scratch log triage and debugging utility for Kubernetes-style application logs that I can run locally from the command line, because I want to turn raw text logs into actionable incident summaries without depending on any existing starter project or input dataset. I do not want a data-analysis notebook or anything that assumes pre-labeled files; I want the code itself, built from scratch, and I want the implementation to be grounded in current best practices for log parsing, CLI design, and testing, so you should research appropriate libraries and patterns on the web before coding.

The tool should accept plain-text logs pasted into stdin or supplied as a file path, parse multiple common structured and semi-structured formats, and produce a compact incident report that groups repeated errors, identifies likely root-cause signatures, and highlights suspicious time ranges. I need it to handle at least JSON logs, logfmt/key=value lines, and conventional unstructured lines with timestamps and severity tags. It should normalize timestamps to UTC when possible, detect duplicates and bursts, and compute a few simple but defensible summaries: first occurrence, last occurrence, frequency, severity breakdown, and a short natural-language synopsis of the most likely failure cluster. If the input is insufficiently structured, it should still degrade gracefully and report what it could parse instead of failing hard.

I want the utility to be designed for realistic debugging workflows. That means it should support a few common filters and flags, such as selecting a time window, filtering by minimum severity, grouping by service/component if that metadata exists, and choosing between a human-readable report and JSON output. It also needs clear exit codes, helpful error messages, and a small but meaningful test plan that covers tricky edge cases like malformed JSON lines, mixed timestamp formats, repeated stack traces, empty input, and log lines that lack severity labels. Please make the CLI behavior explicit and deterministic.

Please base the implementation on your own web research of current Python logging and CLI ecosystem recommendations, but keep the actual build self-contained and from scratch. I am looking for a real code deliverable, not just advice: produce the source files, the tests, and a README that explains usage, assumptions, and limitations. I care especially about correctness under messy real-world log input, so I want the code to be conservative in parsing and transparent about confidence when generating summaries.
```

### 952. D5_s984494_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool named logprobe: it should ingest live app logs from stdin or a tail command, detect likely root causes for exceptions/timeouts, and print a ranked diagnosis with evidence. I want app.py, parser.py, rules.py, tests/, and a short README.md with setup and example usage.
```

### 953. D5_s984513_zh (domain=D5, difficulty=7)

```
帮我从零做一个“服务端日志异常排查”小工具，目标是能快速读入应用日志并定位可疑错误模式。
- 用 Python 3 实现一个可安装/可运行的命令行工具，核心功能包括日志解析、按时间窗口聚合、错误模式归类和简单的根因线索输出。
- 希望支持至少两种常见日志格式（比如 JSON 行日志和传统文本日志），还能扩展自定义正则规则。
- 请同时给出测试方案和一套能直接跑的单元测试，重点覆盖解析失败、空日志、重复报错、乱序时间戳、超长日志行这些边界情况。
- 最终我想要的是可运行的代码和 README，里面要写清楚安装方式、命令示例、输出解释，以及你参考过的相关 Python 日志处理/CLI 最佳实践。
- 如果你查到更适合做日志分析的现成库或规范，也请结合 Web 资料做取舍说明，但实现本身要是从头写的。不要用现成项目直接拼装。
```

### 954. D5_s984530_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool for Kubernetes crash-loop debugging: generate a structured triage report from raw pod logs pasted in at runtime, with severity scoring, likely root-cause classification, and recommended next steps. Create app.py, parser.py, classifier.py, report.py, tests/, and README.md; no input files, just the code and docs.
```

### 955. D5_s984536_en (domain=D5, difficulty=7)

```
I want a small but real observability tool built from scratch for debugging service logs. Please implement a Python CLI that reads app logs from stdin, groups related lines into incidents, and highlights probable root causes using configurable patterns.
- Use current best practices for Python logging, regex parsing, and CLI design after checking the latest docs/examples for `argparse`, `re`, and at least one lightweight terminal UI library if needed.
- Build the core incident-correlator logic, a command-line interface, and a compact test suite so I can run it locally and extend it later.
- Include useful output formats for both human-readable summaries and JSON, plus clear error handling for malformed log lines.
- Add a short README that explains how to run it, how the grouping logic works, and how to customize the rules.
- Keep it self-contained: no input files, no external datasets, just code and documentation generated from scratch.
```

### 956. D5_s984548_en (domain=D5, difficulty=7)

```
I want a small but real log-debugging tool built from scratch for our engineering team.
- Build a CLI that parses application logs and flags likely root causes for incidents, not just keyword matches.
- Include support for JSON logs and plain-text logs, plus a compact summary of error spikes, repeated stack traces, and correlation IDs.
- Research current best practices for log parsing and a sensible Python library stack before you code, then implement the tool and document how to run it.
- Add a test plan with a few representative synthetic log examples created in the codebase itself, and make sure the CLI exits cleanly on bad input.
- Deliver the code and a short README so another engineer can use it right away.
```

### 957. D5_s984558_en (domain=D5, difficulty=7)

```
We need a small internal command-line tool that helps our support and engineering team make sense of messy logs faster when an incident happens, because right now people are copying snippets into chats and missing patterns. Please build it from scratch as a real working utility, not a mockup, so it can take plain text logs pasted into the terminal, spot common error patterns, group related lines, and produce a short incident summary we can share with the team. I want you to research the best current Python libraries and approaches for parsing logs, terminal output formatting, and lightweight similarity matching so the design is sensible, then implement the tool, include tests, and write a short README explaining how to use it and how the detection works. There are no input files to start from; the tool should work on pasted log text or stdin.
```

### 958. D5_s984559_zh (domain=D5, difficulty=7)

```
我们现在要把客服和运维里最耗时间的“日志排查”和“故障复盘”流程标准化，目标是做一个从零开始的内部工具，能把一段系统日志快速归类、提炼关键错误、生成可读的排障摘要，还能输出给工程师看的测试建议。我希望你直接把这个工具的代码和说明都做出来，不要依赖任何现成输入文件，日志样例可以你自己在代码里构造。请先帮我研究一下适合做日志解析和命令行工具的主流 Python 方案、推荐做法和常见坑，然后从零实现一个可运行的程序：它至少要支持读取纯文本日志、识别时间戳/错误级别/请求ID这类关键信息、按问题类型聚合、输出一份简洁的故障摘要，并提供一个可选的命令行入口，方便团队以后直接拿来用。最后请把代码、测试和使用说明一起给我，确保别人拿到就能跑、能测、能看懂。
```

### 959. D5_s984628_en (domain=D5, difficulty=7)

```
I need you to build a small Python log-triage tool from scratch for debugging flaky CI jobs: something that reads plain-text build logs, detects common failure patterns, groups repeated exceptions, highlights probable root causes, and prints a compact summary plus a JSON report. Please use current best practices from the web for Python regex/log parsing, structured logging, and CLI design, then implement the code and tests in a couple of files I can run locally.
```

### 960. D5_s984686_en (domain=D5, difficulty=7)

```
Build a from-scratch Python tool called logtrace that triages app logs and test output for flaky failures, root-cause clustering, and timeline reconstruction. I want app.py, parser.py, cluster.py, and README.md, plus a small test suite under tests/; no input files, just implement the tool and its CLI.
Use web research to pick a good logging parser/regex approach and a lightweight clustering library or standard-library strategy, then wire it up cleanly.
```

### 961. D5_s984697_zh (domain=D5, difficulty=7)

```
从零做一个 Python 终端工具，帮我分析应用日志里的异常堆栈并生成排查报告。我要一个可安装的 CLI，支持 `tail`/`file` 两种输入、按规则聚合重复错误、输出 Markdown/JSON 报告，并带一个最小可用的 Web API（FastAPI）方便我把它接到现有告警系统里。把核心解析、CLI、API、测试和 README 分开做，代码要能直接跑起来。
```

### 962. D5_s984701_zh (domain=D5, difficulty=7)

```
我需要你从零做一个给 SRE/后端团队用的日志排障小工具，目标是把一堆应用日志里常见的报错模式自动归类、提炼时间线，并生成一份可直接给值班同事看的诊断报告。你帮我把代码和说明文档一起做出来，最好有一个命令行入口，支持读取标准输入或指定日志文本，输出结构化结果、可读报告和基础测试；如果需要选技术方案、日志解析方式、CLI 框架或报告格式，先查一下现在常用的做法和相关库再定。
```

### 963. D7_s980563_en (domain=D7, difficulty=7)

```
We need a small but real incident-automation tool for our operations team because too much time is being lost copying details between Slack, Jira, and our status page during outages. Build a from-scratch web service that can take a plain-English incident summary, turn it into a structured incident record, create a postmortem draft, and generate a clean API workflow we can use to open or update tickets. I want the actual code and a short README showing how to run it locally. Please research current best practices for incident management and a couple of relevant APIs or libraries before you build, then implement the tool in a way that feels practical for a real team to use.
```

### 964. D7_s980566_zh (domain=D7, difficulty=7)

```
我需要你帮我从零构建一个轻量级的事件响应与事后分析自动化工具，用于运维工作流。工具名为 `incidex`。核心功能：用户通过 CLI 创建事件、分配响应人、设置严重等级（sev1-sev4），事件有状态机（未分派→已分派→处理中→已解决→已关闭；支持驳回回退到处理中）。每个事件可以关联事后分析（postmortem）模板，模板是 Markdown 文件，包含固定字段（标题、日期、受影响的系统、时间线、根因、行动项）。CLI 支持以下子命令：`create`, `assign`, `update`, `list`, `postmortem`（生成空白模板并填充事件数据）。此外需要提供一个 REST API 暴露这些功能（使用 Flask），以便被其他系统集成。工具需要处理边界情况：创建事件时严重等级非法则报错；更新状态转换不合法则拒绝；`postmortem` 命令如果事件未解决则提示必须先解决。所有数据持久化在本地 SQLite 数据库中，启动时自动创建表。你不需要给我输入文件，所有代码从零写。请先快速调研一下当前业界常见的事件管理 API（如 PagerDuty 的 incident API 模式，Jira 的 issue 状态机）和 postmortem 最佳实践（如 Atlassian 的 postmortem 模板），以便借鉴命名和流程。然后构建完整的 Python 工程，包括：一个核心模块（incidex.core）实现事件与状态机逻辑；一个 CLI 模块（incidex.cli）使用 Click 库；一个 API 模块（incidex.api）使用 Flask；一套 pytest 单元测试（覆盖所有状态转换、非法输入、数据库 CRUD）；以及一个 README.md 说明安装使用和示例。最终交付物是工程文件夹内的 `incidex/` 目录（包含 `__init__.py`, `core.py`, `cli.py`, `api.py`, `models.py`, `db.py`），以及根目录的 `tests/` 和 `README.md`。请确保 CLI 有完善的 `--help` 输出，API 返回 JSON 且包含适当 HTTP 状态码。所有代码需符合 PEP8，注释中英文皆可。如果没有额外问题，直接开始构建并输出完整代码文件。
```

### 965. D7_s980653_zh (domain=D7, difficulty=7)

```
帮我从零写一个“事故响应自动化”小工具，做成一个可运行的 Python 项目，支持：接收 JSON 格式 incident、自动生成 postmortem 草稿、调用外部 HTTP API 拉取服务状态/告警上下文、以及把结果导出成 Markdown。请把代码放在 app.py、postmortem.py、integrations.py、tests/、README.md 里，别给我半成品，要能直接跑。顺手查一下现在主流的 Python HTTP/重试/Markdown 生成最佳实践，再按这个实现。
```

### 966. D7_s980690_en (domain=D7, difficulty=7)

```
Build a small incident automation service from scratch for Slack + PagerDuty style workflows. I want a Python FastAPI app with a rule engine that can ingest incident webhook payloads, auto-apply routing/escalation rules, and generate a postmortem draft Markdown file from an incident timeline. Add a CLI for creating rules and replaying sample incidents, plus tests and a README with setup/run examples. Use current docs for FastAPI, Pydantic, and any webhook signing / HTTP client best practices as needed.
```

### 967. D7_s980700_en (domain=D7, difficulty=7)

```
Build a small incident-postmortem automation service from scratch: a Python FastAPI app plus a CLI that ingests incident events, creates a postmortem draft, and generates follow-up Jira/Slack action items. Put the code in app.py, the CLI in cli.py, tests in tests/, and a README.md with setup and usage. Use current best practices and APIs from the web for FastAPI, Jira, and Slack integration design.
```

### 968. D7_s980720_zh (domain=D7, difficulty=7)

```
帮我从零做一个面向运维和事故响应的自动化工具，目标是把一次事故从“告警触发”到“复盘输出”串起来。

- 先调研一下现成做法：需要支持 Slack、PagerDuty、GitHub Issues 这类常见系统的 API 集成思路，顺便参考几种 incident/postmortem 的最佳实践。
- 实现一个可运行的本地工具，能创建事故、记录时间线、自动生成复盘提纲，并把结果导出成 Markdown。
- 再做一个命令行界面，方便用几个命令完成“新建事故 / 更新状态 / 添加行动项 / 生成复盘”。
- 代码要包含清晰的模块划分、错误处理和单元测试，能从零跑起来，不依赖现成数据文件。
- 最后给我一份简短的 README，说明安装、使用方式、以及它能接哪些外部 API（哪怕先只做模拟适配层也行）。
```

### 969. D7_s980796_zh (domain=D7, difficulty=7)

```
帮我从零构建一个事件管理与事后复盘CLI工具，支持创建、分配、关闭事件，自动生成复盘报告，并集成Slack通知。项目文件：incident_cli.py, postmortem_template.md, slack_integration.py, test_incident_cli.py, README.md。代码要模块化，用Python的click库写CLI，用sqlite存事件数据，事后复盘报告用Jinja2模板生成Markdown，Slack用webhook发送。先调研Slack Webhook API和最佳实践，然后开干。
```

### 970. D7_s980803_en (domain=D7, difficulty=7)

```
Our team handles dozens of incidents each month, and writing postmortems is painfully manual and inconsistent. I need a command-line tool that helps automate this: after an incident is resolved, someone runs a command with the incident ID, the tool fetches the timeline from PagerDuty, prompts for a few missing details (like root cause, action items), and outputs a clean Markdown postmortem file ready for review. It should also support saving a template and listing past postmortems. Please build it from scratch as a Python CLI tool — no starter code, just a solid, testable implementation with clear documentation. I can give you the PagerDuty API token and Slack webhook URL later; the tool should read those from a config file or environment variables.
```

### 971. D7_s980832_zh (domain=D7, difficulty=7)

```
从零做一个 Python 工具，帮值班工程师把 incident / postmortem 工作流自动化：支持创建 incident、记录时间线、生成 RFO/5 Whys 初稿、导出 Markdown 和 JSON。你直接产出代码文件和 README，顺手把外部 API/库选型也查一下，按现在主流做法来设计。别给我方案稿，直接写可运行实现。
```

### 972. D7_s980839_zh (domain=D7, difficulty=7)

```
我们团队每次线上事故后都要手动写事后复盘报告，从不同系统（Slack、Jira、监控工具）扒聊天记录和工单，再套模板写成Markdown，然后发邮件归档。这个流程太慢，还经常漏掉关键字段。我想让你开发一个命令行工具，能直接从零开始构建，不用任何现有数据文件。工具要能交互式录入事故时间、影响范围、根因分析、行动项等，并且自动生成结构化的复盘报告。最好还能集成Slack API发送通知到指定频道，以及通过Jira API创建对应的跟踪任务。你帮我研究一下当前主流的复盘模板格式、Slack和Jira的API用法，然后把这个工具做出来。我要一个可运行的Python脚本和一个简单的README说明怎么用。
```

### 973. D7_s980844_en (domain=D7, difficulty=7)

```
Build a from-scratch incident workflow tool for our SRE team: an API-first service that creates incidents, assigns owners, tracks timeline events, and generates a postmortem markdown report from the incident record. Put the code in app.py, tests in test_app.py, and a short README.md with setup and usage. Use the current Slack/Atlassian/Jira style workflow patterns you find useful, but don’t rely on any starter files or sample data.
```

### 974. D7_s980872_en (domain=D7, difficulty=7)

```
I need you to build a CLI tool called 'postmortem-gen' that automates incident postmortems. It should fetch incident details from PagerDuty (using their API v2), allow posting a Slack message to a specified channel, and generate a structured Markdown report. Also include a lightweight webhook endpoint (using Flask or FastAPI) that can be called to trigger the same workflow. Use Python. Write everything from scratch – no starter files. Include unit tests and a README with setup and usage instructions.
```

### 975. D7_s980906_zh (domain=D7, difficulty=7)

```
帮我从零构建一个事件响应工作流自动化CLI工具，使用Python。支持通过命令行创建、确认、解决事件，并自动发送Slack通知、创建Jira工单，以及生成事后分析Markdown报告。要求包含单元测试和README文档，项目结构使用src/、tests/、docs/。没有输入文件。输出文件：incident_cli.py, README.md。
```

### 976. D7_s980913_zh (domain=D7, difficulty=7)

```
帮我开发一个用于事件响应自动化的命令行工具（incident_ctl.py），纯Python从零开始，不依赖外部数据文件。需求如下：
- 支持从 PagerDuty API 拉取最近的事件（列表），需要模拟或使用真实token；
- 能基于事件生成事后分析报告模板（包含摘要、时间线、根因、行动项等章节）；
- 支持将报告通过 Slack Webhook 发送，以及创建 Jira 工单（可选）；
- 所有功能通过子命令（list、generate、workflow）调用，带帮助信息；
- 编写单元测试，mock 掉外部 API 调用；
- 提供详细的 README 文档，包括安装、配置环境变量、示例用法。
研究 PagerDuty API 端点、Slack Webhook 格式、Jira REST API 作为参考；代码需要模块化，异常处理清晰。
```

### 977. D7_s980931_en (domain=D7, difficulty=7)

```
I need you to build a small from-scratch incident workflow tool for Ops that can open, update, and close incidents, generate a postmortem skeleton, and push notifications to Slack and PagerDuty through configurable webhooks/API calls. Please create the code, a README, and a few working examples so I can run it locally, and use current docs for the API patterns and best practices while you design it.
```

### 978. D7_s980939_en (domain=D7, difficulty=7)

```
Build a from-scratch incident automation service for PagerDuty + Slack that can open an incident, collect timeline updates, generate a postmortem draft, and post a summary back to Slack. I want the code in app.py plus tests in tests/ and a short README.md with setup and run commands.
```

### 979. D7_s980957_en (domain=D7, difficulty=7)

```
We need a small internal tool to make incident follow-up faster and more consistent, because right now our postmortems and action items are scattered across Slack, Jira, and docs and people keep missing the same steps. Please build a from-scratch workflow automation service that can open a new incident record, generate a simple postmortem outline, track action items through a few states, and push updates to a webhook or API endpoint. I want the actual code files, a short README, and enough tests that we can trust the basic flows. Please use current best practices and sensible library choices after checking what is commonly used today, especially for webhooks, API design, and lightweight workflow/state handling.
```

### 980. D7_s980966_en (domain=D7, difficulty=7)

```
I need you to build a small incident-automation tool from scratch for our ops team: a Python service that takes a Slack-formatted incident summary plus a list of API endpoints, then generates a clean postmortem markdown draft, a timeline, and follow-up action items, with a CLI to run it locally and a minimal HTTP API to trigger it. Please research the current docs for Slack message formatting, FastAPI, Pydantic, and a sensible markdown templating approach before coding, then give me the code files and README so I can run it end to end.
```

### 981. D7_s980967_zh (domain=D7, difficulty=7)

```
我需要你从零搭一个给值班/事故处理用的自动化小工具，最好是一个可直接运行的 Python 项目：能接收一条事故描述，自动生成 incident 摘要、影响范围、时间线模板和 postmortem 草稿，并且支持把结果整理成 Markdown 和 JSON 两种输出，方便后续接 PagerDuty、Slack、Jira 或 GitHub Issues 的 API 流程。你先帮我把代码、README 和必要的测试都写出来，别用现成模板直接拼，接口设计、库选型和这类工作流的最佳实践你需要自己查资料后再定。
```

### 982. D7_s981012_zh (domain=D7, difficulty=7)

```
帮我从零做一个 Rust 的 incident postmortem 自动化工具，先产出可运行代码和 README.md。工具要能接收一次事故的标题、时间线、影响范围、根因、行动项，自动生成一份结构化的 Markdown 复盘报告，并支持把行动项导出成 Jira/Linear 风格的 JSON。先查一下现成的 postmortem 模板、Jira/Linear API 字段习惯、以及 Rust 里适合做 Markdown/CLI/序列化的库，再开始实现。
```

### 983. D7_s981087_en (domain=D7, difficulty=7)

```
I need you to build a small incident-response workflow tool from scratch that helps an ops team create incident records, generate a postmortem template, and kick off follow-up actions through API webhooks. Please research current best practices for incident/postmortem structure and any relevant API patterns with web search, then implement the code and docs in a clean repo with tests. I want it to be usable from the command line and also expose a simple local HTTP API, with sensible defaults for severity, timestamps, ownership, and action-item tracking.
```

### 984. D7_s981093_zh (domain=D7, difficulty=7)

```
我需要你帮我设计并实现一个基于命令行的故障事后复盘（Postmortem）自动化工具。这个工具的核心功能是：通过与 PagerDuty API 交互，获取指定时间范围内的故障（Incident）列表，自动生成结构化的 Markdown 复盘报告，并支持通过 Slack Webhook 发送报告摘要。整个工具完全从零构建，没有现成的代码或数据文件。

具体要求如下：

1. **数据模型**：定义 Incident 对象，包含 id、title、status、created_at、resolved_at、urgency、escalation_policy、assignees 等字段。支持从 PagerDuty API v2 的 GET /incidents 接口获取数据，需要处理分页（cursor-based pagination）。
2. **复盘报告生成**：基于预设的模板（例如：标题、摘要、时间线、根本原因、行动项），将获取的故障数据填入 Markdown 模板。模板支持 Jinja2 变量替换。报告文件名包含故障 ID 和日期。
3. **CLI 接口**：使用 Click 库实现命令行界面，提供以下子命令：
   - `fetch`：根据时间范围（--from, --to）和状态（--status）获取故障列表，输出 JSON 格式。
   - `report`：根据故障 ID 生成复盘报告，输出 Markdown 文件。
   - `notify`：将报告摘要通过 Slack Webhook 发送。
   - `init`：生成示例配置文件 config.yaml，包含 API key、Slack webhook URL 等。
   所有子命令需有 --help 信息，参数需做有效性和类型校验。
4. **错误处理**：网络请求失败、API 限流、无效配置等场景需给出明确错误信息，并建议用户检查配置或重试。
5. **测试**：使用 pytest 编写至少 3 个测试用例：一个 mock 网络请求测试 fetch 功能，一个测试报告模板渲染，一个测试 CLI 参数解析。测试需隔离外部依赖。
6. **文档**：README.md 包含安装步骤（pip install -r requirements.txt 即可）、环境变量配置、使用示例以及常见问题。

你不需要提供任何输入文件——所有数据通过 API 获取。你需要通过 web 搜索来了解 PagerDuty API 认证方式、分页参数、Slack Webhook 消息格式以及 Jinja2 模板的最佳实践。

最终交付物为两个文件：`postmortem-cli.py`（含所有功能代码）和 `README.md`。代码需包含清晰的注释，并遵循 PEP8 规范。
```

### 985. D7_s981160_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops automation tool from scratch: a Python service that ingests API/webhook incident events, creates a lightweight postmortem draft, and exposes a CLI plus a REST endpoint for generating incident timelines, action items, and a summary report. Please use current web research to confirm good patterns and libraries for webhook handling, markdown/report generation, and scheduling/retries, then implement the code, tests, and README in the repo.
```

### 986. D7_s981209_en (domain=D7, difficulty=7)

```
We keep losing time when incidents move from Slack to ticketing to postmortems, and I want a small internal tool that makes that flow less manual. Build a from-scratch incident workflow service for our ops team that can take a new incident, create a structured incident record, generate a clean postmortem draft from the timeline, and expose a simple API plus command line so team members can use it without opening a browser.

Please research a few current best-practice patterns for incident management and postmortem structure, plus one or two realistic API/library choices for implementing the service, then build the code and docs from scratch. I do not have any input files for you; I want the finished codebase and a short README explaining how to run it and use the main flows. Make sure it feels like something a real support or platform team could adopt, not a toy script.
```

### 987. D7_s981235_zh (domain=D7, difficulty=7)

```
帮我从零做一个用于事故响应和复盘流程自动化的小工具，尽量贴近真实团队会用的样子。

- 先调研一下现在常见的 incident / postmortem / webhook 工作流做法，看看 Slack、GitHub Issues、PagerDuty 风格的通知和 API 交互一般怎么设计。
- 然后实现一个可直接运行的本地工具：能创建事故记录、更新状态、自动生成复盘模板、导出为 Markdown，并且支持通过 REST API 触发这些流程。
- 我希望代码结构清晰，能单独跑起来，带基本测试和使用说明，最好能模拟一个“事故开始 → 升级 → 复盘”的完整链路。
- 如果需要用第三方库，选成熟、维护活跃的；把你查到的设计依据和取舍也简单写出来。
- 最终给我可运行的代码文件和 README，不要只给思路。
```

### 988. D7_s981269_en (domain=D7, difficulty=7)

```
We need a small internal tool that helps our ops team handle incidents faster and write cleaner postmortems. Build a from-scratch app that can open an incident, track status updates, generate a simple incident timeline from those updates, and then turn that into a postmortem draft with action items. It should be practical enough for a real team to try, with a simple API or command-line interface, clear setup instructions, and sensible defaults. Please research current best practices and any relevant libraries or API patterns first, then build the code and the documentation from scratch.
```

### 989. D7_s981307_en (domain=D7, difficulty=7)

```
Build a small incident-operations automation tool from scratch for Slack-first teams. I want a usable prototype that can take a webhook payload for a new incident, create a structured incident record, generate a postmortem outline, and produce follow-up tasks/status updates without relying on any starter data.

- Make it work as a real code project, not a mockup: include the core logic, a CLI or minimal API, and clear README usage.
- Research a few current best-practice options for incident tooling and API/webhook handling before implementing, so the design choices are grounded in real libraries and patterns.
- Support one incident intake path, one postmortem generation path, and one task/status workflow path, with sensible validation and error handling.
- Include automated tests for the critical workflow behaviors and edge cases.
- Keep the implementation self-contained, but structure it so it could later plug into Slack, PagerDuty, or Jira APIs.

```

### 990. D7_s981336_en (domain=D7, difficulty=7)

```
Build a from-scratch incident automation service for Slack and PagerDuty: I want a small Python app that opens incidents, posts a threaded Slack update, generates a postmortem template, and closes the loop with a follow-up checklist. Research the current Slack and PagerDuty API patterns first, then implement the code and include README.md with setup and usage.
```

### 991. D7_s981360_zh (domain=D7, difficulty=7)

```
从零写一个面向值班/事故处理的工具：做一个可本地运行的 Python CLI，支持创建 incident、自动生成 timeline、收集 action items、输出 postmortem 草稿，并能通过 GitHub Issues 和 Slack Webhook（都做成可插拔适配器）同步状态。把代码放到 app.py、integrations/、tests/、README.md，顺手把命令设计、数据模型、错误处理和示例用法都补齐。
```

### 992. D7_s981416_en (domain=D7, difficulty=7)

```
I want a small but real incident-workflow tool built from scratch for our team.

- Build a CLI app that can create, update, and close incidents, then generate a basic postmortem summary from the incident timeline.
- Include a webhook/API workflow so it can fetch a service status from a public endpoint and attach that to the incident record.
- Add persistence, validation, and a clean project structure so it feels like something we could extend later.
- Include tests and a short README with setup and example commands.
- Use current best-practice libraries and patterns you verify with web research, not guesswork.
```

### 993. D7_s981444_zh (domain=D7, difficulty=7)

```
从零做一个 Incident/Postmortem 自动化工具，先实现一个可运行的命令行应用，支持从 YAML 配置读取监控事件模板，自动生成 incident 初稿、时间线、RCA 问题清单和 postmortem Markdown。顺手把 GitHub Issues / Slack / Jira 的 API 对接方式调研一下，代码里留好可替换的集成接口和示例配置，别用现成模板项目。把代码放在 `incidentflow/`，并补上 `README.md` 和最少一组单元测试。
```

### 994. D7_s981522_en (domain=D7, difficulty=7)

```
We keep losing time during incidents because updates, escalation decisions, and the postmortem write-up all happen in different places. I want a small internal tool we can actually use to make that workflow smoother for our team.

Build a from-scratch incident workflow assistant that can create a new incident record, generate a simple timeline from manual updates, track owners and next actions, and produce a first-draft postmortem at the end. It should be something we can run locally and extend later, with a basic interface for creating incidents and exporting the summary in a clean format. Please research the best current approach for the libraries and patterns to use, then build the code and the supporting docs from scratch.
```

### 995. D7_s981592_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops workflow tool from scratch that helps a team turn a Slack/Teams incident into a structured postmortem package: it should take a live incident summary from stdin or a pasted prompt, generate an incident timeline, capture owners, mitigation steps, and follow-ups, and export a clean Markdown postmortem plus a JSON record. Please make it work as a CLI app with sensible defaults, add the core workflow logic, and include docs and tests so someone can run it locally and use it for real incident reviews.
```

### 996. D7_s981623_en (domain=D7, difficulty=7)

```
Build a from-scratch incident workflow tool for PagerDuty + Slack that can open an incident, generate a postmortem draft, and post status updates through web APIs. I want the code in app.py plus tests and a short README.md showing setup, env vars, and example commands.
```

### 997. D7_s981649_zh (domain=D7, difficulty=7)

```
帮我从零做一个 Incident Ops 工作流工具：生成一个可运行的 Python 项目，支持创建 incident、记录时间线、自动生成 postmortem 草稿，并导出到 Markdown。把代码放在 app.py、workflow.py、templates/postmortem.md、tests/ 里，顺手补一份 README.md。先查一下 GitHub Issues / PagerDuty / Jira / Slack webhook 的常见 API 设计和 Python 最佳实践，再按这些思路实现，不要用现成脚手架。
```

### 998. D7_s981679_en (domain=D7, difficulty=7)

```
I need a small but real incident-response workflow tool built from scratch for our ops team.

- Build a command-line app that creates incident timelines, tracks status changes, and generates a postmortem draft from structured incident notes.
- Include a lightweight API client for one public incident/status or ticketing service so the tool can pull in event metadata where available.
- Make it easy to export the final incident summary and action items as Markdown.
- Add tests for the core workflow logic and the API integration layer.
- Keep the design practical: use current best practices and a sensible library choice, but don’t assume any existing codebase or input files.
```

### 999. D7_s981695_zh (domain=D7, difficulty=7)

```
帮我从零做一个事故/复盘自动化工具，输出代码到 app.py、README.md 和 tests/ 目录：它要能接收一段事故信息（服务名、时间、影响、根因、缓解动作），生成一份结构化 postmortem Markdown，并把关键字段转换成适合发到 Slack/Jira 的 JSON payload。顺手把接口设计、异常处理、幂等键、重试策略也一起补上，能直接跑单元测试。
```

### 1000. D7_s981770_en (domain=D7, difficulty=7)

```
I need you to build a small incident automation tool from scratch for Ops & Workflow Automation: a Python service that lets a team create incidents, generate a postmortem skeleton, and run a few API workflow actions like paging, updating status, and closing the incident, with a simple CLI and a lightweight HTTP API. Please research current best practices and a couple of real-world libraries or API patterns first, then implement the code, tests, and a short README in the repo.
```

### 1001. D7_s981803_en (domain=D7, difficulty=7)

```
Build a from-scratch incident workflow tool for our on-call team: a small FastAPI service plus a CLI that can open incidents, collect timeline events, generate a postmortem draft, and export the result as Markdown and JSON. Put the code in app.py, cli.py, and tests/; include a README.md with setup and usage.

Use web research to confirm current best practices and relevant API/library details before coding, especially FastAPI, Typer/Click, Pydantic, and postmortem template guidance.
```

### 1002. D7_s981817_zh (domain=D7, difficulty=7)

```
给我从零做一个 Incident Postmortem Automation 工具：用 Python 写一个可运行的 CLI + 本地服务，能接收事故事件 JSON、自动生成时间线、5 Whys、影响面、根因、行动项，并导出 Markdown 报告。顺手把 README、示例命令、以及最小测试都补上；如果需要选型，先查一下现成的 Python 库和常见 postmortem 模板做设计再开写。
```

### 1003. D7_s981832_en (domain=D7, difficulty=7)

```
I need you to build a small incident automation service from scratch for ops workflows: it should ingest incident/postmortem events from webhook JSON, normalize them, and expose a CLI plus a tiny HTTP API for creating incidents, generating a postmortem draft, and routing follow-up tasks to Slack/Jira-style endpoints. Please include the source code, tests, and a README with setup and usage. Use current docs for a couple of real libraries or APIs where it helps, but the implementation should be your own.
```

### 1004. D7_s981864_en (domain=D7, difficulty=7)

```
Build a small incident-response workflow tool from scratch for our SRE team: an API-first service that opens an incident, generates a Slack/Jira-ready postmortem outline, and keeps a timeline of actions with retries/backoff. Put the code in src/ and include a README.md with setup, API examples, and the failure modes you handled. Use current best-practice research on FastAPI/Pydantic, webhook signing, and idempotency patterns before you code.
```

### 1005. D7_s981896_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops workflow tool from scratch: a Python service that ingests PagerDuty-style webhook events, deduplicates and groups related alerts into incidents, auto-generates a postmortem markdown draft when an incident is resolved, and exposes a tiny API/CLI for creating, updating, and closing incidents. Please research current best practices and any relevant library/API behavior first, then implement the code, tests, and a README for how to run it locally — there are no input files, just the finished project.
```

### 1006. D7_s981912_en (domain=D7, difficulty=7)

```
I want a from-scratch incident automation tool for our on-call workflow, not a data exercise.
- Build a small service that takes an incident title, severity, timestamp, affected service, and free-text notes, then generates a structured Slack-ready incident update and a postmortem draft.
- Include an API workflow for creating incidents, appending updates, and exporting a markdown postmortem with timeline, impact, root-cause placeholders, and follow-up actions.
- Use current best practices for incident/postmortem structure and make the design choices based on web research into real incident-management guidance and at least one modern API/web framework.
- Ship the code, tests, and a README with setup/run instructions; no starter files or input datasets are provided.
- Keep it realistic for an ops team: idempotent request handling, basic validation, and a clear path to later Slack/Jira integration.
```

### 1007. D7_s981916_en (domain=D7, difficulty=7)

```
Build a small incident-automation service from scratch: a FastAPI app with a Slack command endpoint, a GitHub issue/postmortem generator, and a rules engine that turns incident metadata into escalation + follow-up actions. I want the code in app.py, a tests/ suite, and a README.md with setup and usage.

Use current docs for Slack interactivity, GitHub issue APIs, and FastAPI best practices; wire in env-based config and keep it runnable locally.
```

### 1008. D7_s981920_en (domain=D7, difficulty=7)

```
I need you to build a small but real incident-ops tool from scratch: a Python service that takes an incident ID plus a few API tokens and automatically generates a postmortem draft by pulling status-page updates, GitHub issue/PR links, and PagerDuty incident details, then produces a structured Markdown report and a JSON summary. Please include the code, tests, and a short README explaining how to run it locally with env vars, and make sure the design follows current best practices for the APIs and libraries you choose.
```

### 1009. D7_s981935_en (domain=D7, difficulty=7)

```
We need a small internal tool that helps our ops team turn incident notes into a clean postmortem workflow, because right now too much time is lost copying details between Slack, Jira, and our incident tracker, and the quality is inconsistent. I want you to build the tool from scratch so it can generate a structured incident record, suggest the next follow-up tasks, and expose a simple API we can plug into our workflow later. Please research a few current best-practice approaches for incident/postmortem automation and any relevant API patterns before you build it, then create the code and a short README that explains how to run it and what it does. No input files will be provided.
```

### 1010. D7_s981946_en (domain=D7, difficulty=7)

```
We need a small internal incident workflow tool because our team still pieces together incident notes, postmortems, and follow-up tasks in chat, and it’s slowing down response times. I want you to build a from-scratch command-line app for incident management that can create an incident, track status changes, generate a postmortem draft from the incident timeline, and export a clean summary for handoff. Please research a few current best practices for incident/postmortem structure and any sensible open-source libraries for command-line parsing, storage, and markdown generation before you build it. I’m not giving you any files — just create the code and a short README that explains how to run it and what it does.
```

### 1011. D7_s981978_en (domain=D7, difficulty=7)

```
Build a small Python incident-workflow service from scratch for on-call ops: `incident_bot.py` plus `README.md`. It should ingest webhook-style incident events, open/append postmortem notes, and expose a CLI to create incidents, update status, and generate a markdown postmortem template. Research current best practices for incident/postmortem fields and any relevant webhook/API patterns before coding.
```

### 1012. D7_s982009_en (domain=D7, difficulty=7)

```
I want a small internal incident-ops tool built from scratch for our on-call workflow.

- Build a command-line app that helps engineers generate a postmortem draft from an incident timeline, then export it as Markdown.
- Include a lightweight API client for Slack and Jira so the tool can fetch incident metadata and create follow-up tickets.
- Make the design realistic by checking current API/library docs for the best Python packages and auth patterns before you code.
- Add tests, a clean README with setup/usage, and a few example commands that work end to end.
- Keep it self-contained with no input data files; the tool should accept typed command-line args or JSON pasted in the terminal.
```

### 1013. D7_s982031_en (domain=D7, difficulty=7)

```
We need a lightweight incident workflow tool because our current process for outages, follow-ups, and postmortems is too manual and people keep losing track of who needs to do what next. Build a small from-scratch service that helps us create incidents, assign owners, track follow-up tasks, and generate a simple postmortem summary we can share with leadership. I want the code built, plus a short README so our team can run it locally and understand how to use it. Please look up a few current best-practice references for incident management and a couple of modern API or library choices before you build it, then implement the solution cleanly from scratch.
```

### 1014. D7_s982038_en (domain=D7, difficulty=7)

```
Build a small incident-workflow service from scratch: a FastAPI app plus a CLI that ingests incident updates, creates a postmortem draft, and pushes summaries to Slack and Jira using their current webhook/API patterns. Put the code in app.py, workflow.py, and README.md, and include whatever config/examples are needed to run it locally.
```

### 1015. D7_s982060_en (domain=D7, difficulty=7)

```
Build a from-scratch incident automation tool for our SRE team: a small Python service that ingests PagerDuty-style webhooks, opens/closes Jira issues, and generates a postmortem markdown template with timeline, impact, and action items. Put the code in app.py, tests in tests/, and a README.md with setup and usage.
```

### 1016. D7_s982096_en (domain=D7, difficulty=7)

```
Build a from-scratch incident workflow tool for Ops: a small Python service that ingests incident events, generates a structured postmortem draft, and exposes a webhook/API workflow for Slack and Jira handoff. I want the code in app.py plus README.md, with clear setup, API examples, and local run instructions.
```

### 1017. D7_s982119_en (domain=D7, difficulty=7)

```
Build a small incident automation service from scratch for PagerDuty + Slack + GitHub. I want the code in app.py plus a README.md with setup and usage, and it should ingest a webhook, open an incident record, post to Slack, and generate a postmortem markdown template with timestamps and action items. Use current docs for PagerDuty Events API, Slack incoming webhooks, and GitHub Issues/PR links so the implementation matches real endpoints.
```

### 1018. D7_s982120_zh (domain=D7, difficulty=7)

```
帮我从零做一个 incidents/postmortems API 工作流工具，代码和文档都一起交付：做一个 FastAPI 服务，支持创建 incident、生成 postmortem 草稿、追踪 action items、以及把事件同步到 Slack 和 Jira 的 webhook 流程。顺手把配置、示例 `.env.example`、`README.md`、和一套可跑的测试都补齐，文件名你自己定，但要能直接跑起来。
```

### 1019. D7_s982123_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops automation tool from scratch that helps with postmortems and API-driven workflows: it should take a manually entered incident summary, generate a structured postmortem draft, and push a follow-up checklist to a webhook or REST endpoint. Please create the code files, tests, and a short README; use current web research on best-practice postmortem formats and a couple of real API/webhook libraries before you implement it.
```

### 1020. D7_s982131_en (domain=D7, difficulty=7)

```
Build a small incident automation service from scratch for PagerDuty + Slack + Jira: I want a Python FastAPI app with a CLI that ingests incident webhook payloads, creates a normalized incident timeline, drafts a postmortem markdown report, and can open/update a Jira ticket and post to Slack. Put the code in app.py, cli.py, and tests/; add a README.md with setup and usage.
```

### 1021. D7_s982132_zh (domain=D7, difficulty=7)

```
帮我从零写一个事件/事故响应自动化小工具，代码和文档一起交付。我要一个可直接运行的 Python 项目：命令行接收告警事件，自动生成事件工单、拉取相关 API 状态、输出初版 postmortem 模板，并把流程串成可扩展的工作流。
```

### 1022. D7_s982159_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops tool from scratch for our team: a webhook-driven incident intake service that accepts alerts, normalizes them, opens or updates incidents, and generates a draft postmortem timeline from the event history. Please research the best current approach for a lightweight Python API stack, webhook verification patterns, and a couple of incident-management API examples so the design is sensible, then produce the code and a short README. There are no input files — just build the app, tests, and docs.
```

### 1023. D7_s982169_en (domain=D7, difficulty=7)

```
Build a small incident-ops workflow service from scratch for PagerDuty-style triage: I want a FastAPI app with a rules engine that ingests incident webhooks, classifies severity, assigns an on-call team, and creates a postmortem task bundle. Add a CLI for replaying incidents and exporting the workflow decisions to JSON, plus a README and tests. Use current docs for FastAPI, Pydantic, and at least one real webhook/API pattern so the design matches modern practice.
```

### 1024. D7_s982205_en (domain=D7, difficulty=7)

```
Build a from-scratch incident workflow service in Python: `incident_router.py`, `postmortem_bot.py`, and `README.md`. I want a small FastAPI app plus a CLI that creates incidents, assigns owners, tracks status changes, and generates a postmortem template from an incident timeline. Use current best practices for Slack and PagerDuty-style webhook handling, and research any relevant API patterns before you code.
```

### 1025. D7_s982270_en (domain=D7, difficulty=7)

```
We need a small internal incident-ops tool because our team is still copying incident updates between Slack, Jira, and our postmortem doc by hand, and we keep missing follow-ups. Please build the code from scratch for a lightweight service that can create an incident record, track status changes, auto-generate a postmortem draft, and push a simple workflow update through an API. Use current best practices for whichever stack you think is most practical, but make the design choices yourself after checking recent docs for the relevant libraries and APIs. I want the finished code files and a short README that explains how to run it locally and how the workflow works.
```

### 1026. D7_s982308_en (domain=D7, difficulty=7)

```
Build a small incident-automation tool from scratch for a real DevOps workflow, inspired by how teams use Slack, Jira, and PagerDuty-style incident handling.
- I want a working backend service that can ingest incident events, group related alerts into incidents, and generate a postmortem draft when an incident is resolved.
- Use current public docs to pick sensible APIs/libraries and implement against one lightweight, real integration path or a clean mock adapter if auth is impractical.
- Include a simple CLI or HTTP API so I can create incidents, append timeline events, resolve them, and export the postmortem in Markdown.
- Make the workflow opinionated but realistic: dedupe noisy alerts, track severity/status/owners, and keep an audit trail of actions.
- Add tests and a short README showing how to run it locally and exercise the main incident lifecycle.
```

### 1027. D7_s982341_en (domain=D7, difficulty=7)

```
We need a small internal incident-ops tool because our team keeps losing time during outages when updates, handoffs, and postmortem follow-ups live in different places. Please build a from-scratch command-line app for incident workflow automation that helps us create an incident, log timeline updates, assign owners, generate a clean postmortem draft, and export the result as Markdown and JSON. I want it to feel practical for a real operations team, not a demo, and it should be easy to use without a database or external account. Please research a few current best practices and lightweight libraries first so the design matches common incident-management workflows, then build the code, tests, and a short README for how to run it.
```

### 1028. D7_s982362_zh (domain=D7, difficulty=7)

```
我需要你从零开发一个面向值班和事故响应的轻量工具，做成一个可运行的命令行小项目，最好顺手带一个简单的本地 HTTP 接口；核心是把事故记录、时间线、行动项和复盘模板串起来，支持从 API 拉取工单/告警事件、自动生成 postmortem 草稿、导出 Markdown 和 JSON，并能按服务名和严重级别查询历史事故。你先帮我把项目代码、README 和必要测试都搭好，后面我再接到现有流程里。
```

### 1029. D7_s982371_en (domain=D7, difficulty=7)

```
Build a from-scratch incident workflow service for our on-call team: a small Python app with FastAPI that creates incidents, tracks status changes, and auto-generates postmortem drafts from incident metadata and timeline events. Add a Slack webhook notifier and a GitHub Issues exporter, with config in env vars and a clean CLI to run local dev tasks. Put the code in app/, tests in tests/, and include a README.md with setup and usage.
```

### 1030. D7_s982372_zh (domain=D7, difficulty=7)

```
给我从零做一个“事故响应工作流”小工具：用 Python 写一个可运行的 CLI + 本地 HTTP 服务，支持创建 incident、更新状态、生成 postmortem 模板、导出 Markdown/JSON，并把 Slack/Jira/GitHub Issues 的 webhook/API 对接都留成可配置模块。顺手把 README、示例配置、单元测试一起补齐，代码放在 app.py、workflow.py、integrations/、tests/ 这些文件里。先按现成最佳实践把技术方案和依赖选型研究清楚再实现。
```

### 1031. D7_s982392_en (domain=D7, difficulty=7)

```
I want a small internal incident-response tool built from scratch for SRE/on-call work.
- Build a CLI that can open an incident, generate a postmortem draft, and export a timeline from a set of API calls or pasted notes.
- Use current best practices and a couple of real public APIs/libraries for reference before coding, especially for incident management and markdown/JSON export patterns.
- Make it usable as a standalone repo with clear commands, tests, and docs so another engineer can run it locally.
- Include a lightweight workflow for tagging owners, action items, and follow-ups, not just a one-off script.
- I want the code, tests, and README, not a research-only answer.
```

### 1032. D7_s982396_en (domain=D7, difficulty=7)

```
Build a small incident automation service from scratch for PagerDuty-like workflows: Python FastAPI backend, a React admin UI, and a CLI to create incidents, start postmortems, and trigger API actions against mock/webhook endpoints. I want the repo scaffolded with the core code, tests, and README.md, and please use current docs for FastAPI, React, and one workflow/orchestration library before implementing.
```

### 1033. D7_s982426_en (domain=D7, difficulty=7)

```
We need a small internal tool to speed up how we handle incidents and the postmortem follow-up, because right now everything lives in Slack and scattered notes and it’s easy to miss owners, timelines, and action items. Build a from-scratch workflow app that lets us create an incident, update its status, capture key events, and generate a clean postmortem summary with action items we can copy into our process. I want the code and a short README so someone on the team can run it locally and understand how it works. Please research a few sensible implementation options first so the design fits modern API and workflow patterns, then build the actual app from scratch rather than using a starter template.
```

### 1034. D7_s982443_en (domain=D7, difficulty=7)

```
Build a small incident-ops workflow service from scratch: a Python FastAPI app with an API for creating incidents, generating postmortem templates, and triggering Slack/Jira webhook actions, plus a CLI for local use. I want app.py, a README.md, and tests that cover the incident lifecycle and webhook routing.
```

### 1035. D7_s982469_en (domain=D7, difficulty=7)

```
Build a small incident-automation service from scratch for Slack and Jira: I want a Python FastAPI app with a webhook receiver, a postmortem draft generator, and a CLI to create incident summaries and follow-up tasks. Put the code in app.py and tests in tests/test_app.py, and add a README.md with setup and usage.
```

### 1036. D7_s982479_en (domain=D7, difficulty=7)

```
Build a small incident automation service from scratch in Python: a FastAPI app that ingests PagerDuty-style incident webhooks, creates a normalized incident record, runs a webhook retry worker, and generates a postmortem markdown draft from a template. Put the code in app/, tests in tests/, and include a README.md with setup and run instructions.
```

### 1037. D7_s982487_en (domain=D7, difficulty=7)

```
I want a small but real incident-management automation tool built from scratch for our team. Please make it practical for API-driven ops workflows and not just a demo.

- Build a command-line tool that can create an incident, open a postmortem draft, and generate a follow-up task checklist from a short incident summary.
- Use current best practices from the web for incident/postmortem structure and at least one real API workflow or library choice you verify online.
- Keep it self-contained with no input files; the tool should work from flags/typed text and produce useful output files or terminal output.
- Include tests, a README with setup/run examples, and a clear internal module design so it’s easy to extend later.
- I want the code, not a research memo — but the implementation should reflect up-to-date research you do before building it.
```

### 1038. D7_s982507_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops workflow tool from scratch that helps a team draft postmortems and run incident follow-ups: include a webhook/API service, a CLI to create/update incidents and action items, and a rule-based engine that can auto-generate a postmortem template from incident fields and timelines. Please use current best practices for the API framework and any library choices, and base the design on real integrations like Slack and GitHub issue workflows where it makes sense. I want the finished code plus a short README explaining how to run it, plus tests.
```

### 1039. D7_s982519_en (domain=D7, difficulty=7)

```
I need you to build a small from-scratch incident automation tool for ops teams: a Python service/CLI that ingests a JSON incident event, opens or updates a postmortem template, and can trigger follow-up API workflows like Slack alerts, Jira ticket creation, and a GitHub issue when an incident is marked resolved. Please research the current API/auth patterns for Slack, Jira, and GitHub first, then implement the code, tests, and a short README with setup and usage examples. There are no input files; just build the project and make sure it’s cleanly organized and runnable.
```

### 1040. D7_s982539_en (domain=D7, difficulty=7)

```
Build a from-scratch Python incident automation service for PagerDuty-style workflows: ingest a POST /incidents webhook, enrich it with Slack and Jira actions, and generate a postmortem markdown report with timeline, owners, and follow-ups. Put the code in app.py, tests in test_app.py, and setup/instructions in README.md; no starter files or input data, just build it.
```

### 1041. D7_s982541_en (domain=D7, difficulty=7)

```
Build a small incident postmortem automation tool from scratch for Slack/GitHub workflows. I want a working CLI plus a lightweight API service in src/ that can create incident timelines, generate a postmortem markdown report, and post status updates to Slack or GitHub via pluggable adapters. Include README.md with setup/run steps and tests for the core workflow.
```

### 1042. D7_s982613_en (domain=D7, difficulty=7)

```
Build a small incident automation service from scratch for PagerDuty + Slack. I want a FastAPI app with a webhook endpoint that ingests incident events, a rules engine that maps severity/service to Slack routing and postmortem templates, and a minimal CLI for replaying sample events and generating a postmortem draft. Put the code in app/ and include tests plus a README with setup and usage.
```

### 1043. D7_s982622_en (domain=D7, difficulty=7)

```
Build a from-scratch incident automation service in Python for our ops workflow that can ingest incident updates over HTTP, generate a structured incident timeline, and emit a postmortem draft with the standard sections we use (summary, customer impact, root cause, contributing factors, detection, mitigation, action items). I want a small but production-shaped codebase, not a toy script: expose a FastAPI app with endpoints for creating incidents, appending timeline events, and rendering a postmortem markdown document; include a minimal CLI for local use; and wire in a pluggable adapter layer for Slack and Jira-style outbound actions so we can later connect real webhooks.

Use web research where it helps to confirm current FastAPI/Pydantic patterns, markdown rendering libraries, and practical webhook/auth handling approaches, then implement everything from scratch with no starter files or dataset. Keep the design clean enough that each major module can be built independently and then integrated. I want the built code files and a short README with setup and usage.
```

### 1044. D7_s982662_zh (domain=D7, difficulty=7)

```
我需要你从零做一个面向运维值班的事件自动化小工具，最好是一个可直接运行的 Python 项目：它能接收一次事故的手工输入（比如标题、时间线、影响范围、处理动作、负责人、恢复时间），自动生成一份结构化 postmortem 草稿，并支持把总结通过 GitHub Issues 或 Jira API 发出去，另外再带一个简单的本地命令行界面方便值班同学创建、查看和导出事件。请顺手把项目目录、核心代码、测试和 README 都一起补齐，重点是要能真实落地，不是只写示意代码。
```

### 1045. D7_s982697_en (domain=D7, difficulty=7)

```
Build a small incident-automation service from scratch that ingests PagerDuty and Jira webhooks, creates a normalized incident timeline, and generates a postmortem draft in Markdown. Put the core logic in src/, expose it through a FastAPI app in app.py with endpoints for webhook intake, incident status, and postmortem export, and include a README.md with setup and usage. Research the current webhook payload shapes and any relevant FastAPI/Pydantic best practices first, then implement and test it.
```

### 1046. D7_s982739_en (domain=D7, difficulty=7)

```
I want a small but realistic incident-automation tool built from scratch for our ops team, not a mockup. Please implement a working command-line utility that helps create and manage incident postmortems with API-driven workflows.
- It should let me open an incident, add timeline entries, attach action items, and generate a polished postmortem markdown report.
- I want the design to be based on a quick review of real incident-management and webhook/API patterns from current docs, then implemented cleanly in code.
- Include a simple local storage layer so it works offline, plus validation and error handling for bad inputs.
- Add a few unit tests and a short README showing how to run it and extend it.
- Keep it self-contained: no input files, just the code and docs you create.
```

### 1047. D7_s982791_zh (domain=D7, difficulty=7)

```
帮我从零写一个可运行的 Python 工具，做“事故响应 + 复盘”自动化：输入一条工单/告警标题和一组手工事件 JSON，就能生成 incident timeline、分级建议、复盘模板和可发 Slack 的摘要。请直接产出代码文件和 README，CLI 要能本地运行。先去查一下 PagerDuty、Slack incoming webhook、以及常见 postmortem 结构的最佳实践，再开始实现。
```

### 1048. D7_s982792_en (domain=D7, difficulty=7)

```
Build a small Python service from scratch for incident ops automation: ingest PagerDuty- and Slack-style webhook payloads, normalize them into one incident model, generate a basic postmortem draft, and expose it through a FastAPI API plus a CLI. Use current best practices and verify any webhook/signature handling, incident-status conventions, and FastAPI patterns with web research first; then implement the code, tests, and a README.
```

### 1049. D7_s982805_en (domain=D7, difficulty=7)

```
Build a small incident-workflow service from scratch for postmortems: I want a FastAPI app plus a CLI that can create incidents, add timeline events, generate a postmortem template, and export the result as Markdown in the repo. Use a durable local store, add tests, and include a short README with setup and usage. Research current FastAPI/Pydantic patterns and a good Markdown export approach before you code.
```

### 1050. D7_s982875_en (domain=D7, difficulty=7)

```
Build a small incident-automation service from scratch for PagerDuty/Slack-style workflows. I want a webhook receiver, a postmortem generator, and a rule engine that routes incidents, dedupes alerts, and emits follow-up tasks; put the code in app.py with tests in test_app.py and a short README.md showing how to run it locally. Use current web research for a couple of real API patterns and best-practice references, then implement everything cleanly with no starter files or input data.
```

### 1051. D7_s982931_en (domain=D7, difficulty=7)

```
Build a small but realistic incident-ops workflow tool from scratch for on-call teams. I want something I can actually run locally to manage incident timelines, action items, and postmortem drafts without relying on a spreadsheet.
- Make it a CLI app with commands to open an incident, add/update timeline entries, assign owners to follow-ups, and generate a postmortem markdown draft.
- Include a lightweight storage layer and a clean data model so incidents persist across runs.
- Add sensible validation, helpful error messages, and a few example workflows in the README.
- Use current best practices from the web for incident/postmortem structure and whichever library choices you make.
- Please deliver the built code and a short README with setup, usage, and testing instructions.
```

### 1052. D7_s982960_zh (domain=D7, difficulty=7)

```
给我从零做一个 Python 工具，做值班事故的复盘和后续行动自动化：能接收一段事故时间线/会议纪要，输出结构化 postmortem Markdown，并自动生成 Jira/GitHub issue 的待办条目草稿。把代码放在 `src/`，CLI 做成 `pmflow`，再写 `README.md` 和最少一套测试。需要你先查一下目前比较稳妥的 Python Markdown 生成、CLI 参数解析、以及 Jira/GitHub API 请求封装的最佳实践，再开始实现。
```

### 1053. D7_s982975_en (domain=D7, difficulty=7)

```
I need you to build a small incident-automation tool from scratch that helps ops teams create, track, and close incidents plus generate a clean postmortem draft. Make it a real code project, not a mockup: include the core logic, a CLI or tiny API for creating incidents and updating status, automatic timeline/event capture, a postmortem template generator, and a couple of example workflows for things like alert intake, escalation, and resolution. Use current web research where it helps, especially for best practices around incident management and any relevant Python/Node libraries or APIs you’d want to integrate with. Please deliver the finished code and a README with setup and usage.
```

### 1054. D7_s982995_en (domain=D7, difficulty=7)

```
Build a small incident-ops workflow tool from scratch: a Python service that creates incident timelines, generates postmortem drafts, and can push/update issues in Jira and Slack via APIs. I want the code in app.py plus a README.md with setup, env vars, and example workflows; no input files. Use current API/library best practices and make it runnable locally.
```

### 1055. D7_s982999_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops workflow tool from scratch for our team: a Python CLI app that can open an incident, generate a structured postmortem checklist, and call external APIs for Slack and PagerDuty style webhook notifications, with a clean README and tests. Please research current best practices and the relevant API patterns before coding, then produce the source files and docs — no starter files, just the finished code.
```

### 1056. D7_s983009_en (domain=D7, difficulty=7)

```
Build a small incident-postmortem workflow service from scratch: I want a FastAPI app with a CLI in `app.py` that lets me create incidents, collect timeline entries, generate a blameless postmortem draft, and export it as Markdown. Pull in current best-practice references for incident templates and API design from the web before coding. Include `README.md` with setup/run instructions and `tests/` covering the main flows.
```

### 1057. D7_s983022_zh (domain=D7, difficulty=7)

```
我需要你从零搭一个面向值班和事故响应的小工具，做成一个可以本地运行的 Python 项目：它要能读取我手动写的 incident 描述，自动生成一份规范的 postmortem 草稿，顺便给出一套 API 工作流检查清单（比如告警确认、回滚、状态页更新、复盘行动项），最好还能把结果导出成 Markdown 和 JSON。你先帮我把项目代码、README、测试都写好，命名尽量贴近实际团队会用的东西，别依赖任何现成模板或输入数据。
```

### 1058. D7_s983068_en (domain=D7, difficulty=7)

```
Build a small incident workflow service from scratch in Python: an API that creates incidents, runs a simple state machine, generates postmortem templates, and posts updates to Slack and Jira via pluggable adapters. I want the code in app.py, the adapter interfaces and implementations, tests, and a README with setup and API examples.
```

### 1059. D7_s983079_en (domain=D7, difficulty=7)

```
Build a small Python service from scratch for incident ops automation: it should create/update incident records, generate postmortem templates, and fan out webhooks to Slack/Jira/PagerDuty-style endpoints with retries and idempotency. I want the code in app.py plus tests and a README.md that explains setup, config, and example flows.
```

### 1060. D7_s983085_en (domain=D7, difficulty=7)

```
I need a small but real internal tool that helps us handle incidents faster and write better postmortems. Please build it from scratch as a working Python service with a simple web UI or API, so our team can create an incident, track status updates, capture timeline notes, and then generate a structured postmortem summary we can copy into our docs. I want it to be practical for a real ops team, not a demo: use sensible defaults, include a way to export the postmortem in Markdown, and make sure the workflow feels like something we could actually adopt. Please research current best practices for incident workflows and any relevant Python libraries or lightweight web framework choices before you build it, then give me the finished code and a short README explaining how to run it.
```

### 1061. D7_s983087_en (domain=D7, difficulty=7)

```
I want a small but real incident-automation tool I can actually run locally for our on-call workflow.

- Build a from-scratch service that can create, update, and resolve incident records, then generate a clean postmortem markdown summary from the timeline and tags.
- Add an API workflow layer for common actions like opening an incident, appending notes, changing severity/owner, and exporting a postmortem draft.
- Include a lightweight CLI so I can use it from terminal as well as through HTTP.
- Use current best practices and real library/API patterns you research first, especially for markdown generation, structured validation, and HTTP API design.
- Ship the code, tests, and a short README showing how to run it locally and exercise the main flows.
```

### 1062. D7_s983091_en (domain=D7, difficulty=7)

```
Build a small incident automation service from scratch: add a Python FastAPI app in `app.py` that ingests PagerDuty- and Jira-style incident webhooks, stores incidents in memory or SQLite, generates a Markdown postmortem template, and exposes API endpoints to create/update incidents and export a postmortem bundle. Add `README.md` with setup/run instructions and example `curl` calls, plus tests for the webhook handlers and postmortem generator. Use current docs for FastAPI, Pydantic, and any webhook-signature or retry best practices you need.
```

### 1063. D7_s983095_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops tool from scratch: a Python service that turns raw incident notes into a structured postmortem draft and can also kick off a simple workflow via an external API like Slack or Jira. Make it real-world usable, with a clean CLI plus a tiny REST API, a rule-based template for incident timelines and action items, and a way to configure integrations with environment variables. Please include the code, tests, and a README with setup and example usage — no starter files or data, just build the whole thing.
```

### 1064. D7_s983099_en (domain=D7, difficulty=7)

```
I want a small but real incident-ops tool built from scratch for our team.
- Build a command-line app that takes an incident timeline, generates a postmortem draft, and can export a clean Markdown report.
- Add an API workflow layer so it can post incident updates to Slack and create follow-up tickets in Jira or Linear.
- Research current Slack and Jira/Linear API patterns and any good Python libraries or SDKs first, then use that to design the implementation.
- Include sensible defaults for templates, error handling, retries, and secrets/env var configuration.
- I want the code, tests, and a short README showing how to run it locally.
```

### 1065. D7_s983103_en (domain=D7, difficulty=7)

```
Build a small Python service from scratch for incident workflow automation: ingest a Slack incident command, create an incident record, generate a postmortem template, and sync updates to Jira and GitHub Issues. Use current API docs for Slack, Jira, and GitHub, then implement the service, a CLI to trigger workflows, and a README with setup and usage.

Put the code in app.py, workflows.py, and cli.py, add tests in test_workflows.py, and include a concise README.md.
```

### 1066. D7_s983117_en (domain=D7, difficulty=7)

```
Build a small incident-ops workflow tool from scratch in Python: a CLI + FastAPI service that can create incidents, generate postmortem skeletons, and call Jira/Slack-style webhooks for status updates. Put the code in app.py, tests in tests/, and add a README.md with setup and usage; use current docs for FastAPI, Pydantic, and any webhook/API best practices you need.
```

### 1067. D7_s983151_en (domain=D7, difficulty=7)

```
Build a small incident/postmortem automation tool from scratch: a Python CLI + local web app that creates incident timelines, collects follow-up actions, and generates a structured postmortem markdown report from user-entered incident notes. Research a couple of current API/workflow patterns first (Slack webhook formatting, GitHub Issues API, and common postmortem templates) and then implement the app, tests, and README.

Put the code in app.py, the report template in templates/postmortem.md, and the docs in README.md.
```

### 1068. D7_s983212_zh (domain=D7, difficulty=7)

```
帮我从零做一个 incident/postmortem 自动化工具，做成一个可运行的 CLI + 本地 Web 界面，支持创建事故、收集时间线、生成复盘草稿、导出 Markdown。代码放在 app.py、workflow.py、templates/ 下面，README.md 里写清楚安装和用法；另外顺手给我一份 research_brief.md，总结你查到的 SRE/incident management 最佳实践和可选库。不要用现成模板，自己实现核心流程。
```

### 1069. D7_s983225_en (domain=D7, difficulty=7)

```
Build a small incident-ops workflow tool from scratch in Python: a CLI and package that opens an incident, posts a Slack-style update, creates a postmortem template, and exports a runbook checklist as JSON. Use real API/library best practices from current docs for Click/Typer, Pydantic, and HTTPX, and make the code clean enough to extend to PagerDuty/Slack later. Put the code in app.py, with tests in tests/, and add a short README.md explaining install, config, and usage.
```

### 1070. D7_s983229_en (domain=D7, difficulty=7)

```
We need a lightweight incident command tool because our on-call process still depends too much on Slack threads and manual follow-ups, and that is making postmortems slower than they should be. Build a small from-scratch app that helps us open an incident, track the timeline, capture owners and actions, and generate a clean postmortem summary we can paste into our docs. I want it to work as a local command-line tool first, with a simple API so we can later connect it to Slack or our internal dashboard. Please research the best current libraries and patterns for a Python-based CLI plus API service, then build the code, tests, and a short README that explains how to run it and how the workflow is meant to be used. No input files are needed; this is a fresh build.
```

### 1071. D7_s983244_zh (domain=D7, difficulty=7)

```
想做一个从零开始的运维自动化小工具，面向值班和事故处理流程，目标是把“告警触发 → 创建工单/事件 → 拉起响应群组 → 生成 postmortem 草稿”这条链路尽量自动化。

- 做一个可本地运行的命令行工具，能接收一段事故描述或 Webhook 事件，自动整理成标准 incident 记录
- 支持把 incident 发送到一个可配置的 API 目标（先做通用 HTTP 接口适配，不绑定单一厂商），并能回写状态
- 生成一份结构化的 postmortem 草稿，包含时间线、影响范围、根因、行动项这些常见字段
- 需要带上合理的配置文件示例、错误处理、日志，以及可运行的测试
- 先做技术调研，参考现成的 incident/postmortem/API workflow 最佳实践，再从零实现代码和文档
```

### 1072. D7_s983247_en (domain=D7, difficulty=7)

```
Build a small incident-ops workflow tool from scratch for our on-call team: a Python service that creates incident records, tracks status transitions, generates a lightweight postmortem template, and can call external APIs for Slack/Jira webhooks. I want the code in app.py plus a README.md with setup, usage, and example commands. No input files; just build the tool and include tests.
```

### 1073. D7_s983251_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops automation tool from scratch that helps us turn a raw incident into a clean postmortem package: it should accept a few manual inputs at runtime, track incident timeline entries, generate a structured postmortem report, and optionally push a summary to Slack and create follow-up tickets through a generic API workflow. Please research current best practices and a couple of real API/library options first, then implement the code, tests, and a short README for running it locally.
```

### 1074. D7_s983289_en (domain=D7, difficulty=7)

```
We need a small internal tool to speed up incident follow-up after outages, because right now the notes, postmortem draft, and action items get scattered across Slack, Jira, and email and people miss what they promised to do. I want you to build the code for a simple workflow app from scratch that can create an incident record, collect timeline events, generate a postmortem draft, and export action items in a clean format for our team to review. Please research a couple of practical options for how teams usually structure incident/postmortem data and any lightweight libraries that would fit a small Python or Node app, then implement the best approach you find. I do not have any input files for you; this should start from zero and include the working code, tests, and a short README so another person can run it and use it right away.
```

### 1075. D7_s983309_en (domain=D7, difficulty=7)

```
Build a small incident-automation service from scratch for PagerDuty + Slack that opens a postmortem workspace, creates an incident timeline, and posts API-driven status updates. I want the code in app.py plus a README.md with setup and usage, no starter files, and use current docs for the APIs and any Python libraries you pick.
```

### 1076. D7_s983385_en (domain=D7, difficulty=7)

```
Our incident response process is still too manual, and it slows down both customer updates and internal follow-up. I want a small but real workflow tool built from scratch that can take a new incident, generate a clean incident record, help draft the first customer status update, and create a postmortem summary with action items after the incident is closed. Please research current, practical options and best practices for incident and postmortem workflows first, then build the tool in code. I want the finished code files plus a short README that explains how to run it locally and how to use it in a simple API workflow. There are no input files to start from.
```

### 1077. D7_s983392_zh (domain=D7, difficulty=7)

```
帮我从零实现一个“事故响应 + 复盘”自动化小工具：用 Python 做一个本地 CLI，支持从 Slack/Email 风格的事件文本生成标准 incident summary、时间线、action items 和 postmortem 草稿，最后输出 Markdown 和 JSON。顺手把 API 对接层、模板引擎、命令行参数、错误处理、以及一套可运行的单元测试都补齐，README 里写清楚安装和用法。
```

### 1078. D7_s983519_en (domain=D7, difficulty=7)

```
I want a small internal tool for incident response and postmortems that we can actually run locally.
- Build a Python service that ingests incident updates from Slack-style webhook payloads, normalizes them, and stores them in SQLite.
- Add an API workflow that can generate a draft postmortem timeline and action-item list from the stored incident events.
- Include a lightweight CLI so ops can create an incident, append updates, and export a markdown postmortem.
- Research a good current stack for the webhook receiver, SQLite persistence, and markdown/API generation patterns before coding.
- Keep it self-contained, with tests and a README showing how to run it end to end.
```

### 1079. D7_s983589_zh (domain=D7, difficulty=7)

```
我们现在要把事故响应和事后复盘流程尽量自动化，不然每次线上出问题都靠人工拉群、手动写复盘，效率很低，也容易漏掉关键步骤。我需要你从零做一个可运行的小工具，帮我们把“事故通知—处理记录—复盘产出”这条链路串起来，尽量贴近真实团队能直接用的样子。

请你先做一点必要的方案调研，再直接实现代码，不要用现成模板拼凑。工具希望包含这些能力：
1）可以从命令行创建一个事故工单，填写事故标题、严重级别、影响服务、开始时间、负责人和当前状态；
2）可以持续追加处理过程日志，自动整理成时间线；
3）可以在事故结束后生成一份结构清晰的复盘草稿，至少包括：事件概述、影响范围、根因、处置过程、行动项、需要跟进的人；
4）最好能支持把结果导出成 Markdown，方便直接贴到 Confluence 或 Notion；
5）如果合适，也请参考一些常见的事故管理或通知工具的做法，看看哪些字段和流程最实用，但最终代码要自己写出来。

我不要求你直接接任何真实账号或外部系统，但希望代码结构以后容易接入 Slack、PagerDuty、Jira 这类工具。请把这个东西做成一个完整的小项目，包含主程序、核心逻辑、必要的测试和使用说明，能在本地跑起来。你自己决定最合理的实现方式，但要尽量简单、可靠、适合小团队日常使用。
```

### 1080. D7_s983637_en (domain=D7, difficulty=7)

```
I need a small internal incident-automation tool built from scratch because we keep losing time during outages and the handoffs between Slack, PagerDuty, and our postmortem notes are too messy. Please build a working prototype that can ingest a simple incident event from the command line or a local API, track the incident timeline, generate a clean postmortem draft, and create follow-up tasks that could be pushed to a ticketing system later. I want the solution to be realistic enough that we could actually pilot it, with a clear README and tests, and I want you to lean on current best practices and up-to-date library choices where needed rather than guessing.
```

### 1081. D7_s983644_zh (domain=D7, difficulty=7)

```
帮我从零写一个事件响应自动化小工具：做一个“P1 事故处置 + 复盘”工作流引擎，支持用 JSON 定义告警路由、自动建群/开工单、阶段性状态更新和事后复盘模板生成。代码放到 `incidentflow/`，至少包含 `engine.py`、`cli.py`、`templates/`、`tests/` 和 `README.md`，直接给我可运行的实现。
```

### 1082. D7_s983679_en (domain=D7, difficulty=7)

```
Build a from-scratch incident workflow tool in Python for our SRE team: a small FastAPI service plus CLI that opens incidents, adds timeline events, generates postmortem drafts, and exports a Slack-ready summary. Use current best practices for incident/postmortem workflows and any sensible open-source libraries after checking the web first. Put the code in app.py, cli.py, and tests in test_incidents.py, with a short README.md for setup and usage.
```

### 1083. D7_s983745_en (domain=D7, difficulty=7)

```
Our incident process is too manual and too slow, and I want a small internal tool that helps the team run incidents and write postmortems without everything living in chat. Build a from-scratch command-line app that can create an incident record, add timeline entries, assign owners, track status changes, and generate a clean postmortem draft at the end. I also want it to fit a real workflow, so please research a couple of current incident-management and postmortem best practices and use sensible defaults rather than guessing. Deliver the code, tests, and a short README showing how to use it.
```

### 1084. D7_s983789_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops tool from scratch that helps on-call teams turn a Slack incident report into a structured postmortem draft and follow-up task list. Make it support a simple API or CLI for creating an incident, adding timeline events, generating a postmortem template, and exporting JSON/Markdown, and include a short README with setup and usage. Please use current docs for any libraries or APIs you pick, and make sure the code is clean enough to extend later.
```

### 1085. D7_s983865_en (domain=D7, difficulty=7)

```
We keep losing time during incidents because updates, handoffs, and postmortems are scattered across Slack, Jira, and email, and I want a small internal tool that makes the process consistent and faster. Please build a from-scratch incident workflow service that can create an incident record, generate a simple timeline from manual updates, assign follow-up actions, and export a postmortem summary I can share with leadership. It should support a basic API and a command-line way to use it, and it should be practical enough that an engineering team could actually run it internally. I need the built code and a short README explaining how to use it.
```

### 1086. D7_s983874_zh (domain=D7, difficulty=7)

```
我需要你从零做一个用于事故处理和复盘的工作流小工具，目标是把一次 incident 的时间线、行动项、责任人和状态都整理成一份可追踪的 postmortem 记录，并能通过 API 触发常见流程，比如创建事故、追加事件、生成复盘草稿和导出摘要。请先做一点 web 调研，看看现成的 incident/postmortem 工作流、常见字段设计、以及适合做这种服务的 Python/FastAPI 或类似库的最佳实践，然后直接把代码和说明文档一起做出来；我不需要输入文件，代码要从头实现，最好还能带上测试和一个简单的命令行入口，方便本地启动和演示。
```

### 1087. D7_s984171_en (domain=D7, difficulty=7)

```
Build a small incident automation service from scratch for our ops team: a Python FastAPI app with a CLI that can create incidents, add timeline updates, generate a Markdown postmortem draft, and trigger a follow-up workflow via webhook to Slack or Jira. Put the code in app/, include tests in tests/, and write a concise README.md with setup and usage.
```

### 1088. D7_s984190_en (domain=D7, difficulty=7)

```
I want a small but real incident-ops tool built from scratch for our on-call workflow.
- Build a command-line app that can open a service incident, add timeline updates, and generate a postmortem draft with sections for impact, root cause, detection, mitigation, and follow-ups.
- Use current best-practice patterns for incident handling and postmortems, and research a couple of real vendor APIs or libraries first so the design fits common workflows.
- Include a simple local persistence layer so incidents and updates survive restarts, plus a clean JSON export for downstream automation.
- Add practical validation and tests so bad incident data is rejected and the generated postmortem output is predictable.
- Write concise usage docs and examples so another engineer can run it right away.
```

### 1089. D7_s984225_en (domain=D7, difficulty=7)

```
We keep losing time during incidents because handoffs, status updates, and postmortem notes are scattered across Slack, Jira, and our API tools. I want a small internal incident-ops tool built from scratch that helps us create an incident, track updates, and generate a clean postmortem draft at the end. Please design and build the code for it, using whatever modern approach you think is best. I want it to be practical for a real ops team: it should accept incident details, let us add timeline entries, support a few workflow actions like acknowledging, escalating, and resolving, and then export a readable postmortem summary we can share. Use web research where helpful to choose sensible libraries and current best practices, but do not rely on any starter files or sample data. Deliver the finished code and a short README explaining how to run it.
```

### 1090. D7_s984279_en (domain=D7, difficulty=7)

```
Build a small incident automation service from scratch for our on-call workflow: a Python FastAPI app that ingests PagerDuty-style incident webhooks, creates a postmortem draft, and exposes a CLI to generate/update incidents and postmortems. Put the code in app.py, the tests in tests/, and a short README.md with run instructions and sample requests.
```

### 1091. D7_s984315_en (domain=D7, difficulty=7)

```
Build a from-scratch incident automation service for Jira Service Management + Slack that opens incident tickets from a webhook, posts updates to Slack, and generates a postmortem markdown draft with timeline, impact, root cause, and action items. I want the code in app.py, tests in tests/, and a short README.md with setup and API usage.
```

### 1092. D7_s984519_en (domain=D7, difficulty=7)

```
Build a small incident automation service from scratch for PagerDuty-style workflows: a FastAPI app plus CLI that lets me create incidents, run a postmortem checklist, and call external APIs through configurable webhooks. I want app.py, cli.py, workflow_engine.py, tests/, and README.md; include a sample YAML config schema and no starter data files.
```

### 1093. D7_s984574_en (domain=D7, difficulty=7)

```
I want a small but production-minded incident workflow tool built from scratch for on-call use.

- Build a Python service that ingests incident updates over HTTP, tracks incident state, and generates a postmortem draft when the incident is closed.
- Add one CLI so responders can create an incident, append updates, change severity/status, and export the final timeline as Markdown.
- Research and use a sensible stack for async APIs and validation, plus a lightweight persistence option that doesn’t need a big external system.
- Include a clean data model for incidents, updates, owners, timestamps, severity, status transitions, and postmortem sections like impact, root cause, contributing factors, and action items.
- Add tests for the state machine, API endpoints, and postmortem generation, and include a README with setup, example commands, and operational notes.
```

### 1094. D7_s984580_en (domain=D7, difficulty=7)

```
Build a small incident-automation service from scratch for our ops team: create `incident_bot.py` and `README.md` for a FastAPI app that can open an incident, collect update templates, generate a postmortem outline, and call Slack + PagerDuty webhooks. Research the current Slack incoming webhook and PagerDuty Events API guidance first, then wire the code so the integrations are configurable by env vars and fully testable with mocked requests.
```

### 1095. D7_s984602_zh (domain=D7, difficulty=7)

```
帮我从零实现一个用于事故响应和复盘的轻量工具，输出代码和 README：做一个支持“事件创建 / 状态流转 / 复盘草稿生成 / 通过 API 推送到 Slack 和 Jira”的小型服务，文件名你自己定，但要能直接跑起来。先用 web 查一下 Slack Incoming Webhooks、Jira REST API、以及适合做任务编排/重试的 Python 库最佳实践，再开始写代码。
```

### 1096. D7_s984607_en (domain=D7, difficulty=7)

```
I need you to build a small incident-ops tool from scratch for our team: a Python service that ingests PagerDuty-style incident webhooks, auto-generates a structured postmortem draft, and exposes a simple CLI plus HTTP API to create, list, and resolve incidents. Please research a couple of current webhook/event formats and a good lightweight stack before coding, then produce the working code and a README explaining setup, endpoints, and example commands.
```

### 1097. D7_s984639_en (domain=D7, difficulty=7)

```
Build a from-scratch incident automation tool for Slack + Jira: create a small Python service that ingests incident webhook payloads, opens/updates Jira issues, posts status updates to Slack, and generates a postmortem markdown template after resolve. I want the code in app.py, tests in tests/, and a README.md with setup and example payloads; no input files, just implement it.
```

### 1098. D7_s984731_en (domain=D7, difficulty=7)

```
I want a small but real incident-ops tool built from scratch for our on-call team.

- Build a Python CLI that creates incident timelines, tracks owners/actions, and generates a polished postmortem markdown report from an incident JSON you define.
- Include a lightweight API client layer for Slack and Jira so the tool can post an incident summary and open follow-up tickets, but make it work with mocked/local config by default.
- Add a local storage layer for incidents, action items, and postmortem drafts so it can resume work across runs.
- Make the workflow practical: validate inputs, support status transitions, and produce a clean summary suitable for handoff and review.
- I need tests and a README with setup, example commands, and the data model/API assumptions you chose.

Use current Python tooling and follow best practices for whichever libraries you pick, but implement the whole thing from scratch.
```

### 1099. D7_s984771_zh (domain=D7, difficulty=7)

```
帮我从零实现一个“事故响应 + 复盘”自动化工具，参考 PagerDuty / GitHub / Slack 的常见工作流，但不要接任何真实账号；代码里做成可配置的模拟适配器，支持创建 incident、同步状态、生成复盘草稿、导出 webhook 事件。请直接给出可运行的代码和 README.md，文件名就按你设计的来，别只写方案。
```

### 1100. D7_s984873_zh (domain=D7, difficulty=7)

```
我们现在每次出故障后，复盘材料都靠人工拼：事故时间线、影响范围、相关 API 调用、处理过程、根因和后续动作分散在聊天记录和工单里，整理慢，而且容易漏项。我想做一个从零开始的内部工具，帮助值班同学把一次线上事故快速整理成一份标准化的 postmortem，并且能把常见的 API 流程串起来，自动留痕、生成时间线、导出总结，方便后面审计和复盘。

请你直接帮我设计并实现这个工具的代码。你需要先自己查一下现成做法和可用库，看看事故复盘、工单自动化、API 工作流这类工具一般怎么设计，再从头写出一个可运行的方案。最后交付完整代码和说明文档，要求能本地运行、能创建事故记录、能追加事件、能生成一份可读的复盘输出，并且支持基本的 API/命令行操作。不要依赖我提供任何输入文件，全部从头实现。
```

### 1101. D7_s984888_zh (domain=D7, difficulty=7)

```
我需要你从零开始构建一个轻量级的工单管理CLI工具，用于运维和事件响应场景。这个工具要能记录事件（incidents）、执行事后复盘（postmortems）并触发简单的API工作流（比如通知Slack或PagerDuty）。不要给我任何预置数据文件——完全从零写代码。

具体要求如下：
1. **数据模型**：事件至少包含 id（UUID）、标题、描述、严重级别（critical/major/minor）、状态（open/investigating/resolved/closed）、创建时间、关闭时间。事后复盘记录包含事件ID、触发原因、影响范围、时间线、行动项列表。
2. **存储**：用SQLite本地存储，数据库文件由工具自动创建。
3. **CLI命令**：
   - `incident-cli log`：交互式创建事件，接收必要字段，自动生成ID和时间戳。
   - `incident-cli list`：列出所有事件，支持按状态过滤、排序（默认按创建时间降序）。
   - `incident-cli close <id>`：关闭对应事件，记录关闭时间。
   - `incident-cli postmortem <id>`：对已关闭事件创建事后复盘，交互式输入各字段，输出Markdown报告到当前目录。
4. **API集成**：至少集成两个真实的外部API。
   - Slack：当事件被记录时，通过Webhook发送通知（需要环境变量 SLACK_WEBHOOK_URL）。
   - 另一个可选PagerDuty（使用Events API v2）或Mailgun（发送邮件）。需要实际调用API，不能只是打印模拟。
5. **健壮性**：使用环境变量管理敏感凭据；网络请求失败时友好提示并继续；支持重试机制（指数退避）。
6. **单元测试**：用pytest编写至少5个测试，覆盖核心逻辑、存储操作、CLI解析（mock外部API调用）。测试可独立运行。
7. **文档**：README.md包含安装步骤、环境变量说明、每个命令的用例、以及如何运行测试。

注意：所有代码从零写，不要依赖任何已有的事件管理库（但可以使用requests、sqlite3、argparse等标准或常见库）。你需要先上网搜索PagerDuty和Slack的API文档、最佳实践、以及Python中如何实现指数退避重试。然后并行实现各个模块。最终输出一个可运行的Python包（main.py或app.py）加README.md和requirements.txt。

请确保你的实现考虑了以下边界情况：
- 用户输入空标题或无效严重级别时给出明确报错。
- SQLite数据库文件不存在时自动创建初始表。
- 事件ID冲突（理论上UUID不冲突，但代码仍需处理）。
- 网络请求超时或返回非2xx时记录错误日志但不中断整体操作。
- 事后复盘的时间线字段支持多行输入。
```

### 1102. D7_s984916_en (domain=D7, difficulty=7)

```
Build a small incident-automation service from scratch for Slack + PagerDuty workflows. I want the code in app.py plus a README.md, with a local API that can create incidents, generate a postmortem skeleton, and open a remediation checklist from a webhook payload. Use current Slack and PagerDuty API/docs patterns in the implementation, and keep everything runnable locally with mocked integrations by default.
```

### 1103. D7_s985054_en (domain=D7, difficulty=7)

```
Build a small but real incident-ops automation tool from scratch for SRE use: a CLI app that ingests an incident report in plain text, extracts the key facts, and generates a clean postmortem draft plus a follow-up checklist.
- I want the core parser, incident/postmortem data model, and a rule-based extraction pipeline implemented from scratch.
- Add a CLI with commands to create a draft, validate the report for missing sections, and export Markdown/JSON.
- Research current best practices and relevant APIs/libraries first so the design matches modern incident-management workflows.
- Include tests and a short README with usage examples and design notes.
- No input files are provided; create the feature and sample fixtures yourself.
```

