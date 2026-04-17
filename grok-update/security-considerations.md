# grok-update.yaml — Security Considerations

## 1. Never combine `auto_commit: true` with `require_approval: false` on public repos

This combination allows Grok to push changes directly to your default branch without any human review. On a public repository, this means a compromised update job or a malicious source URL could silently modify your codebase, documentation, or configuration files. Always set `require_approval: true` on any job with `auto_commit: true`.

## 2. Scope `sources` globs carefully to exclude secrets and credentials

A glob like `"**/*"` will include `.env` files, private key files, and anything else in the repository as update sources. Grok will read and potentially modify these files. Use explicit paths (`README.md`, `docs/`) or add exclusion patterns, and never include `**/.env`, `**/secrets/**`, or `**/*.pem` in your sources list.

## 3. The `security_patch` action should always require human approval before merging

Automatic dependency patching is valuable, but a security patch can introduce breaking changes, alter behaviour, or in rare cases be itself a supply-chain compromise. Set `require_approval: true` specifically for jobs that include `security_patch` in their actions, even if other jobs in the same file auto-commit.

## 4. Stagger `schedule_cron` jobs to avoid hammering external APIs

Multiple update jobs that run simultaneously and each call external APIs (research sources, package registries, translation providers) can trigger rate-limit responses that block legitimate CI runs. Space cron schedules at least 10–15 minutes apart and set the lowest `frequency` that still meets your freshness requirements.

## 5. Never auto-commit directly to main or production branches

The `branch` field defaults to the repository default branch (typically `main`). An update job with `auto_commit: true` that targets `main` can bypass branch protection rules that normally require PR review. Set `branch` to a dedicated update branch (e.g. `grok-updates`) and let branch protection rules enforce the PR flow from there to `main`.
