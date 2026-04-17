# Security Policy

## Supported Versions

| Version | Support status |
|---------|---------------|
| 1.2.x | ✅ Full support — security fixes and new features |
| 1.1.x | ⚠️ Security fixes only |
| < 1.1 | ❌ End of life — please upgrade |

---

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Open issues are visible to everyone, which means disclosing a vulnerability publicly before a fix is available could expose users to risk.

Instead, report privately via one of these channels:

1. **GitHub Security Advisory** (preferred): Navigate to the [Security tab](https://github.com/agentmindcloud/grok-yaml-standards/security/advisories/new) and open a private advisory. This keeps the report confidential until we coordinate a fix and disclosure.

2. **Email**: If you prefer, email the maintainer directly via the contact listed on the [@JanSol0s X profile](https://x.com/JanSol0s).

Please include:
- A description of the vulnerability and its potential impact
- The spec file(s) and version(s) affected
- Steps to reproduce or a proof-of-concept (even a minimal YAML snippet helps)
- Any suggested mitigations you have identified

---

## Response Timeline

| Milestone | Target |
|-----------|--------|
| Acknowledgement | Within 48 hours of receipt |
| Initial assessment | Within 5 business days |
| Fix or mitigation | Within 14 calendar days for critical issues |
| Public disclosure | Coordinated with reporter after fix is available |

We will keep you informed at each stage. If you do not receive an acknowledgement within 48 hours, please follow up — reports can occasionally be caught by spam filters.

---

## Scope

### In scope

- **Schema validation gaps**: A JSON Schema that accepts values a correctly-functioning Grok implementation would reject, or rejects values it should accept
- **Example YAML files that expose secrets**: Any `.grok/` template that inadvertently includes hardcoded credentials, tokens, or PII
- **Security documentation errors**: A `security-considerations.md` file that gives misleading advice that would cause a user to misconfigure their Grok setup insecurely
- **Injection vulnerabilities in spec design**: Schema field definitions or example patterns that facilitate prompt injection or command injection when used as documented

### Out of scope

- **xAI platform and Grok AI vulnerabilities**: These should be reported directly to xAI via their responsible disclosure programme
- **X (Twitter) platform vulnerabilities**: Report to Twitter/X via their security programme
- **Vulnerabilities in tools you build on top of these standards**: We define the schemas; your implementation security is your responsibility
- **Social engineering**: Issues that require deceiving a user into configuring their repo incorrectly

---

## PII and Data Policy

This repository does not collect, store, or process any personally identifiable information (PII).

- No analytics are collected by the repo itself
- `grok-analytics.yaml` is an **opt-in configuration spec** — no data is sent unless a user explicitly enables it and configures a provider
- All telemetry settings default to `false`

---

## Coordinated Disclosure

We follow [responsible disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure) principles. Once a fix is ready, we will:

1. Publish a patched release
2. Update the relevant spec files and schemas
3. Credit the reporter in the release notes (unless they prefer to remain anonymous)
4. Post a brief summary of the issue and fix in a GitHub Security Advisory

Thank you for helping keep grok-yaml-standards and its users safe.
