---
title: grok-voice
description: Voice-first interface bindings
image: /docs/posters/grok-voice.png
---

# grok-voice.yaml

**What problem it solves**
`grok-ui.yaml` has a lightweight `voice_commands` block for wake-phrase → action bindings, but real voice interactions need a full pipeline: input capture with voice-activity detection, speech-to-text, intent routing into an agent, text-to-speech, a latency budget, and explicit privacy controls on audio retention. `grok-voice.yaml` is the dedicated voice spec that makes all of that declarative.

**X Trigger Example**
`@grok voice start` — opens the voice session using the configured input source
`@grok voice status` — reports latency, current pipeline stage, and active privacy mode

**Compatible with**
`grok-install.yaml@1.0+` · `grok@2026.4+` · `grok-yaml-standards@2.0+`

**Benefits**
- Complete STT → intent → agent → TTS pipeline defined as ordered, typed steps
- Explicit `latency_budget_ms` so the runtime can downgrade quality before it misses the budget
- Separate `retain_audio` and `retain_transcript` privacy flags — audio and text have different risk profiles
- `fallback` handles STT failures, TTS failures, and timeouts distinctly instead of collapsing them into one catch-all
- New in `grok-yaml-standards@2.0` alongside `grok-swarm.yaml` as part of the 14-spec set
