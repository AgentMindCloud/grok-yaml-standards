# grok-analytics.yaml Field Reference

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this analytics config (e.g. `"1.0.0"`). |
| `author` | `string` | ✅ | X handle prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `analytics` | `object` | ✅ | Analytics configuration block. |

## analytics fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `enabled` | `boolean` | ✅ | Master switch — no data is sent unless `true`. Defaults to `false`. |
| `provider` | `string` | ✅ | Analytics backend: `posthog`, `mixpanel`, `amplitude`, `segment`, `datadog`, `custom`. |
| `provider_config` | `object` | — | Provider-specific settings (API key secret reference, host URL). |
| `events` | `object[]` | — | List of event definitions (see below). |
| `sampling_rate` | `number` | — | Fraction of events to capture (0.0–1.0). `1.0` = 100%. Defaults to `1.0`. |
| `anonymize_user_ids` | `boolean` | — | Hash user identifiers before sending. Defaults to `true`. |
| `data_retention_days` | `integer` | — | Days the provider retains event data (1–730). |
| `opt_out_roles` | `string[]` | — | User roles excluded from tracking (e.g. `["guest", "bot"]`). |

## provider_config fields

| Field | Type | Description |
|-------|------|-------------|
| `api_key_secret` | `string` | Repository secret key holding the provider API key. |
| `host` | `string` | Self-hosted provider endpoint URL. Only used for self-hosted deployments. |
| `project_id` | `string` | Provider project or workspace identifier. |

## Event definition fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `string` | ✅ | Event name in snake_case (e.g. `grok_invoked`). |
| `description` | `string` | — | When and why this event fires. |
| `properties` | `string[]` | — | List of property names collected with this event. |
| `pii_safe` | `boolean` | ✅ | `true` if no property contains personally identifiable information. |
| `enabled` | `boolean` | — | Set to `false` to stop collecting this event without removing it. Defaults to `true`. |
