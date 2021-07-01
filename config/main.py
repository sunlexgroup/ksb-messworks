import os
import secrets
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


try:
    from .dev import postgres_database_settings
except ImportError:
    from .prod import postgres_database_settings


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
    POSTGRES_SERVER: str = postgres_database_settings['POSTGRES_SERVER']
    POSTGRES_USER: str = postgres_database_settings['POSTGRES_USER']
    POSTGRES_PASSWORD: str = postgres_database_settings['POSTGRES_PASSWORD']
    POSTGRES_DB: str = postgres_database_settings['POSTGRES_DB']
    POSTGRES_PORT: int = postgres_database_settings['POSTGRES_PORT']
    DATABASE_URI: Optional[PostgresDsn] = f'postgresql://{POSTGRES_USER}' \
                                          f':{POSTGRES_PASSWORD}' \
                                          f'@{POSTGRES_SERVER}' \
                                          f':{POSTGRES_PORT}/{POSTGRES_DB}'

    BASE_DIR: str = os.path.dirname(os.path.dirname(__file__))

    TENACITY_MAX_TRIES: int = 60*5
    TENACITY_WAIT_SECONDS: int = 1

    class Config:
        case_sensitive = True


settings = Settings()
