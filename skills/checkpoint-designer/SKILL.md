---
name: checkpoint-designer
description: Turns a marketing workflow into numbered steps with a yes/no checkpoint after each one, says who or what answers each checkpoint, and builds a register of decision categories with rules for which calls an agent makes alone and which come back to a person. Use when someone says "agent skipped a step", "it drifted from the brief", "make this workflow reliable", "design the process for the agent", "what should it decide on its own", "it asks me about everything", "set up review for the campaign", or "write the SOP". Use for recurring work such as campaign launches, paid search builds, email sends, SEO updates and content production, and any time an agent is handed a multi-step job.
metadata:
  version: "1.0"
  owner: content-camel
---

# Checkpoint designer

Hand an agent ten steps and it won't tell you it skipped step five. The fix is a yes/no checkpoint
after every step, where step two doesn't start until step one is checked and done. The second half
of the job is deciding who answers each checkpoint, so the agent neither asks about everything nor
decides things it should not.

## Steps

1. **List the steps** of the workflow in order. If the user has no process, ask for the last real
   run and work back from what happened. Aim for 5 to 12 steps. Fewer means they are too coarse to
   check. More means some belong together.
2. **Write one checkpoint per step** as a yes/no question that a stranger could answer from the
   output alone ("Does every ad group have at least three headlines?", not "Is the copy good?"). If a
   check needs judgment, name the standard it's judged against.
3. **Assign who answers.** Use the first that fits:
   - *Script or tool*, for anything countable (character limits, links resolve, UTM tags present).
   - *The agent*, checking its own output against a written standard.
   - *A person*, only where the answer needs taste, politics or accountability.
4. **Say what happens on "no".** Default: the agent fixes and re-checks once, then stops and
   reports. "Continue anyway" isn't an option.
5. **Classify each decision the step contains** as a two-way door or a one-way door:
   - *Two-way door*: cheap to reverse (headline variant, subject line, send-time within a window).
     Decided inside the boundary by the agent or the person doing the step. No escalation.
   - *One-way door*: expensive or impossible to reverse (spend above a cap, a send to the full list,
     publishing under an executive's name, a claim about a customer). It stops and comes back to a
     person as completed staff work: the problem, the options, a recommendation.
6. **Build the decision register.** Group the decisions into categories and write one rule each, so
   the same decision gets solved once. Use `decision-register-template.md`.
7. **Check, then fix.** Verify each of these. Every step has a checkpoint. Every checkpoint has an answerer and a "no" path. Every one-way door has an escalation. Rewrite any checkpoint answered by "looks fine".
   Fix gaps and re-verify.

## Why these rules

- Without an answerer, a checkpoint becomes "the agent says it checked". A script or a person is
  the only answer that costs nothing to trust.
- Without the door split, every agent escalates every small call and the reviewer drowns, or the agent
  quietly makes the one call that needed you. The register is how a "stop only for critical
  decisions" instruction becomes a written policy.
- Rules go in the register by category, not by incident, so the next case you didn't predict is
  still covered.

## Example

Input: "Weekly newsletter: write, check links, schedule, send to 12,000 subscribers."

Output (abridged):

| # | Step | Checkpoint (yes/no) | Answered by | On no |
|---|---|---|---|---|
| 1 | Draft issue | Does it follow the issue outline and name one call to action? | Agent | Fix, re-check once |
| 2 | Check links | Do all links resolve and carry UTM tags? | Script | Fix, re-run |
| 3 | Approve copy | Do claims about customers match approved sources? | Person | Return to step 1 |
| 4 | Schedule | Is the send set to the right segment and a time inside the window? | Agent | Fix |
| 5 | Send | Has a person approved the full-list send? | Person (one-way door) | Hold |

Register rows: "Subject line variants" two-way, agent decides. "Full-list send" one-way, person
decides, comes as problem, options, recommendation.

## Output

Deliver the step table, the register, and a one-line instruction the user can paste into the agent:
"Run the steps in order. Don't start a step until the previous checkpoint passes. Decide two-way
doors yourself and log them. Stop and bring me any one-way door as problem, options, recommendation."

## Changelog

- 1.0: Initial version.
