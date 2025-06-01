import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

from domain.model.accommodation.gateways.get_expense_boxplot_by_accommodation_type import GetExpenseBoxplotByAccommodationType

class GetExpenseBoxplotByAccommodationTypeCSV(GetExpenseBoxplotByAccommodationType):
    def __init__(self, csv_path: str, output_dir: str):
        self.csv_path = csv_path
        self.output_dir = output_dir

    def execute(self) -> None:
        df = pd.read_csv(self.csv_path)

        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x='tipo_alojamiento', y='gasto_diario', palette="Set2")
        plt.title('Daily Expense Distribution by Accommodation Type')
        plt.xlabel('Accommodation Type')
        plt.ylabel('Daily Expense')
        plt.xticks(rotation=45)
        plt.tight_layout()

        output_path = os.path.join(self.output_dir, 'expense_boxplot_by_accommodation_type.png')
        plt.savefig(output_path)
        print(f"[✓] Chart saved to: {output_path}")
