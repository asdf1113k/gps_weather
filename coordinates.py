# import gpsd
# gpsd.connect()

# packet = gpsd.get_current()
# if packet.mode >= 2:
#      print(f"Широта: {packet.lat}, Долгота: {packet.lon}")

import asyncio
import winsdk.windows.devices.geolocation as wdg

async def get_location():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return pos.coordinate.latitude, pos.coordinate.longitude

lat, lon = asyncio.run(get_location())
print(f"Широта: {lat}, Долгота: {lon}")