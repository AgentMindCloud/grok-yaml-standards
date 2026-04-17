# grok-tools.yaml Field Reference

Every tool in the registry is a **formal contract**: typed `parameters`, typed
`returns`, an explicit `errors` vocabulary, and a `security` block. Agents and
workflows reference tools by name; the contract here is the single source of
truth for I/O shape and safety constraints.

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this tool registry file (e.g. `"1.2.0"`). |
| `author` | `string` | ✅ | X handle of the maintainer, prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with (e.g. `grok-install.yaml@1.0+`). |
| `tools` | `object` | ✅ | Map of `tool_id` → tool definition. Keys match `^[a-z][a-z0-9_]{1,63}$`. |

## Tool definition fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `category` | `string` | ✅ | One of: `filesystem`, `shell`, `x_platform`, `github`, `web`, `memory`, `workflow`. |
| `description` | `string` | ✅ | One-sentence explanation of what the tool does (10–500 chars). |
| `parameters` | `object` | ✅ | JSON Schema fragment for the input. Must be `type: object` with `properties` and (optionally) `required`. |
| `returns` | `object` | ✅ | JSON Schema fragment for the success output. Must be `type: object`. |
| `errors` | `array` | — | Explicit error vocabulary. Each entry has `code` (UPPER_SNAKE_CASE) and `message`. |
| `security` | `object` | ✅ | Safety constraints. Keys vary by category; see below. |
| `enabled` | `boolean` | — | Set to `false` to disable the tool without deleting its definition. Defaults to `true`. |

## Category enum

| Value | Purpose |
|-------|---------|
| `filesystem` | Scoped I/O against the repository working tree (read, write, list, search). |
| `shell` | Arbitrary command execution. Always gated by `safety_profile` + explicit grant. |
| `x_platform` | Posting to or reading from X. Writes require human approval and daily caps. |
| `github` | GitHub API operations. Writes default to draft. |
| `web` | Outbound HTTP. HTTPS only; SSRF guards are mandatory. |
| `memory` | Agent-scoped persistent state. No sensitive data. |
| `workflow` | Composite transforms that orchestrate other tools. |

## Parameter / return fragment keys

Both `parameters` and `returns` accept a JSON Schema fragment:

| Field | Type | Description |
|-------|------|-------------|
| `type` | `string` | `string`, `integer`, `number`, `boolean`, `array`, `object`, `null`. |
| `description` | `string` | Human-readable explanation (max 500 chars). |
| `default` | any | Value used when the caller omits the parameter. |
| `enum` | `any[]` | Restricts value to the listed options. |
| `format` | `string` | `date-time`, `date`, `time`, `email`, `uri`, `uuid`, `ipv4`, `ipv6`. |
| `pattern` | `string` | Regex the string value must match. |
| `minimum` / `maximum` | `number` | Numeric range (inclusive). |
| `minLength` / `maxLength` | `integer` | String length range. |
| `minItems` / `maxItems` | `integer` | Array length range. |
| `properties` | `object` | Map of field → nested fragment. |
| `required` | `string[]` | Names of fields that must be present. |
| `items` | `object` | Fragment describing array element type. |

## Errors array

Each entry is `{ code, message }`:

| Field | Type | Description |
|-------|------|-------------|
| `code` | `string` | Machine-readable identifier, `^[A-Z][A-Z0-9_]{1,63}$`. |
| `message` | `string` | One-line explanation of when the error is raised (5–300 chars). |

Common codes: `NOT_FOUND`, `RATE_LIMIT`, `APPROVAL_MISSING`, `AUTH_REQUIRED`,
`TIMED_OUT`, `PATH_TRAVERSAL`, `SSRF_BLOCKED`.

## Security block keys

The `security` block is intentionally permissive so new categories can add
their own controls. Recognised keys:

### Common
| Key | Type | Description |
|-----|------|-------------|
| `requires_auth` | `boolean` | Tool calls out to an authenticated service. |
| `auth_provider` | `string` | `github`, `x_oauth2`, `google`, `slack`, `stripe`, `aws`, `gcp`, `azure`, `custom`. |
| `read_only` | `boolean` | Tool cannot mutate state. |
| `rate_limit` | `object` | `requests_per_minute` and/or `requests_per_day`. |

### filesystem
| Key | Description |
|-----|-------------|
| `path_traversal_regex` | Regex used to reject `..` or absolute paths. |
| `max_bytes` | Cap on bytes read or written per call. |
| `no_symlink_follow` | Refuse to follow symlinks out of the tree. |
| `overwrite_default` | Default value for the `overwrite` parameter. |
| `respects_gitignore` | Search tool skips paths matched by `.gitignore`. |
| `scoped_to_repo` | All paths are interpreted relative to the repo root. |

### shell
| Key | Description |
|-----|-------------|
| `requires_safety_profile` | List of `grok-config` `safety_profile` values that permit the tool. |
| `requires_explicit` | Additional explicit grant string, e.g. `"shell_access: true"`. |
| `sandbox` | Command runs inside an isolated sandbox. |
| `network_isolated_by_default` | No outbound network unless explicitly enabled. |

### x_platform
| Key | Description |
|-----|-------------|
| `approval_required` | A human must approve before the tool posts. |
| `blocks_if_require_approval_false` | Refuses to run if the caller disables approval. |
| `no_bulk_collection` | Search/read tools reject bulk scraping patterns. |
| `own_tweets_only` | Metrics tools refuse to query accounts other than the authenticated user. |

### github
| Key | Description |
|-----|-------------|
| `draft_default` | New PRs open as draft unless explicitly set otherwise. |
| `owner_pattern` | Regex validating the `owner` parameter. |
| `repo_pattern` | Regex validating the `repo` parameter. |

### web
| Key | Description |
|-----|-------------|
| `https_only` | Only `https://` URLs are accepted. |
| `ssrf_protection` | Resolve URLs and reject blocked ranges before fetching. |
| `blocked_ranges` | CIDR list of disallowed address ranges (RFC1918, loopback, link-local, ULA). |
| `uses_grok_builtin` | Delegates to Grok's built-in web search. |

### memory
| Key | Description |
|-----|-------------|
| `no_sensitive_data_warning` | Registry warns callers not to store PII/secrets. |
| `scope` | `agent`, `workspace`, or `global`. |
| `encrypted_at_rest` | Memory entries are encrypted on disk. |

### workflow
| Key | Description |
|-----|-------------|
| `delegates_to` | Array of tool IDs this composite invokes. |
| `inherits_security_of_delegates` | Union of delegate security constraints applies. |
| `pure_transform` | Tool performs computation only; no I/O or side effects. |

## Cross-referencing

- `grok-agent.yaml` `tools:` entries must match keys in this registry.
- `grok-workflow.yaml` step `action:` values that are not a spec name
  (`grok-test`, `grok-docs`, …) must match keys here.
- `grok-update.yaml` `actions:` that invoke tools resolve against this registry.

Unknown tool names should fail validation in CI — keep the registry as the
single source of truth.
