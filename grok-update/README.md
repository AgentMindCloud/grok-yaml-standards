# grok-update.yaml

**What problem it solves**  
Keeps your repo fresh automatically.

---

## Cross-References

### Depends On
- **grok-config.yaml**: model and language defaults drive content generation quality.
- **grok-docs.yaml**: `regenerate_docs` action references doc target names defined there.

### Used By
- **grok-workflow.yaml**: `steps[].action: grok-update` references update job names.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `sources[]` | Files read and provided as context in the prompt |
| `actions[]` | Maps to tool calls sent in the completion request |
| `frequency` / `schedule_cron` | Scheduler config — not an SDK param |

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| `actions[]` | `tools=` list when the update invokes tool calls |
| `model` (from grok-config) | `model="xai/grok-4"` |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| `actions[]` | `KernelFunction` invocations in a pipeline |
| `sources[]` | `TextChunker` input files for memory ingestion |
