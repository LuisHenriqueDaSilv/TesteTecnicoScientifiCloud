import matplotlib.pyplot as plt
import logging
from typing import List
from services.territoryService import Territory

def create_chart(territories: List[Territory], chart_path:str):
    if not territories:
        logging.warning("No territories provided to create the chart.")
        return
    try:

        territoriesNames = [territory.name for territory in territories]
        territoriesDimensions = [territory.dimension for territory in territories]

        plt.bar(territoriesNames, territoriesDimensions)

        plt.title(" x ".join(territoriesNames))
        plt.xlabel('territories')
        plt.ylabel('dimensions')
        plt.yticks(territoriesDimensions)

        file_name = f"{chart_path if chart_path.endswith('.png') else chart_path + '.png'}"
        plt.savefig(file_name, format="png")

        logging.info(f"Chart {chart_path} has been successfully created.")
    except Exception as error:
        logging.error(f"An unexpected error occurred while creating the chart {chart_path}: {error}")
        return
