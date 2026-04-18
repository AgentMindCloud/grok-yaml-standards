# grok-docs.yaml

**What problem it solves**  
Auto-generated, always-up-to-date docs.

---

## Cross-References

### Depends On
- **grok-config.yaml**: global model and language defaults drive generation quality and locale.
- **grok-update.yaml**: `regenerate_docs` action in update jobs calls docs targets by name.

### Used By
- **grok-workflow.yaml**: `steps[].action: grok-docs` references target names.
- **grok-update.yaml**: `actions: [regenerate_docs]` triggers doc regeneration.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `sections[]` | Drives the structured prompt sent to the model. |
| `style` | Injected as a system-level style instruction. |
| `max_length_words` | Approximate `max_tokens` budget. |
| `language` | Language constraint in system message. |

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| `max_length_words` | approximate `max_tokens=` |
| `language` | system message instruction |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| `sections[]` | `KernelFunction` prompt template sections |
| `style` | `OpenAIPromptExecutionSettings.ChatSystemPrompt` prefix |
