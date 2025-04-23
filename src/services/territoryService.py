import json
import requests
import logging
from typing import NamedTuple
import pandas as pd

from db import dbConnection, dbCursor

class Territory(NamedTuple):
    name: str
    id: int
    dimension: float

class TerritoryService():
    @staticmethod
    def fetch_in_db(id:int) -> Territory | None:
        result = dbCursor.execute("SELECT nome, id, dimensao FROM territorios WHERE id = ?", (id,)).fetchone()
        if result:
            name, tid, dimension = result
            return Territory(name=name, id=tid, dimension=float(dimension))
        else: return None
    
    @staticmethod
    def fetch_name_by_id(target_id: int) -> str|None:
        try:            
            csv_path = "data/dict.csv"
            csv_data = pd.read_csv(csv_path, delimiter=",", dtype=str)
            match = csv_data[csv_data["id"] == str(target_id)]

            if not match.empty:
                return match.iloc[0]["nome"]
            else:
                logging.warning(f"No match found for ID: {target_id}")
                return None
        except Exception as error:
            logging.error(f"Error reading CSV file: {error}") 
        return None
        
    @staticmethod
    def fetch_in_api(id:int) -> Territory | None:
        try:
            url = f"https://servicodados.ibge.gov.br/api/v3/malhas/estados/{id}/metadados"
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                logging.error(
                    f"Failed to fetch the state from the API. Returned status code: {response.status_code}"
                )
                return None

            try:
                response_data = response.json()[0]
            except (json.JSONDecodeError, IndexError, TypeError) as e:
                logging.error(f"Failed to parse API response: {e}")
                return None
            
            dimension = response_data.get("area", {}).get("dimensao")
            fetched_id = response_data.get("id")
            name = TerritoryService.fetch_name_by_id(id)

            if not dimension or id != fetched_id:
                logging.error(
                    f"The API returned inconsistent results for the search with ID: {id}"
                )
                return None
            return Territory(name=name,id=fetched_id, dimension=dimension)
        
        except requests.RequestException as e:
            logging.error(f"Network error during API request: {e}")
        except Exception as error:
            logging.error(f"An unexpected error occurred: {error}")
        
        return None

    @staticmethod
    def save_in_db(territory:Territory) -> bool:
        try:
            dbCursor.execute("""
                            INSERT INTO territorios 
                            VALUES (?, ?, ?)
            """,  (territory.id, territory.name, territory.dimension))
            dbConnection.commit()
            return True
        except Exception as error:
            logging.error(f"An unexpected error occurred while saving to the database: {error}")
        return False
    
    @staticmethod
    def get_territory(id: int) -> Territory| None:
        territory = TerritoryService().fetch_in_db(id)
        if not territory: 
            territory = TerritoryService.fetch_in_api(id)
            if not territory:
                return None
            
            saved_in_db= TerritoryService.save_in_db(territory)
            if not saved_in_db:
                logging.warning(f"Failed to save territory with ID {territory[0]} to the database.")

        return territory