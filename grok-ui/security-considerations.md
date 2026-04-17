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
