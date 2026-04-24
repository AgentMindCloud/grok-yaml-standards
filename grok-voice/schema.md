# grok-voice.yaml Field Reference

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this voice config file (e.g. `"2.0.0"`). |
| `author` | `string` | ✅ | X handle prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `voice` | `object` | ✅ | Voice interface definition (see below). |

## voice fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `string` | ✅ | Stable machine identifier for this voice interface. |
| `name` | `string` | ✅ | Human-readable name shown in dashboards. |
| `version` | `string` | ✅ | Semver of the voice definition itself. |
| `input` | `object` | ✅ | Audio input configuration (see below). |
| `output` | `object` | ✅ | TTS output configuration (see below). |
| `pipeline` | `object[]` | ✅ | Ordered pipeline steps (see below). |
| `latency_budget_ms` | `integer` | — | End-to-end latency target in milliseconds. Runtime may downgrade quality to stay under this. |
| `fallback` | `object` | — | Failure-handling policy for STT, TTS, and timeouts. |
| `privacy` | `object` | — | Audio and transcript retention controls. |
| `metadata` | `object` | — | Free-form map for tags, owners, lineage. |

## input fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `source` | `string` | ✅ | Audio source: `mic`, `stream`, `file`. |
| `format` | `string` | ✅ | Audio container / codec: `wav`, `mp3`, `ogg`, `flac`, `webm`, `pcm`. |
| `language` | `string` | ✅ | BCP-47 language code (e.g. `en-US`, `fr-FR`). |
| `vad` | `string` | — | Voice activity detection backend: `webrtc`, `silero`, `none`. Defaults to `webrtc`. |
| `sample_rate_hz` | `integer` | — | Sample rate for mic / stream sources. Typical: 16000 or 48000. |

## output fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `tts_provider` | `string` | ✅ | TTS provider: `elevenlabs`, `openai`, `azure`, `polly`, `google`, `coqui`, `custom`. |
| `voice_id` | `string` | ✅ | Provider-specific voice identifier. |
| `format` | `string` | ✅ | Output audio format: `mp3`, `wav`, `ogg`, `opus`, `pcm`. |
| `speed` | `number` | — | Playback speed multiplier (0.5–2.0). Defaults to `1.0`. |

## pipeline[] item fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `step` | `string` | ✅ | Pipeline stage: `stt`, `intent`, `agent`, `tts`, `filter`. |
| `provider` | `string` | — | Provider for the step (e.g. `whisper`, `grok`, `elevenlabs`). |
| `agent_id` | `string` | — | Agent to invoke when `step: agent`. Must match an id in `grok-agent.yaml`. |

## fallback fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `on_stt_failure` | `string` | — | `prompt_user`, `text_fallback`, `abort`. |
| `on_tts_failure` | `string` | — | `text_response`, `cached_audio`, `silent`, `abort`. |
| `on_timeout` | `string` | — | `abort`, `degrade`, `retry`. |
| `max_retries` | `integer` | — | Maximum retry attempts per stage. Defaults to `1`. |

## privacy fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `retain_audio` | `boolean` | ✅ | Persist raw audio after the session ends. |
| `retain_transcript` | `boolean` | ✅ | Persist the text transcript after the session ends. |
| `transcript_retention_days` | `integer` | — | Days to keep transcripts when `retain_transcript: true`. |
| `audio_retention_days` | `integer` | — | Days to keep audio when `retain_audio: true`. |
