# @grok Trigger Examples

All triggers are written as comment text in GitHub issues, pull requests, or commit message bodies. Grok reads the `@grok` mention and dispatches to the spec file that matches the command.

**Format:** `@grok <command> [arguments]`  
**Context:** Any issue comment, PR review comment, or PR description.

---

## 1 — Agents

Spawn and interact with persistent agents defined in [`grok-agent.yaml`](.grok/grok-agent.yaml).

| Trigger | What happens |
|---------|-------------|
| `@grok spawn agent:CodePartner` | Spawns `CodePartner` with the tools and memory defined in `grok-agent.yaml`. The agent reads the current issue or PR for context. |
| `@grok spawn agent:DeepResearcher` | Spawns the reasoning agent (uses `grok-4-reasoning`). Best for long research or multi-source analysis tasks. |
| `@grok spawn agent:Orchestrator` | Spawns the orchestrator. Routes sub-tasks to `FastClassifier` or `DeepResearcher` via subsequent workflow steps. |
| `@grok agents list` | Lists all agents defined in `grok-agent.yaml` with their memory mode and tool count. |
| `@grok agent:CodePartner what is the status of the open refactor tasks?` | Sends a direct query to a running session of `CodePartner`. The agent replies inline. |

**Tips:**
- Agents with `memory: long_term` remember context across sessions in the same repo.
- `max_turns_per_session` limits how many back-and-forths one invocation can run.
- Pair with `grok-workflow.yaml` to chain agent output into downstream steps.

---

## 2 — Workflows

Run and control multi-step pipelines defined in [`grok-workflow.yaml`](.grok/grok-workflow.yaml).

| Trigger | What happens |
|---------|-------------|
| `@grok run workflow:ReleasePipeline` | Executes the `ReleasePipeline` workflow — runs tests, scans, deploys to staging, then pauses at `approval_required` steps. |
| `@grok run workflow:ContentPipeline` | Runs the content pipeline: drafts X thread and newsletter from the current PR description, then waits for approval before posting. |
| `@grok run workflow:ResearchAndPublish` | Executes parallel web + X search, synthesizes findings, conditionally critiques, then posts with an approval gate. |
| `@grok workflow:ReleasePipeline status` | Returns the current step, last output, and any pending approval gates. |
| `@grok workflow:ReleasePipeline abort` | Immediately halts the workflow. No deploy or post actions will proceed. |

**Tips:**
- Steps without `depends_on` run in parallel when the runtime supports it.
- `approval_required: true` pauses at that step — reply `@grok approve` or `@grok reject` to resume or abort.
- `on_failure: notify_user` keeps the thread alive even when a step errors.

---

## 3 — Security & Compliance

Run scans defined in [`grok-security.yaml`](.grok/grok-security.yaml).

| Trigger | What happens |
|---------|-------------|
| `@grok security scan` | Runs all enabled scans against the current PR diff. Reports findings as PR comments with severity and remediation hints. |
| `@grok security scan:SecretsScan` | Runs only the `SecretsScan` scan definition (fastest, lowest false-positive rate). |
| `@grok security scan:VulnerabilityScan` | Runs dependency CVE and SAST scan. Returns a structured JSON report. |
| `@grok security scan:ComplianceScan` | Checks against declared `compliance_standards` (GDPR, PCI-DSS, etc.). Generates an audit log entry. |
| `@grok security report` | Summarises findings from all scans run on this PR since it was opened. |

**Tips:**
- Scans with `frequency: on_commit` run automatically — the trigger above forces a manual re-run.
- `auto_block_prs: true` blocks merge if a `fail_on_finding: true` scan finds a critical issue.
- Never disable `SecretsScan` on a PR that touches `.env`, config, or CI files.

---

## 4 — Prompts & Content

Invoke reusable templates from [`grok-prompts.yaml`](.grok/grok-prompts.yaml).

| Trigger | What happens |
|---------|-------------|
| `@grok use prompts:viral_thread topic:"Building in public" tone:"bold"` | Runs the `viral_thread` template with the given variable values. Outputs an 8-tweet thread draft. |
| `@grok use prompts:code_review language:"TypeScript" focus:"security" code:<paste diff>` | Runs structured code review using the `code_review` template. Returns a severity-annotated markdown checklist. |
| `@grok use prompts:product_idea` | Runs the `product_idea` template — generates a structured product brief from the current issue body. |
| `@grok prompts list` | Lists all entries in `prompt_library` with their description and required variables. |

**Variable passing:** Inline after the prompt key as `key:"value"` pairs. Required variables listed in the template definition under `variables:`.

**Tips:**
- Templates with `cache_responses: false` always generate fresh output — important for creative or compliance-sensitive prompts.
- `system_prompt` is a static layer that variable values cannot override — brand rules and compliance constraints live there.
- `reasoning_mode: high` engages extended thinking; always set `max_tokens` when using it to cap cost.

---

## 5 — Testing & Docs

Run test suites from [`grok-test.yaml`](.grok/grok-test.yaml) and regenerate docs from [`grok-docs.yaml`](.grok/grok-docs.yaml).

| Trigger | What happens |
|---------|-------------|
| `@grok test` | Runs all enabled test suites in `grok-test.yaml` against the changed files in the PR. |
| `@grok test suite:CodeQuality` | Runs only the `CodeQuality` suite. Faster for targeted feedback. |
| `@grok test suite:SecuritySmokeTest` | Runs only the security smoke test. Pairs with `grok-security.yaml` scans for defence-in-depth. |
| `@grok docs` | Regenerates all documentation targets in `grok-docs.yaml` — typically `AutoREADME` and `APIDocs`. |
| `@grok docs target:AutoREADME` | Regenerates only the `AutoREADME` target. |
| `@grok docs target:APIDocs` | Regenerates only the API reference documentation. |

**Tips:**
- `grok-test.yaml` suites with low `temperature` (0.1–0.2) give deterministic, repeatable results.
- Pair `@grok test` with `grok-security.yaml`'s `block_merge_on_fail: true` to enforce a hard test gate.
- Doc targets with `update_on: pr_merged` update automatically — the trigger forces a manual refresh.

---

## 6 — Deploy & Update

Deploy to targets defined in [`grok-deploy.yaml`](.grok/grok-deploy.yaml) and run update jobs from [`grok-update.yaml`](.grok/grok-update.yaml).

| Trigger | What happens |
|---------|-------------|
| `@grok deploy staging` | Deploys the current branch to the `staging` target. Runs health checks after deploy. |
| `@grok deploy production` | Deploys to `production`. Pauses at the `require_approval` gate if set; waits for explicit approval. |
| `@grok deploy staging rollback` | Rolls back the `staging` environment to the previous healthy deploy. |
| `@grok update` | Runs all update jobs in `grok-update.yaml` — refreshes the knowledge base and checks dependency CVEs. |
| `@grok update job:KnowledgeBase` | Runs only the `KnowledgeBase` update job. |
| `@grok update job:DependencyCheck` | Runs only the CVE dependency audit. Results appear as PR comments. |

**Tips:**
- `require_approval: true` on the `production` target means this trigger pauses at the approval step — reply `@grok approve` to continue.
- Update jobs with `auto_commit: true` open a PR for their changes rather than committing directly when run on a protected branch.
- Deploy targets with `rollback_on_unhealthy: true` automatically roll back if health checks fail.

---

## 7 — Config, Tools & Analytics

Inspect global config via [`grok-config.yaml`](.grok/grok-config.yaml), query the tool registry from [`grok-tools.yaml`](.grok/grok-tools.yaml), and pull analytics from [`grok-analytics.yaml`](.grok/grok-analytics.yaml).

| Trigger | What happens |
|---------|-------------|
| `@grok config` | Shows the active configuration — model, temperature, personality, privacy settings. |
| `@grok config show context` | Prints the `context.domain_knowledge` and `context.key_constraints` currently loaded. |
| `@grok tools list` | Lists all registered tools with name, category, description, and security level. |
| `@grok tools inspect read_file` | Shows the full JSON Schema for `read_file`: parameters, return type, errors, and rate limits. |
| `@grok tools inspect run_command` | Inspects the `run_command` tool — important before granting it to a new agent. |
| `@grok analytics report` | Generates a usage summary from the last 30 days: invocation counts, top prompts, workflow completion rates. |
| `@grok analytics reset` | Clears locally cached analytics data. Does not affect data already sent to the configured provider. |
| `@grok ui status` | Shows the active dashboard widget configuration and any registered voice commands. |
| `@grok ui reload` | Reloads `grok-ui.yaml` without restarting the IDE extension. |

**Tips:**
- `@grok config` is the fastest way to verify `allow_telemetry: false` is active on an enterprise repo.
- `@grok tools inspect <name>` before adding a tool to an agent — check its `security.read_only` flag and rate limits.
- Analytics triggers only work when `analytics.enabled: true` is set in `grok-analytics.yaml`.
