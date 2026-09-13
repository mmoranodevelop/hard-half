# Client ticket — preview

```
CLIENT TICKET  |  [tracker]  |  as-of: [date]
Mode: File | Preview | Split | Refuse
ASK: [file / pick list / pick type / stop] by [date]  owner: [user unless named]

DESTINATION
Tracker: ClickUp | Jira | Asana | Linear | other
Space / project: [ ]    Folder: [ ]
List / board / section: [name]  [id]
Status on create: [exact string]    Language: [from sample / from request]
Overlay used: .hard-half/client-ticket.md | list description | none

CONTRACT (one per request)
Client: [name] → code [from field or list]
Ask (mechanism-free): [ ]
Type (heuristic → live option): [ ] → [ ]
Size: [S/M/L/XL or live label]
Surfaces: [ ]
Urgency → priority: [ ] → [native]
Dates: due [ ]  start [ ]  analysis [ ]  dev [ ]
Assignee: none unless named [ ]

BIND (label is preview; native value is what you post)
| Slot | Field name | Field id | Native value | Hole? |
| Client | [ ] | [ ] | [option id] | |
| Type | [ ] | [ ] | [ ] | |
| Size | [ ] | [ ] | [ ] | |
| Surfaces | [ ] | [ ] | [ ] | |
| … | | | | |

Required schema fields still empty: [none / names]  → cannot File

TITLE
[CODE]: [outcome]

CHECKLISTS (template on destination / fallback pack, pruned)
- [name]: [items kept]

CREATE
Done: [url]
Holes remaining: [ ]
Do not invent option ids. Do not create fields. Do not assign unless named.
```
