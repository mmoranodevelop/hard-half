---
name: verified-hard-problem
description: >-
  Attack one locked SUPER-COMPLEX claim that has stayed unsolved — millennial
  and prize-grade statements, systems-safety or legal-grade proofs, or anything
  the field calls unsolvable — with claim-lock, a lemma swarm, a dual
  deliverable (human-auditable writeup plus machine-checkable artifact), and an
  independent verification gate before any "solved" language. Use when the user
  wants to crack a problem nobody has solved, names a Clay / Millennium /
  P-vs-NP-class claim, says false certainty would be fatal, or asks for a proof
  that can be checked rather than a confident essay. NOT for first-principles
  floor-and-gap work on a stuck industry metric. NOT for whether a millennial
  market problem is worth solving (use value-problem-solver). NOT for
  issue-tree, experiment-brief, or kill-criteria. NOT a claim that this agent
  is a Millennium solver: a nearby variant is not the official claim, and prose
  that looks right is never verification.
license: MIT
---

# Verified Hard Problem

## The lock is the whole skill

The default agent, asked an unsolved problem, retrieves the consensus survey and sounds sure. On a millennial or "unsolvable" claim that survey *is* the wall: everyone already has it. The complementary failure is worse — a fluent essay that announces a solution. **Prose that looks right is not a proof.**

The leading word is **lock**. Nothing is attacked until the exact claim is locked. A nearby variant is not the official claim. A lemma swarm before the lock is theatre. "Solved" before an independent verification **gate** is forbidden.

What changes versus the default is not a personality ("be a superintelligence"). It is a research-program loop this model will not run unless forced:

1. lock the official statement
2. decompose into lemmas and attack them in parallel
3. share intermediates on a protocol
4. produce a **dual deliverable** — a writeup a human can audit *and* a machine-checkable artifact (or an explicit hole)
5. plan the gate before any solved language

This is how you prosecute a problem nobody has solved. It is also how you refuse to fake one. The skill does **not** claim this agent wins prize problems. It claims the agent will run the only method that has a chance, and will stop where the wall is real.

When a lemma cites a theorem or conservation law, invoke `first-principles` on that lemma (Class A: attack the premise, never the theorem; walls with no door stay walls). When they ask whether a millennial *market* pain is worth solving, that is `value-problem-solver`.

## When to stop

- Stuck industry metric, physics/cost floor, "impossible with current technology" without a locked official statement → `first-principles`
- "Does anyone actually want this / will they pay the switching cost?" → `value-problem-solver`
- Messy business "why is X down?" → `issue-tree`
- Cheap product falsification → `experiment-brief`
- Next-tranche kill tests → `kill-criteria`
- They want a lecture on Millennium problems or Lean → one paragraph, then produce or stop
- Two of the three load-bearing intake facts still blank after one ask → issues list, stop
- The official claim, even if proved, would not change the week they care about → `ghost-problem` first
- All published approaches sit on one line and they suspect a missing coordinate → `missing-axis`
- They want this agent to *be* the solver and to announce "solved" on prose or a nearby variant → refuse

## Mode

| Mode | When | Output |
|---|---|---|
| **Attack** | Default. A named hard claim, unsolved, false certainty fatal | Lock + lemma board + attack on open lemmas + dual-deliverable status + gate + one ASK |
| **Redline** | They pasted a "proof", a swarm log, or a "we solved it" deck | Force lock, fidelity, dual artifact, gate; kill invented greens |
| **Refuse** | No claim id after one ask, or "solved" without dual + gate | Issues list. Stop |

Infer. Ask only when Attack and Redline are equally live.

## Protocol

### 0. Intake — name the claim or stop

Load-bearing (two missing after one round → refuse):

1. Exact claim text + official statement id / acceptance criterion
2. Definition fidelity: **equals** the official claim, or a **nearby variant** (name the delta)
3. Why false certainty is fatal (prize, safety, legal, or "the field will treat a fake solved as real")

Also collect: current lemma board or "not decomposed"; share protocol or none; verifier name or hole; who would run the independent gate; the ASK this cycle.

> **Done when:** the three load-bearing facts exist or you have refused, and the mode is named.

### 1. Lock

Write the official statement so that a stranger could score yes/no against it. If the official source offers A/B/C/D (Clay-style), lock **exactly one**. "We made progress on a related PDE" is a nearby variant: record the delta and **forbid official-solved language** for the rest of the run.

Lock the terms. Open a definition CR for every word that still forks (forced vs unforced, worst-case vs average, …). An unlocked term is how a nearby variant sneaks in later and gets announced as the prize.

Read `references/claim-lock.md` **now** if the claim is prize-grade, has multiple official statements, or they already said "solved" on something that might be nearby.

> **Done when:** claim id, acceptance criterion, and equals-vs-nearby are on the page. Nearby ⇒ official-solved is off the table.

### 2. Classify the wall (do not skip)

Before swarming, name why it has stayed unsolved — the `first-principles` classes, in one line:

| If it is… | Then |
|---|---|
| **A — Proven** | Do not attack the theorem. Premise-attack or relocate. A violation of conservation / causality is never a path |
| **B — Complexity-bounded** | Attack instance structure, approximation, average case — not "we beat NP" |
| **C — Empirically unachieved** | The real target. Swarm at full strength |
| **F — Definitional** | Force an operational lock; the impossibility often dissolves or relocates |

If Class A and you cannot write the premise-attack sentence, **stop attacking**. Invoke `first-principles` or reshape the objective. Continuing is crackpottery with better stationery.

> **Done when:** the class is named, and a Class-A wall without a premise attack has stopped the run.

### 3. Lemma swarm — only after lock

Decompose the locked claim into lemmas / branches. Each lemma is a smaller claim with its own yes/no. Do not swarm the slogan.

For every open lemma, **attack** it (this is the work, not the board):

- restate it mechanism-free
- derive or cite; label **verified / assumed / unknown**
- status: `open / won / killed / hole`
- what intermediate, if won, **propagates** to other branches
- blocker

Retrieval of the survey is not an attack. If the lemma is the place the field is stuck, derive; if it cites a theorem, run the Class-A move.

Read `references/lemma-swarm.md` **now** if there are more than three branches, if intermediates must move between agents, or if you are about to mark a lemma "won" on prose.

Share protocol (required once there is more than one branch): who consolidates, cadence, what propagates, what stays local. Swarm without a consolidator is a pile of essays.

> **Done when:** every branch of the locked claim is a lemma with a status, no swarm started before lock, and the share protocol is written or holed.

### 4. Dual deliverable

Any use of "solved", even softly, requires both:

- **(a) Analytical writeup** a human expert can audit (definitions = locked claim, every lemma cited or derived)
- **(b) Machine-checkable artifact** — Lean (or another named kernel/verifier) whose *encoded* claim equals the lock — **or an explicit HOLE** that the verifier is unavailable

Kernel pass is necessary and **not sufficient**. The kernel checks the encoded logic. Experts still check that the encoded definitions are the official claim. A Lean green on a nearby variant is a nearby variant.

If (b) is a hole, you may continue attacking. You may **not** say solved.

Read `references/dual-deliverable.md` **now** if they want "solved", if a verifier is named, or if only prose exists.

> **Done when:** (a) and (b) each have a path, a pass, or a hole — and "solved" is absent unless both exist and the gate in step 5 is planned.

### 5. Independent verification gate

Before any announcement language: **who** checks **which artifact** by **when**. Timebox it. Prize / official acceptance is an external process — never invent Clay, court, or regulator outcomes.

ASK, exactly one, from this set: continue swarm / freeze claim / escalate named expert / kill branch / open definition CR. Owner, date.

Use `assets/one-pager.md` for the page. Use `assets/lemma-board.md` as annex only — it does not replace page 1.

Read `references/worked-examples.md` if the honest output wants to be "we solved it", or if they asked you to become the Millennium solver. One example is a refusal.

> **Done when:** the page has lock, fidelity, class, lemma statuses, dual-deliverable holes, a gate plan (or an explicit forbid on solved), one ASK, and no invented theorem names, kernel greens, or prize claims.

## Anti-patterns

- **Unlocked swarm.** Agents (or paragraphs) attacking "Navier–Stokes" / "alignment" / "P vs NP" without a statement id.
- **Nearby as official.** A variant proved; the prize claim announced.
- **Prose-as-proof.** The writeup is eloquent; no kernel; labelled verified.
- **Kernel-as-fidelity.** Green Lean, wrong definition.
- **Survey-as-attack.** Ten pages of what the field already knows, zero lemmas won.
- **Solved-before-gate.** Press language before an independent checker is even named.
- **Oracular upgrade.** "I am now a superintelligence" — a no-op. The lock is the upgrade.
- **Invented greens.** Theorem names, Lean status, Clay acceptance, agent-count heroics. Holes stay holes: `[not verified — gate by DATE]`.

## Bundled references

| File | Read it when |
|---|---|
| `references/claim-lock.md` | Prize-grade or multi-statement claims, or they already said "solved" |
| `references/lemma-swarm.md` | More than three branches, share across agents, or a lemma about to be marked won on prose |
| `references/dual-deliverable.md` | They want "solved", a verifier is named, or only prose exists |
| `references/worked-examples.md` | The run wants to announce a solution, or they asked you to be the prize solver |
| `assets/one-pager.md` | You are writing the deliverable |
| `assets/lemma-board.md` | Annex after lock — never instead of page 1 |
