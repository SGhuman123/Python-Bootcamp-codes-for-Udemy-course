import requests
from twilio.rest import Client

weather_params = {
    "lat": "YOUR LATITUDE",
    "lon": "YOUR LONGITUDE",
    "appid": "OWM_API_KEY",
    "exclude": "current,minutely,daily"
}
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_data = requests.get(url=OWM_Endpoint, params=weather_params)
account_sid = "YOUR ACCOUNT SID"
auth_token = "AUTH_TOKEN"

# print(weather_data.status_code)
weather_data.raise_for_status()
finalised_weather_data = weather_data.json()
print(finalised_weather_data["hourly"])

# print(finalised_weather_data["hourly"][0:13])
weather_slice = finalised_weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='YOUR TWILIO VIRTUAL NUMBER',
        to='YOUR TWILIO VERIFIED REAL NUMBER'
    )
    print(message.status)
