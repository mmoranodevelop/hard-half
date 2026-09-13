---
name: finance-workbook
description: >-
  Use when making a real .xlsx: IB three-statement MODEL or ISA/PCAOB WORKING-
  PAPER / flux — never mixed. NOT for business-case, cash-runway, budget-
  variance, working-capital, or other finance one-pagers.
license: MIT
---

# Finance Workbook

**Real `.xlsx`.** Two modes, never mixed: **(A) MODEL** — IB three-statement (IS / BS / CFS + schedules + Checks). **(B) WORKING-PAPER** — ISA/PCAOB schedule / flux. Color is a control system. A number that cannot be traced to an input or a source is a fail.

Method origin: ICAEW Financial Modelling Code 2024 + Twenty Principles; FAST 02c July 2019 (CC BY 4.0) **indexed only** (PDF captcha-walled — do not invent further FAST rules); PCAOB AS 1215 / AS 2305; ISA 230 / ISA 520; ACCA headers; JOA AU-C 230. Training labelled: WSP / CFI / TTS / BIWS. Macabacus = vendor palette, not IB font law. PwC Global Financial Modelling Guidelines PDF was **not retrieved** — do not reconstruct.

If they want a DCF lecture: one paragraph then produce the file or stop.

## When to use

- Integrated three-statement forecast the next analyst can type into
- Audit-grade flux / lead schedule a stranger can reperform
- Cover + key + Checks the MD can print

## When not to use

- Fund/kill NPV page — [Business Case](../../strategy/business-case/SKILL.md)
- Named-unit contribution — [Unit Economics](../../strategy/unit-economics/SKILL.md)
- 13-week bank strip — [Cash Runway](../../management/cash-runway/SKILL.md)
- This vs last vs plan P&L — [Budget Variance](../../management/budget-variance/SKILL.md)
- Gross/CM drivers — [Margin Bridge](../../strategy/margin-bridge/SKILL.md)
- CCC this month — [Working Capital](../../finance/working-capital/SKILL.md)
- Remaining FY vs original plan — [Reforecast](../../finance/reforecast/SKILL.md)
- Fully diluted ownership — [Cap Table](../../finance/cap-table/SKILL.md)
- “IB model + audit file in one blob” — split or refuse

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Mode A or B chosen | `.xlsx` on the sheet map |
| **redline** | Pasted book / yellow-everywhere / no Checks | Force key, unmerge calc grid, add Checks |
| **refuse** | Mixed A+B; invented actuals; hardcoded plug | Issues list. Stop |

Pick **A or B** before a single formula. Do not mix.

## Hard rules

1. **Color is a control system**, not decoration. ICAEW: when format carries meaning, **key it** on Cover; distinguish inputs by **fill and/or border, not font colour alone**.
2. **MODEL colour (training cluster, not bank policy):** blue font + light yellow fill = typed input; black = formula; **green** = cross-sheet (WSP/CFI/TTS); **red** = external workbook (purple is a house variant — document on Cover if used). Yellow fill is **training-common, not ICAEW-mandated**; it satisfies the fill/border rule. Do not invent Goldman RGB. **Macabacus** (blue inputs, purple/orange calcs, yellow = caution) is **not** the IB font convention — do not mix.
3. **FAST is a different language.** Indexed 02c only: four classes Foundation / Workings / Presentation / Control; comments **column** on inputs; **never purposeful circularity**; **do not merge cells** (Center Across Selection); keys for colour / abbreviations / names / functions. Openbox (vendor): FAST export **red**, import **blue** — opposite of IB green-for-cross-sheet. If they ask FAST, switch palettes and say so on Cover. Do not paint FAST colours onto an IB book and call it FAST.
4. **No hardcoded constants inside formulas** (ICAEW P14 / WSP). Unique location per input. Call up, then calculate — no daisy-chained cross-sheet inside a calc.
5. **Circularity (MODEL):** Cover says **OFF**. Named `circ_switch` 0/1 on Inputs. Interest = beginning balances when 0. Iteration is not the shipped default. Switch = 1 only with a visible circuit breaker **and** a check for #REF!/#DIV/0!. FAST indexed: never release with purposeful circ. **WORKING-PAPER: no circularity at all.**
6. **No merged cells in the calc grid.** No hidden sheets / white font. Group, don’t hide. External links registered on Audit and coloured red.
7. **No hardcoded plug** that forces Assets = L+E or sources = uses. Cash/revolver as a *calculated* 3-statement closer is allowed in MODEL only if CFS still proves cash and Checks stay red until it ties.
8. **Checks sheet is mandatory.** Master check in the freeze pane of every sheet (ICAEW). One screen.
9. **Units** on Cover (“unless labelled, figures are $000 / $m / actuals”) and a Units column. Round in presentation, never Precision-as-displayed.
10. **WORKING-PAPER:** every tested amount has source + procedure + conclusion. Tick marks **without a legend fail**. Do not invent a PwC tick alphabet. Flux = analytical procedures (ISA 520 / AS 2305): **expectation + threshold**; management inquiry **plus corroboration**; residual after corroboration. “Per discussion with CFO” with no evidence = fail. Invented actuals = fail. This skill does **not** certify an audit / PCAOB opinion.
11. **Do not reconstruct PwC GFMG** or Goldman/McKinsey internals.

## Intake

If **mode (A/B)** and **entity + as-of** are both missing after one round: issues list.

1. Mode A MODEL or B WORKING-PAPER (load-bearing)
2. Entity; currency; scale; as-of / horizon (load-bearing)
3. MODEL: historicals with **source**; cases. WP: TB/GL/PBC identified; assertion
4. Circularity policy (MODEL) — default OFF
5. Owner / preparer; reviewer if WP; date
6. What decision the file feeds (NPV page stays [Business Case](../../strategy/business-case/SKILL.md))
7. FAST palette requested Y/N (default = IB training key)

## Output shape

Copy `assets/sheet-map.md`. Build Inputs first, dashboard last. Freeze panes **and** Print Titles (they do not sync).

```
FINANCE WORKBOOK  |  mode: [MODEL | WORKING-PAPER]  |  [entity]  |  as-of: [date]
Scale: [$000 / $m / actuals]   circ_switch: [0 / 1]   palette: [IB training | FAST]
Author: [ ]  Version: [ ]  Color key: ON COVER

Cover → Index → Inputs/Source → Model/Workings → Checks → Outputs → Audit

MODEL Checks (one screen): (1) A−L−E=0  (2) cash rec  (3) RE bridge
  (4) roll-forward ties  (5) sources=uses no plug  (6) master OR  (7) circ state
WP: header client/period/subject/file-ref/preparer+date/reviewer+date
  tick legend; expectation; residual after corroboration; conclusion

ASK: [what the reviewer/MD must do with this file]
Owner: [ ]  Date: [ ]
Holes: [ ]
```

## QA (must pass) — one-screen fail list

1. One mode. Not mixed. Not a one-pager in costume.
2. Cover has key, units, circ policy, owner, date.
3. Inputs (or sources) only once; no stealth constants; no invented actuals.
4. No merged calc-grid cells. No hidden sheets. No hardcoded plug.
5. Checks sheet + master check visible. Circularity has a switch or is absent.
6. WP: legend, source, procedure, who/when, conclusion. Flux has expectation + corroboration.
7. Palette is IB **or** FAST, keyed, not both. Not Macabacus mixed in. Not reconstructed PwC/Goldman.

If 1, 3, 4, 5, or 6 fail: do not ship.

## Escalate / stop

- Merged calc grid / plug / circ with no switch / no Checks → refuse.
- Mixing MODEL + WP → split or refuse.
- One-pager request → route (table above).
- “Make it PCAOB-compliant” as a certification → refuse; produce a reviewable file only.

## Related

- [Close Calendar](../../finance/close-calendar/SKILL.md) — lock before actuals are controller-grade
- [Business Case](../../strategy/business-case/SKILL.md) / [Cash Runway](../../management/cash-runway/SKILL.md) / [Working Capital](../../finance/working-capital/SKILL.md) — pages that **consume** extracts
- [Document Kit](../../documents/document-kit/SKILL.md) — print chrome only; color-as-control stays this skill
