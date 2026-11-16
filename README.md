# AI Marketing Team Skills

Skills, templates and workflow cards for marketing teams that run AI agents. Built by
[Content Camel](https://www.contentcamel.io).

If your team uses AI agents, your team of 4 is really 40, and anyone running an agent is a manager now,
reports or not. The tools are new. Running a team well is not. This repo turns the habits that
work for human teams into skills your agents can actually follow.

It's the companion to our field guide, *Your Team of 4 Is Actually 40*, which came out of
[The Build Report #4](https://www.contentcamel.io) webinar with Keith Holloway of
[PureSEM](https://www.puresem.com).

## The six practices

1. **Start with the outcome, not the solution.** Say what done looks like and let the agent
   propose the plan.
2. **Checkpoint every step.** A yes/no check after each step, and step two doesn't start until
   step one passes. Decide up front which calls the agent can make on its own and which come back
   to you.
3. **Write the goal down at every level.** Company, team, project, task. Every task carries three
   sentences: who the customer is, who uses it, what the work is for.
4. **Review to define good, then write it down.** Review closely until you know what good looks
   like, then turn your corrections into a versioned skill.
5. **Run a pre-mortem, then build small.** Ask what will go wrong before you start, then ship the
   smallest useful piece.
6. **Solve one bottleneck at a time.** Find what takes the most time and fix that one thing all the
   way down.

## What's in here

Six skills and two one-page workflow cards. Each skill is a folder you can drop into your agent.

| Skill | What it does | Practice |
|---|---|---|
| [`goal-cascade`](skills/goal-cascade) | Writes the goal for each level and the three-sentence task brief | 3 |
| [`checkpoint-designer`](skills/checkpoint-designer) | Turns a workflow into steps with yes/no checks and decision rules | 2 |
| [`pre-mortem`](skills/pre-mortem) | Runs "it failed, what went wrong", "what could go wrong" and devil's advocate, matched to the stakes | 5 |
| [`completed-staff-work`](skills/completed-staff-work) | Brings a decision up as the problem, the options and a recommendation | 2 |
| [`skill-from-session`](skills/skill-from-session) | Turns a long correction session into a new or updated skill | 4 |
| [`brand-voice-review`](skills/brand-voice-review) | Checks a draft against your voice rules and fixes the flagged lines | 4 |

Two one-page workflow cards, one for team leads and one for the people doing the work:

- [Card A: Team lead](cards/team-lead.md)
- [Card B: Individual contributor](cards/individual-contributor.md)

There's also a [30-minute agenda for a team AI practice meeting](templates/ai-practice-meeting-agenda.md).

## How to use a skill

Each skill is a folder with a `SKILL.md` file in the open
[Agent Skills format](https://agentskills.io/specification): a name, a description of when to use
it, then plain instructions.

- **Claude:** zip the skill folder and upload it under Customize > Skills. On a Team or Enterprise
  plan you can share it with your team. ([Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude))
- **ChatGPT:** workspaces with Skills can import the same format. Otherwise, paste the `SKILL.md`
  into a Project's instructions.
- **No team setup:** keep the `SKILL.md` files as docs in a shared Drive or OneDrive folder and
  attach the one you need to the chat.

Name the skill in your prompt when it matters. A short request may not pick it up on its own.

To check a skill you've edited against the format's limits, run `python3 scripts/validate.py`. It checks the name, the folder match, the description length and the version fields.

## Make them yours

These are starting points. The skill only gets good once it holds your corrections:

1. Do the work with the agent and fix what's wrong.
2. Ask it to unpack what you fixed into the skill, with the reason for each rule.
3. Bump the `version` in the frontmatter and add a changelog line.
4. Try the new version in a fresh chat on real work before you trust it.

Give every skill an owner. Neither Claude nor ChatGPT documents an edit history for skills, so the master
copy belongs here or in your team's shared folder.

## About Content Camel

[Content Camel](https://www.contentcamel.io) is where marketing keeps the content sales actually
sends, and where you see what buyers do with it. It connects to Claude and other AI assistants over
MCP. Your people and your agents work from the same approved content.

Questions or ideas: open an issue, or [talk to us](https://www.contentcamel.io).
