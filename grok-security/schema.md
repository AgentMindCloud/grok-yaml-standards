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

---

## Validation Examples

```yaml
# INVALID — scans map is empty
security:
  scans: {}
# Error: scans must have at least 1 property

# INVALID — unknown scan type
security:
  scans:
    MyCheck:
      type: "xss_scanner"
# Error: type must be one of: secrets, dependencies, license_gdpr, sast, dast, sca, container, iac, api_security

# VALID — minimal secrets scan
security:
  scans:
    SecretDetection:
      type: "secrets"
      alert_level: "critical"
      fail_on_finding: true
      enabled: true
```

---

## Security Notes

- **`auto_block_prs`**: Test on a non-production branch before enabling — an overly broad `files` glob can inadvertently block legitimate PRs.
- **`fail_on_finding: true`** unconditionally for `type: secrets`; `false` is appropriate only for informational scan dashboards.
- **`notify_on_x`**: Always requires human review before security findings are posted publicly (see ST2 in `security-considerations.md`).
- **`allowed_licenses`**: Only declare compliance frameworks you have actually mapped; declaring `GDPR` without enforcement gives false assurance that is worse than none.

---

## Cross-References

| Spec / SDK | Field | Relationship |
|------------|-------|--------------|
| `grok-config.yaml` | `grok.safety_profile: strict` | Strict safety profile auto-enables secret detection scanning. |
| `grok-agent.yaml` | agents with `run_command` tool | Agents that can execute shell commands should always be paired with a complementary `sast` scan. |
| `grok-workflow.yaml` | `steps[].action: grok-security` | Schedule scans as steps within a workflow (e.g. nightly `SecretDetection`). |
| xAI SDK | scan result payload | Returned as `response_format: json_object` containing CVE identifiers and severity bands. |

### Depends On
- **grok-config.yaml**: `safety_profile` in config is the global baseline; per-scan `severity_threshold` overrides it.

### Used By
- **grok-agent.yaml**: agents set `safety_profile` which must align with this spec.
- **grok-workflow.yaml**: `steps[].action: grok-security` runs named scans.
- **grok-deploy.yaml**: `require_approval` behaviour is informed by security policy.
- **grok-test.yaml**: `block_merge_on_fail` integrates with the security gate.

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| (all fields) | Security scan results are returned as structured JSON from the Grok runtime; no direct LiteLLM parameters correspond to scan configuration fields. |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| (all fields) | No direct SK equivalents — scan configuration is resolved by the Grok runtime, not the SK kernel. |
