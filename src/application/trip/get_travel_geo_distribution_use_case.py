from domain.model.trip.gateways.get_travel_geo_distribution import GetTravelGeoDistribution

class GetTravelGeoDistributionUseCase:
    def __init__(self, service: GetTravelGeoDistribution):
        self.service = service

    def execute(self):
        return self.service.execute()
