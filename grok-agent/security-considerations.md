# grok-agent.yaml — Security Considerations

## 1. Apply the principle of least privilege to every agent's tools list

Only list tools an agent genuinely needs to perform its defined purpose. A docs-generation agent has no reason to hold `deploy` or `write_database` permission. Each additional tool in the list is an additional attack surface — a compromised or misbehaving agent can only cause harm within the scope of its granted tools.

## 2. Treat `run_command` as a high-risk tool requiring explicit justification

`run_command` with unconstrained input is equivalent to arbitrary code execution on the host environment. If an agent must have it, pair it with a `rate_limit`, set a short `timeout_seconds` in `grok-tools.yaml`, and limit the agent's `permissions` to exclude `network` and `deploy`. Never grant `run_command` to agents that accept any form of user-supplied input.

## 3. Audit what `long_term` memory stores and persists

An agent with `memory: long_term` and `auto_save_state: true` writes its working memory to disk after every session. If that memory includes secrets, PII, or internal URLs encountered during a session, they will persist indefinitely. Periodically review stored agent state, and ensure the storage location is excluded from version control and any public artifact uploads.

## 4. Use `rate_limit` to prevent runaway automation loops

An agent in an automated pipeline that hits an unexpected error can retry indefinitely, exhausting API quotas or triggering rate-limit bans on downstream services. Set `rate_limit.requests_per_minute` and `rate_limit.requests_per_day` on every agent that interacts with external APIs to create a hard ceiling on runaway behaviour.

## 5. Never include user-controlled strings in `system_prompt`

The `system_prompt` field defines the agent's persona and operating rules. If you dynamically construct a system prompt by interpolating user input (e.g. a GitHub issue title), an attacker can override the agent's rules with a crafted input. Treat `system_prompt` as a static, developer-controlled string that is never modified at runtime.
