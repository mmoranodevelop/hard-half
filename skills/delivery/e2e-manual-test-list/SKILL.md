---
name: e2e-manual-test-list
description: >-
  Use when designing a MANUAL end-to-end test inventory for an app, web app, or
  enterprise system from PRD / stories / AC / Figma — prioritized list humans
  (or later automation) execute. Not Playwright scripts, not a11y audit, not
  pen-test, not go-live gate.
license: MIT
---

# E2E Manual Test List

**Prioritized manual E2E test inventory + one control page** — journeys, risk heat, Smoke/P0 pack, full list counts, gaps, one ASK. Default: product / program release; same spine for F500 SIT→UAT.

Method origin: ISTQB black-box techniques (EP / BVA / decision tables / state / use-case) + risk-based prioritization (impact × likelihood) + scenario / E2E path coverage — operator inventory, not a syllabus.

If they want an ISTQB / RBT lecture: one paragraph then produce or stop.

## When to use

- Release needs a human-executable E2E / SIT / UAT candidate list from docs or mockups
- QA lead / PM must show what is P0 vs deferred and what residual risk remains
- Acceptance or go-live will consume a pack — design the list first
- Pasted "test cases" are a novel, missing priorities, or invent expected results

## When not to use

- Client signs evidence against agreed tests — [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md)
- Go / no-go of the live event — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Hour-by-hour cutover — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- Writing / rewriting the PRD — [PRD Spec](../../documents/prd-spec/SKILL.md)
- Automating the suite (Playwright et al.) — stop; redline may only flag *convert-later* candidates
- Full WCAG audit or penetration test — not this skill (optional smoke rows only if in scope)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named SUT + artifacts | Control page + inventory (+ packs) |
| **redline** | They pasted a bloated / vague list or "automation scripts" labelled E2E | Force risk, packs, trace, kill invented expected; list what you cut |
| **refuse** | Two load-bearing facts missing, or they want scripts / coverage % theatre / pen-test | Issues list. Stop |

## Hard rules

1. **Clarify SUT first:** product, release/build, environments, roles/personas. Missing build or env → hole, not fiction.
2. **Journey map before techniques.** Critical E2E paths first; expand with EP / BVA / decision table / state / negative **only where risk warrants**.
3. **Risk every candidate:** business impact × likelihood of failure (and change frequency when known). Map to P0–P3. Relative scores only.
4. **Never invent product behaviour.** Docs silent → expected = `[UNCLEAR — need AC]`. Do not fake pass criteria.
5. **Never invent coverage %.** BLUF = journeys claimed + P0 count + top residual risk. No "87% covered."
6. **Separate packs:** Smoke/P0 · Full E2E · UAT candidate. Smoke is a gate subset, not the whole list.
7. **Trace or hole.** Every row → requirement / AC / mockup frame — or mark gap.
8. **One ASK** with owner to unblock missing AC / env / data fixtures. Do not "monitor."
9. **Not automation scripts.** High-level actionable steps. Redline may note convert-later; do not write Playwright here.
10. **a11y / security = optional checklist rows only if in scope** — do not turn this into audit or pen-test.
11. **One control page + inventory table** — not a textbook.

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake inventory.

1. SUT — product / surface, release or build id, environments — load-bearing
2. Artifacts — PRD / stories / AC, Figma/flows, and/or API contracts — load-bearing
3. Personas / roles in scope — load-bearing
4. Known defects, prior bugs, change hotspots
5. Explicit out-of-scope
6. Who owns missing AC / fixtures (for the ASK)
7. Whether UAT pack is required this release

## Output shape

```
E2E MANUAL TEST LIST  |  [product]  |  [release/build]  |  as-of: [date]
Env: [ ]     Personas: [ ]     Owner: [QA lead / PM]

ASK: [owner] to [provide AC / env access / data fixtures / Figma frame] by [date].

BLUF
Coverage claim: [n named journeys in scope]. P0/smoke: [n]. Top residual risk: [one line].
Do not claim a coverage percentage.

SCOPE / OUT OF SCOPE
In: [surfaces, journeys, roles]
Out: [named — deliberate]. Untested ≠ out-of-scope unless listed here.

JOURNEY MAP
| Journey | Persona | Criticality | Source (AC/mockup) |
| [name] | [ ] | H/M/L | [ ] |

RISK HEAT (top)
| Area / journey | Impact | Likelihood | Why | Pack |
| [ ] | H/M/L | H/M/L | [≤12 words] | smoke-p0 / full / uat |

SMOKE / P0 PACK (executable)
| ID | Title | Preconditions | Steps (high-level) | Expected | Trace |
| [ ] | [ ] | [ ] | [ ] | [doc or UNCLEAR] | [ ] |

FULL LIST — summary counts
P0: [n]  P1: [n]  P2: [n]  P3: [n]
By type: happy [ ] alt [ ] exception [ ] neg [ ] regression [ ]
UAT candidates: [n]     Inventory: assets/test-case-row.md

GAPS / UNCLEAR
| Hole | Blocks | Owner needed |
| [missing AC / frame / fixture] | [which IDs] | [ ] |

NOT THIS PAGE
Automation scripts → elsewhere (flag convert-later only)
Performance soak → elsewhere    Pen-test / full a11y → elsewhere
Acceptance signature → acceptance-signoff    Go/no-go → go-live-readiness
```

Inventory rows: `assets/test-case-row.md` (ID, title, preconditions, steps, expected, P0–P3, type, trace, pack).

## QA (must pass)

1. SUT, release/build, env, personas named (or holed).
2. Journey map present before the long list.
3. Each shipped row has priority, type, expected from docs **or** `[UNCLEAR — need AC]`.
4. No invented expected results; no coverage %.
5. Smoke/P0 pack is a subset and executable.
6. Full list counts by priority and type.
7. Gaps section lists what docs could not support.
8. One ASK with owner and date.
9. Not a Playwright file; not an ISTQB essay; not pen-test/a11y project.

If 3, 4, 5, or 8 fail: do not ship.

## Escalate / stop

- No product / no artifacts after one ask → refuse.
- They demand automation scripts as the deliverable → refuse; point convert-later only under redline.
- They demand a fake coverage % → refuse the theatre.
- Docs so thin every expected is UNCLEAR → issues list + ASK; do not invent a green pack.
- Live go/no-go is the question → [Go-Live Readiness](../../project/go-live-readiness/SKILL.md).
- Client must sign → [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md).

## Related

- [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) — signs evidence this list may feed
- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — gate that may consume P0 results
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — hours; not test design
- [PRD Spec](../../documents/prd-spec/SKILL.md) — intake source
- [Launch Brief](../../delivery/launch-brief/SKILL.md) — external launch narrative; not the inventory
- [RAID Register](../../management/raid-register/SKILL.md) — program risks; this page treats product test risk
