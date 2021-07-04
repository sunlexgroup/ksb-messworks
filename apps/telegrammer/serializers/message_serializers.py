import datetime
import typing
from pydantic import BaseModel


class ChatMessageSerializer(BaseModel):
    """
    Модель является сериализатором данных для сообщений из чатов
    """
    id: int
    chat_id: int
    chat_title: str
    created_datetime: datetime.datetime
    author_id: int
    author_firstname: str
    author_lastname: str
    author_username: str
    message: str

    class Config:
        orm_mode = True


class UserBotMessageSerializer(BaseModel):
    """
    Модель pydantic является сериализатором данных для прямых сообщений для бота
    """
    id: int
    created_datetime: datetime.datetime
    username_id: int
    firstname: str
    lastname: str
    username: str
    message: str

    class Config:
        orm_mode = True