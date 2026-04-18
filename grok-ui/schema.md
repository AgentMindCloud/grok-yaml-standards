# grok-ui.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-ui.json`

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the config owner, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `ui` | object | ✅ | — | — | Top-level UI personalisation and extension settings. |

---

## UI Object

### Example

```yaml
ui:
  theme: "dark"
  locale: "en-US"
  voice_commands:
    enabled: false      # requires explicit opt-in; triggers microphone permission prompt
  dashboard:
    enabled: true
    refresh_seconds: 30
  shortcuts:
    keyboard:
      - key: "ctrl+shift+t"
        action: "grok-test"
        description: "Run all test suites"
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `theme` | string | — | `"system"` | enum: `dark`, `light`, `system`, `high-contrast` | Colour theme for the Grok IDE extension and dashboard. |
| `locale` | string | — | `"en-US"` | pattern: `^[a-z]{2}(-[A-Z]{2,4})?$` (BCP-47) | Locale for UI text and number formatting. |
| `voice_commands` | object | — | — | — | Voice command configuration. See [Voice Commands Object](#voice-commands-object). |
| `dashboard` | object | — | — | — | Live dashboard configuration. See [Dashboard Object](#dashboard-object). |
| `shortcuts` | object | — | — | — | Keyboard shortcut bindings. See [Shortcuts Object](#shortcuts-object). |

---

## Voice Commands Object

### Example

```yaml
ui:
  voice_commands:
    enabled: true             # triggers microphone permission prompt
    language: "en-US"
    wake_phrase: "hey grok"
    commands:
      - phrase: "run tests"
        action: "grok-test"
      - phrase: "deploy staging"
        action: "grok-deploy"
        target: "staging"
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `enabled` | boolean | ✅ | `false` | — | Activate voice command listening. Requires explicit opt-in (triggers microphone permission). |
| `language` | string | — | `"en-US"` | pattern: `^[a-z]{2}(-[A-Z]{2,4})?$` | BCP-47 code for speech recognition. |
| `wake_phrase` | string | — | `"hey grok"` | minLength: 2; maxLength: 50 | Phrase that activates the listener. Case-insensitive. |
| `commands` | array | — | `[]` | — | Voice command bindings. See [Voice Command Item](#voice-command-item). |

---

## Voice Command Item

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `phrase` | string | ✅ | — | minLength: 2; maxLength: 100 | Spoken phrase (after the wake phrase) that triggers this command. |
| `action` | string | ✅ | — | enum: `grok-test`, `grok-deploy`, `grok-security`, `grok-docs`, `grok-workflow`, `grok-agent`, `grok-update`, `grok-prompts`, `grok-ui` | Grok spec or built-in action to execute. |
| `suite` | string | — | — | test suite identifier | Test suite filter when `action: grok-test`. |
| `target` | string | — | — | deploy or docs target | Target identifier when `action: grok-deploy` or `grok-docs`. |
| `scan` | string | — | — | security scan identifier | Scan identifier when `action: grok-security`. |
| `command` | string | — | — | — | Sub-command for built-in UI actions. |

---

## Dashboard Object

### Example

```yaml
ui:
  dashboard:
    enabled: true
    refresh_seconds: 30      # global default; can be overridden per widget
    widgets:
      - type: "test_results"
        title: "Latest Test Run"
        show_last_n: 5
      - type: "security_summary"
        title: "Security Alerts"
        alert_level: "high"    # filter to high and critical only
      - type: "deployment_history"
        target: "production"
        show_last_n: 10
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `enabled` | boolean | ✅ | `false` | — | Show the Grok dashboard panel in the IDE extension. |
| `refresh_seconds` | integer | — | `30` | minimum: 5; maximum: 3600 | Default data refresh interval for all widgets. |
| `widgets` | array | — | `[]` | — | Ordered list of widgets displayed top-to-bottom. See [Widget Item](#widget-item). |

---

## Widget Item

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `type` | string | ✅ | — | enum: `agent_status`, `test_results`, `deployment_history`, `security_summary`, `analytics_pulse`, `custom` | Widget type determining what data is fetched and rendered. |
| `title` | string | — | — | maxLength: 100 | Display title in the widget header. |
| `refresh_seconds` | integer | — | — | minimum: 5; maximum: 3600 | Per-widget refresh interval override. |
| `show_last_n` | integer | — | — | minimum: 1; maximum: 100 | Number of most recent items to display in list widgets. |
| `suite` | string | — | — | test suite identifier | Filter for `test_results` widgets. |
| `target` | string | — | — | deploy target identifier | Filter for `deployment_history` widgets. |
| `alert_level` | string | — | `"info"` | enum: `info`, `warning`, `high`, `critical` | Minimum severity shown in `security_summary` widgets. |
| `time_window_hours` | integer | — | `24` | minimum: 1; maximum: 8760 | Time window for `analytics_pulse` widgets. |

---

## Shortcuts Object

### Example

```yaml
ui:
  shortcuts:
    keyboard:
      - key: "ctrl+shift+t"
        action: "grok-test"
        description: "Run all test suites"
      - key: "ctrl+shift+d"
        action: "grok-docs"
        target: "AutoREADME"
        description: "Regenerate README"
```

### Keyboard Shortcut Item

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `key` | string | ✅ | — | pattern: `^(ctrl\|cmd\|alt\|shift\|meta)(\+(ctrl\|cmd\|alt\|shift\|meta\|[a-z0-9]))+$`; maxLength: 50 | Key combination. Use `ctrl` for Win/Linux, `cmd` for macOS. |
| `action` | string | ✅ | — | minLength: 1; maxLength: 100 | Grok spec or action to invoke. Approval gates on target actions are never bypassed. |
| `description` | string | — | — | maxLength: 200 | Human-readable description shown in the shortcut help panel. |
