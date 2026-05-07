# grok-swarm

**File:** `specs/grok-swarm.yaml`  
**Schema:** [`schemas/grok-swarm.schema.json`](../schemas/grok-swarm.schema.json)  
**Introduced:** grok-yaml-standards v2.0.0  
**Requires:** grok@4.20+

---

## Overview

`grok-swarm.yaml` defines a coordinated group of Grok 4.20 agents that share a task queue and execute in parallel. A coordinator agent distributes subtasks; specialist agents (researcher, logic, critic, etc.) process them concurrently up to `max_parallel_calls`.

Swarms are best used for:
- Deep research pipelines that benefit from parallel web + X search
- Tasks requiring cross-checking (logic agent verifies researcher output)
- High-throughput classification where `grok-4.20-fast` reduces latency and cost

---

## Modes

| Mode | Max Agents | Use When |
|------|-----------|----------|
| `realtime-multi-agent` | 16 | Interactive tasks requiring low-latency streaming responses |
| `high-effort-16` | 16 | Long-running research; ignores `agent_count`, always uses max agents |
| `single` | 1 | Single-agent fallback; swarm orchestration disabled |

---

## Agent Roles

| Role | Typical Model | Responsibility |
|------|--------------|----------------|
| `coordinator` | `grok-4.20-multi-agent` | Receives top-level task; dispatches subtasks to other agents |
| `researcher` | `grok-4.20` | Gathers information via `web_search` and `x_search` |
| `logic` | `grok-4.20` | Structured reasoning, code execution, fact-checking |
| `creative` | `grok-4.20` | Generates text, threads, or media drafts |
| `critic` | `grok-4.20-fast` | Reviews outputs; scores quality 1-10; flags issues |
| `moderator` | `grok-4.20-fast` | Applies safety and compliance checks |
| `custom` | any | User-defined role; set `system_prompt` explicitly |

---

## Swarm Tool Set

The following tools are available to swarm agents. Assign only what each role needs:

| Tool | Purpose |
|------|---------|
| `web_search` | Search the open web for current information |
| `x_search` | Search X (Twitter) posts and threads |
| `code_execution` | Run sandboxed Python/JS for computation and data processing |
| `image_generation` | Generate images via Grok image model |
| `voice_synthesis` | Synthesize audio (requires `grok-voice-tts-natural`) |

---

## State

| Field | Values | Default | Notes |
|-------|--------|---------|-------|
| `encrypted` | `true / false` | `true` | Always `true` in production |
| `persistence` | `session-only / long-term / none` | `session-only` | `long-term` writes to repo memory store |

---

## Orchestration

| Field | Range | Default | Notes |
|-------|-------|---------|-------|
| `timeout_seconds` | 1–3600 | 300 | Coordinator aborts all agents after this |
| `max_parallel_calls` | 1–16 | 4 | Reduce to lower API cost at the expense of speed |
| `retry_policy.max_attempts` | 1–10 | 3 | Per-agent call |
| `retry_policy.backoff` | `none / linear / exponential` | `exponential` | Exponential recommended |
| `retry_policy.delay_seconds` | 1–60 | 2 | Base delay for linear/exponential backoff |

---

## Minimal Example

```yaml
version: "2.0.0"
author: "@yourhandle"
compatibility:
  - "grok@4.20+"
  - "grok-yaml-standards@2.0+"

swarm:
  mode: "realtime-multi-agent"
  agent_count: 2
  agents:
    - role: "coordinator"
      model: "grok-4.20-multi-agent"
      tools: ["web_search"]
    - role: "critic"
      model: "grok-4.20-fast"
      system_prompt: "Review coordinator output and score accuracy 1-10."
  state:
    encrypted: true
    persistence: "session-only"
  orchestration:
    timeout_seconds: 120
    max_parallel_calls: 2
```

See [`specs/grok-swarm.yaml`](../specs/grok-swarm.yaml) for the full annotated reference.

---

## Cross-References

**Depends On:**
- [`grok-prompts.yaml`](../grok-prompts/schema.md) — `prompt_ref` keys must match entries in `prompt_library`
- [`grok-security.yaml`](../grok-security/schema.md) — swarm agents inherit the active `safety_profile`
- [`grok-tools.yaml`](../grok-tools/schema.md) — `tools` values must be registered in the tool registry

**Used By:**
- [`grok-workflow.yaml`](../grok-workflow/schema.md) — a workflow step can invoke a swarm via `action: "grok-swarm"`

**Grok 4.20 SDK Mapping:**

| YAML field | xAI SDK param |
|-----------|--------------|
| `mode` | `swarm_mode` |
| `agents[].model` | `model` per agent request |
| `orchestration.max_parallel_calls` | `max_concurrency` |
| `state.persistence` | `memory_scope` |
