# grok-voice.yaml — X Trigger Examples

Drop any of these trigger comments into a GitHub issue, PR description, or commit message, then tag `@grok`.

---

## Trigger 1 — Start the voice session
```
@grok voice start
```
Opens the voice session using the `input.source` configured in `.grok/grok-voice.yaml` and wires the full STT → intent → agent → TTS pipeline.

---

## Trigger 2 — Show voice session status
```
@grok voice status
```
Prints current pipeline stage, end-to-end latency versus `latency_budget_ms`, active privacy mode, and any retries consumed from the fallback budget.

---

## Trigger 3 — Transcribe an audio file
```
@grok voice transcribe path/to/clip.wav
```
Runs the `stt` step only against the referenced file and returns the transcript, honoring the configured `retain_transcript` and `retain_audio` privacy flags.

---

## Trigger 4 — Switch voice output
```
@grok voice switch rachel
@grok voice switch speed:1.25
```
Hot-swaps `voice.output.voice_id` or `voice.output.speed` without restarting the session. Changes persist to `.grok/grok-voice.yaml` on confirmation.

---

## Trigger 5 — End voice session and purge audio
```
@grok voice end --purge-audio
```
Stops the current session, flushes any in-flight TTS audio, and deletes retained audio immediately regardless of `audio_retention_days`. Transcripts follow their configured retention.
