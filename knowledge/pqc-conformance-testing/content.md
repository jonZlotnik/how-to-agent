# PQC Conformance Testing

Even a correct-looking post-quantum implementation can fail in bug-class patterns that recur across audits — and passing NIST's Known Answer Tests does not catch them, because KATs only exercise correct-input round-trips. A conformance harness like Symbolic Software's Crucible drives malformed, out-of-bounds, and edge-case inputs against curated bug-class categories. It detects known bugs; it does not certify your system or replace an audit.

## When to use

- Integrating a new PQC library and establishing a baseline
- Adding crypto-conformance gates to CI
- Preparing a release artefact for sign-off
- Deciding whether KATs or a passing handshake are sufficient evidence

## Protocol

1. **Run conformance at three points.** When you first integrate a library (baseline — where the surprises happen); in CI on every commit touching the crypto dependency or harness; and once per release against the *release artefact*, not a dev build.
2. **Wire the harness as a thin shim.** Crucible speaks line-delimited JSON over stdin/stdout: accept a request (`keygen`/`encaps`/`decaps`/`sign`/`verify` + parameter set + input bytes), invoke the implementation, return one JSON line. The cross-language friction stays in that shim; example harnesses exist for Rust, Go, and C.
3. **Cover the bug-class categories, not just round-trips.** ML-KEM (78 tests / 6 categories): compression arithmetic, NTT correctness, coefficient bounds, decapsulation robustness, serialisation, rejection sampling. ML-DSA (51 tests / 6 categories): norm checks, arithmetic, signing internals, verification edge cases, serialisation, constant-time.
4. **Layer the complementary techniques.** NIST KATs catch encoding and gross numeric bugs (correct input only); fuzzing hits deserialisation paths; `ctgrind`/`TIMECOP`/`dudect` find timing-distinguishable code at the binary level; formal verification can remove whole bug classes at real cost.
5. **Feed findings back.** A bug the battery missed should become a new test — the harness sharpens over time.

## Red flags (rationalizations to reject)

- "It passes the NIST KATs." — KATs exercise correct-input round-trips only; implementations pass every KAT and still accept malformed ciphertexts a stricter peer rejects.
- "Conformance-clean means the system is secure." — It certifies primitive correctness, not your protocol integration; a correct ML-KEM is still misusable upstream.
- "The source looks constant-time." — The optimiser can compile it to branchy code; verify at the binary level, not the source.

## Composes with

- [[pqc-library-selection]] — conformance is the battery behind a "conformance-clean" shortlist.
- [[prove-dont-assume]] — a passing battery is evidence; "it looks correct" is not.
- [[pqc-bugs-primitive]] — the primitive-level bug classes these categories are built to catch.
- [[mpc-audit]] — conformance complements, never replaces, a design-and-integration audit.
