---
name: pqc-bugs-operational
description: "Use when auditing the operational and dependency side of a post-quantum deployment — keygen entropy, key leakage, rotation amnesia, prekey replay, reference-implementation-in-production, stale libraries, FFI boundaries."
---

<!-- DO NOT EDIT — generated from knowledge/ by scripts/sync_knowledge.py -->

# PQC Bugs: Operational and Dependency

The migration can be correct in the primitive and the protocol and still fail in operations and key management. These seven bug classes are the recall list for the layer where keys are generated, stored, rotated, and linked across an FFI boundary — and where a successfully migrated system quietly undoes its own migration. Recognise the pattern; either eliminate it or justify your instance in writing.

## When to use

- Auditing key generation, storage, rotation, or escrow in a post-quantum deployment
- Reviewing prekey handling in PQ messaging ([[pqc-messaging-migration]])
- Checking which implementation and version actually ship in production
- Reviewing FFI boundaries around post-quantum buffers

## The bug classes

1. **Insufficient entropy at keygen.** A keygen drawing from a non-cryptographic, unseeded, or deterministic source. Lattice schemes have specific entropy requirements — check the RNG path is actually exercised, not assumed.
2. **Leaking long-term keys via test endpoints.** Debug interfaces and "compatibility" modes that expose private key material under conditions the threat model ignores but that are reachable in production.
3. **Key-rotation amnesia.** A system rotates its post-quantum keys, but the backup/archive/escrow mechanism keeps encrypting to the original, now-deprecated key. Three years later the migration is materially undone.
4. **Prekey replay in PQ messaging.** One-shot post-quantum prekeys distributed without a server-side mechanism to retire them on use; an attacker who reads the prekey response replays the encapsulation and defeats forward secrecy. Remove a prekey atomically when consumed.
5. **Reference implementation in production.** The reference build is for clarity, not performance or constant-time. Replacing it with an audited optimised one — and verifying they agree on every KAT and conformance test — is a common omission.
6. **Out-of-date library dependency.** A library that shipped post-quantum support six months ago may have shipped a security fix four months ago. Pin to a current version, not the one that worked when you integrated.
7. **FFI boundary mistakes.** Foreign-function-interface boundaries lose buffer-length, ownership, and zeroisation invariants; post-quantum primitives have larger buffers, so the chance of a length mismatch there is correspondingly larger.

## Red flags (rationalizations to reject)

- "The keys rotated, so we're migrated." — Check escrow and backups didn't keep encrypting to the old key.
- "That endpoint is test-only." — If it's reachable in production, it's a production key leak.
- "The library worked when we shipped." — It may be missing a since-released security fix; pin to current.

## Composes with

- [[pqc-messaging-migration]] — prekey replay and rotation amnesia are the messaging-specific instances.
- [[pqc-library-selection]] — reference-in-production, stale versions, and FFI fit are library-choice consequences.
- [[broken-windows]] — a stale dependency or a known test-endpoint leak left unfixed signals the rest is tolerated too.
- [[pqc-bugs-primitive]] — the primitive-level companion gallery.
