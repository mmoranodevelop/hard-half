---
name: acceptance-signoff
description: >-
  Use for client UAT / acceptance of named deliverables: tests, evidence, named
  acceptor, fail path. NOT for vendor-sow (buying the tests), not project-close,
  not go-live-readiness.
license: MIT
---

# Acceptance Signoff

**Client Acceptance — Named Deliverables** — one page: tests run, evidence, named acceptor, accept / conditional / reject, fail path (rework / credit / stop). Default: venture program; same spine for F500.

Method origin: UAT sign-off public craft (exit criteria, evidence pack, named authority, accept / conditional / reject) — operator cut, not ISTQB.

If they want a UAT / ISTQB lecture: one paragraph then produce or stop.

## When to use

- Client must accept named deliverables (UAT, milestone, product)
- Tests exist (or must be written) and someone with authority must sign
- Conditional accept needs defects with owners and dates, not "we'll fix it"
- An email "LGTM" is being treated as acceptance

## When not to use

- Buying the vendor / writing the tests into paper — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Ending the project after signature — [Project Close](../../project/project-close/SKILL.md)
- Go / no-go of the live event — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Hour-by-hour live run — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- Vendor monthly pass/fail — [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md)
- Who is A on the UAT row — [RACI Delivery](../../project/raci-delivery/SKILL.md)
- Accept-with-conditions moves the signed baseline — [Change Control](../../project/change-control/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named deliverables | One-page sign-off + ASK |
| **redline** | They pasted a 40-case sheet or "LGTM" | Force tests, evidence, acceptor, fail path |
| **refuse** | Two load-bearing facts missing, or a QA lecture | Issues list. Stop |

## Hard rules

1. **Clock is this signature.** SOW bought the tests; this page runs and signs them; close ends the project. Mixing the three is a fail.
2. **Tests are pass/fail.** "Client will review" is not a test. If criteria were never agreed, write them as a hole — do not fake a sign-off.
3. **Evidence or it did not happen.** What was run, by whom, when, on which build/environment.
4. **One named acceptor.** "The business" is not an acceptor. PM countersign is optional; client A is mandatory.
5. **Decision is Accept / Accept with conditions / Reject.** Conditions = each open defect has owner, date, workaround. P1 open + Accept = fail unless the acceptor writes the residual.
6. **Fail path is on the page:** rework window, credit, stop, slip go-live. If reject two days before go-live would still ship, say so — ceremony.
7. **Do not invent pass counts or defect severity.** Holes stay holes.

## Intake

If **two** of 1, 3, 4 are missing after one round: issues list, not a fake sign-off.

1. Named deliverables (version / build / environment) — load-bearing
2. Tests / criteria already agreed (from SOW/charter) or "none"
3. Named acceptor — client person with authority — load-bearing
4. Results they have (pass/fail counts) or "not run" — load-bearing
5. Open defects (severity) or "unknown"
6. Fail path already written? (rework / credit / stop)
7. By when the signature is needed; who owns the ASK

## Output shape

```
CLIENT ACCEPTANCE  |  [project]  |  [client]  |  [deliverable / milestone]
Build / env: [ ]     Tests run: [dates]     Acceptor (A): [name, title]
PM: [name]     SOW / charter pointer: [ ]     as-of: [date]

ASK: [acceptor] to ACCEPT / ACCEPT WITH CONDITIONS / REJECT by [date].
Owner of ASK: [acceptor]     Decide-by: [date]

TESTS
| ID | Test (pass/fail) | Result | Evidence (where) | Tester |
| [ ] | [ ] | pass / fail / blocked / not run | [ ] | [ ]
Run: [n]  Pass: [n]  Fail: [n]  Blocked: [n]  Not run: [n]

DEFECTS STILL OPEN
| ID | Sev | Workaround | Owner | Fix-by | Acceptor accepts residual? |
| [ ] | P1/P2/P3 | [ ] | [ ] | [ ] | Y/N |

DECISION: ACCEPT / ACCEPT WITH CONDITIONS / REJECT
Fail path if Reject: [rework by date / credit / stop / slip go-live]
If we would ship anyway on Reject: [say so — ceremony]

NOT THIS PAGE
Buying tests → vendor-sow    End project → project-close    Live event → go-live-readiness

Holes: [ ]
```

## QA (must pass)

1. Named acceptor + as-of date.
2. ASK is accept / conditional / reject by a date.
3. Every test has pass/fail wording (or not-run).
4. Evidence pointer, not "LGTM".
5. P1 open on Accept has a written residual.
6. Fail path on the page.
7. Not an SOW and not a project-close pack.
8. No invented pass counts.
9. One page.

If 1, 2, 6, or 8 fail: do not ship.

## Escalate / stop

- No acceptor after one ask → refuse.
- Tests never agreed and they want a signature anyway → issues list; criteria first, not a fake accept.
- Vendor wants "accepted on delivery" with no tests → refuse; [Vendor SOW](../../management/vendor-sow/SKILL.md) is broken.
- They want to close the project on this page → [Project Close](../../project/project-close/SKILL.md) after signature.
- Regulated / safety acceptance → specialist; this page still names the A.

## Related

- [Vendor SOW](../../management/vendor-sow/SKILL.md) — bought the tests this page runs
- [Project Close](../../project/project-close/SKILL.md) — after acceptance, end the project
- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — live event uses this evidence
- [RACI Delivery](../../project/raci-delivery/SKILL.md) — who is A/R on UAT
- [Vendor Scorecard](../../management/vendor-scorecard/SKILL.md) — monthly pass/fail, not this signature
- [Change Control](../../project/change-control/SKILL.md) — if conditions move the baseline
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — hour-by-hour after this evidence exists
