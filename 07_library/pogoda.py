"""
Korzystajac z API pogodowego (MetaWeather)

https://www.metaweather.com/api/

$ python pogoda.py warsaw

Pogoda w warsaw:

Temperatura: 15 stopni C.
Wilgotność:  67 %
Ciśnienie powietrza: 1111 hPa


resp = requests.get("adres")
resp.json() - z tego jsona coś tam trzeba wybrać
1. woeid
2. parametry pogody

print(resp.json()[1]["klucz"][3])

https://www.metaweather.com/api/location/search/?query=san
https://www.metaweather.com/api/location/44418/

"""
import sys
import requests
from collections import namedtuple

Weather = namedtuple("Weather", ["the_temp", "air_pressure", "humidity"])

if len(sys.argv) > 1:
    location_name = sys.argv[1]
else:
    location_name = "Warsaw"


def get_location_id(location_name):
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={location_name}")
    # print(resp.json())
    # print(resp.json()[0])
    # print(resp.json()[0]["woeid"])
    #
    woeid = resp.json()[0]["woeid"]
    return woeid

def get_location_weather(location_id):

    resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    w = resp.json()['consolidated_weather'][0]
    weather = Weather(w['the_temp'], w['air_pressure'], w['humidity'])
    return weather

def report(w, location_name):
    rep = f"Pogoada w {location_name}\n"
    rep += f"Temperatura: {w.the_temp:.1f} stopni Celsjusza\n"
    rep += f"Wilgotność: {w.humidity} %\n"
    rep += f"Ciśnienie: {w.air_pressure} hPa\n"
    return rep

if __name__ == "__main__":
    location_id = get_location_id(location_name)
    weather = get_location_weather(location_id)
    rep = report(weather, location_name)
    print(rep)
