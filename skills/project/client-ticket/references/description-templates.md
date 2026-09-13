# Description templates

Write in the list's language (see discover-schema). The headings below are English; translate them if the list is not (Obiettivo / Contesto / …).

Pick by **bound type** and **size**. If type is a hole, use the S Feature/Config skeleton and mark the hole on the preview.

## Feature or Refactoring — size M, L, XL

```
**Objective:**
[One sentence: what we want to be true, for whom]

**Context:**
[Current state and why this is asked now]

**In scope:**
- [Each deliverable]

**Out of scope:**
- [What is not included]

**Prerequisites:**
- [What must exist before work starts]

**Acceptance:**
- [How we would know it is done — testable]

**Next steps:**
- [Immediate next actions]
```

If size is L or XL and no PRD exists, add one line: PRD still needed (`prd-spec`) — do not expand this ticket into a spec.

## Feature, Refactoring, or Config — size S

```
**Description:**
[What was asked, who, in what channel]

**Objective:**
[What needs to be true]

**Notes:**
[References, constraints, environment]
```

## Data Entry / campaign / launch / price

```
## General
- **Client:** [name / code as on the field]
- **Activity:** [New campaign / Product launch / Price change / …]
- **Go-live:** [date or hole]
- **Surfaces:** [only those mentioned or bound]
- **Scope:** [scope notes]

---

## Detail
- **Name:** [campaign or product]
- **Window:** [from / to]
- **Price:** [as given]
- **Entities / IDs:** [as given — never invent SKUs]
- **Stacking / conflicts:** [yes/no + detail, or hole]
- **Inclusions / exclusions:** [as given, or hole]
```

Drop a bullet that has no data rather than writing "TBD" everywhere. Holes belong in the preview bind table.

## Bug

```
**Description:**
[What happens, where, since when]

**Objective:**
[Expected behaviour]

**Steps to reproduce:**
1. [ ]
2. [ ]

**Notes:**
[Who reported, workaround, links]
```

If steps were not given, write `Steps: hole — ask reporter` rather than inventing a path.

## Title

`[CODE]: outcome`

- Outcome, not a verb of work (`Campaign X 25/07`, not `Implement campaign X`)
- CODE from the Client field option or the list name
- Date in the title when the ask is a dated launch or campaign and the date is known
