# Rule of Composition

Programs should be expected to feed each other. A tool that only talks to humans, or only emits a private binary format, or only runs as a daemon, has cut itself off from the rest of the system. Design as if your output is someone else's input — because eventually it will be.

## When to use

- Designing a CLI, library function, or service endpoint
- Tempted to "just put a UI on it" instead of exposing a callable interface
- The natural way to use your tool involves copy-pasting from a window into another window
- A future "let me automate this" requires reverse-engineering screens or scraping logs

## Protocol

1. **Default to stdin → process → stdout.** Streams of text first; objects in a stable serialization second; interactive UI last. The UI can wrap a composable core; the inverse is painful.
2. **Take the data, not the path.** A function that accepts a path or filename refuses to be composed; one that accepts an open stream or a value composes freely. Make I/O the caller's problem.
3. **Don't reach for state.** Reading globals, environment, or shared singletons kills composition. State should arrive as arguments.
4. **Emit one record per line, or a stable structured format.** Pipelines work on streams. Whatever you emit, downstream tools should be able to filter, count, and slice without parsing your prose.
5. **Document what you read and what you emit** as a contract, including how you behave on EOF, partial input, and empty input.

## Red flags (rationalizations to reject)

- "Nobody's going to script this." — Six months later, you will.
- "It's easier to do it all in one program." — Easier to write, harder to extend. The monolith resists the next requirement.
- "We need a UI." — You need a composable core *and* a UI. The UI is one consumer, not the only one.

## Composes with

- [[rule-of-textuality]] — composability is multiplied by streams that humans and tools can both read.
- [[rule-of-silence]] — pipeline-friendly output means saying nothing routine and letting useful records flow through.
- [[rule-of-separation]] — the engine is what you compose; the UI is one of many possible callers.
- [[orthogonality-check]] — composable tools are by construction more orthogonal.
