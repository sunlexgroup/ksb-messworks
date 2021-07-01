from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.main import settings


def apply_cors_middleware(app: FastAPI) -> None:
    """
    Метод разрешает получение запросов из разных источников
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
