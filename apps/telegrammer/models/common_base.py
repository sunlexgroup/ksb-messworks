import datetime

import sqlalchemy

from config.db import metadata


# Таблица для хранения всех сообщений получаемых из каналов
chat_messages = sqlalchemy.Table(
    "messworks_messages", metadata,
    sqlalchemy.Column(
        "id", sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        index=True
    ),
    # ID чата
    sqlalchemy.Column(
        'chat_id', sqlalchemy.BigInteger
    ),
    # Заголовок чата
    sqlalchemy.Column(
        'chat_title', sqlalchemy.String(128),
        index=True
    ),
    # Дата и время сообщения
    sqlalchemy.Column(
        'created_datetime',
        sqlalchemy.DateTime,
        nullable=False,
        server_default=sqlalchemy.func.current_timestamp()
    ),
    # ID автора сообщения
    sqlalchemy.Column(
        'author_id', sqlalchemy.BigInteger
    ),
    # Имя автора
    sqlalchemy.Column(
        'author_firstname', sqlalchemy.String(128)
    ),
    # Фамилия автора
    sqlalchemy.Column(
        'author_lastname', sqlalchemy.String(128)
    ),
    # Имя пользователя в телеграмм
    sqlalchemy.Column(
        'author_username', sqlalchemy.String(128)
    ),
    # Сообщение
    sqlalchemy.Column(
        'message', sqlalchemy.Text()
    ),
)

user_bot_messages = sqlalchemy.Table(
    "messworks_user_bot_messages", metadata,
    # ID записи
    sqlalchemy.Column(
        "id", sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        index=True
    ),
    # Дата получения записи
    sqlalchemy.Column(
        'created_datetime',
        sqlalchemy.DateTime(timezone=True),
        nullable=False,
        server_default=sqlalchemy.func.current_timestamp(),
        index=True
    ),
    # ID пользователя отправившего сообщение
    sqlalchemy.Column(
        'username_id', sqlalchemy.BigInteger
    ),
    # Имя пользователя отправившего сообщение
    sqlalchemy.Column(
        'firstname', sqlalchemy.String(128)
    ),
    # Фамилия пользователя отправившего сообщение
    sqlalchemy.Column(
        'lastname', sqlalchemy.String(128)
    ),
    # Имя пользователя в телеграмм отправившего сообщение
    sqlalchemy.Column(
        'username', sqlalchemy.String(128),
        index=True
    ),
    # Сообщение от пользователя боту
    sqlalchemy.Column(
        'message', sqlalchemy.Text()
    ),
)
