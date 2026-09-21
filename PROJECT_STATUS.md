# Project Status — Career Transition Astrology V1

**Last updated:** 2026-09-21  
**Status:** V1-alpha acceptance evidence complete; V2 remains unopened.

## Objective and scope
Build a testable V1 for Vedic astrology career/job-transition decision support. Scope is limited to career/job transitions. No deterministic outcomes, unsupported classifications, or expansion into wealth, health, family, love, legal, or unrelated astrology.

## Current V1-alpha boundary
The alpha is intentionally limited to collecting and validating a birth-input/provenance envelope and returning structured status. It does not calculate planetary longitudes, Dasha, transits, or career outlook. `career_outlook` remains null; `career_rules_eligible` remains false. The isolated `src/astrology/dasha.py` module is not integrated into the CLI and is not independently certified.

## Acceptance evidence
The acceptance-satisfying commit is `5cc14f40f1c71f9772c3c8163a83a903c9401bdd`.
- GitHub Actions run #51 (`35547730899`) completed successfully for that exact commit on 2026-09-21.
- The acceptance evidence files and tests are present in the repository tree at that commit.
- `V1_ACCEPTANCE.md` records the individual evidence paths and explicitly keeps the optional local form optional.

## Repository evidence
- `.gitignore` excludes caches, virtual environments, secrets/local config, private birth-data/output directories, ZIP dumps, and logs.
- README documents Python 3.11+, standard-library test setup, CLI/test commands, synthetic envelope example, opt-in saving, and scope limits.
- CLI hardening covers structured errors, mutually exclusive input sources, and restricts opt-in persistence to the gitignored `outputs/` directory.
- CLI contract tests cover malformed JSON, file errors, output contract, input-source exclusivity, opt-in saving, and the root-level `cli.py` entrypoint.
- A dedicated `src/cli.py` entrypoint delegates to the single root CLI implementation; a regression test executes `python src/cli.py --help` and verifies the V1 CLI surface.
- Input-contract regression coverage explicitly includes numeric timezone-offset rejection and boolean/non-finite coordinate rejection.
- `src/validation/input_contract.py` review confirms strict date/time parsing, IANA timezone handling, finite bounded coordinates, explicit calculation metadata, provider-settings attestation requirement, and rejection of ambiguous/nonexistent DST local times.
- `.github/workflows/python-tests.yml` targets pushes to `main` and PRs targeting `main`, and runs unittest discovery plus CLI tests.
- `V1_HANDOFF.md` provides run commands, limits, privacy cautions, and next gates.
- `docs/PUBLIC_BIRTH_DATA_AUDIT.md` documents the tracked-tree/content privacy audit; no personal birth charts are part of the public repository.

## Original project-register caveat
Original task register #1–#45 remains unrecovered. Do not fabricate it. Historical ZIPs/artifacts from the original project remain unavailable for full inspection; do not reconstruct or infer their contents from version labels.

## Explicitly out of scope until a human opens V2
Provider chart calculations, independent astronomy goldens, Dasha/transits, career rule engine, 12-month outlook, deployment, domain, payments, and recovery of missing historical ZIPs. Provider licensing and calculation accuracy must be reviewed before any later integration.

## Operating constraints
No background runner is verified; work proceeds during active sessions. No local test execution is available. Do not claim unperformed actions. Do not use real birth data in public fixtures. Human approval is required before release/deployment or paid services.
