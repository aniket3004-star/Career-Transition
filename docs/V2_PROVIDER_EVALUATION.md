# V2 Provider Evaluation

## Candidate architecture

Use a provider adapter rather than coupling the career engine to an ephemeris
library. Every adapter must return provider/version, ephemeris source,
calculation timestamp, explicit settings, planetary longitudes and Ascendant.

## Candidate reference path: Astropy + JPL ephemeris

Astropy documents solar-system body calculations with built-in ERFA routines
and optional JPL ephemerides. JPL ephemerides require the `jplephem` package
and provide a useful independent astronomy reference path.

This is a reference/calculation component, not yet a Vedic chart provider:
sidereal ayanamsha, house conventions, nodes and the exact Vedic output contract
still require explicit implementation and validation.

## Swiss Ephemeris

Swiss Ephemeris is a candidate Vedic calculation provider, but its official
documentation states that distribution/public-service use requires choosing
between AGPL and its Professional License. No license purchase has been made.
Do not make it a mandatory dependency until licensing is deliberately chosen.

## Required validation sequence

1. Freeze explicit conventions.
2. Generate non-identifying golden cases from an independent reference path.
3. Run the candidate Vedic provider against those cases.
4. Compare circular longitudes using predeclared tolerances.
5. Record provider/version/ephemeris/settings and evidence digest.
6. Only then allow `accuracy_verified=true`.
