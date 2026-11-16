---
name: brand-voice-review
description: Reviews a marketing draft against the team's own brand voice rules, fixes each flagged line, and re-checks until it passes. The user fills in their voice rules in a marked section of this file. Use when someone says "check this against our voice", "does this sound like us", "brand review", "tighten this up", "make this less robotic", "review my draft", "edit this email", or hands over a blog post, landing page, email, ad or social post and asks for feedback. Use before anything ships to a customer, and to review a draft a colleague or another AI wrote.
metadata:
  version: "1.0"
  owner: content-camel
---

# Brand voice review

A reviewer who has read the voice rules catches what the writer can't see. This skill runs the
review, applies the fixes, and checks again, so the draft that comes back is one you can send.

## Your voice rules (fill this in)

Replace the examples below with your own. Tag every rule with why it exists and, when you can, the
correction that produced it. Rules without reasons get applied too rigidly or too loosely. Describe
the mechanism, and keep sample sentences out: examples get copied word for word.

<!-- START YOUR RULES -->
| # | Rule | Why | Source |
|---|---|---|---|
| V1 | Example: say what changes for the reader before saying what we built. | Readers decide fast whether it's for them. | Your edit, date |
| V2 | Example: no claims about customers that you can't source. | Trust, and legal exposure. | |
| V3 | Example: contract where you'd in speech. | Uncontracted copy reads as machine-written. | |
| V4 | Example: banned words and phrases: add your list here. | These mark generic copy. | |
<!-- END YOUR RULES -->

If this section is still the examples, say so and review only against the general checks below.

## Steps

1. **Run the countable checks first**, if you have a script or tool: length limits, banned words,
   links, required elements. These are facts, so fix them before spending judgment.
2. **Read the draft against each rule,** in order. For every miss, quote the exact line, name the rule
   (V2, say), and say why it misses. Don't give an overall score before the reasoning.
3. **Apply the general checks** (they hold for most teams):
   - Can you tell who wrote it and who it's for?
   - Does every claim carry a source, a number the writer owns, or a hedge?
   - Does it commit to a point, or hedge every sentence?
   - Is the structure varied, or is every paragraph the same shape?
4. **Weight by severity.** Missing a point, an unsourced claim, or a broken rule on the voice's core
   fails the draft. A single odd word is a polish note. Low-severity findings get fixed too. They add up.
5. **Fix, don't just flag.** Rewrite each flagged line and keep the writer's meaning. Show both. Add no facts, figures or quotes beyond what's in the draft.
6. **Re-check.** Run steps 1 to 4 again. Three rounds at most. Still failing? Stop and report the rule instead of contorting the sentence.
7. **Report:** verdict (passes or needs a human), the fixes made, and any rule you suggest adding
   because the same miss happened twice.

## Why these rules

- The reasoning comes before the verdict because a score produced first is a guess with a number.
- Fixing is part of the job. A list of problems is a to-do list for someone else.
- The "suggest a rule" step is how the review compounds: repeated misses become rules, with a version bump.

## Example

Input draft line (email): "We are thrilled to announce our new reporting feature, which empowers
teams to unlock actionable insights."

Output: *Flagged V1 (opens with us, not the reader) and V4 (generic phrases). Fix:* "Your weekly
report now builds itself. Pick the metrics once and it lands in your inbox Monday." Re-check: passes V1 and V4. The claim describes the product's own behavior, so it needs no outside source. Confirm the detail against the feature before sending.

## Changelog

- 1.0: Initial version.
