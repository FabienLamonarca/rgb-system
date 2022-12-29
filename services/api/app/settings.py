from functools import lru_cache
from logging import getLogger

from pydantic import BaseSettings

logger = getLogger()


class Settings(BaseSettings):

    class Config:
        env_file = "application.env"
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return Settings()
