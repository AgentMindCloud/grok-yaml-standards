# standards-overview.md

## Comparison of All 12 Grok YAML Standards

### Core Standards (8)

| Feature                  | grok-config | grok-prompts | grok-agent | grok-workflow | grok-update | grok-test | grok-docs | grok-security |
|--------------------------|-------------|--------------|------------|---------------|-------------|-----------|-----------|---------------|
| **Primary Use**          | Settings    | Prompt library | Persistent agents | Automation | Auto-updates | Testing | Documentation | Security & compliance |
| **Versioned**            | Yes         | Yes          | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **X Trigger Ready**      | Yes         | Yes          | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **Stateful**             | No          | No           | Yes        | Yes           | Partial     | No        | No        | No            |
| **Shareable**            | Yes         | High         | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **Forward-compatible**   | Yes         | Yes          | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **Security Level**       | Medium      | Low          | High       | High          | Medium      | Medium    | Low       | Critical      |

### Spec Extensions (4, added in v1.2.0)

| Feature                  | grok-tools | grok-deploy | grok-analytics | grok-ui |
|--------------------------|------------|-------------|----------------|---------|
| **Primary Use**          | Typed tool registry | Deployment targets | Opt-in telemetry | Voice + UI surface |
| **Versioned**            | Yes        | Yes         | Yes            | Yes     |
| **X Trigger Ready**      | Yes        | Yes         | Yes            | Yes     |
| **Stateful**             | No         | Partial     | Yes            | No      |
| **Shareable**            | Yes        | Yes         | Yes            | Yes     |
| **Forward-compatible**   | Yes        | Yes         | Yes            | Yes     |
| **Security Level**       | High       | Critical    | High (PII)     | Medium  |

**All files** follow the same modern YAML structure:

```yaml
version: "1.2.0"
author: "@yourhandle"
compatibility: ["grok-install.yaml@1.0+", "grok@2026.4+"]
# …
```

### JSON Schema Validation (introduced in v1.2.0)

All 12 magic files have official JSON Schemas in the [`schemas/`](schemas/) folder.
This enables automatic validation in GitHub, VS Code, and any modern editor.

**Benefits:**
- Real-time error checking
- Auto-complete for contributors
- Future-proof for xAI native support

> Schemas currently target JSON Schema **Draft 7**. Draft 2020-12 migration is on the v1.3 roadmap once all downstream consumers confirm compatibility.

See [`version-reconciliation.md`](version-reconciliation.md) for the authoritative list and the one-line PR text to correct any downstream repo that claims a different count.
