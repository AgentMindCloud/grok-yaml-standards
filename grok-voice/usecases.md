# grok-voice.yaml — Use Cases

## 1. Hands-free pair programming
`source: mic` with `vad: webrtc`, `language: en-US`, and a pipeline of `whisper → grok → CodePartner → elevenlabs`. `latency_budget_ms: 1500` keeps responses snappy enough to feel conversational. `retain_transcript: true` builds a searchable log of every coding session.

## 2. Voice-driven support triage
`source: stream` pulling from a call-centre WebRTC feed. The `intent` step routes into the `TriageRouter` agent defined in `grok-swarm.yaml`, which dispatches to the right specialist. `retain_audio: false` and `retain_transcript: false` for regulated environments where recording is disallowed.

## 3. Accessibility layer for visually impaired contributors
`output.speed: 1.25` and `tts_provider: elevenlabs` with a natural-sounding `voice_id` reads GitHub issues, PR descriptions, and code-review comments aloud. `fallback.on_tts_failure: cached_audio` means common UI strings keep working during TTS outages.

## 4. Podcast pre-production
`source: file` with pre-recorded `wav` inputs. The pipeline runs STT only (no TTS step), producing show notes and topic segmentation via the `DocsWriter` agent. `retain_audio: true` with `audio_retention_days: 180` keeps source audio available for re-cutting.

## 5. Live-demo narration during X Spaces
`source: stream` from the active Space, pipeline ends at `intent` (no TTS back into the Space). Detected topics trigger `grok-workflow` runs so the demo's actions follow the narration automatically. `latency_budget_ms: 800` for tight lip-sync between words and on-screen actions.
