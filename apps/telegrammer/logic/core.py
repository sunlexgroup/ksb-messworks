import datetime
from typing import Optional
from sqlalchemy import desc
from config.base_models import common_base
from config.db import db


class ChatMessages:
    """
    Класс для работы с таблицей chat_messages
    """

    @classmethod
    async def add_message(cls, message_data: dict):
        """
        Метод добавляет полученное сообщение из чата в таблицу
        """
        query = common_base.chat_messages.insert().values(**message_data)
        try:
            await db.connect()
            await db.execute(query)
        except Exception:
            return False
        finally:
            await db.disconnect()
            return True


    @classmethod
    async def get_message(cls,
                          start_date: Optional[datetime.datetime],
                          end_date: Optional[datetime.datetime],
                          offset: int = 0,
                          limit: int = 100):
        """
        Метод возвращает записи из базы в обратном порядке
        """
        if end_date is None:
            query = common_base.chat_messages.select() \
                .order_by(desc(common_base.chat_messages.c.created_datetime)) \
                .limit(limit) \
                .offset(offset)
        elif start_date is None:
            query = common_base.chat_messages.select() \
                .where(common_base.chat_messages.c.created_datetime > end_date) \
                .order_by(desc(common_base.chat_messages.c.created_datetime)) \
                .limit(limit) \
                .offset(offset)
        else:
            query = common_base.chat_messages.select() \
                .where(common_base.chat_messages.c.created_datetime > start_date) \
                .where(common_base.chat_messages.c.created_datetime < end_date) \
                .order_by(desc(common_base.chat_messages.c.created_datetime)) \
                .limit(limit) \
                .offset(offset)
        rows = await db.fetch_all(query)

        return [dict(row) for row in rows]


    @classmethod
    async def get_all_message_by_chat_id(cls,
                                         chat_id: int,
                                         start_date: Optional[datetime.datetime],
                                         end_date: Optional[datetime.datetime],
                                         offset: int = 0,
                                         limit: int = 100
                                         ):
        """
        Метод возвращает сообщения из конкретного чата.
        Входные параметры:

        - chat_id (обязательный параметр) - id чата из которого хотим получить
        сообщения.
        """
        if start_date is None:
            if end_date is None:
                query = common_base.chat_messages.select() \
                    .where(common_base.chat_messages.c.chat_id == chat_id) \
                    .limit(limit) \
                    .offset(offset) \
                    .order_by(desc(common_base.chat_messages.c.created_ditetime))
            else:
                query = common_base.chat_messages.select() \
                    .where(common_base.chat_messages.c.chat_id == chat_id) \
                    .where(common_base.chat_messages.c.created_datetime > end_date) \
                    .limit(limit) \
                    .offset(offset) \
                    .order_by(desc(common_base.chat_messages.c.created_ditetime))
        elif end_date is None:
            query = common_base.chat_messages.select() \
                .where(common_base.chat_messages.c.chat_id == chat_id) \
                .where(common_base.chat_messages.c.created_datetime < start_date) \
                .limit(limit) \
                .offset(offset) \
                .order_by(desc(common_base.chat_messages.c.created_ditetime))
        else:
            query = common_base.chat_messages.select() \
                .where(common_base.chat_messages.c.chat_id == chat_id) \
                .where(
                common_base.chat_messages.c.created_datetime < start_date) \
                .where(
                common_base.chat_messages.c.created_datetime > end_date) \
                .limit(limit) \
                .offset(offset) \
                .order_by(desc(common_base.chat_messages.c.created_ditetime))

        rows = await db.fetch_all(query)
        return [dict(row) for row in rows]





class UserMessages:
    """
    Класс для работы с таблицей user_bot_messages
    """

@classmethod
async def add_message(cls, message_data: dict):
    """
    Метод добавляет полученное сообщение из чата в таблицу
    """
    query = common_base.user_bot_messages.insert().values(**message_data)
    try:
        await db.connect()
        await db.execute(query)
    except Exception:
        return False
    finally:
        await db.disconnect()
        return True
