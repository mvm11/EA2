from dataclasses import dataclass

@dataclass(frozen=True)
class Purpose:
    description: str
