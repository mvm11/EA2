from abc import ABC, abstractmethod
from typing import Dict

class GetMostPopularMonths(ABC):
    @abstractmethod
    def execute(self) -> Dict[str, int]:
        """Returns number of trips by month"""
        pass
