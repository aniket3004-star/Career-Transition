# V1 Next Execution Plan

Date: 2026-09-19

## Purpose

Convert the current artifact-review findings into a practical, gated sequence of work. This is a newly created execution plan; it is **not** a reconstruction of the original numbered task register (#1–#45), which has not yet been recovered from an authoritative source.

## Current verified checkpoint

- The v33 packaged synthetic regression script was run successfully: 20 cases, 0 failures.
- The fixtures and runner use the same Swiss Ephemeris implementation/conventions, so this is a self-consistency check, not independent astronomical validation.
- Existing review documents identify unresolved provider, timezone, Dasha, transit, career-rule, and deployment validation.
- No independent agent processes are running. Work is being coordinated and executed sequentially in this environment.

## Workstreams and gates

### Gate 0 — Source-of-truth recovery

**Objective:** Recover the exact original task register #1–#45 and preserve its wording/status.

**Acceptance criteria:**
- Locate an authoritative original file/message/export.
- Transcribe all 45 tasks verbatim, retaining original numbering and any status/ownership/dependencies.
- If unavailable, explicitly mark it unrecovered; do not synthesize substitute tasks and call them original.

**Status:** BLOCKED — authoritative register not found in the material reviewed so far.

### Gate 1 — Artifact inventory and version reconciliation

**Objective:** Establish which ZIP is canonical for each subsystem and identify version drift.

**Actions:**
- Inventory all project ZIPs and their internal files, versions, assumptions, and entry points.
- Compare successive harness versions (v29–v33) and validator/rules packages.
- Record duplicate, superseded, or incompatible artifacts and recommend one canonical path per subsystem.

**Acceptance criteria:** A reproducible manifest maps artifact → version → purpose → dependencies → status, with no unsupported claims of execution.

**Status:** IN PROGRESS — prior reviews cover a subset; remaining package reconciliation is pending.

### Gate 2 — Calculation provenance and independent astronomy validation

**Objective:** Ensure input metadata and provider configuration are verified, not silently defaulted.

**Actions:**
- Require explicit provider identity, timezone identifier, UTC conversion evidence, ayanamsha, zodiac, house convention, ephemeris/version, and calculation timestamp where applicable.
- Reject missing or contradictory metadata rather than filling in assumptions.
- Compare representative chart outputs against at least one independent trusted reference using matching birth data and settings.
- Include boundary cases for sign/Nakshatra/pada/Ascendant and timezone/DST transitions.

**Acceptance criteria:** Independently sourced evidence is retained; tolerances and expected values are documented; all mismatches fail closed.

**Status:** BLOCKED — no independent provider comparison evidence established.

### Gate 3 — Dasha validation

**Objective:** Validate Mahadasha/Antardasha and, only after approval, Pratyantardasha timing.

**Actions:**
- Verify Moon longitude, Nakshatra, balance at birth, sequence, durations, and boundary transitions against an independent calculation/reference.
- Test date handling and avoid treating fixed-year approximations as authoritative.
- Add PD only after MD/AD validation passes.

**Acceptance criteria:** Independently checked fixtures, documented conventions, boundary tests, and explicit failure behavior.

**Status:** BLOCKED — current helper is a sanity aid, not authoritative validation.

### Gate 4 — Transit validation

**Objective:** Verify transit ingress/egress and retrograde handling before career interpretation.

**Actions:**
- Define exact conventions for Jupiter, Saturn, and Rahu/Ketu (including true/mean node choice).
- Validate ingress/egress dates against independent references across representative periods.
- Test retrograde loops, station points, sign boundaries, and timezone display.

**Acceptance criteria:** Independent reference fixtures and reproducible pass/fail tests.

**Status:** PENDING.

### Gate 5 — Career-rule evidence and backtesting

**Objective:** Keep candidate rules disabled until their evidence is adequate.

**Actions:**
- Maintain each rule as a candidate with source, rationale, scope, exclusions, expected observable, and evidence status.
- Address selection bias, coarse event dating, missing/blinded controls, and reproducibility in prior exploratory work.
- Keep D10 excluded until separately validated; prevent fast planets from changing primary classification.
- Avoid causal, deterministic, or guaranteed-career language.

**Acceptance criteria:** Pre-registered criteria, independent/blinded evaluation where feasible, reproducible analysis, and explicit promotion approval. No rule is promoted solely from exploratory association.

**Status:** BLOCKED — no primary rule promoted.

### Gate 6 — Product, privacy, and release readiness

**Objective:** Ensure user control, privacy, explainability, and safe release.

**Actions:**
- Confirm in-memory-by-default behavior and opt-in persistence design.
- Document deletion/export behavior, data minimization, and handling of birth data.
- Generate explanations only from validated calculation/rule outputs; show uncertainty and non-deterministic framing.
- Add integration tests, deployment checks, and human release approval.

**Acceptance criteria:** Privacy and security review, end-to-end tests, documented limitations, and explicit human approval before public release.

**Status:** PENDING; production readiness not established.

## Operating roles (workflow roles, not autonomous agents)

- **Orchestrator:** maintain dependency order, task log, and evidence links.
- **Astronomy/Dasha reviewer:** verify calculation conventions and reference fixtures.
- **Rules/evidence reviewer:** scrutinize candidate rule definitions and validation design.
- **QA/auditor:** independently inspect evidence and prevent unsupported promotion.
- **Product/privacy reviewer:** review consent, data handling, user messaging, and release gates.

These are responsibility labels for sequential work in this chat/repository. They do not represent persistent or independently running agents.

## Immediate next action

Complete Gate 1 by reconciling the remaining ZIPs and recording the canonical artifact map. In parallel, continue searching for the authoritative #1–#45 register; do not block useful artifact reconciliation on that recovery.
