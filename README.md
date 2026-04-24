<!-- Hero banner — uses locked brand tokens from .grok/brand-tokens.yaml -->
<p align="center">
  <img alt="grok-yaml-standards — 12 magic YAML standards for Grok on X"
       src="data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%20640%20120%27%20role%3D%27img%27%20aria-label%3D%27grok-yaml-standards%27%3E%3Crect%20width%3D%27640%27%20height%3D%27120%27%20fill%3D%27%230D0D0D%27%20rx%3D%2716%27%2F%3E%3Ctext%20x%3D%2740%27%20y%3D%2772%27%20font-family%3D%27Inter%2C%20system-ui%2C%20sans-serif%27%20font-size%3D%2740%27%20font-weight%3D%27800%27%20fill%3D%27%23FFFFFF%27%3Egrok-yaml-%3C%2Ftext%3E%3Ctext%20x%3D%27295%27%20y%3D%2772%27%20font-family%3D%27Inter%2C%20system-ui%2C%20sans-serif%27%20font-size%3D%2740%27%20font-weight%3D%27800%27%20fill%3D%27%231DA1F2%27%3Estandards%3C%2Ftext%3E%3Ctext%20x%3D%2740%27%20y%3D%27100%27%20font-family%3D%27Inter%2C%20system-ui%2C%20sans-serif%27%20font-size%3D%2714%27%20font-weight%3D%27500%27%20fill%3D%27%238899A6%27%3E12%20magic%20YAML%20standards%20for%20Grok%20on%20X%3C%2Ftext%3E%3Ccircle%20cx%3D%27600%27%20cy%3D%2760%27%20r%3D%2716%27%20fill%3D%27%23F5C518%27%2F%3E%3C%2Fsvg%3E"
       width="640" />
</p>

<p align="center">
  <a href="https://github.com/agentmindcloud/grok-yaml-standards"><img alt="GitHub stars" src="https://img.shields.io/github/stars/agentmindcloud/grok-yaml-standards?color=F5C518&labelColor=0D0D0D"></a>
  <a href="https://opensource.org/licenses/Apache-2.0"><img alt="License: Apache 2.0" src="https://img.shields.io/badge/License-Apache_2.0-1DA1F2?labelColor=0D0D0D"></a>
  <a href="standards-overview.md"><img alt="Version" src="https://img.shields.io/badge/version-1.3.0-1DA1F2?labelColor=0D0D0D"></a>
  <a href="CHANGELOG.md"><img alt="Changelog" src="https://img.shields.io/badge/changelog-keep--a--changelog-F5C518?labelColor=0D0D0D"></a>
  <a href="https://x.com/JanSol0s/status/2044691252327993364"><img alt="Launched on X" src="https://img.shields.io/badge/Launched%20on%20X-0D0D0D?logo=x"></a>
</p>

# grok-yaml-standards

**The official community reference library extending `grok-install.yaml` with 12 magic YAML standards for Grok on X. Instant agents, workflows, prompts, security, deployments & more — all via simple YAML + `@grok` triggers.**

**The Central Community Hub for Grok YAML Magic on X** — the definitive open reference library so that **X users, developers, and xAI** can all benefit from frictionless Grok-powered features via simple YAML files in any repo.

> Brand tokens (colors, typography, hero logo) are locked in [`.grok/brand-tokens.yaml`](.grok/brand-tokens.yaml). The hero banner above is an inline SVG data-URI — no binary assets.

---

## Why This Repo Exists

`grok-install.yaml` showed the world how a single YAML file can turn any GitHub repo into a Grok-native experience.

**grok-yaml-standards v1.3.0** extends `grok-agent` with an optional **GrokHub Card** for registry publishing, adds a **GrokForge Orchestration** block to `grok-workflow` (hybrid, graph, crew, debate_swarm modes), and ships seven drop-in reference configs under `grok-*/examples/`. The library keeps its ready `.grok/` folder, full JSON Schema coverage, and CI validation — now extended to the new examples too.

---

## How to Use Today (Zero Setup)

1. Copy any file from the ready `.grok/` sample folder
2. Place it in your repo at `.grok/grok-xxx.yaml`
3. Add a magic trigger comment in any issue, PR, or README
4. Tag `@grok` — Grok instantly activates the feature

---

## Quick Start

```bash
git clone https://github.com/agentmindcloud/grok-yaml-standards.git
cd grok-yaml-standards
# Drop the ready .grok/ folder into your repo and start triggering today!
cp -r .grok/ /your/repo/.grok/
```

---

## The 12 Magic YAML Standards

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

> Count authority: [`version-reconciliation.md`](version-reconciliation.md). If you see "14 standards" anywhere in the wild, it is incorrect as of v1.3.0.

---

## JSON Schema Validation

Every standard ships with a full JSON Schema in [`/schemas/`](schemas/). Validators are available for all 12 specs:

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

Schemas target **JSON Schema Draft 7**. Draft 2020-12 migration is planned for v1.4.

Add this to your VS Code `settings.json` for live validation:

```json
{
  "yaml.schemas": {
    "https://github.com/agentmindcloud/grok-yaml-standards/schemas/grok-config.json": ".grok/grok-config.yaml",
    "https://github.com/agentmindcloud/grok-yaml-standards/schemas/grok-agent.json": ".grok/grok-agent.yaml",
    "https://github.com/agentmindcloud/grok-yaml-standards/schemas/grok-tools.json": ".grok/grok-tools.yaml"
  }
}
```

---

## Validation & CI

Two GitHub Actions workflows back every change in this repo:

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| [`validate-schemas.yml`](.github/workflows/validate-schemas.yml) | `pull_request`, `push` to `main` | Runs `yamllint` (config: [`.yamllint`](.yamllint)) against `.grok/` + every `grok-*/example.yaml` + every `grok-*/examples/*.yaml`, then `ajv-cli` (Draft 7) against each of the 12 schemas, plus a smoke check that every `schemas/*.json` declares `$id`, `title`, `description`, and `$schema: draft-07`. |
| [`release.yml`](.github/workflows/release.yml) | `push` of a `v*` tag | Publishes a GitHub Release via `softprops/action-gh-release@v2` with auto-generated notes. |

Run the same validation locally against a single file:

```bash
npx ajv validate --spec=draft7 --all-errors --strict=false \
  -s schemas/grok-agent.json -d .grok/grok-agent.yaml
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
| grok-tools *(new)* | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-deploy *(new)* | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-analytics *(new)* | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-ui *(new)* | `@1.0+` | `@2026.4+` | `@1.2+` |

---

## New in v1.3.0

- **GrokHub Card** — optional `hub_card` block on `grok-agent` for publishing agents to a discoverable registry (opt-in; existing agents unaffected).
- **GrokForge Orchestration** — optional `orchestration` block on `grok-workflow` supporting `hybrid`, `graph`, `crew`, and `debate_swarm` modes with vector-memory backing.
- **4 reference agents** in [`grok-agent/examples/`](grok-agent/examples/) (`research-swarm-v2`, `trend-to-thread-bot`, `code-reviewer-agent`, `private-ops-agent`).
- **3 reference workflows** in [`grok-workflow/examples/`](grok-workflow/examples/) (`massive-x-research-swarm`, `debate-swarm-example`, `simple-graph-agent`).
- **CI coverage** — [`validate-schemas`](.github/workflows/validate-schemas.yml) now lints and validates every `grok-*/examples/*.yaml` file.
- Count stays **12**. No new schemas; no new top-level standards.

See the full history in [`CHANGELOG.md`](CHANGELOG.md).

---

## What's Coming

### v1.4 — tooling pass
- `grok-validate` CLI (Node + Go builds) that wraps ajv + yamllint against the 12 shipped schemas
- VS Code extension pre-wired to the schema registry
- JSON Schema Draft 2020-12 migration, gated on downstream compatibility testing

### v2.14 — exploratory (no commitment)
A long-horizon look at whether two extra standards (`grok-cache`, `grok-auth`) are worth adding. Tracked in [`version-reconciliation.md`](version-reconciliation.md). **Until and unless a future release explicitly bumps it, the library stays at 12 standards.**

---

## Related Docs

- [`ROADMAP.md`](ROADMAP.md) — path to official xAI adoption and per-version milestones.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — branching convention, review flow, and what we welcome.
- [`SECURITY.md`](SECURITY.md) — threat model and private vulnerability reporting.
- [`how-xai-can-adopt.md`](how-xai-can-adopt.md) — the pitch we hand to the xAI team.
- [`standards-overview.md`](standards-overview.md) — side-by-side comparison of all 12 standards.
- [`schemas/README.md`](schemas/README.md) — per-schema notes and the full VS Code snippet.

---

## Contributors

Thank you to everyone building the future of Grok on X.

| Contributor | Role | Contributions |
|---|---|---|
| <a href="https://github.com/JanSol0s"><img src="https://github.com/JanSol0s.png" width="48" height="48" alt="@JanSol0s" /></a><br/>**[@JanSol0s](https://github.com/JanSol0s)** | Creator &amp; Maintainer | v1.0.0 → v1.3.0 · All 12 standards · JSON Schemas · Compatibility matrix · Apache 2.0 relicense · X launch · Hub Card · Orchestration |

Full list + "how to be added" in [`CONTRIBUTORS.md`](CONTRIBUTORS.md). Security reports go through [`SECURITY.md`](SECURITY.md).

---

Made with love by the Grok community for xAI and every X user.

**Version 1.3.0** · Forward-compatible with `grok-install.yaml@1.0+` · Licensed under Apache 2.0 · [Launched on X April 16, 2026](https://x.com/JanSol0s/status/2044691252327993364)
