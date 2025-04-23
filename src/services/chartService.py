import matplotlib.pyplot as plt
import logging
from typing import List
from services.territoryService import Territory

def create_chart(territories: List[Territory], chart_path:str):
    try:

        territoriesNames = []
        territoriesDimensions = []
        for territory in territories:
            territoriesDimensions.append(territory.dimension)
            territoriesNames.append(territory.name)

        plt.bar(territoriesNames, territoriesDimensions)

        plt.title(f"{chart_path}")
        plt.xlabel('territories')
        plt.ylabel('dimensions')
        file_name = chart_path if chart_path.endswith(".png") else f"{chart_path}.png"
        plt.savefig(file_name, format="png")
        logging.info(f"Chart {chart_path} has been successfully created.")
    except Exception as error:
        logging.error(f"An unexpected error occurred while creating the chart {chart_path}: {error}")
        return
