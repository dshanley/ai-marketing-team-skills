---
name: pre-mortem
description: Runs a pre-mortem on a marketing plan before anyone builds it, using one of three flavours (it failed so what went wrong, what could go wrong, or devil's advocate with a simpler alternative) matched to the stakes, then shrinks the plan to the smallest useful first piece. Use when someone says "what could go wrong", "stress-test this plan", "poke holes in this", "pre-mortem", "is this a good idea", "before we launch", "play devil's advocate", or "am I overbuilding this". Use before a campaign launch, a new landing page, a paid search budget change, an email blast, a site migration or any plan an agent is about to execute.
metadata:
  version: "1.0"
  owner: content-camel
---

# Pre-mortem

A requirements review confirms the plan matches the request. A pre-mortem asks whether the request
was right. It catches the things where every box ticks yes and the plan is still wrong: no spend cap
on the campaign, an email blast that isn't metered, six small decisions that quietly made the
project three times bigger.

## Pick the flavour by stakes

| Stakes | Use | Prompt |
|---|---|---|
| Low: cheap to undo, small audience, internal | None. Just build small. | Skip it. A pre-mortem on every small change is review fatigue. |
| Medium: real spend, real audience, reversible with effort | **What could go wrong** | "List what could go wrong with this plan, ranked by likelihood times damage." |
| High: public, hard to undo, or tied to a number someone reports | **It failed** | "It's a month from now and this failed. What went wrong?" |
| A plan that feels big, or one that hasn't been questioned | **Devil's advocate** | "How is this plan completely wrong? Is there a much simpler way to get the outcome?" |

Default when unsure: "what could go wrong". Use two flavours only when the plan is both high-stakes
and large. "It failed" works best because stating a failure as fact lets people name causes they
wouldn't raise as possibilities.

## Steps

1. **State the plan and the outcome** in two or three sentences. If the outcome is missing, ask
   for it before going on. A pre-mortem with no outcome has nothing to fail against.
2. **Pick the flavour** from the table. Say which and why in one line.
3. **Run it.** Produce at most seven failure causes. Make each specific to this plan, not a generic
   risk ("no cap on daily spend in the new campaign", not "budget risk"). Mark each *likely* or
   *possible*, and say what you'd see first if it were happening.
4. **Turn each cause into a decision.** One of: add a checkpoint, change the plan, accept the risk
   on purpose, or find out first.
5. **Shrink the plan.** Name the smallest piece that tests the riskiest assumption and ships in days,
   not weeks. State what result would justify building the rest.
6. **Check, then fix.** Are the causes specific to this plan? Does each have a decision? Is the
   smallest piece actually smaller than the plan, and does it test the biggest assumption? Fix and
   re-check.

## Why these rules

- The cap of seven keeps the list readable. A list of thirty risks gets ignored.
- Devil's advocate asks for a simpler alternative, because the usual failure is a plan bigger
  than the outcome needs.
- Building small is part of the exercise. A pre-mortem with no change to the plan was theatre.

## Example

Input: "Launch a 12-ad-group paid search campaign for our new feature next Monday."

Flavour: it failed (public spend, hard to recover a wasted week).

Output (abridged): *Likely:* no daily cap, so a broad-match ad group burns the budget before anyone
looks. First sign: spend by Tuesday morning far above the daily average. Decision: add a cap and a
spend checkpoint each morning. *Possible:* the landing page doesn't match the ad promise, so the
bounce is high. Decision: find out first, by checking three ads against the page. Smallest first
piece: two ad groups on the highest-intent terms for one week. Build the other ten only if the cost
per sign-up is acceptable to the campaign owner.

## Changelog

- 1.0: Initial version.
