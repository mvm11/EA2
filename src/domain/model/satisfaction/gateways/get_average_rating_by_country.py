from abc import ABC, abstractmethod
from typing import Dict

class GetAverageRatingByCountry(ABC):
    @abstractmethod
    def execute(self) -> Dict[str, float]:
        """Returns average satisfaction rating per country"""
        pass
