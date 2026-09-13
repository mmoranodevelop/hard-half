# Ghost classes

Five ways a stated problem fails to be load-bearing. Pick the class whose death does the most work. Stacking is allowed; reporting four classes with no parent is not.

Each class has a **kill test**: the observation that would make this class the wrong diagnosis. If you cannot write the kill test, you do not have a class yet.

## 1. Proxy

They named the stand-in they can chart (NPS, ticket volume, cycle time, a RAG status) instead of the hurt.

**Monday test usually fires.** The dashboard owner is the only Monday.

**Kill test:** a named person, outside the reporting chain, whose actual hour of work changes when the proxy moves — and they would notice without being told the number.

Typical failure of the default agent: optimize the proxy.

## 2. Dissolved

The conditions that made the problem real ended. The ritual (standup, committee, OKR, vendor) continues because stopping would require someone to say the war is over.

**Origin test usually fires.** The asserter has left, the regulation changed, the customer churned, the outage was three years ago.

**Kill test:** one current week in which a named person still pays the original cost, not the cost of maintaining the ritual.

Typical failure: a "revamp" of the ritual.

## 3. Political

The ticket exists to keep a coalition together, to occupy a rival, or to prove a function is busy. Solving it would cost the people who opened it.

**Monday test fires in reverse:** someone's Monday gets *worse* if you solve it (they lose a reason to meet, a budget line, a scapegoat).

**Kill test:** the owner will still sponsor the work after you write the Monday-gets-worse sentence on the page. If they flinch, you have the class.

Do not moralize. Name the coalition and the cost of solving. The ASK is often `stop the ritual` or `keep stated` with eyes open — that is a political choice, not a reasoning failure.

Typical failure: a "better alignment workshop" that feeds the coalition.

## 4. Symptom

A parent problem's death would kill this one. The ticket is a downstream flare.

**Parent test fires.** Y is nameable; X is what Y looks like on this team's board.

**Kill test:** solve (or cheaply simulate solving) Y in a slice and watch whether X's tickets still open. If they do, this is not a symptom of that Y.

The parent must be *more local* than a slogan ("culture", "communication", "tech debt"). A parent you cannot put a confirmation test on is not a parent.

If the parent is stuck on a floor, hand to `first-principles`. If it is a customer job, hand to `jobs-to-be-done` *on the parent*.

Typical failure: treating every symptom as its own epic.

## 5. Inherited slogan

Nobody in the room can say who asserted the problem or what "solved" means. It arrived with a strategy deck, a predecessor, or an industry cliché.

**Origin test fires hard.** "We've always had a data quality problem" with no owner, no Monday, no date.

**Kill test:** a dated assertion with a name, and a yes/no for solved that a stranger could score.

Until the slogan is locked into a stated problem, you cannot displace it — there is nothing to displace. Force a sentence or dissolve.

Typical failure: a new workstream titled with the slogan.

## Choosing among them

If Monday is empty and origin is empty → inherited or dissolved; check current cost.
If a Y is obvious → symptom; do not also call it proxy unless the Y is itself a metric.
If solving would punish the sponsor → political; say so.
If the only Monday is a chart → proxy.

Unknown is allowed. "Could be political or dissolved — ASK: one interview with the original asserter" is a complete step-3.
