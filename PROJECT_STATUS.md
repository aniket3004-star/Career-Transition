# Project Status — Career Transition Astrology V1

**Last updated:** 2026-09-20  
**Status:** In progress; V1-alpha is an input-validation CLI, not a certified astrology engine.

## Objective and scope
Build a testable V1 for Vedic astrology career/job-transition decision support. Scope is limited to career/job transitions. No deterministic outcomes, unsupported classifications, or expansion into wealth, health, family, love, legal, or unrelated astrology.

## Current V1-alpha boundary
The alpha is intentionally limited to collecting and validating a birth-input/provenance envelope and returning structured status. It must not calculate planetary longitudes, Dasha, transits, or career outlook. `career_outlook` remains null; `career_rules_eligible` remains false. The isolated `src/astrology/dasha.py` module is not integrated into the CLI and is not independently certified.

## Evidence observed in repository
- `.gitignore` exists and excludes caches, virtual environments, secrets/local config, private birth-data/output directories, ZIP dumps, and logs (commit `9d5776008b2059acee0422c73183be1705c2c760`).
- README documents Python 3.11+, standard-library test setup, CLI/test commands, synthetic envelope example, opt-in saving, and scope limits (commit `8eafa62277a8744c93565f55ee7daac1bc54f38`; current README reviewed 2026-09-20).
- CLI hardening covers structured errors, mutually exclusive input sources, and restricts opt-in persistence to the gitignored `outputs/` directory (commit `11ec432f7cfc93814b741f08829869d2c3c908ef`).
- CLI tests were added for malformed JSON, file errors, output contract, input-source exclusivity, and opt-in saving (commit `f333f75e04ec7a2b3c9d3155f7583a520abb5189`).
- Input-contract source review confirms strict date/time parsing, IANA timezone handling, finite bounded coordinates, explicit calculation metadata, provider-settings attestation requirement, and rejection of ambiguous/nonexistent DST local times. Test source includes happy path and several fail-closed cases. This is code review, not a new local test run.
- `.github/workflows/python-tests.yml` targets pushes to `main` and PRs targeting `main`, and runs unittest discovery plus CLI tests.
- `V1_HANDOFF.md` now exists (added in commit `9a1b01d27ca9e5b57c63ae02fc59ef17fbcbefb6`) and provides run commands, limits, privacy cautions, and next gates.
- GitHub Actions run #27 for current `main` commit `9a1b01d27ca9e5b57c63ae02fc59ef17fbcbefb6` completed with conclusion `success`: https://github.com/aniket3004-star/Career-Transition/actions/runs/35464628771

## Acceptance status
`V1_ACCEPTANCE.md` remains **NOT DONE** and its checklist remains unchecked. Do not claim V1-alpha acceptance until every checklist item has evidence. The repository currently uses standard-library `unittest` and has no third-party test dependencies; the acceptance phrase “pins test deps” needs an explicit rationale/reconciliation rather than adding an unnecessary dependency solely to satisfy wording.

## Remaining work / gaps
1. Reconcile each acceptance checkbox with concrete evidence; only mark items complete when directly verified and documented.
2. Confirm privacy behavior and absence of raw personal birth data in tracked files/logging; current review is not a comprehensive secret or history scan.
3. Verify edge cases and CLI behavior with CI on the exact candidate commit; no local test execution is available in this environment.
4. Resolve the acceptance checklist’s test-dependency wording while preserving the stdlib-only design if appropriate.
5. Original task register #1–#45 remains unrecovered; do not fabricate it.
6. Historical ZIPs/artifacts remain unavailable for full inspection; preserve existing archive material and ask the user to supply source files if they are needed.

## Explicitly out of scope until a human opens V2
Provider chart calculations, independent astronomy goldens, Dasha/transits, career rule engine, 12-month outlook, deployment, domain, payments, and recovery of missing historical ZIPs. Provider licensing and calculation accuracy must be reviewed before any later integration.

## Operating constraints
No background runner is verified; work proceeds during active sessions. No local test execution is available. Do not claim unperformed actions. Do not use real birth data in public fixtures. Human approval is required before release/deployment or paid services.
