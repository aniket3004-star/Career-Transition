# Free Reference Sources & Provider Integration Plan

Date: 2026-09-20
Status: Research-backed design; no live API call or independent accuracy validation implied.

## Purpose

Use credible, freely accessible references to fill missing research/data inputs while keeping computation, validation, and astrological interpretation separate. Free access does not itself establish correctness, stability, permission for commercial use, or independence.

## Reference tiers

### Tier 1 — Astronomy engine and its official documentation

- Swiss Ephemeris documentation: https://www.astro.com/swisseph/swephinfo_e.htm
- General documentation mirror (secondary convenience only): https://ephe.scryr.io/swisseph/doc/swisseph.htm
- Python binding project: https://github.com/astrorigin/pyswisseph

Use for reproducible planetary positions/astronomical calculations, after pinning version, ephemeris flags/files, coordinate frame, time scale, and ayanamsha. Swiss Ephemeris licensing is dual-license; confirm AGPL/commercial obligations before any hosted or proprietary release. It does not itself provide the Jyotisha interpretation layer or certify career rules.

### Tier 2 — Independent or separately implemented Jyotisha calculators

- Open-source Vedic Jyotish API repository: https://github.com/rsaisankalp/vedic-jyotish-api
- Orrery repository: https://github.com/prashnavatika/orrery
- Jyotishika repository: https://github.com/ruta-gadgil/jyotishika

Treat these as candidate comparators, not automatically authoritative references. Inspect source, commit/version, tests, calculation flags, ayanamsha, node type, timezone handling, house convention, and license. A repository's own claim of cross-validation is not independent proof until its fixtures and methods are inspected and reproduced.

### Tier 3 — Hosted free/sandbox APIs

- FreeAstroAPI Dasha documentation: https://www.freeastroapi.com/docs/vedic/dasha
- Vedika API Dasha documentation: https://vedika.io/blog/vimshottari-dasha-api-explained

Potentially useful for schema/behavior comparison and exploratory checks. Before sending any birth data, verify current free-tier limits, authentication, retention/privacy terms, service terms, and whether API responses disclose exact settings. Never send real personal birth data to a third party without explicit consent; use synthetic fixtures first. Hosted API outputs are comparators, not ground truth.

## Dasha validation requirements

1. Establish a trusted sidereal Moon longitude from a pinned ephemeris configuration.
2. Record exact birth local datetime, IANA timezone, UTC conversion, coordinates, ayanamsha, node conventions if relevant, ephemeris version/flags, and reference date.
3. Derive nakshatra, pada, starting lord, elapsed fraction, and birth balance explicitly.
4. Compare MD/AD start/end instants against at least one independently implemented/reference calculation using identical conventions.
5. Include nakshatra boundaries, 360° wrap, leap dates, timezone/DST boundaries, and birth-balance edge cases.
6. Store raw request/response, normalized output, source URL/version/date, configuration, circular/temporal tolerances, and pass/fail rationale.
7. Keep disagreement visible. Do not average conflicting outputs or silently default configuration.
8. Do not enable career interpretation until the Dasha gate and relevant rule-evidence gate independently pass.

## API adapter contract (to implement when source/interface is available)

Each adapter should expose:

- provider name, API/version, endpoint, retrieval timestamp, terms/license note;
- explicit input settings and provider-echoed settings (distinguish requested from verified);
- raw response preserved separately from normalized values;
- typed errors for timeout, rate limit, auth, schema drift, and provider failure;
- no secret values in logs;
- no automatic retries that can incur cost or leak sensitive inputs;
- fixture mode for deterministic offline tests;
- provenance completeness flag, which remains false if settings are absent or inferred.

## Current project status

The repository currently contains a standalone Vimshottari timeline helper. The project artifact audit describes a provider-pack prototype and a Dasha-validator ZIP, but those ZIP contents are not integrated into the repository in this checkpoint. No live provider request, API-to-normalizer integration, independent Dasha comparison, or provider accuracy pass is claimed here.

## Immediate implementation sequence

1. Recover/download the exact existing provider-pack and Dasha-validator artifacts and produce file manifests/hashes.
2. Inspect and compare source/license/interface; select candidates without assuming their claims are true.
3. Add provider-neutral request/response schemas and adapters behind fixture-first tests.
4. Connect Moon longitude output to the Dasha validator; reject absent/mismatched provenance.
5. Run reproducible tests and capture actual CI logs.
6. Perform synthetic cross-provider checks; only then consider consented real-data checks.

## Source notes

The Swiss Ephemeris docs describe its computational scope and dual licensing. The linked Vedic repositories document their own feature sets and methods; these are useful leads but are not independent certification. API documentation is a contract description, not evidence of uptime, free-tier availability, or accuracy.
