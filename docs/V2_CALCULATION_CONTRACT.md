# V2 Calculation Contract

## Purpose

Define the evidence boundary between astronomical calculation and downstream Vedic-astrology logic.

## Required calculation record

A certified calculation record must identify:
- birth date and local birth time;
- IANA timezone;
- UTC-normalized instant;
- latitude and longitude;
- calculation provider and exact version;
- ephemeris data/version where applicable;
- ayanamsha and its exact convention;
- zodiac mode;
- house-system convention when houses are calculated;
- calculation timestamp;
- source/provenance identifier.

## Validation requirements

Before a calculated value can feed Dasha, transit, or career rules:
- the provider configuration must be explicit;
- no hidden defaults may establish accuracy;
- longitude values must have documented reference frame and units;
- timezone conversion must be reproducible;
- boundary cases must be covered by tests;
- independent reference values must exist for the supported calculation scope;
- discrepancies must be recorded rather than silently tolerated.

## Downstream gate

career_rules_eligible remains false until the calculation layer and all required upstream validations have passed their respective gates.

## Dasha gate

Vimshottari Dasha requires an independently validated sidereal Moon longitude. The existing Dasha prototype may be used as research material, but it is not certified merely because its unit tests pass.