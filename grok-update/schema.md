# grok-update.yaml Field Reference

Full JSON Schema: [`/schemas/grok-update.json`](../schemas/grok-update.json)

---

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this update config file (e.g. `"1.2.0"`). |
| `author` | `string` | ✅ | X handle of the config owner, prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `updates` | `object` | ✅ | Named update job definitions. At least one entry required. |

---

## updates entries

Each key becomes the job identifier used in `@grok update <Name>` triggers.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | `string` | ✅ | What this job refreshes and why. Min 5 chars, max 500 chars. |
| `sources` | `string[]` | ✅ | File paths, directory globs, or URLs to read and refresh. Glob patterns supported. At least one item required. |
| `frequency` | `string` | ✅ | How often this job runs automatically. See enum values below. |
| `auto_commit` | `boolean` | `false` | Automatically commit changes without human review. Use with caution on public repos. |
| `require_approval` | `boolean` | `true` | Open a PR for human review before merging. Takes precedence over `auto_commit`. |
| `actions` | `string[]` | — | Ordered list of named actions to perform on each source. See enum values below. |
| `notify_on_change` | `boolean` | `false` | Post an X notification when the job produces changes. |
| `branch` | `string` | — | Target branch for committed changes. Pattern: `^[a-zA-Z0-9/_.-]+$`. |
| `schedule_cron` | `string` | — | Cron expression overriding `frequency`. e.g. `"0 9 * * 1"` = every Monday 09:00 UTC. |
| `enabled` | `boolean` | `true` | Set to `false` to pause the job without removing its definition. |

---

## frequency enum values

| Value | Runs |
|-------|------|
| `hourly` | Every 60 minutes |
| `daily` | Once per day |
| `weekly` | Once per week |
| `monthly` | Once per month |
| `on_commit` | Every push to the default branch |
| `on_pr` | Every time a PR is opened or updated |
| `manual` | Only when explicitly triggered via `@grok update` |

---

## actions enum values

| Value | What it does |
|-------|-------------|
| `refresh_links` | Verify and update hyperlinks in source files |
| `update_stats` | Re-fetch live statistics (stars, downloads) embedded in docs |
| `pull_latest_research` | Fetch and summarise new publications or releases from configured URLs |
| `update_dependencies` | Bump dependency versions in package manifests |
| `security_patch` | Apply security-only version updates to dependencies |
| `regenerate_docs` | Re-run `grok-docs` targets to rebuild documentation |
| `sync_translations` | Push new strings to the translation provider and pull approved translations |
| `archive_stale` | Move files unchanged for more than N days to an archive folder |
| `notify_maintainers` | Send a summary of all changes to the configured notification channels |

---

## schedule_cron format

Standard 5-field cron syntax (minute hour day-of-month month day-of-week):

```
"0 9 * * 1"    # Every Monday at 09:00 UTC
"0 0 * * *"    # Daily at midnight UTC
"*/30 * * * *" # Every 30 minutes
```

When `schedule_cron` is set it overrides the `frequency` field entirely.
