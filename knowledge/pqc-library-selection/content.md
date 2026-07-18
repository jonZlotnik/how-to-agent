# PQC Library Selection

Several post-quantum libraries are now production-grade, but "ships an ML-KEM function" is not the bar. A production-ready implementation tracks the finalised standards, has constant-time guarantees with evidence, stays actively maintained, is independently auditable, fits your runtime, and passes a conformance battery in CI. Pick for maintenance, audit posture, and ecosystem fit — not for the longest feature list.

## When to use

- Selecting a PQC library or platform crypto provider for a deployment
- Judging whether a given implementation is production-ready
- A reference implementation is being considered for production use
- Reconciling library choice with conformance testing ([[pqc-conformance-testing]])

## Protocol

1. **Apply the six readiness criteria.** Implements finalised FIPS 203/204(/205); constant-time with evidence (`ctgrind`/`TIMECOP`/`dudect`, ideally formal verification); actively maintained with recent releases; open and auditable; supported in your language/runtime/FFI; passes a conformance battery, reproducible in CI.
2. **Start from a conformance-clean shortlist.** Implementations that passed Symbolic Software's Crucible battery cleanly: AWS-LC, Cloudflare CIRCL, the Go standard library (`crypto/mlkem`), libcrux, mlkem-native, liboqs, wolfCrypt, Trail of Bits ml-dsa, Kyber-K2SO. Verify the current run — landscapes move quickly.
3. **Prefer the platform default.** For most teams that's your language's standard library or your platform vendor's crypto (Apple CryptoKit, AWS-LC, CIRCL) — not a third-party crate with unclear maintenance.
4. **Never run the reference implementation in production.** It's written for clarity, not performance or constant-time; replace it with an audited optimised build and verify the two agree on every KAT and conformance test.
5. **Don't split implementations across environments.** Reference in tests and optimised in production is a differential-environment bug; pin one current version and test what you ship.

## Red flags (rationalizations to reject)

- "It's been stable and done for two years." — In post-quantum crypto that's probably out of date and missing a security fix; pin to current, not to what worked when you integrated.
- "The optimised build is faster, ship it." — Unaudited optimisations diverge from the reference in subtle ways (e.g. rejection-sampling order); test against KATs and the conformance battery first.
- "Reference in tests is fine." — Differential testing is good; differential *environments* are bad. Run the production implementation in tests.

## Composes with

- [[pqc-conformance-testing]] — the battery that produces the "conformance-clean" judgement.
- [[pqc-bugs-operational]] — reference-in-production, stale dependencies, and FFI mistakes are library-layer findings.
- [[reversible-decisions]] — a library swap is reversible; an unaudited custom optimisation baked into your protocol is less so.
