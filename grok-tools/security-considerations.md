# grok-tools.yaml — Security Considerations

## 1. Principle of least privilege
Only register tools an agent genuinely needs. A docs-generation agent has no reason to hold `deploy` or `admin` permission — keep the `permissions` array minimal per tool and let each agent declare only the subset it requires.

## 2. Treat `run_command` as a high-risk tool
`run_command` with unrestricted input is equivalent to arbitrary code execution. Always set a `timeout_seconds`, restrict it to specific agents via `grok-agent.yaml`, and never grant it to untrusted or community-contributed agent definitions.

## 3. Store auth credentials in secrets, not YAML
`requires_auth: true` tells Grok a credential is needed — it does not store the credential. Use repository secrets (GitHub Actions secrets, `.env` files listed in `grok-config.yaml` `privacy.never_share`) to supply tokens at runtime.

## 4. Rate limits are a safety net, not a firewall
`rate_limit` throttles honest automation but does not stop a compromised agent. Pair rate limits with monitoring via `grok-analytics.yaml` to detect abnormal invocation patterns.

## 5. Validate inputs at the tool boundary
JSON Schema constraints (`enum`, `maxLength`, `pattern`) on tool inputs prevent prompt injection via malformed parameters. Always add `maxLength` to string inputs that flow into shell commands or API calls.
