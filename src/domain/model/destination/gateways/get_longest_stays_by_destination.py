from abc import ABC, abstractmethod
from typing import Dict

class GetLongestStaysByDestination(ABC):
    @abstractmethod
    def execute(self) -> Dict[str, float]:
        """Returns destinations with longest average stay"""
        pass
