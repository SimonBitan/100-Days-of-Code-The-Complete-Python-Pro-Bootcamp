import os
from twilio.rest import Client
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


# TWILIO authentication.
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Twilio phone number to send from, and your authenticated phone number.
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:

    def __init__(self):
        self.code = {}

    def send_text(self, price, origin_city, origin_airport, dest_city, dest_airport, arrival_date, return_date):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages \
            .create(
                body=f"Low price alert! Only £{price} to fly from {origin_city}-{origin_airport} "
                     f"to {dest_city}-{dest_airport}, from {arrival_date} to {return_date}.",
                from_=f'{TWILIO_PHONE_NUMBER}',
                to=f'{PHONE_NUMBER}'
            )
