# Project Status — Career Transition Astrology V1

**Last updated:** 2026-09-20  
**Status:** In progress; no verified autonomous background AI runner.

## Objective and scope
Build a testable V1 for Vedic astrology career/job-transition decision support. Scope is limited to career/job transitions. No deterministic outcomes, no unsupported classifications, and no expansion into wealth, health, family, love, legal, or unrelated astrology.

## Verified this session
- Added `.gitignore` to exclude Python caches, virtual environments, secrets/local config, private birth-data/output directories, ZIP dumps, and logs.
- Commit: `9d5776008b2059acee0422c73183be1705c2c760`.
- Reviewed `V1_ACCEPTANCE.md`, `cli.py`, `src/validation/input_contract.py`, `tests/test_input_contract.py`, README, and artifact audit/disposition/template documents.
- Confirmed the README does not yet provide exact local run commands; CLI and input-contract tests exist, but this review did not execute them.
- Checked the Dasha commit combined status; no status entries were returned, so CI cannot be reported green.

## Validation status
No local test execution was available in this session. No new CI result verified. No provider comparison, Dasha/transit validation, deployment, or release was run. Nothing is certified by this status update.

## Known acceptance gaps
- `requirements.txt` exists but does not pin a test dependency; current test suite uses `unittest` from Python standard library.
- README needs exact local run/test commands and an explicitly synthetic CLI example.
- CLI behavior for malformed JSON/file errors needs review and tests.
- Privacy checklist still needs evidence that `--save` targets a gitignored location by default or through documented usage; current CLI accepts arbitrary save paths.
- `V1_HANDOFF.md` does not yet exist.
- CI status must be checked on the latest commit before acceptance.
- The original task register #1–#45 remains unrecovered; do not fabricate it.

## Scope boundary
V1-alpha is an input-validation CLI only. It does not calculate planetary positions, Dasha, transits, or career outlook. Those remain blocked until a human opens V2 and the required independent validation is completed.

## Next actions
1. Add precise README setup/run/test instructions with synthetic data only.
2. Harden CLI error handling and add tests for malformed JSON, missing files, output shape, and nonzero reject behavior.
3. Verify privacy behavior and document safe opt-in persistence.
4. Run tests through CI and capture an actual green result.
5. Create `V1_HANDOFF.md` only after checklist items have evidence.
6. Continue repository cleanup only where redundancy is proven; preserve archive until its contents can be inspected.

## User-only escalation
Ask only for missing source artifacts/access, authentication or permissions, personal product decisions that cannot be inferred, paid service activation, data retention changes, production deployment, or release approval. Continue independent work meanwhile.