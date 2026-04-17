# grok-tools.yaml — Use Cases

## 1. Unified tool contract for agents and workflows
Define `read_file`, `write_file`, and `run_command` once in `grok-tools.yaml`. Every agent in `grok-agent.yaml` and every workflow step in `grok-workflow.yaml` references the same contract. When a tool's signature changes, you update one file.

## 2. Permission-gated tool access
A social-media agent gets `post_thread` and `analyze_engagement` but not `run_command` or `deploy`. The tools registry enforces this via `permissions` arrays — Grok refuses to use a tool an agent wasn't granted.

## 3. Rate-limit protection for expensive APIs
A `web_search` tool configured with `requests_per_minute: 20` prevents a runaway agent loop from exhausting a paid search API quota overnight.

## 4. IDE autocomplete and schema validation
Because every input and output is fully typed, editors that understand JSON Schema (VS Code, JetBrains) can autocomplete tool names and parameter values directly inside `grok-agent.yaml` and `grok-workflow.yaml`.

## 5. Custom tool extensions
Add your own tools alongside the built-ins — for example a `call_stripe_api` tool with inputs `{endpoint, payload}` and outputs `{response, status_code}`. Teams can publish shared tool registries as npm or PyPI packages and compose them via `compatibility` entries.
