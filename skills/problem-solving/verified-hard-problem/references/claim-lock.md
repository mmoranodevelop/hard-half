# Claim lock

A hard problem stays unsolved for a long time in part because people attack *different* statements and then argue. The lock makes the yes/no scorable.

## What to write down

1. **Official source** — Clay statement, RFC, statute, safety spec, theorem number, or the user's own acceptance criterion if no official source exists.
2. **Exact text** of the claim, quoted or tightly paraphrased with a cite.
3. **Acceptance criterion** — the sentence a stranger uses to mark solved. "Progress" is not a criterion.
4. **Equals vs nearby** — if the attack target is not the official text, name the delta in one line. Nearby work can be real and still **must not** be labelled official-solved.
5. **Open definition CRs** — every term that still forks.

## Multi-statement official problems

Some official write-ups offer a menu (prove *exactly one* of A/B/C/D). Lock one letter. "We have results that touch A and C" is not a lock.

If the user cannot choose, the ASK is `freeze claim` or `open definition CR` — not a swarm.

## Nearby variants (typical deltas)

| Official-shaped claim | Nearby variant that is not it |
|---|---|
| Unforced / physical formulation | Forced, periodic, or smoothed stand-in |
| Worst-case / general instance | Average-case, restricted graph family, oracle |
| Full system safety property | A lemma about a subsystem |
| Statutory test as written | A similar test from another jurisdiction |
| Exact complexity class collapse | A conditional or relativized result |

Write the delta. Then keep attacking the variant if that is the honest target — under its own id, never under the prize id.

## When there is no official source

The user may own the acceptance criterion (a safety property, a legal standard they must meet). Then *they* are the official source. Write their criterion so it is yes/no. If they give adjectives ("secure", "aligned", "correct"), force an operational lock or refuse: Class F work first.

## Forbidden language until lock

"Solved", "broken", "proved", "we have Navier–Stokes / P=NP / alignment", agent-count heroics. After lock, those words still wait on the dual deliverable and the gate.
