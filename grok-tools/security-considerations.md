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

---

## Threat Model

This spec defines the canonical tool registry — every tool agents and workflows may invoke. The threats we defend against are:

**T1 — Credential Exposure**
Attack: A contributor adds a hardcoded API key (e.g. `xai-...`) inside a tool's default value. Once merged, the key is scraped.
Defense: The JSON Schema rejects strings matching `/^xai-[a-zA-Z0-9]{32,}$/` outside env-reference fields. `requires_auth: true` signals a credential is needed — the credential itself lives in repo secrets, never here.

**T2 — Prompt Injection via Tool Output**
Attack: A web-returning tool (`fetch_url`, `search_x`) returns adversarial text that hijacks the calling agent.
Defense: Every tool in this registry is expected to return its output wrapped in XML delimiters at the runtime layer. The tool's `returns:` contract describes the structured shape, not the untrusted text. Callers are instructed (via system prompt) to treat returned content as data.

**T3 — Path Traversal in Filesystem Tools**
Attack: A filesystem tool receives `"../../etc/passwd"` as a path parameter.
Defense: Every filesystem tool declares `path_traversal_regex: "^(?!.*\\.\\.)[^/].*$"` and the runtime enforces it before invocation. See `read_file`, `write_file`, `list_directory`.

**T4 — Over-Permissioned Actions**
Attack: A tool is registered with scopes broader than necessary (e.g. X `tweet.write` when only `tweet.read` is used).
Defense: Every tool declares the minimum scopes in its `security:` block. `post_thread` is the only x_platform write tool; agents that should not post must omit it from their `tools:` list.

**T5 — Rate Limit Abuse**
Attack: A runaway loop calls `post_thread` until the X daily cap is reached.
Defense: Every rate-limited tool declares a `rate_limit` block. `post_thread` caps at 20/day per the X Developer Agreement; `reply_to_mentions` at 50/day. Runtime enforces with a token bucket.

**T6 — Supply Chain via Remote Tool Import**
Attack: A workflow imports a tool definition from a user-supplied URL that points to a malicious registry.
Defense: The registry in `.grok/grok-tools.yaml` is the only trusted source. External URLs must be whitelisted in `grok-security.yaml`. Dynamic loading from user-controlled URLs is rejected at validation time.

### Out of Scope for This Spec

- Vulnerabilities in the xAI API or the Grok model itself — report to xAI's security team.
- X platform vulnerabilities — report to X's security team.
- Host OS, container runtime, or network security — handled by the deployment platform.

### Reporting Security Issues

See the repository [`SECURITY.md`](../SECURITY.md). Never file a public issue for a suspected vulnerability; use a private GitHub Security Advisory or the email listed in `SECURITY.md`.
