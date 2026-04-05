#!/usr/bin/env python3.14
from weather_great import  weather_great_greet_russia
from filter_color import filter_color
from weather_api_service import get_weather
from coordinates import get_coordinates

from colorama import init, Fore
init(autoreset=True)

            

class Weather:
    def __init__(self, json_api_weather):
        self.city = json_api_weather['name']
        self.temp = json_api_weather['main']['temp']
        self.temp_feels_like = json_api_weather['main']['feels_like']
        self.weather_description = json_api_weather['weather'][0]['description']
        self.wind_speed = json_api_weather['wind']['speed']

    def print_weather(self):
        print(f'{filter_color(self.weather_description)} в {self.city}'.rjust(30))
        print(f'температура: {filter_color((self.temp))}°C'.rjust(25), end=' ')
        print(f'чуствуеться как: {filter_color(self.temp_feels_like)}°C', end='\n')
        print(f'скорость ветра: {self.wind_speed} м/с'.rjust(25))

    def print_weather_new_description(self):
        print(f'{self.weather_description} в {self.city}'.rjust(30))
        print(f'температура: {filter_color((self.temp))}°C'.rjust(25), end=' ')
        print(f'чуствуеться как: {filter_color(self.temp_feels_like)}°C', end='\n')
        print(f'скорость ветра: {self.wind_speed} м/с'.rjust(25))


    

if __name__ == "__main__":
    weather_great_greet_russia()
    wt = Weather(get_weather(get_coordinates()))
    try:
        wt.print_weather()
    except TypeError:
        wt.print_weather_new_description()
        print(Fore.YELLOW + "новое описание погоды(\"сделать логирование не известного описания погоды\")")