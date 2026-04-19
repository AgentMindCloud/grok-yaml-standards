# Changelog

All notable changes to `grok-yaml-standards` are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] — 2026-04-19

Released as part of the **ecosystem-wide Session 2** cleanup pass
across the GrokInstall family of repositories. Session 1 established
the brand foundation in `grok-install-brand`; Session 2 brings this
canonical spec source up to the shared ecosystem standard and grows
the standards set from 12 to 14.

### Added
- `grok-swarm/` — new spec for multi-agent swarm coordination.
  - `grok-swarm/README.md`, `example.yaml`, `schema.md`,
    `usecases.md`, `security-considerations.md`,
    `x-trigger-examples.md`
  - `.grok/grok-swarm.yaml` — canonical sample
  - `schemas/grok-swarm.json` — full draft-07 JSON Schema with
    `members[]`, `coordinator`, `communication`, `consensus`, and
    `fallback` constraints
- `grok-voice/` — new spec for voice interaction pipelines.
  - `grok-voice/README.md`, `example.yaml`, `schema.md`,
    `usecases.md`, `security-considerations.md`,
    `x-trigger-examples.md`
  - `.grok/grok-voice.yaml` — canonical sample
  - `schemas/grok-voice.json` — full draft-07 JSON Schema covering
    input, output, the STT → intent → agent → TTS pipeline,
    latency budget, fallback, and explicit audio/transcript
    privacy controls
- `CHANGELOG.md` — this file.
- `DISCLAIMER.md` — canonical "not affiliated with xAI, Grok, or X"
  disclaimer, mirrored verbatim from `grok-install-brand`.
- `.github/FUNDING.yml` — GitHub Sponsors pointer for
  `AgentMindCloud` and `@JanSol0s`, matching the ecosystem
  foundation.

### Changed
- **Spec count 12 → 14**. The core + extensions tables in
  `README.md` and `standards-overview.md` now list `grok-swarm` and
  `grok-voice` alongside the existing twelve.
- **Repo version v1.2 → v2.0**. Every per-spec `version:` field in
  `.grok/*.yaml` and `grok-*/example.yaml` bumped to `"2.0.0"`.
- **Compatibility strings** bumped from `grok-yaml-standards@1.1+`
  and `@1.2+` to `grok-yaml-standards@2.0+` across all per-spec
  YAML files and README compatibility lines.
- `schemas/*.json` — `examples` hints for the top-level `version`
  field updated to `"2.0.0"` for consistency. No schema shape
  changes to any of the 12 existing specs; `$id` and `$schema`
  fields untouched.
- `README.md`, `schemas/README.md`, `standards-overview.md`,
  `CONTRIBUTORS.md` — updated spec count, version badge, table
  rows, and narrative to reflect 14 specs at v2.0.0.

### Unchanged / compatibility notes
- No breaking shape changes to the existing 12 specs. Downstream
  consumers (e.g. `grok-install-cli`) that validate against the
  existing schemas will continue to parse every v1.x-authored file.
- The `compatibility` pattern (`^[a-zA-Z0-9._-]+@[0-9]+\.[0-9]+(\+|\.[0-9]+)?$`)
  is unchanged, so `grok-yaml-standards@1.1+` and `@1.2+` strings
  already in the wild remain structurally valid.

---

## [1.2.0] — 2026-04-16

### Added
- **4 spec extensions**: `grok-tools`, `grok-deploy`,
  `grok-analytics`, `grok-ui`.
- Comprehensive JSON Schema validation — property-level schemas
  with enums, constraints, required fields, and descriptions for
  all 12 specs.
- `.github/ISSUE_TEMPLATE/` for community requests.
- Compatibility matrix in `README.md`.

### Changed
- Official X launch with `@grok` endorsement.

---

## [1.1.0] — 2026-03-XX

### Added
- `CONTRIBUTING.md`, `CONTRIBUTORS.md`, `ROADMAP.md`.
- Per-spec directories with `README.md`, `example.yaml`,
  `schema.md`, `usecases.md`, `security-considerations.md`,
  `x-trigger-examples.md`.

---

## [1.0.0] — 2026-02-XX

### Added
- Initial 8 core standards: `grok-config`, `grok-prompts`,
  `grok-agent`, `grok-workflow`, `grok-update`, `grok-test`,
  `grok-docs`, `grok-security`.
