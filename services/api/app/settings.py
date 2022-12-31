from functools import lru_cache
from logging import getLogger

from pydantic import BaseSettings

logger = getLogger()


class Settings(BaseSettings):
    kafka_host: str
    kafka_port: int

@lru_cache()
def get_settings():
    return Settings()
