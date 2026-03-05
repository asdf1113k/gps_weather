import requests as rq

responce = rq.get("https://ipinfo.io")

json = responce.json()

for key in json:
    print(key, ":", json[key])