---
name: pqc-tls-key-exchange
description: "Use when enabling post-quantum key exchange in TLS 1.3 (or QUIC, DTLS, SSH), when ordering named groups, or when defending a hybrid handshake against downgrade stripping."
---

<!-- DO NOT EDIT — generated from knowledge/ by scripts/sync_knowledge.py -->

# PQC TLS Key Exchange

Enabling the `X25519MLKEM768` named group in TLS 1.3 is the single change with the highest Harvest-Now-Decrypt-Later mitigation per unit of effort, and it is already in production at Cloudflare, Google, AWS, Microsoft, and Apple. The handshake key exchange is the easy half of TLS migration; the work is enabling it everywhere, ordering it first, and making sure a man-in-the-middle can't strip it back to classical.

## When to use

- Turning on post-quantum key exchange for TLS-terminating services or clients
- Ordering supported-groups / named-group preferences
- Migrating QUIC, DTLS, or SSH key exchange
- Reviewing whether a hybrid handshake can be downgraded

## Protocol

1. **Enable `X25519MLKEM768` alongside `x25519` on both ends.** Order the hybrid first so it's preferred when both peers support it; keep `x25519` for backward compatibility with peers that don't.
2. **Treat downgrade as a policy problem, not just a transcript one.** TLS 1.3's transcript hash detects tampering only *after* negotiation; a peer steered into a weaker group can't tell from the transcript alone. For peers known to support the hybrid, configure a hard-fail "require" policy, not merely "prefer".
3. **Carry the same handshake to other transports.** QUIC reuses the TLS 1.3 handshake (mind the 1,200-byte initial-packet limit); DTLS 1.3 likewise (watch fragmentation). For SSH, OpenSSH 9.0+ offers `sntrup761x25519-sha512@openssh.com` — a config change today.
4. **Reject custom fallback paths.** A separate "compatibility" message that drops to classical mid-handshake without re-deriving session state is an attacker-inducible downgrade. Standard TLS 1.3 doesn't have this; non-standard protocols sometimes do.
5. **Defer certificate-signature migration.** It's a separate, longer programme — see [[pqc-certificate-migration]]. Don't let it block the key-exchange change.

## Red flags (rationalizations to reject)

- "The transcript hash protects us from downgrade." — Only post-negotiation; cleartext supported-groups stripping happens before the hash binds anything. Require, don't prefer.
- "Preferring the hybrid is enough." — A MITM removes it from the ClientHello and both sides happily complete on classical. Policy must fail closed.
- "We added a fallback message for robustness." — That fallback is the downgrade. Fail closed on post-quantum-handshake failure instead.

## Composes with

- [[pqc-hybrid-construction]] — the named group is the combiner you're deploying.
- [[pqc-certificate-migration]] — the harder, slower other half of TLS migration.
- [[pqc-rollout-monitoring]] — negotiation rate is how you confirm the group is actually being used.
- [[pqc-bugs-protocol]] — supported-groups stripping is the concrete instance of hybrid downgrade.
