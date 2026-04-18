# grok-config.yaml

**What problem it solves**  
Centralizes all Grok settings so every repo has consistent behavior.

**X Trigger Example**  
`@grok config` → Grok instantly respects this file.

**Benefits**  
- One source of truth for temperature, model, context  
- Forward-compatible with future Grok versions  
- Zero setup for X users

---

## Cross-References

### Depends On
- **grok-install.yaml**: installation must be present before config is applied.

### Used By
- **All 11 other specs**: every spec reads `grok-config.yaml` for global defaults before applying its own overrides. Conflicts resolve in favour of the more-specific spec.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `default_model` | `model` in `CreateChatCompletionRequest` |
| `temperature` | `temperature` |
| `max_tokens` | `max_tokens` |
| `stream_responses` | `stream=True` |
| `reasoning_depth` | `reasoning_effort` ("low"/"medium"/"high") |
| `response_language` | system message language instruction |

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| `default_model` | `model="xai/grok-4"` |
| `temperature` | `temperature=` |
| `max_tokens` | `max_tokens=` |
| `stream_responses` | `stream=True` |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| `default_model` | `OpenAIPromptExecutionSettings.ModelId` |
| `temperature` | `OpenAIPromptExecutionSettings.Temperature` |
| `max_tokens` | `OpenAIPromptExecutionSettings.MaxTokens` |
| `personality` | `OpenAIPromptExecutionSettings.ChatSystemPrompt` |
