"""Optional astronomical reference adapter using Astropy.

This is an astronomy reference component, not the Vedic provider. It returns
geocentric true-ecliptic tropical longitudes and records the explicit JPL
ephemeris used. Sidereal conversion and house calculations are intentionally
not performed here.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Mapping

BODIES = ("sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune")


def calculate_tropical_longitudes(
    utc_instant: datetime,
    latitude: float,
    longitude: float,
    ephemeris: str = "de432s",
) -> Mapping[str, float]:
    """Return geocentric true-ecliptic tropical longitudes in degrees.

    Requires optional astropy and jplephem packages. No package defaults are
    hidden: the ephemeris is an explicit argument.
    """
    if utc_instant.tzinfo is None or utc_instant.utcoffset() is None:
        raise ValueError("utc_instant must be timezone-aware")
    if not -90 <= latitude <= 90 or not -180 <= longitude <= 180:
        raise ValueError("latitude/longitude out of range")

    try:
        from astropy.coordinates import EarthLocation, GeocentricTrueEcliptic
        from astropy.coordinates import get_body, solar_system_ephemeris
        from astropy.time import Time
    except ImportError as exc:
        raise RuntimeError(
            "Astropy reference adapter requires optional dependencies: astropy and jplephem"
        ) from exc

    obstime = Time(utc_instant.astimezone(timezone.utc))
    location = EarthLocation.from_geodetic(longitude, latitude)
    values: dict[str, float] = {}

    with solar_system_ephemeris.set(ephemeris):
        for body in BODIES:
            coord = get_body(body, obstime, location=location, ephemeris=ephemeris)
            ecliptic = coord.transform_to(
                GeocentricTrueEcliptic(equinox=obstime, obstime=obstime)
            )
            values[body.capitalize()] = float(ecliptic.lon.deg % 360.0)

    return values
