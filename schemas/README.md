# schemas/ — JSON Schema Validation

This folder contains official JSON Schema files (draft-07) for **all 14 grok-yaml-standards specs**.

Every schema is a complete, property-level contract with:
- Typed and described fields at every nesting level
- `enum` constraints for all known string values
- `pattern` validation for semver strings, X handles, language codes, and glob patterns
- `minimum`/`maximum` bounds on numeric fields
- `required` declarations at every nesting level
- `additionalProperties: false` on closed objects to catch typos immediately
- `default` values documenting runtime behaviour

## Files included

### Core standards
| Schema | Validates |
|--------|-----------|
| `grok-config.json` | Model settings, temperature, privacy, shortcuts |
| `grok-prompts.json` | Prompt templates, variables, per-prompt overrides |
| `grok-agent.json` | Agent definitions, tools, memory modes, rate limits |
| `grok-workflow.json` | Workflow steps, conditions, error handling, timeouts |
| `grok-update.json` | Update jobs, frequency, cron schedules, actions |
| `grok-test.json` | Test suites, categories, alert levels, PR blocking |
| `grok-docs.json` | Doc targets, sections, style presets, update triggers |
| `grok-security.json` | Scans, compliance standards, notifications, licenses |

### Spec extensions
| Schema | Validates |
|--------|-----------|
| `grok-tools.json` | Tool signatures, input/output schemas, permissions, rate limits |
| `grok-deploy.json` | Deploy targets, env vars, resource limits, health checks |
| `grok-analytics.json` | Events, PII safety, provider config, sampling rate |
| `grok-ui.json` | Voice commands, dashboard widgets, keyboard shortcuts, themes |
| `grok-swarm.json` | Swarm members, roles, coordinator, communication, consensus, fallback |
| `grok-voice.json` | Voice pipeline (STT → intent → agent → TTS), latency budget, privacy controls |

## Using schemas in your IDE

**VS Code** — add to `.vscode/settings.json`:
```json
{
  "yaml.schemas": {
    "./schemas/grok-config.json": ".grok/grok-config.yaml",
    "./schemas/grok-prompts.json": ".grok/grok-prompts.yaml",
    "./schemas/grok-agent.json": ".grok/grok-agent.yaml",
    "./schemas/grok-workflow.json": ".grok/grok-workflow.yaml",
    "./schemas/grok-update.json": ".grok/grok-update.yaml",
    "./schemas/grok-test.json": ".grok/grok-test.yaml",
    "./schemas/grok-docs.json": ".grok/grok-docs.yaml",
    "./schemas/grok-security.json": ".grok/grok-security.yaml",
    "./schemas/grok-tools.json": ".grok/grok-tools.yaml",
    "./schemas/grok-deploy.json": ".grok/grok-deploy.yaml",
    "./schemas/grok-analytics.json": ".grok/grok-analytics.yaml",
    "./schemas/grok-ui.json": ".grok/grok-ui.yaml",
    "./schemas/grok-swarm.json": ".grok/grok-swarm.yaml",
    "./schemas/grok-voice.json": ".grok/grok-voice.yaml"
  }
}
```

**Version:** 2.0.0 · Forward-compatible with `grok-install.yaml@1.0+`
