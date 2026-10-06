from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Studio"
    APP_VERSION: str = "0.1.0"
    OPENAI_API_KEY: str = ""
    GOOGLE_API_KEY: str = ""
    STORAGE_PATH: str = "./storage"
    MODEL_PATH: str = "./models"
    REDIS_URL: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"

settings = Settings()
