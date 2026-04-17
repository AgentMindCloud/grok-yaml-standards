# grok-ui.yaml

**What problem it solves**  
Interacting with Grok requires typing @grok commands in text fields. `grok-ui.yaml` extends that interaction model with voice commands, a configurable dashboard of live widgets, keyboard shortcuts, and theme settings — all declared in YAML so teams can standardise their Grok UI experience across every developer's setup without per-machine configuration.

**X Trigger Example**  
`@grok ui status` — shows the active dashboard and voice command configuration  
`@grok ui reload` — reloads the UI config from `.grok/grok-ui.yaml` without restarting

**Compatible with**  
`grok-install.yaml@1.0+` · `grok@2026.4+` · `grok-yaml-standards@1.2+`

**Benefits**  
- Voice commands enable hands-free Grok invocation during coding sessions  
- Dashboard widgets surface agent status, test results, and deploy health in real time  
- Keyboard shortcuts eliminate context-switching — trigger any @grok command without leaving the editor  
- Theme and locale settings ensure a consistent look and feel for every contributor
