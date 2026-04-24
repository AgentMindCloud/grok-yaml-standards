# grok-workflow reference configurations

Three drop-in `grok-workflow.yaml` files showing the **`orchestration`** block (added in `grok-yaml-standards@1.3`) across the three execution modes that benefit most from concrete templates: a large hybrid swarm, a debate swarm, and a minimal linear graph.

## How to use

1. Pick the file whose mode matches the topology you need.
2. Copy it into your repository as `.grok/grok-workflow.yaml`.
3. Update `author`, the workflow name, agent `role` strings, and the `steps` body to match your pipeline.
4. Validate locally:
   ```bash
   npx ajv validate --spec=draft7 --all-errors --strict=false \
     -s schemas/grok-workflow.json -d .grok/grok-workflow.yaml
   ```

All three files validate against `schemas/grok-workflow.json`.

## Files

| File                             | `mode`          | Agent roles | Total instances | Memory             | X-native step             |
| -------------------------------- | --------------- | ----------- | --------------- | ------------------ | ------------------------- |
| `massive-x-research-swarm.yaml`  | `hybrid`        | 6           | 28              | `vector` / qdrant  | `post_thread` + scan      |
| `debate-swarm-example.yaml`      | `debate_swarm`  | 3           | 3               | `session`          | `post_thread`, `reply_to_mentions` |
| `simple-graph-agent.yaml`        | `graph`         | 3           | 3               | `session`          | `post_thread`, `reply_to_mentions` |

## Notes

- `orchestration` describes **how agents coordinate** during the workflow; it does not replace `steps`. Every reference file still declares a concrete ordered `steps` list.
- `mode: hybrid` allows both graph edges and free-form coordination. `mode: graph` requires edges to form a valid DAG.
- `mode: debate_swarm` requires the `debate_swarm` object with `rounds` and `voter_model`. `quorum` defaults to `0.66`.
- When `memory.type` is `vector`, `memory.vector_store` is required.
