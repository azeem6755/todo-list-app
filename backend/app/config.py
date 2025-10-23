import pytz
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Todo List App"
    ENV: str
    database_name: str
    database_user: str
    database_password: str
    database_host: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    allowed_hosts: list[str]
    debug: bool = True

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()

timezone = pytz.timezone("Asia/Kolkata")

