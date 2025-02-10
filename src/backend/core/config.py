from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CLIMATEMPO_API_KEY: str  # 🔄 Alterado para API_KEY para corresponder ao código

    class Config:
        env_file = ".env"

settings = Settings()
