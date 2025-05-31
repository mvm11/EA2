from dataclasses import dataclass

@dataclass(frozen=True)
class Transport:
    type: str
