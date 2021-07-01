from typing import Coroutine, Any, List

from fastapi import APIRouter, HTTPException, status

from ..serializers.tag_deskription_serializer import TagDescription
from ..models.tag_description_model import TagDescription as TDmodels

router = APIRouter(
    prefix="/telegrammer",
    tags=["telegrammer"],
    responses={404: {"description": "Not found"}}
)


@router.get("/{tag}", response_model=TagDescription)
async def get_endpoint_description(tag: str):
    """
    Данный метод возвращает форматированную строку с кратким описание возможностей данного ендпоинта, а также ссылку на
    интерактивную документацию.
    """
    data = await TDmodels.get_tag(tag)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Нет данных по тегу")
    return TagDescription(**data).dict()


@router.post("/add-tag/")
async def add_new_tag(tag: TagDescription):
    tag_id = await TDmodels.add_new_tag(**tag.dict())
    return {"created": tag_id}
