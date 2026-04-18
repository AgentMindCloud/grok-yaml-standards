# grok-update.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-update.json`

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the config owner, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `updates` | object | ✅ | — | minProperties: 1 | Named update job definitions. Each key is a job ID used in `@grok update <Name>`. |

---

## Update Job Object

### Example

```yaml
updates:
  WeeklyDepPatch:
    description: "Apply security-only dependency patches every Monday."
    sources: ["package.json", "package-lock.json"]
    frequency: "weekly"
    schedule_cron: "0 9 * * 1"   # every Monday 09:00 UTC
    actions: ["security_patch"]
    auto_commit: false
    require_approval: true        # always review security patches before merging
    branch: "grok-updates/deps"
    notify_on_change: true
    enabled: true
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `description` | string | ✅ | — | minLength: 5; maxLength: 500 | What this job refreshes and why. |
| `sources` | string[] | ✅ | — | minItems: 1 | File paths, globs, or URLs to read. Avoid `**/.env`, `**/secrets/**`. |
| `frequency` | string | ✅ | — | enum: `hourly`, `daily`, `weekly`, `monthly`, `on_commit`, `on_pr`, `manual` | Automatic run cadence. |
| `schedule_cron` | string | — | — | 5-field cron format | Overrides `frequency` when set. E.g. `"0 9 * * 1"` = Monday 09:00 UTC. |
| `actions` | string[] | — | `[]` | enum items below | Ordered operations performed on each source on each run. |
| `auto_commit` | boolean | — | `false` | — | Commit changes without opening a PR. Never combine with `require_approval: false` on public repos. |
| `require_approval` | boolean | — | `true` | — | Open a PR for human review before merging. Takes precedence over `auto_commit`. |
| `branch` | string | — | — | pattern: `^[a-zA-Z0-9/_.-]+$` | Target branch for commits. Set to a non-default branch; never commit directly to `main`. |
| `notify_on_change` | boolean | — | `false` | — | Post an X notification when the job produces changes. Requires approval. |
| `max_changes_per_run` | integer | — | `100` | minimum: 1; maximum: 1000 | Hard cap on files changed in a single run. Prevents runaway rewrites. |
| `enabled` | boolean | — | `true` | — | Set `false` to pause the job without removing its definition. |

---

## frequency Enum

| Value | Runs |
|-------|------|
| `hourly` | Every 60 minutes |
| `daily` | Once per day (midnight UTC unless `schedule_cron` overrides) |
| `weekly` | Once per week |
| `monthly` | First day of each month |
| `on_commit` | Every push to the default branch |
| `on_pr` | Every time a PR is opened or updated |
| `manual` | Only when explicitly triggered via `@grok update` |

---

## actions Enum

| Value | What it does |
|-------|-------------|
| `refresh_links` | Verify and update hyperlinks in source files |
| `update_stats` | Re-fetch live statistics (stars, downloads) embedded in docs |
| `pull_latest_research` | Fetch and summarise new publications or releases from configured URLs |
| `update_dependencies` | Bump dependency versions in package manifests |
| `security_patch` | Apply security-only version updates. Always set `require_approval: true` for this action. |
| `regenerate_docs` | Re-run `grok-docs` targets to rebuild documentation |
| `sync_translations` | Push new strings to the translation provider and pull approved translations |
| `archive_stale` | Move files unchanged for more than N days to an archive folder |
| `notify_maintainers` | Send a summary of all changes to configured notification channels |

---

## schedule_cron Format

Standard 5-field cron syntax: `minute hour day-of-month month day-of-week`

```yaml
schedule_cron: "0 9 * * 1"     # Every Monday 09:00 UTC
schedule_cron: "0 0 * * *"     # Daily at midnight UTC
schedule_cron: "0 9 1 * *"     # 1st of each month 09:00 UTC
schedule_cron: "*/30 * * * *"  # Every 30 minutes (use sparingly — triggers API calls)
```

When set, `schedule_cron` overrides `frequency` entirely.

---

## Cross-References

### Depends On
- **grok-config.yaml**: model and language defaults drive content generation quality.
- **grok-docs.yaml**: `regenerate_docs` action references doc target names defined there.

### Used By
- **grok-workflow.yaml**: `steps[].action: grok-update` references update job names.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `sources[]` | Files read and provided as context in the prompt |
| `actions[]` | Maps to tool calls sent in the completion request |
| `frequency` / `schedule_cron` | Scheduler config — not an SDK param |

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| `actions[]` | `tools=` list when the update invokes tool calls |
| `model` (from grok-config) | `model="xai/grok-4"` |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| `actions[]` | `KernelFunction` invocations in a pipeline |
| `sources[]` | `TextChunker` input files for memory ingestion |
