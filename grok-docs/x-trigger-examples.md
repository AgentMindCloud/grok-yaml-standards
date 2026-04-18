# grok-docs.yaml — X Trigger Examples

Two complementary trigger systems are available for docs automation:

1. **GitHub comment triggers** — drop `@grok docs <command>` into a PR, issue, or
   commit message to run on-demand doc generation.
2. **X monitoring triggers** — YAML config blocks in `.grok/grok-docs.yaml` that fire
   based on X social activity (mentions, keyword searches, schedule).

All X write actions (posting threads, replying) require `approval_required: true`.
Read-only monitors (search, mention detection) run without approval.

---

## Part 1 — GitHub Comment Triggers

Drop any of these into a GitHub issue, PR description, or commit message, then tag `@grok`.

---

### Trigger 1 — Regenerate README
```
@grok docs AutoREADME
```
Regenerates the root `README.md` using the `AutoREADME` target defined in `.grok/grok-docs.yaml`.

---

### Trigger 2 — Refresh API Documentation
```
@grok docs APIDocs
```
Regenerates `docs/API.md` with up-to-date endpoint listings, auth instructions, and code samples.

---

### Trigger 3 — Compile Changelog
```
@grok docs Changelog
```
Reads recent commits and merged PRs, then writes a human-readable changelog entry to `CHANGELOG.md`.

---

### Trigger 4 — Run All Doc Targets
```
@grok docs all
```
Regenerates every target defined in `.grok/grok-docs.yaml` in declaration order.

---

### Trigger 5 — List All Targets
```
@grok docs list
```
Prints a table of every docs target, its output path, and the timestamp of its last successful generation.

---

### Trigger 6 — Check Staleness
```
@grok docs status
```
Identifies targets whose source files have changed since the last generation run, so you know what needs updating before a release.

---

### Trigger 7 — Preview Without Publishing
```
@grok docs preview AutoREADME
```
Generates the `AutoREADME` target and posts the output as a PR comment for review — does **not** write to the file. Useful for checking output before committing.

---

### Trigger 8 — Diff Without Writing
```
@grok docs diff AutoREADME
```
Shows a unified diff between the current file and what would be generated, without writing any changes. Zero side effects.

---

## Part 2 — X Monitoring Triggers

Configure these blocks in `.grok/grok-docs.yaml` under an `x_triggers:` key.
All triggers are read-only monitors. Write actions (posting replies or threads)
require explicit human approval.

---

### 1. Mention-Based Triggers

#### Basic Mention Trigger
```yaml
# Fires when @youragent is mentioned on X
x_triggers:
  on_mention:
    enabled: true
    filter:
      min_follower_count: 0       # respond to everyone
      exclude_bots: true
      exclude_spam: true          # grok safety spam classifier applied
      exclude_retweets: true
    action: "draft_docs_reply"    # drafts a reply pointing to relevant docs
    approval_required: true
    rate_limit:
      per_hour: 10
      per_day: 100
```

#### Docs-Keyword Mention Filter
```yaml
# Only fires when the mention asks a documentation-related question
x_triggers:
  on_mention:
    enabled: true
    filter:
      keywords_any: ["docs", "documentation", "readme", "how do I", "where is", "?"]
      keywords_none: ["spam", "promo", "sale", "discount", "follow back"]
      languages: ["en", "es", "fr"]
    action: "classify_and_route_docs_query"
    approval_required: true
```

#### Tiered Response by Account Weight
```yaml
# Priority handling for verified or high-follower accounts
x_triggers:
  on_mention:
    tiers:
      - name: "priority"
        filter:
          verified: true
          min_followers: 10000
        action: "draft_priority_docs_reply"
        notify_user: true           # extra notification so human sees it promptly
        approval_required: true
      - name: "standard"
        filter:
          verified: false
        action: "draft_standard_docs_reply"
        approval_required: true
```

---

### 2. Keyword Timeline Search Triggers
```yaml
# Monitors X public search for docs-related discussion — not trending,
# just any posts matching these queries
x_triggers:
  on_search:
    enabled: true
    queries:
      - '"grok-docs" lang:en'
      - '"missing documentation" grok -is:retweet lang:en'
      - '#GrokDocs -is:retweet'
      - '"grok yaml" docs -is:retweet'
    poll_interval_minutes: 30     # check every 30 minutes
    max_results_per_poll: 20
    action: "compile_docs_mentions_digest"
    approval_required: true       # digest is reviewed before any reply is posted
    rate_limit:
      daily_calls: 48             # 30-min interval × 48 = covers 24 hours
```

---

### 3. Reply Chain Triggers
```yaml
# Fires when someone replies to a thread this agent posted
# (e.g. a doc-announcement thread)
x_triggers:
  on_reply_to_own:
    enabled: true
    filter:
      exclude_own_replies: true   # don't re-trigger on the agent's own replies
      exclude_bots: true
    action: "draft_followup_docs_reply"
    max_thread_depth: 5           # stop replying after 5 levels deep (prevents storms)
    approval_required: true
```

---

### 4. Schedule-Based Triggers
```yaml
# Time-based triggers — not X events, but produce X-postable content
x_triggers:
  on_schedule:
    - name: "daily_freshness_check"
      cron: "0 9 * * *"          # 9am UTC daily
      timezone: "UTC"
      action: "check_docs_freshness"
      skip_if_no_changes: true   # silent if all docs are current

    - name: "weekly_docs_roundup"
      cron: "0 17 * * 5"         # 5pm UTC every Friday
      action: "compile_weekly_docs_roundup"
      approval_required: true    # human approves the roundup thread before it posts
      skip_if_no_content: true

    - name: "monthly_link_audit"
      cron: "0 9 1 * *"          # 1st of each month, 9am UTC
      action: "audit_dead_links"
      notify_user: true          # always notify results even if no dead links
```

---

### 5. Multi-Agent Docs Generation Swarm
```yaml
# Incoming mention asking for comprehensive docs → routes to a multi-agent swarm
x_triggers:
  on_mention:
    filter:
      keywords_any: ["research", "comprehensive docs", "complete guide", "deep dive", "full tutorial"]
    action: "spawn_docs_swarm"
    swarm:
      agents:
        - name: "researcher"
          role: "Gathers source material, API signatures, and examples"
        - name: "writer"
          role: "Drafts the documentation from researcher output"
        - name: "editor"
          role: "Reviews for accuracy, completeness, and style consistency"
        - name: "publisher"
          role: "Formats output and queues thread for human approval"
      handoff_strategy: "sequential"
      max_total_turns: 30
    approval_required: true      # publisher shows final output; human approves before post
```

---

### 6. Safety Override Examples
```yaml
# These safety rules are enforced by grok-security.yaml — they cannot be
# overridden by trigger config even if a user tries
x_triggers:
  safety_overrides:

    # ALWAYS blocked — protects X platform from abuse
    never_trigger_on:
      - "is:retweet"              # don't respond to retweets (spam amplification risk)
      - "author_is_self: true"    # never respond to own posts (infinite loop)
      - "is_spam: true"           # grok safety spam classifier result
      - "contains_slurs: true"    # safety classifier result

    # ALWAYS require approval — no exceptions regardless of trigger config
    always_require_approval_for:
      - "post_thread"
      - "reply_to_mention"
      - "create_pr"
      - "send_dm"
```

---

### 7. Error Recovery Triggers
```yaml
x_triggers:
  error_handling:
    on_rate_limit_error:
      strategy: "exponential_backoff"
      initial_delay_seconds: 60
      max_delay_seconds: 3600
      max_retries: 3

    on_api_error:
      strategy: "skip_and_log"
      notify_user: true

    on_content_filtered:
      strategy: "abort_and_notify"
      message: "Content was blocked by safety filter. No action taken."
      # Note: a blocked action is logged but NEVER retried automatically.
      # The human is notified and decides whether to revise and resubmit.
```

---

## Pro Tips

**Chain docs with a release workflow:**
```yaml
# In grok-workflow.yaml
steps:
  - name: "Regenerate Docs"
    action: "grok-docs"
    input: "all"
  - name: "Post Docs Announcement"
    action: "publish_thread"
    requires_approval: true
```

**Watch for documentation gaps via X search:**
Monitor `"how do I" grok -is:retweet` to surface undocumented features that
users are asking about on X — a leading indicator of docs debt.

**Combine staleness check + scheduled roundup:**
Run `check_docs_freshness` daily and feed its output into the Friday
`compile_weekly_docs_roundup`. If nothing changed all week, `skip_if_no_content`
keeps the roundup silent.
