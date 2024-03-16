from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_password: str = "localhost"
    database_username: str = "fastapi"


settings = Settings()
