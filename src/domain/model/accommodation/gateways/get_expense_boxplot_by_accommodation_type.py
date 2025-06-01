from abc import ABC, abstractmethod

class GetExpenseBoxplotByAccommodationType(ABC):
    @abstractmethod
    def execute(self) -> None:
        """Generates and saves a boxplot showing the daily expense distribution by accommodation type."""
        pass
