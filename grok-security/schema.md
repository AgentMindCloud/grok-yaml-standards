# grok-security.yaml Field Reference

Full JSON Schema: [`/schemas/grok-security.json`](../schemas/grok-security.json)

---

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this security config file (e.g. `"1.2.0"`). |
| `author` | `string` | ✅ | X handle of the config owner, prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `security` | `object` | ✅ | Top-level security configuration block. |

---

## security object fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `scans` | `object` | ✅ | Named scan definitions. At least one scan required. |
| `auto_block_prs` | `boolean` | `false` | Block PR merges when any `critical`-level scan finding is detected. |
| `notify_on_slack` | `boolean` | `false` | Send Slack notifications on findings at or above `alert_level`. |
| `notify_on_x` | `boolean` | `false` | Post X notifications on findings at or above `alert_level`. |
| `notify_email` | `string` | — | Email address for critical findings. Must be valid email format. |
| `compliance_standards` | `string[]` | — | Compliance frameworks to validate against. See enum values below. |
| `allowed_licenses` | `string[]` | — | SPDX identifiers approved for use in dependencies (e.g. `MIT`, `Apache-2.0`). |

---

## scans entries

Each key becomes the scan identifier used in `@grok security scan:<Name>` triggers.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | `string` | ✅ | Category of security check to perform. See enum values below. |
| `files` | `string[]` | — | Glob patterns selecting files in scope. Defaults to `["**/*"]`. |
| `exclude_files` | `string[]` | — | Glob patterns for files to exclude from scope. |
| `alert_level` | `string` | `"high"` | Minimum severity at which this scan raises an alert. |
| `frequency` | `string` | `"on_pr"` | How often this scan runs automatically. |
| `severity_threshold` | `string` | `"medium"` | CVSS severity band — findings below this are suppressed. |
| `fail_on_finding` | `boolean` | `true` | Mark scan failed when any finding meets or exceeds `alert_level`. |
| `enabled` | `boolean` | `true` | Set to `false` to disable the scan without removing its definition. |

---

## type enum values

| Value | Checks |
|-------|--------|
| `secrets` | API keys, tokens, passwords, and private keys committed to files |
| `dependencies` | Known CVE vulnerabilities in package dependencies |
| `license_gdpr` | License compliance and GDPR data-handling issues |
| `sast` | Static application security testing — dangerous code patterns |
| `dast` | Dynamic application security testing — runtime behaviour |
| `sca` | Software composition analysis — full dependency inventory |
| `container` | Container image vulnerabilities and misconfigurations |
| `iac` | Infrastructure-as-code misconfigurations (Terraform, CloudFormation) |
| `api_security` | API endpoint security: auth, rate limits, input validation |

## alert_level / severity_threshold enum values

`info` · `warning` · `high` · `critical`

## frequency enum values

`on_commit` · `on_pr` · `hourly` · `daily` · `weekly`

## compliance_standards enum values

`GDPR` · `PCI-DSS` · `HIPAA` · `SOC2` · `ISO-27001` · `NIST` · `OWASP-Top10` · `CIS`
