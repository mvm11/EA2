from domain.model.accommodation.gateways.get_expense_boxplot_by_accommodation_type import GetExpenseBoxplotByAccommodationType

class GetExpenseBoxplotByAccommodationTypeUseCase:
    def __init__(self, repository: GetExpenseBoxplotByAccommodationType):
        self.repository = repository

    def execute(self) -> None:
        self.repository.execute()
