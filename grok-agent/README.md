# grok-agent.yaml

**What problem it solves**  
Turns any repo into a stateful Grok agent.

**X Trigger Example**  
`@grok spawn agent`

**Benefits**  
Long-running, memory-aware automation.

---

## Cross-References

### Depends On
- **grok-config.yaml**: global model, temperature, and personality defaults apply before per-agent overrides.
- **grok-tools.yaml**: every string in `tools[]` must be a registered key in the tool registry.
- **grok-security.yaml**: `safety_profile` must align with the declared security policy.
- **grok-prompts.yaml**: `system_prompt` field mirrors the static layer of a prompt entry.

### Used By
- **grok-workflow.yaml**: `steps[].action: grok-agent` spawns agents by name.
- **grok-install.yaml**: `intelligence_layer` block controls which agents are activated.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `description` | agent persona in `messages[{role:"system"}]` |
| `tools[]` | `tools` array in `CreateChatCompletionRequest` |
| `model_override` | `model` parameter |
| `max_turns_per_session` | session loop iteration limit |
| `memory: long_term` | persistent context via RAG + embeddings |
| `system_prompt` | `messages[{role:"system", content:"..."}]` |
| `temperature` (via grok-config) | `temperature` |

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
