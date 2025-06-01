from domain.model.satisfaction.gateways.get_rating_boxplot_by_country import GetRatingBoxplotByCountry

class GetRatingBoxplotByCountryUseCase:
    def __init__(self, repo: GetRatingBoxplotByCountry):
        self.repo = repo

    def execute(self) -> None:
        self.repo.generate_plot()
