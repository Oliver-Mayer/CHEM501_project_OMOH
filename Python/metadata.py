
import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 53.4084,
    "longitude": -2.9916,
    "current": [
        "temperature_2m",
        "relative_humidity_2m",
        "wind_speed_10m"
    ],
    "timezone": "Europe/London"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    weather = response.json()

    print("Weather metadata retrieved!")
    print(weather)

else:
    print("Error:", response.status_code)
