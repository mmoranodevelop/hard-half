# [The decision, stated as a sentence]

<!--
  File as .agents/adr/NNNN-short-slug.md, numbered in order.

  Write one when a decision is EXPENSIVE TO REVERSE and its reasoning is NOT
  OBVIOUS FROM THE CODE. Both conditions: a reversible decision needs no
  record, an obvious one documents itself.

  The title is the decision, not the topic. "Use Postgres rather than
  SQLite for local development", not "Database choice" — a reader scanning
  filenames should get the answer without opening anything.
-->

## Context

[What was true when this was decided. The constraint, the problem, the forces
in tension. Write it so it still makes sense to someone who arrives two years
later and knows none of the surrounding situation.]

## Decision

[What was decided, in plain terms. Present tense: "We store X as Y."]

## Alternatives rejected

<!-- The most valuable section. Rejected options come back — someone proposes
     them again, or an agent notices the obvious gap and helpfully implements
     one. Without the reasons, the same argument runs every six months. -->

**[Alternative]** — [why not. Be specific: "slower" is not a reason,
"adds a network hop on the read path, which is the 100ms budget" is.]

**[Alternative]** — [...]

## Consequences

[What this costs, what it makes harder, what now has to be true. An ADR
listing only benefits is a sales pitch, and a reader who spots that discounts
the whole file.]

## Revisit if

[The condition that would make this decision worth reopening — a scale
threshold, a dependency maturing, a constraint expiring. Constraints have
expiry dates, and naming this one prevents both blind adherence and pointless
re-litigation.]
