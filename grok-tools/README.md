# grok-tools.yaml

**What problem it solves**  
Agents and workflows reference tools by name but have no formal contract for what those tools accept, return, or require. `grok-tools.yaml` is the dedicated tools registry that gives every tool a full typed signature — inputs, outputs, permissions, and rate limits — so Grok can invoke them safely and editors can autocomplete them.

**X Trigger Example**  
`@grok tools list` — prints all registered tools with descriptions  
`@grok tools inspect read_file` — shows the full schema for a specific tool

**Compatible with**  
`grok-install.yaml@1.0+` · `grok@2026.4+` · `grok-yaml-standards@2.0+`

**Benefits**  
- Single source of truth for every tool used across `grok-agent.yaml` and `grok-workflow.yaml`  
- Full input/output schemas enable IDE autocomplete and runtime validation  
- Permission model prevents agents from silently acquiring capabilities they weren't granted  
- Rate-limit declarations protect APIs from runaway automation
