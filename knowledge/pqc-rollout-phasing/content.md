# PQC Rollout Phasing

Treat a post-quantum migration as a normal production rollout: feature-flag the library, dark-launch to a sliver of traffic, ramp by percentage, and keep an explicit rollback path you have actually exercised. Even a sophisticated, well-instrumented operator treats this as a multi-year programme — the discipline that protects you is staging the change and defining, in advance, the thresholds at which you roll back.

## When to use

- Planning the deployment of a PQC change to production
- Defining rollback policy and thresholds before a ramp
- A change is heading to 100% without staging
- Operational surprises (middleboxes, OCSP, races) are appearing during rollout

## Protocol

1. **Stage the rollout in five phases.** (1) Library upgrade behind a feature flag, hybrid built-in but off, verify no regression. (2) Dark launch to 1–5% of traffic, observe. (3) Ramp 5 → 25 → 50 → 100%, watching the indicators at each step ([[pqc-rollout-monitoring]]). (4) Default-on, classical fallback retained for non-supporting peers. (5) Harden — fail closed for peers known to support the hybrid.
2. **Have a rollback path before you start, and rehearse it.** For a hybrid KEM, rollback is re-disabling the group in the supported-groups list — classical key exchange keeps working. A rollback you've never executed is not a rollback.
3. **Write explicit rollback thresholds.** e.g. "if hybrid handshake failure rate exceeds 0.5% over a 30-minute window, automatically halve the hybrid percentage." Ad-hoc decisions during an incident are how you end up rolling forward when you should have rolled back.
4. **Test through every layer of the real path.** Corporate proxies, load balancers, DPI boxes, and TLS-terminating CDNs can silently strip a hybrid group or reject larger ClientHellos; a single middlebox can block a rollout for weeks.
5. **Watch for second-order size surprises.** A larger handshake plus OCSP stapling can cross a buffer or fragmentation threshold the TLS change passed in isolation; rollouts also have data-race surfaces (e.g. a racy prekey-pool refresh) that pure protocol designs don't — test under load.

## Red flags (rationalizations to reject)

- "The hybrid doesn't work — negotiation is at zero." — Usually asymmetric upgrade: servers upgraded, clients not. The hybrid is fine; instrument both sides.
- "We'll roll back if something goes wrong." — Without a rehearsed path and a numeric threshold, you'll rationalise rolling forward through the incident.
- "It passed staging, push to 100%." — Middleboxes and OCSP-inflated chains fail only on the real production path under real load.

## Composes with

- [[pqc-rollout-monitoring]] — the indicators whose thresholds trigger the rollback defined here.
- [[tracer-bullet]] — dark launch is a tracer through the full production path before committing.
- [[reversible-decisions]] — a phased ramp with a tested rollback keeps every step reversible.
