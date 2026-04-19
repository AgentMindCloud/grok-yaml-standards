# grok-swarm.yaml — Use Cases

## 1. Release swarm — PR → tests → docs → release notes → X announcement
A `ShipItSwarm` with `CodePartner` (leader), `TestRunner`, `DocsWriter`, `ReleaseNotes`, and `SocialManager`. `consensus: majority` so three out of five must approve before the release proceeds. `fallback.strategy: reassign` moves DocsWriter's tasks to CodePartner if DocsWriter times out.

## 2. Customer-support triage swarm
Three specialist agents (`BillingBot`, `TechSupportBot`, `AccountBot`) coordinated by a `TriageRouter` with `communication: pubsub`. Each incoming ticket is published to the bus; the agent whose domain matches picks it up. `consensus: none` — no voting needed, each agent owns its lane.

## 3. Research sweep swarm
Five `WebResearcher` instances run in parallel over distinct sub-queries. `communication: broadcast` so intermediate findings are shared across the swarm, reducing duplicate work. `consensus: unanimous` on the final summary ensures no single researcher's bias dominates.

## 4. Red-team / blue-team security drill
`RedTeamAgent` and `BlueTeamAgent` as peers with `coordinator: "none"`. `communication: direct` so the two exchange probe-and-defend messages without leaking to observers. Results feed into `grok-security.yaml` findings at session end.

## 5. Incident-response swarm
`OnCallEngineer` (leader), `PagerBot`, `RunbookExecutor`, and `PostmortemDrafter`. On `fallback.on_coordinator_loss: elect_highest_priority`, a secondary engineer is auto-promoted. `metadata.owner_team` and `metadata.sev` fields drive routing in `grok-analytics.yaml`.
