from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root: distributed-cloud-download-manager/
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# backend/manager/.env
ENV_FILE = PROJECT_ROOT / "backend" / "manager" / ".env"


class Settings(BaseSettings):
    APP_NAME: str = "Distributed Download Manager"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    DATABASE_URL: str

    AWS_REGION: str
    AWS_BUCKET: str

    SECRET_KEY: str

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        extra="ignore",
    )


settings = Settings()
