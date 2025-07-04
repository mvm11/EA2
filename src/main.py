import os

from application.destination.get_longest_stays_by_destination_use_case import GetLongestStaysByDestinationUseCase
from application.satisfaction.get_average_rating_by_country_use_case import GetAverageRatingByCountryUseCase
from domain.model.accommodation.gateways.get_expense_boxplot_by_accommodation_type import GetExpenseBoxplotByAccommodationType
from infrastructure.satisfaction.get_average_rating_by_country_csv import GetAverageRatingByCountryCSV

from application.destination.get_average_stay_by_city_use_case import GetAverageStayByCityUseCase
from infrastructure.destination.get_average_stay_by_city_csv import GetAverageStayByCityCSV

from application.destination.get_most_visited_cities_use_case import GetMostVisitedCitiesUseCase
from infrastructure.destination.get_most_visited_cities_csv import GetMostVisitedCitiesCSV

from infrastructure.destination.get_longest_stays_by_destination_csv import GetLongestStaysByDestinationCSV

from application.trip.get_travel_geo_distribution_use_case import GetTravelGeoDistributionUseCase
from infrastructure.trip.get_travel_geo_distribution_csv import GetTravelGeoDistributionCSV

from application.trip.get_most_popular_months_use_case import GetMostPopularMonthsUseCase
from infrastructure.trip.get_most_popular_months_csv import GetMostPopularMonthsCSV

from application.accommodation.get_average_expense_by_accommodation_use_case import GetAverageExpenseByAccommodationUseCase
from infrastructure.accommodation.get_average_expense_by_accommodation_csv import GetAverageExpenseByAccommodationCSV

from application.accommodation.get_average_rating_by_accommodation_use_case import GetAverageRatingByAccommodationUseCase
from infrastructure.accommodation.get_average_rating_by_accommodation_csv import GetAverageRatingByAccommodationCSV

from application.accommodation.get_expense_boxplot_by_accommodation_type_use_case import GetExpenseBoxplotByAccommodationTypeUseCase
from infrastructure.accommodation.get_expense_boxplot_by_accommodation_type_csv import GetExpenseBoxplotByAccommodationTypeCSV

from application.satisfaction.get_rating_boxplot_by_country_use_case import GetRatingBoxplotByCountryUseCase
from infrastructure.satisfaction.get_rating_boxplot_by_country_csv import GetRatingBoxplotByCountryCSV

from application.satisfaction.get_rating_boxplot_by_country_use_case import GetRatingBoxplotByCountryUseCase
from infrastructure.satisfaction.get_rating_boxplot_by_country_csv import GetRatingBoxplotByCountryCSV



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

    # --- Ciudades más visitadas ---
    visited_repo = GetMostVisitedCitiesCSV(csv_path=dataset_path, output_dir=output_dir)
    visited_use_case = GetMostVisitedCitiesUseCase(visited_repo)
    visited_cities = visited_use_case.execute()
    print("\n=== Most Visited Cities ===")
    for city, count in visited_cities:
        print(f"{city}: {count} visitas")

    # --- Gasto diario por tipo de alojamiento ---
    expense_repo = GetAverageExpenseByAccommodationCSV(csv_path=dataset_path, output_dir=output_dir)
    expense_use_case = GetAverageExpenseByAccommodationUseCase(expense_repo)
    average_expenses = expense_use_case.execute()
    print("\n=== Average Daily Expense by Accommodation Type ===")
    for acc_type, expense in average_expenses.items():
        print(f"{acc_type}: ${expense:.2f}")

    # --- Valoración promedio por tipo de alojamiento ---
    rating_repo = GetAverageRatingByAccommodationCSV(csv_path=dataset_path, output_dir=output_dir)
    rating_use_case = GetAverageRatingByAccommodationUseCase(rating_repo)
    avg_ratings_accommodation = rating_use_case.execute()
    print("\n=== Average Rating by Accommodation Type ===")
    for acc_type, rating in avg_ratings_accommodation.items():
        print(f"{acc_type}: {rating}/5")

    # --- Destinos con estancias más largas en promedio ---
    longest_repo = GetLongestStaysByDestinationCSV(csv_path=dataset_path, output_dir=output_dir)
    longest_use_case = GetLongestStaysByDestinationUseCase(longest_repo)
    longest_stays = longest_use_case.execute()
    print("\n=== Longest Average Stays by Country ===")
    for country, days in longest_stays.items():
        print(f"{country}: {days} days")

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

    # --- Boxplot: Gasto diario por tipo de alojamiento ---
    expense_boxplot_repo = GetExpenseBoxplotByAccommodationTypeCSV(csv_path=dataset_path, output_dir=output_dir)
    expense_boxplot_use_case = GetExpenseBoxplotByAccommodationTypeUseCase(expense_boxplot_repo)
    expense_boxplot_use_case.execute()

    # --- Boxplot de valoraciones por país ---
    rating_boxplot_repo = GetRatingBoxplotByCountryCSV(csv_path=dataset_path, output_dir=output_dir)
    rating_boxplot_use_case = GetRatingBoxplotByCountryUseCase(rating_boxplot_repo)
    rating_boxplot_use_case.execute()   


if __name__ == '__main__':
    main()
