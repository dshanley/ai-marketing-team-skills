---
name: goal-cascade
description: Writes the goal for each level of a marketing team (company, team, project, task) and turns any task into a three-sentence brief (who the customer is, who uses the work, what it's for) before an AI agent starts. Use when someone says "brief the agent", "write the brief", "set up context for this project", "the AI keeps missing the point", "it doesn't understand what this is for", "write our team goal", "kick off a campaign with AI", or hands over a task with no stated purpose. Use it before drafting a campaign, landing page, email sequence, paid search plan or blog post, and whenever agent output is on topic but misses the point.
metadata:
  version: "1.0"
  owner: content-camel
---

# Goal cascade

Agents are rocket fuel on whatever direction you give them. A task with no stated purpose still gets
done, fast, in the wrong direction. This skill writes the goal down at every level, then boils it to
a three-sentence brief the agent carries into each task.

## Steps

1. **Collect what exists.** Ask for any current company goal, team goal, project brief or OKR.
   Use what is there. Don't invent a company mission. If a level is missing, draft one line from the
   levels above it and mark it `DRAFT: confirm`.
2. **Fill the cascade, one line per level**, top down, using `cascade-template.md`:
   company, team, project, task. Each level says what it's for. Not just what it is.
   Could a competitor post this level unchanged? Then it's too generic. Rewrite it.
3. **Write the three-sentence task brief.** Exactly three sentences:
   - *Customer:* who pays for or is helped by the outcome.
   - *User:* who touches the work product day to day (often a different person from the customer).
   - *Purpose:* what this work is for, and what changes if it works.
4. **Check, then fix.** Run these yes/no checks. Fix any "no", then re-run.
   - Does each level follow from the one above it (could you trace task to company)?
   - Does the brief name a real person or role for customer and for user, not "the audience"?
   - Does the purpose describe done in the world? It shouldn't describe what the agent produces.
   - Could the agent choose between two plausible approaches using only this brief?
5. **Hand over in loading order**: company, team, project, task. Give the agent only the levels the
   task needs. A paid search task needs the project and task lines plus the company line, not the
   full strategy deck.

## Why these rules

- Customer and user are split because they often differ. A marketer buys the content library, a rep
  uses it daily. Copy written for the buyer fails the user, and the reverse.
- "What it's for" beats "what to make", because an agent that knows the purpose can propose a better
  plan than the one you had in mind. State the outcome and let it design the approach.
- One line per level keeps the cascade readable. Long goals get skimmed by people and agents alike.

## Example

Input: "Write a landing page for our spring webinar."

Output brief:

> **Company:** Help mid-size B2B teams turn their content into pipeline.
> **Team:** Demand gen owns registrations and show-up for webinars this quarter.
> **Project:** Spring webinar on repurposing sales calls into content, 400 registrations target set by the demand gen lead.
> **Task brief:** The customer is the Director of Content at a 50 to 500 person B2B company who must show content drives pipeline. The user is the demand gen manager, who will send traffic to this page and read its conversion rate weekly. The page exists to get a Director of Content to register in under a minute, and it works if registrants say the topic matched a problem they already have.

Note the 400 figure is the team's own target, supplied by the user. Leave out any number the user didn't give.

## Output

Return the filled `cascade-template.md`, then the three-sentence brief on its own so it can be pasted
into any new chat. Offer to save the cascade as the standing context for the project.

## Changelog

- 1.0: Initial version.
