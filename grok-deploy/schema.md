# grok-deploy.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-deploy.json`

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the config owner, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `deploy` | object | ✅ | — | — | Top-level deploy block containing `targets`. |

---

## Deploy Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `targets` | object | ✅ | — | minProperties: 1 | Map of target names to target definitions. Invoke with `@grok deploy <name>`. |

---

## Target Object

### Example

```yaml
deploy:
  targets:
    production:
      provider: "vercel"
      branch: "main"
      require_approval: true           # always for production
      approval_from: ["@JanSol0s"]
      rollback_on_unhealthy: true
      notify_on_success: true
      notify_on_failure: true
      env_vars:
        - name: "DATABASE_URL"
          source: "secret"             # never use 'literal' for sensitive values
          secret_key: "PROD_DB_URL"
          required: true
      resource_limits:
        memory_mb: 512
        max_instances: 10
      health_check:
        path: "/health"
        interval_seconds: 30
        timeout_seconds: 5
        unhealthy_threshold: 3
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `provider` | string | ✅ | — | enum: `vercel`, `aws`, `gcp`, `azure`, `fly`, `railway`, `render`, `heroku`, `docker`, `k8s`, `custom` | Hosting provider. |
| `branch` | string | ✅ | — | pattern: `^[a-zA-Z0-9/_.-]+$` | Git branch to deploy from. |
| `require_approval` | boolean | — | `true` | — | Require a human approval before deploying. Always `true` for production. |
| `approval_from` | string[] | — | `[]` | each pattern: `^@[A-Za-z0-9_]{1,50}$` | X handles whose approval comment unblocks the deploy. |
| `build_command` | string | — | — | maxLength: 500 | Build command to run before deploy (e.g. `"npm run build"`). |
| `env_vars` | object[] | — | `[]` | — | Environment variables injected at deploy time. See [Env Var Object](#env-var-object). |
| `resource_limits` | object | — | — | — | Cloud resource caps. See [Resource Limits Object](#resource-limits-object). |
| `health_check` | object | — | — | — | Post-deploy liveness probe. See [Health Check Object](#health-check-object). |
| `rollback_on_unhealthy` | boolean | — | `false` | — | Auto-rollback to previous deploy if health check fails. |
| `notify_on_success` | boolean | — | `false` | — | Post notification on successful deploy. |
| `notify_on_failure` | boolean | — | `true` | — | Post notification on failed deploy. |
| `notify_on_x` | boolean | — | `false` | — | Post deploy result as an X thread. Requires approval. |
| `enabled` | boolean | — | `true` | — | Set `false` to disable target without removing its definition. |

---

## Env Var Object

### Example

```yaml
env_vars:
  - name: "API_KEY"
    source: "secret"         # use 'secret' for all sensitive values
    secret_key: "PROD_API_KEY"
    required: true
  - name: "NODE_ENV"
    source: "literal"        # 'literal' is safe only for non-sensitive config
    value: "production"
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `name` | string | ✅ | — | pattern: `^[A-Z][A-Z0-9_]{0,99}$` | Environment variable name (UPPER_SNAKE_CASE). |
| `source` | string | ✅ | — | enum: `secret`, `literal`, `env` | How to resolve the value. Use `secret` for all sensitive data. |
| `secret_key` | string | — | — | required when `source: secret` | Repository secret identifier (e.g. `PROD_DB_URL`). |
| `value` | string | — | — | required when `source: literal`; never for secrets | Hardcoded value. Safe only for non-sensitive config like `NODE_ENV`. |
| `required` | boolean | — | `true` | — | Fail the deploy if this variable cannot be resolved. |

---

## Resource Limits Object

### Example

```yaml
resource_limits:
  memory_mb: 512         # cap prevents runaway memory costs
  cpu_cores: 1.0
  timeout_seconds: 30
  max_instances: 5       # hard ceiling prevents scaling DoS
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `memory_mb` | integer | — | — | minimum: 128; maximum: 65536 | Maximum memory in MB. |
| `cpu_cores` | number | — | — | minimum: 0.1; maximum: 64 | vCPU allocation (fractional values e.g. `0.5` are valid). |
| `timeout_seconds` | integer | — | — | minimum: 1; maximum: 3600 | Request or function timeout in seconds. |
| `max_instances` | integer | — | `1` | minimum: 1; maximum: 100 | Maximum concurrent service instances. Cap limits scaling cost. |

---

## Health Check Object

### Example

```yaml
health_check:
  path: "/health"
  interval_seconds: 30
  timeout_seconds: 5
  healthy_threshold: 2
  unhealthy_threshold: 3   # declare unhealthy after 3 consecutive failures
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `path` | string | — | `"/health"` | must start with `/` | HTTP path polled after deploy. |
| `interval_seconds` | integer | — | `30` | minimum: 5; maximum: 300 | How often the endpoint is polled. |
| `timeout_seconds` | integer | — | `5` | minimum: 1; maximum: 60 | Seconds before a poll attempt is considered failed. |
| `healthy_threshold` | integer | — | `2` | minimum: 1; maximum: 10 | Consecutive successes needed to declare healthy. |
| `unhealthy_threshold` | integer | — | `3` | minimum: 1; maximum: 10 | Consecutive failures needed to trigger rollback (if enabled). |
