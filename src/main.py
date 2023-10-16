import asyncio

from config import REQUESTS_PER_DAY
from db.cities import CITIES
from tools.requestor import OWMRequestor
from tools.scheduler import Scheduler


async def main():
    await Scheduler.add_job(
        function_=OWMRequestor.cities_weather_request,
        args=CITIES,
        requests_per_day=REQUESTS_PER_DAY,
        job_name="OWM Request",
    )


if __name__ == "__main__":
    asyncio.run(main())
