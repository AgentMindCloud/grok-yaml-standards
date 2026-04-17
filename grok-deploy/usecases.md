# grok-deploy.yaml — Use Cases

## 1. One-comment staging deploy
Add `@grok deploy staging` to any PR comment. Grok reads `.grok/grok-deploy.yaml`, resolves secrets from the repository secret store, deploys to Vercel, polls the `/health` endpoint, and replies with a deploy URL — all without leaving GitHub.

## 2. Approval-gated production releases
Set `require_approval: true` and `approval_from: ["@CEO", "@CTO"]` on the `production` target. Grok waits for an approval comment from a listed approver before proceeding, creating an auditable, YAML-defined change management process.

## 3. Resource-capped preview environments
Define a `preview` target with `max_instances: 1` and `memory_mb: 256` to cap the cost of ephemeral per-PR preview deployments while still enabling full end-to-end testing.

## 4. Automatic rollback on failed health check
Set `rollback_on_unhealthy: true`. If the post-deploy health check fails three consecutive times, Grok re-deploys the previous successful build and posts an incident summary to X, completing the rollback loop without human intervention.

## 5. Multi-cloud deployment matrix
Define targets for `aws_us_east`, `gcp_eu_west`, and `fly_apac` in the same file. Use `@grok deploy aws_us_east` and `@grok deploy gcp_eu_west` independently, or chain them in a `grok-workflow.yaml` global-release step for coordinated multi-region rollouts.
