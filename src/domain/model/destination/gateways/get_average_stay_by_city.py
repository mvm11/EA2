from abc import ABC, abstractmethod
from typing import Dict

class GetAverageStayByCity(ABC):
    @abstractmethod
    def execute(self) -> Dict[str, float]:
        """Returns the average stay duration per city"""
        pass
