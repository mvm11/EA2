from typing import Dict
from domain.model.destination.gateways.get_most_visited_cities import GetMostVisitedCities

class GetMostVisitedCitiesUseCase:
    def __init__(self, repository: GetMostVisitedCities):
        self.repository = repository

    def execute(self) -> Dict[str, int]:
        return self.repository.execute()
