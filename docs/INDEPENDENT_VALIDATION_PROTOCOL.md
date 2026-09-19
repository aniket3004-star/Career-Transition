# Independent Validation Protocol — Career Transition Astrology V1

**Status:** Protocol only; no independent validation results are implied.

## Purpose
Define evidence required before V1 may describe chart, dasha, transit, or career-timing outputs as independently verified. Schema validation and internally consistent fixtures are not independent accuracy evidence.

## 1. Freeze the test inputs
For every test case, retain:
- Stable case ID and consent/authority to use the birth data.
- Original date, local time, IANA timezone, location coordinates, and source record.
- Any uncertainty in recorded birth time, historical timezone, or location.
- Provider name/version, ephemeris/version, ayanamsha, zodiac, house system, and calculation timestamp.
- Exact request and raw provider response, stored with appropriate access controls.

Do not silently normalize missing settings. Missing or unverified provenance blocks comparison.

## 2. Independent astronomical reference
Select a reference implementation that is not the same provider/library used by the system under test. Record its version, ephemeris files, time-scale handling, coordinate conventions, and configuration. Use published test vectors where available, and include independently calculated cases spanning:
- Different centuries/timezones and both hemispheres.
- Boundary cases near sign/house transitions and retrograde stations.
- Leap days, historical timezone changes, and DST gaps/repeats.
- Several planets and lunar positions, not only one favorable example.

Compare raw longitudes/latitudes and derived placements using predeclared tolerances. Explain any convention differences rather than adjusting tolerances after seeing results.

## 3. Dasha verification
For each case, independently calculate the Moon's sidereal longitude and nakshatra, the remaining balance of the starting mahadasha, and the full MD/AD/PD boundaries. Check:
- Correct nakshatra ruler and proportional balance at birth.
- Continuous, non-overlapping intervals with documented boundary convention.
- Correct sequence and duration for every level exposed by V1.
- Date/timezone conversion and exact-boundary behavior.

A validator that checks only sequence shape or durations is not proof that birth-based balance is correct.

## 4. Provider parity and provenance
Use a golden corpus with independently sourced expected outputs. Store raw output and normalized output separately. Require explicit configuration evidence; an attestation flag alone is not proof. Fail closed on missing provider version, ephemeris, ayanamsha, zodiac, house system, time standard, or location convention.

## 5. Career-rule evidence
Keep interpretive rules separate from astronomical calculations. Before testing, preregister:
- Rule definitions and direction of each claimed association.
- Outcome definition, population, time window, exclusions, and missing-data policy.
- Baseline, comparison method, multiple-testing handling, and success criteria.
- Holdout or prospective validation plan.

Report denominators, uncertainty, null findings, and selection effects. Exploratory anecdotes or a small selected set cannot establish predictive validity. Do not claim that astrology determines employment outcomes.

## 6. Release gates
A gate is passed only with linked, reproducible evidence:
1. Input/provenance contract tests pass in CI.
2. Independent astronomical comparison completed with discrepancies documented.
3. Birth-based MD/AD/PD calculation independently checked.
4. Provider configurations and raw evidence retained for each evaluated case.
5. Career rules independently evaluated under a preregistered protocol—or clearly labeled exploratory and excluded from predictive claims.
6. Privacy, consent, retention, and user-facing uncertainty disclosures reviewed.

## 7. Required report format
For each gate: `NOT STARTED`, `IN PROGRESS`, `PASS`, `FAIL`, or `BLOCKED`; evidence links; sample size; method; known limitations; reviewer; date. Never convert missing evidence into a pass.

## Current limitation
This document specifies a process. It does not provide an independent reference corpus, execute calculations, validate any provider, or establish career-prediction accuracy.