from typing import Dict
from domain.model.trip.gateways.get_most_popular_months import GetMostPopularMonths

class GetMostPopularMonthsUseCase:
    def __init__(self, service: GetMostPopularMonths):
        self.service = service

    def execute(self) -> Dict[str, int]:
        return self.service.execute()
