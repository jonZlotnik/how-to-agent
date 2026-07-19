---
name: writing-agent-skills
description: "Writes or revises a SKILL.md so an agent triggers it at the right time and follows it reliably. Use when creating, editing, or reviewing a skill. Do not use for instructions that apply to every session — put those in AGENTS.md or CLAUDE.md."
---

# Writing Agent Skills

A skill has two jobs: fire at the right moment, and change what the agent does once it fires. The description does the first job; the body does the second. Most bad skills fail at one of these — they never trigger, or they trigger and the agent behaves the same as without them.

## When to use

- Creating a new skill or reviewing a skill in a PR
- A skill exists but agents never seem to invoke it
- A skill fires but the agent's output looks the same as without it
- Deciding whether guidance belongs in a skill or in an always-on file

## Protocol

1. **Write the description as a routing rule.** Lead with a third-person action verb stating what the skill does — "Deletes stale branches", not "Delete stale branches". The description is a catalog entry loaded into every session; an imperative there reads as a standing instruction, while imperatives belong in the body, which loads only on activation. Follow with "Use when" triggers, then a "Do not use" boundary. Keep the first 250 characters self-sufficient — some agents truncate there. State triggers generously: agents under-trigger skills more often than they over-trigger them.
2. **State each rule with its reason.** "Never invent a measurement, because a fabricated number reads as authority" generalizes to cases the skill never mentions; a bare list of MUSTs does not. Use literal language throughout ([[concrete-over-figurative]]).
3. **Constrain what the agent may invent.** Any step of the form "replace vague with specific" or "fill in the details" must name the source of the specifics and say what to do when no source exists: delete the claim, cite where it came from, or ask. A step that demands specificity without a source produces fabrication.
4. **Give the body three working parts.** A worked before/after example in a fenced block; explicit prohibitions with the rationalizations they reject; and a validation loop that tells the agent how to check its output and when to stop.
5. **Keep the body lean.** The description loads in every session, the body loads on activation, and bundled files load on demand — so put reference material in `references/` and keep the body under ~500 lines. Cut any rule that does not change behavior.
6. **Test against a baseline.** Run an agent on a target task without the skill and record what it does; run again with the skill. If the output does not change, the skill teaches nothing, no matter how well it reads. Validate structure with `skills-ref validate` and a quality linter.

## Example

```
Bad:  description: "Helps with error handling best practices."

Good: description: "Wraps fallible calls in explicit error handling.
      Use when writing code that does I/O, parsing, or network calls.
      Do not use for throwaway prototype code."
```

## Red flags (rationalizations to reject)

- "The agent will figure out when to use it." — The description is the only signal at routing time. A trigger that is not written there does not exist.
- "More rules make it safer." — More rules make it longer, and every body token competes with the task. Keep the rules that change behavior; delete the rest.
- "It scores well, so it works." — Linters measure form. Only a baseline comparison measures whether the skill changes what an agent does.

## Composes with

- [[concrete-over-figurative]] — skill prose must be literal; agents execute what the words say, not what the image implies.
- [[omit-needless-words]] — body length is a budget spent against the task itself.
- [[lead-with-the-point]] — the description's first clause is the routing signal; lead with what the skill does.
- [[prove-dont-assume]] — the baseline test is proof; a well-formatted skill is an assumption.
