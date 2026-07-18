---
name: pqc-bugs-protocol
description: "Use when auditing how a post-quantum primitive is integrated into a protocol — hybrid downgrade, transcript binding, serialisation length-confusion, and post-quantum 'support' that doesn't reach the data path."
---

<!-- DO NOT EDIT — generated from knowledge/ by scripts/sync_knowledge.py -->

# PQC Bugs: Protocol Integration

A correct primitive can still be broken by how it's wired into a protocol. These four bug classes are the integration-layer recall list: a hybrid that collapses to its weaker half, a combiner that doesn't bind its inputs, length fields sized for classical primitives, and "post-quantum support" that never touches the data path. Recognise the shape; don't assume your instance is the safe one.

## When to use

- Reviewing how ML-KEM/ML-DSA is integrated into a handshake or messaging protocol
- Auditing a hybrid combiner or negotiation path
- Checking serialisation and length handling around post-quantum-sized values
- Validating a "post-quantum ready" claim against the actual data path

## The bug classes

1. **Hybrid downgrade.** A hybrid reduces to its weaker component if any of: the negotiation can be tampered with, the post-quantum half can be selectively failed, or the combiner XORs/discards rather than KDFs. Fail closed on post-quantum-half failure; don't keep a fallback path that re-introduces the downgrade.
2. **Transcript-binding omissions.** A hybrid KEM combined via a KDF *must* bind both public keys and both ciphertexts into the KDF input. Deriving only from the two shared secrets is vulnerable to maliciously chosen public keys. The X-Wing combiner binds correctly; rolled-your-own combiners often don't. See [[pqc-hybrid-construction]].
3. **Length-confusion in serialisation.** Post-quantum values have larger, more varied byte lengths than classical ones. Length fields hard-coded for X25519's 32 bytes silently truncate ML-KEM-768's 1184-byte public key. The same buffers make FFI-boundary length mismatches more likely.
4. **Compliance theatre.** The codebase contains a post-quantum implementation; the data path still uses classical primitives end-to-end. It shows up in marketing claims, compliance checklists, and self-attestation more than in reviewed designs. The fix: validate the data path under live traffic, not the dependency graph.

## Red flags (rationalizations to reject)

- "The hybrid handshake completes, so it's hybrid." — It may have been steered or selectively failed onto the classical half; verify the post-quantum secret actually contributes.
- "We derive the session key from both secrets." — Without binding both public keys and ciphertexts, a malicious peer can exploit it. Bind the transcript.
- "We ship an ML-KEM implementation." — Shipping it isn't using it; trace the live data path before claiming support.

## Composes with

- [[pqc-hybrid-construction]] — the correct combiner and downgrade resistance these bugs violate.
- [[design-by-contract]] — combiner binding inputs and length fields are contracts that, unwritten, fail at the seam.
- [[pqc-bugs-primitive]] — the primitive-level companion to these integration findings.
- [[pqc-tls-key-exchange]] — supported-groups stripping is the concrete TLS instance of bug class 1.
