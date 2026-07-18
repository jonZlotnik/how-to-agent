---
name: tracer-bullet
description: "Use when starting a new feature, integration, or system with unknown end-to-end behavior — before writing the full implementation. Also use when crossing module/service boundaries for the first time."
---

<!-- DO NOT EDIT — generated from knowledge/ by scripts/sync_knowledge.py -->

# Tracer Bullet

Build the thinnest possible end-to-end path through the system *first*. Hard-code the middle, fake the edges if you must, but make a real input produce a real output along the actual code path. Then flesh it out under tests. Unlike a prototype, the tracer stays — it becomes the skeleton.

## When to use

- The work spans multiple components (UI → API → DB → external service) and you're unsure how they connect
- You're tempted to "build the data layer first, then the API layer, then the UI" in long phases
- You don't know whether the desired interaction is even possible
- Stakeholders need to *see* something working to give useful feedback

## Protocol

1. **Pick a single concrete path** — one user, one input, one output. No branching, no edge cases.
2. **Stub everything that isn't on that path.** Use hard-coded values, panic-on-call placeholders, and TODO markers. The skeleton must compile and run.
3. **Wire the path end-to-end** before adding any depth at any layer. Real input enters the real first stage; real output leaves the real last stage.
4. **Instrument it.** A log line or assertion at each handoff makes future debugging cheap.
5. **Demo or test the path** to confirm the architecture works as conceived. Only then add breadth (more cases) and depth (more logic per stage).

## Distinguish from [[prototype-to-learn]]

- Tracer code is **kept** and grown. Write it production-style: real names, real interfaces, real error types.
- A prototype is **thrown away**. It answers one question and dies.
- If you find yourself promising "I'll clean it up later" — that's a prototype masquerading as a tracer. Pick one.

## Red flags (rationalizations to reject)

- "I'll just build the backend first, then wire it up." — That's a phase-gate plan. You won't know it works until the last day.
- "It's faster to skip the boring layers." — Until the layers don't fit together at the end.
- "There's no point in stubs, I'll do it for real." — You'll be debugging integration and business logic at the same time.

## Composes with

- [[dig-for-requirements]] — clarify what the bullet should *hit* before firing.
- [[prototype-to-learn]] — when even the path is unknown, prototype first, then tracer-bullet the chosen path.
- [[design-by-contract]] — define the handoff contracts before stubbing the layers.
