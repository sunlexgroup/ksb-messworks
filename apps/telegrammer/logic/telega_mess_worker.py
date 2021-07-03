from telethon.sync import TelegramClient, events
from config.main import settings
from apps.telegrammer.logic.core import ChatMessages, UserMessages

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


if settings.USE_PROXY:
    telegram_proxy_settings = {
        'proxy_type': settings.PROXY_TYPE,
        'addr': settings.PROXY_HOST,
        'port': settings.PROXY_PORT,
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD,
        'rdns': settings.PROXY_RDNS,
    }
else:
    telegram_proxy_settings = None

# Инициализируем бота на работу
bot = TelegramClient('ksb_telegramer_bot',
                     settings.TELEGRAM_API_ID,
                     settings.TELEGRAM_API_HASH,
                     proxy=telegram_proxy_settings) \
    .start(bot_token=settings.TELEGRAM_BOT_HTTP_TOKEN)


@bot.on(events.NewMessage(incoming=True))
async def telegram_event_handler(event):
    """
    Бот слушает все сообщения групп в которых он состоит, а также личные сообщения.
    На личные сообщения от отправляет уведомления о его получении.
    При получении любого сообщения в любой группе мы получаем данные этого
    сообщения. После чего, данные записываются в базу данных.
    """
    chat = await event.get_chat()
    sender = await event.get_sender()
    if hasattr(chat, 'title'):
        # полученные данные отправляем в базу.
        data = {
            'chat_id': chat.id,
            'chat_title': chat.title,
            'author_id': sender.id,
            'author_firstname': sender.first_name,
            'author_lastname': sender.last_name,
            'author_username': sender.username,
            'message': event.raw_text,
        }
        await ChatMessages.add_message(data)
    else:
        if event.raw_text == '/start':
            await bot.send_message(str(sender.username),"Добрый день!\n"
                                                        "Опишите ваше обращение как можно полнее и детальнее, "
                                                        "это поможет нам лучше разобраться в сути обращения.")
            return True
        await bot.send_message(str(sender.username), "Благодарю вас за обращение, я принял его в работу...")
        data = {
            'username_id': sender.id,
            'firstname': sender.first_name,
            'lastname': sender.last_name,
            'username': sender.username,
            'message': event.raw_text,
        }
        await UserMessages.add_message(data)



async def main():
    me = await bot.get_me()

    print(me.stringify())

bot.start()
bot.run_until_disconnected()
