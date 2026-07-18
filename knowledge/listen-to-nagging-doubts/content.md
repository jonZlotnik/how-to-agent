# Listen to Nagging Doubts

A vague unease about a piece of code is not noise. It's pattern recognition from below the threshold of articulation. The mistake is to push through it because you can't yet name it. Capture it, give it ten minutes, and either disprove it or escalate.

## When to use

- "Something about this feels wrong" but you can't articulate what
- Tests pass and the code looks right, yet you don't trust it
- You reviewed your own change and felt a flinch at one spot
- You're about to merge and there's a small reluctance you'd like to ignore

## Protocol

1. **Write the doubt down verbatim** — even half-formed. "The order of these two calls is off somehow." "I don't believe this test covers the case I care about." The act of writing often sharpens it.
2. **Spend ≤10 minutes investigating.** Read the suspicious code carefully, run the relevant test with one extra assertion, trace one input by hand. Time-box hard.
3. **Resolve to one of three states**:
   - **Disproved**: leave a one-line comment or commit note ("checked — handler does dedupe upstream") so future-you doesn't re-doubt.
   - **Confirmed**: now it's a known bug; use [[fix-the-problem-not-the-blame]].
   - **Still vague after 10 min**: escalate. File a ticket, ask a teammate, or hold the merge. Do not silently dismiss.
4. **Never silence a doubt without record.** The next person who runs into the same instinct deserves to find your note.

## Red flags (rationalizations to reject)

- "I'm probably just tired." — Maybe. Spend the 10 minutes anyway; it's cheap insurance.
- "I can't justify it, so it's not worth saying." — Doubts are evidence even before they're arguments.
- "Tests pass, doubt overruled." — Tests cover what was thought of. Doubts cover what wasn't.

## Composes with

- [[fix-the-problem-not-the-blame]] — once the doubt is named, treat it like any bug investigation.
- [[prove-dont-assume]] — turning a doubt into a one-line check is exactly the prove step.
- [[broken-windows]] — a doubt about code rot is itself a signal worth acting on.
