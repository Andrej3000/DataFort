import asyncio
import logging
from typing import Optional

import pymongo
from motor.core import AgnosticCursor
from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_NAME, APP_NAME, MONGO_URI

log = logging.getLogger()

client = AsyncIOMotorClient(MONGO_URI, appname=APP_NAME, uuidRepresentation="standard")
client.get_io_loop = asyncio.get_running_loop


class MongoDB:
    __db = client[MONGO_DB_NAME]

    @classmethod
    async def init(cls):
        await cls.__db["current_weather"].create_index([("city_id", pymongo.ASCENDING)], name="city_id_index")
        await cls.__db["five_day_weather_forecast"].create_index([("city_id", pymongo.ASCENDING)], name="city_id_index")

    @classmethod
    async def insert_one(cls, collection: str, data: dict) -> None:
        return await cls.__db[collection].insert_one(data)

    @classmethod
    def get_cursor(cls, collection: str) -> AgnosticCursor:
        return cls.__db[collection].find(projection={"_id": 0})

    @classmethod
    async def get_document(cls, collection: str, filter_: dict) -> Optional[dict]:
        return await cls.__db[collection].find_one(filter=filter_, projection={"_id": 0})

    @classmethod
    async def update_document(cls, collection: str, filter_: dict, update: dict) -> None:
        await cls.__db[collection].update_one(filter=filter_, update=update)
