# import requests as rq
# from coordinates import json_ipinfo


# responce = rq.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={json_ipinfo["lat"]}&lon={lon}&exclude={part}&appid={API key}")

import subprocess

subprocess.run("curl https://api.openweathermap.org/data/2.5/weather\?lat\=55.7\&lon\=37.5\&appid\=7549b3ff11a7b2f3cd25b56d21c83c6a\&lang\=ru\&units\=metric")