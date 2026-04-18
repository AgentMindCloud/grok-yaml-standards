# grok-workflow — Real-World Use Cases

---

### CI/CD Lite (Small Development Team)

**Who uses this:** A small engineering team (2–8 developers) that wants automated test-then-deploy without setting up a full CI/CD platform like GitHub Actions or CircleCI.

**Scenario:** Every time someone opens a PR, a senior dev has to manually run tests and kick off a staging deploy. It's a 20-minute bottleneck per PR that blocks junior developers from shipping independently and delays feedback by hours.

**How grok-workflow helps:** A workflow chaining `grok-test` → `grok-security` → `grok-deploy` automates the full flow. `on_failure: abort` blocks at the first failure. `approval_required: true` on the deploy step keeps a human in the loop for staging, while `depends_on` enforces strict sequencing so no deploy runs before tests pass.

**Example:**
```yaml
workflows:
  PRPipeline:
    description: "Run tests and security scan on every PR, then deploy to staging after approval."
    trigger: "@grok run workflow:PRPipeline"
    timeout_minutes: 45
    on_failure: "abort"
    steps:
      - name: "run-tests"
        action: "grok-test"
        input: "all"
        on_error: "abort"
      - name: "security-scan"
        action: "grok-security"
        depends_on: ["run-tests"]
        on_error: "abort"
      - name: "deploy-staging"
        action: "grok-deploy"
        input: "staging"
        depends_on: ["security-scan"]
        approval_required: true
```

**Pitfalls to avoid:** Setting `on_error: skip` on the security scan step — a workflow that continues past a failed security check creates a false sense of safety. Never omit `depends_on` between the test and deploy steps; without it they can run in parallel and a deploy may succeed before tests finish.

**Next step:** See `grok-deploy.yaml` to configure the staging target with health checks and automatic rollback rules.

---

### Content Publishing Pipeline (Creator / Marketer)

**Who uses this:** A content team or solo creator who publishes weekly X threads, newsletters, and blog posts — all derived from a single writing session — and wants the reformatting automated.

**Scenario:** You write a long-form article every Friday. Turning it into an X thread, a newsletter summary, and a LinkedIn post currently takes another two hours of reformatting. You want one trigger to produce all three formats and queue them for review before anything goes live.

**How grok-workflow helps:** A sequential workflow uses `grok-prompts` templates at each step to reformat the source article. `approval_required: true` on the publish step shows a preview before anything goes live. `notify_on_complete: true` sends a summary when all formats are ready for review.

**Example:**
```yaml
workflows:
  ContentPipeline:
    description: "Turn a draft article into an X thread and newsletter summary, then publish after approval."
    trigger: "@grok run workflow:ContentPipeline"
    notify_on_complete: true
    steps:
      - name: "draft-x-thread"
        action: "grok-prompts"
        template: "article_to_thread"
        on_error: "abort"
      - name: "draft-newsletter"
        action: "grok-prompts"
        template: "article_to_newsletter"
        depends_on: ["draft-x-thread"]
      - name: "publish-all"
        action: "publish_thread"
        depends_on: ["draft-x-thread", "draft-newsletter"]
        approval_required: true
```

**Pitfalls to avoid:** Chaining `publish_thread` without `approval_required: true` risks posting unreviewed AI-generated content publicly. Don't set `on_error: skip` on the drafting steps — if the formatter fails silently, you may publish with empty sections.

**Next step:** See `grok-prompts.yaml` to define the `article_to_thread` and `article_to_newsletter` templates with brand-voice constraints baked in.

---

### Bug → PR → Merge Workflow (Development Team)

**Who uses this:** A development team that wants to close the loop from a bug report to a merged fix with minimal manual handoffs while keeping humans in control of code changes.

**Scenario:** A critical bug is reported. A developer diagnoses it and writes a fix, but then the fix waits hours for review and CI to clear. Meanwhile, the bug is live. You want to automate the verification, PR creation, and deploy sequence while still requiring two human approvals before anything reaches production.

**How grok-workflow helps:** The workflow chains `grok-security` (verify the fix doesn't introduce new issues) → `create_pr` (opens a draft PR) → a manual `approval_required` gate for code review → `grok-deploy` with a second approval for production. `on_error: abort` at every step prevents a bad fix from advancing.

**Example:**
```yaml
workflows:
  BugFixPipeline:
    description: "Verify a bug fix, open a draft PR, wait for review, then deploy to production."
    on_failure: "abort"
    steps:
      - name: "security-check"
        action: "grok-security"
        on_error: "abort"
      - name: "open-pr"
        action: "create_pr"
        depends_on: ["security-check"]
      - name: "await-review"
        action: "grok-agent"
        approval_required: true
        depends_on: ["open-pr"]
      - name: "deploy-fix"
        action: "grok-deploy"
        input: "production"
        depends_on: ["await-review"]
        approval_required: true
```

**Pitfalls to avoid:** Never merge directly to production with only one `approval_required` gate — use separate gates for code review and for the production deploy. Don't chain `deploy-fix` directly after `open-pr`; the PR must be reviewed before it merges.

**Next step:** See `grok-security.yaml` to configure the SAST scan that runs in the `security-check` step with appropriate severity thresholds.

---

### Weekly Report Generator (Team Lead / Manager)

**Who uses this:** An engineering manager or team lead who compiles weekly status updates from multiple data sources — test results, deployment logs, open PR counts — and wants that assembly automated.

**Scenario:** Every Friday afternoon you spend 30 minutes pulling data from GitHub, your CI dashboard, and sprint tracking, then writing a status summary. The format is always the same, the data changes weekly, and it's exactly the kind of repetitive assembly task that automation should handle.

**How grok-workflow helps:** A workflow chains `summarize_changes` (gather diff and deploy data) → a `grok-prompts` step using a `weekly_report` template → `publish_thread` with `approval_required: true` so the manager sees the draft before it posts. `notify_on_complete: true` pings the manager when the draft is ready.

**Example:**
```yaml
workflows:
  WeeklyReport:
    description: "Compile test results, deployment summary, and open PRs into a weekly report draft."
    trigger: "@grok run workflow:WeeklyReport"
    notify_on_complete: true
    steps:
      - name: "gather-metrics"
        action: "summarize_changes"
        on_error: "notify_user"
      - name: "draft-report"
        action: "grok-prompts"
        template: "weekly_engineering_report"
        depends_on: ["gather-metrics"]
      - name: "send-report"
        action: "publish_thread"
        depends_on: ["draft-report"]
        approval_required: true
```

**Pitfalls to avoid:** Setting `on_error: skip` on the `gather-metrics` step — a failed data fetch produces a report with empty sections that looks complete but isn't. Always use `notify_user` so someone can investigate and rerun. Don't publish without `approval_required: true` on the final step.

**Next step:** See `grok-prompts.yaml` to define the `weekly_engineering_report` template with the exact sections and formatting your stakeholders expect.

---

### Onboarding Checklist Executor (Team Lead)

**Who uses this:** A team lead or engineering manager onboarding a new hire who wants every checklist item — environment setup, repo access, first PR — to happen consistently and be tracked automatically.

**Scenario:** Every time a new engineer joins, you run through the same 12-step checklist. Half the steps are manual — request GitHub access, set up local environment, assign a buddy — and things slip through the cracks. The new hire's first week is fragmented and the team lead spends 3 hours on admin.

**How grok-workflow helps:** A multi-step workflow codifies the entire checklist. Automated steps (`grok-docs` to share relevant docs) run immediately; steps requiring human action (assigning a buddy, granting production access) pause with `approval_required: true`. `depends_on` enforces sequencing — nobody gets prod access before code review training is confirmed.

**Example:**
```yaml
workflows:
  Onboarding:
    description: "Walk a new hire through the full onboarding checklist with automated and gated steps."
    trigger: "@grok run workflow:Onboarding"
    max_steps: 15
    on_failure: "notify_user"
    steps:
      - name: "send-welcome-docs"
        action: "grok-docs"
        input: "Onboarding"
      - name: "request-github-access"
        action: "create_pr"
        depends_on: ["send-welcome-docs"]
        approval_required: true
      - name: "assign-buddy"
        action: "grok-agent"
        input: "spawn agent:OpsHelper"
        depends_on: ["request-github-access"]
        approval_required: true
      - name: "first-pr-review"
        action: "grok-test"
        depends_on: ["assign-buddy"]
```

**Pitfalls to avoid:** Don't set `approval_required: false` on the prod-access step — an unchecked prod grant is a real security risk even when it feels like routine admin. Don't skip `depends_on` between steps; without sequencing a new hire could receive a prod access invite before their first PR has been reviewed.

**Next step:** See `grok-docs.yaml` to configure the `Onboarding` documentation target that the `send-welcome-docs` step generates and keeps fresh.
