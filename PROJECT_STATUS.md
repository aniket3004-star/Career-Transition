# Project Status — Career Transition Astrology V1

**Last updated:** 2026-09-20  
**Status:** In progress; V1-alpha is an input-validation CLI, not a certified astrology engine.

## Objective and scope
Build a testable V1 for Vedic astrology career/job-transition decision support. Scope is limited to career/job transitions. No deterministic outcomes, unsupported classifications, or expansion into wealth, health, family, love, legal, or unrelated astrology.

## Verified progress
- Added `.gitignore` for caches, virtual environments, secrets/local config, private birth-data/output directories, ZIP dumps, and logs (commit `9d5776008b2059acee0422c73183be1705c2c760`).
- Updated README with Python 3.11/std-library setup, CLI/test commands, JSON envelope guidance, opt-in save note, and V1-alpha scope (commit `8eafa62277a8744c93565f55ee7daac1bc54f38`).
- Fixed test import path and confirmed CI success on commit `c44aa6ccfed7b59c5e39f39160d61e038d663b48` (workflow run #20).
- Hardened CLI error handling, mutually exclusive input sources, and restricted opt-in persistence to the gitignored `outputs/` directory (commit `11ec432f7cfc93814b741f08829869d2c3c908ef`).
- Added CLI tests for malformed JSON, file errors, output contract, input-source exclusivity, and opt-in saving (commit `f333f75e04ec7a2b3c9d3155f7583a520abb5189`).
- GitHub Actions workflow run #22 for `f333f75e04ec7a2b3c9d3155f7583a520abb5189` completed successfully: https://github.com/aniket3004-star/Career-Transition/actions/runs/35464126747

## Validation status
CI has passed for the commits above. No local test execution was available. No provider comparison, planetary calculation, Dasha/transit validation, career-rule validation, backtest, deployment, or release was run. Nothing in the calculation layer is certified.

## Remaining acceptance gaps
- Review `V1_ACCEPTANCE.md` line-by-line against current repo state; do not infer completion from CI alone.
- `V1_HANDOFF.md` has not yet been created.
- Ensure requirements/test-dependency expectations are accurately reconciled with the standard-library `unittest` approach.
- Confirm all privacy acceptance evidence, including ignored output paths and no raw personal data in logs/docs.
- Original task register #1–#45 remains unrecovered; do not fabricate it.
- Historical ZIPs/artifacts remain unavailable for full inspection; preserve existing archive material.

## Scope boundary
V1-alpha validates birth-input envelopes only. It does not calculate planetary positions, Dasha, transits, or career outlook. These remain blocked pending independent validation and an explicitly opened V2 scope.

## Next actions
1. Audit each acceptance criterion against actual files and CI evidence.
2. Add a handoff document clearly separating usable CLI instructions from limitations and unpassed gates.
3. Reconcile dependency and privacy documentation.
4. Continue independent repository work; request only missing source artifacts/access or decisions requiring user authorization.

## User-only escalation
Ask only for missing source artifacts/access, authentication or permissions, personal product decisions that cannot be inferred, paid service activation, data-retention changes, production deployment, or release approval. No background runner is verified; work proceeds during active sessions.
