# grok-test.yaml

**What problem it solves**  
AI-powered testing on demand.

---

## Cross-References

### Depends On
- **grok-config.yaml**: `default_model` and `temperature` provide defaults; per-suite `temperature` overrides them.
- **grok-security.yaml**: `block_merge_on_fail` integrates with `auto_block_prs`.

### Used By
- **grok-workflow.yaml**: `steps[].action: grok-test` runs named suites.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `prompt` | `messages[{role:"user", content:"..."}]` |
| `temperature` | `temperature` (low values 0.1–0.3 for deterministic review) |
| `model` (from grok-config) | `model` |
| `files[]` | Context files prepended to the prompt |

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| `temperature` | `temperature=` |
| `model` (from grok-config) | `model="xai/grok-4"` |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| `prompt` | `KernelFunction` prompt template |
| `temperature` | `OpenAIPromptExecutionSettings.Temperature` |
| `categories[]` | Semantic routing tags for kernel function selection |
