---
name: orthogonality-check
description: "Use when designing a module, reviewing a PR that touches many files, or considering whether to merge or split a component. Also use when a 'small' change unexpectedly cascades through unrelated areas."
---

# Orthogonality Check

Orthogonal components change independently. The test is simple: change one thing; count what else must move. If unrelated areas have to follow, the design is coupled, and every future change pays that tax.

## When to use

- Designing a new module, service, or class
- Reviewing a diff that spans modules you thought were unrelated
- A bug in feature A is fixed by changing feature B
- Tests fail in distant subsystems when one file changes

## Protocol

1. **Name the change.** "Switch the user store from SQL to KV." "Change the rate limit window."
2. **List what must move with it.** Be ruthless — include tests, docs, configs, types, mocks, fixtures.
3. **Cluster the impacts.** Same module / adjacent module / unrelated module. Anything in the third bucket is a coupling smell.
4. **Trace each unrelated impact to its cause** — shared mutable state, leaked types, implicit ordering, knowledge duplication ([[dry-audit]]), reaching into private guts.
5. **Decide**: refactor the seam (introduce an interface, a parameter, an event), or accept and document the coupling. Don't silently absorb it.

## Quick coupling indicators

- Two modules import each other (cycle)
- A "utility" file is imported by half the codebase and edited every sprint
- Changing a database column requires UI edits
- A test in module A breaks when module B is refactored

## Red flags (rationalizations to reject)

- "It's just one extra change, no big deal." — One extra change, every time, forever.
- "They're naturally related." — Maybe. Often "naturally related" means "I never separated them".
- "Decoupling would be over-engineering." — Coupling is the over-engineering; you're paying compound interest on it.

## Composes with

- [[dry-audit]] — shared knowledge is the most common coupling cause.
- [[reversible-decisions]] — orthogonal designs keep more decisions reversible.
- [[design-by-contract]] — explicit contracts at module seams are the cheapest way to decouple.
- [[broken-windows]] — quietly worsening coupling is the canonical broken window.
