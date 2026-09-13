# Worked examples

Illustrative. Unknowns stay unknown.

## 1. Hunt — two stacks that are the same option

**Incoming:** "We're stuck choosing between the two architectures. They feel like the same argument we've had for three years."

**Current axes:** latency, unit cost, operational familiarity.

**Collinear:** stack A wins cost, loses latency; B the reverse; both assume a server-side write path.

**Candidate axis:** *who can complete the critical action while disconnected* (minutes of useful offline). Unit: minutes. Split: A and B both ≈ 0; a third design that looks worse on latency/cost would score hours.

**Mute-reason:** unmeasured — no dashboard cell; the field froze when clients were thin.

**Confirmation:** two customer weeks scored on "failed actions while radio-down," not on latency. If that rate is noise, kill the candidate.

**ASK:** `run confirmation`. Do not start another A-vs-B rebuild.

## 2. Confirm — both camps look right

**Incoming:** "Safety camp and speed camp both have theorems. We're looking in the wrong place."

Do not adjudicate the theorems (`first-principles` Class A on each, separately, if needed).

**Current axis:** the safety–speed line.

**Candidate:** *who sees the failure in time to reverse it* (reversibility window in hours). Both camps can be locally right and silent on whether a miss is reversible.

**Confirmation:** take one incident class; score time-to-irreversible vs the camp's preferred metric. If they move together, the candidate is a nickname for the current line — `kill candidate`.

**ASK:** `run confirmation`.

## 3. Manifold stands

**Incoming:** "Think outside the box. Give us a new dimension."

Options already differ on cost, latency, and a named consistency model; the user cannot say what "feels the same" means. After one ask, no collinearity. **Manifold stands.** Hand to `first-principles` if they still call it impossible. Do not invent an axis to look creative.

**ASK:** `manifold stands`.

## 4. Refuse slogans

**Incoming:** "The missing piece is culture."

No unit, no split. **Refuse** as an axis. Either they give a comparison (e.g. "time until a dissent is cheap") and you hunt, or issues list. "Culture" as output is the anti-pattern.
