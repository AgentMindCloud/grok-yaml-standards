# grok-ui.yaml Field Reference

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this UI config file (e.g. `"1.0.0"`). |
| `author` | `string` | ✅ | X handle prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `ui` | `object` | ✅ | Top-level UI configuration. |

## ui fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `theme` | `string` | — | UI colour theme: `dark`, `light`, `system`, `high-contrast`. Defaults to `system`. |
| `locale` | `string` | — | BCP-47 locale code for the UI (e.g. `en-US`, `fr-FR`). Defaults to `en-US`. |
| `voice_commands` | `object` | — | Voice command configuration (see below). |
| `dashboard` | `object` | — | Dashboard widget configuration (see below). |
| `shortcuts` | `object` | — | Keyboard shortcut bindings (see below). |

## voice_commands fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `enabled` | `boolean` | ✅ | Activate voice command listening. Requires microphone permission. |
| `language` | `string` | — | BCP-47 language code for speech recognition (e.g. `en-US`). |
| `wake_phrase` | `string` | — | Phrase that activates listening (e.g. `"hey grok"`). Case-insensitive. |
| `commands` | `object[]` | — | List of voice command definitions (see below). |

## Voice command item fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `phrase` | `string` | ✅ | Spoken phrase that triggers the command (after the wake phrase). |
| `action` | `string` | ✅ | Grok spec or action to execute (e.g. `grok-test`, `grok-deploy`). |
| `suite` / `target` / `scan` / `command` | `string` | — | Action-specific argument matching the corresponding spec's identifier key. |

## dashboard fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `enabled` | `boolean` | ✅ | Show the Grok dashboard panel. |
| `refresh_seconds` | `integer` | — | Default data refresh interval for all widgets (seconds). |
| `widgets` | `object[]` | — | Ordered list of dashboard widget definitions (see below). |

## Widget definition fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | `string` | ✅ | Widget type: `agent_status`, `test_results`, `deployment_history`, `security_summary`, `analytics_pulse`, `custom`. |
| `title` | `string` | — | Display title shown in the widget header. |
| `refresh_seconds` | `integer` | — | Per-widget refresh override. |
| `show_last_n` | `integer` | — | Number of most recent items to display. |
| `suite` / `target` / `alert_level` / `time_window_hours` | various | — | Widget-type-specific filter or configuration fields. |

## shortcuts.keyboard item fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `key` | `string` | ✅ | Key combination (e.g. `ctrl+shift+g`, `cmd+k`). |
| `action` | `string` | ✅ | Grok action or spec to invoke. |
| `description` | `string` | — | Human-readable description shown in the shortcut help panel. |
| Additional fields | various | — | Action-specific arguments (e.g. `suite`, `target`, `scan`). |
