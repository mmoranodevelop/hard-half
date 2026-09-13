# Worked examples

Illustrative. Numbers that are not sourced are **assumed** or **unknown**. The point is the shape of an honest run, including a no.

## 1. Audit — refuse the kind verdict (engagement streak)

**Candidate:** a streak + daily-nudge feature on a learning app. The team wants it because "retention is value."

**Mode:** Audit (the feature is specified and about to ship).

**Named:**
- Who — weekly self-learners who already open the app 2–3 times a week **(assumed segment; not verified)**
- State change — from "I forget to practice" to "I practice most days"
- Today — calendar reminders, guilt, a paper habit tracker
- Beat — doing nothing; a calendar reminder they already have

**Filters (compressed):**

| Filter | Status | Note |
|---|---|---|
| 1 Real problem | unknown | Forgetting is real; whether it *hurts enough to change* is unverified |
| 2 Efficacy | unknown | Streaks raise opens in demos; practice quality unmeasured |
| 3 Validation | fail | Team excitement and a competitor screenshot, no behavior test |
| 4 Communication | pass (assumed) | "Don't break your streak" is instantly understood |
| 5 Access | pass | Already in the app |
| 6 Sustainability | fail-risk | The model earns on daily opens. If streaks drive opens without learning, capture detaches from creation |
| 7 Integrity | **fail** | Incentive is aligned with compulsion, not with "I wanted to use it less." Headline test fails. Users who miss a day are punished. Reversibility of the guilt load is poor |

**Formula:** Adoption of opens may rise while relevance-to-learning is unknown. Friction of anxiety sits in the denominator for a subset. Integrity veto fires — do not average.

**Verdict: Extracts** (or will, if shipped as specified). Weakest filter: 7, then 3.

**Kill experiment:** ship the streak to 10% with an explicit "I want to practice less often but better" cohort. Kill if weekly *practice quality* is flat and "I wish I opened it less" rises **(measure: assumed instrument; must be designed)**.

**Do not:** report "high engagement = value."

## 2. Audit — hypothesis, not creation (vendor "AI inbox")

**Candidate:** a vendor proposal to put an LLM on every employee inbox to "save 5 hours a week."

**Named:**
- Who — knowledge workers who triage email as their job **(segment too wide — hole)**
- State change — from "I drown in email" to "I only see what needs me"
- Today — rules, assistants, ignoring it, a second human
- Beat — a competent assistant or a ruleset; doing nothing

**Filters:** 1 is a real pain **(verified anecdotally, n unknown)**. 2 is **assumed** (demo on a clean mailbox). 3 is fail (no behavior in *this* org). 4 is pass-ish (the promise is clear). 5 may fail (trust, mis-send risk, training). 6 unknown (token cost at 100×). 7: who reads mail the model got wrong? Consent of senders whose mail is ingested is often not on the page.

**Verdict: Hypothesis.** The load-bearing assumption is "saves 5 hours of *real* work, not 5 hours of watching the model." Weakest filter: 3.

**Kill experiment:** ten people, two weeks, measure messages they still handle and errors they catch. Kill if hours-saved is self-report only.

This is not `first-principles`. Nothing here is a physics floor. It is also not `prd-spec` — no builder MUST list belongs on this page.

## 3. Design — walk the filters before the PRD

**Candidate:** "We should build a shared decision log for the leadership team."

**Mode:** Design (nothing exists yet).

**Named (after one ask):**
- Who — a six-person leadership team that re-litigates decisions made last month
- State change — from "we thought we decided" to "we can point at the decision, the owner, the date, and what would reopen it"
- Today — Slack archaeology, conflicting decks, the loudest memory
- Beat — a notes doc nobody opens; doing nothing and paying the re-litigation

**Filters as intended (all assumed until tested):**

| Filter | Intended | Hole to close first |
|---|---|---|
| 1 | Pass — they already spend meeting time re-arguing | Confirm with two weeks of counted reopens **(unknown count)** |
| 2 | A one-page log changes the reopen rate | Define "reopen" before building |
| 3 | Not done | Smallest test: a shared doc, one week, one team, no product |
| 4 | Promise: "the decision, the owner, what reopens it" | Fine |
| 5 | Habit change is the cost | If logging takes more than two minutes, adoption dies |
| 6 | A doc is enough for three years; a product is not required | Do not build a system until the doc fails for a named reason |
| 7 | Pass — no off-books victim | Watch for a log used as ammunition against absentees |

**Guardrails:** reversible (it is a doc). Incentives aligned if the team wants fewer reopens, not if someone wants a paper trail to trap colleagues — name that.

**Design output:** do **not** write a PRD. Run a paper log for ten working days. Kill the product idea if reopens do not drop. Promise: "We can point at what we decided, who owns it, and what would make us reopen it."

**Not built yet:** workflow engine, integrations, permissions model.

## 4. Stop — this is the neighbour

**Incoming:** "Our cost per transaction cannot go under €14; legal says AML makes it impossible."

Do not run the filters. That is a stuck-floor claim. Invoke `first-principles` (or say so and stop). A value pass here would produce a polite essay about "relevance" and miss the floor.
