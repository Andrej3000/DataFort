import datetime
import logging

from db.models import City
from db.mongodb import MongoDB

log = logging.getLogger()


class WeatherHandler:
    _mongodb = MongoDB
    _collection_name: str

    @classmethod
    async def handler(cls, city: City, data: dict) -> None:
        data = {"city_id": city.city_id} | cls._data_cleaner(data)
        log.info(f"Handle: {city.city_name}")
        await cls._mongodb.insert_one(cls._collection_name, data)

    @classmethod
    def _data_cleaner(cls, data: dict):
        return data


class CurrentWeather(WeatherHandler):
    """
    https://openweathermap.org/current
    """

    _collection_name = "current_weather"


class FiveDayWeatherForecast(WeatherHandler):
    """
    https://openweathermap.org/forecast5
    """

    _collection_name = "five_day_weather_forecast"
