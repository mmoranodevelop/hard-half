# ARR/MRR bridge table (annex)

Companion to [NRR Bridge](sand-workflow:nrr-bridge).

```
BRIDGE ANNEX  |  grain: [ARR/MRR]  |  period: [start → end]  |  currency: [ ]

| Line | $ | Logos (opt) | Definition notes |
| Beginning |  |  | freeze rule: |
| + New |  |  | excluded from NRR |
| + Expansion |  |  | upsell/seat/price/cross/reactivation |
| − Contraction |  |  | downgrade/seat loss |
| − Churn |  |  | logo exit $ |
| Ending |  |  | tie-out: begin+new+exp−con−churn |

GRR % = [ ]    NRR % = [ ]
Tie-out check: PASS / GAP [ ]
Holes: [ ]
```
