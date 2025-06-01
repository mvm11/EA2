import os
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict
from domain.model.accommodation.gateways.get_average_rating_by_accommodation import GetAverageRatingByAccommodation

class GetAverageRatingByAccommodationCSV(GetAverageRatingByAccommodation):
    def __init__(self, csv_path: str, output_dir: str = None):
        self.csv_path = csv_path
        self.output_dir = output_dir or os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs')

    def execute(self) -> Dict[str, float]:
        df = pd.read_csv(self.csv_path)
        avg_rating = df.groupby('tipo_alojamiento')['valoracion'].mean().round(2).sort_values(ascending=False)

        self._generate_chart(avg_rating)
        return avg_rating.to_dict()

    def _generate_chart(self, avg_rating: pd.Series):
        plt.figure(figsize=(10, 5))
        bars = plt.bar(avg_rating.index, avg_rating.values, color='mediumseagreen')
        plt.title('Average Rating by Accommodation Type')
        plt.xlabel('Tipo de Alojamiento')
        plt.ylabel('Valoración Promedio')
        plt.ylim(0, 5)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval:.2f}', ha='center', va='bottom')

        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, 'average_rating_by_accommodation.png')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        print(f"[✓] Chart saved to: {output_path}")
