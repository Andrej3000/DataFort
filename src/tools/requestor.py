import asyncio
import inspect
import logging
from typing import Optional, Iterable

import httpx

from config import DELAY_BETWEEN_REQUESTS
from db.models import City
from db.cities import CITIES

log = logging.getLogger()
logging.getLogger("httpx").setLevel("WARNING")


class OWMRequestor:
    delay_between_requests: float = DELAY_BETWEEN_REQUESTS
    cities: list[City] = CITIES

    @classmethod
    async def city_weather_request(
        cls,
        city: City,
        delay: float = 0,
        client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        await asyncio.sleep(delay)
        if client is None:
            client = httpx.AsyncClient()
        for city_request in city.weather_tasks:
            if city_request is not None:
                r = await client.send(httpx.Request(**city_request.request.model_dump()))
                if 200 <= r.status_code < 300:
                    weather_data = r.json()
                    if city_request.callback:
                        if inspect.iscoroutinefunction(city_request.callback):
                            await city_request.callback(city, weather_data)
                        else:
                            city_request.callback(city, weather_data)
                    await asyncio.sleep(cls.delay_between_requests)
                else:
                    log.error(f"URL status code {r.status_code}")

    @classmethod
    async def cities_weather_request(
        cls,
        cities: Optional[Iterable[City]] = None,
    ) -> tuple:
        if cities is None:
            cities = cls.cities
        tasks = []
        delay_accum = 0
        client = httpx.AsyncClient()
        for city in cities:
            tasks.append(cls.city_weather_request(city=city, delay=delay_accum, client=client))
            delay_accum += cls.delay_between_requests * len(city.weather_tasks)
        result = await asyncio.gather(*tasks)
        await client.aclose()
        return result
