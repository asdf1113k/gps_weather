from weather_great import weather_great

from weather_api_service import json_openweathermap
from coordinates import json_ipinfo

from colorama import init, Fore

init(autoreset=True)
if __name__ == "__main__":
    weather_great()
    # ip скрыт в weather_api_service
    # print(json_ipinfo)
    # print(json_openweathermap)
    print(Fore.GREEN + f'погода в {json_ipinfo["region"]}, {json_ipinfo["city"]}')
    print(Fore.LIGHTBLUE_EX + f'{json_openweathermap['weather'][0]['description']}'.center(25))
    print(Fore.LIGHTYELLOW_EX + f'{json_openweathermap['main']}'.center(25),'\n'
          f'температура: {json_openweathermap['main']['temp']}'.center(25))
    


