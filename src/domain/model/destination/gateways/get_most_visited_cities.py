from abc import ABC, abstractmethod
from typing import List, Tuple

class GetMostVisitedCities(ABC):
    @abstractmethod
    def execute(self, top_n: int = 10) -> List[Tuple[str, int]]:
        """Returns a list of the most visited cities with visit count"""
        pass
