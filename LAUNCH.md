# grok-yaml-standards v1.2.0 — Launch

## Official Launch — April 16, 2026

**grok-yaml-standards v1.2.0** is live on X.

Full launch thread: https://x.com/JanSol0s/status/2044691252327993364

> @grok replied: "This is epic community work! YAML standards for Grok…
> Let's build this future together. 🚀"

---

## What's in v1.2.0

### 12 magic YAML standards

**Core standards** (grok-install.yaml@1.0+ compatible):

| Standard | What it does |
|----------|-------------|
| `grok-config.yaml` | Repo-wide model settings, personality, privacy controls |
| `grok-prompts.yaml` | Reusable versioned prompt library with variable interpolation |
| `grok-agent.yaml` | Persistent stateful agents with memory and tool access |
| `grok-workflow.yaml` | Multi-step automated pipelines with conditional branching |
| `grok-update.yaml` | Scheduled smart updates for docs, deps, and knowledge bases |
| `grok-test.yaml` | AI-powered test suites for code quality, security, and a11y |
| `grok-docs.yaml` | Auto-generated, always-up-to-date documentation |
| `grok-security.yaml` | Real-time security and compliance scanning |

**Spec extensions** (new in v1.2.0):

| Standard | What it does |
|----------|-------------|
| `grok-tools.yaml` | Typed tool registry for agents and workflows |
| `grok-deploy.yaml` | Deployment targets, env vars, resource limits, health checks |
| `grok-analytics.yaml` | Opt-in telemetry with PII-safe event declarations |
| `grok-ui.yaml` | Voice commands, live dashboard widgets, keyboard shortcuts |

### Full JSON Schema validation for all 12 specs

Every spec ships a draft-07 JSON Schema in `/schemas/` with:
- Enum constraints on all known string values
- Pattern validation (semver, X handles, BCP-47 language codes, globs)
- Numeric bounds on temperature, token counts, timeouts, and retry counts
- `required` declarations at every nesting level
- Human-readable descriptions on every field

### Apache 2.0 license

Relicensed from MIT to Apache 2.0 to align with the xAI ecosystem.

---

## No Breaking Changes from v1.1.x

All v1.1.x `.grok/` folders remain valid. v1.2.0 is purely additive.

To opt in to new v1.2.0 features, update one line in your compatibility array:

```yaml
# Before (v1.1.x)
compatibility:
  - "grok-yaml-standards@1.1+"

# After (v1.2.0)
compatibility:
  - "grok-yaml-standards@1.2+"
```

No other changes required.

---

## Quick Start

```bash
git clone https://github.com/agentmindcloud/grok-yaml-standards.git
cp -r grok-yaml-standards/.grok/ your-repo/.grok/
# Then tag @grok in any issue or PR comment
```

---

Star ⭐ Fork 🍴 Build something great.

— The Grok YAML Standards Community
