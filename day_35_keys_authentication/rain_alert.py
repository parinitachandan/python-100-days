import requests
import os
from twilio.rest import Client

api_key = ""
weather = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = ''
auth_token = ''

my_lat = 12.971599
my_lon = 77.594566

weather_params = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get(weather, weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])

hourly_report = weather_data["hourly"][0:12]  # slice function

will_rain = False

for hour_data in hourly_report:
    report_code = hour_data["weather"][0]["id"]
    if int(report_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today.Remember your umbrella☂️.",
        from_='',
        to=''
    )

    print(message.status)