# FINANCE WORKBOOK  |  mode: [MODEL | WORKING-PAPER]  |  [entity]  |  as-of: [date]
Scale: [unless labelled, $000 / $m / actuals]     Currency: [ ]     circ_switch: [0 OFF / 1 ON]
Palette: [IB training | FAST]     Author: [ ]     Version: [ ]     Date: [ ]

**One mode per file. Never mix.** FAST 02c PDF was captcha-walled — indexed rules only (four classes; comments column; no purposeful circ; no merge; keys). Do not invent further FAST rules. PwC GFMG PDF not retrieved — do not reconstruct.

## Color key (must live on Cover)

### IB training cluster (default MODEL) — not bank policy; labelled WSP/CFI/TTS/BIWS

| Cell | Font | Fill / border | Meaning |
|---|---|---|---|
| Typed input | Blue | Light yellow fill (training-common; satisfies ICAEW fill/border — **not ICAEW-mandated hue**) | You may type |
| Same-sheet formula | Black | None | Do not type |
| Cross-sheet link | Green | None | IB cluster; **not** FAST |
| External workbook | Red | None | Default (WSP/TTS/CFI). Purple = house variant — document here if used |
| Needs update | [optional red] | — | Sell Side variant; not universal |

Macabacus (blue inputs / purple-orange calcs / yellow = caution) is **vendor, not IB font law**. Do not mix.

### FAST (only if Cover says FAST)

Indexed + Openbox vendor: export formula **red**, import **blue**, intra-sheet counterflow gray. Opposite of IB green-for-cross-sheet. Comments **column** on inputs. Do not merge (Center Across Selection).

### WORKING-PAPER

ISA/PCAOB do not prescribe blue/yellow. Control system = **source + procedure + tick legend**. Tame IB-like input colour so typed vs formula is visible. **Legend on Cover**, repeated on lead schedules. Do not invent a PwC tick alphabet.

## Sheet map (left → right) — synthesis of ICAEW / FAST classes / WSP / TTS, not a bank SOP

| Tab | MODEL | WORKING-PAPER |
|---|---|---|
| **Cover** | Entity, purpose, author, version, date, **this key**, units/scale, sign convention, circ policy + `circ_switch` cell | Client, period-end, engagement, **file index**, **tick legend**, preparer/reviewer convention, retention note (PCAOB 7y / ISA ≥5y) |
| **Index** | Hyperlinked TOC, sheet purpose, tab-color key | Same + cross-ref to lead schedule / TB |
| **Inputs** or **Source** | All hardcodes **once**. Comments column. Scenario toggle. `circ_switch`. | TB / GL / client-prepared schedule, identified **PBC** if so. Do not type “actuals” without a source. |
| **Model** or **Workings** | IS, BS, CFS, BASE/corkscrew roll-forwards. One row, one formula. **No merged cells in the calc grid.** | Lead schedule → supporting. Flux: **expectation + threshold**. No forecast engine. |
| **Checks** | See list below. Master check. One screen. | Footing, cross-foot, TB tie, flux residual after corroboration. Master check still. |
| **Outputs** | Print-ready statements. **No new logic.** | Conclusion, issues, unadjusted differences. **No new logic.** |
| **Audit** | Change log, version, external-link register, limitations, who to call | Who prepared, who reviewed, dates; inconsistent-info note (ISA 230 / AS 1215.08); assembly clock |

FAST class map (indexed): Foundation ≈ Inputs; Workings ≈ Model; Presentation ≈ Outputs; Control ≈ Cover/Index/Checks/Audit.

## MODEL Checks (one screen; freeze header + master)

1. Assets − Liabilities − Equity = 0 every period (**flag, not a plug**)
2. Beginning cash + Δcash on CFS = ending BS cash
3. Opening RE + NI − dividends ± other equity = closing RE
4. Each major roll-forward ties (PP&E, debt, WC)
5. Sources = uses if a transaction schedule exists — direct calc + check, **not a plug**
6. Master check = OR of the above, in the **freeze pane of every sheet** (ICAEW)
7. `circ_switch` state displayed. Iteration is **not** the shipped default.

Cash/revolver as a *calculated* 3-statement closer is allowed only if CFS still proves cash and Checks stay red until it ties. Typed override of cash = refuse.

## WORKING-PAPER header (every schedule — ACCA)

Client: [ ]  Period: [ ]  Subject: [ ]  File ref: [ ]
Preparer + date: [ ]     Reviewer + date: [ ]
Objective / assertion: [ ]
Source: [TB / GL / invoice / contract / PBC]     PBC checked by: [ ]
Procedure: [ ]     Tick marks: [see Cover legend]
Expectation (ISA 520 / AS 2305): [ ]     Threshold: [ ]
Result: [ ]     Residual **after corroboration**: [ ]
Conclusion: [ ]
Inconsistent info retained: [Y/N + ref]

“Per discussion with CFO” with no corroborating evidence = fail.

## Print

Freeze panes **and** Print Titles (they do not sync). Repeat: entity / purpose / scenario / scale / currency. Footer: path + page + date. Checks print area = one landscape page. Cover = PDF page 1.

## ASK

[what the MD / reviewer must do with this file]
Owner: [ ]  Date: [ ]
Holes: [ ]
