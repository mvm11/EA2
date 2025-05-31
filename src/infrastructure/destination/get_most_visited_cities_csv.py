import os
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict
from domain.model.destination.gateways.get_most_visited_cities import GetMostVisitedCities

class GetMostVisitedCitiesCSV(GetMostVisitedCities):
    def __init__(self, csv_path: str, output_dir: str = None):
        self.csv_path = csv_path
        self.output_dir = output_dir or os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs')

    def execute(self) -> Dict[str, int]:
        df = pd.read_csv(self.csv_path)
        city_counts = df['ciudad'].value_counts().head(10)

        self._generate_chart(city_counts)

        return city_counts.to_dict()

    def _generate_chart(self, city_counts: pd.Series):
        plt.figure(figsize=(10, 5))
        bars = plt.bar(city_counts.index, city_counts.values, color='seagreen')
        plt.title('Most Visited Cities')
        plt.xlabel('Ciudad')
        plt.ylabel('Cantidad de Visitas')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, f'{int(yval)}', ha='center', va='bottom')

        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, 'most_visited_cities.png')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        print(f"[✓] Chart saved to: {output_path}")
