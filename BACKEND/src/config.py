from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    app_name: str = "Awesome API"

    model_config = SettingsConfigDict(
        env_file = ".env",
        extra = "ignore"
    )

Config = Settings()