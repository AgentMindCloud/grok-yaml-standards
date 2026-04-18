# grok-prompts.yaml

**What problem it solves**  
Reusable, versioned prompt library anyone can call on X.

**X Trigger Example**  
`@grok use prompts:marketing_post`

**Benefits**  
Instant creativity without rewriting prompts every time.

---

## Cross-References

### Depends On
- **grok-config.yaml**: `temperature`, `max_tokens`, and `default_model` are overridden per-prompt; the global values serve as fallbacks.

### Used By
- **grok-agent.yaml**: `system_prompt` field mirrors the static layer of a prompt entry.
- **grok-workflow.yaml**: `steps[].template` references `prompt_library` keys.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `template` | `messages[{role:"user", content:"..."}]` with variables substituted |
| `system_prompt` | `messages[{role:"system", content:"..."}]` |
| `reasoning_mode` | `reasoning_effort` ("off"→none / "low"/"high"/"max") |
| `response_format` | `response_format` object (`text` / `json_object` / `json_schema`) |
| `temperature` | `temperature` |
| `max_tokens` | `max_tokens` |
| `model` | `model` |

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| `model` | `model="xai/grok-4"` (or variant) |
| `temperature` | `temperature=` |
| `max_tokens` | `max_tokens=` |
| `response_format` | `response_format={"type":"json_object"}` |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| `template` | `KernelFunction` prompt template string |
| `variables[]` | `KernelArguments` keys |
| `system_prompt` | system message in `ChatHistory` |
| `reasoning_mode` | `OpenAIPromptExecutionSettings` extended thinking |
| `output_format` | `OpenAIPromptExecutionSettings.ResponseFormat` |
