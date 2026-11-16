---
name: skill-from-session
description: Turns a long correction session into a new reusable skill, or into a version bump of an existing one, by unpacking what the user fixed into rules with reasons, generalizing past the last case, and testing in a fresh chat. Use when someone says "turn this into a skill", "unpack what we just fixed", "write down what you learned", "I keep correcting the same things", "make this repeatable", "update the skill with these corrections", "version this", or at the end of any session where the user edited the agent's output several times. Use after drafting a campaign brief, email, landing page, ad copy, report or blog post with heavy edits.
metadata:
  version: "1.0"
  owner: content-camel
---

# Skill from session

Corrections are the most valuable thing a session produces and the first thing lost. If you fix the
same problem downstream every week, the fix belongs upstream, in a written skill the next run reads
first. This skill turns a session's rework into that skill, and keeps it from becoming a transcript.

## Steps

1. **Collect the corrections.** Go through the session and list each place the user changed,
   rejected or redirected the output. Quote the before and after. If the session isn't in context, ask
   for the final version and the first draft.
2. **Unpack each correction into a rule with a reason.** For each: *what the agent did*, *what the
   user wanted instead*, *why*. If the user hasn't said why, ask once, or write your best guess and mark
   it `CONFIRM`. A rule without a reason gets applied rigidly or dropped.
3. **Generalize past the last case.** Ask of every rule: what is the broader pattern, and would it
   apply to the next piece of work that looks different? "Don't open with a question" becomes "Open with
   the reader's situation or a plain claim", because the next draft will find a new way to break the
   narrow version. Don't paste examples from the session as the rule; they get copied back verbatim.
4. **Sort by how strict it should be.** Where the output must be consistent, write an exact template.
   Where it's judgment, write the principle and the reason. Cut anything the model already knows.
5. **Write or update the SKILL.md.** New skill: write the frontmatter. Give it a `name`. Give it a `description` saying what it does and when to use it, in the phrases people say. Add `metadata` with `version: "1.0"` and an owner. Existing skill: merge the rules in, remove ones now covered, and bump the version
   (1.0 to 1.1 for added rules, 2.0 for a change in how it works). Add a changelog line saying
   which corrections drove the change. One focused job per skill, one default rather than a menu.
6. **Add a check-then-fix loop** so the skill can also review other people's work: check the draft
   against the rules, fix what fails, re-check.
7. **Keep at least three test tasks.** Save three real pieces of work, including one that looks
   different from the session. Run each without the skill, note the misses, then run with it.
8. **Test once in a fresh chat on real work.** Not the session that produced it, which has the
   context the skill lacks. Whatever still goes wrong comes back as corrections. Repeat from step 1.

## Why these rules

- A pasted transcript isn't a skill. It encodes the last case and misses the next.
- Versions and a changelog matter because neither Claude nor ChatGPT documents an edit history for
  skills. The master copy lives with you.
- The fresh-chat test is the only way to learn whether the skill carries what the session carried.

## Example

Input: a session where the user rewrote three product-launch emails, each time cutting the opening
paragraph and moving the call to action up.

Output rules (abridged): *Lead with what changes for the reader, not company news. Reason: readers decide
in the first two lines whether this is for them.* *Put one call to action above the fold. Reason:
the click rate depends on seeing it without scrolling.* The version goes from 1.0 to 1.1. The changelog reads "Opening and call-to-action rules from launch email edits." Test tasks saved: a launch email, a webinar invite, a newsletter intro.

## Changelog

- 1.0: Initial version.
