# Changelog

All notable changes to grok-yaml-standards are documented here.
Versions follow [Semantic Versioning](https://semver.org/).

---

## [2.0.0] — 2026-04-18

Grok 4.20 support. Two new official YAML specs, a schema discovery manifest, and non-breaking additions to four existing schemas.

### Added
- **`specs/grok-swarm.yaml`** — Annotated reference spec for Grok 4.20 multi-agent swarm orchestration. Configures swarm mode (`realtime-multi-agent`, `high-effort-16`, `single`), agent roles (coordinator, researcher, logic, creative, critic, moderator), model selection from the Grok 4.20 family, state persistence, and retry-with-backoff orchestration.
- **`schemas/grok-swarm.schema.json`** — Full JSON Schema (draft/2020-12) for `grok-swarm.yaml`. Validates all swarm fields with constrained enums, ranges, and examples.
- **`specs/grok-voice.yaml`** — Annotated reference spec for Grok 4.20 voice API. Configures STT/TTS models, voice identity, features (`real-time-conversation`, `emotion-aware`, `multi-speaker`, `speaker-diarization`), fallback behaviour, and safety limits.
- **`schemas/grok-voice.schema.json`** — Full JSON Schema (draft/2020-12) for `grok-voice.yaml`.
- **`schemas/index.json`** — Single-fetch discovery manifest listing all 14 schemas with `spec`, `spec_version`, `introduced_in`, `schema_url`, `file_glob`, and `required_by` fields. Use for VS Code integration and CI schema discovery.
- **`docs/index.md`** — Overview of all 14 specs with anchor links, VS Code snippet, and CI integration notes.
- **`docs/grok-swarm.md`** — Reference documentation for `grok-swarm.yaml`: mode table, agent role guide, tool set, state/orchestration field tables, examples, cross-references, and xAI SDK mapping.
- **`docs/grok-voice.md`** — Reference documentation for `grok-voice.yaml`: model table, feature guide, field table, fallback table, voice + agent pattern example, cross-references, and xAI SDK mapping.

### Changed (non-breaking — additive enum extensions)
- **`schemas/grok-agent.json`** `model_override` enum: added `grok-4.20`, `grok-4.20-multi-agent`, `grok-4.20-fast`
- **`schemas/grok-config.json`** `default_model` and `fallback_model` enums: added same three Grok 4.20 variants
- **`schemas/grok-security.json`** `x_scopes` enum: added `voice.read`, `voice.write` for Grok 4.20 voice API OAuth
- **`schemas/grok-tools.json`** `category` enum: added `voice`, `swarm` for Grok 4.20 tool categories
- **`README.md`**: updated badge and footer to v2.0.0; added Grok 4.20 specs table; expanded VS Code snippet with two new schema mappings; added `schemas/index.json` reference; updated "What's New" section

### No Breaking Changes
All v1.x `.grok/` folders remain valid. Existing `model_override`, `default_model`, `fallback_model`, `x_scopes`, and `category` values are unchanged. Update `compatibility` to `grok-yaml-standards@2.0+` to opt in to swarm and voice specs.

---

## [1.2.0] — 2026-04-16

Official launch on X. See [LAUNCH.md](LAUNCH.md) for the full announcement and @grok endorsement.

### Added
- **4 new spec extensions**: `grok-tools.yaml`, `grok-deploy.yaml`, `grok-analytics.yaml`, `grok-ui.yaml`
- **JSON Schema upgraded to draft/2020-12** across all 12 specs — `$schema`, `$id`, and `title` updated; breaking constraints added to agent, workflow, security, and prompts schemas
- **Comprehensive `schema.md` field references** for all 12 specs with full field tables, validation examples, security notes, and Cross-References sections (Depends On, Used By, xAI SDK / LiteLLM / Semantic Kernel mapping)
- **Advanced `.grok/*.advanced.yaml` templates** — multi-agent orchestration (`grok-agent.advanced.yaml`), parallel-capable workflows with retry logic (`grok-workflow.advanced.yaml`), research-grade security profile (`grok-security.advanced.yaml`)
- **Expanded use cases** (`usecases.md`) for 5 specs — 5 real-world scenarios each with persona, scenario, example YAML, pitfalls, and next steps (grok-agent, grok-workflow, grok-security, grok-prompts, grok-config)
- `SECURITY.md` threat model, `CONTRIBUTING.md`, `ROADMAP.md`, `CONTRIBUTORS.md`
- GitHub issue template (`bug-report.yml`)
- Compatibility matrix

### Changed
- Relicensed from MIT to Apache 2.0 to align with the xAI ecosystem
- README overhauled: centered header with badges, SDK mapping table, ecosystem section, links to CHANGELOG.md and LAUNCH.md

### No Breaking Changes
All v1.1.x `.grok/` folders remain valid — update `compatibility` to `grok-yaml-standards@1.2+` to opt in to new features.

---

## [1.1.0] — 2026-03

- Initial 8 core specs: grok-config, grok-prompts, grok-agent, grok-workflow, grok-update, grok-test, grok-docs, grok-security
- Starter `.grok/` template folder
- Basic JSON Schema validation (draft-07)
