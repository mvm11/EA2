import os
import pandas as pd
import matplotlib.pyplot as plt
from domain.model.trip.gateways.get_most_popular_months import GetMostPopularMonths
from typing import Dict

class GetMostPopularMonthsCSV(GetMostPopularMonths):
    def __init__(self, csv_path: str, output_dir: str = None):
        self.csv_path = csv_path
        self.output_dir = output_dir or os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs')

    def execute(self) -> Dict[str, int]:
        df = pd.read_csv(self.csv_path, parse_dates=['fecha'])

        df['mes'] = df['fecha'].dt.month
        month_counts = df['mes'].value_counts().sort_index()

        # Mapear número a nombre del mes
        month_names = {
            1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
            5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
            9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
        }
        month_counts.index = month_counts.index.map(month_names)

        self._generate_chart(month_counts)

        return month_counts.to_dict()

    def _generate_chart(self, month_counts: pd.Series):
        plt.figure(figsize=(10, 5))
        bars = plt.bar(month_counts.index, month_counts.values, color='tomato')
        plt.title('Most Popular Travel Months')
        plt.xlabel('Mes')
        plt.ylabel('Cantidad de Viajes')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, f'{int(yval)}', ha='center', va='bottom')

        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, 'most_popular_months.png')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        print(f"[✓] Chart saved to: {output_path}")
