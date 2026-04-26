---
title: grok-analytics
description: Opt-in telemetry with PII controls
image: /docs/posters/grok-analytics.png
---

# grok-analytics.yaml

**What problem it solves**  
Grok usage telemetry is either all-or-nothing: either you share everything with xAI or you share nothing. `grok-analytics.yaml` gives teams fine-grained, opt-in control over exactly which events are tracked, which properties are collected, which provider receives the data, and how long it is retained — all declared transparently in version-controlled YAML.

**X Trigger Example**  
`@grok analytics report` — generates a usage summary from the last 30 days  
`@grok analytics reset` — clears locally cached analytics data

**Compatible with**  
`grok-install.yaml@1.0+` · `grok@2026.4+` · `grok-yaml-standards@1.2+`

**Benefits**  
- Opt-in by default — no data leaves the repo unless `enabled: true` is set explicitly  
- PII-safe event design: every event declares `pii_safe: true/false` so reviewers can audit at a glance  
- Provider-agnostic: works with PostHog, Mixpanel, Amplitude, or a custom webhook  
- Sampling rate and role-based opt-out give organisations GDPR and CCPA compliance levers without code changes
