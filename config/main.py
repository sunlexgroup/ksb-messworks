import os
import secrets
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator
from dotenv import load_dotenv

load_dotenv(".env")


class Settings(BaseSettings):
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://127.0.0.1"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []


    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SECRET_KEY: str = secrets.token_urlsafe(32)

    PROJECT_NAME: str = "KSB MESSWORKS"
    PROJECT_DESCRIPTION: str = "Сервис для работы с мессенджерами"
    PROJECT_AUTHOR: str = "Aleksandr Kochetkov"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_OWNER: str = 'ООО "НПЦ"КСБ" г.Чебоксары'

    # Database settings
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str ="ksb-messworks-dev"
    DATABASE_URI: Optional[PostgresDsn] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:5432/{POSTGRES_DB}'

    BASE_DIR: str = os.path.dirname(os.path.dirname(__file__))

    DEBUG: bool = True

    TENACITY_MAX_TRIES: int = 60*5
    TENACITY_WAIT_SECONDS: int = 1

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = True


settings = Settings()
