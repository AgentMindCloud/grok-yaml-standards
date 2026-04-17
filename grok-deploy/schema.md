# grok-deploy.yaml Field Reference

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this deploy config (e.g. `"1.0.0"`). |
| `author` | `string` | ✅ | X handle prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `deploy` | `object` | ✅ | Top-level deploy config containing `targets`. |

## deploy fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `targets` | `object` | ✅ | Map of target names to target definitions. |

## Target definition fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `provider` | `string` | ✅ | Hosting provider: `vercel`, `aws`, `gcp`, `azure`, `fly`, `railway`, `render`, `heroku`, `docker`, `custom`. |
| `branch` | `string` | ✅ | Git branch to deploy from. |
| `require_approval` | `boolean` | — | Require a human approval comment before deploying. Defaults to `true` for production-like targets. |
| `approval_from` | `string[]` | — | X handles of users whose approval comment unblocks the deploy. |
| `env_vars` | `object[]` | — | Environment variables injected at deploy time (see below). |
| `resource_limits` | `object` | — | Cloud resource caps (see below). |
| `health_check` | `object` | — | Post-deploy liveness probe config (see below). |
| `rollback_on_unhealthy` | `boolean` | — | Auto-rollback to the previous deploy when health check fails. |
| `notify_on_success` | `boolean` | — | Post a notification on successful deploy. |
| `notify_on_failure` | `boolean` | — | Post a notification on failed deploy. |
| `notify_on_x` | `boolean` | — | Post the deploy result as an X tweet. |
| `enabled` | `boolean` | — | Defaults to `true`. Set to `false` to disable target. |

## env_vars item fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `string` | ✅ | Environment variable name (UPPER_SNAKE_CASE recommended). |
| `source` | `string` | ✅ | How to resolve the value: `secret` (from repository secrets), `literal` (hardcoded value), `env` (from CI environment). |
| `secret_key` | `string` | — | Secret identifier when `source: secret`. |
| `value` | `string` | — | Hardcoded value when `source: literal`. Never use for sensitive data. |
| `required` | `boolean` | — | Fail the deploy if this variable cannot be resolved. Defaults to `true`. |

## resource_limits fields

| Field | Type | Description |
|-------|------|-------------|
| `memory_mb` | `integer` | Maximum memory allocation in megabytes. |
| `cpu_cores` | `number` | vCPU allocation (supports fractional, e.g. `0.5`). |
| `timeout_seconds` | `integer` | Request/function timeout in seconds. |
| `max_instances` | `integer` | Maximum number of concurrent service instances. |

## health_check fields

| Field | Type | Description |
|-------|------|-------------|
| `path` | `string` | HTTP path polled after deploy (e.g. `/health`). |
| `interval_seconds` | `integer` | How often Grok polls the endpoint. |
| `timeout_seconds` | `integer` | Seconds before a poll attempt is considered failed. |
| `healthy_threshold` | `integer` | Consecutive successes needed to declare healthy. |
| `unhealthy_threshold` | `integer` | Consecutive failures needed to declare unhealthy. |
