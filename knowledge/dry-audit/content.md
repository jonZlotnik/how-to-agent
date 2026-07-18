# DRY Audit

DRY is about *knowledge*, not characters. Two functions that look alike but encode different rules aren't duplication. One business rule encoded in code + config + docs + a test fixture is. The audit hunts for knowledge with more than one home.

## When to use

- A change forces edits in 3+ files that "always have to move together"
- You're about to copy a block "just to tweak it slightly"
- Constants, enums, or strings appear in both code and configuration
- A schema lives in code and is re-described in markdown and a test fixture

## Protocol

1. **Pick a piece of knowledge** — a rule, threshold, name, schema, format. Not a function — a fact.
2. **Find every place it lives.** Grep widely: code, tests, configs, env vars, fixtures, docs, comments, migrations.
3. **Mark one as canonical.** Usually the one closest to the runtime decision (code beats doc, generator beats copy).
4. **Derive the rest.** Generate, import, reference, or delete. The non-canonical copies should disappear or become provably-equal references.
5. **Defend the boundary.** Add a test, type, or build step that fails if drift returns.

## Worked example

A `maxRetries=5` constant appears in `client.ts`, in `config.yaml`, in a README example, and as the literal `5` in a test. Real duplication. Canonical home: `config.yaml`. Code reads from config. README example links to the same key. Test reads it from the loaded config. One fact, one home, four references.

## Red flags (rationalizations to reject)

- "These two functions just happen to look alike." — Then they'll drift. Either they encode the same rule (deduplicate) or different rules (rename to make the difference obvious).
- "It's only two places." — It's two places that will diverge silently the first time one is updated.
- "Documentation is supposed to repeat the code." — No: documentation should *describe* code, not encode the same facts in a form that can rot.

## Composes with

- [[orthogonality-check]] — duplicated knowledge is one of the strongest coupling signals; the audits often surface the same modules.
- [[broken-windows]] — fresh duplication noticed early is a window. Patch it before it becomes the norm.
- [[design-by-contract]] — when a duplicated rule becomes a contract, the contract enforces the single source of truth.
