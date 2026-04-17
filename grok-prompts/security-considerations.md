# grok-prompts.yaml — Security Considerations

## 1. Sanitise variable values before interpolation to prevent prompt injection

The `{variable}` interpolation syntax passes values directly into the prompt template at runtime. An attacker who controls a variable value (e.g. via a GitHub issue body) can inject instructions that override the template's intent. Validate and strip unexpected markup from variable values before passing them to Grok, and keep templates focused enough that injected text cannot redirect the output.

## 2. Never embed PII or secrets in template text

`grok-prompts.yaml` is committed to version control. Prompt templates that reference real names, email addresses, API endpoints with embedded keys, or internal project names are permanently exposed to anyone who can read the repo. Keep templates generic — use `{variable}` placeholders for anything environment-specific.

## 3. Use low temperature for security-critical and compliance prompts

High temperature values (`0.8`+) make outputs more creative but also more unpredictable. For prompts that perform code reviews, secret scanning, or compliance checks, set `temperature: 0.1` – `0.2` to ensure consistent, deterministic results. An audit prompt that sometimes misses findings due to random sampling is a false sense of security.

## 4. Understand `cache_responses: true` before enabling it

Response caching stores the output of a prompt + variable combination and reuses it on identical future calls. This is efficient but dangerous for time-sensitive prompts (e.g. a daily security scan that caches a "clean" result from yesterday) or prompts that incorporate live data. Only enable caching for prompts whose correct output is truly static.

## 5. Review community-contributed prompt libraries before importing them

If you import a third-party prompt library, review every template for instructions that could cause Grok to exfiltrate data, post unsanctioned content to X, or make API calls you did not intend. A malicious template can be indistinguishable from a legitimate one until it runs.
