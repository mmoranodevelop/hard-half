---
name: prd-spec
description: >-
  Use when builders need a spec: one named problem, RFC 2119 MUST with test and
  owner, non-goals, alternatives, privacy, rollout/kill. NOT for pr-faq, jobs-
  to-be-done, experiment-brief, launch-brief, or OpenAPI as the whole document.
license: MIT
---

# PRD Spec

**Builder SPEC** (markdown or docx): one named problem, RFC 2119 MUST/SHOULD/MAY in **ALL CAPS**, each MUST has test + owner, non-goals = declined plausible goals, alternatives, privacy/security/telemetry, rollout/kill/rollback. OpenAPI/TypeSpec = **annex**, not the PRD.

Method origin: RFC 2119 + RFC 8174; Malte Ubl public design-doc culture (not a Google template); Gerrit design-docs; SWE-book Ch.10 culture (search-confirmed); Azure REST guidelines (API annex language). Cagan / Pichler / Intercom = **wallpaper refuse**, not the stencil. No leaked Google/Meta template as official.

If they want a PRD lecture: one paragraph then produce or stop.

## When to use

- Discovery (or a signed PR/FAQ, or a job + decision to build) already exists
- Builders need behaviour, tests, owners, and a kill path
- API surface is an annex to a product decision

## When not to use

- Should we build it / customer narrative — [PR/FAQ](../../strategy/pr-faq/SKILL.md)
- Situation / motivation / outcome only — [Jobs to Be Done](../../strategy/jobs-to-be-done/SKILL.md)
- One test, one metric, one sample — [Experiment Brief](../../strategy/experiment-brief/SKILL.md)
- Customer-facing go/no-go this week — [Launch Brief](../../delivery/launch-brief/SKILL.md)
- Kill the **bet** — [Kill Criteria](../../strategy/kill-criteria/SKILL.md); last-sell of a feature — [Deprecation Notice](../../delivery/deprecation-notice/SKILL.md)
- Roadmap / outcomes — [OKR Cascade](../../strategy/okr-cascade/SKILL.md)
- OpenAPI file only — annex, or “not a PRD”
- Scientific manuscript — [Research Paper](../../documents/research-paper/SKILL.md)
- Filing the ask as a ClickUp/Jira/Asana ticket — `client-ticket` (this spec is not a ticket)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Problem named; discovery exists | Spec + MUST table + annex pointer |
| **redline** | Wallpaper PRD / lowercase must / OpenAPI-as-PRD | Force tests, owners, non-goals; strip laundry list |
| **refuse** | No discovery; MUST without test/owner; it is a PR/FAQ | Issues list. Stop |

## Hard rules

1. **One problem, one spec.** Feature laundry list / roadmap is not a spec (Cagan).
2. **RFC 2119 in capitals only** (RFC 8174). Spell the BCP 14 boilerplate once. MUST = interoperability or harm-prevention, not taste (§6). lowercase “must” has **no** special meaning — refuse if used as if it did.
3. **Each MUST = unique ID + owner + verification (test / demo / analysis) + pass/fail.** No test or no owner = a wish. SHOULD = weighed default. MAY = truly optional.
4. **Non-goals are load-bearing:** plausible goals **explicitly declined** (Ubl). “The system shouldn’t crash” is not a non-goal.
5. **Alternatives considered** with trade-offs. If there are none, you did not need a spec — write the code (Ubl) or you are in the wrong clock.
6. **Do not write instead of discovery** (Cagan). No evidence of value / usability / feasibility / viability → refuse; route to JTBD / experiment-brief / PR/FAQ.
7. Cross-cutting: privacy, security, observability/telemetry (how the success metric is measured). Rollout: staged / canary, feature flags, **kill of this feature in prod**, rollback. Launch go/no-go stays [Launch Brief](../../delivery/launch-brief/SKILL.md).
8. **OpenAPI / TypeSpec is an annex.** OAS has no non-goals, no kill, no privacy review. Do not paste formal IDL as the body (Ubl: it rots). Azure DO/YOU SHOULD language is for the API annex.
9. **No leaked-Google-template cosplay.** Cite Ubl / Gerrit / SWE-book / styleguide as culture, not an official Google form. No invented Meta stencil.
10. Freeze after ship (Chromium docguide: archive of decisions, not a half-correct wiki). New behaviour = dated amendment.
11. Length: Ubl ~10–20 pages typical; 1–3 page mini-doc is valid. A 50-page unread file is the SVPG failure mode.

## Intake

If **named problem** and **evidence discovery happened** are both missing after one round: issues list.

1. One named problem / primary use-case (load-bearing)
2. What was discovered, or signed PR/FAQ / job + go (load-bearing)
3. Non-goals: at least two plausible declines — or ASK
4. Who owns each MUST; who reviews; date
5. Success metric + guardrail + how measured
6. API surface Y/N (annex only)
7. Rollout / kill / rollback owners

## Output shape

Copy `assets/spec-skeleton.md`. Order: freeze the problem → alternatives → design → MUST table → cross-cutting → rollout → annex.

```
PRD / TECH SPEC  |  [one named problem]  |  [date]  |  Owner: [ ]
Status: [review / decided / archive]

BCP 14: MUST / SHOULD / MAY only when ALL CAPS, as shown here.

Context (facts, not a requirements dump)
Goals
Non-goals (declined plausible goals — not “don’t crash”)
Use-cases (primary vs secondary; secondary MAY be out of scope)
Acceptance = done
Design + trade-offs
Alternatives considered (one block each; conclusion dated)
MUST table: ID | MUST text | Owner | Test | Pass/fail
SHOULD / MAY
Privacy / security / telemetry
Rollout / kill-in-prod / rollback
Metrics (clock labelled: launch vs scale)
API annex pointer (OpenAPI/TypeSpec) — not the body

ASK: [decide this spec / name the missing owner / run discovery instead]
Owner: [ ]  Date: [ ]
Holes: [ ]
```

## QA (must pass) — one-screen fail list

1. One named problem. Not a laundry list. Not a PR/FAQ / JTBD / experiment / launch brief.
2. Non-goals are declined plausible goals.
3. Every MUST is ALL CAPS and has ID + owner + test.
4. Alternatives exist (or an explicit “solution is obvious — skip spec” stop).
5. Privacy/security/telemetry + rollout/kill/rollback present.
6. OpenAPI is annex, not the doc. No lowercase-must-as-BCP-14. No fake Google stencil.
7. ASK + owner + date. Discovery existed; this is not wallpaper.

If 1, 2, 3, or 7 fail: do not ship.

## Escalate / stop

- MUST without test or owner → issues list.
- PRD instead of discovery → refuse; route.
- “Paste the Google template” → refuse; use this spine.
- OpenAPI as the whole document → refuse.

## Related

- [PR/FAQ](../../strategy/pr-faq/SKILL.md) / [Jobs to Be Done](../../strategy/jobs-to-be-done/SKILL.md) / [Experiment Brief](../../strategy/experiment-brief/SKILL.md) / [Launch Brief](../../delivery/launch-brief/SKILL.md)
- [Document Kit](../../documents/document-kit/SKILL.md) — type/chrome only
