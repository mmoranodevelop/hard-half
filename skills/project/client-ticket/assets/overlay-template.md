# Overlay template

Copy to **the working repo** as `.hard-half/client-ticket.md` (or paste into the ClickUp list / Jira project description). Do not put client names in the public skill.

```markdown
# client-ticket overlay

tracker: clickup          # clickup | jira | asana | linear
workspace:                # optional id or name
clients_folder:           # folder/space that holds per-client lists

# Extra field aliases (live name → slot)
# aliases:
#   Categoria: type
#   T-shirt: size

language:                 # it | en | (empty = sample the list)

# Title pattern if not [CODE]: outcome
# title: "[{code}]: {outcome}"
```

Live schema still wins. This file cannot create a field that does not exist.
