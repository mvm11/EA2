from abc import ABC, abstractmethod
from typing import Dict

class GetAverageExpenseByAccommodation(ABC):
    @abstractmethod
    def execute(self) -> Dict[str, float]:
        """Returns average daily expense by type of accommodation"""
        pass
