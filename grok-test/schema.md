# grok-test.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-test.json`

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the config owner, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `test_suites` | object | ✅ | — | minProperties: 1 | Named test suite definitions. Use `all` as a key to run every suite with `@grok test all`. |

---

## Test Suite Object

### Example

```yaml
test_suites:
  SecurityScan:
    description: "Detect secrets, vulnerable deps, and SAST findings before every merge."
    prompt: |
      Scan the files in scope for: hardcoded API keys, known CVEs in imports,
      and SQL injection / XSS patterns. Rate each finding: critical / high / medium / low.
      Fail if any critical or high findings exist.
    files: ["src/**/*", "scripts/**/*"]
    exclude_files: ["**/*.test.ts", "node_modules/**"]
    temperature: 0.1         # deterministic for security — never random
    alert_level: "critical"
    fail_on: "error"
    block_merge_on_fail: true
    categories: ["security"]
    max_findings: 50
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `description` | string | ✅ | — | minLength: 5; maxLength: 500 | What this suite evaluates. |
| `prompt` | string | ✅ | — | minLength: 10; maxLength: 2000 | Evaluation directive sent to Grok. Be explicit about pass/fail criteria. |
| `files` | string[] | — | `["**/*"]` | glob patterns | File scope for the suite. Defaults to entire repository. |
| `exclude_files` | string[] | — | `[]` | glob patterns | Files excluded even when matched by `files`. Exclude `node_modules/`, `dist/`, vendored dirs. |
| `temperature` | number | — | `0.2` | minimum: 0; maximum: 1 | Sampling temperature. Use `0.1`–`0.2` for security/compliance; higher for documentation. |
| `alert_level` | string | — | `"warning"` | enum: `info`, `warning`, `high`, `critical` | Minimum severity at which Grok raises an alert. |
| `fail_on` | string | — | `"error"` | enum: `error`, `warning`, `all` | Severity threshold at which the suite is marked failed. |
| `block_merge_on_fail` | boolean | — | `false` | — | Block PR merges until all findings in this suite are resolved. |
| `categories` | string[] | — | `[]` | enum items below | Test categories this suite covers. Used for filtering and reporting. |
| `max_findings` | integer | — | — | minimum: 1; maximum: 500 | Cap on findings reported per run. Prevents noise from exhaustive lists. |
| `max_tokens` | integer | — | `2048` | minimum: 1; maximum: 8192 | Token budget for the evaluation response. |
| `enabled` | boolean | — | `true` | — | Set `false` to disable the suite without removing its definition. |

---

## alert_level Enum

| Value | Meaning |
|-------|---------|
| `info` | Informational — no action required |
| `warning` | Non-critical issue worth reviewing |
| `high` | Significant issue — should be fixed before merging |
| `critical` | Blocking — must be resolved immediately; always page a human |

---

## fail_on Enum

| Value | Suite fails when... |
|-------|---------------------|
| `error` | Any `critical`-level finding is detected |
| `warning` | Any `high` or `critical`-level finding is detected |
| `all` | Any finding at any severity is detected |

---

## categories Enum

| Value | Focus area |
|-------|------------|
| `security` | Secrets, CVEs, injection vulnerabilities, permission issues |
| `performance` | Latency regressions, memory leaks, inefficient algorithms |
| `accessibility` | WCAG compliance, ARIA attributes, colour contrast |
| `code_quality` | Readability, complexity, duplication, dead code |
| `documentation` | Missing docs, stale examples, broken links |
| `testing` | Test coverage gaps, flaky tests, missing edge cases |
| `dependencies` | Outdated packages, licence compliance, supply-chain risk |
| `compliance` | GDPR, PCI-DSS, HIPAA, SOC2, and other regulatory requirements |

---

## temperature Guidance

| Range | Recommended for |
|-------|----------------|
| `0.0`–`0.2` | Security scans, secret detection — deterministic results |
| `0.2`–`0.4` | Code quality and dependency reviews — consistent |
| `0.4`–`0.7` | Accessibility and documentation checks |
| `0.7`–`1.0` | Creative suggestions (more variation between runs) |
