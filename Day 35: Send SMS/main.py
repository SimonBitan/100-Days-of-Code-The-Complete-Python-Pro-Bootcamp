import requests
from twilio.rest import Client

account_sid = 'Your twilio account sid'
auth_token = 'Your twilio account auth token'

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "Your OWM API Key"

# Latitude and Longitude for Timmins, Canada.
weather_params = {
    "lat": 48.476109,
    "lon": -81.328331,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

rain_check_list = []
count = 0
for _ in range(0, 4):
    rain_check_list.append(weather_data["list"][count]["weather"][0]["id"])
    count += 1

for code in rain_check_list:
    if code < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella!",
            from_="your twilio free number",
            to='your verified twilio phone number'
        )
        print(message.status)
        break


