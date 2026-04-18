# Changelog

All notable changes to grok-yaml-standards are documented here.
Versions follow [Semantic Versioning](https://semver.org/).

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
