# grok-security.yaml — Security Considerations

## 1. Test `auto_block_prs: true` on non-production branches before enabling globally

An untested PR-blocking rule can stall your entire development workflow if it fires on false positives. Before enabling `auto_block_prs` on your main repository, validate each scan's false-positive rate on a feature branch or test repository. Set `severity_threshold` appropriately so only actionable findings trigger blocks, not every informational note.

## 2. Ensure `alert_level: critical` scans have `fail_on_finding: true`

A scan that raises a critical alert but does not mark itself as failed will still show as "passed" in your CI status. For secrets detection and known vulnerability scans, always set `fail_on_finding: true` alongside `alert_level: critical`. This ensures the failed status propagates to branch protection rules and blocks the PR merge path.

## 3. Maintain an explicit `allowed_licenses` allowlist and reject anything not on it

Omitting `allowed_licenses` means all licenses are accepted by default, including copyleft licenses (GPL, AGPL) that may be incompatible with your project's license. Define a clear allowlist (e.g. `["MIT", "Apache-2.0", "BSD-3-Clause", "ISC"]`) so the `license_gdpr` scan flags any new dependency whose license falls outside it, rather than relying on periodic manual audits.

## 4. Use a team email alias, not a personal address, for `notify_email`

`notify_email` receives alerts for every critical finding across all scans. A personal email address creates single-point-of-failure alerting — if that person is unavailable, critical alerts are missed. Use a team alias or a paging service (PagerDuty, OpsGenie) that distributes alerts across the on-call rotation and maintains an audit trail.

## 5. Only declare `compliance_standards` you have actually validated against

Listing `HIPAA` or `PCI-DSS` in `compliance_standards` will cause `license_gdpr` and related scans to apply those frameworks' rules. If your organisation has not completed the corresponding compliance programme, this will either generate excessive false positives or give a false sense of compliance assurance. Declare only the frameworks whose requirements you have mapped to your codebase.

---

## Threat Model

This spec **is the security policy itself** — scan definitions, compliance gates, and blocking rules. The threats here include meta-threats that exist because the policy can be misconfigured, absent, or bypassed.

**T1 — Credential Exposure**
Attack: A contributor adds a webhook URL or notification token directly into this file.
Defense: The JSON Schema rejects strings matching known credential patterns outside env-reference fields. Notification targets must use `${ENV_VAR}` references.

**T2 — Prompt Injection via Tool Output**
Attack: A scan output summary is fed into a notification prompt, carrying injected instructions that alter the notification.
Defense: Scan outputs are wrapped in XML delimiters and the notification prompt treats them as data, not instructions.

**T3 — Path Traversal in Filesystem Tools**
Attack: A scan's `scope:` resolves to paths outside the repo.
Defense: Scope paths are validated against `^(?!.*\.\.)[^/].*$`. Scans execute in a read-only sandbox rooted at the repo.

**T4 — Over-Permissioned Actions**
Attack: The security file grants write scopes to the scanner agent so it can "auto-fix" findings; a compromised scanner rewrites production code.
Defense: Scanners are read-only by default. Auto-fix requires `require_approval: true` and opens a PR rather than committing directly.

**T5 — Rate Limit Abuse**
Attack: A misconfigured scan runs on every commit in a busy repo, generating alert spam.
Defense: Per-scan `min_interval_minutes` and debounced notifications. Critical alerts page only once per 15-minute window for the same finding.

**T6 — Supply Chain via Remote Tool Import**
Attack: A custom scanner is imported from a compromised URL, giving the attacker full visibility into the codebase.
Defense: External scanner URLs must be whitelisted here; the whitelist is itself part of the security policy and is diffed on every change.

### Security-Spec-Specific Threats

**ST1 — Missing Security File (Fail-Safe Default)**
Attack: A repo ships without `grok-security.yaml`, so the runtime has no declared policy and (if misdesigned) defaults to permissive.
Defense: When `grok-security.yaml` is absent, the runtime **defaults to the most restrictive profile** — equivalent to `safety_profile: "strict"`. No X writes, no shell execution, no external network. Explicitly declaring the file is required to loosen any restriction.

**ST2 — Runtime Permission Escalation**
Attack: An agent tries at runtime to invoke a permission that was not declared in `grok-security.yaml`.
Defense: The runtime must **block and audit-log the attempt**, never silently allow. The attempt is surfaced as a CRITICAL alert so a human can investigate whether the agent is compromised or the policy is missing a legitimate grant.

**ST3 — Permission Inheritance in Multi-Agent Setups**
Attack: A parent agent with broad permissions spawns a child agent. The child inherits the parent's scope and uses it to perform actions outside its own declared purpose.
Defense: Child agents **never inherit** parent permissions. Each agent's `tools:` and permission list stands alone; child spawn must declare its own scope explicitly. The validator rejects any spawn that references undeclared permissions.

### Out of Scope for This Spec

- Vulnerabilities in the xAI API or the Grok model itself — report to xAI's security team.
- X platform vulnerabilities — report to X's security team.
- Host OS, container runtime, or network security — handled by the deployment platform.

### Reporting Security Issues

See the repository [`SECURITY.md`](../SECURITY.md). Never file a public issue for a suspected vulnerability; use a private GitHub Security Advisory or the email listed in `SECURITY.md`.
