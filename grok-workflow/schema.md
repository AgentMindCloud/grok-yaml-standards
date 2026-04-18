# grok-workflow.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-workflow.json`

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the config owner, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `workflows` | object | ✅ | — | minProperties: 1 | Named workflow definitions. Each key is an ID used in `@grok run workflow:<Name>`. |

---

## Workflow Definition Object

### Example

```yaml
workflows:
  ReleasePipeline:
    description: "Run tests, build docs, post changelog thread, then open a release PR."
    trigger: "@grok run workflow:ReleasePipeline"
    timeout_minutes: 60
    on_failure: "notify"
    notify_on_complete: true
    max_steps: 8
    steps:
      - name: "RunTests"
        action: "grok-test"
        input: "all"
        on_error: "stop"    # block release if tests fail
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `description` | string | ✅ | — | minLength: 10; maxLength: 500 | What this workflow accomplishes end-to-end. |
| `steps` | object[] | ✅ | — | minItems: 1 | Ordered sequence of actions. Executed top-to-bottom. |
| `trigger` | string | — | — | starts with `@grok` | Canonical `@grok` trigger string for this workflow. |
| `timeout_minutes` | integer | — | `30` | minimum: 1; maximum: 1440 | Maximum wall-clock minutes before the workflow is force-stopped. |
| `on_failure` | string | — | `"stop"` | enum: `stop`, `continue`, `retry`, `notify` | Global failure strategy applied when a step fails without a local `on_error`. |
| `notify_on_complete` | boolean | — | `false` | — | Post a summary to X when the workflow finishes (requires approval). |
| `max_steps` | integer | — | `50` | minimum: 1; maximum: 200 | Hard cap on steps executed per run. Prevents infinite loops. |

---

## Step Definition Object

### Example

```yaml
steps:
  - name: "RunTests"
    action: "grok-test"
    input: "security"
    on_error: "stop"
    timeout_minutes: 15

  - name: "PostChangelog"
    action: "publish_thread"
    condition: "steps.RunTests.exit_code === 0"   # skip if tests failed
    approval_required: true                         # human approves before X post
    env:
      BASE_REF: "main"
      HEAD_REF: "${{ github.sha }}"
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `name` | string | ✅ | — | minLength: 1; maxLength: 100 | Display name shown in workflow progress and logs. |
| `action` | string | ✅ | — | minLength: 1; maxLength: 200 | Action to execute: a spec name (`grok-test`), a tool ID, or a prompt key. |
| `input` | string | — | — | maxLength: 1000 | Static input string passed to the action (e.g. `"all"` for `grok-test all`). |
| `template` | string | — | — | pattern: `^[a-z_][a-z0-9_]*$` | Prompt library key when action is `publish_thread`. |
| `prompt` | string | — | — | pattern: `^[a-z_][a-z0-9_]*$` | Prompt library key when action is `grok-prompts`. |
| `condition` | string | — | — | maxLength: 500 | Boolean expression against prior step outputs. Step skipped when `false`. |
| `on_error` | string | — | — | enum: `stop`, `continue`, `retry`, `notify` | Per-step error handling. Overrides workflow-level `on_failure`. |
| `retry_count` | integer | — | `3` | minimum: 1; maximum: 5 | Auto-retries on transient failure. Only active when `on_error: retry`. |
| `timeout_minutes` | integer | — | — | minimum: 1; maximum: 120 | Per-step timeout override. |
| `approval_required` | boolean | — | `false` | — | Pause the workflow and require human approval before this step executes. |
| `env` | object | — | — | additionalProperties: string | Environment variables scoped to this step's action. Use secret references, not literal values. |
| `depends_on` | string[] | — | `[]` | each item: step name in same workflow | Explicit dependency ordering. Step will not start until all dependencies succeed. |

---

## Condition Expression Syntax

Conditions are evaluated server-side against a `steps` context object keyed by step name:

```yaml
# Previous step produced a zero exit code
condition: "steps.RunTests.exit_code === 0"

# No security alerts were raised
condition: "steps.SecurityScan.alerts.length === 0"

# Prior step completed successfully
condition: "steps.BuildDocs.status === 'success'"
```

A step whose condition evaluates to `false` is **skipped** (not failed). Use `on_error` for failure handling.

---

## on_failure / on_error Enum

| Value | Behaviour |
|-------|-----------|
| `stop` | Halt the workflow immediately. Default. Recommended for security and release pipelines. |
| `continue` | Log the failure and proceed to the next step. Use only for non-critical informational steps. |
| `retry` | Retry the step up to `retry_count` times with exponential backoff. |
| `notify` | Stop and post an alert (X or email) so a human can investigate and re-trigger. |
