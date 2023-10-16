import json
import logging

from config import CITY_JSON
from db.models import City
from weather.task import CityTaskCreator

log = logging.getLogger()


def _get_cities() -> list[City]:
    log.info(f"Cities data loading...")
    cities = []
    with open(CITY_JSON, encoding="utf-8") as f:
        for city_data in json.load(f):
            city = City(**city_data)
            city.weather_tasks.append(CityTaskCreator.current_weather(lat=city.lat, lon=city.lon))
            city.weather_tasks.append(CityTaskCreator.five_day_weather_forecast(lat=city.lat, lon=city.lon))
            cities.append(city)
    log.info(f"Cities data loading OK. [{len(cities)} cities]")
    return cities


CITIES = _get_cities()
