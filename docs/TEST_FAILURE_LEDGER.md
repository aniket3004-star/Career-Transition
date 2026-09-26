# V1 Test Failure Ledger

Scope: GitHub Actions history available for v2-calculation-foundation, reviewed 2026-09-27.

- Workflow runs reviewed: 155
- Failed workflow runs: 66
- Unique commits with at least one failed run: 44
- Current head: 05c677bfd5add7ab75dca7bdf4502deb46358af4
- Current head: green in both workflows

## Every unique failed commit

| Commit | Failed runs | Workflows | Audit status |
|---|---|---|---|
| de44c06e9f42 | 36264279025, 36264279018 | Python validation tests, Tests | Dasha helper moved class methods; fixed by 05c677b. |
| 2c71dc811a73 | 36264274061, 36264274057 | Tests, Python validation tests | Dasha boundary harness regression; later green correction. |
| dbe8972f5b0f | 36263694256, 36263694249 | Python validation tests, Tests | Dasha reference harness regression; later green correction. |
| 0b293f8e880a | 36263668701, 36263668693 | Python validation tests, Tests | Dasha boundary test regression; later corrected. |
| a1c5a6204a38 | 36263153749, 36263153714 | Tests, Python validation tests | Priyanka AD expectation wrong (Sun vs Moon); fixed by d78d62a. |
| 8b6247762356 | 36262212277 | Python validation tests | Network timeout in astronomy dependency-boundary test. |
| 7777c38d44a2 | 36260977628, 36260977611 | Tests, Python validation tests | NameError in convention refactor; fixed by 32a64c6. |
| f6ab8d0c2d25 | 36260958808, 36260958760 | Tests, Python validation tests | CalculationConventions signature regression; fixed by 32a64c6. |
| 31759d88fc27 | 36260625433, 36260625416 | Tests, Python validation tests | Golden validation swallowed longitude/tolerance checks; fixed by 8fa4fba. |
| 9d73813dbfd6 | 36260326639, 36260326626 | Python validation tests, Tests | Golden validation swallowed longitude/tolerance checks; fixed by 8fa4fba. |
| ab75241dc470 | 36260316929, 36260316850 | Tests, Python validation tests | Initial convention compatibility regression; fixed by 8fa4fba. |
| 2e7eb33caac3 | 36257712733, 36257712729 | Python validation tests, Tests | Golden provenance transition failure; later green. |
| 8193fdae36df | 36257705893, 36257705818 | Python validation tests, Tests | Golden provenance transition failure; later green. |
| 0a39682223be | 36257700882, 36257700863 | Python validation tests, Tests | Golden provenance transition failure; later green. |
| cbe7748e984c | 36257127993, 36257127985 | Python validation tests, Tests | GoldenCaseMetadata constructor skipped validate(); fixed by e4913446. |
| be5a97412333 | 36257123781, 36257123772 | Python validation tests, Tests | Golden loader iterative regression; later green. |
| 9202282e3c51 | 36257110202, 36257110184 | Tests, Python validation tests | Golden loader iterative regression; later green. |
| 49c3ecfca833 | 36257100487, 36257100483 | Tests, Python validation tests | Golden loader iterative regression; later green. |
| af4a48b8478f | 36257098090, 36257098073 | Python validation tests, Tests | Golden loader iterative regression; later green. |
| 60dca5cf76a5 | 36256564398, 36256564397, 36256553674, 36256553605 | Tests, Python validation tests | Golden metadata constructor validation missing; fixed by e4913446. |
| f8db2961630b | 36248840655, 36248840611 | Tests, Python validation tests | CI workflow integration failure; later baseline green. |
| 5cc35dd421ad | 36248803209 | Python validation tests | Golden-set validation failure; later green. |
| 963fa55159f0 | 36248278540 | Python validation tests | Golden-set validation failure; later green. |
| 4e88f4386a68 | 36245110201 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 3d2e4e756955 | 36245108077 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 38ae213dd982 | 36241719236 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| f26d2f969d44 | 36241714752 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 0a15a805f88f | 36241491597 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 1031aca24d51 | 36241478766 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| c1af8556da79 | 36241476019 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| bd0ebf44f705 | 36241468677 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 9b13cff3fb1a | 36240366773 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 1af7beb1fcaa | 36240363285 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| ff165deff795 | 36235705997 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 4e26ee3859d2 | 36235704858 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 8ea53ca9373a | 36235123138 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 2fbf4949d5c7 | 35478633940 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 710d83998033 | 35475998450 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| a22cb5d2877b | 35473364311 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 3bc8ae118b5e | 35470252432 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 8fe1c516df42 | 35467402126 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 137b459d7ecf | 35464288783 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 8eafa62277a8 | 35463663962 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |
| 066793a7e0c5 | 35463430739 | Python validation tests | **UNRESOLVED HISTORICAL FAILURE** — no root-cause claim made yet. |

## Verified clusters

- Calculation-gate failures: repeated ValueError-not-raised failures for provenance_complete during the gate refactor.
- CLI failures: missing src.cli import and later non-zero CLI exit-code regressions.
- Golden metadata failures: constructor did not invoke validation; fixed in e4913446.
- Golden longitude/tolerance failures: validation was swallowed by a method-boundary refactor; fixed in 8fa4fba.
- Convention failures: API signature / NameError regressions; fixed in 32a64c6.
- Reference-snapshot failure: one Python validation run failed from an HTTP timeout, not a deterministic assertion.
- Priyanka Dasha failure: incorrect active Antardasha expectation; fixed in d78d62a.
- Dasha boundary-harness failures: recent refactor regressions; current head is green.

## Important unresolved historical set

Rows without a verified diagnosis remain explicitly marked unresolved. A later green commit is not treated as proof of cause or resolution.

## Mandatory verification rule

For every future code change: run CI, wait for completion, inspect both workflows, fix any failure, rerun both, verify both are completed and green, and only then proceed.
