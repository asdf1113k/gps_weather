from coordinates import get_coordinates
import requests as rq
from colorama import init, Fore
init(autoreset=True)
# https://api.openweathermap.org/data/2.5/weather?lat=55.7&lon=37.5&appid=7549b3ff11a7b2f3cd25b56d21c83c6a&lang=ru&units=metric

def get_weather(
        coordinates: get_coordinates, 
        TOKEN="7549b3ff11a7b2f3cd25b56d21c83c6a", 
        lang='ru'
        ) -> dict:
    responce_api_openweather = rq.get(f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&appid={TOKEN}&lang={lang}&units=metric")
    json_openweathermap = responce_api_openweather.json()

    if   responce_api_openweather.status_code >= 199 and 226 >= responce_api_openweather.status_code:
        print(Fore.GREEN + f'api.openweathermap.org подключено статус код \'{responce_api_openweather.status_code}\'')

    elif responce_api_openweather.status_code >= 400 and 499 >= responce_api_openweather.status_code:
        raise('api.openweathermap.org ошибка на стороне клиента')
    
    elif responce_api_openweather.status_code >= 500 and 526 >= responce_api_openweather.status_code:
        raise('api.openweathermap.org ошибка на стороне сервера')

    
    return json_openweathermap

if __name__ == '__main__':
    print((get_weather(get_coordinates())))