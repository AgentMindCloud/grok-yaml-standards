<div align="center">
  <h1>grok-yaml-standards</h1>
  <p>Modular YAML extensions for Grok-native agents</p>

  [![Spec: v1.2.0](https://img.shields.io/badge/spec-v1.2.0-blue.svg)](CHANGELOG.md)
  [![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
  [![Compatible: xAI SDK](https://img.shields.io/badge/compatible-xAI%20SDK-FF6B00.svg)](https://docs.x.ai)
  [![Compatible: grok-install](https://img.shields.io/badge/compatible-grok--install%401.0%2B-00B300.svg)](https://github.com/agentmindcloud/grok-install)
  [![Compatible: LiteLLM](https://img.shields.io/badge/compatible-LiteLLM-7C3AED.svg)](https://github.com/BerriAI/litellm)
  [![CI](https://img.shields.io/badge/CI-passing-brightgreen.svg)](https://github.com/agentmindcloud/grok-yaml-standards/actions)

  [**Quickstart**](#quickstart) · [**Spec Files**](#the-grok-folder) ·
  [**Tool Registry**](#tool-registry) · [**Security**](#security) ·
  [**Changelog**](CHANGELOG.md)
</div>

---

## What Is This?

Drop a `.grok/` folder into any repo and it becomes Grok-native.
This library defines modular YAML specs that extend `grok-install.yaml`:
agent definitions, workflows, security policies, prompts, and tool configurations.

Compatible with the official xAI SDK, LiteLLM, and Semantic Kernel.
Used by the `grok-install` runtime to power agents on X.

---

## Quickstart

```bash
# Copy the starter templates into your repo
cp -r .grok/ /your/repo/.grok/

# Or fetch a single spec
curl -LO https://raw.githubusercontent.com/agentmindcloud/grok-yaml-standards/main/.grok/grok-agent.yaml
mv grok-agent.yaml /your/repo/.grok/grok-agent.yaml

# Then tag @grok in any issue or PR comment to activate
```

---

## The `.grok/` Folder

| File | Purpose | Required? |
|------|---------|-----------|
| [`grok-agent.yaml`](.grok/grok-agent.yaml) | Define named agents — tools, memory, model, safety profile | For agents |
| [`grok-workflow.yaml`](.grok/grok-workflow.yaml) | Multi-step workflow pipelines with conditions and retry logic | For complex flows |
| [`grok-security.yaml`](.grok/grok-security.yaml) | Permissions, rate limits, scan policies, safety profile | Recommended |
| [`grok-prompts.yaml`](.grok/grok-prompts.yaml) | Reusable prompt templates — system prompts, temperature, reasoning mode | Recommended |
| [`grok-config.yaml`](.grok/grok-config.yaml) | Global defaults — model, language, privacy, shortcuts | Optional |
| [`grok-tools.yaml`](.grok/grok-tools.yaml) | Tool registry — typed signatures, permissions, rate limits | For custom tools |

> **Advanced examples** for multi-agent orchestration, parallel workflows, and research security
> profiles are in `.grok/*.advanced.yaml`. Full spec documentation lives in each
> [`grok-*/`](grok-agent/) subfolder.

The library also ships four spec extensions added in v1.2.0:
[`grok-deploy.yaml`](grok-deploy/),
[`grok-update.yaml`](grok-update/),
[`grok-analytics.yaml`](grok-analytics/), and
[`grok-ui.yaml`](grok-ui/).

---

## Tool Registry

[`grok-tools.yaml`](grok-tools/) is the formal tool registry for every built-in tool.
Each entry carries a full JSON Schema for inputs and outputs, error codes, security notes,
and per-tool rate limits. Agents reference tools by key — if a key isn't in the registry,
the agent won't call it.

Browse the 17 built-in tools across 7 categories in [`grok-tools/schema.md`](grok-tools/schema.md).

---

## Security

All security considerations in this library are **defensive**. The specs help teams:

- Prevent credential leaks with pre-commit secret scanning (`grok-security.yaml`)
- Enforce least-privilege tool access for agents (`grok-tools.yaml`, `safety_profile`)
- Guard against prompt injection via `key_constraints` and static `system_prompt` layers
- Audit AI-generated content before it reaches X (`approval_required` in `grok-workflow.yaml`)

This library never enables attacks on xAI, Grok, or the X platform.
Full threat model: [`SECURITY.md`](SECURITY.md).

---

## Ecosystem Integration

| Project | What it does |
|---------|-------------|
| [`grok-install`](https://github.com/agentmindcloud/grok-install) | The YAML standard this library extends — foundation layer |
| [`grok-install-cli`](https://github.com/agentmindcloud/grok-install-cli) | CLI runtime that reads `.grok/` and activates features |
| [`awesome-grok-agents`](https://github.com/agentmindcloud/awesome-grok-agents) | Community-built agents using these specs |
| [xAI SDK docs](https://docs.x.ai) | Official SDK this library maps to |

### SDK Field Mapping

| grok-yaml field | xAI SDK | LiteLLM | Semantic Kernel |
|-----------------|---------|---------|-----------------|
| `default_model` | `model` in `CreateChatCompletionRequest` | `model="xai/grok-4"` | `OpenAIPromptExecutionSettings.ModelId` |
| `temperature` | `temperature` | `temperature=` | `OpenAIPromptExecutionSettings.Temperature` |
| `max_tokens` | `max_tokens` | `max_tokens=` | `OpenAIPromptExecutionSettings.MaxTokens` |
| `stream_responses` | `stream=True` | `stream=True` | `StreamingChatMessageContent` |
| `reasoning_depth` | `reasoning_effort` ("low"/"medium"/"high") | N/A (model-level) | N/A |
| `tools[]` | `tools` array in request | `tools=` list of function dicts | `KernelPlugin` methods |
| `system_prompt` | `messages[{role:"system"}]` | `messages=` system entry | system message in `ChatHistory` |

Full per-spec mappings in each spec's `schema.md` under **Cross-References**.

---

## JSON Schema Validation

All 12 specs ship a JSON Schema (draft/2020-12) in [`/schemas/`](schemas/).

Add live VS Code validation:

```json
{
  "yaml.schemas": {
    "https://raw.githubusercontent.com/agentmindcloud/grok-yaml-standards/main/schemas/grok-agent.json": ".grok/grok-agent.yaml",
    "https://raw.githubusercontent.com/agentmindcloud/grok-yaml-standards/main/schemas/grok-workflow.json": ".grok/grok-workflow.yaml",
    "https://raw.githubusercontent.com/agentmindcloud/grok-yaml-standards/main/schemas/grok-security.json": ".grok/grok-security.yaml",
    "https://raw.githubusercontent.com/agentmindcloud/grok-yaml-standards/main/schemas/grok-prompts.json": ".grok/grok-prompts.yaml",
    "https://raw.githubusercontent.com/agentmindcloud/grok-yaml-standards/main/schemas/grok-config.json": ".grok/grok-config.yaml",
    "https://raw.githubusercontent.com/agentmindcloud/grok-yaml-standards/main/schemas/grok-tools.json": ".grok/grok-tools.yaml"
  }
}
```

---

## What's New in v1.2.0

See [**CHANGELOG.md**](CHANGELOG.md) for the full version history and [**LAUNCH.md**](LAUNCH.md) for the official launch notes and @grok endorsement.

Highlights: 4 new spec extensions (grok-tools, grok-deploy, grok-analytics, grok-ui),
JSON Schema upgraded to draft/2020-12, advanced `.grok/*.advanced.yaml` templates,
comprehensive `schema.md` field references with SDK mapping tables for all 12 specs.

---

## Contributors

- **[@JanSol0s](https://x.com/JanSol0s)** — Founder & Maintainer

*(Open a PR to add your name ⭐)*

---

**v1.2.0** · `grok-install.yaml@1.0+` · Apache 2.0 · [Launched on X April 16, 2026](https://x.com/JanSol0s/status/2044691252327993364)
