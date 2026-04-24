# grok-yaml-standards Documentation

All 14 official YAML specs for configuring Grok agents, workflows, and AI pipelines.

---

## Core Specs (v1.1.0+)

| Spec | File | Purpose |
|------|------|---------|
| [grok-config](../grok-config/schema.md) | `.grok/grok-config.yaml` | Global model, temperature, privacy and context settings |
| [grok-prompts](../grok-prompts/schema.md) | `.grok/grok-prompts.yaml` | Reusable prompt templates with variable interpolation |
| [grok-agent](../grok-agent/schema.md) | `.grok/grok-agent.yaml` | Persistent agent definitions — tools, memory, safety |
| [grok-workflow](../grok-workflow/schema.md) | `.grok/grok-workflow.yaml` | Multi-step pipelines with triggers and approval gates |
| [grok-update](../grok-update/schema.md) | `.grok/grok-update.yaml` | Scheduled knowledge base and dependency update jobs |
| [grok-test](../grok-test/schema.md) | `.grok/grok-test.yaml` | Automated test suites for agent and prompt quality |
| [grok-docs](../grok-docs/schema.md) | `.grok/grok-docs.yaml` | Auto-generated documentation targets (README, API ref) |
| [grok-security](../grok-security/schema.md) | `.grok/grok-security.yaml` | Secret detection, SAST, dependency CVE scanning |

## Extension Specs (v1.2.0+)

| Spec | File | Purpose |
|------|------|---------|
| [grok-tools](../grok-tools/schema.md) | `.grok/grok-tools.yaml` | Tool registry — capabilities, rate limits, security |
| [grok-deploy](../grok-deploy/schema.md) | `.grok/grok-deploy.yaml` | Deploy targets with health checks and rollback policy |
| [grok-analytics](../grok-analytics/schema.md) | `.grok/grok-analytics.yaml` | Usage metrics, cost tracking, provider configuration |
| [grok-ui](../grok-ui/schema.md) | `.grok/grok-ui.yaml` | IDE dashboard widgets and voice command bindings |

## Grok 4.20 Specs (v2.0.0+)

| Spec | File | Purpose |
|------|------|---------|
| [grok-swarm](grok-swarm.md) | `specs/grok-swarm.yaml` | Multi-agent swarm orchestration — parallel agent execution |
| [grok-voice](grok-voice.md) | `specs/grok-voice.yaml` | Speech-to-text and text-to-speech voice session config |

---

## Schema Discovery

All 14 schemas are listed in [`schemas/index.json`](../schemas/index.json). Load it once to discover every `schema_url` and `file_glob`:

```bash
# Fetch and pretty-print the manifest
curl -s https://raw.githubusercontent.com/agentmindcloud/grok-yaml-standards/main/schemas/index.json | python3 -m json.tool
```

## VS Code Integration

Add both the v1 glob and the new `specs/` glob to your workspace settings:

```json
{
  "yaml.schemas": {
    "https://raw.githubusercontent.com/agentmindcloud/grok-yaml-standards/main/schemas/grok-swarm.schema.json": "specs/grok-swarm.yaml",
    "https://raw.githubusercontent.com/agentmindcloud/grok-yaml-standards/main/schemas/grok-voice.schema.json": "specs/grok-voice.yaml"
  }
}
```

For the full VS Code snippet covering all 14 specs, see the [README](../README.md#vs-code--jetbrains-yaml-validation).

## CI Validation

The CI workflow at [`.github/workflows/validate.yml`](../.github/workflows/validate.yml) automatically validates every `.grok/*.yaml` and `specs/*.yaml` file against its JSON Schema on every push and pull request.
