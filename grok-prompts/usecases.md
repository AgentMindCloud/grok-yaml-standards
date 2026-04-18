# grok-prompts — Real-World Use Cases

---

### Viral Thread Templates (Content Creator)

**Who uses this:** A content creator, newsletter writer, or developer advocate who publishes multiple X threads per week and wants consistent structure without rewriting the format from scratch every time.

**Scenario:** You write threads on the same topics repeatedly — product launches, technical explainers, hot takes. Each time you start from a blank slate and spend 20 minutes getting the format right before writing a single word of real content. A shared template library would cut that to five minutes.

**How grok-prompts helps:** A `viral_thread` template with `output_format: thread` and `variables: ["topic", "tone"]` generates an 8-tweet draft on demand. `temperature: 0.85` keeps output creative and varied across invocations. `cache_responses: false` ensures each call produces a fresh draft rather than a cached repeat.

**Example:**
```yaml
prompt_library:
  viral_thread:
    description: "Turns any topic into a punchy 8-tweet X thread with a strong hook."
    template: |
      Write an 8-tweet thread about {topic}.
      Tone: {tone}. Target audience: {audience}.
      Tweet 1: strong hook — surprising stat or bold claim.
      Tweets 2–7: one insight per tweet, max 260 chars each.
      Tweet 8: call to action — follow or retweet.
    variables: ["topic", "tone"]
    optional_variables: ["audience"]
    output_format: "thread"
    temperature: 0.85
    cache_responses: false
    tags: ["social", "content", "x-native"]
```

**Pitfalls to avoid:** Setting `cache_responses: true` on a creative template means repeated calls return the same thread — your audience will notice identical posts. Don't set `temperature: 0` on a thread template; deterministic output produces flat, repetitive prose that underperforms on X.

**Next step:** See `grok-workflow.yaml` to build a pipeline that runs this template, reviews the draft, and posts the result to X after human approval.

---

### Consistent Code-Review Prompts (Development Team)

**Who uses this:** An engineering team that wants every code review to follow the same checklist — security, performance, readability — regardless of which developer is doing the reviewing.

**Scenario:** Code review quality varies wildly across the team. Senior devs catch security issues; junior devs focus on style. There's no shared standard, so critical bugs slip through inconsistent reviews. You want every PR to receive the same baseline security and performance pass before it merges.

**How grok-prompts helps:** A `code_review` template with `temperature: 0.1` produces deterministic, structured reviews. `variables: ["language", "focus", "code"]` makes it reusable across every language in the monorepo. `reasoning_mode: "high"` engages deeper analysis for subtle bugs. `output_format: markdown` produces a checklist compatible with GitHub PR comments.

**Example:**
```yaml
prompt_library:
  code_review:
    description: "Structured security and performance code review for any language."
    template: |
      Review the following {language} code for {focus}.
      Output a markdown checklist with severity: critical / high / medium / low.
      For each finding: describe the issue, cite the line number, suggest a fix.
      Code:
      {code}
    variables: ["language", "focus", "code"]
    output_format: "markdown"
    temperature: 0.1
    reasoning_mode: "high"
    response_format: "text"
    tags: ["code", "security", "review"]
```

**Pitfalls to avoid:** Passing an entire large file as `{code}` — token limits will truncate the review mid-analysis; pass only the changed diff. Don't set `cache_responses: true`; the same code diff should always be reviewed fresh, not served a cached result from a prior commit.

**Next step:** See `grok-workflow.yaml` to trigger this prompt automatically on every PR via a `grok-prompts` step in a review workflow.

---

### Brand-Voice Prompts (Marketing Team)

**Who uses this:** A marketing team at a startup that wants all AI-assisted content — social posts, blog intros, email subject lines — to match the brand's established voice and avoid off-brand phrasing.

**Scenario:** Your marketing team uses AI assistants ad hoc and the outputs are inconsistent. One post sounds corporate, the next sounds casual. The brand guide exists, but nobody feeds it to the AI consistently. You need brand constraints baked in by default, not enforced by individual discipline.

**How grok-prompts helps:** A `brand_post` template embeds the brand voice guide in `system_prompt` — a static layer that variable values can't override. `temperature: 0.6` balances creativity with consistency. `tags: ["brand", "marketing"]` makes the template discoverable and filterable in the library.

**Example:**
```yaml
prompt_library:
  brand_post:
    description: "Generates on-brand social copy in AcmeCorp's voice for any platform."
    system_prompt: |
      You write for AcmeCorp. Voice: bold, witty, never corporate.
      Avoid: jargon, passive voice, exclamation marks except very sparingly.
      Always end with one concrete next step for the reader.
    template: |
      Write a {format} about {topic} for {platform}.
      Length: {length}. Audience: {audience}.
    variables: ["format", "topic", "platform", "length", "audience"]
    output_format: "plain"
    temperature: 0.6
    cache_responses: false
    tags: ["brand", "marketing", "social"]
```

**Pitfalls to avoid:** Putting brand rules in `template` instead of `system_prompt` — brand constraints must be in the static system layer, not the user message, so they can't be overridden by variable values. Don't set `cache_responses: true` for marketing copy; cached responses produce duplicate posts across different campaigns.

**Next step:** See `grok-config.yaml` `grok.context.tone` to set a global tone baseline that all prompts in the library inherit before their own overrides apply.

---

### Essay & Research Templates (Students / Academics)

**Who uses this:** Students, academics, or researchers who write the same types of structured documents repeatedly — literature review sections, methodology justifications, executive summaries — and want a consistent analytical framework each time.

**Scenario:** You write literature review sections for multiple grant proposals per year. Each one starts with a blank page and the same structural decisions. A template that enforces your preferred framework and citation style saves 45 minutes per section and produces more consistent output across co-authors.

**How grok-prompts helps:** A `lit_review_section` template with `reasoning_mode: "high"` engages deeper analysis for academic quality. `temperature: 0.3` keeps the prose measured and evidence-focused rather than creative. An explicit `max_tokens: 8192` budget prevents the extended thinking from silently hitting limits.

**Example:**
```yaml
prompt_library:
  lit_review_section:
    description: "Generates a structured literature review section with citations and synthesis."
    template: |
      Write a literature review section on {topic} synthesizing {num_sources} sources.
      Structure:
      1. Thematic overview (2 sentences)
      2. Key findings across sources with inline citations
      3. Contradictions or gaps in the literature
      4. Relevance to {research_question}
      Use {citation_style} format for all citations.
    variables: ["topic", "num_sources", "research_question", "citation_style"]
    output_format: "markdown"
    temperature: 0.3
    reasoning_mode: "high"
    max_tokens: 8192
    tags: ["academic", "research", "writing"]
```

**Pitfalls to avoid:** Setting `temperature: 0.85` on academic writing produces hallucinated citations — keep it at 0.3 or below for any factual, cited output. Don't omit `max_tokens` when using `reasoning_mode: high`; extended thinking tokens count toward the total and can silently hit the model's context limit.

**Next step:** See `grok-agent.yaml` to create a `LitReviewer` agent that runs this prompt across a folder of papers and accumulates structured summaries in long-term memory.

---

### Standardized Customer-Support Replies (Enterprise Support Team)

**Who uses this:** A customer support team at a company with compliance requirements — financial services, healthcare — that needs every AI-assisted response to follow approved language, escalation paths, and regulatory disclosures.

**Scenario:** Support agents use AI to draft replies, but the outputs vary. One agent's draft promises a refund timeline the company can't honor; another's omits a required regulatory disclosure. You need guardrails that make compliant responses the default, not the exception that requires a manager to catch.

**How grok-prompts helps:** A `support_reply` template with `system_prompt` embedding the compliance ruleset locks the persona before any variable is interpolated. `response_format: "json_object"` structures the output so the reply text, the escalation flag, and the disclosure checklist are all parseable fields for downstream systems. `temperature: 0.2` keeps language consistent and on-script.

**Example:**
```yaml
prompt_library:
  support_reply:
    description: "Drafts a compliant customer support reply with escalation and disclosure fields."
    system_prompt: |
      You draft support replies for FinanceCo. Rules:
      - Never promise refund timelines without manager approval.
      - Always include the required FDIC disclosure for account questions.
      - If the issue involves a transaction over $10,000, set escalate: true.
    template: |
      Draft a support reply for this customer message: {customer_message}
      Issue category: {category}. Account type: {account_type}.
      Output JSON with fields: reply (string), escalate (boolean), disclosures_included (list).
    variables: ["customer_message", "category", "account_type"]
    output_format: "json"
    response_format: "json_object"
    temperature: 0.2
    cache_responses: false
    tags: ["support", "compliance", "finance"]
```

**Pitfalls to avoid:** Setting `cache_responses: true` caches a reply to one customer's message and may serve it to a different customer — every support reply must be generated fresh. Don't set `temperature: 0.8`; high temperature on compliance-sensitive text produces creative variations that may deviate from legally approved language.

**Next step:** See `grok-analytics.yaml` to track `escalate: true` events over time and identify the top categories driving escalations, so the knowledge base can be expanded to handle them automatically.
