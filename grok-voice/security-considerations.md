# grok-voice.yaml — Security Considerations

## 1. Audio retention is a recording — treat it as regulated data
`retain_audio: true` produces an audio archive that in many jurisdictions triggers wiretap, two-party-consent, or biometric-data regulation. Default to `retain_audio: false` and only enable it after explicit, logged user consent. `audio_retention_days` must be set alongside any `true` value — no indefinite retention.

## 2. Transcripts often contain PII the speaker did not realise they disclosed
Even when `retain_audio: false`, a `retain_transcript: true` setting captures names, addresses, credentials, and medical details spoken aloud. Route transcripts through the same PII-redaction pipeline used by `grok-analytics.yaml` before persisting.

## 3. Wake-phrase listeners are always-on microphones
Any `source: mic` configuration implies a continuous listening loop. Ensure the host OS permission prompt fires, and require the user to explicitly enable voice (never via template default). In shared spaces, recommend `vad: webrtc` with tight sensitivity to reduce accidental capture of nearby conversations.

## 4. TTS replies can exfiltrate context audibly
If the `agent` step pulls in secrets, API responses, or other sensitive strings, the `tts` step will read them aloud — potentially in a shared physical space. Agents used in voice pipelines should have `permissions` reduced to the minimum needed, and sensitive outputs should be filtered before reaching the TTS step.

## 5. Third-party STT / TTS providers see every interaction
`tts_provider: elevenlabs` or `stt: whisper` (hosted) sends audio and text to a third party subject to their terms. Review provider data-processing agreements before adopting. For regulated contexts prefer `provider: whisper` (self-hosted) or `provider: coqui` to keep audio on-prem.
