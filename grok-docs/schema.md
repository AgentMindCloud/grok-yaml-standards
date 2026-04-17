# grok-docs.yaml Field Reference

Full JSON Schema: [`/schemas/grok-docs.json`](../schemas/grok-docs.json)

---

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this docs config file (e.g. `"1.2.0"`). |
| `author` | `string` | ✅ | X handle of the config owner, prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `docs` | `object` | ✅ | Named documentation target definitions. At least one entry required. |

---

## docs entries

Each key becomes the target identifier used in `@grok docs <Name>` triggers.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `target` | `string` | ✅ | Output file path relative to repo root. Must end in `.md`, `.rst`, `.txt`, or `.html`. |
| `sections` | `string[]` | ✅ | Ordered list of document sections to generate. At least one required. |
| `style` | `string` | `"technical-clean"` | Writing style preset applied to the entire document. |
| `update_on` | `string[]` | — | Events that trigger automatic regeneration. |
| `include_code_samples` | `boolean` | `false` | Include fenced code examples in API reference and quickstart sections. |
| `source_files` | `string[]` | — | Glob patterns selecting source files Grok analyses. Defaults to entire repo. |
| `language` | `string` | `"en"` | BCP-47 language tag for the output (e.g. `"en"`, `"fr"`, `"de"`). |
| `table_of_contents` | `boolean` | `false` | Prepend an auto-generated table of contents. |
| `max_length_words` | `integer` | — | Soft word-count limit. Range: `100` – `50000`. |
| `enabled` | `boolean` | `true` | Set to `false` to disable without removing the definition. |

---

## target filename pattern

`^[a-zA-Z0-9_./-]+\.(md|rst|txt|html)$`

**Valid examples:** `README.md` · `docs/API.md` · `docs/guide.rst` · `public/index.html`

---

## sections enum values

Sections are composed top-to-bottom in the order listed:

| Value | Generates |
|-------|-----------|
| `hero` | Project name, tagline, and badges |
| `features` | Bulleted feature highlights |
| `installation` | Step-by-step install instructions |
| `quickstart` | Minimal working example |
| `magic_triggers` | `@grok` trigger reference table |
| `configuration` | All config options with defaults |
| `api_reference` | Full API method/endpoint listing |
| `examples` | Extended code examples |
| `auth` | Authentication and authorisation guide |
| `endpoints` | REST/GraphQL endpoint listing |
| `changelog` | Version history |
| `contributing` | Contribution guidelines |
| `license` | License summary |
| `faq` | Frequently asked questions |
| `troubleshooting` | Common errors and fixes |
| `architecture` | System design diagrams and explanations |
| `deployment` | Deployment instructions |
| `security` | Security policy summary |

---

## style enum values

| Value | Tone |
|-------|------|
| `technical-clean` | Precise, minimal prose; focuses on accuracy |
| `exciting-professional` | Energetic but polished; suited for public READMEs |
| `minimal` | Headers and code blocks only; no narrative prose |
| `comprehensive` | Long-form with full context and rationale |
| `tutorial` | Step-by-step learning style with explanations |
| `reference` | Dense, scannable; optimised for quick lookup |

---

## update_on enum values

`push` · `pr_merged` · `release` · `manual` · `schedule` · `on_tag`
