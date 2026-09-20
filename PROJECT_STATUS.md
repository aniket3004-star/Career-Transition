# Project Status — Career Transition Astrology V1

**Last updated:** 2026-09-20  
**Status:** In progress; V1-alpha is an input-validation CLI, not a certified astrology engine.

## Objective and scope
Build a testable V1 for Vedic astrology career/job-transition decision support. Scope is limited to career/job transitions. No deterministic outcomes, unsupported classifications, or expansion into wealth, health, family, love, legal, or unrelated astrology.

## Current V1-alpha boundary
The alpha is intentionally limited to collecting and validating a birth-input/provenance envelope and returning structured status. It must not calculate planetary longitudes, Dasha, transits, or career outlook. `career_outlook` remains null; `career_rules_eligible` remains false. The isolated `src/astrology/dasha.py` module is not integrated into the CLI and is not independently certified.

## Latest repository evidence
- `.gitignore` exists and excludes caches, virtual environments, secrets/local config, private birth-data/output directories, ZIP dumps, and logs.
- README documents Python 3.11+, standard-library test setup, CLI/test commands, synthetic envelope example, opt-in saving, and scope limits.
- CLI hardening covers structured errors, mutually exclusive input sources, and restricts opt-in persistence to the gitignored `outputs/` directory.
- CLI contract tests cover malformed JSON, file errors, output contract, input-source exclusivity, opt-in saving, and the root-level `cli.py` entrypoint.
- A dedicated `src/cli.py` entrypoint now delegates to the single root CLI implementation; a regression test executes `python src/cli.py --help` and verifies the V1 CLI surface.
- Input-contract regression coverage explicitly includes numeric timezone-offset rejection (`3bc8ae1`) and boolean/non-finite coordinate rejection (`a22cb5d`).
- `src/validation/input_contract.py` review confirms strict date/time parsing, IANA timezone handling, finite bounded coordinates, explicit calculation metadata, provider-settings attestation requirement, and rejection of ambiguous/nonexistent DST local times. This is code review, not a local test run.
- `.github/workflows/python-tests.yml` targets pushes to `main` and PRs targeting `main`, and runs unittest discovery plus CLI tests.
- `V1_HANDOFF.md` exists and provides run commands, limits, privacy cautions, and next gates.
- GitHub Actions run #42 (`35529052301`) completed successfully on `f225aeea37619d2a9ab6de29a8b30360c071ac22` after the src-entrypoint and tracked-ZIP cleanup changes.
- The tracked `v1_alpha_upload.zip` dump was removed from `main` because V1 acceptance explicitly requires ZIP dumps to be excluded; its prior blob was `3bddd450adfdff25e8932e707ce6f21bbf90c485`.
- Privacy hardening removed personal birth data from `tests/test_input_contract.py` (`cbee045`) and `tests/test_cli.py` (`150eb043`).

## Acceptance status
`V1_ACCEPTANCE.md` remains **NOT DONE**. Do not claim V1-alpha acceptance until every checklist item has evidence. The repository uses standard-library `unittest` and has no third-party test dependencies; the acceptance phrase “pins test deps” needs explicit rationale/reconciliation rather than adding an unnecessary dependency solely to satisfy wording.

## Remaining work / gaps
1. Reconcile each acceptance checkbox with concrete evidence; only mark items complete when directly verified and documented.
2. Resolve the checklist terminology mismatch between its `timezone_id` wording and the implementation's `timezone` field while preserving the IANA-only requirement.
3. Resolve the acceptance checklist’s test-dependency wording while preserving the stdlib-only design if appropriate.
4. Complete a repository-content privacy review sufficient to support the remaining “no personal birth charts” and public-log/document claims; a recursive path inventory alone is not a full content scan.
5. Original task register #1–#45 remains unrecovered; do not fabricate it.
6. Historical ZIPs/artifacts from the original project remain unavailable for full inspection; do not reconstruct or infer their contents from version labels.

## Explicitly out of scope until a human opens V2
Provider chart calculations, independent astronomy goldens, Dasha/transits, career rule engine, 12-month outlook, deployment, domain, payments, and recovery of missing historical ZIPs. Provider licensing and calculation accuracy must be reviewed before any later integration.

## Operating constraints
No background runner is verified; work proceeds during active sessions. No local test execution is available. Do not claim unperformed actions. Do not use real birth data in public fixtures. Human approval is required before release/deployment or paid services.
