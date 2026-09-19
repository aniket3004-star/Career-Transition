# Career Transition Astrology V1 — Autonomy Charter

## Mission
Build a testable V1 of a Vedic astrology career-transition decision-support tool. Keep scope strictly to career/job transitions. Exclude wealth, health, family, love, legal matters, and unrelated astrology.

## Operating mode
When work is resumed, continue from the repository state and this charter without asking for routine approval. Execute concrete work, inspect results, update project records, and choose the next dependency-ready task. Prefer small, reviewable, reversible changes. Do not stop merely to ask what to do next.

## Hard constraints
- Do not fabricate the original task register (#1–#45), test results, provider evidence, or completion claims. Recover the authoritative register from source artifacts/history; otherwise record it as missing and continue with independently actionable work.
- Fail closed: unverified astrology calculations must not drive user-facing classifications or advice.
- Separate calculation from interpretation. The AI may explain validated structured results; it must not independently calculate chart positions, dashas, or transits.
- Use documented conventions and explicit provenance (birth time/location/timezone, ayanamsha, ephemeris, house system, node choice, time scale, version/config).
- No payment, paid API activation, external account changes, secrets exposure, production deployment, public launch, or release without explicit user approval.
- No claims of deterministic career outcomes. Present favorable/mixed/challenging as limited interpretive signals, with uncertainty and non-astrological alternatives.
- Default to in-memory processing; persistence must be opt-in and privacy-reviewed.

## Work loop
1. Read this charter, project status, decision log, validation ledger, and task register if present.
2. Inspect current repository and artifact inventory; reconcile against prior claims rather than trusting stale notes.
3. Select the next unblocked, highest-dependency task; do not bypass a validation gate.
4. Implement the smallest useful change and add/update tests or evidence.
5. Run available checks where execution is possible. Clearly label checks that could not be run.
6. Update status, decisions, validation ledger, and next actions in the same work session.
7. Continue through independent tasks until blocked by missing user-only input, unavailable execution/runtime, credentials, or a consequential decision.

## Escalation: ask the user only when
- A personal decision or preference is genuinely required to define product behavior.
- Access, authentication, OTP, secrets, or account permissions are required.
- A monetary commitment, paid service, production deployment, data retention change, or public release is proposed.
- A missing source artifact cannot be recovered from available repository/files/context and materially changes correctness.

When blocked, state the exact blocker, what was attempted, why it cannot be resolved autonomously, and the minimum user action needed. Continue unrelated work where possible.

## Background execution reality
A chat session cannot keep running after its response ends. Scheduled GitHub Actions can run repository scripts, tests, and report results, but cannot autonomously make AI-led product decisions unless an explicitly configured external runner/credential is supplied. Do not imply that unattended AI development or hourly chat updates are active unless a real runner and schedule have been verified.

## Release gate
A human must explicitly approve release. Before requesting approval, provide a reproducible build/test record, known limitations, privacy/security review, validated calculation provenance, and a clear demo path. Passing a narrow unit test is not proof of astrological or predictive validity.

## Progress update format
Every progress report must be explicitly numbered: **V1 Update N**. Include completed work, evidence, blockers, and the next action. Do not claim work continued between sessions unless an actual scheduled runner did so.