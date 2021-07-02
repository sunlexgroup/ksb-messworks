import os
import secrets
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator

try:
    from .dev import postgres_database_settings, telegram_settings, proxy_settings
except ImportError:
    from .prod import postgres_database_settings, telegram_settings, proxy_settings


class Settings(BaseSettings):
    """
    Класс унаследован от базового класса настроек библиотеки Pydantic
    """

    # CORS settings
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:8000",
        "http://localhost:3000",
        "http://0.0.0.0:8000",
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) \
            -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SECRET_KEY: str = secrets.token_urlsafe(32)

    PROJECT_NAME: str = "KSB MESSWORKS"
    PROJECT_DESCRIPTION: str = "Сервис для сбора данных из мессенджеров"
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

    # Telegram settings
    TELEGRAM_BOT_HTTP_TOKEN: str = telegram_settings['TELEGRAM_BOT_HTTP_TOKEN']
    TELEGRAM_API_ID: str = telegram_settings['TELEGRAM_API_ID']
    TELEGRAM_API_HASH: str = telegram_settings['TELEGRAM_API_HASH']

    TENACITY_MAX_TRIES: int = 60 * 5
    TENACITY_WAIT_SECONDS: int = 1

    # Proxy settings
    USE_PROXY: bool = False

    PROXY_TYPE = proxy_settings['PROXY_TYPE']
    PROXY_HOST: str = proxy_settings['PROXY_HOST']
    PROXY_PORT: int = proxy_settings['PROXY_PORT']
    PROXY_USERNAME: str = proxy_settings['PROXY_USERNAME']
    PROXY_PASSWORD: str = proxy_settings['PROXY_PASSWORD']
    PROXY_RDNS: Optional[bool] = proxy_settings['PROXY_RDNS']

    class Config:
        case_sensitive = True


settings = Settings()
