import logging
from services.territoryService import TerritoryService
from services.chartService import create_chart

def dimension(id: int, chartPath: str):
    try:
        
        territory = TerritoryService().get_territory(id)        
        if not territory:
            logging.info(f"Territory with ID {id} could not be found in the database or fetched from the API.")
            return None
        print(f"Name: {territory.name}")
        print(f"Dimension: {territory.dimension}km2")
        print(f"Bar chart: {chartPath}")
        create_chart([territory], chartPath)        

    except Exception as error:
        logging.error(f"An unexpected error occurred: {error}")
    return None
