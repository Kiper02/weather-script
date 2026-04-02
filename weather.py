import os
import sys
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
base_url = "https://api.openweathermap.org/data/2.5/weather"


def read_params():
    args = sys.argv
    if len(args) > 2:
        raise TypeError('Переданы неизвестные аргументы')
    if len(args) == 1:
        raise TypeError("Укажите название города")
    city = args[1]
    return city



def get_weather():
    try:
        city = read_params()
        response = requests.get(f"{base_url}?units=metric&q={city}&appid={api_key}")
        if response.status_code != 200:
            raise Exception(f"{response.json()["message"]}")
        weather_data = response.json()
        return weather_data
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None




if __name__ == '__main__':
    weather = get_weather()
    if weather is None:
        sys.exit(1)

    current_temp = weather['main']['temp']
    description = weather['weather'][0]['description']
    print(f"{current_temp} {description}")