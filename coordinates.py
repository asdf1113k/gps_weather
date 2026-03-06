import requests as rq

responce_ipinfo = rq.get("https://ipinfo.io")
json_ipinfo = responce_ipinfo.json()

if __name__ == "__main__":
    json_ipinfo["ip"] = "hidden"
    for key in json_ipinfo:
        print(key, ":", json_ipinfo[key])
