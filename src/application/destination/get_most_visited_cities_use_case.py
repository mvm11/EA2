from typing import List, Tuple
from domain.model.destination.gateways.get_most_visited_cities import GetMostVisitedCities

class GetMostVisitedCitiesUseCase:
    def __init__(self, repository: GetMostVisitedCities):
        self.repository = repository

    def execute(self, top_n: int = 10) -> List[Tuple[str, int]]:
        return self.repository.execute(top_n=top_n)
