from abc import ABC, abstractmethod

class GetRatingBoxplotByCountry(ABC):
    @abstractmethod
    def generate_plot(self) -> None:
        pass
