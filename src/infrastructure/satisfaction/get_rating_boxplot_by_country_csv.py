import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

from domain.model.satisfaction.gateways.get_rating_boxplot_by_country import GetRatingBoxplotByCountry

class GetRatingBoxplotByCountryCSV(GetRatingBoxplotByCountry):
    def __init__(self, csv_path: str, output_dir: str):
        self.csv_path = csv_path
        self.output_dir = output_dir

    def generate_plot(self) -> None:
        df = pd.read_csv(self.csv_path)
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df, x='pais', y='valoracion')
        plt.xticks(rotation=45)
        plt.title("Boxplot of Ratings by Country")
        plt.xlabel("Country")
        plt.ylabel("Rating")
        output_path = os.path.join(self.output_dir, "boxplot_rating_by_country.png")
        plt.tight_layout()
        plt.savefig(output_path)
        print(f"[✓] Chart saved to: {output_path}")
