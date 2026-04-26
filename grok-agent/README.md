---
title: grok-agent
description: Persistent stateful Grok agents
image: /docs/posters/grok-agent.png
---

# grok-agent.yaml

**What problem it solves**  
Turns any repo into a stateful Grok agent.

**X Trigger Example**  
`@grok spawn agent`

**Benefits**  
Long-running, memory-aware automation.

## Hub Card (v1.3+)

Since v1.3.0, any agent may declare an optional `hub_card` block that turns the
definition into a discoverable GrokHub registry entry. It carries `publish`,
`registry_name`, `model`, `github`, `tags`, `safety_profile`,
`permission_scopes`, install/deploy commands, stats, `x_native_features`, and
`leaderboard_score`.

The block is fully optional — existing `grok-agent.yaml` files validate
unchanged. See [`examples/`](examples/) for four drop-in reference configs
covering public, content-generation, strict read-only, and private opt-out
shapes.
