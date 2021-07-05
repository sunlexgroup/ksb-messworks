import datetime
from typing import List, Optional
from fastapi import APIRouter, HTTPException, status

from ..serializers.message_serializers import ChatMessageSerializer
from ..logic.core import ChatMessages

router = APIRouter(
    prefix="/telegramer",
    tags=["telegramer"],
    responses={404: {"description": "Not found"}}
)


@router.get("/chat-messages/", response_model=List[ChatMessageSerializer])
async def get_chat_messages(sdate: Optional[datetime.datetime] = None,
                            edate: Optional[datetime.datetime] = None,
                            offset: Optional[int] = 0,
                            limit: Optional[int] = 100):
    """
    Endpoint для выборки данных из таблицы с сообщениями из чатов.

    Пример запроса:
    http:example.com/telegramer/chat-messages?sdate=<start_datetime>&edate=<end_datetime>&offset=0&limit=100

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


# @router.get("/chat-messages/{username}", response_model=List[ChatMessageSerializer])
# async def get_chat_messages_by_username():
#     """
#     Endpoint для выборки данных из таблицы с сообщениями из чатов по конкретному username пользователя Telegram
#
#     Пример запроса:
#     http:example.com/telegramer/chat-messages/TelegramUser?sdate=<start_datetime>&edate=<end_datetime>&offset=0&limit=100
#
#     Параметры пути:
#     - **chat_id** - Передается id чата, по которому необходима выборка
#
#     Параметры запроса:
#     - **sdate** (необязательный параметр)- Дата и время начала выборки.
#     Указывается дата и время с которой будет осуществляться отбор данных.
#     Если параметр не указан, то будет отбираться все имеющиеся в базе записи.
#
#     - **edate** (необязательный параметр) - Дата и время окончания выборки.
#     Указывается дата и время до которой будет осуществляться отбор данных.
#     Если параметр не указан то будет отбираться до последнего сообщения.
#     В случае отсутствия параметра sdate, данный параметр игнорируется.
#
#     - **offset** (необязательный параметр) - данный параметр необходим для отсчета смещения начала выборки.
#     По умолчанию параметр равен 0, что говорит о выборке данных с самого начала в таблице.
#
#     - **limit** (необязательный параметр) - данный параметр необходим для ограничения
#     (порционности) запрашиваемых данных. По умолчанию параметр равен 100
#     """
#     data = {}
#     if data is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     return paginate(ChatMessageSerializer(**data).dict())


@router.get("/chat-messages/{chat_id}/", response_model=List[ChatMessageSerializer])
async def get_chat_messages_by_chat_id(chat_id: int,
        sdate: Optional[datetime.datetime] = None,
        edate: Optional[datetime.datetime] = None,
        offset: Optional[int] = 0,
        limit: Optional[int] = 100):
    """
    Endpoint для выборки данных из таблицы с сообщениями из чатов по конкретному id чата

    Пример запроса:
    http:example.com/telegramer/chat-messages/1234567?sdate=<start_datetime>&edate=<end_datetime>&offset=0&limit=100

    Параметры пути:
    - **chat_id** - Передается id чата, по которому необходима выборка

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
    data = await ChatMessages.get_all_message_by_chat_id(
        chat_id=chat_id,
        start_date=sdate,
        end_date=edate,
        offset=offset,
        limit=limit)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return [ChatMessageSerializer(**row) for row in data]

