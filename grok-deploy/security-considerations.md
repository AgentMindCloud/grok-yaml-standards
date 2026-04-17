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
