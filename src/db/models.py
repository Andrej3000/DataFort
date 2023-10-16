from typing import Optional, Callable, Literal

from pydantic import BaseModel


class Request(BaseModel):
    method: Literal["GET", "POST"] = "GET"
    url: str


class WeatherTask(BaseModel):
    request: Request
    callback: Optional[Callable] = None


class City(BaseModel):
    city_id: int | str
    city_name: str
    country: str
    lat: float
    lon: float
    weather_tasks: list[WeatherTask] = []
