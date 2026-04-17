# grok-test.yaml Field Reference

Full JSON Schema: [`/schemas/grok-test.json`](../schemas/grok-test.json)

---

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this test config file (e.g. `"1.2.0"`). |
| `author` | `string` | ✅ | X handle of the config owner, prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `test_suites` | `object` | ✅ | Named test suite definitions. At least one entry required. |

---

## test_suites entries

Each key becomes the identifier used in `@grok test <Name>` triggers. Use `all` as a key to run all suites together with `@grok test all`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | `string` | ✅ | What this suite evaluates. Min 5 chars, max 500 chars. |
| `prompt` | `string` | ✅ | Evaluation directive sent to Grok. Be explicit about pass/fail criteria. Min 10 chars, max 2000 chars. |
| `files` | `string[]` | — | Glob patterns selecting files in scope. Omit to scan the entire repository. |
| `exclude_files` | `string[]` | — | Glob patterns for files to exclude even when matched by `files`. |
| `temperature` | `number` | `0.2` | Sampling temperature for evaluation. Range: `0` – `1`. Lower = more deterministic. |
| `alert_level` | `string` | `"warning"` | Minimum severity at which Grok raises an alert. |
| `fail_on` | `string` | `"error"` | Severity threshold at which the suite is marked failed. |
| `max_findings` | `integer` | — | Maximum findings to report per run. Range: `1` – `500`. |
| `categories` | `string[]` | — | Test categories this suite covers. Used for filtering and reporting. |
| `block_merge_on_fail` | `boolean` | `false` | Block PR merges until issues in this suite are resolved. |
| `enabled` | `boolean` | `true` | Set to `false` to disable without removing the definition. |

---

## alert_level enum values

| Value | Meaning |
|-------|---------|
| `info` | Informational — no action required |
| `warning` | Non-critical issue worth reviewing |
| `high` | Significant issue — should be fixed before merging |
| `critical` | Blocking — must be resolved immediately |

## fail_on enum values

| Value | Suite fails when... |
|-------|---------------------|
| `error` | Any `critical`-level finding is detected |
| `warning` | Any `high` or `critical`-level finding is detected |
| `all` | Any finding at any severity is detected |

## categories enum values

`security` · `performance` · `accessibility` · `code_quality` · `documentation` · `testing` · `dependencies` · `compliance`

---

## temperature guidance

| Range | Recommended for |
|-------|----------------|
| `0.0` – `0.2` | Security scans, secret detection (deterministic) |
| `0.2` – `0.4` | Code quality reviews (consistent) |
| `0.5` – `0.7` | Accessibility and documentation checks |
| `0.8` – `1.0` | Creative suggestions (more varied output) |
