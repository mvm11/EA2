from typing import Dict
from domain.model.trip.gateways.get_most_popular_months import GetMostPopularMonths

class GetMostPopularMonthsUseCase:
    def __init__(self, repository: GetMostPopularMonths):
        self.repository = repository

    def execute(self) -> Dict[str, Dict[str, float]]:
        return self.repository.execute()
