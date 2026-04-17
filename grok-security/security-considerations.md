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
