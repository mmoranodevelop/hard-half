CUTOVER RUN  |  [what switches]  |  [client]
Window: [start–end] [timezone]     Freeze from: [time]     Point of no return: [time]
Cutover lead: [name]     D (rollback call): [name]     Comms: [name]
Go/no-go: [called Go date / draft for gate]

ASK: [D or cutover lead] to approve this runbook + freeze by [date], [n] hours before window.

FREEZE
From [time]: [what cannot change]. Test: [write fails / banner]. Told: [who, channel].

ROLLBACK
Trigger: [observable]. Call by: [name] within [n min]. Time to reverse: [ ]. After point of no return: fix-forward only.

SEQUENCE
| Time | Step | Owner | Validation | Rollback now? |
| [ ] | [ ] | [one name] | [observable] | Y/N |

IN-WINDOW GATES
| Time | Gate | D | If no |
| [ ] | go/no-go before point of no return | [ ] | rollback / abort |

COMMS
| Time | Message | From → to | Channel |
| [ ] | freeze start / live / rollback | [ ] | [ ]

NOT THIS PAGE
Go/no-go criteria → go-live-readiness    Day 1–100 → integration-100
Holes: [ ]
