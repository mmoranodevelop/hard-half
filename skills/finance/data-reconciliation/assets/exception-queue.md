# Exception queue (annex)

Companion to [Data Reconciliation](sand-workflow:data-reconciliation). Use when Top N on the one-pager is not enough. Rank by $ / hours / risk. Never invent matches.

```
EXCEPTION QUEUE  |  recon: [purpose]  |  as-of: [date]  |  materiality: [$ / h]
Owner of queue: [ ]    SLA: P1 [ ]d / P2 [ ]d / P3 [ ]d

| Rank | Class | Source L ref | Source R ref | Key used | L value | R value | Δ $ or h | Conf | Age (d) | Disposition | Owner | Due | Status |
| 1 | Conflict/Partial/Unmatched L/Unmatched R |  |  | exact/composite/fuzzy |  |  |  |  |  | accept / investigate / correct source / write-off |  |  | open |
| 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |

DISPOSITION RULES (default)
- accept          — within tolerance or documented business OK; attest
- investigate     — need evidence; do not clear conf upward without evidence
- correct source  — fix left or right system / master data; re-run recon
- write-off       — residual below policy or approved loss; named approver

BANDS (if fuzzy)
auto ≥ [ ]    review [ ]–[ ]    refuse < [ ]

AGING
>30d open → escalate to [manager]. >90d → disposition mandatory (no silent park).

Holes / blocked on: [ ]
```
