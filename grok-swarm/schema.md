# grok-swarm.yaml Field Reference

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this swarm config file (e.g. `"2.0.0"`). |
| `author` | `string` | ✅ | X handle prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `swarm` | `object` | ✅ | Swarm definition (see below). |

## swarm fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `string` | ✅ | Stable machine identifier used in `@grok spawn swarm:<id>` triggers. |
| `name` | `string` | ✅ | Human-readable swarm name shown in dashboards and logs. |
| `version` | `string` | ✅ | Semver of the swarm definition itself (independent of the file version). |
| `description` | `string` | — | One- or two-sentence summary of the swarm's purpose. |
| `members` | `object[]` | ✅ | Ordered list of agent members (see below). At least one required. |
| `coordinator` | `string` | ✅ | `agent_id` of the lead agent, or the literal `"none"` for peer swarms. |
| `communication` | `string` | ✅ | Message-passing mode: `direct`, `broadcast`, `pubsub`. |
| `consensus` | `string` | — | Decision rule when members disagree: `none`, `majority`, `unanimous`. Defaults to `none`. |
| `fallback` | `object` | — | Failure-handling policy (see below). |
| `metadata` | `object` | — | Free-form map of string, number, or array values for tags, owners, lineage. |

## members[] item fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `agent_id` | `string` | ✅ | Identifier of an agent defined in `grok-agent.yaml`. |
| `role` | `string` | ✅ | Swarm role: `leader`, `worker`, `specialist`, `observer`, `router`. |
| `priority` | `integer` | — | Tiebreaker weight (0–100) when electing a new coordinator. Defaults to `50`. |

## fallback fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `strategy` | `string` | ✅ | What to do when a member fails: `reassign`, `degrade`, `halt`, `retry`. |
| `reassign_to` | `string` | — | `agent_id` to take over when `strategy: reassign`. |
| `on_coordinator_loss` | `string` | — | Behaviour when the coordinator drops: `elect_highest_priority`, `halt`, `rotate`. |
| `max_retries` | `integer` | — | Maximum retry attempts before escalating. Defaults to `1`. |
