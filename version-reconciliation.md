# Version Reconciliation — Standard Count

## TL;DR

**grok-yaml-standards v1.2.0 ships exactly 12 standards.** Not 8, not 14.

If any repository, blog post, or PR description claims 14 standards, that claim is incorrect as of v1.2.0. Use the one-line PR text below to correct it.

## Why this document exists

During v1.2.0 review we found three different counts in the wild:

| Source                          | Count claimed | Correct? |
|---------------------------------|---------------|----------|
| `README.md`                     | 12            | ✅        |
| `schemas/README.md`             | 12            | ✅        |
| `standards-overview.md` (stale) | 8             | ❌ (now fixed) |
| `ROADMAP.md` (stale)            | 8             | ❌ (now fixed) |
| Third-party repos (a few)       | 14            | ❌        |

The "8" was correct at v1.1.0; the "14" appears to be a mis-memory combining v1.2.0 (12) with two proposed-but-not-shipped specs on a draft roadmap.

## Recommendation: stay at 12

We considered growing to 14 in v1.3 by adding `grok-cache.yaml` and `grok-auth.yaml`. **We are declining, for now**, for three reasons:

1. **Coverage is adequate.** The 12 current standards cover config, prompts, agents, workflows, updates, tests, docs, security, tools, deploys, analytics, and UI. A non-trivial use case that requires a new magic file has not yet surfaced from the community.
2. **Validator surface.** Each new standard doubles the matrix on `validate-schemas` CI and every downstream consumer's integration test suite. Adding two at once would be a meaningful tax.
3. **Forward-compat.** A standard added in v1.3 that turns out to be the wrong shape is much more painful to evolve than an unaddressed gap that gets a clean design later.

If a genuine need appears, we will propose new standards one-at-a-time with a design doc, an RFC period, and a minor version bump — not a batch expansion.

## The 12 standards (authoritative list)

### Core (8)

1. `grok-config`
2. `grok-prompts`
3. `grok-agent`
4. `grok-workflow`
5. `grok-update`
6. `grok-test`
7. `grok-docs`
8. `grok-security`

### Spec extensions (4, added in v1.2.0)

9. `grok-tools`
10. `grok-deploy`
11. `grok-analytics`
12. `grok-ui`

## One-line PR text for other repos

Copy-paste into the PR title or a single-commit message in any downstream repo that currently claims 14:

> ```
> docs: correct standard count from 14 → 12 (grok-yaml-standards v1.2.0 ships 8 core + 4 spec extensions)
> ```

And for the PR body, if one is needed:

> v1.2.0 of `grok-yaml-standards` ships exactly 12 standards: 8 core (`grok-config`, `grok-prompts`, `grok-agent`, `grok-workflow`, `grok-update`, `grok-test`, `grok-docs`, `grok-security`) plus 4 spec extensions added in v1.2.0 (`grok-tools`, `grok-deploy`, `grok-analytics`, `grok-ui`). See https://github.com/AgentMindCloud/grok-yaml-standards/blob/main/version-reconciliation.md.

## If you need to revisit this

File an issue labelled `discussion/new-standard` with:
- The use case that isn't covered by one of the existing 12.
- Why it needs its own file rather than a section under an existing standard.
- A sketch of the YAML shape.

We will triage within one release cycle.
