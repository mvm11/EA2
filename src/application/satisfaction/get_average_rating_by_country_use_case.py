from typing import Dict

from domain.model.satisfaction.gateways.get_average_rating_by_country import GetAverageRatingByCountry

class GetAverageRatingByCountryUseCase:
    def __init__(self, rating_service: GetAverageRatingByCountry):
        self._rating_service = rating_service

    def execute(self) -> Dict[str, float]:
        return self._rating_service.execute()
