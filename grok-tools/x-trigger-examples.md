# grok-tools.yaml — X Trigger Examples

Drop any of these trigger comments into a GitHub issue, PR description, or commit message, then tag `@grok`.

---

## Trigger 1 — List all registered tools
```
@grok tools list
```
Prints a table of every tool in `.grok/grok-tools.yaml` with its category and description.

---

## Trigger 2 — Inspect a specific tool
```
@grok tools inspect read_file
```
Shows the full input/output schema, permission requirements, and rate-limit config for `read_file`.

---

## Trigger 3 — Validate tools registry
```
@grok tools validate
```
Runs JSON Schema validation against `.grok/grok-tools.yaml` and reports any structural errors or missing required fields.

---

## Trigger 4 — Show tools used by an agent
```
@grok tools used-by CodePartner
```
Lists all tools referenced by the `CodePartner` agent definition in `grok-agent.yaml` and confirms each tool is registered in `grok-tools.yaml`.
