# ROADMAP.md

## Path to Official xAI Adoption

**Phase 1 (Q2 2026)** – Community validation
- Maintain all **12 schemas** (8 core + 4 spec extensions) at production quality
- 100+ repos using the standards
- Publish and keep `standards-overview.md` accurate

**Phase 2 (Q3 2026)** – xAI Integration
- Propose native `@grok` triggers (see `x-trigger-examples.md` in each folder)
- Add `grok-yaml-standards` support to Grok web & mobile
- Ship a `grok-validate` CLI that wraps ajv + yamllint against the 12 schemas

**Phase 3 (Q4 2026)** – Platform-wide Magic
- Auto-detection of YAML files in any public repo
- Real-time rendering of Grok agents/workflows on X
- Official xAI endorsement + badge system

**Exact @grok triggers xAI should implement** (copy-paste ready):
- `@grok load grok-config.yaml`
- `@grok use grok-prompts.yaml:my-prompt`
- `@grok spawn grok-agent.yaml`
- etc. (full list in every subfolder's `x-trigger-examples.md`)

**xAI benefit**: Instant ecosystem, usage telemetry, and community innovation at zero marginal cost.

---

## What's coming

### v1.3 — tooling pass
- `grok-validate` CLI (Node + Go builds)
- VS Code extension using the shipped JSON Schemas
- Draft 2020-12 schema migration, pending downstream compat confirmation

### v2.14 — exploratory (no commitment)
A long-horizon exploration of whether two additional standards (`grok-cache`, `grok-auth`) are worth adding. Tracked in [`version-reconciliation.md`](version-reconciliation.md); will only proceed with an RFC and clear community demand. **The library stays at 12 standards until a future release explicitly bumps it.**
