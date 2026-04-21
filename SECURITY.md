# Security Policy

`grok-yaml-standards` is a reference library of YAML specifications and JSON Schemas. This document describes what is in scope, how to report a vulnerability, and what to expect in response.

## Supported Versions

Only the latest minor release line receives security fixes. Older lines may receive advisories but not patches.

| Version | Supported          |
|---------|--------------------|
| 1.2.x   | :white_check_mark: |
| 1.1.x   | Advisories only    |
| < 1.1   | :x:                |

## Threat Model

This repository ships three categories of artifact. The threat model differs for each.

### In scope

1. **JSON Schemas (`schemas/*.json`)** — Incorrect or permissive schemas that let malicious YAML slip past validation in downstream consumers (e.g. a schema that accepts arbitrary shell commands in a field documented as "string literal only"). Also: schema identifiers (`$id`) that could be spoofed or mis-resolved.
2. **Sample YAML (`.grok/*.yaml`, `grok-*/example.yaml`)** — Samples that, if copied verbatim, would expose a downstream repo to credential leakage, prompt-injection sinks, or unsafe-by-default tool permissions.
3. **GitHub Actions workflows (`.github/workflows/*.yml`)** — Supply-chain risks in our own CI: unpinned actions, untrusted inputs flowing into `run:` blocks, secrets exfiltration, or release impersonation.

### Out of scope

- Vulnerabilities in **downstream tools** that consume these specs (Grok itself, xAI platform, third-party validators, IDE plugins). Report those upstream.
- Behavior of user-authored `.grok/*.yaml` files in other repositories.
- Social-engineering claims about authorship/trust (e.g. "the README should warn users more sternly").
- Denial-of-service via pathological-but-valid YAML (validators are expected to bound their own resource use).
- Typos and broken links in documentation — please open a regular issue or PR.

## Reporting a Vulnerability

**Please do not open a public GitHub issue for security reports.**

Use **GitHub's Private Vulnerability Reporting** for this repository:

1. Go to <https://github.com/AgentMindCloud/grok-yaml-standards/security/advisories/new>
2. Fill in a title, description, affected artifact, and (if you have one) a proof of concept.
3. Submit. Only repository maintainers will see it.

If you have never used this feature before, GitHub's own guide is here: <https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability>.

Please include in your report:
- A clear description of the issue and the artifact affected (schema filename, workflow path, or sample YAML path).
- Steps to reproduce, a proof-of-concept, or a concrete attack scenario.
- Your assessment of severity and impact.
- Whether you would like public credit in the advisory.

## Disclosure SLA

| Stage                | Target         |
|----------------------|----------------|
| Acknowledgement      | Within 7 days  |
| Initial assessment   | Within 14 days |
| Fix or mitigation    | Within 30 days for high/critical; 90 days otherwise |
| Public advisory      | Coordinated with reporter after fix ships |

We follow a coordinated-disclosure model. We will credit reporters in the release notes and the published GitHub Security Advisory unless they request anonymity.

## Hardening Guidance for Consumers

If you ship a product that consumes `grok-yaml-standards`:

1. Pin to an exact release tag (e.g. `v1.2.0`), not `main`.
2. Validate every `.grok/*.yaml` against the matching schema in `schemas/` before acting on it.
3. Treat YAML fields documented as free-text (e.g. prompt templates) as untrusted input when they reach an LLM or a shell.
4. Never auto-execute workflow steps from an untrusted `.grok/grok-workflow.yaml` without human review.

## Acknowledgements

Thanks to everyone who reports issues responsibly. See `CHANGELOG.md` for the list of reporters credited in each release.
