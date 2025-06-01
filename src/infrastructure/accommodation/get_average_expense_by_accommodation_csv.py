import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict
from domain.model.accommodation.gateways.get_average_expense_by_accommodation import GetAverageExpenseByAccommodation

class GetAverageExpenseByAccommodationCSV(GetAverageExpenseByAccommodation):
    def __init__(self, csv_path: str, output_dir: str = None):
        self.csv_path = csv_path
        self.output_dir = output_dir or os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs')

    def execute(self) -> Dict[str, float]:
        df = pd.read_csv(self.csv_path)
        avg_expense = df.groupby('tipo_alojamiento')['gasto_diario'].mean().round(2).sort_values(ascending=False)

        self._generate_chart(avg_expense)
        return avg_expense.to_dict()

    def _generate_chart(self, avg_expense: pd.Series):
        os.makedirs(self.output_dir, exist_ok=True)

        plt.figure(figsize=(8, 6))
        sns.boxplot(data=avg_expense.to_frame().T, orient='h')
        sns.stripplot(x=avg_expense.values, y=avg_expense.index, color='black', size=8)
        plt.title("Average Daily Expense by Accommodation Type")
        plt.xlabel("Average Expense (USD)")
        plt.ylabel("Accommodation Type")

        output_path = os.path.join(self.output_dir, 'average_expense_by_accommodation.png')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        print(f"[✓] Chart saved to: {output_path}")
