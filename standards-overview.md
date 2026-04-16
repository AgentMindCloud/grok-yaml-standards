# standards-overview.md

## Comparison of All 8 Grok YAML Standards

| Feature                  | grok-config | grok-prompts | grok-agent | grok-workflow | grok-update | grok-test | grok-docs | grok-security |
|--------------------------|-------------|--------------|------------|---------------|-------------|-----------|-----------|---------------|
| **Primary Use**          | Settings    | Prompt library | Persistent agents | Automation | Auto-updates | Testing | Documentation | Security & compliance |
| **Versioned**            | Yes         | Yes          | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **X Trigger Ready**      | Yes         | Yes          | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **Stateful**             | No          | No           | Yes        | Yes           | Partial     | No        | No        | No            |
| **Shareable**            | Yes         | High         | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **Forward-compatible**   | Yes         | Yes          | Yes        | Yes           | Yes         | Yes       | Yes       | Yes           |
| **Security Level**       | Medium      | Low          | High       | High          | Medium      | Medium    | Low       | Critical      |

**All files** follow the same modern YAML structure:
```yaml
version: "1.0.0"
author: "@yourhandle"
compatibility: ["grok-install.yaml@1.0+", "grok@2026.4+"]
...
### JSON Schema Validation (New in v1.2.0)
All 8 magic files now have official JSON Schemas in the `/schemas/` folder.  
This enables automatic validation in GitHub, VS Code, and any modern editor.

**Benefits:**
- Real-time error checking
- Auto-complete for contributors
- Future-proof for xAI native support
