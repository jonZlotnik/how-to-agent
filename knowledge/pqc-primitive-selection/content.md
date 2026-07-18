# PQC Primitive Selection

NIST standardised one KEM (ML-KEM) and two signature schemes (ML-DSA, SLH-DSA). For the KEM the only question is the parameter set; for signatures you also choose between a small, fast lattice scheme and a large, conservative hash-based one. Pick the security category your regime demands, then make sure the symmetric primitives in the same data path match it — a post-quantum KEM in front of a 128-bit KDF is only as strong as the KDF.

## When to use

- Selecting ML-KEM / ML-DSA / SLH-DSA parameters for a new or migrating system
- Deciding whether a signature use case justifies SLH-DSA's size cost
- A protocol's symmetric or KDF layer is being chosen alongside the PQ handshake
- Reconciling a parameter choice against a compliance regime ([[pqc-regulatory-compliance]])

## The decision

| Need | Civilian default | CNSA 2.0 | Notes |
|---|---|---|---|
| KEM | ML-KEM-768 (cat 3, pk 1184 B) | ML-KEM-1024 (cat 5) | Avoid ML-KEM-512 unless size/compute-bound |
| Signature | ML-DSA-65 (cat 3, sig 3309 B) | ML-DSA-87 (cat 5) | Fast; ~50× larger than Ed25519 |
| Conservative sig | SLH-DSA (sig ~7.8–30 KB) | SLH-DSA | Only when you need hash-only assumptions |

## Protocol

1. **Choose the KEM by category.** ML-KEM-768 for almost every civilian system (AES-192 level, industry consensus, what Cloudflare/Google/AWS settled on); ML-KEM-1024 for CNSA. Avoid ML-KEM-512 unless an extreme size or compute constraint forces it.
2. **Default signatures to ML-DSA-65** (ML-DSA-87 for CNSA) — TLS certs, tokens, attestations, ordinary code signing.
3. **Reach for SLH-DSA only with a specific reason** — long-lived root keys or firmware where you'll pay 5–10× the signature size for hash-only security. Wait on FN-DSA until it finalises and its floating-point pitfalls settle.
4. **Match the symmetric suite to the category.** AES-256, SHA-256/384/512, ChaCha20-Poly1305, HKDF/HMAC are all post-quantum acceptable — migrate them too, don't leave AES-128 beside ML-KEM-1024.
5. **Don't undo the lift in the KDF.** Deriving a 128-bit session key from an ML-KEM-768 handshake throws away the security category; match KDF output and AEAD key length to your stated level.

## Red flags (rationalizations to reject)

- "ML-KEM-512 saves bytes." — The bytes saved aren't worth the thinner margin against future cryptanalysis.
- "We upgraded the KEM, the rest is fine." — A correctly-chosen ML-KEM beside AES-128 or a 128-bit KDF is only as strong as the weakest link.
- "SLH-DSA is more conservative, so use it everywhere." — Its signatures are 5–10× larger; pay that only where the threat model needs it.

## Composes with

- [[pqc-regulatory-compliance]] — your regime constrains which categories are legal.
- [[pqc-hybrid-construction]] — these primitives are the post-quantum half of any hybrid.
- [[reversible-decisions]] — parameter sets are easy to revise; the protocol framing around them is not.
