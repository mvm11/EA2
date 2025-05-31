from dataclasses import dataclass

@dataclass(frozen=True)
class Satisfaction:
    country: str
    rating: float
