from config import OPENWEATHERMAP_API_KEY
from db.models import WeatherTask, Request
from weather.handlers import CurrentWeather, FiveDayWeatherForecast


class CityTaskCreator:
    @classmethod
    def current_weather(cls, lat: float, lon: float) -> WeatherTask:
        current_weather_url_template: str = (
            "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid="
            + OPENWEATHERMAP_API_KEY
            + "&units=metric"
        )
        request = Request(url=current_weather_url_template.format(lat=lat, lon=lon))
        callback = CurrentWeather.handler
        return WeatherTask(request=request, callback=callback)

    @classmethod
    def five_day_weather_forecast(cls, lat: float, lon: float) -> WeatherTask:
        forecast5_url_template: str = (
            "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid="
            + OPENWEATHERMAP_API_KEY
            + "&units=metric"
        )
        request = Request(url=forecast5_url_template.format(lat=lat, lon=lon))
        callback = FiveDayWeatherForecast.handler
        return WeatherTask(request=request, callback=callback)
