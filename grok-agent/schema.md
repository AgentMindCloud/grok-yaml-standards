# grok-agent.yaml Field Reference

Full JSON Schema: [`/schemas/grok-agent.json`](../schemas/grok-agent.json)

---

## Top-level fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `version` | `string` | ✅ | Semver of this agent config file (e.g. `"1.2.0"`). |
| `author` | `string` | ✅ | X handle of the config owner, prefixed with `@`. |
| `compatibility` | `string[]` | ✅ | Spec identifiers this file is compatible with. |
| `agents` | `object` | ✅ | Named agent definitions. At least one entry required. |

---

## agents entries

Each key becomes the agent identifier used in `@grok spawn agent:<Name>` triggers.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | `string` | ✅ | Purpose and domain expertise of this agent. Min 10 chars, max 500 chars. |
| `tools` | `string[]` | — | Tool identifiers the agent is permitted to invoke. Cross-reference with `grok-tools.yaml`. |
| `memory` | `string` | `"session_only"` | Memory persistence strategy across sessions. |
| `max_turns_per_session` | `integer` | `50` | Back-and-forth turns allowed before the agent requires re-spawning. Range: `1` – `1000`. |
| `auto_save_state` | `boolean` | `false` | Persist agent state after every session. Only meaningful with `memory: long_term`. |
| `personality` | `string` | — | Agent-level personality override. Overrides `grok.personality` from `grok-config.yaml`. |
| `system_prompt` | `string` | — | Custom system prompt prepended to every session. Min 10 chars, max 4000 chars. |
| `permissions` | `string[]` | — | Explicit capability grants beyond standard read access. |
| `rate_limit` | `object` | — | Per-agent request throttling. See below. |
| `enabled` | `boolean` | `true` | Set to `false` to disable this agent without removing its definition. |

**`memory` enum values:**
`long_term` · `session_only` · `none`

**`personality` enum values:**
`helpful-maximalist` · `concise` · `creative` · `technical` · `balanced` · `socratic` · `executive`

**`permissions` enum values:**
`read` · `write` · `execute` · `network` · `publish` · `deploy` · `admin`

---

## tools — known identifiers

The following tool identifiers are defined in `grok-tools.yaml` and available for assignment:

| Tool | Category | Description |
|------|----------|-------------|
| `read_file` | file_system | Read file contents from the repository |
| `write_file` | file_system | Write or overwrite a file |
| `list_files` | file_system | List files matching a glob pattern |
| `delete_file` | file_system | Delete a file from the repository |
| `run_command` | code | Execute a shell command and capture output |
| `search_code` | code | Full-text and semantic code search |
| `create_pr` | code | Open a GitHub pull request |
| `create_branch` | code | Create a new git branch |
| `merge_pr` | code | Merge an approved pull request |
| `run_tests` | testing | Run the repository test suite |
| `post_thread` | social | Post a thread of tweets to X |
| `analyze_engagement` | social | Fetch engagement metrics for recent posts |
| `reply_to_mentions` | social | Reply to X mentions |
| `web_search` | web | Search the open web |
| `web_fetch` | web | Fetch content from a URL |
| `call_api` | data | Make an authenticated HTTP API call |
| `read_database` | data | Execute a read query against a database |
| `write_database` | data | Execute a write query against a database |
| `deploy` | deployment | Trigger a deployment via `grok-deploy.yaml` |
| `send_notification` | notification | Send a notification via a configured channel |

---

## rate_limit object fields

| Field | Type | Description |
|-------|------|-------------|
| `requests_per_minute` | `integer` | Maximum tool invocations per 60-second window. Range: `1` – `600`. |
| `requests_per_day` | `integer` | Maximum tool invocations per calendar day. Range: `1` – `100000`. |
