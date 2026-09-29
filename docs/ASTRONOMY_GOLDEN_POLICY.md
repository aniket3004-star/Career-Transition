# V2 Astronomy Golden-Test Policy

## Purpose

The V2 calculation layer must be validated against independently produced astronomical reference values before its outputs can feed Nakshatra, Vimshottari Dasha, transit, or career-rule logic.

This document defines the evidence standard. It does **not** certify any calculation provider.

## Independence rule

A golden value must come from a source independent of the runtime implementation being tested.

The preferred external reference for planetary geocentric validation is JPL Horizons. Horizons supports reproducible ephemeris queries with explicit target, center, time scale, reference frame, output quantities, and units. Reference requests must record those settings rather than relying on service defaults.

Reference: https://ssd.jpl.nasa.gov/horizons/manual.html
API documentation: https://ssd-api.jpl.nasa.gov/doc/horizons.html

## Required golden record

Every promoted golden case must record:

- case_id
- target body and unique identifier
- observer/center and unique identifier
- input instant and time scale
- calendar convention
- reference frame
- reference plane
- geometric vs apparent/light-time treatment
- requested output quantity
- output units
- reference-source name and version/date when available
- complete reproducible query or query-equivalent settings
- captured reference value
- numeric tolerance
- provenance URL
- capture date
- notes on known model/convention differences

No hidden defaults are permitted for fields that can materially change the result.

## What counts as a golden

A case is **CERTIFIED** only when:

1. the reference query/settings are fully recorded;
2. the captured value is traceable to the external source;
3. the unit and coordinate conventions are explicit;
4. the test tolerance is justified;
5. the case contains no personal birth data;
6. the runtime provider can be tested against the case without importing the reference implementation.

A case with a query but no independently captured value is **REFERENCE_PENDING**, not a golden.

## Layering

The first astronomy goldens should validate the provider adapter at the astronomical boundary:

external reference -> provider output -> normalized calculation record

Do not combine this test with ayanamsha, Nakshatra, Dasha, or career-rule assertions. Those layers receive their own independent validation gates.

For sidereal Vedic outputs, the reference contract must separately identify:

- tropical/geometric astronomical longitude source;
- ayanamsha model and exact version/convention;
- zodiac mode;
- normalization to [0, 360).

A value produced by subtracting an undocumented ayanamsha is not a certified sidereal golden.

## Tolerance policy

Tolerance is property-specific. Do not use one global epsilon.

- Angular longitude/latitude: define tolerance in arcseconds.
- Distance: define tolerance in km or AU.
- Time: define tolerance in seconds.
- Derived values: tolerance must include documented upstream uncertainty and numerical rounding.

Boundary-sensitive tests must use explicit stricter checks where a small error could change a Nakshatra or other categorical boundary.

## Failure behavior

If a provider disagrees with a certified golden outside tolerance:

- fail the test;
- retain the failing value and provider metadata in the test output;
- do not silently widen tolerance;
- do not alter conventions solely to fit a single case;
- keep downstream eligibility disabled until the discrepancy is explained.

## Promotion rule

Reference data may be promoted from REFERENCE_PENDING to CERTIFIED only after independent review of the captured source output and conventions. The V2 implementation must never treat an uncaptured URL/query as proof that a value is correct.
