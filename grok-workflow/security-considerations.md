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
