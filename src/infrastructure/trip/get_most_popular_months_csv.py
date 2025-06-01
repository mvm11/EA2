import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict
from domain.model.trip.gateways.get_most_popular_months import GetMostPopularMonths

class GetMostPopularMonthsCSV(GetMostPopularMonths):
    def __init__(self, csv_path: str, output_dir: str = None):
        self.csv_path = csv_path
        self.output_dir = output_dir or os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs')

    def execute(self) -> Dict[str, Dict[str, float]]:
        df = pd.read_csv(self.csv_path)

        # Convertir fechas a datetime y extraer mes
        df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
        df = df.dropna(subset=['fecha'])
        df['mes'] = df['fecha'].dt.month_name()

        viajes_por_mes = df['mes'].value_counts().sort_index()
        duracion_por_mes = df.groupby('mes')['duracion_estancia'].mean().round(2)
        gasto_por_mes = df.groupby('mes')['gasto_diario'].mean().round(2)
        valoracion_por_mes = df.groupby('mes')['valoracion'].mean().round(2)

        self._generate_dashboard(viajes_por_mes, duracion_por_mes, gasto_por_mes, valoracion_por_mes)

        return {
            'viajes_por_mes': viajes_por_mes.to_dict(),
            'duracion_promedio_por_mes': duracion_por_mes.to_dict(),
            'gasto_diario_promedio_por_mes': gasto_por_mes.to_dict(),
            'valoracion_promedio_por_mes': valoracion_por_mes.to_dict()
        }

    def _generate_dashboard(self, viajes, duracion, gasto, valoracion):
        os.makedirs(self.output_dir, exist_ok=True)
        fig, axs = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle("Monthly Travel Patterns", fontsize=16)

        sns.barplot(x=list(viajes.index), y=viajes.values, ax=axs[0, 0])
        axs[0, 0].set_title("Number of Trips per Month")
        axs[0, 0].tick_params(axis='x', rotation=45)

        sns.lineplot(x=list(duracion.index), y=duracion.values, ax=axs[0, 1], marker="o")
        axs[0, 1].set_title("Average Stay Duration")

        sns.lineplot(x=list(gasto.index), y=gasto.values, ax=axs[1, 0], marker="s", color='green')
        axs[1, 0].set_title("Average Daily Expense")

        sns.lineplot(x=list(valoracion.index), y=valoracion.values, ax=axs[1, 1], marker="^", color='orange')
        axs[1, 1].set_title("Average Rating")

        for ax in axs.flat:
            ax.grid(True)

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        output_path = os.path.join(self.output_dir, 'most_popular_months.png')
        plt.savefig(output_path)
        plt.close()
        print(f"[✓] Dashboard saved to: {output_path}")
