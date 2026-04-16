# grok-config.yaml Schema

Full field documentation + validation rules.

- `version` (string, required): Semantic version of the standard.
- `author` (string, required): GitHub/X handle of the maintainer.
- `compatibility` (array, required): List of compatible Grok standards.
- `grok` (object): All Grok model settings (temperature, max_tokens, etc.).
- `context` (object): Persistent key-value context injected into every Grok call.
- `privacy` (object): Telemetry and data-sharing preferences.

JSON Schema validation available in the repo root (coming in v1.1).
