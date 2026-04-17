# grok-analytics.yaml — Security Considerations

## 1. Opt-in by default, never opt-out by default
`enabled` defaults to `false`. Teams must explicitly set `enabled: true` and commit that change. This prevents silent data collection when the file is copied from a template.

## 2. Declare every event as PII-safe or not
Every event definition requires `pii_safe: true/false`. Events with `pii_safe: false` trigger a mandatory security review before being enabled. Never collect properties like `user_email`, `username`, or `commit_message` without explicit PII handling.

## 3. Store provider API keys in secrets, not YAML
Use `api_key_secret: "MY_SECRET_NAME"` referencing a repository secret. Never hardcode an analytics API key in the YAML file — it will be committed to version control and potentially exposed in public repositories.

## 4. Set a retention policy that matches your legal obligations
Different jurisdictions mandate different data retention limits. GDPR recommends no longer than necessary; many teams use 90 days. Set `data_retention_days` explicitly and configure the same limit in your provider's dashboard.

## 5. Exclude bots and CI from analytics
Add `"bot"` and your CI service account to `opt_out_roles`. Automated runs inflate event counts, skew performance metrics, and may inadvertently capture secrets present in CI environment variables if properties are logged naively.

---

## Threat Model

This spec defines opt-in telemetry collection and provider routing. The threats we defend against are:

**T1 — Credential Exposure**
Attack: An event property captures a request header that includes a bearer token, or a debug log line with an API key.
Defense: The analytics runtime scans every property value against known credential patterns before emission. Properties containing matches are dropped and flagged. Provider API keys themselves must use `api_key_secret:` references, never literals.

**T2 — Prompt Injection via Tool Output**
Attack: An event property's `text` field contains injected instructions; downstream dashboards that surface it via Grok summaries get hijacked.
Defense: User-generated content fields are emitted wrapped in XML delimiters so downstream prompts treat them as data.

**T3 — Path Traversal in Filesystem Tools**
Attack: A file-based event logger writes to an attacker-controlled path.
Defense: File-based emitters are sandboxed to the analytics output directory; paths validated against `^(?!.*\.\.)[^/].*$`.

**T4 — Over-Permissioned Actions**
Attack: Analytics is enabled by default in a forked template, silently exfiltrating data.
Defense: `enabled` defaults to `false`. A project must explicitly opt in via commit, making the choice auditable in git history.

**T5 — Rate Limit Abuse**
Attack: A buggy emitter fires events in a loop, racking up provider costs and flooding the backend.
Defense: Per-event `max_events_per_minute` and global `max_events_per_hour` caps. Overages are dropped with a warning.

**T6 — Supply Chain via Remote Tool Import**
Attack: A custom analytics provider library is loaded from a compromised URL.
Defense: Provider libraries must be whitelisted in `grok-security.yaml`.

### Out of Scope for This Spec

- Vulnerabilities in the xAI API or the Grok model itself — report to xAI's security team.
- X platform vulnerabilities — report to X's security team.
- Host OS, container runtime, or network security — handled by the deployment platform.

### Reporting Security Issues

See the repository [`SECURITY.md`](../SECURITY.md). Never file a public issue for a suspected vulnerability; use a private GitHub Security Advisory or the email listed in `SECURITY.md`.
