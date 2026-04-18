# grok-agent.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-agent.json`

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the config owner, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `agents` | object | ✅ | — | minProperties: 1 | Named agent definitions. Each key is an agent ID used in `@grok spawn agent:<Name>`. |

---

## Agent Definition Object

### Example

```yaml
agents:
  CodePartner:
    description: "Senior engineer agent with full read-write access to the repo."
    tools:
      - read_file
      - write_file
      - run_command    # high-risk: pairs with rate_limit below
      - search_code
      - create_pr
    memory: "long_term"
    max_turns_per_session: 100
    auto_save_state: true
    personality: "technical"
    system_prompt: "You are a senior TypeScript engineer. Always explain trade-offs."
    permissions: ["read", "write", "execute"]
    rate_limit:
      requests_per_minute: 60
      requests_per_day: 1000
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `description` | string | ✅ | — | minLength: 10; maxLength: 500 | Purpose and domain expertise of this agent. |
| `tools` | string[] | — | `[]` | uniqueItems; each item: enum of registered tool IDs | Tool identifiers the agent may invoke. Cross-reference with `grok-tools.yaml`. |
| `memory` | string | — | `"session_only"` | enum: `long_term`, `session_only`, `none` | Memory persistence across sessions. |
| `max_turns_per_session` | integer | — | `50` | minimum: 1; maximum: 1000 | Back-and-forth turns before the agent requires re-spawning. |
| `auto_save_state` | boolean | — | `false` | — | Persist agent state after every session. Only meaningful when `memory: long_term`. |
| `personality` | string | — | — | enum: `helpful-maximalist`, `concise`, `creative`, `technical`, `balanced`, `socratic`, `executive` | Agent-level personality. Overrides `grok.personality` from `grok-config.yaml`. |
| `system_prompt` | string | — | — | minLength: 10; maxLength: 4000 | Static system prompt prepended to every session. Never interpolate user input here. |
| `permissions` | string[] | — | `[]` | uniqueItems; enum items: `read`, `write`, `execute`, `network`, `publish`, `deploy`, `admin` | Explicit capability grants beyond default read access. |
| `rate_limit` | object | — | — | — | Per-agent request throttling. See [Rate Limit Object](#rate-limit-object). |
| `enabled` | boolean | — | `true` | — | Set `false` to disable the agent without removing its definition. |

---

## Rate Limit Object

### Example

```yaml
agents:
  SocialManager:
    rate_limit:
      requests_per_minute: 10   # prevents accidental X spam in loops
      requests_per_day: 200
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `requests_per_minute` | integer | — | — | minimum: 1; maximum: 600 | Maximum tool invocations per 60-second window across all tools. |
| `requests_per_day` | integer | — | — | minimum: 1; maximum: 100000 | Maximum total tool invocations per calendar day. |

---

## Tool Identifiers

The following tools are defined in `grok-tools.yaml` v1.2.0 and available for agent assignment:

| Tool | Category | Key Security Constraint |
|------|----------|------------------------|
| `read_file` | filesystem | path traversal regex enforced |
| `write_file` | filesystem | `overwrite: false` by default |
| `list_directory` | filesystem | scoped to repo root |
| `search_code` | filesystem | read-only |
| `run_command` | shell | requires `safety_profile: balanced` or `research` + explicit `shell_access: true` |
| `post_thread` | x_platform | `approval_required: true`; 20/day cap |
| `reply_to_mentions` | x_platform | `approval_required: true`; 50/day cap |
| `search_x` | x_platform | read-only; `no_bulk_collection: true` |
| `analyze_engagement` | x_platform | `own_tweets_only: true` |
| `create_pr` | github | `draft_default: true` |
| `fetch_repo` | github | read-only |
| `web_search` | web | uses Grok built-in |
| `fetch_url` | web | HTTPS only; SSRF protection |
| `save_memory` | memory | `no_sensitive_data_warning: true` |
| `recall_memory` | memory | agent-scoped |
| `summarize_changes` | workflow | pure transform |
| `publish_thread` | workflow | delegates to `summarize_changes` + `post_thread` |

---

## memory Enum

| Value | Behaviour |
|-------|-----------|
| `long_term` | State persists across sessions on disk. Requires `auto_save_state: true` to write. |
| `session_only` | State is cleared at the end of each session. Default. |
| `none` | No memory; each turn is fully stateless. |
