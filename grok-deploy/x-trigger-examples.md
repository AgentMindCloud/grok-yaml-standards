# grok-deploy.yaml — X Trigger Examples

Drop any of these trigger comments into a GitHub issue, PR description, or commit message, then tag `@grok`.

---

## Trigger 1 — Deploy to staging
```
@grok deploy staging
```
Deploys the current branch to the `staging` target defined in `.grok/grok-deploy.yaml`.

---

## Trigger 2 — Deploy to production
```
@grok deploy production
```
Initiates a production deploy. If `require_approval: true` is set, Grok waits for an approval comment from a listed approver before proceeding.

---

## Trigger 3 — List all deployment targets
```
@grok deploy list
```
Prints all targets defined in `.grok/grok-deploy.yaml` with their provider, branch, and current status.

---

## Trigger 4 — Check deploy status
```
@grok deploy status production
```
Polls the production health check endpoint and reports the current health, last deploy time, and instance count.

---

## Trigger 5 — Rollback last deploy
```
@grok deploy rollback production
```
Re-deploys the previous successful build for the `production` target.
