# grok-prompts.yaml Field Reference

Full JSON Schema: [`/schemas/grok-prompts.json`](../schemas/grok-prompts.json)

---

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this prompt library file (e.g. `"1.2.0"`). |
| `author` | `string` | ✅ | X handle of the library maintainer, prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `prompt_library` | `object` | ✅ | Named prompt definitions. At least one entry required. |

---

## prompt_library entries

Each key becomes the prompt identifier used in `@grok use prompts:<id>` triggers.

**Key format**: snake_case recommended (e.g. `viral_thread`, `code_review`).

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `template` | `string` | ✅ | The prompt text. Use `{variable_name}` placeholders for runtime interpolation. Min 10 chars, max 8000 chars. |
| `description` | `string` | — | Human-readable explanation of when to use this prompt. Max 500 chars. |
| `variables` | `string[]` | — | Required variable names that must be supplied at invocation. Must match `{placeholders}` in the template. |
| `optional_variables` | `string[]` | — | Variable names that enrich the prompt when supplied but are not mandatory. |
| `temperature` | `number` | — | Per-prompt sampling temperature override. Range: `0` – `2`. Overrides `grok.temperature`. |
| `max_tokens` | `integer` | — | Per-prompt token cap override. Range: `1` – `131072`. |
| `model` | `string` | — | Per-prompt model override. Useful when this prompt needs a specific capability. |
| `tags` | `string[]` | — | Categorisation tags for filtering and discovery (e.g. `social`, `code`, `marketing`). Pattern: `^[a-z0-9_-]+$`. |
| `output_format` | `string` | — | Expected output structure. See enum values below. |
| `cache_responses` | `boolean` | `false` | Cache the response for identical variable combinations to reduce latency. |

**`model` enum values:**
`grok-4` · `grok-3` · `grok-3-mini` · `grok-3-fast` · `grok-2` · `grok-1`

**`output_format` enum values:**
`plain` · `markdown` · `json` · `yaml` · `thread` · `bullet_list` · `table`

---

## Variable placeholder syntax

Variables in `template` use curly-brace syntax: `{variable_name}`.

- Variable names must match the pattern `^[a-z_][a-z0-9_]*$`
- All names listed in `variables` must appear as `{name}` in the template
- Names in `optional_variables` may or may not appear in the template

**Example:**
```yaml
viral_thread:
  template: "Write a thread about {topic}. Tone: {tone}."
  variables: ["topic", "tone"]
  temperature: 0.85
  output_format: "thread"
```
