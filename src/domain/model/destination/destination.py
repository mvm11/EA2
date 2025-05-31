from dataclasses import dataclass


@dataclass(frozen=True)
class Destination:
    country: str
    city: str
    latitude: float
    longitude: float
