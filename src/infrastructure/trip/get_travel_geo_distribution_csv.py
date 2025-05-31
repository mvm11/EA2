import os
import pandas as pd
import plotly.express as px
from domain.model.trip.gateways.get_travel_geo_distribution import GetTravelGeoDistribution

class GetTravelGeoDistributionCSV(GetTravelGeoDistribution):
    def __init__(self, csv_path: str, output_dir: str = None):
        self.csv_path = csv_path
        self.output_dir = output_dir or os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs')

    def execute(self):
        df = pd.read_csv(self.csv_path)

        fig = px.scatter_mapbox(
            df,
            lat='latitud',
            lon='longitud',
            color='pais',
            size='duracion_estancia',
            hover_name='ciudad',
            hover_data={'pais': True, 'duracion_estancia': True, 'gasto_diario': True},
            zoom=2,
            height=600
        )

        fig.update_layout(
            mapbox_style='open-street-map',
            title='Travel Geo Distribution',
            title_x=0.5,
            margin=dict(l=0, r=0, t=40, b=0)
        )

        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, 'geo_distribution_map.html')
        fig.write_html(output_path)
        print(f"[✓] Interactive map saved to: {output_path}")
