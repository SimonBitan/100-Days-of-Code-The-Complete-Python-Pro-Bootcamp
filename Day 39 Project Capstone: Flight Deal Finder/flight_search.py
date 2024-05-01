import requests
import os
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_SEARCH_API_KEY = os.getenv("FLIGHT_SEARCH_API_KEY")

HEADER = {
    "Content-Type": "application/json",
    "apikey": FLIGHT_SEARCH_API_KEY,
    "Content-Encoding": "gzip"
}

CITY_LIST = ["Paris", "Berlin", "Tokyo", "Sydney", "Istanbul", "Kuala Lumpur", "New York", "San Francisco", "Cape Town"]

# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def __init__(self):
        self.code = {}

    def get_iata_code(self):

        iata_code_list = []

        for city in CITY_LIST:
            params = {
                "term": city,
                "location_types": "city"
            }
            response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=HEADER, params=params)
            data = response.json()
            iata_code = data["locations"][0]["code"]
            iata_code_list.append(iata_code)

        return iata_code_list