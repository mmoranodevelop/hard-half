# Dual deliverable and the gate

"Solved" is a two-key lock. One key is a human-auditable argument. The other is a machine check of *the same claim*. Either key alone is how false certainty ships.

## (a) Analytical writeup

A stranger in the domain can follow it. It must:

- quote or cite the locked claim
- show equals-vs-nearby
- list lemmas and which are won
- derive or cite every won lemma
- label holes

Eloquence is not a criterion. Length is not a criterion.

## (b) Machine-checkable artifact

Name the kernel or verifier (Lean 4, another proof assistant, a model checker, a SAT/SMT run with a pinned solver, a mechanically checked type/proof object). The **encoded** statement must be the lock, not a cousin.

| Result | Means | Does not mean |
|---|---|---|
| Kernel pass | The encoded logic has no hole *as encoded* | Definitions match the official claim |
| Kernel fail | The encoding or the proof is wrong | The informal idea is dead |
| Verifier unavailable | HOLE — keep attacking | You may say solved |

If the environment cannot run a verifier, write the hole and the smallest artifact that *would* be checked. Do not simulate a green.

## Independent gate

**Who** (named expert, lab, or process — not "the community" and not this agent) checks **which artifact** by **when**.

The gate can fail the run after a kernel pass: that is the fidelity check. Plan it *before* announcement language. Prize committees, courts, and regulators are external; never invent their outcome.

## Language after a pass

Allowed: "the writeup argues X; the kernel accepts encoding Y; fidelity to the official claim is [yes / no / hole]; independent gate is [plan]."

Forbidden: "we solved [prize name]", "Clay will accept", "the theorem is proved" on a nearby encoding, invented greens.
