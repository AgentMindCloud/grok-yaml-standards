# grok-workflow.yaml

**What problem it solves**  
Multi-step automation without leaving X.

**X Trigger Example**  
`@grok run workflow`

**Benefits**  
One-click complex processes.

---

## Cross-References

### Depends On
- **grok-config.yaml**: global model and defaults apply to all LLM-driven steps.
- **grok-agent.yaml**: agent names referenced in `steps[].action`.
- **grok-tools.yaml**: tool IDs used in `steps[].action` must exist in the registry.
- **grok-deploy.yaml**: deploy target names referenced in `steps[].action: grok-deploy`.
- **grok-test.yaml**: suite names referenced in `steps[].action: grok-test`.
- **grok-security.yaml**: scan names referenced in `steps[].action: grok-security`.
- **grok-docs.yaml**: target names referenced in `steps[].action: grok-docs`.
- **grok-prompts.yaml**: prompt keys referenced in `steps[].template`.
- **grok-analytics.yaml**: event emission wired to workflow completion events.

### Used By
- Nothing — grok-workflow is the top-level orchestrator. `grok-install.yaml` activates the workflow runtime.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `steps[].action` (spec name) | Resolved to a multi-turn `messages[]` sequence |
| `steps[].condition` | Evaluated against prior step outputs in the message context |
| `steps[].template` | `messages[{role:"user"}]` from `grok-prompts` library |
| `timeout_minutes` | Session-level deadline enforced by the runtime |
| `steps[].approval_required` | Pause point; human reply resumes the `messages[]` thread |

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| `model` (from grok-config) | `model="xai/grok-4"` for LLM-driven steps |
| `steps[].template` | `messages=` constructed from prompt template |
| `steps[].retry` | `num_retries=` in `litellm.completion` |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| `steps[]` sequence | `KernelFunction` pipeline (sequential planner) |
| `steps[].condition` | `KernelFunctionFilter` predicate |
| `steps[].approval_required` | `HumanInTheLoopFilter` pattern |
| `on_failure` | `KernelPlugin` exception handling strategy |
