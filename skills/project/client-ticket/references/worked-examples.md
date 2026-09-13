# Worked examples

Illustrative. No real account names. Unknowns stay holes.

## 1. File — schema matches the fallback pack

**Incoming:** a chat paste asking to set up a dated campaign on two named surfaces, launch Friday, client identifiable from the thread.

**Discover:** list name equals the client code; fields Type, Size, Surfaces, Client exist; options include Data Entry, S, and the two surfaces.

**Bind:** Type=Data Entry (option uuid), Size=S, Surfaces=those two label uuids, Client=list's code, due=Friday.

**Title:** `[CODE]: Campaign … Friday`

**Checklists:** operating pack; asset items dropped (not in the ask).

**Gate:** spec complete, bind clean → create. Summary + url.

## 2. Preview — Jira has Story/Bug only

**Incoming:** "config change: disable the named feature flag on staging."

**Discover:** Jira project, issue types Story and Bug, no Data Entry.

**Bind:** type hole on the fallback pack; map Config → Story; say so. Size field absent → hole.

**Gate:** Preview. Ask whether to file as Story. Do not invent an issue type.

## 3. Split

**Incoming:** two asks in one mail (a campaign and a production login bug).

**Split:** two contracts. Campaign → Data Entry S on the client list. Bug → Bug, Urgent, same list, reproduce-steps hole.

**Gate:** file the campaign if bind clean; Preview the bug until steps exist *unless* they said to file both now — then file the bug with `Steps: hole`.

## 4. Refuse

**Incoming:** "open a ticket for that thing we talked about."

**Discover:** destination unnamed; client unnamed.

**Gate:** Refuse. Issues list. Do not create.
