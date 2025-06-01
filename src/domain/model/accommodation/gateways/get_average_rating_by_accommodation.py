from abc import ABC, abstractmethod
from typing import Dict

class GetAverageRatingByAccommodation(ABC):
    @abstractmethod
    def execute(self) -> Dict[str, float]:
        """Returns average rating per accommodation type"""
        pass
