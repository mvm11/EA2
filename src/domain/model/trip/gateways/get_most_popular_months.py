from abc import ABC, abstractmethod
from typing import Dict

class GetMostPopularMonths(ABC):
    @abstractmethod
    def execute(self) -> Dict[str, Dict[str, float]]:
        """
        Returns a dictionary with:
        {
            'viajes_por_mes': {mes: count},
            'duracion_promedio_por_mes': {mes: avg_duracion},
            'gasto_diario_promedio_por_mes': {mes: avg_gasto},
            'valoracion_promedio_por_mes': {mes: avg_valoracion}
        }
        """
        pass
