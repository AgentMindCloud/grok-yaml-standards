# grok-deploy.yaml — Security Considerations

## 1. Never hardcode secrets in YAML
Always use `source: secret` with a `secret_key` reference. The `source: literal` option is for non-sensitive config only (e.g. `NODE_ENV`). Secrets must live in repository secrets or a vault — never in version-controlled YAML.

## 2. Require approval for production targets
Set `require_approval: true` on every production-grade target. Pair it with `approval_from` to restrict who can unblock a deploy. This prevents a compromised PR from deploying malicious code to production via a crafted @grok comment.

## 3. Scope `enabled` to reduce attack surface
If a target is not in active use (e.g. a deprecated region), set `enabled: false`. Disabled targets cannot be triggered even if a valid @grok comment is posted.

## 4. Resource limits as a cost control and DoS mitigation
`max_instances` and `memory_mb` caps prevent runaway scaling attacks. An adversary who can trigger a deploy cannot use it to rack up unlimited cloud costs when limits are in place.

## 5. Audit deploy history via notifications
Enable `notify_on_success: true` and `notify_on_failure: true` on production targets. Unexpected success notifications (a deploy you didn't initiate) are an early warning sign of a compromised trigger.

---

## Threat Model

This spec defines deployment targets and their approval gates. The threats we defend against are:

**T1 — Credential Exposure**
Attack: A contributor sets `source: literal` with a production database URL containing embedded credentials.
Defense: The JSON Schema rejects strings matching known credential patterns in `source: literal` fields. `source: secret` with `secret_key` references is the only supported path for sensitive values.

**T2 — Prompt Injection via Tool Output**
Attack: A deploy notification is composed from external status output containing injected instructions.
Defense: Deploy status text is wrapped in XML delimiters before being used in any downstream prompt; delegate tools treat it as data.

**T3 — Path Traversal in Filesystem Tools**
Attack: A deploy artifact path points outside the build directory.
Defense: Artifact paths validated against `^(?!.*\.\.)[^/].*$`; the runtime refuses to upload files outside the build root.

**T4 — Over-Permissioned Actions**
Attack: A deploy is triggered via `@grok deploy production` in a PR comment without approval.
Defense: Every production target requires `require_approval: true` + `approval_from:` allowlist. The runtime rejects any deploy that reaches a production target without a signed approval.

**T5 — Rate Limit Abuse**
Attack: A loop in a failing deploy retries indefinitely, hammering the cloud provider's API.
Defense: Per-target `max_concurrent` and global `max_deploys_per_hour` caps. Failed deploys apply exponential backoff.

**T6 — Supply Chain via Remote Tool Import**
Attack: A deploy imports a container image from an unverified registry.
Defense: Container registries must be whitelisted in `grok-security.yaml`. Image digests (not tags) are required for production targets.

### Out of Scope for This Spec

- Vulnerabilities in the xAI API or the Grok model itself — report to xAI's security team.
- X platform vulnerabilities — report to X's security team.
- Host OS, container runtime, or network security — handled by the deployment platform.

### Reporting Security Issues

See the repository [`SECURITY.md`](../SECURITY.md). Never file a public issue for a suspected vulnerability; use a private GitHub Security Advisory or the email listed in `SECURITY.md`.
