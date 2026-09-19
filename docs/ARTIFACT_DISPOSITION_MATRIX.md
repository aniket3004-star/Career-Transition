# Artifact Disposition Matrix

Date: 2026-09-19

## Scope and evidence standard

This matrix consolidates artifact names and findings already recorded in the project audit/review notes. It is a **provisional disposition**, not a complete fresh inspection of every ZIP's internal files. “Reviewed” means described in the existing audit record; it does not mean tests were run. The original task register #1–#45 remains unrecovered.

## Disposition

| Artifact | Known purpose / evidence | Disposition | Integration decision |
|---|---|---|---|
| `career-transition-v1-canonical-engine.zip` | Provider-neutral schema and calculation/validation flow described in engine review | Candidate foundation; not certified | Preserve as design/reference pending full source and interface review |
| `career-transition-v1-career-rules-v35.zip` | Seven candidate rule families, all blocked; D10 excluded; fast planets cannot alter primary classification | Research registry only | Do not enable rules in user-facing classification |
| `career-transition-v1-backtest-v36.zip` | Provenance-first evidence/promotion gates | Evidence workflow | Retain as methodology; independently inspect/reproduce before relying on outputs |
| `career-transition-v1-critical-audit-v37.zip` | Exploratory 5/5 association reported, with selection-bias/coarse-date/no-blinded-control caveats; no rule promoted | Audit evidence, not validation | Preserve caveats; do not treat 5/5 as proof |
| `career-transition-v1-validation-harness.zip` | Includes Swiss-reference layer, validator, Dasha helper, Supabase scaffold; fixed fixture path/timestamp and approximate Dasha concerns noted | Candidate QA scaffold | Do not treat as production-ready; review source, dependencies, and test portability |
| `career-transition-v1-validation-harness-v29.zip` through `v32.zip` | Earlier harness versions listed in project inventory; detailed version-by-version diff not established here | Historical candidates | Compare against v33 before selecting or discarding |
| `career-transition-v1-validation-harness-v33.zip` | Regression script actually executed: 20 synthetic cases, 0 failures; same Swiss Ephemeris conventions used by fixture generator and runner | Latest confirmed synthetic regression checkpoint | Keep as narrow regression evidence only; not independent astronomy validation |
| `career-transition-v1-dasha-validator.zip` | Sequence/continuity and AD checks; reported gaps include birthDate not used, no full birth-balance/PD validation | Incomplete validator candidate | Fix and independently validate before relying on Dasha output |
| `career-transition-v1-provider-pack.zip` | Adapter skeletons; normalizer reportedly assigns defaults rather than verifying provider configuration; no live accuracy pass | Integration prototype | Do not certify provider data; require explicit verified metadata and live evidence |
| `career-transition-v1-reference-connector.zip` | External Swiss Ephemeris API connector proposal; output remains `validated:false`; endpoint not independently verified | Unverified connector proposal | Do not call or rely on endpoint until documentation, access, licensing, and behavior are verified |
| `career-transition-v1-cloud-runner-v40.zip` | Provider-capture runbook; explicitly no live provider call or accuracy pass | Runbook | Use only to guide evidence collection |
| `career-transition-v1-evidence-capture-v41.zip` | Browser form captures request/response/reference/comparison; syntax checks only | Evidence-capture utility | Useful for recordkeeping, not calculation or certification |
| `career-transition-v1-payload-validator-v44.zip` | Manual numeric longitude comparison; 1-arcsec default provisional; numeric pass does not prove provenance/configuration/derivations | Narrow comparison utility | Retain with explicit limitations; justify tolerance and verify provenance separately |
| `career-transition-v1-validator-tests-v45.zip` | Five circular-angle test cases; README states expected 5/5, but no execution recorded | Unexecuted test candidate | Run in controlled environment and capture output before marking executed |
| `career-transition-v1-offline-testpack.zip` | Narrow angular normalization and invalid-input coverage | Narrow offline tests | Keep as supplemental tests; not end-to-end coverage |
| `career-transition-v1-prototype.zip` | Prior conversation notes describe browser-testable prototype using fixture data | Fixture-based prototype | Treat as UI/prototype only until its exact ZIP contents and integration are inspected |
| `career-transition-v1-audit.zip` | Listed in Library inventory; detailed contents not established in this matrix | Unclassified | Inspect contents before disposition |
| `career-transition-v1-career-rules-v34.zip` | Listed in Library inventory; superseded-looking relative to v35, but full diff not performed | Historical candidate | Compare against v35; do not assume safe deletion |

## Cross-cutting defects / gates

1. **Configuration provenance:** do not infer that a provider used Lahiri, sidereal zodiac, Whole Sign, or another setting merely because a normalizer defaults to it.
2. **Independent reference:** self-generated expected values are regression fixtures, not independent accuracy evidence.
3. **Timezone:** numeric UTC offsets do not demonstrate historical IANA timezone/DST correctness.
4. **Dasha:** validate Moon/Nakshatra balance, full MD/AD chronology and boundaries independently; fixed-year approximations are not authoritative.
5. **Transits:** no independent ingress/egress validation established; specify node convention and retrograde handling.
6. **Rules:** candidate associations remain blocked until evidence and promotion criteria are met; no deterministic career claims.
7. **Privacy/release:** no production privacy implementation or deployment readiness established; retain in-memory-by-default, opt-in persistence, and human release approval.
8. **Traceability:** exact original tasks #1–#45 must be recovered from an authoritative source; this matrix is not a substitute register.

## Next execution sequence

1. Obtain/access exact ZIP bytes and produce SHA-256 + internal-file manifests for every artifact.
2. Diff v29–v33 harnesses and v34/v35 rules; inspect v37 and the prototype source.
3. Execute v45 angle tests and the remaining reproducible offline tests; capture exact commands/output.
4. Fix provider metadata validation and Dasha validation defects in isolated, tested changes.
5. Build independent astronomy/Dasha/transit golden cases before enabling any career rule.
6. Only then integrate calculation outputs into report generation; require review and human approval before release.
