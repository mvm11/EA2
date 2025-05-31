from abc import ABC, abstractmethod
from typing import Dict

class GetMostVisitedCities(ABC):
    @abstractmethod
    def execute(self) -> Dict[str, int]:
        """Returns the most visited cities"""
        pass
