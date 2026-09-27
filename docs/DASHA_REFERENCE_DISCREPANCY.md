# Priyanka Dalwani Dasha Reference Discrepancy

Status: open research discrepancy; no production calculation convention changed.

## Source facts

The Dharmayana Kundli supplied for Priyanka Dalwani states:

- Birth: 20 October 1989, 05:23, Sambalpur, Odisha, India.
- Ayanamsa: 23.795366°.
- Moon: 13°36′53.12″ Gemini, Nakshatra Ardra, Pada 3, lord Rahu.
- Mahadasha table: Rahu 30-May-1980 → 30-May-1998; Jupiter 30-May-1998 → 30-May-2014; Saturn 30-May-2014 → 30-May-2033.
- Saturn Antardasha endpoints are internally proportional to the source Saturn interval; Saturn/Moon ends 02-Dec-2026.

These are source observations, not values recomputed by this repository.

## Current engine result

The repository's Vimshottari implementation uses:

- 27 equal nakshatras of 13°20′.
- Standard Vimshottari lord order and durations.
- 365.2425 days per dasha year.
- Opening balance calculated from the Moon's fractional position within its nakshatra.

Using the Moon longitude printed by the PDF, the engine places the Rahu Mahadasha endpoint about **4.415 days later** than the source's 30-May-1998 endpoint.

Changing only the year length does not resolve this:

- 365.25 days/year moves the endpoint only slightly later.
- 365.0 days/year still places it about two days later.
- 360 days/year moves it substantially earlier.

Therefore the observed four-day difference cannot be responsibly attributed to ordinary 365.24/365.25 year-length rounding.

## Reverse diagnostic

If the source endpoint 30-May-1998 is combined with the printed birth time and the repository's 365.2425-day convention, the source endpoint implies an opening balance equivalent to a Moon longitude of approximately **73.623709°**, about **32.23 arcseconds** higher than the Moon longitude printed in the PDF.

This is a diagnostic only. It does **not** establish that Dharmayana internally used that longitude.

## External convention evidence

Published calculators/software use different year-length conventions, including 365.25 days, 365.2425 days, and approximately 365.2564 days. The existence of multiple conventions is documented by independent astrology references; therefore exact date agreement with a specific calculator requires its calculation convention to be known.

Dharmayana's public Panchanga documentation says its Panchanga is calculated from precise Sun/Moon longitudes adjusted for location and timezone, but the public material reviewed here does not document the specific internal Vimshottari opening-balance convention used for this PDF.

## Engineering decision

Do **not** change the production Dasha engine to fit this one Kundli.

The Priyanka case remains a real-world regression/reference case with an explicit five-day source-boundary tolerance. The discrepancy remains visible and documented rather than hidden.

Next validation target: obtain an independently reproducible Dasha calculation using the same birth data and determine whether the disagreement comes from the source's internal Moon longitude/ayanamsa/ephemeris or from its opening-balance convention. Only a demonstrated convention should be promoted into the engine.
