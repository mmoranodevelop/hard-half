# Information architecture

Step 4. Where each piece of a skill sits, and when one skill should become two.

---

## The two content types

A skill is built from **steps** and **reference**, mixed freely. A skill can be all steps, all reference, or both — and "all reference" is a legitimate shape, not a degenerate one.

**Steps** — ordered actions. What the agent does, in sequence.

**Reference** — definitions, rules, facts. Consulted on demand rather than executed in order. Often a genuinely flat peer-set: every rule of a review sitting on one rung. Flatness there is an arrangement, not a smell.

---

## The ladder

The **information hierarchy** ranks material by how immediately the agent needs it.

| Tier | What it is | Cost |
|---|---|---|
| **1. In-skill step** | An ordered action in `SKILL.md` | Loaded on every invocation |
| **2. In-skill reference** | A rule or definition in `SKILL.md`, consulted as needed | Loaded on every invocation |
| **3. External reference** | A sibling file reached by a **context pointer** | Loaded only when the pointer fires |

Tier 3 is where depth becomes cheap. A skill can carry a thousand lines of reference and cost almost nothing per invocation, provided the body only points at it.

**The tension is the whole decision.** Push too little down and the body bloats — every invocation pays for material most runs never touch. Push too much down and you hide material the agent actually needs, and it proceeds without it. No rule resolves this; judgement does.

---

## Branching decides disclosure

The cleanest test.

A **branch** is a distinct way the skill gets used — different runs taking different paths through it.

> **Inline what every branch needs. Push behind a pointer what only some branches reach.**

A debugging skill used on both database and network problems has two branches. The diagnostic loop is shared → inline. The Postgres lock-mode table is one branch only → disclose.

If a skill has exactly one branch and still feels too long, that is **sprawl**, and the cure is pruning rather than disclosure.

---

## Context pointers

A **context pointer** is the line that sends the agent to a disclosed file. **Its wording, not its target, decides whether the agent goes.**

| Pointer | Result |
|---|---|
| "See `references/x.md` for more details." | Often ignored — reads as optional colour |
| "More information is available in `references/x.md`." | Same problem: no trigger, no imperative |
| "**Read `references/x.md` now if the problem cites a theorem or a physical law** — it holds the premise-attack table." | Fires reliably |

Three ingredients in the good version: an **imperative** (read), a **trigger condition** (if the problem cites…), and a **payoff** (it holds…). The trigger is what turns a suggestion into routing.

A table of pointers at the end of a body works well — one row per file, with the *when* in its own column, so the condition is impossible to skim past.

---

## Completion criteria

Every step ends on a **completion criterion**: the condition that tells the agent the work is done.

Two properties:

- **Checkable** — can the agent tell done from not-done? "Analyse the schema" cannot be checked. "Every table with a foreign key accounted for" can.
- **Exhaustive, where it matters** — "every modified model accounted for" binds; "produce a change list" invites stopping at three.

A vague criterion invites **premature completion**: the agent's attention slips to *being done* rather than *doing*. A demanding criterion drives thorough **legwork** — the digging the agent does inside the work — and it binds flat reference just as well as sequences, because "every rule applied" is the same kind of gate as "every step done".

---

## Co-location

Where the ladder decides *how far down* a piece sits, **co-location** decides *what sits beside it* once it's there.

Keep a concept's definition, rules, and caveats under one heading rather than scattered across the file. Reading one part should bring its neighbours with it.

The failure this prevents is the agent applying a rule while its caveat sits four hundred lines away, unread.

---

## When to split a skill

**Granularity** is how finely you divide skills, and every cut spends one of the two loads. Split only when the cut earns it.

### Cut by invocation

Split off a **model-invoked** skill when there is a distinct leading word that should trigger it on its own, or when another skill must be able to reach it.

You pay **context load** for the new always-loaded description, permanently. That independent reach has to be worth a permanent tax.

### Cut by sequence

Split a run of steps when the steps still ahead tempt the agent to rush the one in front of it. Keeping the later steps out of view removes the pull toward being finished, and the agent does more legwork on the current task.

This cut is a **defence against premature completion, and it is the second line of defence.** Try sharpening the completion criterion first — that is cheap and local. Split only when the criterion is irreducibly fuzzy *and* you have actually observed the rush.

### When not to split

- Because the file "feels long" — measure the branches first; sprawl is cured by pruning.
- Because the pieces are conceptually distinct — conceptual tidiness is not worth a permanent context tax.
- Into a skill nothing will ever invoke independently — that is a disclosed reference file wearing a costume.

---

## Deciding, in practice

1. List every piece of material the skill needs.
2. Mark each with the branches that need it.
3. Everything marked *all branches* → inline.
4. Everything marked *some branches* → disclose, with a triggered pointer.
5. If the inlined set is still too long, prune it; do not disclose your way out of sprawl.
6. If two groups share nothing and one has its own leading word, consider the invocation cut.
