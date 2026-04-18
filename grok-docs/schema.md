# grok-docs.yaml — Complete Field Reference

Version: 1.2.0
JSON Schema: `schemas/grok-docs.json`

---

## Root Object

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `version` | string | ✅ | — | pattern: `^\d+\.\d+\.\d+$` | Spec version this file targets (e.g. `"1.2.0"`). |
| `author` | string | ✅ | — | pattern: `^@[A-Za-z0-9_]{1,50}$` | X handle of the config owner, prefixed with `@`. |
| `compatibility` | string[] | ✅ | — | minItems: 1; uniqueItems | Platform specs this file is compatible with. |
| `docs` | object | ✅ | — | minProperties: 1 | Named documentation target definitions. Each key is a target ID used in `@grok docs <Name>`. |

---

## Docs Target Object

### Example

```yaml
docs:
  AutoREADME:
    target: "README.md"             # must end in .md, .rst, .txt, or .html
    sections: ["hero", "features", "installation", "quickstart", "magic_triggers"]
    style: "exciting-professional"
    source_files: ["src/**/*.ts", "*.json"]   # explicit scope — never include .env
    include_code_samples: true
    update_on: ["pr_merged", "release"]       # never "push" for public-facing docs
    language: "en"
    table_of_contents: true
    max_length_words: 2000
```

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `target` | string | ✅ | — | pattern: `^[a-zA-Z0-9_./-]+\.(md\|rst\|txt\|html)$` | Output file path relative to repo root. Must end in a supported extension. |
| `sections` | string[] | ✅ | — | minItems: 1; enum items below | Ordered doc sections to generate. Composed top-to-bottom. |
| `style` | string | — | `"technical-clean"` | enum: `technical-clean`, `exciting-professional`, `minimal`, `comprehensive`, `tutorial`, `reference` | Writing style applied to the entire document. |
| `source_files` | string[] | — | `["**/*"]` | glob patterns | Files Grok analyses. Explicitly list source dirs; exclude `.env`, secrets, credentials. |
| `exclude_patterns` | string[] | — | `[]` | glob patterns | Files excluded even when matched by `source_files`. |
| `include_code_samples` | boolean | — | `false` | — | Include fenced code examples. Review auto-generated samples for hardcoded values before publish. |
| `include_diagrams` | boolean | — | `false` | — | Generate Mermaid diagrams for architecture and flow sections. |
| `update_on` | string[] | — | `["manual"]` | enum items: `push`, `pr_merged`, `release`, `manual`, `schedule`, `on_tag` | Events that trigger automatic regeneration. Avoid `push` for public-facing docs. |
| `language` | string | — | `"en"` | pattern: `^[a-z]{2}(-[A-Z]{2,4})?$` (BCP-47) | Output language. |
| `table_of_contents` | boolean | — | `false` | — | Prepend an auto-generated table of contents. |
| `max_length_words` | integer | — | — | minimum: 100; maximum: 50000 | Soft word-count limit for the generated document. |
| `enabled` | boolean | — | `true` | — | Set `false` to disable this target without removing its definition. |

---

## sections Enum

Sections are composed top-to-bottom in the order declared:

| Value | Generates |
|-------|-----------|
| `hero` | Project name, tagline, and badges |
| `features` | Bulleted feature highlights |
| `installation` | Step-by-step install instructions |
| `quickstart` | Minimal working example |
| `magic_triggers` | `@grok` trigger reference table |
| `configuration` | Config options with defaults |
| `api_reference` | Full API method/endpoint listing |
| `examples` | Extended code examples |
| `auth` | Authentication and authorisation guide |
| `endpoints` | REST/GraphQL endpoint listing |
| `changelog` | Version history (review before publishing — may contain internal ticket numbers) |
| `contributing` | Contribution guidelines |
| `license` | License summary |
| `faq` | Frequently asked questions |
| `troubleshooting` | Common errors and fixes |
| `architecture` | System design diagrams and explanations |
| `deployment` | Deployment instructions |
| `security` | Security policy summary |

---

## style Enum

| Value | Tone |
|-------|------|
| `technical-clean` | Precise, minimal prose; focuses on accuracy |
| `exciting-professional` | Energetic but polished; suited for public READMEs |
| `minimal` | Headers and code blocks only; no narrative prose |
| `comprehensive` | Long-form with full context and rationale |
| `tutorial` | Step-by-step learning style with explanations |
| `reference` | Dense, scannable; optimised for quick lookup |

---

## update_on Enum

| Value | Trigger |
|-------|---------|
| `push` | Every commit to the default branch. **Avoid for public-facing targets** — may expose WIP content. |
| `pr_merged` | After a PR is merged. Recommended for public docs. |
| `release` | After a GitHub release is published. |
| `manual` | Only via `@grok docs <Name>` comment. Default. |
| `schedule` | On a cron schedule configured in `grok-update.yaml`. |
| `on_tag` | When a git tag is pushed. |
