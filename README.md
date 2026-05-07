# grok-yaml-standards

**The official community reference library extending grok-install.yaml with 14 magic YAML standards for Grok on X. Instant agents, workflows, prompts, swarms, voice, security, deployments & more — all via simple YAML + @grok triggers.**

[![GitHub stars](https://img.shields.io/github/stars/agentmindcloud/grok-yaml-standards)](https://github.com/agentmindcloud/grok-yaml-standards)  
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)  
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](standards-overview.md)  
[![Launched on X](https://img.shields.io/badge/Launched%20on%20X-000000?logo=x)](https://x.com/JanSol0s/status/2044691252327993364)

<!-- NEON / CYBERPUNK REPO TEMPLATE · GROK-YAML-STANDARDS -->

**Extending the official `grok-install.yaml` standard with 14 magic YAML files** — the definitive open reference library so that **X users, developers, and xAI** can all benefit from frictionless Grok-powered features via simple YAML files in any repo.

<h1 align="center">⚡ grok-yaml-standards</h1>

<p align="center">
  <b>The official community reference library extending <code>grok-install.yaml</code>.</b><br/>
  Twelve YAML standards. Zero setup. Trigger Grok-powered features in any repo via <code>@grok</code>.
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&weight=700&size=22&pause=1000&color=00E5FF&center=true&vCenter=true&width=900&lines=12+Magic+YAML+Standards;Zero-Setup+Grok+Features+on+X;JSON+Schema+Draft+7+Validated;Forward-Compatible+with+grok-install.yaml" alt="typing" />
</p>

**grok-yaml-standards v2.0.0** ships rich templates, a ready-to-drop `.grok/` folder, GitHub release automation, comprehensive JSON Schema validation, issue templates, two brand-new specs (`grok-swarm.yaml` and `grok-voice.yaml`), and the ecosystem foundation files (`LICENSE`, `DISCLAIMER.md`, `CHANGELOG.md`, `.github/FUNDING.yml`) shared across every repo in the GrokInstall family.

See the [CHANGELOG](CHANGELOG.md) for the full v2.0.0 release notes.

---

## ✦ What This Is

`grok-install.yaml` showed the world how a single YAML file can turn any GitHub repo into a Grok-native experience. **grok-yaml-standards** extends that with **12 drop-in YAML standards** — instant agents, workflows, prompts, security, deployments, analytics, and more — all triggered via `@grok` comments in any issue, PR, or README.

**v1.3.0** adds an optional **GrokHub Card** for registry publishing, **GrokForge Orchestration** on workflows (hybrid, graph, crew, debate_swarm modes), and 7 drop-in reference configs. Count stays at 12.

## ✦ The 12 Standards — At a Glance

<p align="center">
  <img src="https://img.shields.io/badge/grok--config-00E5FF?style=for-the-badge&logoColor=001018&labelColor=0A0D14" />
  <img src="https://img.shields.io/badge/grok--prompts-7C3AED?style=for-the-badge&logoColor=FFFFFF&labelColor=0A0D14" />
  <img src="https://img.shields.io/badge/grok--agent-FF4FD8?style=for-the-badge&logoColor=FFFFFF&labelColor=0A0D14" />
  <img src="https://img.shields.io/badge/grok--workflow-00D5FF?style=for-the-badge&logoColor=001018&labelColor=0A0D14" />
  <img src="https://img.shields.io/badge/grok--update-9D4EDD?style=for-the-badge&logoColor=FFFFFF&labelColor=0A0D14" />
  <img src="https://img.shields.io/badge/grok--test-5EF2FF?style=for-the-badge&logoColor=001018&labelColor=0A0D14" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/grok--docs-C026D3?style=for-the-badge&logoColor=FFFFFF&labelColor=0A0D14" />
  <img src="https://img.shields.io/badge/grok--security-38BDF8?style=for-the-badge&logoColor=001018&labelColor=0A0D14" />
  <img src="https://img.shields.io/badge/grok--tools%20(new)-00E5FF?style=for-the-badge&logoColor=001018&labelColor=0A0D14" />
  <img src="https://img.shields.io/badge/grok--deploy%20(new)-7C3AED?style=for-the-badge&logoColor=FFFFFF&labelColor=0A0D14" />
  <img src="https://img.shields.io/badge/grok--analytics%20(new)-FF4FD8?style=for-the-badge&logoColor=FFFFFF&labelColor=0A0D14" />
  <img src="https://img.shields.io/badge/grok--ui%20(new)-00D5FF?style=for-the-badge&logoColor=001018&labelColor=0A0D14" />
</p>

## ✦ Why You'd Use It

<table>
  <tr>
    <td width="33%">
      <h3>⚡ Zero Setup</h3>
      <p>Copy the <code>.grok/</code> folder, drop it in any repo, tag <code>@grok</code>. That's the entire install.</p>
    </td>
    <td width="33%">
      <h3>🛡️ Schema Validated</h3>
      <p>Every standard ships with JSON Schema Draft 7. CI runs <code>yamllint</code> + <code>ajv-cli</code> on every PR.</p>
    </td>
    <td width="33%">
      <h3>🔗 Forward Compatible</h3>
      <p>All 12 standards work with <code>grok-install.yaml@1.0+</code> and <code>grok@2026.4+</code>.</p>
    </td>
  </tr>
</table>

## ✦ 30 Seconds to First Trigger

```bash
git clone https://github.com/agentmindcloud/grok-yaml-standards.git
cd grok-yaml-standards
cp -r .grok/ /your/repo/.grok/          # drop in any repo
# Then in any issue, PR, or README, add a magic comment:
# @grok spawn agent:ResearchBot
# @grok run workflow:DailyDigest
# @grok security scan
```

## The 14 Magic YAML Standards

## ✦ Core Standards

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

## ✦ Spec Extensions

| YAML File | Primary Trigger | What It Unlocks | Benefit |
|-----------|----------------|-----------------|---------|
| [`grok-tools.yaml`](grok-tools/) | `@grok tools list` | Typed tool registry for agents & workflows | Correctness |
| [`grok-deploy.yaml`](grok-deploy/) | `@grok deploy <target>` | Deployment targets, env vars, health checks | Reliability |
| [`grok-analytics.yaml`](grok-analytics/) | `@grok analytics report` | Opt-in telemetry with PII controls | Insight |
| [`grok-ui.yaml`](grok-ui/) | `@grok ui status` | Voice commands, dashboard widgets, shortcuts | Experience |
| [`grok-swarm.yaml`](grok-swarm/) *(new in v2.0)* | `@grok spawn swarm:<id>` | Multi-agent swarms with coordinator, consensus, fallback | Scale |
| [`grok-voice.yaml`](grok-voice/) *(new in v2.0)* | `@grok voice start` | Full STT → intent → agent → TTS voice pipelines | Accessibility |

> Count authority: [`version-reconciliation.md`](version-reconciliation.md). If you see "14 standards" anywhere in the wild, it is incorrect as of v1.3.0.

## ✦ JSON Schema Validation

Every standard ships with a full JSON Schema in [`/schemas/`](schemas/). Target: **Draft 7**. Draft 2020-12 migration planned for v1.4.

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

</details>

Add this to VS Code `settings.json` for live validation:

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

Run the same validation locally:

```bash
npx ajv validate --spec=draft7 --all-errors --strict=false \
  -s schemas/grok-agent.json -d .grok/grok-agent.yaml
```

## ✦ Validation & CI

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| [`validate-schemas.yml`](.github/workflows/validate-schemas.yml) | `pull_request`, `push` to `main` | `yamllint` (config: [`.yamllint`](.yamllint)) against `.grok/` + every `grok-*/example.yaml` + every `grok-*/examples/*.yaml`, then `ajv-cli` Draft 7 against each of the 12 schemas, plus a smoke check on `$id`, `title`, `description`, `$schema` |
| [`release.yml`](.github/workflows/release.yml) | `push` of a `v*` tag | Publishes a GitHub Release via `softprops/action-gh-release@v2` with auto-generated notes |

## ✦ Compatibility Matrix

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
