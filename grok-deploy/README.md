---
title: grok-deploy
description: Deployment targets, env vars, health checks
image: /docs/posters/grok-deploy.png
---

# grok-deploy.yaml

**What problem it solves**  
Deployment configuration lives scattered across CI scripts, hosting dashboards, and tribal knowledge. `grok-deploy.yaml` brings deployment targets, environment variables, resource limits, and health checks into a single version-controlled YAML file that Grok can read, validate, and execute with a single @grok trigger.

**X Trigger Example**  
`@grok deploy staging` — deploys the current branch to the staging target  
`@grok deploy production` — deploys to production (requires approval when `require_approval: true`)

**Compatible with**  
`grok-install.yaml@1.0+` · `grok@2026.4+` · `grok-yaml-standards@1.2+`

**Benefits**  
- Zero-config deployments: define once, trigger from any issue or PR comment  
- Environment variable management with secret-reference syntax (no plain-text secrets in YAML)  
- Per-target resource limits prevent cost runaway in cloud environments  
- Built-in health check polling so Grok confirms the deploy succeeded before posting a status update
