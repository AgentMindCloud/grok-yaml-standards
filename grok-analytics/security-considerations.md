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
