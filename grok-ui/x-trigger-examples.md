# grok-ui.yaml — X Trigger Examples

Drop any of these trigger comments into a GitHub issue, PR description, or commit message, then tag `@grok`.

---

## Trigger 1 — Show UI configuration status
```
@grok ui status
```
Prints the active theme, locale, dashboard widget list, and voice command state from `.grok/grok-ui.yaml`.

---

## Trigger 2 — Reload UI config
```
@grok ui reload
```
Hot-reloads `.grok/grok-ui.yaml` in all connected Grok IDE extension instances without requiring a restart.

---

## Trigger 3 — List keyboard shortcuts
```
@grok ui shortcuts
```
Prints a formatted table of all configured keyboard shortcuts with their bound actions.

---

## Trigger 4 — Toggle dark mode
```
@grok ui theme dark
```
Switches the active theme to `dark` for the current session. Persists when committed to `.grok/grok-ui.yaml`.

---

## Trigger 5 — Enable or disable voice commands
```
@grok ui voice on
@grok ui voice off
```
Toggles voice command listening without editing the YAML file directly. The state is saved back to `.grok/grok-ui.yaml` on confirmation.
