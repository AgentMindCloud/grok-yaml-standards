# grok-voice

**File:** `specs/grok-voice.yaml`  
**Schema:** [`schemas/grok-voice.schema.json`](../schemas/grok-voice.schema.json)  
**Introduced:** grok-yaml-standards v2.0.0  
**Requires:** grok@4.20+

---

## Overview

`grok-voice.yaml` configures Grok 4.20's voice API — speech-to-text (STT) input and text-to-speech (TTS) output. It controls model selection, voice identity, optional features, fallback behaviour, and safety limits.

**Required X OAuth2 scopes** (add to `grok-security.yaml` → `permissions.x_scopes`):
- `voice.read` — read voice session state and transcripts
- `voice.write` — initiate voice sessions and post audio

---

## Models

| Model | Direction | Notes |
|-------|-----------|-------|
| `grok-voice-stt-latest` | Speech → Text | Rolling-latest model; always use this identifier |
| `grok-voice-tts-natural` | Text → Speech | Prosody and emotion modelling; preferred for all TTS |

---

## Features

Optional capabilities. Only enable features you need — each adds latency.

| Feature | Effect |
|---------|--------|
| `real-time-conversation` | Bidirectional streaming; agent can respond while user is still speaking |
| `emotion-aware` | TTS adjusts tone and pacing to match the sentiment of the output text |
| `multi-speaker` | Session handles multiple concurrent speakers |
| `speaker-diarization` | STT transcript labels each speaker with an ID (requires `multi-speaker`) |

---

## Fields

| Field | Type | Default | Notes |
|-------|------|---------|-------|
| `enabled` | boolean | `false` | Master switch. No voice API calls when false. |
| `stt_model` | string | `grok-voice-stt-latest` | Only valid value currently |
| `tts_model` | string | `grok-voice-tts-natural` | Only valid value currently |
| `voice_id` | string | — | From Grok voices catalog API; omit for model default |
| `features` | array | `[]` | Subset of the four feature enum values |
| `fallback` | string | `text-only` | `text-only / queue / error` |
| `safety.profanity_filter` | boolean | `true` | Applies to TTS output only |
| `safety.max_duration_seconds` | integer | `300` | Hard cap per voice session (1–3600) |

---

## Fallback Behaviour

| Value | What happens |
|-------|-------------|
| `text-only` | Voice quietly disabled; agent continues in text mode. **Recommended for production.** |
| `queue` | Voice request buffered; retried when API recovers. Use for async/batch workflows. |
| `error` | Exception raised and surfaced to caller. Use only in strict testing environments. |

---

## Minimal Example

```yaml
version: "2.0.0"
author: "@yourhandle"
compatibility:
  - "grok@4.20+"
  - "grok-yaml-standards@2.0+"

voice:
  enabled: true
  stt_model: "grok-voice-stt-latest"
  tts_model: "grok-voice-tts-natural"
  features:
    - "real-time-conversation"
  fallback: "text-only"
  safety:
    profanity_filter: true
    max_duration_seconds: 300
```

See [`specs/grok-voice.yaml`](../specs/grok-voice.yaml) for the full annotated reference.

---

## Real-Time Conversation Pattern

Pair `grok-voice.yaml` with a `grok-agent.yaml` agent that has `memory: "session_only"` for a stateless voice assistant:

```yaml
# .grok/grok-agent.yaml (excerpt)
agents:
  VoiceAssistant:
    model_override: "grok-4.20"
    tools: ["recall_memory"]
    memory: "session_only"
    safety_profile: "strict"
```

```yaml
# specs/grok-voice.yaml (excerpt)
voice:
  enabled: true
  features:
    - "real-time-conversation"
    - "emotion-aware"
  fallback: "text-only"
```

---

## Cross-References

**Depends On:**
- [`grok-security.yaml`](../grok-security/schema.md) — `x_scopes` must include `voice.read` and `voice.write`
- [`grok-config.yaml`](../grok-config/schema.md) — `default_model` must be a Grok 4.20 variant when voice is enabled

**Used By:**
- [`grok-swarm.yaml`](grok-swarm.md) — swarm agents with `role: custom` and `model: grok-voice-tts-natural` use this config for `voice_synthesis` tool calls
- [`grok-workflow.yaml`](../grok-workflow/schema.md) — workflow steps can call `action: "voice_synthesis"` when voice is enabled

**Grok 4.20 SDK Mapping:**

| YAML field | xAI SDK param |
|-----------|--------------|
| `stt_model` | `model` in `/v1/audio/transcriptions` request |
| `tts_model` | `model` in `/v1/audio/speech` request |
| `voice_id` | `voice` in `/v1/audio/speech` request |
| `features` | `stream: true` for `real-time-conversation`; `emotion_mode: true` for `emotion-aware` |
| `safety.max_duration_seconds` | `max_seconds` session param |
