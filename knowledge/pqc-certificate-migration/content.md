# PQC Certificate Migration

Certificate-signature migration is the hard half of TLS: authentication touches the whole chain — leaf, intermediates, roots in client trust stores, and every layer that parses and presents signatures — and no single deployment can drive it unilaterally. It is a coordinated, multi-year, three-phase programme, and unlike key exchange there is no Harvest-Now-Decrypt-Later pressure forcing it early.

## When to use

- Planning the certificate/PKI side of a TLS migration
- Estimating handshake-size and performance impact from post-quantum signatures
- Operating an internal PKI you control end-to-end (mTLS, private CAs)
- Tempted to issue or accept post-quantum certificate chains now

## Protocol

1. **Stage the migration in three phases.** Current: post-quantum *key exchange* with classical certificate signatures (HNDL addressed, chain still classical). Next: post-quantum or hybrid certificate signatures, likely dual-algorithm certs for a transition window. Last: deprecate classical signatures.
2. **Don't issue or accept post-quantum chains until the whole path supports them** — your trust store, your TLS library, and your peers' implementations. Track the IETF LAMPS/TLS groups, CA/Browser Forum baseline, and the major root programmes.
3. **Move faster only where you control both ends.** Internal services and mTLS within your own fleet can adopt pure ML-DSA-65 now; there's no HNDL threat to signatures, so a hybrid signature scheme here is the wrong cost/benefit.
4. **Budget for size.** ML-DSA-65 signatures are ~50× larger than Ed25519. A full post-quantum chain (leaf + intermediate + OCSP staple) can exceed TCP's initial window — test under realistic loss, especially on mobile, embedded, and initial page load.
5. **Plan for Certificate Transparency scale.** Both certificates and their SCTs grow; CT log operators and relying parties must handle larger SCT lists.

## Red flags (rationalizations to reject)

- "Migrate certificates at the same time as key exchange." — Authentication is the multi-year project; bundling it stalls the easy, high-value KEX change.
- "Use hybrid signatures on our TLS certs to be safe." — No HNDL threat exists for signatures verified at handshake time; the dual-signature complexity isn't justified.
- "Our handshake tested fine." — In isolation. The OCSP-plus-full-chain case is where the buffer/fragmentation failure actually appears.

## Composes with

- [[pqc-tls-key-exchange]] — the easy half you should ship first and not block on this.
- [[pqc-primitive-selection]] — ML-DSA-65/87 vs. SLH-DSA is the certificate-signature choice.
- [[reversible-decisions]] — phased dual-algorithm certs keep the transition reversible.
