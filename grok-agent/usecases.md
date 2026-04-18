# grok-agent — Real-World Use Cases

---

### 24/7 Coding Partner (Indie Hacker)

**Who uses this:** Solo developer or indie hacker building a side project with limited hours to spend on routine engineering tasks.

**Scenario:** You're shipping a SaaS product alone and can't afford to context-switch constantly. Between meetings and client work you need an agent that knows your codebase, picks up exactly where you left off, and never forgets the architecture decisions you made last Tuesday.

**How grok-agent helps:** `memory: long_term` with `auto_save_state: true` persists everything the agent learns about your repo across sessions. A focused `system_prompt` anchors it to your stack and coding conventions. A tight `tools` list (`read_file`, `write_file`, `search_code`, `create_pr`) keeps the blast radius small — only the tools the agent actually needs.

**Example:**
```yaml
agents:
  CodePartner:
    description: "Daily coding partner with read-write access to this TypeScript monorepo."
    tools: ["read_file", "write_file", "search_code", "create_pr"]
    memory: "long_term"
    auto_save_state: true
    safety_profile: "balanced"
    system_prompt: "You are a senior TypeScript engineer who knows this monorepo. Always open PRs as drafts. Prefer small, focused commits."
    rate_limit:
      requests_per_minute: 30
      requests_per_day: 500
```

**Pitfalls to avoid:** Granting `run_command` without also setting `safety_profile: balanced` — shell access without a safety gate can run destructive scripts. Don't omit `rate_limit` on a long-running session; uncapped agents can exhaust API quotas overnight.

**Next step:** See `grok-workflow.yaml` for chaining this agent into a full release pipeline with approval gates.

---

### Bug Triager (Open-Source Maintainer)

**Who uses this:** Open-source project maintainer receiving dozens of GitHub issues per week, many of which are duplicates, missing reproduction steps, or simply off-topic.

**Scenario:** Your inbox fills with "it doesn't work" issues every Monday morning. You spend an hour a day labelling, closing duplicates, and asking for repro steps — time that should go to actual development. The triage backlog grows faster than you can clear it.

**How grok-agent helps:** A dedicated triage agent with `memory: session_only` handles each issue in isolation so no state leaks between tickets. Its `system_prompt` encodes your triage checklist: check for duplicates via `search_code`, request OS and version, label appropriately. Read-only tools mean it can comment but never commit.

**Example:**
```yaml
agents:
  BugTriager:
    description: "Reads new issues, checks for duplicates, and posts a structured triage comment."
    tools: ["read_file", "search_code"]
    memory: "session_only"
    system_prompt: |
      You triage GitHub issues for this project. For every new issue:
      1. Search existing issues for duplicates.
      2. If duplicate, comment with the original issue link.
      3. Otherwise, ask for: OS, version, minimal reproduction steps.
      Never close issues — only label and comment.
    rate_limit:
      requests_per_day: 200
```

**Pitfalls to avoid:** Using `memory: long_term` here wastes storage — each triage is stateless by design. Don't give this agent `write_file` or `create_pr`; it should comment on issues, not touch the codebase.

**Next step:** See `grok-workflow.yaml` to trigger this agent automatically on issue-open and `on_pr` events.

---

### Feature Brainstorming Agent (Product Team)

**Who uses this:** Product managers and designers at a startup who want structured brainstorming facilitated by an AI that understands the product's constraints and can challenge assumptions.

**Scenario:** Your team holds weekly feature brainstorming sessions, but the output is inconsistent — great ideas get buried in meeting notes and nobody tracks which constraints were considered. You want a facilitated, structured output every time that you can reference in the next sprint.

**How grok-agent helps:** `personality: socratic` combined with domain knowledge from `grok-config.yaml` gives the agent enough product context to challenge assumptions and surface edge cases. `memory: long_term` lets it remember prior session decisions so it doesn't re-litigate settled questions. `save_memory` and `recall_memory` build a growing decision log.

**Example:**
```yaml
agents:
  ProductBrainstormer:
    description: "Facilitates structured feature brainstorming using Socratic questioning."
    tools: ["read_file", "save_memory", "recall_memory"]
    memory: "long_term"
    auto_save_state: true
    personality: "socratic"
    system_prompt: |
      You facilitate product brainstorming. For each feature idea:
      1. Ask who benefits and what job it does.
      2. Identify the top constraint: performance, cost, or privacy.
      3. Propose two alternative approaches with trade-offs.
      4. Record the decision in memory with today's date.
    rate_limit:
      requests_per_minute: 20
      requests_per_day: 300
```

**Pitfalls to avoid:** Giving this agent `write_file` or `create_pr` turns a brainstorming tool into one that can commit unreviewed ideas to the codebase. Keep it read-and-memory-only until ideas are explicitly approved by a human.

**Next step:** See `grok-prompts.yaml` to create reusable templates for specific brainstorming formats such as RICE scoring or jobs-to-be-done analysis.

---

### Ticket Resolver (Customer Support Team)

**Who uses this:** A support team at a SaaS company handling repetitive tier-1 tickets — password resets, billing questions, feature how-tos — that consume agent time better spent on complex escalations.

**Scenario:** Sixty percent of your support queue is the same 20 questions. Agents spend their best hours copy-pasting from the knowledge base instead of handling escalations that require human empathy and judgment. Response times suffer and agent morale drops.

**How grok-agent helps:** An agent with `memory: long_term` accumulates product knowledge over time via `recall_memory`. Its `system_prompt` encodes escalation rules: respond to tier-1 automatically, escalate tier-2 with a structured summary. `rate_limit` prevents the agent from flooding customers with duplicate messages.

**Example:**
```yaml
agents:
  SupportBot:
    description: "Handles tier-1 support tickets using the internal knowledge base."
    tools: ["read_file", "search_code", "recall_memory"]
    memory: "long_term"
    auto_save_state: true
    personality: "helpful-maximalist"
    system_prompt: |
      You are a support agent for AcmeSaaS. You may only answer questions
      covered in the knowledge base under docs/. If you cannot find a clear
      answer, respond: 'Escalating to a human agent — please hold.'
      Never disclose internal pricing tiers or unreleased roadmap items.
    rate_limit:
      requests_per_minute: 10
      requests_per_day: 1000
```

**Pitfalls to avoid:** Don't grant `write_file` or `create_pr` — a support agent should never modify the codebase as a side effect of answering a ticket. Avoid `memory: none`; without state the agent can't learn from past resolutions and will repeat mistakes.

**Next step:** See `grok-analytics.yaml` to track which ticket categories the agent resolves versus escalates, and use that data to improve the knowledge base.

---

### Literature Review Agent (Researcher)

**Who uses this:** Academic researchers or data scientists who need to synthesize large volumes of papers, reports, and documentation into structured summaries with consistent citation format.

**Scenario:** You're preparing a literature review for a grant proposal. You have 80 PDFs and need structured summaries — methodology, key findings, limitations — that you can cross-reference and cite. Manual processing takes two weeks; the proposal deadline is in five days.

**How grok-agent helps:** `tools: ["read_file", "web_search", "save_memory", "recall_memory", "summarize_changes"]` let the agent fetch papers, extract key points, and accumulate a structured knowledge base in `memory: long_term`. The `system_prompt` enforces citation format and summary structure. `max_turns_per_session: 200` handles large batches without hitting the default 50-turn cap.

**Example:**
```yaml
agents:
  LitReviewer:
    description: "Reads research papers and produces structured summaries with citations."
    tools: ["read_file", "web_search", "save_memory", "recall_memory", "summarize_changes"]
    memory: "long_term"
    auto_save_state: true
    personality: "technical"
    max_turns_per_session: 200
    system_prompt: |
      You are a research assistant. For each paper:
      1. Extract: authors, year, methodology, key findings, limitations.
      2. Save a structured summary to memory with the DOI as the key.
      3. Flag contradictions with prior summaries already in memory.
      Always cite in APA format. Never fabricate citations or statistics.
    rate_limit:
      requests_per_day: 2000
```

**Pitfalls to avoid:** `max_turns_per_session` defaults to 50 — for sessions processing many papers this cap is hit quickly; set it explicitly. Don't enable `write_file` unless you intend the agent to modify source documents as it reviews them.

**Next step:** See `grok-workflow.yaml` to build a pipeline that fetches papers from a URL list, runs this agent, then publishes a consolidated summary report.
