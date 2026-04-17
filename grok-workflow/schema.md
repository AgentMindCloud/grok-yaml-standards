# grok-workflow.yaml Field Reference

Full JSON Schema: [`/schemas/grok-workflow.json`](../schemas/grok-workflow.json)

---

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this workflow config file (e.g. `"1.2.0"`). |
| `author` | `string` | ✅ | X handle of the config owner, prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `workflows` | `object` | ✅ | Named workflow definitions. At least one entry required. |

---

## workflows entries

Each key becomes the identifier used in `@grok run workflow:<Name>` triggers.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | `string` | ✅ | What this workflow accomplishes end-to-end. Min 10 chars, max 500 chars. |
| `steps` | `object[]` | ✅ | Ordered sequence of actions. At least one step required. |
| `trigger` | `string` | — | Canonical `@grok` trigger string. Must start with `@grok`. |
| `timeout_minutes` | `integer` | `30` | Maximum wall-clock minutes before the workflow is force-stopped. Range: `1` – `1440`. |
| `on_failure` | `string` | `"stop"` | Global failure strategy when a step fails without a local `on_error` override. |
| `notify_on_complete` | `boolean` | `false` | Post an X notification when the workflow finishes. |

**`on_failure` enum values:**
`stop` · `continue` · `retry` · `notify`

---

## steps — step definition fields

Steps execute top-to-bottom and share a runtime context object.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `string` | ✅ | Display name shown in workflow progress output. Max 100 chars. |
| `action` | `string` | ✅ | Action to execute: a grok spec name (e.g. `grok-test`), a tool identifier, or a prompt key. |
| `input` | `string` | — | Static input string passed to the action (e.g. `"all"` for `grok-test`). Max 1000 chars. |
| `template` | `string` | — | Prompt library key when the action is `publish_thread`. Pattern: `^[a-z_][a-z0-9_]*$`. |
| `prompt` | `string` | — | Prompt library key when the action is `grok-prompts`. Pattern: `^[a-z_][a-z0-9_]*$`. |
| `condition` | `string` | — | Boolean expression evaluated against prior step outputs. Step skipped when `false`. Max 500 chars. |
| `on_error` | `string` | — | Per-step error handling. Overrides workflow-level `on_failure`. |
| `retry_count` | `integer` | `3` | Auto-retries on transient failure. Only active when `on_error: retry`. Range: `1` – `5`. |
| `timeout_minutes` | `integer` | — | Per-step timeout override. Range: `1` – `120`. |
| `env` | `object` | — | Environment variables available to this step's action. String values only. |

**`on_error` enum values:**
`stop` · `continue` · `retry` · `notify`

---

## condition expression syntax

Conditions are evaluated against a `steps` context object keyed by step name:

```yaml
condition: "steps.RunTests.exit_code === 0"
condition: "steps.SecurityScan.alerts.length === 0"
condition: "steps.BuildDocs.status === 'success'"
```

A step whose condition evaluates to `false` is **skipped** (not failed). Use `on_error` for failure handling.
