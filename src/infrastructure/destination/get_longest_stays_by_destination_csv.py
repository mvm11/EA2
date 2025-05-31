import os
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict
from domain.model.destination.gateways.get_longest_stays_by_destination import GetLongestStaysByDestination

class GetLongestStaysByDestinationCSV(GetLongestStaysByDestination):
    def __init__(self, csv_path: str, output_dir: str = None):
        self.csv_path = csv_path
        self.output_dir = output_dir or os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs')

    def execute(self) -> Dict[str, float]:
        df = pd.read_csv(self.csv_path)
        avg_stay = df.groupby('pais')['duracion_estancia'].mean().round(2).sort_values(ascending=False).head(10)

        self._generate_chart(avg_stay)
        return avg_stay.to_dict()

    def _generate_chart(self, avg_stay: pd.Series):
        plt.figure(figsize=(10, 5))
        bars = plt.bar(avg_stay.index, avg_stay.values, color='purple')
        plt.title('Top Countries by Average Stay Duration')
        plt.xlabel('País')
        plt.ylabel('Duración Promedio (días)')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, f'{yval:.2f}', ha='center', va='bottom')

        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, 'longest_stays_by_country.png')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        print(f"[✓] Chart saved to: {output_path}")
