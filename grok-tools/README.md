# grok-tools.yaml

**What problem it solves**  
Agents and workflows reference tools by name but have no formal contract for what those tools accept, return, or require. `grok-tools.yaml` is the dedicated tools registry that gives every tool a full typed signature — inputs, outputs, permissions, and rate limits — so Grok can invoke them safely and editors can autocomplete them.

**X Trigger Example**  
`@grok tools list` — prints all registered tools with descriptions  
`@grok tools inspect read_file` — shows the full schema for a specific tool

**Compatible with**  
`grok-install.yaml@1.0+` · `grok@2026.4+` · `grok-yaml-standards@1.2+`

**Benefits**  
- Single source of truth for every tool used across `grok-agent.yaml` and `grok-workflow.yaml`  
- Full input/output schemas enable IDE autocomplete and runtime validation  
- Permission model prevents agents from silently acquiring capabilities they weren't granted  
- Rate-limit declarations protect APIs from runaway automation

---

## Cross-References

### Depends On
- **grok-config.yaml**: `safety_profile` determines which tool categories are available.
- **grok-security.yaml**: `shell` category tools require `safety_profile: balanced` or higher.

### Used By
- **grok-agent.yaml**: `tools[]` array items must be keys in this registry.
- **grok-workflow.yaml**: `steps[].action` tool IDs resolve against this registry.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `parameters` (JSON Schema) | `tools[].function.parameters` in the API request |
| `returns` (JSON Schema) | Shape of the parsed tool response |
| `errors[].code` | Error discriminant in tool response handling |
| `security.rate_limit` | Client-side throttling before tool calls |
| `category: x_platform` | Requires `tools[].function` with X OAuth header |

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| `parameters` | `tools=[{"type":"function","function":{"parameters":{...}}}]` |
| `description` | `tools[].function.description` |
| `errors[].code` | Exception handling in `litellm.completion` callback |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| Tool definition | `KernelFunction` decorated with `@kernel_function` |
| `parameters` | `KernelFunctionMetadata` parameter descriptors |
| `returns` | `KernelFunctionMetadata` return type |
| `security.read_only` | `KernelPlugin` permission attribute |
| `category: memory` | `ISemanticTextMemory` plugin |
