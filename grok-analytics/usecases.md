# grok-analytics.yaml — Use Cases

## 1. Usage dashboard for open-source maintainers
Track `grok_invoked` events with properties `["spec", "trigger", "repo"]` to see which specs your community uses most. PostHog provides a free tier sufficient for most open-source projects and the data never leaves your PostHog instance.

## 2. Workflow performance benchmarking
Capture `workflow_completed` with `duration_ms` to identify which workflows are slowest. If `ReleasePipeline` consistently takes over 10 minutes, the data points to which step to optimise first.

## 3. GDPR-compliant enterprise telemetry
Set `anonymize_user_ids: true`, `data_retention_days: 90`, and `opt_out_roles: ["guest"]` to ensure telemetry meets GDPR retention and anonymisation requirements without touching application code.

## 4. Security incident frequency tracking
Enable the `security_finding` event with `properties: ["scan_type", "alert_level"]`. Spike detection in your analytics dashboard provides an early warning when a new vulnerability class starts appearing across multiple PRs.

## 5. A/B testing prompt library effectiveness
Track `grok_invoked` with `properties: ["spec", "trigger", "prompt_name", "output_length"]`. Correlate prompt variants with engagement metrics from `analyze_engagement` to learn which prompts produce the most viral output.
