---
root: true
targets: ["*"]
description: "Always-on rules from how-to-agent. Loaded in every session; lessons with a clear trigger live in the skills library and load on demand."
globs: ["**/*"]
cursor:
  alwaysApply: true
---

# Always-on rules

These rules apply to every action, so they load in every session. A rule belongs
here only if it must apply when no skill fires. Everything with a clear trigger
lives in `skills/` and loads on demand.

## Writing

Apply to all prose: docs, comments, commit messages, error messages, UI text, replies.

- Use literal, specific language. Replace metaphor, decorative wording, and insider jargon with the plain verb or the concrete condition. [[concrete-over-figurative]]
- Delete words that add no information. [[omit-needless-words]]
- State the conclusion or instruction first, then the supporting detail. [[lead-with-the-point]]
- Write in active voice: name the actor who performs the action. [[prefer-active-voice]]
- Give each sentence one idea. Split sentences that chain clauses. [[one-idea-per-sentence]]
- Use exactly one name for each concept. Do not alternate synonyms. [[consistent-terminology]]

## Claims

- Never invent a fact, measurement, or name. Every specific claim needs a source:
  the code, the docs, or the conversation. When no source exists, delete the
  claim or ask.
