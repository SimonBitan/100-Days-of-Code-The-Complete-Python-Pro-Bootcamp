import os
import requests
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


SHEETY_ENDPOINT = "https://api.sheety.co/577b178ca3a49f03e15fec03e78e7437/flightDeals/prices"
TOKEN = os.getenv("TOKEN")

SHEETY_HEADERS = {
        "Authorization": TOKEN
    }


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        self.response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        self.response.raise_for_status()
        self.data = self.response.json()

    def __getitem__(self, key):
        return self.data[key]

    def update_iata_codes(self, iata_code, row_id):
        put_response = requests.put(url=SHEETY_ENDPOINT + f"/{row_id}", headers=SHEETY_HEADERS, json=iata_code)
        put_response.raise_for_status()

    def update_lowest_price(self, lowest_price, row_id):
        put_response = requests.put(url=SHEETY_ENDPOINT + f"/{row_id}", headers=SHEETY_HEADERS, json=lowest_price)
        put_response.raise_for_status()

