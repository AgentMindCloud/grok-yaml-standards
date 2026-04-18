# grok-analytics.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-analytics.json`

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the config owner, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `analytics` | object | ✅ | — | — | Analytics configuration block. See [Analytics Object](#analytics-object). |

---

## Analytics Object

### Example

```yaml
analytics:
  enabled: false            # must be explicitly opted in — never true by default
  provider: "posthog"
  api_key_secret: "POSTHOG_API_KEY"   # references a repo secret, never hardcoded
  sampling_rate: 0.1        # 10% sample on high-volume repos to control cost
  anonymize_user_ids: true  # hash all user identifiers before sending
  data_retention_days: 90
  opt_out_roles: ["bot", "github-actions[bot]"]
  events:
    grok_invoked:
      description: "Fires each time a @grok trigger is processed."
      pii_safe: true
      enabled: true
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `enabled` | boolean | ✅ | `false` | — | Master switch. No data is sent unless explicitly `true`. Never default to `true` in templates. |
| `provider` | string | ✅ | — | enum: `posthog`, `mixpanel`, `amplitude`, `segment`, `datadog`, `custom` | Analytics backend provider. |
| `endpoint` | string | — | — | format: uri | Self-hosted provider endpoint. Used when `provider: custom` or for EU data residency. |
| `api_key_secret` | string | — | — | references a repo secret | Repository secret key holding the provider API key. Never hardcode here. |
| `events` | object | — | `{}` | additionalProperties: event objects | Map of event identifiers to event definitions. See [Event Object](#event-object). |
| `sampling_rate` | number | — | `1.0` | minimum: 0; maximum: 1 | Fraction of events captured. `1.0` = 100%; `0.1` = 10%. Reduce for high-volume repos. |
| `anonymize_user_ids` | boolean | — | `true` | — | Hash all user identifiers (GitHub usernames, X handles) before sending. |
| `data_retention_days` | integer | — | `90` | minimum: 1; maximum: 730 | Days the provider retains event data. Align with your legal jurisdiction. |
| `opt_out_roles` | string[] | — | `[]` | uniqueItems; each maxLength: 100 | User roles excluded from all tracking. Always include `"bot"` and CI accounts. |

---

## Event Object

### Example

```yaml
analytics:
  events:
    grok_invoked:
      description: "Fires each time a @grok trigger is processed."
      pii_safe: true
      properties:
        trigger_type:
          type: string
          description: "The spec triggered (e.g. grok-test, grok-deploy)."
        duration_ms:
          type: integer
          description: "Wall-clock milliseconds for the invocation."
      enabled: true
    pr_reviewed:
      description: "Fires when grok-test runs on a pull request."
      pii_safe: false    # may include branch names with PII — requires security review
      enabled: false     # disabled until PII handling is confirmed
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `description` | string | — | — | maxLength: 500 | When and why this event fires. |
| `pii_safe` | boolean | ✅ | — | — | `true` only if no property can contain personally identifiable information. `false` triggers mandatory security review. |
| `properties` | object | — | `{}` | additionalProperties: `{type, description}` | Map of property names to their type and description. |
| `enabled` | boolean | — | `true` | — | Set `false` to stop collecting without removing the definition. |

---

## provider Enum

| Value | Service |
|-------|---------|
| `posthog` | PostHog (open-source, self-hostable) |
| `mixpanel` | Mixpanel |
| `amplitude` | Amplitude |
| `segment` | Twilio Segment |
| `datadog` | Datadog |
| `custom` | Self-hosted or custom endpoint via `endpoint` field |
