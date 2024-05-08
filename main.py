import requests
import urllib.parse


def get_weather(locations_list):
    for loc in locations_list:
        url = f"https://wttr.in/{loc}?nTqu&lang=en"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Weather for {loc}:")
            print(response.text)
        else:
            print(f"Failed to get weather data for {loc}, status code: {response.status_code}")


locations = ["London", "SVO", "Cherepovets"]
get_weather(locations)


def get_weather_ru(city):
    city_encoded = urllib.parse.quote(city)
    url = f"https://wttr.in/{city_encoded}?MTnq&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print("Failed to get weather data:", response.status_code)


get_weather_ru('Череповец')
