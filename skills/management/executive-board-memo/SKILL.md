---
name: executive-board-memo
description: >-
  Write a decision-grade memo a CEO, ELT, or board uses to decide — for-
  decision, for-discussion, or for-noting papers and one-pagers a principal can
  sign. Use when the user asks for an executive decision memo, board paper, CEO
  letter to the board, or board covering memo. NOT for a strategy slide deck,
  NOT for a weekly operating review, NOT for a product PR/FAQ, and NOT for a
  status update with no ask.
license: MIT
---

# Executive / Board Memo

Write a decision-grade memo: the artifact a CEO, ELT, or board uses to decide, not a status email and not a slide deck.

Two modes, one skeleton. Classify first. Never feed a board template an operating review.

## When to use

Use this skill when the user asks to write, rewrite, review, or structure any of:

- an executive decision memo / action memo / ELT paper
- a board paper, board covering memo, CEO letter to the board, or board dashboard cover
- a "for decision / for discussion / for noting" paper
- a one-pager a principal can sign

## When not to use

Do not use this skill for:

- a strategy deck (slides)
- a full investment-committee memo + model (use an IC-memo skill)
- a weekly operating review / MOR pack
- a product PR/FAQ
- a status update with no ask
- a 40-page report whose first page is labelled "memo"

If the user wants a deck, a model, or a status note, say so and route away.

## Mode flag (mandatory first step)

Set `audience` to **elt** or **board**. If unclear, ask.

| | ELT / exec memo | Board paper |
|---|---|---|
| Reader | Manager who lives inside the P&L | Part-time director discharging a duty |
| Ask language | Decide / proceed / assign | Approve a **minutable resolution** / discuss / note |
| Jargon | Team-standard is fine | Define or cut |
| Ops detail | Expected | Appendix or omit |
| Discoverability | Internal | Write as if a court or regulator will read it |
| Options including do-nothing | Good practice | Required for decisions |
| Stakeholders / conflicts | Optional unless material | Mandatory on material items |
| Covering layer | Not needed | Covering memo + CEO letter + dashboard |
| Success test | A decision gets executed | Directors can show they were informed; minutes can record a resolution |
| Failure mode | Slow ops | Uninformed approval |

Routing rule: if the reader is a director acting as a director, use Board-Ready Paper. If the reader is a manager acting as a manager, use the exec memo. Never mix.

Also classify **paper type** (one only):

- **FOR DECISION / FOR APPROVAL** — a yes/no/conditional; board papers need a draft resolution
- **FOR DISCUSSION / FOR ADVICE** — judgement sought; still needs a clear question
- **FOR NOTING / FOR INFORMATION** — on the record as seen; never smuggle an approval
- **FOR RATIFICATION** — action already taken under delegated authority; high legal sensitivity
- **FOR RECOMMENDATION** — committee-to-board

If two types are needed, split into two papers. One topic per paper.

## Method (public, fused)

Four traditions converge on one operating rule: **the reader must be able to decide after one rapid reading.**

1. **Pyramid Principle (Minto).** Governing thought is a complete-sentence claim, not a topic. Think bottom-up, present top-down. 2–4 MECE reasons; if they are all true, the recommendation must be true.
2. **SCQA / SCR.** Situation → Complication → (Question) → Answer is the *opening*, not the whole memo. Flip to answer-first (RSC) when the audience already leans toward the recommendation.
3. **BLUF (Army AR 25-50).** Main point and required action in the first sentences. Active voice. Understood in a single rapid reading.
4. **Narrative constraint (Bezos / Amazon).** Complete sentences; data inside the prose; no presenter required. Default is **not** a 6-pager.

Board papers add **CQC** (Context, Questions, Conclusions) on page 1, a minutable resolution, and a fiduciary completeness test (FRC four-line standard; AICD / Governance Institute paper taxonomy; NACD pack checklist).

Type 1 vs Type 2 (Bezos 2015/2016): irreversible / one-way-door decisions need method and consultation. Reversible Type 2 decisions should be made at ~70% information with a kill criterion. Do not run Type 2 through a Type 1 process.

## Inputs — ask before writing

Refuse to draft a FOR DECISION paper until the decision and the decider are named. If they cannot answer "what is the decision?" and "who decides by when?", write an issues list, not a fake decision memo.

Ask in this order. Skip what is already in the brief. Do not interview for sport.

### Always

1. **Audience:** named decision-maker and title. ELT or board? Who else reads it?
2. **The decision, one sentence, with a verb:** approve / fund / kill / sign / hire / enter / exit / note / discuss.
3. **Paper type** (list above).
4. **Deadline and action-forcing event.** Cost of delay if they do nothing.
5. **What they already believe.** What they have said no to.
6. **Headline numbers** that move the decision, with source and date.
7. **Real options**, including do-nothing. Why losers lose.
8. **Owner the day after yes**, first action, date.
9. **Linchpin:** the assumption that, if false, reverses the recommendation.

### Add for board mode

10. Meeting type, date, jurisdiction / code (UK Code, ASX, NYSE, PE SHA, charity, regulated FS).
11. Why this is a **board** matter (matters reserved, materiality, legal, reputation) vs delegated.
12. Draft resolution, including any delegation to named officers.
13. Conflicts / related parties / recusals.
14. Committee already seen it? Their recommendation?
15. Legal, risk, and Finance sign-off status.
16. Stakeholder groups affected (workforce, customers, suppliers, community, environment, creditors).

If a load-bearing number is missing on a Type 1 / board item, the memo's job is to say so and ask for a gated decision (e.g. approve diligence spend of $X to resolve Y by DATE). Do not fake certainty.

## Workflow

### Phase 0 — Classify

Pick audience, paper type, and length:

| Job | Artifact | Default length |
|---|---|---|
| One ELT decision | Template A — 1-page exec memo | ~400–700 words, one page |
| Same decision plus execution path | Template B — 2–3 page action memo | Still one decision |
| Orient the board pack | Template C — board covering memo | 1–2 pages |
| Board approval | Template D — board decision paper | Body 2–4 pages + appendices |
| Performance cover | Template E — one-page dashboard | One page; red cells link to papers |
| Inform, no ask | Information / noting paper | One page; never labelled FOR DECISION |

Default to Template A for ELT. Expand to B only when implementation is in-scope. Do not default to an Amazon 6-pager. Do not write a 40-page report and call page 1 a memo.

### Phase 1 — Think (do not write yet)

1. Answer the input questions. Stop if the decision is undefined.
2. Dump evidence. Group. Draw insights. Build the pyramid on paper.
3. Draft SCQA in four lines and the ask in one sentence: body, verb, option, scale, outcome, date.
4. List 2–4 MECE reasons. MECE-check. Linchpin-check.
5. List options + rejects. Top 3 risks with likelihood, impact, mitigation, owner.
6. **Readiness gate:** a colleague who was not in the work can restate the recommendation, the ask, and the main risk in 60 seconds. If not, keep thinking.

Board extra: write the draft resolution first, then the ASK line, then the CQC page, then the body that proves it. Move evidence to appendices. Reconcile every number to the CFO pack.

### Phase 2 — Write from the top

Order of writing is not order of thinking.

1. Header (To / From / Date / Re / classification).
2. BLUF / governing thought + ask (first 3–8 lines). Board: draft resolution on page 1.
3. Compressed SCQA (or CQC for board).
4. Rationale — headings that **are claims**, not topics.
5. Options including do-nothing.
6. Risks, linchpin, contrary fact, minority view.
7. Implementation / owner / date / fallback. Board: legal, stakeholders, process/advice relied on.
8. Decision block (Approve / Approve with conditions / Reject / Discuss) or minutable resolution.

Write in complete sentences, active voice. Numbers live in the sentence, not only in a table. Bold the recommendation, the ask, the headline numbers, and the date.

### Phase 3 — Edit for a single rapid reading

- Cut fillers: actually, generally, very, moreover, "it is important to note."
- One idea per paragraph; main idea in the first two sentences.
- Re line contains the decision, not the project name.
- Every number matches the source exhibit.
- White space. If you cannot fit white space, you have not cut.
- Appendix is optional. Never make it required reading for the decision.
- Board: bad news in the body, not the appendix. No new facts in the room.

### Phase 4 — Gate before delivery

Run the quality checklist below. If it fails, rewrite. Do not send a failing paper.

## Output templates

Fill every bracket. Delete a section only when it truly does not apply, and say so (e.g. "Legal: GC confirmed no listing-rule issue, 12 Aug").

### Template A — 1-page executive decision memo (default ELT)

```
MEMORANDUM

TO:           [Decision-maker, title]
FROM:         [Author / team — named]
DATE:         [YYYY-MM-DD]
RE:           [DECISION verb + object + date]
CLASS:        FOR DECISION
CC:           [Who else will see this]

1. BLUF / RECOMMENDATION
[Complete-sentence governing thought.] Recommend that [decision body]
[approve / reject / approve-with-conditions] [Option X] [amount / scope]
by [date] in order to [outcome metric].

Why this, why now: [Complication in one sentence].
Cost of delay: [what breaks if we slip past the action-forcing event].
Headline numbers: [the 2–4 figures that move the decision].

2. CONTEXT (SCQA, compressed)
S: [Facts already agreed.]
C: [What changed / the tension.]
Q: [Decision question — omit if BLUF already states it.]
A: [Recommendation, if not fully spent in §1.]
Do not retell the project history.

3. RATIONALE
Each heading is a claim. 2–4 MECE reasons. If all are true, the BLUF must be true.
• [Reason 1 — claim.] [1–2 numbers or facts. Source/date.]
• [Reason 2 — claim.] [evidence]
• [Reason 3 — claim.] [evidence]

4. OPTIONS CONSIDERED
| Option | What it is | Outcome / cost | Why it wins or loses |
| A Do nothing | | | |
| B [Recommended] | | | |
| C [Serious alternative] | | | |

5. RISKS AND LINCHPIN
Top 3 only.
• [Risk] — likelihood / impact — mitigation — owner.
Linchpin (if this is false, reverse): [assumption]. Watch [indicator] by [date].
Minority view (if any): [one sentence].

6. ASK AND DECISION BLOCK
Ask: [body, verb, option, scale, outcome, date.]
Owner after yes: [name/role]. First action: [what] by [date].
If deferred: [consequence].

DECISION
[ ] Approve as written
[ ] Approve with conditions: __________________
[ ] Reject
[ ] Discuss — hold for [date]
Signature / date: __________________
```

### Template B — 2–3 page action memo

Same header and BLUF as A. Then:

1. BLUF AND ASK (~½ page) — do not save the ask for the end.
2. SITUATION AND COMPLICATION (~¼ page) — SCQA as prose; state framing assumptions as assumptions.
3. OPTIONS AND RECOMMENDATION (~½–¾ page) — including do-nothing and reversibility (Type 1 vs 2). Fallback if the preferred option dies.
4. RATIONALE (~½–¾ page) — default pillars if none are obvious: (i) strategic fit / why now, (ii) economics, (iii) risk and execution.
5. RISKS, LINCHPIN, CONTRARY FACTS (~⅓ page) — what would change our mind.
6. IMPLEMENTATION (~⅓–½ page) — 30/90 days, stage gates, decision rights, kill criteria.
7. DECISION BLOCK — conditions as testable clauses, not vibes.

Page 1 = BLUF + SCQA + options. Page 2 = rationale + economics. Page 3 = risks + implementation + decision block. Methodology goes to an appendix or is cut.

### Template C — Board covering memo (CoSec + Chair, 1–2 pages)

```
[Company]  BOARD COVERING MEMO
Meeting of the Board of Directors  |  [date, time, place / video]
From: [Company Secretary]  (agreed with the Chair)
To:   All directors  |  Copy: CEO, CFO, GC
Classification: Confidential — Board only
Pack version: [vX.Y]  |  Distributed: [date]  |  Late items: [none / list]

1. Purpose of this meeting
   The Board is asked to [the 1–3 real jobs]. Routine performance is in the
   dashboard and is taken as read.

2. How to read this pack
   (1) This memo  (2) CEO letter  (3) One-page dashboard
   (4) Decision papers in agenda order  (5) Discussion papers
   (6) Noting / committee reports  (7) Appendices only as needed.

3. Agenda map
 # | Paper | Type | ASK (one line) | Owner | Time | Pre-read

4. Items that must not be truncated
5. Conflicts, related parties, privilege, recusals
6. Late / tabled papers (none, or Chair-approved reason)
7. Committee referrals already done
8. Consent / unstarred items

The Chair will treat circulated papers as taken as read. Presenters start at the ASK.
```

### Template D — Board decision paper (body 2–4 pages + appendices)

```
[COMPANY]  BOARD / [COMMITTEE]  |  [meeting date]  |  Agenda item [#]
Title:  [same as agenda]
Paper type:  FOR DECISION
Author: [name, title]   Sponsor: [name, title]   Presenter: [name]
Date of paper: [YYYY-MM-DD]   Version: [n]   Time requested: [mins]
Classification: Confidential — Board   Privilege: [none / restrict]

DRAFT RESOLUTION
THAT the Board approve [precise, stand-alone action], and delegate to
[named officer(s)] authority to [execute on terms not materially less
favourable than those described in this paper], and that the Company
Secretary be authorised to do all things necessary to give effect to
this resolution.

EXECUTIVE SUMMARY (CQC — max 1 page; directors should be able to act from it)
Context (why this, why now, link to strategy)
Questions this paper answers (3–5, MECE)
Conclusions (answer each question; no suspense)
Input sought (APPROVE the draft resolution; invite challenge on the 1–2 genuine uncertainties)

1. Purpose and context
2. Recommendation and why
3. Options (including do nothing) — table: option, value, cost, key risks, residual, why not preferred
4. Strategic alignment (or explicit that it is opportunistic)
5. Financial and resource implications (CFO-reviewed). Statement:
   "Figures reconcile to the [Month] CFO pack, version [n]."
6. Risk analysis — include the risk of doing nothing
7. Legal, regulatory, governance — GC review; related-party / conflict map; recusal
8. Stakeholders (s.172 or equivalent)
9. Implementation — owner, milestones, when the Board next hears, kill-criteria
10. Process and advice relied on — who challenged this; external advisers (name, date, scope); divergent views
11. Next steps if approved / if not approved

Sign-off: CEO, Sponsor, CFO (if financial), GC (if legal), CoSec (quality gate)
Appendices: evidence, not argument. Model, legal note, adviser letter.
```

Discussion variant: type FOR DISCUSSION; still needs questions and options. Noting variant: "The Board note the contents of this paper"; no hidden ASK.

### Template E — One-page board dashboard cover

```
[COMPANY]  BOARD DASHBOARD  |  Period to [date]  vs  plan / prior / LTM
Owner: CFO   Reviewed: CEO   Red items have a paper behind them.

Overall (one sentence): Performance [ahead/in line/behind] because [cause].
Decisions flagged by these numbers: [none / see papers #x, #y]

KPI | Actual | Plan | Δ | Prior | Trend | Status | So what / action
[Revenue, margin, EBITDA/FCF, net debt/runway, covenant headroom,
 orders, quality, safety, people, cyber, 2–3 strategy KPIs]

Red / amber commentary on this page. Each red cell points to a paper.
Forward look (90 days): 3 bullets. No new surprises.
Reconciled to: [CFO pack v#]. Changes vs last Board dashboard: [restatements].
```

A dashboard never carries a capital, M&A, going-concern, related-party, or safety-incident decision by itself.

## Quality checklist

### ELT memo

- [ ] One decision. Mixed issues were split.
- [ ] Re line is a decision, not a project name. CLASS is honest (FOR DECISION vs information).
- [ ] BLUF is a complete-sentence claim. Ask has body, verb, amount, date.
- [ ] Cost of delay is priced.
- [ ] 2–4 MECE reasons; headings are claims.
- [ ] Real options including do-nothing; losers lose for a stated reason.
- [ ] Top risks ≤3 in the body, each with owner and mitigation. Linchpin named.
- [ ] Named owner and date after yes.
- [ ] Numbers in sentences, sourced, internally consistent.
- [ ] Complete sentences, active voice, single rapid reading (1 page default).
- [ ] Decision block present. No "happy to discuss" as the ask.

### Board paper (add these)

- [ ] ASK labelled on page 1 and matches the type. No approval inside a noting paper.
- [ ] Draft resolution is minutable without amendment and stands alone.
- [ ] Named author, sponsor, presenter, date, version.
- [ ] CQC executive summary ≤1 page.
- [ ] Why this is a board matter; why now; strategy link or "opportunistic."
- [ ] Options including do-nothing; process that challenged the proposal.
- [ ] Money, risk, legal, stakeholders, implementation, residual risk in the **body**.
- [ ] Numbers reconcile to the CFO pack. Statement of reconciliation present.
- [ ] Conflicts / RPTs mapped; recusal described; privileged material marked.
- [ ] Bad news in the body. No surprises planned for the room.
- [ ] Altitude: if it belongs in Monday's operating review, it is not in the board body.
- [ ] Duty-of-care test: would this file let a director show they were informed?
- [ ] FRC four-line test: accurate/clear/comprehensive/up-to-date; contains a summary; tells the director what is expected of them; delivered in time.

## Escalation — do not auto-resolve

A memo prepares a decision. It does not replace the human who holds the liability.

Escalate to the named principal (and for board papers: Chair + GC + CEO). Delay the item rather than fake completeness.

**Always human:**

1. Legal: contract, filing, privilege, employment, fiduciary duty.
2. Reputational / public / regulator / earnings.
3. Type 1 irreversible capital: acquisitions, closures, one-way architecture, public accusations.
4. Missing linchpin data on a Type 1 or board item.
5. True misalignment, not a facts gap.
6. Safety / life / security.

**Board papers that must never be a thin memo or a dashboard cell:**

- Capital allocation, large capex, dividends, buybacks, leverage
- M&A / disposals / takeovers
- Going concern / viability / solvency
- Legal exposure, investigations, privilege
- Related-party / conflicted transactions
- Safety, clinical, environmental, modern slavery, mission-critical ops
- Cyber / data material incident
- CEO / chair succession, executive remuneration
- Auditor independence / control failures
- Ratification of a fait accompli ("management already signed")

**Stop-the-machine triggers:**

- Author cannot state the ASK in one sentence
- Numbers in the paper ≠ numbers in the CFO pack
- Options missing or straw-man
- Related party not mapped
- Legal has not seen a paper that creates disclosure, privilege, or liability
- Material decision tabled on the day
- Going-concern, safety, or cyber treated as FYI
- A director could later say "I did not see that"

Type 2 (reversible) ELT choices: a 1-page memo with a 70% recommendation, explicit kill criterion, and named owner is the correct artifact. Do not over-process.

## Anti-patterns (refuse these)

1. Mystery novel — chronology of the work, punchline on page 3.
2. Buried ask — "happy to discuss," "endorse the direction," "align."
3. Vague verbs — consider, explore, leverage, optimize, socialize.
4. Topic headings — "Background," "Analysis," "Next steps" instead of claims.
5. Mixed issues in one paper.
6. No owner, no date, no version.
7. Adjectives without figures ("significant," "many").
8. Bullet soup in a Word doc (PowerPoint by other means).
9. Data dump with no synthesis.
10. Fake options (two unusable extremes and the pre-chosen middle).
11. Hidden uncertainty / stacked hedges. Label confidence: high / moderate / low.
12. Methodology theater in the body.
13. Presenter-dependent — unreadable without a voice-over.
14. Wrong scope — 6-pager for a Type 2, or a Type 1 run as a Slack message.
15. Two asks taped together.
16. No cost of delay.
17. Jargon and undefined acronyms (fatal for NEDs).
18. Passive voice.
19. Risks without mitigations, or "monitor closely" as a mitigation.
20. Inconsistent numbers across summary, body, and model.
21. Recycled ELT pack labelled as a board pack.
22. Noting paper that is actually a decision.
23. Warts hidden in Appendix F.
24. Circular resolution for a contentious item.
25. Consent-agenda abuse for material items.

## Voice and constraints

- Lead with the answer. One decision. Explicit ask.
- Complete sentences. Active voice. Numbers in the prose.
- Write for the least-immersed reader who still has to decide.
- Do not invent facts, figures, legal conclusions, or "McKinsey says" internal playbooks. If a number or a legal position is unknown, say it is unknown.
- Do not impersonate counsel. Flag legal questions; do not give legal advice.
- Public method only. The fusion above is a reconstruction from public sources, not a licensed firm template.

## After writing

Return:

1. The memo in the chosen template, ready to send.
2. A 5-line cover to the user: artifact type, audience, the ASK, residual risks, anything that blocked a clean recommendation.
3. Open questions still on the principal, if any.

If reviewing someone else's draft, do not rewrite first. Score it against the checklist, name the three highest-leverage fixes, then offer a rewrite.
