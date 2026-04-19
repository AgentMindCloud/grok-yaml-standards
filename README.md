# grok-yaml-standards

**The official community reference library extending grok-install.yaml with 14 magic YAML standards for Grok on X. Instant agents, workflows, prompts, swarms, voice, security, deployments & more — all via simple YAML + @grok triggers.**

[![GitHub stars](https://img.shields.io/github/stars/agentmindcloud/grok-yaml-standards)](https://github.com/agentmindcloud/grok-yaml-standards)  
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)  
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](standards-overview.md)  
[![Launched on X](https://img.shields.io/badge/Launched%20on%20X-000000?logo=x)](https://x.com/JanSol0s/status/2044691252327993364)

**The Central Community Hub for Grok YAML Magic on X**

**Extending the official `grok-install.yaml` standard with 14 magic YAML files** — the definitive open reference library so that **X users, developers, and xAI** can all benefit from frictionless Grok-powered features via simple YAML files in any repo.

---

## Why This Repo Exists

`grok-install.yaml` showed the world how a single YAML file can turn any GitHub repo into a Grok-native experience.

**grok-yaml-standards v2.0.0** ships rich templates, a ready-to-drop `.grok/` folder, GitHub release automation, comprehensive JSON Schema validation, issue templates, two brand-new specs (`grok-swarm.yaml` and `grok-voice.yaml`), and the ecosystem foundation files (`LICENSE`, `DISCLAIMER.md`, `CHANGELOG.md`, `.github/FUNDING.yml`) shared across every repo in the GrokInstall family.

See the [CHANGELOG](CHANGELOG.md) for the full v2.0.0 release notes.

---

## How to Use Today (Zero Setup)

1. Copy any file from the ready `.grok/` sample folder
2. Place it in your repo at `.grok/grok-xxx.yaml`
3. Add a magic trigger comment in any issue, PR, or README
4. Tag `@grok` — Grok instantly activates the feature

---

## The 14 Magic YAML Standards

### Core Standards

| YAML File | Primary Trigger | What It Unlocks | Benefit |
|-----------|----------------|-----------------|---------|
| [`grok-config.yaml`](grok-config/) | `@grok config` | Repo-wide model settings & defaults | Consistency |
| [`grok-prompts.yaml`](grok-prompts/) | `@grok use prompts:<id>` | Reusable versioned prompt library | Creativity |
| [`grok-agent.yaml`](grok-agent/) | `@grok spawn agent:<Name>` | Persistent stateful Grok agents | Automation |
| [`grok-workflow.yaml`](grok-workflow/) | `@grok run workflow:<Name>` | Multi-step automated processes | Productivity |
| [`grok-update.yaml`](grok-update/) | `@grok update` | Smart repo & knowledge updates | Freshness |
| [`grok-test.yaml`](grok-test/) | `@grok test` | AI-powered testing & validation | Quality |
| [`grok-docs.yaml`](grok-docs/) | `@grok docs` | Auto-generated documentation | Clarity |
| [`grok-security.yaml`](grok-security/) | `@grok security scan` | Real-time security & compliance | Safety |

### Spec Extensions

| YAML File | Primary Trigger | What It Unlocks | Benefit |
|-----------|----------------|-----------------|---------|
| [`grok-tools.yaml`](grok-tools/) | `@grok tools list` | Typed tool registry for agents & workflows | Correctness |
| [`grok-deploy.yaml`](grok-deploy/) | `@grok deploy <target>` | Deployment targets, env vars, health checks | Reliability |
| [`grok-analytics.yaml`](grok-analytics/) | `@grok analytics report` | Opt-in telemetry with PII controls | Insight |
| [`grok-ui.yaml`](grok-ui/) | `@grok ui status` | Voice commands, dashboard widgets, shortcuts | Experience |
| [`grok-swarm.yaml`](grok-swarm/) *(new in v2.0)* | `@grok spawn swarm:<id>` | Multi-agent swarms with coordinator, consensus, fallback | Scale |
| [`grok-voice.yaml`](grok-voice/) *(new in v2.0)* | `@grok voice start` | Full STT → intent → agent → TTS voice pipelines | Accessibility |

---

## Quick Start

```bash
git clone https://github.com/agentmindcloud/grok-yaml-standards.git
cd grok-yaml-standards
# Drop the ready .grok/ folder into your repo and start triggering today!
cp -r .grok/ /your/repo/.grok/
```

---

## JSON Schema Validation

Every standard ships with a full JSON Schema in [`/schemas/`](schemas/). Validators are available for all 14 specs:

| Schema | Validates |
|--------|-----------|
| [`schemas/grok-config.json`](schemas/grok-config.json) | Model settings, privacy, shortcuts |
| [`schemas/grok-prompts.json`](schemas/grok-prompts.json) | Prompt templates, variables, output format |
| [`schemas/grok-agent.json`](schemas/grok-agent.json) | Agent definitions, tools, memory, rate limits |
| [`schemas/grok-workflow.json`](schemas/grok-workflow.json) | Workflow steps, conditions, error handling |
| [`schemas/grok-update.json`](schemas/grok-update.json) | Update jobs, schedule, actions |
| [`schemas/grok-test.json`](schemas/grok-test.json) | Test suites, alert levels, categories |
| [`schemas/grok-docs.json`](schemas/grok-docs.json) | Doc targets, sections, style presets |
| [`schemas/grok-security.json`](schemas/grok-security.json) | Scans, compliance standards, notifications |
| [`schemas/grok-tools.json`](schemas/grok-tools.json) | Tool signatures, permissions, rate limits |
| [`schemas/grok-deploy.json`](schemas/grok-deploy.json) | Deploy targets, resource limits, health checks |
| [`schemas/grok-analytics.json`](schemas/grok-analytics.json) | Event definitions, PII safety, retention |
| [`schemas/grok-ui.json`](schemas/grok-ui.json) | Voice commands, dashboard widgets, shortcuts |
| [`schemas/grok-swarm.json`](schemas/grok-swarm.json) | Swarm members, coordinator, consensus, fallback |
| [`schemas/grok-voice.json`](schemas/grok-voice.json) | Voice pipeline, input/output, latency, privacy |

Add this to your VS Code `settings.json` for live validation:

```json
{
  "yaml.schemas": {
    "https://github.com/agentmindcloud/grok-yaml-standards/schemas/grok-config.json": ".grok/grok-config.yaml",
    "https://github.com/agentmindcloud/grok-yaml-standards/schemas/grok-agent.json": ".grok/grok-agent.yaml",
    "https://github.com/agentmindcloud/grok-yaml-standards/schemas/grok-tools.json": ".grok/grok-tools.yaml",
    "https://github.com/agentmindcloud/grok-yaml-standards/schemas/grok-swarm.json": ".grok/grok-swarm.yaml",
    "https://github.com/agentmindcloud/grok-yaml-standards/schemas/grok-voice.json": ".grok/grok-voice.yaml"
  }
}
```

---

## Compatibility Matrix

Every file in this library is forward-compatible with the specs below. The matrix shows the minimum version required for each standard.

| Standard | grok-install.yaml | grok | grok-yaml-standards |
|----------|------------------|------|---------------------|
| grok-config | `@1.0+` | `@2026.4+` | `@1.1+` |
| grok-prompts | `@1.0+` | `@2026.4+` | `@1.1+` |
| grok-agent | `@1.0+` | `@2026.4+` | `@1.1+` |
| grok-workflow | `@1.0+` | `@2026.4+` | `@1.1+` |
| grok-update | `@1.0+` | `@2026.4+` | `@1.1+` |
| grok-test | `@1.0+` | `@2026.4+` | `@1.1+` |
| grok-docs | `@1.0+` | `@2026.4+` | `@1.1+` |
| grok-security | `@1.0+` | `@2026.4+` | `@1.1+` |
| grok-tools | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-deploy | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-analytics | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-ui | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-swarm *(new)* | `@1.0+` | `@2026.4+` | `@2.0+` |
| grok-voice *(new)* | `@1.0+` | `@2026.4+` | `@2.0+` |

---

## New in v2.0.0

- **Two new specs**: `grok-swarm.yaml` (multi-agent coordination — members, roles, coordinator, consensus, fallback) and `grok-voice.yaml` (full STT → intent → agent → TTS pipelines with latency budgets and explicit privacy controls)
- **Spec count** 12 → 14 and **repo version** v1.2 → v2.0
- **Ecosystem foundation files**: `LICENSE` (full Apache 2.0), `DISCLAIMER.md`, `CHANGELOG.md`, `.github/FUNDING.yml` — shared verbatim across every repo in the GrokInstall ecosystem
- Every per-spec `.grok/*.yaml` and `*/example.yaml` bumped to `version: "2.0.0"` with `grok-yaml-standards@2.0+` compatibility

See [CHANGELOG.md](CHANGELOG.md) for the full details.

---

## Contributors Gallery

Thank you to everyone building the future of Grok on X!

- **@JanSol0s** — Founder & Maintainer

*(Your name here after your first PR ⭐)*

---

Made with ❤️ by the Grok community for xAI and every X user.

**Version 2.0.0** · Forward-compatible with `grok-install.yaml@1.0+` · Licensed under Apache 2.0 · [Launched on X April 16, 2026](https://x.com/JanSol0s/status/2044691252327993364)

---

GrokInstall is an independent community project.
Not affiliated with xAI, Grok, or X.
