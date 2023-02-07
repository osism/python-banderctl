import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    base_url: str = os.getenv("BASE_URL", "http://localhost")
    config_location: str = os.getenv("CONFIG_LOCATION", "/opt/bandersnatch.conf")


settings = Settings()
