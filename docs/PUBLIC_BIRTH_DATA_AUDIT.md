# Public birth-data audit

Date: 2026-09-21

Scope: current `main` tree reviewed before this audit commit, with emphasis on repository hygiene and the V1-alpha gate `No personal birth charts in git`.

Checks performed:

- Inspected the complete recursive `main` tree; no chart/export file or other personal birth-chart artifact is present in the tracked paths.
- Searched repository contents for known personal birth markers used in earlier fixtures: `1987-03-09`, `10:17`, `20.4625`, `85.8828`, and `Cuttack`; no matches were returned.
- Searched for generic personal-birth terms such as `birth chart` and `personal data`; no repository-content matches were returned.
- The tracked root CLI fixture is synthetic and explicitly states that real birth details must not be used in repository tests.

This audit is repository evidence only. It does not claim that untracked local files, GitHub history outside the current tracked tree, or external artifacts contain no personal data.
