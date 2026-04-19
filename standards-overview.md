# standards-overview.md

## Comparison of All 14 Grok YAML Standards

### Core standards

| Feature                  | grok-config | grok-prompts | grok-agent | grok-workflow | grok-update | grok-test | grok-docs | grok-security |
|--------------------------|-------------|--------------|------------|---------------|-------------|-----------|-----------|---------------|
| **Primary Use**          | Settings    | Prompt library | Persistent agents | Automation | Auto-updates | Testing | Documentation | Security & compliance |
| **Versioned**            | Yes         | Yes          | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **X Trigger Ready**      | Yes         | Yes          | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **Stateful**             | No          | No           | Yes        | Yes           | Partial     | No        | No        | No            |
| **Shareable**            | Yes         | High         | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **Forward-compatible**   | Yes         | Yes          | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **Security Level**       | Medium      | Low          | High       | High          | Medium      | Medium    | Low       | Critical      |

### Spec extensions

| Feature                  | grok-tools | grok-deploy | grok-analytics | grok-ui | grok-swarm | grok-voice |
|--------------------------|------------|-------------|----------------|---------|------------|------------|
| **Primary Use**          | Tool registry | Deployments | Telemetry | UI & shortcuts | Multi-agent coordination | Voice pipelines |
| **Versioned**            | Yes | Yes | Yes | Yes | Yes | Yes |
| **X Trigger Ready**      | Yes | Yes | Yes | Yes | Yes | Yes |
| **Stateful**             | No | Yes | Yes | No | Yes | Yes |
| **Shareable**            | High | Yes | Yes | Yes | High | High |
| **Forward-compatible**   | Yes | Yes | Yes | Yes | Yes | Yes |
| **Security Level**       | Medium | High | High | Low | High | Critical |

**All files** follow the same modern YAML structure:
```yaml
version: "2.0.0"
author: "@yourhandle"
compatibility: ["grok-install.yaml@1.0+", "grok@2026.4+", "grok-yaml-standards@2.0+"]
...
```

### JSON Schema Validation
All 14 magic files have official JSON Schemas in the `/schemas/` folder.
This enables automatic validation in GitHub, VS Code, and any modern editor.

**Benefits:**
- Real-time error checking
- Auto-complete for contributors
- Future-proof for xAI native support

### New in v2.0.0
- `grok-swarm.yaml` — multi-agent coordination with coordinator, consensus, and fallback
- `grok-voice.yaml` — full STT → intent → agent → TTS pipeline with latency budget and privacy controls
- Ecosystem foundation files: `LICENSE`, `DISCLAIMER.md`, `CHANGELOG.md`, `.github/FUNDING.yml`
