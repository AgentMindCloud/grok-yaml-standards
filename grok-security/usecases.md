# grok-security — Real-World Use Cases

---

### Pre-Merge Security Gate (Development Team)

**Who uses this:** An engineering team shipping features on a fast release cadence that needs automated security review on every pull request without blocking developers with excessive false positives.

**Scenario:** Your team merges 15–20 PRs per week. Manual security review is a bottleneck — the security engineer can only review 3–4 PRs per day. Without automation, the rest slip through unreviewed and vulnerabilities accumulate silently in the codebase.

**How grok-security helps:** A `secrets` scan and a `sast` scan both set to `frequency: on_pr` and `fail_on_finding: true` block the merge if either scan finds a critical issue. `auto_block_prs: true` integrates with GitHub's required status checks. `severity_threshold: medium` suppresses noise below medium severity so developers aren't drowning in low-priority findings.

**Example:**
```yaml
security:
  auto_block_prs: true
  severity_threshold: "medium"
  scans:
    SecretDetection:
      type: "secrets"
      alert_level: "critical"
      fail_on_finding: true
      frequency: "on_pr"
      enabled: true
    StaticAnalysis:
      type: "sast"
      alert_level: "high"
      fail_on_finding: true
      frequency: "on_pr"
      severity_threshold: "medium"
      enabled: true
```

**Pitfalls to avoid:** Setting `auto_block_prs: true` before testing on a non-production branch — an overly broad `files` glob can block unrelated PRs. Don't set `fail_on_finding: false` on the secrets scan; credentials in code are always critical regardless of environment context.

**Next step:** See `grok-workflow.yaml` to chain this security scan into a broader CI/CD pipeline that also runs tests before deploying.

---

### Open-Source Dependency Audit (OSS Maintainer)

**Who uses this:** An open-source project maintainer responsible for keeping dependencies free of known CVEs so downstream users who depend on the library aren't exposed to vulnerabilities.

**Scenario:** Your library has 40 transitive dependencies. A CVE is published in a popular sub-dependency. You need to know within hours — not weeks — and have a clear audit trail showing which versions are affected and when you patched them. Right now you find out from a user issue.

**How grok-security helps:** A `dependencies` scan with `frequency: daily` checks all lockfiles against the CVE database around the clock. `notify_email` sends an alert to your security alias immediately on a critical finding. `allowed_licenses` rejects dependencies under licenses incompatible with your project's permissive license.

**Example:**
```yaml
security:
  notify_email: "security@myoss.dev"
  allowed_licenses: ["MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "0BSD"]
  scans:
    DependencyAudit:
      type: "dependencies"
      files: ["package.json", "package-lock.json", "yarn.lock", "requirements.txt", "go.mod"]
      alert_level: "high"
      severity_threshold: "medium"
      frequency: "daily"
      fail_on_finding: true
      enabled: true
```

**Pitfalls to avoid:** Only listing `package.json` in `files` misses transitive lockfile CVEs — always include lockfiles (`package-lock.json`, `yarn.lock`) for complete coverage. Don't omit `allowed_licenses`; a copyleft dependency in a permissive library creates downstream legal problems for users who adopt it.

**Next step:** See `grok-update.yaml` to configure an automated `update_dependencies` job that opens a PR when a CVE scan returns a finding.

---

### GDPR / PCI Compliance Check (Compliance Officer + Engineering)

**Who uses this:** An engineering team at a fintech or healthtech company that must demonstrate continuous compliance with GDPR and PCI-DSS before each quarterly audit.

**Scenario:** Your auditor asks for evidence that every code change was scanned for GDPR data-handling issues and PCI-DSS configuration problems before going to production. Right now you have manual review notes that are inconsistent, incomplete, and impossible to present as a coherent audit trail.

**How grok-security helps:** A `license_gdpr` scan and `sca` scan with `compliance_standards: ["GDPR", "PCI-DSS"]` run on every PR and generate a machine-readable audit log. `frequency: on_pr` means every change is covered. `notify_email` routes critical findings to the compliance alias — not just engineering — so nothing is silently suppressed.

**Example:**
```yaml
security:
  auto_block_prs: true
  compliance_standards: ["GDPR", "PCI-DSS"]
  notify_email: "compliance@fintech.example.com"
  scans:
    GDPRCheck:
      type: "license_gdpr"
      alert_level: "high"
      fail_on_finding: true
      frequency: "on_pr"
      enabled: true
    CompositionAnalysis:
      type: "sca"
      alert_level: "high"
      frequency: "on_pr"
      enabled: true
```

**Pitfalls to avoid:** Declaring `compliance_standards: ["PCI-DSS"]` without mapping your controls to PCI-DSS requirements gives false assurance — the scan validates what it can detect, not your full compliance posture. Don't use `notify_on_x: true` for compliance findings; PCI-DSS prohibits public disclosure of cardholder data environment details.

**Next step:** See `grok-analytics.yaml` to retain a timestamped event log of every scan result to build audit evidence packs.

---

### Secret Leak Prevention (Any Developer)

**Who uses this:** Any developer — solo or team — who wants a hard guarantee that API keys, tokens, and passwords never reach the remote repository, regardless of how an accidental commit happens.

**Scenario:** A developer copies a real API key into a config file while debugging locally, commits it before noticing, and pushes. By the time the key is revoked and rotated, it has been indexed by secret-scanning bots. One incident like this costs days of incident response and a forced credential rotation across all consumers.

**How grok-security helps:** A `secrets` scan with `frequency: on_commit` and `fail_on_finding: true` blocks the push before the credential ever leaves the local machine. `alert_level: critical` ensures no secret-shaped string passes silently. `severity_threshold: low` catches even staging or test credentials that should still be rotated.

**Example:**
```yaml
security:
  auto_block_prs: true
  scans:
    SecretDetection:
      type: "secrets"
      files: ["**/*"]
      exclude_files: ["**/fixtures/**", "**/__mocks__/**"]
      alert_level: "critical"
      severity_threshold: "low"
      fail_on_finding: true
      frequency: "on_commit"
      enabled: true
```

**Pitfalls to avoid:** Excluding `**/*.env*` from the scan scope to reduce noise — `.env` files are exactly where secrets live; exclude only test fixtures and mock data with known fake values. Don't set `severity_threshold: high` on a secrets scan; a "low-severity" staging key is still a real credential that should be rotated.

**Next step:** See `grok-deploy.yaml` to ensure all runtime secrets are injected via `source: secret` (never `source: literal`) at deploy time, completing the full secrets hygiene loop.

---

### License Violation Detector (Enterprise Legal / Engineering)

**Who uses this:** An enterprise engineering team whose legal department requires every dependency's license to be explicitly approved before it ships in a commercial product.

**Scenario:** An engineer adds a new npm package licensed under AGPL-3.0. If that package ships in your proprietary SaaS product, you may be legally required to open-source your entire codebase. No one notices until legal reviews the quarterly dependency report — months after the violation was introduced.

**How grok-security helps:** A `license_gdpr` scan with a curated `allowed_licenses` list blocks any PR introducing a dependency under an unapproved license. `frequency: on_pr` catches the violation at the earliest possible point — before code review, not after the quarterly audit.

**Example:**
```yaml
security:
  auto_block_prs: true
  allowed_licenses:
    - "MIT"
    - "Apache-2.0"
    - "BSD-2-Clause"
    - "BSD-3-Clause"
    - "ISC"
    - "0BSD"
    - "Unlicense"
  scans:
    LicenseCheck:
      type: "license_gdpr"
      files: ["package.json", "package-lock.json", "requirements.txt", "Gemfile.lock"]
      alert_level: "critical"
      fail_on_finding: true
      frequency: "on_pr"
      enabled: true
```

**Pitfalls to avoid:** Using `files: ["**/*"]` scans source files rather than dependency manifests — add only manifest and lockfile patterns you actually care about. Don't put `LGPL-2.1` on the `allowed_licenses` list without confirming whether your linking model triggers copyleft obligations for your specific use case.

**Next step:** See `grok-update.yaml` to run a weekly `license_gdpr` scan across all existing dependencies — not just new PRs — to catch licenses that change on package updates.
