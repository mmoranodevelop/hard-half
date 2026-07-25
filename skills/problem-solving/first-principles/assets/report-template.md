# First-principles analysis: [problem]

> Delete the guidance in brackets as you fill each section. Lead with the answer.
> Every number carries a label: **(measured)**, **(cited: source)**, **(estimated: derivation)**, **(assumed)**.
> An unlabelled number is a defect — it makes an assumption look like a fact.

---

## Verdict

[Two or three sentences. What is actually true about this problem, and what should be done about it. If the answer is "the objective is the problem" or "impossible as posed", say it here, in the first line, not on page four.]

**Gap ratio: [N]×** — [current value] against a floor of [floor value] on [metric].

**Recommended next action:** [the single cheapest thing that would most reduce uncertainty]

---

## 1. The objective, restated

**Stated as:** [the problem as it arrived, verbatim — this matters, because the gap between the two framings is often the finding]

**Actually:** [mechanism-free, measurable, owner-facing]

- Unit of value: [one satisfied unit of demand]
- Unit of cost: [what one unit costs today]
- Success threshold: [the number that counts as solved]
- Observably different if solved: [what changes in the world]

---

## 2. Why it is called impossible

**Class: [A / B / C / D / E / F]** — [or the mixture, which is common and is itself a finding]

[If Class A or B: name the theorem or law, state exactly what it forbids, and state which premise does or does not hold. Write the sentence:]

> [Theorem] forbids [W] under premises [P]. We do not need [W] — we need [V]. Premise [Pₖ] does not hold here because [reason].

[If no premise attack exists, say so plainly and go to §6 — the objective must be relocated.]

[If the cited limit is quantitative, compute it now and state how far the current operating point sits from it. A limit two orders of magnitude away is not what is stopping you.]

---

## 3. Constraint ledger

| # | Constraint (with quantities) | Asserted by | Class | Evidence | False if… | Cost to remove |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |

**Walls (Law / Math):** [rows that are genuinely immovable — these shape the design]

**Fences read:** [for each constraint proposed for removal: its original reason, and whether the condition that produced it still holds]

**Unexplained constraints:** [rows where no origin was found — these are research tasks, not permission to remove]

---

## 4. The floor

**Metric:** [units]

| Component | Irreducible requirement | Basis | Cost/value |
|---|---|---|---|
| | | | |
| | | **Floor** | |

**Current:** [value] **(measured / cited)**
**Floor:** [value] **(derivation)**
**Gap ratio:** [N]×

**Reading:** [< 2× → near the wall, change the objective · 2–10× → engineering slack, DFX passes · > 10× → the architecture is the problem · > 100× → recheck the floor for an omitted cost]

**What the floor omits:** [state it — the honest omission is what makes the ratio believable]

---

## 5. Candidate paths

[At least three that share no major assumption with the incumbent. If two would fail for the same reason, they are one path.]

### Path A — [name]

- **What it is:** [two sentences]
- **Traces to:** ledger rows [#] — [why removing them makes this possible]
- **Closes:** [how much of the gap, and how you know]
- **New constraints it introduces:** [every architecture pays somewhere — where does this one pay?]

### Path B — [name]
### Path C — [name]

[Consider including the "50% of the target at 5% of the complexity" candidate. It is frequently the right answer and is almost never generated unless asked for.]

---

## 6. DFX passes

[One table per surviving path. A path that came through with no changes has not been examined.]

| Pass | Finding | Change to the candidate | Residual risk |
|---|---|---|---|
| DFC — Cost | | | |
| DFM — Manufacturing / Execution | | | |
| DFS — Simplicity | | | |
| DFPR — Production rate | | | |
| DFV — Verification | | | |
| DFR — Reversibility | | | |

---

## 7. Red team

### Efficient-market check

**Why has nobody done this?**

- [ ] (a) Newly possible — [what changed, and roughly when]
- [ ] (b) Requires a capability, asset, or dataset few have — [name it]
- [ ] (c) The field is systematically wrong for a structural reason — [incentives / measurement / regulation / training]
- [ ] (d) No answer

[**If (d), say the path is probably wrong.** Smart people have been near this problem. "Everyone missed the obvious" is the least likely explanation available.]

### Kill experiment

| | |
|---|---|
| **What is observed** | |
| **Result that kills the path** | |
| **Cost** | |
| **Duration** | |

[If no experiment could disconfirm the path, mark it as rhetoric rather than a proposal.]

### What would have to be true

Sorted by uncertainty × impact. The top item is what to test first.

1. [assumption] — [uncertainty: high/med/low] · [impact if false]
2.
3.

---

## 8. What was not resolved

[Named gaps, not silent ones. For each: the quantity needed, its plausible range, and where it could be obtained. A fabricated number here would poison everything above it.]

| Unknown | Plausible range | How to obtain it | Blocks |
|---|---|---|---|
| | | | |

---

## 9. If the answer is no

[Use this section only when it applies — and when it applies, use it rather than burying the conclusion.]

**Impossible as posed because:** [the Class-A wall, with no available premise attack]

**The nearby objective that is not blocked:** [the relocation]

**What is traded away by relocating:** [state it explicitly — the relocation is a real concession and should not be presented as a free win]

**Gap ratio on the relocated objective:** [N]× — [which is usually where the actual opportunity was all along]
