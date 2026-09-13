# Worked examples

Illustrative. Unknowns stay unknown.

## 1. Empty pair — consistency vs latency vs the same lock

**Incoming:** "Search is green on latency, catalog is green on strong consistency. Cutover is next month."

**Sets (shared world: one customer-facing read path):**
- L: P95 read < 200ms including catalog
- C: every read sees the latest committed write (no replica lag)

**Pair:** on the current architecture both greens were measured on *different* paths. On the shared path, C forbids the stale replica that L used. Empty pair {L, C}.

**Exit:** `relax C` on the search path (eventual, with a named staleness bound) **or** `relax L` (P95 bound that includes a consistent fetch) **or** `sequence` — consistent path for checkout, stale path for browse — and say browse never satisfies C.

**ASK:** `relax C` on browse, owner, date. Do not ship "both greens."

## 2. Three-way — capacity two, ambitions three

**Incoming:** every squad is green: realtime personalization, full audit trail, and on-device processing. Board wants all three.

**Shared resource:** the same user event cannot be (a) processed only on-device, (b) shipped to an auditable store, and (c) used for a server-side realtime ranker, without relaxing one set.

**Pairs** can be nonempty (on-device + audit with delayed upload; server ranker + audit; on-device + local ranker). **Triple** empty under the current definitions.

**Exit:** `drop` server-side realtime **or** `relax` audit to device-side logs with a different control owner **or** `sequence` phases that never overlap the triple.

**ASK:** `drop` one of the three. `keep fighting` only with the empty triple on the same line.

## 3. Prove-nonempty — exhibit a point

**Incoming:** "Legal says encryption-at-rest AND support must decrypt for this ticket type. Impossible?"

**Sets:** rest-encryption with key held by KMS; support decryption for ticket type T under break-glass G with named two-person rule.

**Point:** ciphertext at rest; G opens KMS for T for 30 minutes; two named roles; session logged. Ugly, nonempty.

**ASK:** none of the empty-tuple exits. The AND stands. If they wanted a floor on cost of G, that is `first-principles`, not this skill.

## 4. Refuse slogans

**Incoming:** "We want it fast AND cheap AND custom AND compliant."

No sets after one ask. **Refuse.** Issues list: four spaces and four cuts. Do not produce a both-and essay.
