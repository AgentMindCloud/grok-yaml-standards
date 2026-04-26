---
title: grok-config
description: Repo-wide model settings & defaults
image: /docs/posters/grok-config.png
---

# grok-config.yaml

**What problem it solves**  
Centralizes all Grok settings so every repo has consistent behavior.

**X Trigger Example**  
`@grok config` → Grok instantly respects this file.

**Benefits**  
- One source of truth for temperature, model, context  
- Forward-compatible with future Grok versions  
- Zero setup for X users
