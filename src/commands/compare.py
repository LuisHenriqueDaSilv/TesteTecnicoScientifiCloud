import logging

from services.territoryService import TerritoryService
from services.chartService import create_chart

def compare(id1: int,id2:int, chart_path: str):
    try:
        territory1 = TerritoryService.get_territory(id1)
        if not territory1:
            logging.info(f"Territory with ID {id1} could not be found in the database or fetched from the API.")
            return None
        
        territory2 = TerritoryService.get_territory(id2)
        if not territory2:
            logging.info(f"Territory with ID {id2} could not be found in the database or fetched from the API.")
            return None
        
        print(f"{territory1.name}: {territory1.dimension}km2")
        print(f"{territory2.name}: {territory2.dimension}km2")
        difference = round(max(territory2.dimension, territory1.dimension) - min(territory2.dimension, territory1.dimension), 3)
        print(f"Difference: {difference}km2")
        print(f"Bar chart: {chart_path}")
        create_chart([territory1, territory2], chart_path)

    except Exception as error:
        logging.error(f"An unexpected error occurred in command: {error}")
    return None