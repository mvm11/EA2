import os
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict
from domain.model.destination.gateways.get_average_stay_by_city import GetAverageStayByCity

class GetAverageStayByCityCSV(GetAverageStayByCity):
    def __init__(self, csv_path: str, output_dir: str = None):
        self.csv_path = csv_path
        self.output_dir = output_dir or os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs')

    def execute(self) -> Dict[str, float]:
        df = pd.read_csv(self.csv_path)
        avg_stay = df.groupby('ciudad')['duracion_estancia'].mean().round(2).sort_values(ascending=False)

        self._generate_chart(avg_stay)

        return avg_stay.to_dict()

    def _generate_chart(self, avg_stay: pd.Series):
        top_cities = avg_stay.head(10)
        plt.figure(figsize=(12, 6))
        bars = plt.bar(top_cities.index, top_cities.values, color='steelblue')
        plt.title("Duración Promedio de Estancia por Ciudad", fontsize=14)
        plt.ylabel("Días promedio")
        plt.xticks(rotation=45, ha='right')

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval:.1f}', ha='center', va='bottom')

        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, 'average_stay_by_city.png')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        print(f"[✓] Chart saved to: {output_path}")
