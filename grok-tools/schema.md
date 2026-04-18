# grok-tools.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-tools.json`

Every tool is a **formal contract**: typed `parameters`, typed `returns`, an explicit
`errors` vocabulary, and a `security` block. Agents and workflows reference tools by
name; this file is the single source of truth for I/O shape and safety constraints.

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the registry maintainer, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `tools` | object | ✅ | — | minProperties: 1; key pattern: `^[a-z][a-z0-9_]{1,63}$` | Map of tool identifiers to formal contracts. |

---

## Tool Definition Object

### Example

```yaml
tools:
  read_file:
    category: filesystem
    description: "Read the contents of a single file by repo-relative path."
    parameters:
      type: object
      properties:
        path:
          type: string
          pattern: "^(?!.*\\.\\.)[^/].*$"   # path traversal guard
        encoding:
          type: string
          enum: ["utf-8", "binary", "base64"]
          default: "utf-8"
      required: [path]
    returns:
      type: object
      properties:
        content: { type: string }
        size_bytes: { type: integer }
    errors:
      - { code: "NOT_FOUND", message: "No file exists at the given path." }
      - { code: "PATH_TRAVERSAL", message: "Path escapes the repository root." }
    security:
      read_only: true
      max_bytes: 10485760
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `category` | string | ✅ | — | enum: `filesystem`, `shell`, `x_platform`, `github`, `web`, `memory`, `workflow` | Functional group. Determines which security keys are expected. |
| `description` | string | ✅ | — | minLength: 10; maxLength: 500 | One-sentence explanation of what the tool does. |
| `parameters` | object | ✅ | — | must have `type: object` | JSON Schema fragment defining the tool's inputs. |
| `returns` | object | ✅ | — | must have `type: object` | JSON Schema fragment defining the success output shape. |
| `errors` | array | — | `[]` | items: `{code, message}` | Explicit error vocabulary this tool may raise. |
| `security` | object | ✅ | — | — | Safety constraints. Keys vary by category. |
| `enabled` | boolean | — | `true` | — | Set `false` to disable the tool without removing its definition. |

---

## category Enum

| Value | Purpose |
|-------|---------|
| `filesystem` | Scoped I/O against the repository working tree. |
| `shell` | Arbitrary command execution. Always gated by `safety_profile` + explicit grant. |
| `x_platform` | Posting to or reading from X. All writes require human approval. |
| `github` | GitHub API operations. Writes default to draft PRs. |
| `web` | Outbound HTTP. HTTPS only; SSRF guards mandatory. |
| `memory` | Agent-scoped persistent state. No sensitive data. |
| `workflow` | Composite transforms that orchestrate other tools. |

---

## Parameters / Returns Fragment

Both `parameters` and `returns` are JSON Schema fragments (draft-07 subset):

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | `string`, `integer`, `number`, `boolean`, `array`, `object`, `null`. |
| `description` | string | Human-readable explanation (max 500 chars). |
| `default` | any | Value used when the caller omits the parameter. |
| `enum` | any[] | Restricts value to the listed options. |
| `format` | string | `date-time`, `date`, `time`, `email`, `uri`, `uuid`, `ipv4`, `ipv6`. |
| `pattern` | string | Regex the string value must match. |
| `minimum` / `maximum` | number | Numeric range (inclusive). |
| `minLength` / `maxLength` | integer | String length range. |
| `minItems` / `maxItems` | integer | Array length range. |
| `properties` | object | Map of field → nested fragment. |
| `required` | string[] | Names of required fields (for `object` type). |
| `items` | object | Fragment describing array element type. |

---

## Errors Array

Each entry: `{ code, message }`

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `code` | string | pattern: `^[A-Z][A-Z0-9_]{1,63}$` | Machine-readable UPPER_SNAKE_CASE error code. |
| `message` | string | minLength: 5; maxLength: 300 | One-line explanation of when this error is raised. |

Common codes: `NOT_FOUND`, `RATE_LIMIT`, `APPROVAL_MISSING`, `AUTH_REQUIRED`, `TIMED_OUT`, `PATH_TRAVERSAL`, `SSRF_BLOCKED`.

---

## Security Block Keys

The `security` block is open — new categories may add their own keys. Recognised keys:

### Common
| Key | Type | Description |
|-----|------|-------------|
| `requires_auth` | boolean | Tool calls out to an authenticated service. |
| `auth_provider` | string | `github`, `x_oauth2`, `google`, `slack`, `aws`, `gcp`, `azure`, `custom`. |
| `read_only` | boolean | Tool cannot mutate state. |
| `rate_limit` | object | `requests_per_minute` (int) and/or `requests_per_day` (int). |

### filesystem
| Key | Description |
|-----|-------------|
| `path_traversal_regex` | Regex rejecting `..` or absolute paths. |
| `max_bytes` | Cap on bytes read or written per call. |
| `no_symlink_follow` | Refuse to follow symlinks out of the repo tree. |
| `overwrite_default` | Default value for the `overwrite` parameter. |
| `scoped_to_repo` | All paths interpreted relative to the repo root. |

### shell
| Key | Description |
|-----|-------------|
| `requires_safety_profile` | List of allowed `grok-config` `safety_profile` values. |
| `requires_explicit` | Additional grant string, e.g. `"shell_access: true"`. |
| `sandbox` | Command runs inside an isolated sandbox. |
| `network_isolated_by_default` | No outbound network unless explicitly enabled. |

### x_platform
| Key | Description |
|-----|-------------|
| `approval_required` | Human must approve before the tool writes to X. |
| `blocks_if_require_approval_false` | Refuses to run if approval is disabled. |
| `no_bulk_collection` | Search/read tools reject bulk scraping. |
| `own_tweets_only` | Metrics tools refuse to query other accounts. |

### github
| Key | Description |
|-----|-------------|
| `draft_default` | New PRs open as draft unless explicitly overridden. |
| `owner_pattern` | Regex validating the `owner` parameter. |
| `repo_pattern` | Regex validating the `repo` parameter. |

### web
| Key | Description |
|-----|-------------|
| `https_only` | Only `https://` URLs accepted. |
| `ssrf_protection` | Resolve URLs and reject blocked address ranges. |
| `blocked_ranges` | CIDR list of disallowed ranges (RFC1918, loopback, link-local). |

### memory
| Key | Description |
|-----|-------------|
| `no_sensitive_data_warning` | Registry warns callers not to store PII or secrets. |
| `scope` | `agent`, `workspace`, or `global`. |
| `encrypted_at_rest` | Memory entries are encrypted on disk. |

### workflow
| Key | Description |
|-----|-------------|
| `delegates_to` | Array of tool IDs this composite invokes. |
| `inherits_security_of_delegates` | Union of delegate security constraints applies. |
| `pure_transform` | Tool performs computation only; no I/O or side effects. |

---

## Cross-References

### Depends On
- **grok-config.yaml**: `safety_profile` determines which tool categories are available.
- **grok-security.yaml**: `shell` category tools require `safety_profile: balanced` or higher.

### Used By
- **grok-agent.yaml**: `tools[]` array items must be keys in this registry.
- **grok-workflow.yaml**: `steps[].action` tool IDs resolve against this registry.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `parameters` (JSON Schema) | `tools[].function.parameters` in the API request |
| `returns` (JSON Schema) | Shape of the parsed tool response |
| `errors[].code` | Error discriminant in tool response handling |
| `security.rate_limit` | Client-side throttling before tool calls |
| `category: x_platform` | Requires `tools[].function` with X OAuth header |

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| `parameters` | `tools=[{"type":"function","function":{"parameters":{...}}}]` |
| `description` | `tools[].function.description` |
| `errors[].code` | Exception handling in `litellm.completion` callback |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| Tool definition | `KernelFunction` decorated with `@kernel_function` |
| `parameters` | `KernelFunctionMetadata` parameter descriptors |
| `returns` | `KernelFunctionMetadata` return type |
| `security.read_only` | `KernelPlugin` permission attribute |
| `category: memory` | `ISemanticTextMemory` plugin |
