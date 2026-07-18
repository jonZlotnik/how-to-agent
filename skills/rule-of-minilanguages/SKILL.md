---
name: rule-of-minilanguages
description: "Use when a problem domain has repeatable declarative structure (rules, schemas, configurations, transformations). Also use when a config file is growing operators, conditionals, or templating. Also use before writing a third bespoke parser this quarter."
---

# Rule of Minilanguages

Some problems are most honest when expressed as a tiny language. A pattern matcher, a build description, a routing table — when the natural way to state the rules is *as rules*, code that pretends to be procedural is fighting the domain. A well-chosen minilanguage compresses a class of problems into something readable, declarative, and extensible.

## When to use

- Users (or you) keep writing the same shape of expression by hand
- A config file is sprouting conditionals, computed values, or shared fragments
- A domain is best described as patterns and transformations, not as steps
- You're about to write a parser ad hoc — for the third time

## Protocol

1. **Confirm the domain has shape.** A minilanguage pays off only when the same kinds of expressions repeat. One-offs are config; recurring patterns are language.
2. **Choose the smallest level of power.** Pick the least expressive form that fits — keyword=value before lists before expressions before Turing-complete. Power is a liability; you can't take it back.
3. **Borrow before inventing.** Existing minilanguages (regex, jq, awk, JSON-Pointer, SQL subset, glob, expr) often fit. Inventing means you also own the parser, errors, docs, and corner cases.
4. **Make it textual and editable** ([[rule-of-textuality]]). Even a binary-backed engine deserves a textual surface.
5. **Resist creep.** When users ask for "just one more feature", first see if existing primitives compose to do it. Macros and "just a quick if" are how minilanguages turn into ad-hoc programming languages without anyone deciding to.

## Red flags (rationalizations to reject)

- "We just need to add an `if`." — That's the moment a configuration becomes a programming language and starts owing you everything a language owes its users.
- "It's just a quick parser." — Quick parsers are how project-specific languages with no error messages happen.
- "Macros will make it cleaner." — Macros postpone complexity; they don't remove it. Beware.

## Composes with

- [[rule-of-generation]] — minilanguage descriptions are exactly the kind of source that generators thrive on.
- [[rule-of-representation]] — a minilanguage is often the most natural textual form of a data table.
- [[reversible-decisions]] — once a language is published, breaking changes are expensive; pick the least power you can.
- [[prototype-to-learn]] — prototype the language by writing example programs first; if they read well, the design is on track.
