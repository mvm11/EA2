import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple
from domain.model.destination.gateways.get_most_visited_cities import GetMostVisitedCities

class GetMostVisitedCitiesCSV(GetMostVisitedCities):
    def __init__(self, csv_path: str, output_dir: str = None):
        self.csv_path = csv_path
        self.output_dir = output_dir or os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs')

    def execute(self, top_n: int = 10) -> List[Tuple[str, int]]:
        df = pd.read_csv(self.csv_path)
        city_counts = df['ciudad'].value_counts().nlargest(top_n)

        self._generate_visualization(city_counts)
        return list(city_counts.items())

    def _generate_visualization(self, city_counts: pd.Series):
        os.makedirs(self.output_dir, exist_ok=True)

        plt.figure(figsize=(10, 6))
        sns.barplot(x=city_counts.values, y=city_counts.index, hue=city_counts.index, palette="crest", legend=False)
        plt.title("Top Visited Cities")
        plt.xlabel("Number of Visits")
        plt.ylabel("City")
        plt.grid(axis='x')

        output_path = os.path.join(self.output_dir, 'most_visited_cities.png')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        print(f"[✓] Chart saved to: {output_path}")
