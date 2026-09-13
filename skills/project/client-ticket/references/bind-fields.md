# Bind fields

A bind is a pair: **contract slot → (field id, native value)**. The native value for a select is the option id, never the display label.

## Fallback pack (used only as search keys)

These names are what many delivery teams put on ClickUp. They are **search keys**, not a schema. If the live field is named something else, aliases still bind. If the options differ, use the live options.

| Slot | Search names | Fallback options (if present) |
|---|---|---|
| Client | Client, Cliente, Account, Customer | whatever the field actually lists |
| Type | Tipologia, Type, Categoria, Issue Type, Kind | Feature, Refactoring, Data Entry, Config, Bug |
| Size | Complessità, Complexity, Size, T-shirt, Estimate | S, M, L, XL |
| Surfaces | Ambiente, Environment, Canali, Components, Platforms | (labels — match mentioned surfaces to options) |
| Analysis due | Deadline Analisi, Analysis due, Analysis deadline | date |
| Dev due | Deadline Sviluppo, Dev due, Development deadline | date |

Aliases are case-insensitive. Strip punctuation. `tipologia` = `Type`.

## Match order

1. **Exact name** of the field.
2. **Alias** from the table.
3. **Option overlap** — you need values A,B,C; the field offers a set that contains most of them. Bind. Values you need that are *not* options stay holes; do not create options.
4. **Type-shaped leftover** — one unbound dropdown whose options look like types, sizes, or clients. Propose it on the preview; do not silently write.

If two fields match the same slot, prefer the one on the destination list over a space-wide field, and the one with options that match the contract.

## Native values

| Tracker type | What you post |
|---|---|
| ClickUp `drop_down` | option UUID (`type_config.options[].id`). Some workspaces still want the option's `orderindex` — if create rejects the UUID, retry with the index **and record which the workspace accepted**. |
| ClickUp `labels` | array of option UUIDs |
| ClickUp `date` | Unix ms |
| ClickUp `short_text` / `text` | string |
| ClickUp `checkbox` | boolean |
| ClickUp `number` | number |
| Jira select / radio | `{ "id": "<option id>" }` or `{ "value": "<label>" }` only when createmeta shows no ids |
| Jira multiselect | array of those objects |
| Jira date | `YYYY-MM-DD` |
| Asana enum | `{ "gid": "<enum option gid>" }` in the `custom_fields` map keyed by field gid |
| Asana multi-enum | array of gids |
| Linear | label ids or state id — Linear has no arbitrary custom fields on all plans |

Never post a label into a ClickUp dropdown. That is the characteristic failure.

## Size heuristic (then bind to live options)

Use this only to pick among options that exist:

- **S** — single action, toggle, copy, campaign / data entry; typically one person, under a day
- **M** — multi-step, 1–2 areas, some coordination; days not sprints
- **L** — cross-system, several people, needs a spec; a sprint or two
- **XL** — multi-sprint initiative

If the field is Fibonacci or story points, map S→1–2, M→3–5, L→8, XL→13+ and pick the nearest existing option.

If the field has no S/M/L, pick the closest label (`Small`, `Quick`, …) and say the mapping on the preview.

## Type heuristic (then bind)

- **Bug** — it worked; now it doesn't
- **Data Entry** — admin / content / configuration that is not a code change (campaign, price, launch, copy)
- **Config** — flags, enable/disable, environment settings
- **Refactoring** — existing behaviour or assets, changed
- **Feature** — behaviour that does not exist yet

If the live options are Bug / Story / Task, map Feature+Refactoring+Config+Data Entry onto Story or Task as the project actually uses them, and say so. Do not invent "Data Entry" on a Jira project that does not have it — put the nuance in the description.

Ambiguous type → ask once.

## Required holes

If createmeta / ClickUp required flag / Asana is_required is true and the slot is a hole, **Preview**. Creating will 400 and leave a partial ticket.
