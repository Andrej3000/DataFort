import asyncio
import logging
from typing import Callable

log = logging.getLogger()


class Scheduler:
    seconds_in_day = 60 * 60 * 24

    @classmethod
    async def add_job(cls, function_: Callable, args, requests_per_day: int = 24, job_name: str = "") -> None:
        delay = cls.seconds_in_day // requests_per_day
        log.info(f"Task frequency: every {delay} seconds")
        while True:
            log.info(f"JOB START: '{job_name}'")
            asyncio.create_task(function_(args))
            await asyncio.sleep(delay)
