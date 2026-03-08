from weather_great import weather_great

from weather_api_service import json_openweathermap
from coordinates import json_ipinfo

from colorama import init, Fore

class weather:
    def __init__(self, json_ipinfo, json_api_weather):
        self.region = json_ipinfo['region']
        self.city = json_ipinfo['city']
        self.temp = json_api_weather['main']['temp']
        self.weather_description = json_api_weather['weather'][0]['description']
        
    def print_weather(self):
        print(Fore.GREEN + f'погода в {self.region}, {self.city}')
        print(Fore.LIGHTBLUE_EX + f'{self.weather_description}'.center(25))
        print(Fore.LIGHTYELLOW_EX + f'температура: {self.temp}'.center(25))

init(autoreset=True)
if __name__ == "__main__":
    weather_great()
    # ip скрыт в weather_api_service
    # print(json_ipinfo)
    # print(json_openweathermap)
    wt = weather(json_ipinfo, json_openweathermap)
    wt.print_weather()