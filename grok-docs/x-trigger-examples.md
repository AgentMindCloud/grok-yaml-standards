# grok-docs.yaml — X Trigger Examples

Drop any of these trigger comments into a GitHub issue, PR description, or commit message, then tag `@grok`.

---

## Trigger 1 — Regenerate README
```
@grok docs AutoREADME
```
Regenerates the root `README.md` using the `AutoREADME` target defined in `.grok/grok-docs.yaml`.

---

## Trigger 2 — Refresh API Documentation
```
@grok docs APIDocs
```
Regenerates `docs/API.md` with up-to-date endpoint listings, auth instructions, and code samples.

---

## Trigger 3 — Run all doc targets
```
@grok docs all
```
Regenerates every target defined in `.grok/grok-docs.yaml` in sequence.

---

## Trigger 4 — Docs on merge
Automatic — no manual trigger needed. When `update_on: ["pr_merged"]` is set, Grok regenerates the target every time a PR is merged to the default branch.

---

## Pro tip
Combine with `grok-workflow.yaml` to chain docs generation as a step in your release pipeline:
```yaml
steps:
  - name: "Generate Docs"
    action: "grok-docs"
    input: "all"
```
