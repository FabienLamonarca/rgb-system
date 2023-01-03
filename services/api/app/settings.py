from functools import lru_cache
from logging import getLogger

from pydantic import BaseSettings

logger = getLogger()


class Settings(BaseSettings):
    kafka_host: str
    kafka_port: int
    kafka_registry_host: str
    kafka_registry_port: int
    schemas_path: str

@lru_cache()
def get_settings():
    return Settings()
