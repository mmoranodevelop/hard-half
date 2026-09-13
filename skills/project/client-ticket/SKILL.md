---
name: client-ticket
description: >-
  Turn a raw client request — email, chat, call notes, or a pasted spec — into
  a structured tracker ticket (ClickUp first; same contract on Jira, Asana,
  Linear) by discovering the destination list's live schema — statuses, custom
  fields, option IDs, templates — and binding every slot to a real field
  instead of guessing names. Use when the user pastes a client ask and wants a
  ticket, says create the ClickUp / Jira / Asana task, open a card for this
  request, or drop this into the client's list. NOT for writing a PRD
  (prd-spec). NOT a change request against a signed baseline (change-control).
  NOT escalating a live issue (issue-escalate). NOT quality-dod, e2e tests, or
  weekly status. Do not invent field IDs or client lists: discover or ask.
license: MIT
---

# Client Ticket

## Fill the live schema

The default agent writes a markdown task and invents field names. On a real workspace that is how you get tickets with empty custom fields, the wrong list, and a status that does not exist. The leading word is **schema**. Nothing is created until the destination's live schema is read and every slot is bound to a real field or marked a hole.

The **ticket contract** is tracker-agnostic (client, type, size, surfaces, intent, dates, checklists). ClickUp, Jira, Asana, and Linear are adapters that *bind* that contract onto whatever the workspace actually has. A dropdown value is the option's id, not the label you wish existed.

Client names, list maps, and field labels belong in the workspace (and optionally in a local overlay). They do not belong in this skill. Discover them.

Write-side effects: the first action is discovery and a preview, not a create. Create when the bind is clean *and* the user asked to file it, or when they pasted a complete spec and nothing load-bearing is still a hole. Spurious activation must produce questions, not tickets.

## When to stop

- Builders need MUST/SHOULD, tests, non-goals → `prd-spec`
- One delta against a signed baseline → `change-control`
- One live issue that needs a ladder → `issue-escalate` (or `client-escalation` if the audience is the account)
- Quality gate before acceptance → `quality-dod`
- Manual E2E inventory → `e2e-manual-test-list`
- Internal weekly narrative → `weekly-status`
- No tracker connected and no destination named after one ask → issues list, stop
- Client or type still ambiguous after one ask → ask; do not guess destructively

## Mode

| Mode | When | Output |
|---|---|---|
| **File** | Default. A request, a destination (or a discoverable one), bind clean | Preview then created ticket + url |
| **Preview** | Bind has holes, or they did not say to create | Filled contract + bind table; no write |
| **Split** | One message holds several requests | One contract per request; file or preview each |
| **Refuse** | No client, no type, no destination after one ask | Issues list |

Infer. Ask only when File and Preview are equally live.

## Protocol

### 0. Destination and schema

Name the tracker (ClickUp / Jira / Asana / Linear / other). If unsaid, infer from connected MCP tools; if several, ask once.

Discover, in order:

1. **Where** — the list / project / board for this client. Match the client name to folder and list names in the workspace. Prefer a clients folder if one exists. Do not use a remembered map from a previous chat.
2. **Statuses** — pick the open status that matches backlog / to do / da fare. If none match, use the list's first open status and say so.
3. **Custom fields** — id, type, options (id + label). This is the schema.
4. **Language** — sample a few recent tasks on that list; match it. Empty list → match the request.
5. **Overlay** — if the current repo has `.hard-half/client-ticket.md`, or the list/project description holds a conventions block, it wins over the fallback pack.

Read `references/discover-schema.md` **now**. It holds how to walk ClickUp folders, Jira createmeta, Asana project field settings, and the overlay format.

Inspect the MCP tools actually available in this session and use those. Do not invent tool names. REST is the fallback when MCP is absent.

> **Done when:** tracker, destination id, status list, and field list exist — or you have asked once and stopped.

### 1. Parse into a contract

Split the input if it contains more than one request. Each request gets its own contract.

Extract (holes allowed, two load-bearing blanks after one ask → refuse):

1. **Client** — name as given; code is whatever the Client field or list name uses
2. **Ask** — outcome, mechanism-free
3. **Type** — bind later to the type field's *actual* options. Fallback pack (only if those options exist on the schema): Feature / Refactoring / Data Entry / Config / Bug
4. **Size** — S / M / L / XL against the complexity field's options, same rule
5. **Surfaces** — environments / components mentioned; bind to a labels or dropdown field
6. **Urgency** — blocking / deadline / incident signals
7. **Dates** — go-live, start, analysis deadline, development deadline if said

Do not invent a type that is not an option on the schema. If the field is called something else (Type, Issue Type, Categoria), bind by alias — `references/bind-fields.md`.

> **Done when:** each request is a contract with client + ask, or you have refused.

### 2. Bind

For every contract slot, find a field:

| Priority | Match |
|---|---|
| 1 | Exact name, case-insensitive |
| 2 | Alias table (Tipologia ↔ Type; Complessità ↔ Size; Ambiente ↔ Components) |
| 3 | Option overlap: most of the values you need exist as options |
| 4 | Hole — show it on the preview; do not invent an option |

Dropdown / labels / select: store the **option id** (ClickUp UUID, Jira option id, Asana enum gid). The label is only for the preview.

Required fields on the create screen that you cannot fill → Preview, not File.

Read `references/bind-fields.md` **now** if any field is drop_down, labels, or Jira select, or if names do not match the fallback pack.

> **Done when:** every slot is bound or holed, and no unbound required field is about to be posted.

### 3. Title, description, checklists

**Title:** `[CLIENT_CODE]: outcome`. The outcome, not the work. Include a date when the ask is a launch or campaign and the date is known. Client code = bound Client option or the destination list's own name.

**Description:** pick the template that matches the bound type and size. Write in the list's language.

Read `references/description-templates.md` **now** — Feature/Refactor (M+ vs S), Data Entry, Config, Bug.

**Checklists:** if the destination has a task template or checklist template for this type, use it. Otherwise take the matching pack from `references/checklist-packs.md` and **drop items that clearly do not apply**. Do not paste the whole M+ set onto an S data-entry.

**Priority:** Urgent = production broken or explicitly blocking; High = deadline inside the current cycle; Normal = default; Low = no date pressure. Map onto the tracker's priority enum (ClickUp 1–4, Jira priority name, Asana none unless a field exists).

**Assignee:** empty unless the user named someone who exists in the workspace.

**Dates:** due = go-live if given; start only if given; analysis/dev deadline fields only if those fields bound.

> **Done when:** title, description, checklists, priority, and dates are filled against the bind, not against a fantasy schema.

### 4. Gate, then create

Show the preview (`assets/ticket-preview.md`): destination, title, bound fields (label → id), holes, checklists.

Create only if:

- the user asked to file it, **or** the spec was complete and every load-bearing slot bound, **and**
- no required schema field is a hole

Adapter: `references/tracker-adapters.md` — ClickUp `POST /list/{id}/task` with `custom_fields: [{id, value}]`, then checklists; Jira `POST /rest/api/3/issue` after createmeta; Asana task + `custom_fields` map; Linear issue + labels.

After create: one-line summary, url, holes that remain.

If several contracts, create several tickets. Do not bundle unrelated asks.

> **Done when:** each request is a url or a preview that was explicitly not filed, and no custom field was created in the workspace unless the user asked.

## Anti-patterns

- **Remembered map.** Client → list from a previous chat, not from this workspace.
- **Label-as-value.** Posting "Feature" into a dropdown that wants an option UUID.
- **Invented option.** Adding a type the field does not have.
- **Schema-blind markdown.** A beautiful description, empty custom fields.
- **Checklist dump.** Every M+ item on a 20-minute config change.
- **Create-on-guess.** Client or type still a hole.
- **Published clients.** Hardcoding account names into anything that ships.

## Bundled references

| File | Read it when |
|---|---|
| `references/discover-schema.md` | Step 0 — walking the workspace, overlays, language sample |
| `references/bind-fields.md` | Dropdowns, aliases, option ids, required holes |
| `references/description-templates.md` | Writing the description for the bound type |
| `references/checklist-packs.md` | S data-entry vs M+ analysis/dev/test/release packs |
| `references/tracker-adapters.md` | Creating on ClickUp, Jira, Asana, Linear |
| `references/worked-examples.md` | Ambiguous client, split asks, or a schema that does not match the fallback pack |
| `assets/ticket-preview.md` | The preview before create |
| `assets/overlay-template.md` | When they need a local `.hard-half/client-ticket.md` — copy, do not invent clients in this catalog |
