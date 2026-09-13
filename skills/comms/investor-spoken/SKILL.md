---
name: investor-spoken
description: >-
  Use for a spoken slot on ALREADY PUBLIC facts, then Q&A. Not the monthly
  letter, not a fundraising one-pager. Regulation FD: refuse private material
  guidance (higher / lower / the same).
license: MIT
---

# Investor Spoken

**INVESTOR SPOKEN — prepared remarks on already-public facts, then Q&A.** One page of spoken remarks, not the letter. Default: venture LP call on the same numbers as the letter. Reporting issuer: FD is a refuse, not a style choice.

Method origin: SEC Regulation FD, Release **33-7881** (intentional MNPI to market professionals or holders likely to trade → **simultaneous** public disclosure; non-intentional → **prompt** = later of **24 hours** or next NYSE session start). Private discussion that earnings will be higher, lower, or **the same** is “almost certainly” an FD violation. The letter is [Investor Update](../../writing/investor-update/SKILL.md). This slot is judgement and interrogation of *the same* numbers.

If they want an IR lecture: one paragraph then produce or stop.

## When to use

- A call / sitting is noticed and the letter or release already hit (or will hit first)
- Need short remarks + Q&A on the same metrics as last time
- Someone wants to “add colour” the market does not have
- The plan is to read the monthly letter aloud on a Zoom to a subset of holders

## When not to use

- Monthly (or quarterly) letter — [Investor Update](../../writing/investor-update/SKILL.md)
- Fundraising one-pager — [Fundraising One-Pager](../../strategy/fundraising-one-pager/SKILL.md)
- Board spoken 8 min — [Board Spoken](../../comms/board-spoken/SKILL.md)
- Sell-side / journalist / industry briefing — [Analyst Brief](../../comms/analyst-brief/SKILL.md)
- Term-sheet legal read — [Term Sheet Read](../../strategy/term-sheet-read/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Public facts exist; call dated | Spoken remarks + do-not-say + ASK of this call |
| **redline** | They pasted the letter as remarks, or a private-colour script | Same metrics; kill MNPI / implied guidance |
| **refuse** | Private earnings guidance; selective one-on-one colour; no public record | Issues list. Stop |

## Hard rules

1. **Writing first.** The letter / 8-K / press release ships. Spoken does **not** introduce a new material fact.
2. **Same metrics as last time.** Rotating vanity on a call creates a second book.
3. Short remarks, long Q&A. Miss first if there is one. One judgement line.
4. **FD refuse (reporting issuer):** no MNPI to enumerated persons without simultaneous public disclosure. Implied guidance (higher / lower / the same) is almost certainly a violation.
5. One-on-ones that “add colour” the market does not have → refuse.
6. Private-company LP updates are not FD — still **one set of facts**. Do not create two books.
7. If MNPI slips: stop the meeting; treat as non-intentional FD — public disclosure promptly (24h / next NYSE open). Do not “finish the thought” privately.
8. For a reporting issuer: call noticed (date, time, access). Website posting alone is not adequate notification (SEC discussion). Do not invent notice.
9. Do not invent numbers. Holes stay holes.

## Intake

If **already-public source (letter / release / 8-K)** and **call date** are both missing after one round: issues list, not fake remarks.

1. Issuer type: private / reporting (load-bearing)
2. Call date/time; who is on it; noticed Y/N
3. Public source already on the wire (title, date) — or “ships first” (load-bearing with 1)
4. Same metrics as last time; miss if any
5. Cash / burn / runway or public-company equivalent **already disclosed**
6. Ask of *this* call, if any — or “none, Q&A only”
7. Do-not-say list; IR/legal owner

## Output shape

```
INVESTOR SPOKEN  |  [entity]  |  call: [date time tz]  |  public source: [letter / 8-K / release, date]
Issuer: private / reporting     Notice: date/time/access posted [Y/N]     Access: [open / LP-only]
Same metrics as last time: [list]     Miss: [one line / none]

PREPARED REMARKS (short — then Q&A)
1. Period + miss first if any: [ ]
2. Same numbers (do not rotate): [ ]
3. Cash / burn / runway or disclosed equivalent: [ ]
4. One judgement line: [ ]
5. Ask of this call: [none / specific]

WILL NOT SAY
No new MNPI. No private guidance (higher / lower / the same, express or implied). No “just between us.”

IF MNPI SLIPS (reporting)
Stop. Prompt public disclosure: later of 24 hours or next NYSE open. Owner: [IR/legal].

ASK: [ship letter first / hold the call as noticed / take Q&A only]. Owner: [ ]. Date: [ ].
HOLES: [ ]
```

## QA (must pass)

1. Remarks rest on an already-public source (or labelled “ships first”).
2. Same metrics as last time. Miss first if there is one.
3. ASK + owner + call date.
4. Do-not-say includes no private guidance.
5. Not the monthly letter. Not a fundraising one-pager.
6. No invented numbers. Reporting issuer: no MNPI.

If 1, 3, 4, or 6 fail: do not ship.

## Escalate / stop

- Private earnings guidance (higher / lower / the same) → refuse.
- Selective colour to a subset of holders → refuse.
- MNPI slipped → stop the meeting; prompt public disclosure.

## Related

- [Investor Update](../../writing/investor-update/SKILL.md) — the letter is the record
- [Fundraising One-Pager](../../strategy/fundraising-one-pager/SKILL.md) / [Analyst Brief](../../comms/analyst-brief/SKILL.md)
- [Board Spoken](../../comms/board-spoken/SKILL.md) — fiduciaries, not holders
- [Pyramid Principle](../../writing/pyramid-principle/SKILL.md) — governing thought for the judgement line, not a second letter
