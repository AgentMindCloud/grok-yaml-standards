# grok-tools.yaml Field Reference

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this tools registry file (e.g. `"1.0.0"`). |
| `author` | `string` | ✅ | X handle of the maintainer prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with (e.g. `grok-install.yaml@1.0+`). |
| `tools` | `object` | ✅ | Map of tool identifiers to tool definitions. |

## Tool definition fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | `string` | ✅ | One-sentence explanation of what the tool does. |
| `category` | `string` | ✅ | Category enum: `file_system`, `code`, `web`, `social`, `ai`, `data`, `notification`. |
| `inputs` | `object` | — | Map of parameter names to parameter schemas (see below). |
| `outputs` | `object` | — | Map of output field names to output schemas. |
| `permissions` | `string[]` | — | Required capability grants: `read`, `write`, `execute`, `network`, `publish`, `deploy`, `admin`. |
| `requires_auth` | `boolean` | — | Whether the tool requires OAuth or API-key authentication. Defaults to `false`. |
| `auth_provider` | `string` | — | Auth provider identifier when `requires_auth` is `true` (e.g. `github`, `x_oauth2`). |
| `rate_limit` | `object` | — | Optional throttling config (see below). |
| `enabled` | `boolean` | — | Set to `false` to disable this tool without removing its definition. Defaults to `true`. |

## Parameter schema fields (inputs / outputs)

| Field | Type | Description |
|-------|------|-------------|
| `type` | `string` | JSON Schema type: `string`, `integer`, `number`, `boolean`, `array`, `object`. |
| `description` | `string` | What this parameter means. |
| `required` | `boolean` | Whether this input must be provided by the caller. |
| `default` | any | Value used when the parameter is not supplied. |
| `enum` | `any[]` | Restricts the value to one of the listed options. |
| `format` | `string` | JSON Schema format hint (e.g. `date-time`, `email`, `uri`). |
| `minimum` / `maximum` | `number` | Numeric range constraints. |
| `minLength` / `maxLength` | `integer` | String length constraints. |
| `items` | `object` | Schema for array element type. |

## rate_limit fields

| Field | Type | Description |
|-------|------|-------------|
| `requests_per_minute` | `integer` | Hard cap on invocations per minute. |
| `requests_per_day` | `integer` | Hard cap on invocations per calendar day. |
