from typing import Dict
from domain.model.destination.gateways.get_average_stay_by_city import GetAverageStayByCity

class GetAverageStayByCityUseCase:
    def __init__(self, repository: GetAverageStayByCity):
        self.repository = repository

    def execute(self) -> Dict[str, float]:
        return self.repository.execute()
