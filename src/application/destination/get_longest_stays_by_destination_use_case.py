from typing import Dict
from domain.model.destination.gateways.get_longest_stays_by_destination import GetLongestStaysByDestination

class GetLongestStaysByDestinationUseCase:
    def __init__(self, repository: GetLongestStaysByDestination):
        self.repository = repository

    def execute(self) -> Dict[str, float]:
        return self.repository.execute()
