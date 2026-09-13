# Tracker adapters

Inspect MCP tools in this session first. The names below are the public APIs; MCP wrappers differ. Do not invent a tool. Do not create fields, lists, or options unless the user explicitly asked to change the workspace.

After a successful create, set checklists in a second call if the create endpoint does not accept them.

## ClickUp

**Create:** `POST /v2/list/{list_id}/task`

Body (typical):

```json
{
  "name": "[CODE]: outcome",
  "markdown_description": "...",
  "status": "<exact status string from the list>",
  "priority": 3,
  "due_date": 1719792000000,
  "start_date": null,
  "assignees": [],
  "custom_fields": [
    { "id": "<field uuid>", "value": "<option uuid or native value>" }
  ]
}
```

Priority integers: `1` urgent, `2` high, `3` normal, `4` low.

`custom_fields` values are only saved if the field applies to this task type (`applied_objects` / default task). If a field silently drops, set it with `POST /v2/task/{task_id}/field/{field_id}`.

**Checklists:** `POST /v2/task/{task_id}/checklist` with `{ "name": "…" }`, then add items. MCP servers often expose `create_task` with `custom_fields` as a map of fieldId → value, plus separate checklist tools.

**MCP note:** some servers want `listName` rather than id. Resolve name → id during discover so you do not create in a homonymous list in another space.

Docs: [Get accessible custom fields](https://developer.clickup.com/reference/getaccessiblecustomfields), [Create task](https://developer.clickup.com/reference/createtask).

## Jira Cloud

1. `GET /rest/api/3/issue/createmeta/{projectKey}/issuetypes/{issueTypeId}`
2. `POST /rest/api/3/issue`

```json
{
  "fields": {
    "project": { "key": "ABC" },
    "issuetype": { "id": "10001" },
    "summary": "[CODE]: outcome",
    "description": { "type": "doc", "version": 1, "content": [] },
    "priority": { "name": "High" },
    "duedate": "2026-07-25",
    "customfield_10040": { "id": "10100" }
  }
}
```

ADF for description on Cloud v3; plain string only if the site still accepts it. Checklists are not native — use a checklist custom field, a subtask per pack, or description checkboxes. Say which on the preview.

Do not send fields that are not on the create screen.

Docs: [Create issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post).

## Asana

1. `GET /projects/{project_gid}/custom_field_settings`
2. `POST /tasks` with `projects`, `name`, `notes` or `html_notes`, `due_on`, `assignee` (null), `custom_fields`: `{ "<field_gid>": <value> }`

Enum value = option gid. Multi-enum = array of gids.

Put the task in the backlog-like section via `POST /sections/{section_gid}/addTask` if sections exist.

Checklists: `POST /tasks/{task_gid}/subtasks` for each item, or a single task's `html_notes` with `- [ ]` if the team treats that as the list.

Docs: [Custom field settings for a project](https://developers.asana.com/reference/getcustomfieldsettingsforproject).

## Linear

`issueCreate` (GraphQL): team, title, description, state (unstarted), label ids, due date, project.

No arbitrary custom fields on all plans — type/size/surfaces become labels that already exist. Do not create labels silently.

## Other trackers

Same contract. Discover the create metadata. Bind. Preview. Create. If you cannot discover fields, Preview-only markdown is acceptable — then say the tracker was not writable.

## After create

Return: title, url, destination, bound fields (label = native id), remaining holes, checklist names. One ASK only if a hole is load-bearing (wrong list, required field empty).
