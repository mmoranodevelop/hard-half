# Worked examples

Illustrative. Facts you do not have stay **unknown**. The point is the shape of an honest run, including a no.

## 1. Load-bearing — do not displace

**Incoming:** "We've been fighting checkout latency for two quarters. Engineering wants to rethink whether latency is even the problem."

**Stated (mechanism-free):** complete a paid order in under T seconds on the P95 path the customer actually uses.

**Monday:** the on-call merchant success person, 14:00–16:00, still refunds carts that die at pay. **Unknown:** exact volume this week.

**Parent:** "maybe it's trust, not latency" — no Y that would evaporate the refunds without the seconds changing.

**Origin:** named PM, dated incident write-up still current.

**Verdict:** **Load-bearing.** Unseat-test: one week of P95 under T with refund volume unchanged → then hunt a ghost. Until that observation exists, do not reframe.

**ASK:** `keep stated`. Hand to `first-principles` if they now say the seconds cannot move.

## 2. Symptom — parent named

**Incoming:** "The backlog of 'data quality' tickets never shrinks. We keep hiring analysts."

**Stated:** "data quality" — still a slogan. Restate: records in store S disagree with source-of-truth R at a rate that breaks report G.

**Monday:** unclear; the analysts' Monday is *maintaining* the tickets.

**Parent:** two writers, no owner of R, no fence on write. Solving the write-ownership would close the disagreement tickets.

**Class:** symptom (of an unowned write), with inherited-slogan flavour on the epic name.

**Verdict:** **Displaced.** Confirmation: assign write-ownership on one entity type for two weeks; count new disagreement tickets on that type.

**ASK:** `confirm parent`. Do not open another data-quality workstream.

## 3. Dissolved — stop the ritual

**Incoming:** "We need a better vendor-risk committee. The current one is theatre."

**Origin:** committee created after a 2019 incident with a vendor no longer in the stack. Current vendors have a different control owner.

**Monday:** nobody outside the committee. The original cost is gone.

**Verdict:** **Dissolved.** Stop-work: do not redesign the committee. If a current control gap exists, that is a *new* stated problem with a current owner — intake it separately, do not inherit the 2019 name.

**ASK:** `stop the ritual`.

## 4. Refuse the brainstorm

**Incoming:** "Let's rethink the problem. Give me five framings."

No ticket, no owner, no shipped fix. **Refuse.** Issues list: stated problem, owner, what already shipped. Five framings without a Monday test are the failure this skill exists to prevent.
