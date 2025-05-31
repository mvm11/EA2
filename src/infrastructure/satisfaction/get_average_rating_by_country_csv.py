import os
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict
from domain.model.satisfaction.gateways.get_average_rating_by_country import GetAverageRatingByCountry

class GetAverageRatingByCountryCSV(GetAverageRatingByCountry):
    def __init__(self, csv_path: str, output_dir: str = "docs"):
        self.csv_path = csv_path
        self.output_dir = os.path.abspath(output_dir)
        os.makedirs(self.output_dir, exist_ok=True)

    def execute(self) -> Dict[str, float]:
        df = pd.read_csv(self.csv_path)
        avg_ratings = df.groupby('pais')['valoracion'].mean().round(2)

        # Visualización
        plt.figure(figsize=(10, 6))
        avg_ratings.sort_values().plot(kind='barh', color='mediumseagreen')
        plt.title('Average Rating by Country')
        plt.xlabel('Average Rating (1-5)')
        plt.xlim(0, 5)
        plt.grid(axis='x', linestyle='--', alpha=0.5)
        plt.tight_layout()

        output_path = os.path.join(self.output_dir, 'average_rating_by_country.png')
        plt.savefig(output_path)
        print(f"[✓] Chart saved to: {output_path}")
        plt.close()

        return avg_ratings.to_dict()
