# grok-security.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-security.json`

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the config owner, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `security` | object | ✅ | — | — | Top-level security policy block. See [Security Object](#security-object). |

---

## Security Object

### Example

```yaml
security:
  auto_block_prs: true          # blocks PR merges on any critical finding
  severity_threshold: "medium"  # suppress findings below medium
  notify_email: "security@example.com"
  compliance_standards: ["SOC2", "GDPR"]
  allowed_licenses: ["MIT", "Apache-2.0", "BSD-3-Clause", "ISC"]
  scans:
    SecretDetection:
      type: "secrets"
      alert_level: "critical"
      fail_on_finding: true
      enabled: true
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `scans` | object | ✅ | — | minProperties: 1 | Named scan definitions. See [Scan Object](#scan-object). |
| `auto_block_prs` | boolean | — | `false` | — | Block PR merges when any scan reports a finding at or above `severity_threshold`. Test on non-production branches first. |
| `severity_threshold` | string | — | `"medium"` | enum: `low`, `medium`, `high`, `critical` | Findings below this level are suppressed from reports and blocking decisions. |
| `notify_on_slack` | boolean | — | `false` | — | Send Slack notifications on findings at or above the scan's `alert_level`. |
| `notify_on_x` | boolean | — | `false` | — | Post X notifications on findings (requires `approval_required: true`). |
| `notify_email` | string | — | — | format: email | Email address for critical findings. Use a team alias, not a personal address. |
| `compliance_standards` | string[] | — | `[]` | enum items below | Compliance frameworks to validate against. Only declare frameworks you have mapped. |
| `allowed_licenses` | string[] | — | `[]` | SPDX identifiers | Approved SPDX licence identifiers. Any dependency licence not on this list is flagged. |

---

## Scan Object

Each key in `security.scans` maps to a scan definition. Invoke with `@grok security scan:<Name>`.

### Example

```yaml
scans:
  DependencyCheck:
    type: "dependencies"
    files: ["package.json", "requirements.txt", "go.mod"]
    alert_level: "high"
    severity_threshold: "medium"
    frequency: "on_pr"
    fail_on_finding: true
    enabled: true
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `type` | string | ✅ | — | enum below | Category of security check to perform. |
| `files` | string[] | — | `["**/*"]` | glob patterns | File scope for the scan. |
| `exclude_files` | string[] | — | `[]` | glob patterns | Files excluded from scope even when matched by `files`. |
| `alert_level` | string | — | `"high"` | enum: `info`, `warning`, `high`, `critical` | Minimum severity at which this scan raises an alert. |
| `severity_threshold` | string | — | `"medium"` | enum: `low`, `medium`, `high`, `critical` | Suppress findings below this level per scan. Overrides the policy-level threshold. |
| `frequency` | string | — | `"on_pr"` | enum: `on_commit`, `on_pr`, `hourly`, `daily`, `weekly` | Automatic run cadence. |
| `fail_on_finding` | boolean | — | `true` | — | Mark scan failed when any finding meets or exceeds `alert_level`. Set `true` for `alert_level: critical`. |
| `enabled` | boolean | — | `true` | — | Set `false` to disable the scan without removing its definition. |

---

## type Enum

| Value | Checks |
|-------|--------|
| `secrets` | API keys, tokens, passwords, and private keys committed to files |
| `dependencies` | Known CVE vulnerabilities in package dependencies |
| `license_gdpr` | Licence compliance and GDPR data-handling issues |
| `sast` | Static application security testing — dangerous code patterns |
| `dast` | Dynamic application security testing — runtime behaviour |
| `sca` | Software composition analysis — full dependency inventory |
| `container` | Container image vulnerabilities and misconfigurations |
| `iac` | Infrastructure-as-code misconfigurations (Terraform, CloudFormation) |
| `api_security` | API endpoint security: authentication, rate limits, input validation |

---

## compliance_standards Enum

| Value | Framework |
|-------|-----------|
| `GDPR` | EU General Data Protection Regulation |
| `PCI-DSS` | Payment Card Industry Data Security Standard |
| `HIPAA` | Health Insurance Portability and Accountability Act |
| `SOC2` | Service Organisation Control 2 |
| `ISO-27001` | ISO/IEC 27001 Information Security Management |
| `NIST` | NIST Cybersecurity Framework |
| `OWASP-Top10` | OWASP Top 10 Web Application Security Risks |
| `CIS` | CIS Critical Security Controls |
