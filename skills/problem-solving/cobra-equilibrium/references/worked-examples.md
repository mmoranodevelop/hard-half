# Worked examples

Illustrative. Unknowns stay unknown. One of these is a refuse.

## 1. Forecast — time-to-close SLA

**Instrument:** support tickets closed in under 24h, bonus on the rate.

**Intent:** customers with a broken thing get a working thing.

**Legal moves:** close and reopen; reclassify as "pending customer"; close with a template that does not fix.

**Playbook:**
1. Agents close-reopen at 23h; instrument up; intent flat.
2. Owner bans reopen-within-48h; instrument dips then recovers.
3. "Pending customer" share explodes; hard cases wait outside the clock; instrument healthy; intent dead.

**Cobra:** 24h-rate green; time-to-working-thing unmeasured and worse.

**Exit:** `change instrument` to time-until-the-customer's-thing-works, sampled by a party who is not the closer — or `do not ship` the bonus on 24h.

**ASK:** `do not ship` the bonus as specified.

## 2. Autopsy — "helpfulness" agent reward

**Incoming:** "The agent is so helpful now. Customers still can't finish the job. The eval looks great."

**Instrument:** a grader that scores message-level helpfulness.

**Intent:** the user completes the job they opened the chat for.

**Playbook already run:** cycle one, longer polite answers; cycle two, they added "be concise" to the prompt; cycle three, the agent asks clarifying questions forever (helpfulness up, completion down).

**Exit:** `change payoff` — reward job-complete on a held-out set the agent cannot detect, or `retire live instrument`.

Do not add a second "helpfulness v2" without a joint-failure story.

## 3. Refuse — a number that cannot survive

**Incoming:** "Give us one KPI for engineering productivity we can bonus on this quarter."

**Intent** (if honest): more valuable software in users' hands per week of engineering.

**Any single volume or activity number** (PRs, story points, commits, lines) has a three-cycle eat-path that is already public knowledge. A composite without a joint-failure story is a dashboard of cobras.

**Mode:** Refuse. What would have to be true: a measure the team cannot move without the product moving, reviewed faster than the eat-path, payoff not attached until the eat-path is broken on paper. Until then, no bonus on a productivity KPI.

**ASK:** `do not ship`.
