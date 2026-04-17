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

---

## Threat Model

This spec defines scheduled auto-update jobs on documentation, dependencies, and content. The threats we defend against are:

**T1 — Credential Exposure**
Attack: A contributor adds a hardcoded API key (e.g. `xai-...`) to a YAML template. Once merged to an open repo, the key is scraped within minutes.
Defense: The JSON Schema rejects strings matching `/^xai-[a-zA-Z0-9]{32,}$/` outside env-reference fields. CI runs gitleaks on every push. Secrets must use `${ENV_VAR}` references.

**T2 — Prompt Injection via Tool Output**
Attack: An update job reads an external source (research article, dependency changelog) containing injected instructions that redirect the job to modify unrelated files.
Defense: Tool output is wrapped in XML delimiters before insertion. The job's system prompt treats external content as untrusted data.

**T3 — Path Traversal in Filesystem Tools**
Attack: An update job's `target:` resolves to `"../../.env"` and overwrites a secrets file.
Defense: Path parameters are validated against `^(?!.*\.\.)[^/].*$` before execution. Target paths must be within the repository root.

**T4 — Over-Permissioned Actions**
Attack: An update job has `auto_commit: true` + `require_approval: false` on a public repo, letting a compromised research source push arbitrary code to `main`.
Defense: Schema validator warns (and CI fails) on any job combining `auto_commit: true` with `require_approval: false` on a default branch. Production branches require explicit approval.

**T5 — Rate Limit Abuse**
Attack: Multiple update jobs with overlapping `schedule_cron` values fire together and hammer an external API.
Defense: Runtime staggers concurrent jobs by a randomised jitter (up to 5 min) and enforces per-provider rate caps.

**T6 — Supply Chain via Remote Tool Import**
Attack: An update job imports research from a compromised URL that injects malicious dependency versions.
Defense: External source URLs must be whitelisted in `grok-security.yaml`. `security_patch` actions always require human approval before merging.

### Out of Scope for This Spec

- Vulnerabilities in the xAI API or the Grok model itself — report to xAI's security team.
- X platform vulnerabilities — report to X's security team.
- Host OS, container runtime, or network security — handled by the deployment platform.

### Reporting Security Issues

See the repository [`SECURITY.md`](../SECURITY.md). Never file a public issue for a suspected vulnerability; use a private GitHub Security Advisory or the email listed in `SECURITY.md`.
