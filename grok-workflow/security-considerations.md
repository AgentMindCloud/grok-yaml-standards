# grok-workflow.yaml — Security Considerations

## 1. Require human approval gates on any step that writes, deploys, or publishes

Fully automated workflows that commit code, deploy to production, or post to X without a human checkpoint create a direct path from a malicious PR comment to a production incident. Add a manual approval step before any `deploy` or `publish_thread` action, especially in workflows triggered by external events like issue comments or PR labels.

## 2. Validate inputs before using them in `condition` expressions

The `condition` field is a JavaScript-style expression evaluated against prior step outputs. If any step output includes user-supplied content (e.g. the body of a GitHub issue), a crafted value could manipulate the condition logic and cause the workflow to skip security gates or execute unintended branches. Sanitise step outputs before referencing them in conditions.

## 3. `on_error: continue` can silently mask cascading failures

Using `continue` as an error strategy means a failing step is logged and skipped, but the workflow proceeds. In a security or release pipeline this can mean a failed security scan is silently bypassed, resulting in a deployment that should have been blocked. Use `stop` or `notify` as the default; only use `continue` for genuinely non-critical informational steps.

## 4. Use secret references, not literal values, in step `env` maps

The `env` map on a step passes environment variables to the action. Hardcoding credentials here is equivalent to hardcoding them in a CI script — they will appear in logs and in version control history. Always reference repository secrets (e.g. `${{ secrets.API_KEY }}`) rather than pasting values directly.

## 5. Avoid embedding sensitive data in `notify_on_complete` notifications

When `notify_on_complete: true`, Grok posts a workflow summary to X. Ensure that step output summaries do not include internal URLs, error messages containing file paths, stack traces, or any data that would be sensitive if posted publicly.

---

## Threat Model

This spec defines multi-step automation workflows. **T5 (Rate Limit Abuse) is the primary threat for this spec** — workflows are the most common source of accidental retry storms.

**T1 — Credential Exposure**
Attack: A contributor hardcodes an API key in a step `env:` map. Once merged, the key is scraped and abused.
Defense: The JSON Schema rejects strings matching `/^xai-[a-zA-Z0-9]{32,}$/` in `env:` literals. All `env:` values should reference repo secrets, e.g. `${{ secrets.API_KEY }}`.

**T2 — Prompt Injection via Tool Output**
Attack: A step's output is fed into the next step's `condition` or `action` input. If the output contains injected instructions, they propagate through the workflow.
Defense: Tool output is wrapped in XML delimiters before insertion into subsequent steps. `condition:` expressions are evaluated server-side against sanitised values, never raw strings.

**T3 — Path Traversal in Filesystem Tools**
Attack: A step's input resolves to a path like `"../../etc/passwd"`.
Defense: Path parameters are validated against `^(?!.*\.\.)[^/].*$` before execution.

**T4 — Over-Permissioned Actions**
Attack: A workflow triggered by a PR comment reaches a deploy step without approval.
Defense: `require_approval: true` on any step invoking `deploy`, `post_thread`, or `publish_thread`. Schema validation fails if a workflow routes from a PR-triggered entry point to an unapproved write step.

**T5 — Rate Limit Abuse (primary threat)**
Attack: A workflow contains a loop (A → B → A) whose terminating condition never evaluates true. The loop calls `search_x` or `post_thread` until daily quota is exhausted.
Defense: Every workflow declares `max_steps` (default 50). The runtime tracks step count per run and aborts on overflow. Cycle detection runs at validation time — a static graph analysis rejects any workflow where a directed cycle exists without a terminating `condition:` that references a decrementing step output.

**T6 — Supply Chain via Remote Tool Import**
Attack: A workflow step imports an external action from a compromised URL.
Defense: External action URLs must be whitelisted in `grok-security.yaml`. Dynamic imports from user-controlled URLs are rejected.

### Workflow-Specific Threats

**WT1 — Workflow Loops and Cycle Detection**
Attack: Steps A → B → C → A form a cycle. A single trigger causes unbounded execution.
Defense: The validator performs a DAG analysis on each workflow. Any directed cycle fails validation unless the edge is gated by a `condition:` referencing a monotonically decreasing counter. Runtime enforces a global `max_steps` cap.

**WT2 — Chained Approval Bypass**
Attack: A workflow with 20 automated steps places the `require_approval` gate at step 19, right before a deploy. A human approver who has been clicking through notifications for weeks rubber-stamps step 19 without realising the prior 18 steps have already mutated state.
Defense: For any workflow that posts to X or deploys to production, the approval gate must be the **first** step after the trigger. Schema validation rejects workflows where `require_approval: true` is not among the first two steps of a publish/deploy workflow.

### Out of Scope for This Spec

- Vulnerabilities in the xAI API or the Grok model itself — report to xAI's security team.
- X platform vulnerabilities — report to X's security team.
- Host OS, container runtime, or network security — handled by the deployment platform.

### Reporting Security Issues

See the repository [`SECURITY.md`](../SECURITY.md). Never file a public issue for a suspected vulnerability; use a private GitHub Security Advisory or the email listed in `SECURITY.md`.
