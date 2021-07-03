from config.base_models import common_base
from config.db import db


async def get_info_about_endpoint() -> str:
    """
    Делает запрос к базе данных на извлечение краткой справки по передаваемому тегу. Если в базе есть запись, с
    данным тегом, то возвращаем краткое описание. В случае отсутствия, возвращаем сообщение: "Описание тега не найдено"
    :return: str - краткое описание тега
    """

    return "abracadabra"


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
