import requests
import os

API_KEY = os.environ.get("API_KEY")
# "049978dcd1c41743f2a2fd1761e23934"
URL = "https://api.openweathermap.org/data/2.5/onecall"

weather_parameters = {
    "lat": 51.513588,
    "lon": 7.465298,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=URL, params=weather_parameters)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"]
# first_twelve = slice(12)
new_data = hourly_data[:12]

ll = []
for id in new_data:
    ll.append(id["weather"][0]["id"])

is_rain = False
for id_num in ll:
    if id_num < 700:
        is_rain = True

if is_rain:
    print("Bring an Umbrella")
