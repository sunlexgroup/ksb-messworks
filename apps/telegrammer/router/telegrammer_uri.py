from typing import Coroutine, Any

from fastapi import APIRouter, HTTPException
from apps.telegrammer.logic.core import get_info_about_endpoint

router = APIRouter(
    prefix="/telegrammer",
    tags=["telegrammer"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def get_endpoint_description() -> Coroutine[Any, Any, str]:
    """
    Данный метод возвращает форматированную строку с кратким описание возможностей данного ендпоинта, а также ссылку на
    интерактивную документацию.
    :return: str
    """
    return get_info_about_endpoint()
