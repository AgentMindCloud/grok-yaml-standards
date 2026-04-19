# grok-swarm.yaml — Security Considerations

## 1. A swarm inherits the union of its members' permissions
If any member agent in `grok-agent.yaml` has `permissions: ["write", "deploy"]`, the swarm as a whole can write and deploy. Review the permission surface of *every* `agent_id` before adding it to a swarm — never assume the coordinator's permissions are the ceiling.

## 2. Coordinator compromise = swarm compromise
A malicious or hallucinating coordinator can instruct workers to execute arbitrary tool calls within their grants. Require human approval for swarms that include agents with `deploy`, `admin`, or `publish` permissions. Treat `coordinator: "none"` peer swarms as safer for untrusted workloads.

## 3. `communication: broadcast` leaks context across members
In broadcast mode, every member sees every message. Do not include agents with low trust (e.g. community-contributed specialists) in broadcast swarms that also handle PII or secrets. Use `communication: direct` or `pubsub` with topic scoping when isolation matters.

## 4. Consensus rules do not enforce alignment — they enforce agreement
`consensus: majority` means three agreeing agents can still be wrong together. Consensus is a safety net against a single misaligned member, not a substitute for sandboxing, rate limits, or human review gates defined in `grok-agent.yaml`.

## 5. `fallback.reassign_to` must not escalate privileges
If the primary worker has `read` permission but the reassign target has `write`, a predictable failure pattern becomes a privilege-escalation primitive. Ensure reassignment targets have permissions equal to or lower than the agents they replace.
