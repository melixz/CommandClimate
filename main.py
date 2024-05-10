import requests


def get_weather(locations_list, lang='en'):
    for loc in locations_list:
        params = {'nTqu': '', 'lang': lang}
        url = f"https://wttr.in/{loc}"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(f"Weather for {loc}:")
            print(response.text)
        else:
            print(f"Failed to get weather data for {loc}, status code: {response.status_code}")


# Запрос погоды для списка местоположений на английском и русском языках
locations = ["London", "SVO", "Cherepovets"]
get_weather(locations, lang='en')  # Погода на английском языке
get_weather(['Череповец'], lang='ru')  # Погода для Череповца на русском языке
