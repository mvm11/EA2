from typing import Dict
from domain.model.accommodation.gateways.get_average_rating_by_accommodation import GetAverageRatingByAccommodation

class GetAverageRatingByAccommodationUseCase:
    def __init__(self, repository: GetAverageRatingByAccommodation):
        self.repository = repository

    def execute(self) -> Dict[str, float]:
        return self.repository.execute()
