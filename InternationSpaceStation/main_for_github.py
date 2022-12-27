import smtplib

import requests
from datetime import datetime
import time

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


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
my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

while True:

    # If the ISS is close to my current position
    # and it is currently dark
    if -5 < iss_longitude-MY_LONG < 5 and -5 < iss_latitude - MY_LAT < 5 and time_now.hour > 17:
        print("Look up")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="jameshyh88@gmail.com",
                msg=f"Subject: THE ISS IS NEAR YOU!!!\n\nLOOK UP"
            )
    else:
        print("Not near")
    time.sleep(60)

# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
