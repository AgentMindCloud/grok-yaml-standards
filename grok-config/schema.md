# grok-config.yaml Field Reference

Full JSON Schema: [`/schemas/grok-config.json`](../schemas/grok-config.json)

---

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this config file (e.g. `"1.2.0"`). Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`. |
| `author` | `string` | ✅ | X handle of the file owner, prefixed with `@` (e.g. `"@JanSol0s"`). |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. At least one item required. |
| `grok` | `object` | — | Global Grok model behavior settings. See below. |
| `context` | `object` | — | Static context prepended to every conversation. See below. |
| `privacy` | `object` | — | Data handling and telemetry controls. See below. |
| `shortcuts` | `object` | — | Keyword → expansion prompt map. See below. |

---

## grok object fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `default_model` | `string` | `"grok-4"` | Grok model for all requests unless overridden per-prompt. |
| `temperature` | `number` | `0.7` | Sampling randomness. Range: `0` (deterministic) – `2` (highly creative). |
| `max_tokens` | `integer` | `16384` | Hard token cap per response. Range: `1` – `131072`. |
| `response_language` | `string` | `"en"` | BCP-47 language tag (e.g. `"en"`, `"fr"`, `"zh-CN"`). |
| `personality` | `string` | `"helpful-maximalist"` | Named personality preset. See enum values below. |
| `reasoning_depth` | `string` | `"high"` | Depth of internal reasoning. See enum values below. |
| `stream_responses` | `boolean` | `true` | Stream tokens as generated rather than waiting for full response. |
| `fallback_model` | `string` | — | Model to use if the primary is unavailable or rate-limited. |

**`default_model` / `fallback_model` enum values:**
`grok-4` · `grok-3` · `grok-3-mini` · `grok-3-fast` · `grok-2` · `grok-1`

**`personality` enum values:**
`helpful-maximalist` · `concise` · `creative` · `technical` · `balanced` · `socratic` · `executive`

**`reasoning_depth` enum values:**
`low` · `medium` · `high` · `ultra`

---

## context object fields

| Field | Type | Description |
|-------|------|-------------|
| `company` | `string` | Project or organisation name. Max 100 chars. |
| `audience` | `string` | Who will read the responses (e.g. `"X power users & developers"`). Max 200 chars. |
| `tone` | `string` | Prose style guidance (e.g. `"clear, witty, actionable"`). Max 200 chars. |
| `key_constraints` | `string[]` | Hard rules Grok must respect in every response. Up to 20 items, 200 chars each. |
| `domain_knowledge` | `string[]` | File paths or URLs injected as background knowledge into every conversation. |

---

## privacy object fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `allow_telemetry` | `boolean` | `false` | Allow xAI to collect usage telemetry for product improvement. |
| `share_anonymous_usage` | `boolean` | `false` | Share anonymised aggregate statistics with the community. |
| `never_share` | `string[]` | — | Categories of data that must never leave the local environment. |
| `data_retention_days` | `integer` | `30` | Days Grok retains conversation history. Range: `0` – `365`. `0` = no retention. |
| `redact_patterns` | `string[]` | — | Regex patterns whose matches are redacted from prompts before sending to xAI. |

**`never_share` enum values:**
`api_keys` · `secrets` · `personal_data` · `passwords` · `tokens` · `env_vars` · `credentials` · `private_keys`

---

## shortcuts object

An open map of trigger keyword → expansion prompt string. Invoked with `@grok <keyword>` in any issue, PR, or thread.

```yaml
shortcuts:
  "todo": "Turn this into a prioritized task list with deadlines"
  "thread": "Convert this into a viral X thread (max 8 tweets)"
```

Values: `string`, min 1 char, max 500 chars.
