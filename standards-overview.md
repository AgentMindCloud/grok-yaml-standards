# standards-overview.md

## The 12 Grok YAML Standards at a Glance

### Core Standards

| Feature | grok-config | grok-prompts | grok-agent | grok-workflow | grok-update | grok-test | grok-docs | grok-security |
|---------|-------------|--------------|------------|---------------|-------------|-----------|-----------|---------------|
| **Primary Use** | Settings | Prompt library | Persistent agents | Automation | Auto-updates | Testing | Documentation | Security & compliance |
| **Versioned** | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **X Trigger Ready** | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **Stateful** | No | No | Yes | Yes | Partial | No | No | No |
| **Shareable** | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **Forward-compatible** | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **Security Level** | Medium | Low | High | High | Medium | Medium | Low | Critical |

### Spec Extensions (new in v1.2.0)

| Feature | grok-tools | grok-deploy | grok-analytics | grok-ui |
|---------|-----------|-------------|----------------|---------|
| **Primary Use** | Tool registry | Deployments | Telemetry | UX / voice |
| **Versioned** | Yes | Yes | Yes | Yes |
| **X Trigger Ready** | Yes | Yes | Yes | Yes |
| **Stateful** | No | No | No | Partial |
| **Shareable** | Yes | Yes | Yes | Yes |
| **Forward-compatible** | Yes | Yes | Yes | Yes |
| **Security Level** | High | Critical | Medium | Medium |

---

## JSON Schema Validation (v1.2.0)

All 12 specs ship official JSON Schemas in the [`/schemas/`](schemas/) folder. Every schema is a complete draft-07 contract with:

- **Enum constraints** on all known string values (model names, memory modes, alert levels, etc.)
- **Pattern validation** for semver, X handles (`@name`), BCP-47 language codes, glob patterns
- **Numeric bounds** on temperature, token counts, timeouts, retry counts
- **`required` declarations** at every nesting level — never silently missing a field
- **`additionalProperties: false`** on closed objects — typos are caught immediately
- **Descriptions** on every field — hover tooltips in VS Code out of the box

This enables automatic validation in GitHub CI, VS Code, JetBrains, and any editor with YAML Schema support.

---

## Shared YAML structure

All 12 files follow the same header convention:

```yaml
version: "1.2.0"
author: "@yourhandle"
compatibility:
  - "grok-install.yaml@1.0+"
  - "grok@2026.4+"
  - "grok-yaml-standards@1.2+"
```

This makes the compatibility contract explicit and machine-readable. xAI can check these fields to determine which features a repo's `.grok/` folder supports before processing any triggers.

---

## Minimum compatibility versions

| Standard | grok-install.yaml | grok | grok-yaml-standards |
|----------|------------------|------|---------------------|
| grok-config | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-prompts | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-agent | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-workflow | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-update | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-test | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-docs | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-security | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-tools | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-deploy | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-analytics | `@1.0+` | `@2026.4+` | `@1.2+` |
| grok-ui | `@1.0+` | `@2026.4+` | `@1.2+` |
