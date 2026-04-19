# grok-swarm.yaml — X Trigger Examples

Drop any of these trigger comments into a GitHub issue, PR description, or commit message, then tag `@grok`.

---

## Trigger 1 — Spawn a named swarm
```
@grok spawn swarm:ShipItSwarm
```
Reads `.grok/grok-swarm.yaml`, starts every member agent, wires up coordinator and communication mode, and reports the active member list.

---

## Trigger 2 — Show swarm status
```
@grok swarm status ShipItSwarm
```
Prints active members, current coordinator, last consensus decision, and any members in `fallback` state.

---

## Trigger 3 — List all defined swarms
```
@grok swarm list
```
Enumerates every `swarm.id` declared across the repo's `.grok/grok-swarm.yaml` (and future multi-swarm files) with their member counts.

---

## Trigger 4 — Disband a running swarm
```
@grok swarm stop ShipItSwarm
```
Gracefully shuts down every member, flushes pending pubsub topics, and writes a final run summary.

---

## Trigger 5 — Re-elect coordinator
```
@grok swarm reelect ShipItSwarm
```
Forces a coordinator re-election using the `priority` field. Useful when the current coordinator is unresponsive but has not formally failed.
