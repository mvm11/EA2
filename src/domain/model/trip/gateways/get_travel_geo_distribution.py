from abc import ABC, abstractmethod
from typing import Any

class GetTravelGeoDistribution(ABC):
    @abstractmethod
    def execute(self) -> Any:
        """Generates a map showing travel distribution by country and stay duration"""
        pass
