import requests
from datetime import datetime
import os

# Constants for exercise data.
APP_ID = os.environ.get("APP_ID", "Please specify an APP_ID.")
API_KEY = os.environ.get("API_KEY", "Please specify an API_KEY.")
NUTRIONIX_ENDPOINT = "https://trackapi.nutritionix.com"
EXERCISE_ENDPOINT = f"{NUTRIONIX_ENDPOINT}/v2/natural/exercise/"

# Constants for Sheety.
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "Please specify a SHEETY_ENDPOINT")
TOKEN = os.environ.get("TOKEN", "Please specify an authorization TOKEN.")

# Header for exercise data.
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Parameters for exercise data.
query = input("What kind of exercise did you do today, and for how long/what distance?: ")

json_parameters = {
    "query": query
}

# Request for exercise data.
response = requests.post(EXERCISE_ENDPOINT, headers=header, json=json_parameters)
response.raise_for_status()
data = response.json()

# Parameters for Sheety.
try:
    count = 0
    for workout in data["exercises"]:
        date = str(datetime.now().strftime("%m/%d/%Y"))
        time = str(datetime.now().strftime("%I:%M:%S %p"))
        exercise = str(data["exercises"][count]["name"]).title()
        duration = str(data["exercises"][count]["duration_min"]) + " minutes"
        calories = str(data["exercises"][count]["nf_calories"]) + " cal"

        row_contents = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }
        }

        sheety_header = {
            "Authorization": TOKEN
        }

        # Post data to the sheet.
        data_response = requests.post(url=SHEETY_ENDPOINT, json=row_contents, headers=sheety_header)
        data_response.raise_for_status()

        count += 1
except:
    print("Something went wrong. Please try again.")
else:
    print("Workout(s) logged successfully.")
