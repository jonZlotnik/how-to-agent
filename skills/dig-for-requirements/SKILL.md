---
name: dig-for-requirements
description: "Identifies the real need behind a vague task before designing. Use when given a terse feature request or a 'just do X' instruction, or when the request names a solution rather than a need. Do not use when the need is already explicit."
---

# Dig for Requirements

Requirements rarely lie on the surface. A user asking for "a way to log in" may actually need "a way to keep their cart between sessions". Solve the wrong problem and you ship perfectly-built waste. The job is to excavate the *real* need before designing anything.

## When to use

- The request is one or two sentences and names a solution ("add a dropdown", "use Redis")
- You catch yourself filling in obvious-seeming gaps with assumptions
- The user said "obviously" or "just" — those words almost always hide constraints
- Multiple plausible interpretations exist and you're about to pick one silently

## Protocol

1. **Restate the ask** in your own words back to the user. If they correct you, you found a gap.
2. **Ask "why" until you reach a user-facing outcome.** "Add export to CSV" → why → "so finance can reconcile" → why → real need is *reconciliation*, which a join report might solve better.
3. **Hunt unstated constraints.** Volume? Frequency? Who is the user? What's the failure mode that prompted this? What did they try before?
4. **List what you're assuming.** Read the list back. **Never** treat an assumption the design depends on as settled — confirm it with the user.
5. **Restate the goal in one sentence** and read it back; repeat steps 1–4 until the user confirms it without correction.

## Example

```
Ask:   "Add CSV export to the reports page."
Why? → "So finance can reconcile against their ledger."
Why? → "The dashboard totals don't match the ledger."
Real need: reconciliation — a matched-totals view may beat raw CSV.
```

## Red flags (rationalizations to reject)

- "The ticket is clear enough." — Tickets describe symptoms. Dig for the disease.
- "I'll just clarify as I go." — Mid-build clarification is the most expensive kind.
- "They said exactly what they want." — They said exactly what they *thought of*. The need is bigger.
- "Asking more questions wastes their time." — Building the wrong thing wastes more.

## Composes with

- [[tracer-bullet]] — once the real need is clear, build the thinnest end-to-end slice.
- [[prototype-to-learn]] — when the requirement is too ambiguous to specify, prototype to make it concrete.
- [[reversible-decisions]] — when the dig surfaces a commitment (vendor, schema), evaluate reversibility before locking in.
