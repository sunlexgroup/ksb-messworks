import datetime
from typing import List, Optional
from fastapi_pagination import Page, paginate, add_pagination
from fastapi import APIRouter, HTTPException, status

from ..serializers.message_serializers import ChatMessageSerializer
from ..models.common_base import chat_messages, user_bot_messages
from ..logic.core import ChatMessages

router = APIRouter(
    prefix="/telegrammer",
    tags=["telegrammer"],
    responses={404: {"description": "Not found"}}
)


@router.get("/chat-messages/", response_model=List[ChatMessageSerializer])
async def get_chat_messages(sdate: Optional[datetime.datetime] = None,
                            edate: Optional[datetime.datetime] = None,
                            offset: Optional[int] = 0,
                            limit: Optional[int] = 100):
    """
    Endpoint для выборки данных из таблицы с сообщениями из чатов.

    Параметры запроса:
    - **sdate** (необязательный параметр)- Дата и время начала выборки.
    Указывается дата и время с которой будет осуществляться отбор данных.
    Если параметр не указан, то будет отбираться все имеющиеся в базе записи.

    - **edate** (необязательный параметр) - Дата и время окончания выборки.
    Указывается дата и время до которой будет осуществляться отбор данных.
    Если параметр не указан то будет отбираться до последнего сообщения.
    В случае отсутствия параметра sdate, данный параметр игнорируется.

    - **offset** (необязательный параметр) - данный параметр необходим для отсчета смещения начала выборки.
    По умолчанию параметр равен 0, что говорит о выборке данных с самого начала в таблице.

    - **limit** (необязательный параметр) - данный параметр необходим для ограничения
    (порционности) запрашиваемых данных. По умолчанию параметр равен 100
    """
    data = await ChatMessages.get_message(start_date=sdate,
                                          end_date=edate,
                                          offset=offset,
                                          limit=limit)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return [ChatMessageSerializer(**row) for row in data]


@router.get("/chat-messages/{username}", response_model=Page[ChatMessageSerializer])
async def get_chat_messages_by_username():
    """
    Endpoint для выборки данных из таблицы с сообщениями
    из чатов по имени пользователя в Telegram.
    """
    data = {}
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return paginate(ChatMessageSerializer(**data).dict())


@router.get("/chat-messages/{chat}", response_model=Page[ChatMessageSerializer])
async def get_chat_messages_by_chat():
    """
    Endpoint для выборки данных из таблицы с сообщениями
    из чатов по названию чата в Telegram.
    """
    data = {}
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return paginate(ChatMessageSerializer(**data).dict())

