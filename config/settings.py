from typing import cast

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_url: str = cast(str, None)

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
