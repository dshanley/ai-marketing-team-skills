# Hand it to your agent: 11 prompts

The prompts from Part 7 of the field guide *Your Team of 4 Is Actually 40*. Copy one into your
agent and fill in the brackets.

Prompts marked **Standing** go into your Project or custom instructions once and apply from then on.

Prompts 07 to 09 and 11 work best in an agent connected to your calendar and shared folder. If it
can't reach them, it drafts the invite or the update for you to paste.

## The work

### 01 Goal cascade

One line per level. The agent does the interviewing.

```text
Interview me for my goal cascade: company, team or client, project, role, task. Ask about one
level at a time. If my answer runs past one line, push back until it fits. For the task, get
three sentences: the customer, who uses it, what it's for. Save the result as goals.md in our
shared folder.
```

Example: **Task:** webinar recap post. For marketing ops leads, who forward it to their team, to
book demos.

Skill version: [`goal-cascade`](../skills/goal-cascade)

### 02 Checkpoint designer

For one recurring workflow.

```text
Here's the brief for [workflow] and the last three outputs. Propose the steps, one yes/no check
per step, who or what answers each check (a script, an agent or a person), and what happens on a
no. Return a table. Flag any check you can't verify from the output itself.
```

Example: **Draft:** Does every claim appear on the approved list? **Answers:** a script, then the
editor. **On a no:** fix and re-run.

Skill version: [`checkpoint-designer`](../skills/checkpoint-designer)

### 03 Skill document

After a long correction session.

```text
Unpack what we just fixed into a skill document. Start with a header: name, version, owner,
description (what it does, when to use it) and when not to use it. If the skill already exists,
bump the version and list what changed.
```

Skill version: [`skill-from-session`](../skills/skill-from-session)

### 07 Weekly bottleneck

Once a week, from what the agent can see.

```text
Look at my calendar and task notes for the last two weeks. Name the recurring step that took the
most hours and estimate them. Say which parts a script or an agent could handle and which need me.
```

## Standing instructions

### 04 Decision log (Standing)

```text
Whenever you make a decision or bring one to me, add a row to decision-log.md: the category,
whether it's reversible, who decided, and the rule we used. When the same category shows up a
third time, propose a written rule for it.
```

Example: **Subject-line variants:** reversible. The agent decides. Pick any that pass the claims
check.

### 05 Completed staff work (Standing)

So decisions arrive ready to make.

```text
Anything you bring to me for a decision arrives on one page: the problem, two or three options
with what each costs, and your recommendation. Don't hand me open questions.
```

Skill version: [`completed-staff-work`](../skills/completed-staff-work)

### 06 Pre-mortem (Standing)

Before anything consequential.

```text
Before any step that sends to a list, spends money or launches something: assume it's next month
and this failed. List what went wrong. Add a check for each risk to the workflow, then continue.
```

Skill version: [`pre-mortem`](../skills/pre-mortem)

## The meeting

### 08 Schedule the practice meeting

```text
Book a 60-minute kickoff with [team] in the next two weeks. Then book a recurring 30-minute AI
practice meeting: weekly for the first month, then every other week, same slot. Put this agenda
in every invite. Rotate the host through the team and name the host in each invite. If you can't
reach my calendar, draft the invites for me to send.

Agenda, 30 minutes:
0 to 3    Win or flop of the week, lead first
3 to 15   Two 5-minute demos. One is a failure every other session.
15 to 22  One correction goes upstream: skill, goal or checkpoint?
22 to 27  Decision rules: allowed, needs a checkpoint, two-way door
27 to 30  One thing each person tries this week
```

Full agenda and roles: [`templates/ai-practice-meeting-agenda.md`](../templates/ai-practice-meeting-agenda.md)

### 09 After each meeting

Keeps the meeting running without an admin.

```text
Here are the notes from today's AI practice meeting. Update our AI track record (works,
struggles, fails), the decision log and the skill library changelog. Then draft the next
session's agenda and name the next host.
```

### 10 What your team already uses

For the kickoff poll.

```text
Draft a five-question poll for our AI kickoff: which AI tools each person uses, for which tasks,
what they've built, and what worries them. When the answers are in, sort them into four areas
(your own assistants, your team's assistants, your vendors' agents, and your heaviest AI user) and show
where we're strong and where we're thin.
```

## Your first week

### 11 Your first week

The agent builds the plan. The lists below are what it should produce.

```text
Read the attached guide. Ask me five questions about my team and my work, then build my
first-week list from the leader path or the solo path, whichever fits. Put each item on my
calendar as a 20-minute task this week.
```

**If you lead a team**

- [ ] Book the kickoff (08)
- [ ] Name a rotating host and a librarian
- [ ] Checkpoint one recurring workflow (02)
- [ ] Write the team goal (01) and share it
- [ ] Say where experimenting is allowed
- [ ] Demo something yourself, flop included

**If you work alone**

- [ ] Write your own goal cascade (01)
- [ ] Three-sentence brief on your next task
- [ ] Pre-mortem one big task (06)
- [ ] Note every correction on one real task
- [ ] Turn it into a skill (03); test it fresh
- [ ] Name your biggest time sink (07)
