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

---

## Validation Examples

```yaml
# INVALID — missing required field
agents:
  MyAgent:
    tools: ["read_file"]
# Error: 'description' is required

# INVALID — tool name not matching pattern
agents:
  MyAgent:
    description: "Does something."
    tools: ["Unknown-Tool"]
# Error: tools[0] must match ^[a-z][a-z0-9_]*$

# VALID — minimal definition
agents:
  CodeHelper:
    description: "Assists with code review and refactoring tasks."
    tools: ["read_file", "search_code"]
    memory: "session_only"
```

---

## Security Notes

- **`system_prompt`**: Never interpolate user-controlled input — attacker-controlled PR descriptions can escape instruction boundaries (see AT1 in `security-considerations.md`).
- **`permissions`**: Least-privilege — only grant `execute` if the agent truly needs shell access; `publish` only if it must post to X.
- **`tools`**: Omit tools the agent doesn't need; tool scope is the primary blast-radius control for what damage a compromised prompt can cause.
- **`rate_limit`**: Always set for agents with `x_platform` tools (`post_thread`, `reply_to_mentions`) to prevent runaway posting loops.

---

## Cross-References

| Spec / SDK | Field | Relationship |
|------------|-------|--------------|
| `grok-tools.yaml` | `tools[]` items | Every string must be a key in the `grok-tools.yaml` registry. |
| `grok-config.yaml` | `grok.personality` | Overridden by agent-level `personality`. |
| `grok-workflow.yaml` | `steps[].action` | Workflow steps can invoke agents via the spec name `grok-agent`. |
| xAI SDK | `system_prompt` | Maps to `messages[{role: "system", content: "..."}]` in the chat completions request. |
| xAI SDK | `model_override` | Maps to `CreateChatCompletionRequest.model`. |

### Depends On
- **grok-config.yaml**: global model, temperature, and personality defaults apply before per-agent overrides.
- **grok-tools.yaml**: every string in `tools[]` must be a registered key in the tool registry.
- **grok-security.yaml**: `safety_profile` must align with the declared security policy.
- **grok-prompts.yaml**: `system_prompt` field mirrors the static layer of a prompt entry.

### Used By
- **grok-workflow.yaml**: `steps[].action: grok-agent` spawns agents by name.
- **grok-install.yaml**: `intelligence_layer` block controls which agents are activated.

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| `model_override` | `model="xai/grok-4"` (or variant) |
| `tools[]` | `tools=` list of function dicts |
| `temperature` (via grok-config) | `temperature=` |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| `tools[]` | `KernelPlugin` methods registered on the kernel |
| `memory` | `ISemanticTextMemory` / `VolatileMemoryStore` |
| `system_prompt` | system message in `ChatHistory` |
| `personality` | `OpenAIPromptExecutionSettings.ChatSystemPrompt` |
