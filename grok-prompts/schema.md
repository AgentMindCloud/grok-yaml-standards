# grok-prompts.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-prompts.json`

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the library maintainer, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `prompt_library` | object | ✅ | — | minProperties: 1; key pattern: `^[a-z_][a-z0-9_]*$` | Named prompt definitions. Each key is a prompt ID used in `@grok use prompts:<id>`. |

---

## Prompt Entry Object

Each key in `prompt_library` maps to a prompt entry. Invoke with `@grok use prompts:<key>`.

### Example

```yaml
prompt_library:
  viral_thread:
    description: "Turns any topic into a punchy 8-tweet X thread."
    template: |
      Write an 8-tweet thread about {topic}.
      Tone: {tone}. Start with a strong hook. End with a call to action.
      Each tweet must be under 280 characters.
    variables: ["topic", "tone"]
    optional_variables: ["audience"]
    output_format: "thread"
    temperature: 0.85      # creative output benefits from higher temperature
    cache_responses: false # threads should always be freshly generated
    tags: ["social", "content", "x-native"]
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `description` | string | — | — | maxLength: 500 | Human-readable explanation of this prompt's purpose. |
| `template` | string | ✅ | — | minLength: 10; maxLength: 8000 | The prompt text. Use `{variable_name}` for runtime interpolation. |
| `variables` | string[] | — | `[]` | each item pattern: `^[a-z_][a-z0-9_]*$` | Required variables. Must appear as `{name}` in `template`. Runtime fails if any are missing. |
| `optional_variables` | string[] | — | `[]` | same pattern as `variables` | Optional enrichment variables. Prompt renders without them if not supplied. |
| `output_format` | string | — | `"plain"` | enum: `plain`, `markdown`, `json`, `yaml`, `thread`, `bullet_list`, `table` | Expected output structure hint. |
| `temperature` | number | — | `0.7` | minimum: 0; maximum: 2 | Per-prompt sampling temperature. Overrides `grok.temperature`. `0` = deterministic. |
| `max_tokens` | integer | — | — | minimum: 1; maximum: 131072 | Per-prompt token cap. Overrides `grok.max_tokens`. |
| `model` | string | — | — | enum: `grok-4`, `grok-3`, `grok-3-mini`, `grok-3-fast`, `grok-2`, `grok-1` | Per-prompt model override for capability-specific prompts. |
| `cache_responses` | boolean | — | `false` | — | Cache response for identical variable combinations. Avoid for time-sensitive or security prompts. |
| `tags` | string[] | — | `[]` | maxItems: 10; each pattern: `^[a-z0-9_-]{1,50}$` | Categorisation tags for discovery and filtering. |

---

## Variable Placeholder Syntax

Variables in `template` use curly-brace syntax: `{variable_name}`.

Rules:
- Variable names: pattern `^[a-z_][a-z0-9_]*$`
- All names in `variables` must appear as `{name}` in the template
- Names in `optional_variables` may or may not appear
- Never interpolate raw user input directly into a `system:` block (see `security-considerations.md`)

### Example

```yaml
code_review:
  template: |
    Review the following {language} code for {focus_area}.
    Severity scale: critical / high / medium / low.
    Code:
    {code_snippet}
  variables: ["language", "focus_area", "code_snippet"]
  output_format: "markdown"
  temperature: 0.1    # low temperature for deterministic security reviews
  tags: ["code", "security", "review"]
```

---

## output_format Enum

| Value | Description |
|-------|-------------|
| `plain` | Unstructured prose. |
| `markdown` | GitHub-flavoured markdown. |
| `json` | JSON object or array. |
| `yaml` | YAML document. |
| `thread` | Ordered list of tweets, each under 280 chars. |
| `bullet_list` | Unordered bullet list. |
| `table` | Markdown table with headers. |

---

## Validation Examples

```yaml
# INVALID — template too short
prompt_library:
  t:
    template: "Hi"
# Error: template must be at least 10 characters

# INVALID — variable used in template but not declared
prompt_library:
  review:
    template: "Review the {code} for {language} issues."
    variables: ["code"]
# Error: {language} is used in template but not declared in variables

# VALID — full review prompt with reasoning
prompt_library:
  code_review:
    description: "Static analysis review prompt for any language."
    template: |
      Review the following {language} code for {focus}.
      Severity: critical / high / medium / low.
      Code:
      {code}
    variables: ["language", "focus", "code"]
    output_format: "markdown"
    temperature: 0.1
    reasoning_mode: "high"
    response_format: "text"
    tags: ["code", "security", "review"]
```

---

## Security Notes

- **`template`**: Never place user-supplied values into a `system:` block — use template variables in the user block only (see PT1 in `security-considerations.md`).
- **`cache_responses: false`** for any prompt whose variables could include PII, session-specific data, or secrets; cached responses may leak across callers.
- **`system_prompt`**: Must be static text; dynamic context belongs in template variables so it stays in the user message layer, not the system boundary.
- **`reasoning_mode: max`** significantly increases token usage and latency; always pair with an explicit `max_tokens` cap to prevent runaway cost.

---

## Cross-References

| Spec / SDK | Field | Relationship |
|------------|-------|--------------|
| `grok-agent.yaml` | `system_prompt` | Static agent-level instruction; the prompt `template` adds the per-call variable layer on top. |
| `grok-workflow.yaml` | `steps[].template` | Workflow steps reference a `prompt_library` key via the `template` field. |
| xAI SDK | `reasoning_mode` | Maps to `reasoning_effort` parameter: `"low"` / `"high"` / `"max"`. |
| xAI SDK | `response_format` | Maps to the `response_format` object in the chat completions API request. |
| xAI SDK | `system_prompt` | Maps to the first `system` role entry in the `messages[]` array. |
