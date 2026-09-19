# V1 Input & Provenance Contract

Status: **Draft specification; not implemented or validated**  
Date: 2026-09-19

## Purpose

Define the minimum evidence required before V1 accepts chart-calculation output. This contract prevents defaults from being mistaken for provider facts. It is an engineering/data-integrity specification, not a claim that astrology predicts career outcomes.

## Required input envelope

Every calculation request and provider response must be associated with a record containing:

| Field | Requirement | Validation rule |
|---|---|---|
| `request_id` | Required opaque identifier | Non-empty; must not contain birth data |
| `birth_date` | Required local civil date | Strict ISO `YYYY-MM-DD`; reject impossible dates |
| `birth_time` | Required local wall-clock time | Strict `HH:MM[:SS]`; reject invalid values |
| `birth_time_precision` | Required enum | `exact`, `rounded`, `estimated`, or `unknown` |
| `birthplace_label` | Required user-entered place label | Preserve as supplied; do not silently geocode |
| `latitude`, `longitude` | Required for calculation | Numeric and within ±90°, ±180° respectively; retain source/provenance |
| `timezone_id` | Required IANA identifier | Must be resolvable; numeric offset alone is insufficient |
| `utc_instant` | Required derived timestamp | Must be derived from local datetime + IANA zone with ambiguity/nonexistence handling recorded |
| `timezone_resolution` | Required evidence | Record zone source and handling of DST folds/gaps; if ambiguous, ask user or block |
| `provider_name` | Required | Exact provider identifier, not inferred from response format |
| `provider_version` | Required when exposed | Record exact version; if unavailable, explicitly `unknown` |
| `ayanamsha` | Required explicit setting | Never silently default; record provider-reported value and verification status |
| `zodiac` | Required explicit setting | E.g. sidereal/tropical; never infer |
| `house_system` | Required explicit setting if houses requested | Never infer; otherwise mark not applicable |
| `node_convention` | Required if nodes used | `true`, `mean`, or `not_used` |
| `ephemeris_source` | Required | Exact source/version or `unknown`; unknown blocks accuracy certification |
| `calculated_at` | Required timestamp | UTC ISO 8601 timestamp |
| `raw_response_digest` | Required for retained provider evidence | SHA-256 of exact raw response bytes, where retention is permitted |

## Validation states

Use separate fields; do not collapse them into one generic `valid` boolean:

- `schema_valid`: required fields/types/ranges are structurally valid.
- `provenance_complete`: source and settings are explicitly evidenced.
- `calculation_reproduced`: independently reproduced under matching conventions.
- `accuracy_verified`: passed documented independent golden cases and tolerances.
- `career_rules_eligible`: only true after upstream gates and rule-specific approval.

A downstream state must never be true if its prerequisites are false or unknown.

## Fail-closed conditions

Reject or quarantine the result when:

1. Local birth time is missing or malformed.
2. The timezone is missing, unresolved, or a DST ambiguity/nonexistent time is not handled.
3. Coordinates are absent, out of range, or their source is unknown where location affects calculation.
4. Ayanamsha, zodiac, house system, or node convention is assumed rather than explicitly reported/configured.
5. Provider identity/configuration cannot be tied to the returned values.
6. Required calculation metadata is contradictory or cannot be reconciled.
7. Independent expected values are unavailable: report `not independently verified`, not `pass`.

## Evidence record

For every independent comparison, retain:

- case identifier (non-identifying)
- input envelope and its provenance
- provider name/version and explicit settings
- independent reference source/version and matching settings
- compared outputs and units
- circular-angle difference method where applicable
- predeclared tolerance and rationale
- command/tool/runtime version
- raw output digests and timestamp
- pass/fail/inconclusive outcome
- reviewer and review date

Do not retain personal birth data in public logs or issue titles. Prefer synthetic cases for repository fixtures.

## Circular longitude comparison

For angles `a` and `b` in degrees, use the shortest signed difference in `[-180, 180)`:

`delta = ((a - b + 180) % 360) - 180`

Compare `abs(delta)` to a tolerance that is specified before examining the result. A numerical match does not establish correct provenance, correct settings, or correctness of derived chart features.

## User-facing status language

- `Schema checked`: input shape/ranges passed only.
- `Configuration recorded`: explicit settings captured, not independently confirmed.
- `Compared`: outputs compared with named reference and stated tolerance.
- `Independently verified`: only when independent source, matching conventions, reproducible evidence, and acceptance criteria are all satisfied.
- `Not verified`: use whenever evidence is missing or inconclusive.

Never use “accurate chart,” “validated prediction,” or deterministic career-outcome language based solely on schema checks or same-implementation fixtures.

## Implementation checklist

- [ ] Implement strict parser and schema validation.
- [ ] Implement IANA timezone resolution with DST ambiguity/nonexistence detection.
- [ ] Require explicit provider settings; remove implicit convention defaults from certification path.
- [ ] Add unit tests for missing, contradictory, out-of-range, and ambiguous inputs.
- [ ] Add independent golden fixtures with documented provenance.
- [ ] Add status dependency enforcement.
- [ ] Add privacy review for birth-data handling and logs.
- [ ] Run tests and publish reproducible outputs before marking implemented.
