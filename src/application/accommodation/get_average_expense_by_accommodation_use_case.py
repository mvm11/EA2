from typing import Dict
from domain.model.accommodation.gateways.get_average_expense_by_accommodation import GetAverageExpenseByAccommodation

class GetAverageExpenseByAccommodationUseCase:
    def __init__(self, repository: GetAverageExpenseByAccommodation):
        self.repository = repository

    def execute(self) -> Dict[str, float]:
        return self.repository.execute()
