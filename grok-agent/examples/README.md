# grok-agent reference configurations

Four drop-in `grok-agent.yaml` files showing the **`hub_card`** block (added in `grok-yaml-standards@1.3`) configured across the most common real-world shapes: public research agent, content bot, strict read-only reviewer, and a private opt-out agent.

## How to use

1. Pick the file whose shape most closely matches the agent you want to ship.
2. Copy it into your repository as `.grok/grok-agent.yaml`.
3. Update `author`, `github`, `registry_name`, and the agent `description` to match your project.
4. Validate locally:
   ```bash
   npx ajv validate --spec=draft7 --all-errors --strict=false \
     -s schemas/grok-agent.json -d .grok/grok-agent.yaml
   ```

All four files validate against `schemas/grok-agent.json` — every commit is checked by the `validate-schemas` CI workflow.

## Files

| File                       | `safety_profile` | `hub_card.publish` | Intent                                                  |
| -------------------------- | ---------------- | ------------------ | ------------------------------------------------------- |
| `research-swarm-v2.yaml`   | `balanced`       | `true`             | Public multi-source research agent, full GrokHub card   |
| `trend-to-thread-bot.yaml` | `balanced`       | `true`             | Content-generation bot tagged `x-native`                |
| `code-reviewer-agent.yaml` | `strict`         | `true`             | Read-only PR reviewer, `permission_scopes: [read]` only |
| `private-ops-agent.yaml`   | `strict`         | `false`            | Internal ops agent, demonstrates the opt-out pattern    |

## Notes

- `hub_card` is optional — omitting it is equivalent to `publish: false` (agent stays private).
- Only agents with `hub_card.publish: true` are discoverable in the GrokHub registry.
- Set `safety_profile: strict` and narrow `permission_scopes` when publishing an agent that ships with elevated tools.
