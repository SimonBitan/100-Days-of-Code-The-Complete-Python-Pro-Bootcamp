import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
# your email
MY_EMAIL = "example@email.com"
# the app password for your email (configure online)
PASSWORD = "abcd1234()"
# Email to send to.
SEND_EMAIL = "example2@gmail.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

current_hour = time_now.hour

# If the ISS is close to my current position
# ,and it is currently dark,
# then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5 and (current_hour > sunset or current_hour < sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=SEND_EMAIL,
                                msg=f"Subject: Look Up\n\nThe ISS is above you!"
                                )
        print(f"Email sent from {MY_EMAIL} to {SEND_EMAIL}.")
    else:
        print("The ISS is not currently above and/or it's too bright to see it.")
    time.sleep(60)



