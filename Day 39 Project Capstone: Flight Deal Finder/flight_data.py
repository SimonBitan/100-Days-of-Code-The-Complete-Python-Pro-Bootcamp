import requests
import os
from datetime import datetime, timedelta
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
FLIGHT_SEARCH_API_KEY = os.getenv("FLIGHT_SEARCH_API_KEY")

HEADER = {
    "Content-Type": "application/json",
    "apikey": FLIGHT_SEARCH_API_KEY,
    "Content-Encoding": "gzip"
}



# This class is responsible for structuring the flight data.
class FlightData:

    def __init__(self):
        self.code = {}

    def get_flight_price(self, params):
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=HEADER, params=params)
        response.raise_for_status()

        lowest_price = float('inf')
        flight_number = None

        # Search for lowest price flight.
        for index, flight in enumerate(response.json()["data"]):
            price = flight["price"]
            if price < lowest_price:
                lowest_price = price
                flight_number = index

        city = response.json()["data"][0]["cityTo"]
        print(f"{city}: £{lowest_price}")
        return [lowest_price, flight_number]

    def get_flight_data(self, params, flight_number):
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=HEADER, params=params)
        response.raise_for_status()
        origin_city = response.json()["data"][flight_number]["cityFrom"]
        origin_airport = response.json()["data"][flight_number]["flyFrom"]
        dest_city = response.json()["data"][flight_number]["cityTo"]
        dest_airport = response.json()["data"][flight_number]["flyTo"]

        # Calculate the return date. This will involve converting the arrival_date to a datetime object, then back into a string.
        arrival_date_str = response.json()["data"][flight_number]["local_arrival"].split("T")[0]
        arrival_date = datetime.strptime(arrival_date_str, "%Y-%m-%d")
        return_date = (arrival_date + timedelta(days=response.json()["data"][flight_number]["nightsInDest"])).strftime("%d/%m/%Y")
        arrival_date = arrival_date.strftime("%d/%m/%Y")
        data = [origin_city, origin_airport, dest_city, dest_airport, arrival_date, return_date]
        return data

