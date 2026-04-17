# grok-analytics.yaml — X Trigger Examples

Drop any of these trigger comments into a GitHub issue, PR description, or commit message, then tag `@grok`.

---

## Trigger 1 — Generate a usage report
```
@grok analytics report
```
Produces a Markdown summary of the top triggered specs, most-used agents, workflow success rates, and security findings over the last 30 days.

---

## Trigger 2 — Show current analytics config
```
@grok analytics status
```
Prints the active provider, enabled events, sampling rate, and data retention policy from `.grok/grok-analytics.yaml`.

---

## Trigger 3 — Clear local analytics cache
```
@grok analytics reset
```
Deletes locally buffered analytics events that have not yet been flushed to the provider.

---

## Trigger 4 — Test provider connectivity
```
@grok analytics test
```
Sends a synthetic `grok_analytics_test` event to the configured provider and confirms it was received, without touching real event data.
