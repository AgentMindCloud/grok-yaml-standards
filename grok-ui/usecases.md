# grok-ui.yaml — Use Cases

## 1. Hands-free testing during live coding sessions
Enable `voice_commands` with `wake_phrase: "hey grok"` and a `"run tests"` command mapped to `grok-test`. During a screen share or pair-programming session, say "hey grok, run tests" to kick off the `CodeQuality` suite without stopping to type a command.

## 2. Team-wide dashboard standardisation
Commit `.grok/grok-ui.yaml` to the repository with a canonical dashboard layout. Every engineer who installs the Grok IDE extension automatically gets the same agent status, test results, and deployment history widgets — eliminating the "works on my machine" dashboard problem.

## 3. Keyboard shortcut profiles for different roles
Backend engineers bind `ctrl+shift+t` to `grok-test CodeQuality`. Front-end engineers override it with `grok-test AccessibilityCheck`. Both profiles live in the same file under different YAML anchors and are activated per-user via `grok-config.yaml` shortcuts.

## 4. Security-first dark mode for sensitive environments
Set `theme: high-contrast` and disable the `analytics_pulse` widget for compliance environments where screen content must stay readable under red-team observation and no analytics data should be visible on screen.

## 5. One-click release workflow via keyboard shortcut
Map `ctrl+shift+r` to `grok-workflow ReleasePipeline`. A single keystroke in the IDE triggers tests, docs regeneration, release notes, and the X announcement — the complete release workflow without leaving the editor.
