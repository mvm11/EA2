from dataclasses import dataclass
from datetime import date

from domain.model.accommodation.accommodation import Accommodation
from domain.model.destination.destination import Destination
from domain.model.purpose.purpose import Purpose
from domain.model.transport.transport import Transport


@dataclass(frozen=True)
class Trip:
    date: date
    destination: Destination
    accommodation: Accommodation
    stay_duration: int
    daily_expense: float
    rating: int
    transport: Transport
    purpose: Purpose
