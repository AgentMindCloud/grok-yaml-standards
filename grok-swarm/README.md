---
title: grok-swarm
description: Multi-agent orchestration patterns
image: /docs/posters/grok-swarm.png
---

# grok-swarm.yaml

**What problem it solves**
A single agent handles one thing at a time. Real release flows, research sweeps, and support queues need *several* agents working in lockstep — with a clear leader, known communication mode, an agreed-upon consensus rule, and a fallback path when a member fails. `grok-swarm.yaml` turns the 12-agent zoo into a named, coordinated swarm.

**X Trigger Example**
`@grok spawn swarm:ShipItSwarm` — spins up every member agent and wires up coordination
`@grok swarm status ShipItSwarm` — shows active members, coordinator, and last consensus decision

**Compatible with**
`grok-install.yaml@1.0+` · `grok@2026.4+` · `grok-yaml-standards@2.0+`

**Benefits**
- Declarative coordination — members, roles, priorities, and the lead agent live in one file instead of being implied by prompt engineering
- Explicit communication mode (`direct`, `broadcast`, `pubsub`) prevents surprise message floods and undocumented coupling
- Named consensus rule (`none`, `majority`, `unanimous`) makes disagreement handling auditable
- `fallback` strategy defines exactly what happens when a worker crashes or the coordinator drops — no silent partial runs
- New in `grok-yaml-standards@2.0` alongside `grok-voice.yaml` as part of the 14-spec set
