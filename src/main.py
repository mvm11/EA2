import os

from application.satisfaction.get_average_rating_by_country_use_case import GetAverageRatingByCountryUseCase
from infrastructure.satisfaction.get_average_rating_by_country_csv import GetAverageRatingByCountryCSV

from application.destination.get_average_stay_by_city_use_case import GetAverageStayByCityUseCase
from infrastructure.destination.get_average_stay_by_city_csv import GetAverageStayByCityCSV

from application.trip.get_travel_geo_distribution_use_case import GetTravelGeoDistributionUseCase
from infrastructure.trip.get_travel_geo_distribution_csv import GetTravelGeoDistributionCSV

from application.trip.get_most_popular_months_use_case import GetMostPopularMonthsUseCase
from infrastructure.trip.get_most_popular_months_csv import GetMostPopularMonthsCSV

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(base_path, '..', 'data', 'dataset.csv')
    output_dir = os.path.join(base_path, '..', 'docs')

    # --- Satisfacción promedio por país ---
    satisfaction_repo = GetAverageRatingByCountryCSV(csv_path=dataset_path, output_dir=output_dir)
    satisfaction_use_case = GetAverageRatingByCountryUseCase(satisfaction_repo)
    average_ratings = satisfaction_use_case.execute()

    print("\n=== Average Rating by Country ===")
    for country, rating in average_ratings.items():
        print(f"{country}: {rating}/5")

    # --- Estancia promedio por ciudad ---
    stay_repo = GetAverageStayByCityCSV(csv_path=dataset_path, output_dir=output_dir)
    stay_use_case = GetAverageStayByCityUseCase(stay_repo)
    average_stays = stay_use_case.execute()

    print("\n=== Average Stay Duration by City ===")
    for city, days in average_stays.items():
        print(f"{city}: {days} days")

    # --- Mapa interactivo de viajes ---
    travel_map_repo = GetTravelGeoDistributionCSV(csv_path=dataset_path, output_dir=output_dir)
    travel_map_use_case = GetTravelGeoDistributionUseCase(travel_map_repo)
    travel_map_use_case.execute()

    # --- Meses más populares para viajar ---
    months_repo = GetMostPopularMonthsCSV(csv_path=dataset_path, output_dir=output_dir)
    months_use_case = GetMostPopularMonthsUseCase(months_repo)
    month_counts = months_use_case.execute()

    print("\n=== Most Popular Travel Months ===")
    for month, count in month_counts.items():
        print(f"{month}: {count} viajes")

if __name__ == '__main__':
    main()
