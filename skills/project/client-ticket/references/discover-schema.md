# Discover the schema

The destination is a living object. Read it this run. A map from last week is how tickets land in the wrong list with the wrong option ids.

## Overlay (local, not in this skill)

If the current working copy has `.hard-half/client-ticket.md`, read it first. It may name:

- default tracker and workspace
- folder that holds client lists
- extra aliases (field names the team actually uses)
- language override

The list or project **description** on the tracker can hold the same block. Overlay wins over the fallback pack; live schema wins over overlay when they disagree (an overlay that names a field that does not exist is a hole, not a create).

Do not commit client names into this catalog. The overlay lives in the *client* repo or in ClickUp.

## ClickUp

Inspect MCP tools in this session (`list_spaces`, `list_folders`, `list_custom_fields`, `create_task`, …). Names vary by server — use what exists.

Walk:

1. Spaces → folders → lists. Match the client string to a list name or folder name (case-insensitive, ignore legal-suffix noise). If a folder looks like a clients bucket (Clienti, Clients, Accounts), search there first.
2. `GET /v2/list/{list_id}` (or MCP equivalent) for statuses.
3. `GET /v2/list/{list_id}/field` for custom fields. Keep `id`, `name`, `type`, and `type_config.options` (`id` + `name` or `label`).
4. Sample 3–5 tasks on the list (`GET /v2/list/{list_id}/task?page=0`) for language and for how titles are actually written.
5. If the list has templates, note checklist names.

Status pick: prefer a name matching `backlog`, `to do`, `todo`, `da fare`, `open`. Else the first status whose type is open.

REST fallback when MCP is missing: [ClickUp API](https://developer.clickup.com/reference/getaccessiblecustomfields) — `GET /v2/list/{list_id}/field`, `POST /v2/list/{list_id}/task`.

## Jira

1. Project key from the client name or from the user. Ask once if several projects match.
2. `GET /rest/api/3/issue/createmeta/{project}/issuetypes` then `.../issuetypes/{issueTypeId}` for the create screen.
3. Bind contract **type** to an issue type if that is how the project splits work; otherwise to a custom field on the screen.
4. For each custom field, keep `fieldId`, `name`, `schema`, `allowedValues` (id + value).
5. Required fields with no bind → Preview, not File.

## Asana

1. Project gid from name match in the workspace.
2. `GET /projects/{project_gid}/custom_field_settings` — each setting has the field gid, name, type, `enum_options`.
3. Asana has no native priority on every org — bind priority to a field if one exists, else leave it off the payload.
4. Sections: pick a section named like backlog / to do if present.

## Linear

1. Team from name match. Project or label for the client if that is how they slice.
2. Workflow states: pick the team's unstarted/backlog state.
3. Labels for type/size/surfaces when no custom fields exist.

## Language

Count the language of sampled titles + descriptions. Majority wins. If the list is empty, use the language of the user's paste. Do not default to Italian unless the schema sample (or overlay) says so — this catalog is used in more than one language.

## What you never do at discover

- Create a list, folder, field, or option to make the bind easier
- Reuse a list id from another workspace
- Treat the fallback pack as the schema
