from coordinates import json_ipinfo
import requests as rq
from my_token import TOKEN
# https://api.openweathermap.org/data/2.5/weather?lat=55.7&lon=37.5&appid=7549b3ff11a7b2f3cd25b56d21c83c6a&lang=ru&units=metric
loc = json_ipinfo["loc"].strip(",")
responce = rq.get(f"https://api.openweathermap.org/data/2.5/weather?lat={loc[0]}&lon={loc[1]}&appid={TOKEN}&lang=ru&units=metric")


if __name__ == "__main__":
    print(responce)
    json_openweathermap = responce.json()
    for key in json_openweathermap:
        print(key, ":", json_openweathermap[key])