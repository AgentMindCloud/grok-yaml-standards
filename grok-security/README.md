# grok-security.yaml

**What problem it solves**  
Real-time security & compliance checks.

---

## Cross-References

### Depends On
- **grok-config.yaml**: `safety_profile` in config is the global baseline; per-scan `severity_threshold` overrides it.

### Used By
- **grok-agent.yaml**: agents set `safety_profile` which must align with this spec.
- **grok-workflow.yaml**: `steps[].action: grok-security` runs named scans.
- **grok-deploy.yaml**: `require_approval` behaviour is informed by security policy.
- **grok-test.yaml**: `block_merge_on_fail` integrates with the security gate.

### xAI SDK Mapping
| This spec field | xAI SDK equivalent |
|-----------------|--------------------|
| `scans[].type` | Drives the analysis prompt sent to the model. |
| scan results | Returned as `response_format: json_object` with CVE data. |
| `severity_threshold` | Post-processing filter on model output. |

### LiteLLM Mapping
| This spec field | LiteLLM parameter |
|-----------------|-------------------|
| (all fields) | Security scan results are returned as structured JSON from the Grok runtime; no direct LiteLLM parameters correspond to scan configuration fields. |

### Semantic Kernel Mapping
| This spec field | SK equivalent |
|-----------------|---------------|
| (all fields) | No direct SK equivalents — scan configuration is resolved by the Grok runtime, not the SK kernel. |
