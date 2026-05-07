---
title: grok-workflow
description: Multi-step automated processes
image: /docs/posters/grok-workflow.png
---

# grok-workflow.yaml

**What problem it solves**  
Multi-step automation without leaving X.

**X Trigger Example**  
`@grok run workflow`

**Benefits**  
One-click complex processes.

## Orchestration (v1.3+)

Since v1.3.0, any workflow may declare an optional `orchestration` block that
coordinates one or more sub-agents under a declared execution mode — `hybrid`,
`graph`, `crew`, or `debate_swarm`. It carries `agents`, an optional `graph`
edge list, a `debate_swarm` config, and a shared `memory` backend
(`ephemeral` / `session` / `long_term` / `vector`).

The block is fully optional — existing `grok-workflow.yaml` files validate
unchanged. See [`examples/`](examples/) for three drop-in reference configs:
a 28-instance hybrid research swarm, a 3-agent debate swarm, and a minimal
linear graph pipeline.
