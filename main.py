import requests

# Глобальные константы
LOCATIONS = ["Лондон", "Шереметьево", "Череповец"]


def get_weather(locations_list, lang='ru'):
    for loc in locations_list:
        params = {'nTqu': '', 'lang': lang}
        url = f"https://wttr.in/{loc}"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(f"Погода для {loc}:")
            print(response.text)
        else:
            print(f"Не удалось получить данные о погоде для {loc}, статус код: {response.status_code}")


def main():
    get_weather(LOCATIONS, lang='ru')


if __name__ == "__main__":
    main()
