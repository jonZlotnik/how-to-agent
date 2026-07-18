---
name: rule-of-generation
description: "Use before hand-writing a large set of similar functions, types, fixtures, or config files. Also use when reviewing a PR that adds the Nth nearly-identical case by hand. Also use when a schema, table, or spec already implicitly contains the answer."
---

# Rule of Generation

If the thing you're about to type follows a rule, type the rule and let a program write the rest. Human-authored repetition is where typos breed and edits go to die. The pattern *is* the source of truth; the expanded forms are derivatives.

## When to use

- About to write the Nth nearly-identical struct, accessor, test case, or migration
- A spec, OpenAPI schema, protobuf, or table already encodes the shape of what you'd write
- A code review reveals copy-paste with small tweaks
- A "table of constants" lives in code and also in docs and also in tests

## Protocol

1. **Find the pattern's authoritative form.** Schema, table, list of names, regex — whatever encodes the shape. If it doesn't exist yet, write *it* first.
2. **Generate the rest.** Codegen, template, macro, build step. The point is that the derivative artifacts can be rebuilt from the source at any time.
3. **Check in the generator and its output** when toolchain reproducibility matters. Check in only the generator when build determinism does.
4. **Add a check that the output is up to date.** A CI step that regenerates and diffs is cheap insurance against drift.
5. **Stop generating the moment the pattern breaks.** If half your cases are special, generation is fighting the domain — fall back to handwriting or split the domain.

## Red flags (rationalizations to reject)

- "It's only six cases." — Six cases now, six places to edit forever.
- "Generators are over-engineering." — Six near-identical hand-edits are over-engineering paid in maintenance instead of design.
- "I'll keep them in sync manually." — You won't. Nobody does. That's the whole reason this rule exists.

## Composes with

- [[rule-of-representation]] — generation is how you fold a pattern into data and re-derive the code that walks it.
- [[rule-of-minilanguages]] — a tiny DSL for the pattern is often the cleanest source for the generator.
- [[dry-audit]] — generation is the standard cure for the duplication an audit surfaces.
- [[crash-early]] — make the generator fail loudly on a malformed source; never silently emit partial code.
