import logging
import os

from dotenv import load_dotenv

log_info_format = "%(asctime)s %(levelname)s %(message)s"
level = logging.INFO

logging.basicConfig(level=level, format=log_info_format)
log = logging.getLogger()

env_file = "../.env"
load_dotenv(env_file)

APP_NAME = os.getenv("APP_NAME")

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

REQUESTS_PER_DAY = int(os.getenv("REQUESTS_PER_DAY"))
DELAY_BETWEEN_REQUESTS = float(os.getenv("DELAY_BETWEEN_REQUESTS"))

CITY_JSON = os.getenv("CITY_JSON")

MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
