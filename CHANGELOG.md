# Changelog

All notable changes to `grok-yaml-standards` are documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `SECURITY.md` with threat model, responsible-disclosure process, and hardening
  guidance for downstream consumers.
- `.github/CODEOWNERS` — maintainer review required on `schemas/**`, `grok-*/**`,
  and `.github/**`.
- `.github/FUNDING.yml` — GitHub Sponsors + Buy Me a Coffee.
- `.grok/brand-tokens.yaml` — locked brand palette + SVG hero logo, referenced
  by `README.md`.
- `CHANGELOG.md` (this file), with backfilled history for 1.0.0 → 1.2.0.
- `version-reconciliation.md` — authoritative list of the 12 standards plus a
  one-line PR text for downstream repos that claim 14.
- README hero banner and "What's coming in v1.3 / v2.14" teaser.
- `CONTRIBUTORS.md` real table (replacing the placeholder gallery).

### Changed
- `standards-overview.md` — updated from "8 Grok YAML Standards" to the full 12,
  with spec extensions added to the comparison table.
- `ROADMAP.md` — Phase 1 milestone now reads "Maintain 12 schemas" (was "Finalize 8 schemas").

### Deferred
- `.github/workflows/validate-schemas.yml` (ajv + yamllint CI) — planned for a
  follow-up PR so the CI contract can be tested on a draft branch before
  becoming required.
- `.github/CODE_OF_CONDUCT.md` (Contributor Covenant v2.1) — deferred until a
  maintainer-owned contact address is available.

## [1.2.0] — 2026-04-17

### Added
- **4 new spec extensions**: `grok-tools.yaml`, `grok-deploy.yaml`,
  `grok-analytics.yaml`, `grok-ui.yaml`, each with a matching JSON Schema,
  spec folder (README + example + security notes + use cases + triggers),
  and ready-to-drop `.grok/` sample.
- **Compatibility matrix** in `README.md` covering all 12 standards.
- **Comprehensive JSON Schema validation** — property-level schemas with enums,
  constraints, required fields, and descriptions for all 12 specs.
- `.github/workflows/release.yml` — GitHub Actions workflow that auto-publishes
  a GitHub Release when a `v*` tag is pushed.
- `.github/ISSUE_TEMPLATE/feature-request.md`.
- `LAUNCH.md` + X launch announcement.

### Changed
- Relicensed from MIT to **Apache License 2.0** to align with xAI standards.
- README restructured around "Core Standards" + "Spec Extensions" tables.

## [1.1.0] — 2026-04-16

### Added
- **JSON Schemas for the 8 core standards** in `schemas/`
  (`grok-config`, `grok-prompts`, `grok-agent`, `grok-workflow`, `grok-update`,
  `grok-test`, `grok-docs`, `grok-security`) — all Draft 7 with `$id`, `title`,
  `description`, required `version` / `author` / `compatibility` fields.
- Ready-to-drop `.grok/` sample folder with production-shape YAML for each
  core standard.
- Expanded examples, security considerations, and `x-trigger-examples.md` in
  every `grok-*/` spec folder.

### Changed
- Every core YAML bumped to `1.1.0` with explicit `compatibility:` entries.

## [1.0.0] — 2026-04-16

### Added
- Initial public release with the 8 core Grok YAML standards:
  `grok-config`, `grok-prompts`, `grok-agent`, `grok-workflow`, `grok-update`,
  `grok-test`, `grok-docs`, `grok-security`.
- Per-standard spec folders (`grok-*/`) containing `README.md`, `example.yaml`,
  `schema.md`, `security-considerations.md`, `usecases.md`, and
  `x-trigger-examples.md`.
- Top-level docs: `README.md`, `CONTRIBUTING.md`, `ROADMAP.md`,
  `standards-overview.md`, `how-xai-can-adopt.md`.
- MIT license (relicensed to Apache 2.0 in 1.2.0).

[Unreleased]: https://github.com/AgentMindCloud/grok-yaml-standards/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/AgentMindCloud/grok-yaml-standards/releases/tag/v1.2.0
[1.1.0]: https://github.com/AgentMindCloud/grok-yaml-standards/releases/tag/v1.1.0
[1.0.0]: https://github.com/AgentMindCloud/grok-yaml-standards/releases/tag/v1.0.0
