# grok-ui.yaml — Security Considerations

## 1. Voice commands require microphone permission — request explicitly
`voice_commands.enabled: true` triggers a browser/OS microphone permission prompt. Ensure the user has consciously granted this permission. Never silently enable voice commands via a template default.

## 2. Wake-phrase eavesdropping risk
Any always-on wake-phrase listener increases the risk of accidental command triggering in shared spaces. In security-sensitive or open-plan environments, set `enabled: false` for voice commands and rely on keyboard shortcuts instead.

## 3. Keyboard shortcuts should not bypass approval gates
A keyboard shortcut mapped to `grok-deploy production` does not bypass the `require_approval` check defined in `grok-deploy.yaml`. Shortcuts are UI convenience — all security gates remain enforced at the action level, not the input level.

## 4. Dashboard widgets display real-time security data
The `security_summary` widget can surface unresolved vulnerability details on screen. In shared-screen contexts (presentations, pair programming), review which widgets are visible and filter `alert_level` to avoid displaying unpatched CVE details publicly.

## 5. Do not expose the UI config to untrusted contributors
`grok-ui.yaml` can define keyboard shortcuts that invoke deploy and execute actions. Treat pull requests that modify this file with the same scrutiny as changes to CI/CD configuration.

---

## Threat Model

This spec defines dashboards, keyboard shortcuts, and voice-command surfaces. The threats we defend against are:

**T1 — Credential Exposure**
Attack: A shortcut or widget embeds a literal API key for a third-party integration.
Defense: The JSON Schema rejects strings matching known credential patterns in shortcut definitions. All integrations must reference secrets by name.

**T2 — Prompt Injection via Tool Output**
Attack: A voice command transcription is treated as a direct instruction, allowing a crafted audio clip to trigger unintended actions.
Defense: Voice transcriptions are wrapped in XML delimiters; the command router parses them as natural-language intent, not as code-level instructions. Unmatched intents require user confirmation.

**T3 — Path Traversal in Filesystem Tools**
Attack: A shortcut's target path escapes the workspace.
Defense: All shortcut-referenced paths are validated against `^(?!.*\.\.)[^/].*$`.

**T4 — Over-Permissioned Actions**
Attack: A keyboard shortcut bound to `grok-deploy production` attempts to bypass the approval gate for convenience.
Defense: Approval gates are enforced at the action level (`grok-deploy.yaml`), not at the input level. A shortcut is a way to **request** an action, never to bypass its gates. Schema validation warns if a shortcut maps directly to a destructive action without a confirmation modal.

**T5 — Rate Limit Abuse**
Attack: A stuck keyboard shortcut fires an action thousands of times.
Defense: Per-shortcut debouncing (250 ms by default); invocations within the debounce window are discarded.

**T6 — Supply Chain via Remote Tool Import**
Attack: A dashboard widget loads its data from a compromised third-party URL.
Defense: Widget data sources must be whitelisted in `grok-security.yaml`.

### Out of Scope for This Spec

- Vulnerabilities in the xAI API or the Grok model itself — report to xAI's security team.
- X platform vulnerabilities — report to X's security team.
- Host OS, container runtime, or network security — handled by the deployment platform.

### Reporting Security Issues

See the repository [`SECURITY.md`](../SECURITY.md). Never file a public issue for a suspected vulnerability; use a private GitHub Security Advisory or the email listed in `SECURITY.md`.
