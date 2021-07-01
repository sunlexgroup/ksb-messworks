from telethon.sync import TelegramClient, events
from config.main import settings

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


bot = TelegramClient('ksb_telegramer_bot',
                     settings.TELEGRAM_API_ID,
                     settings.TELEGRAM_API_HASH)\
    .start(bot_token=settings.TELEGRAM_BOT_HTTP_TOKEN)


async def do_something(me):
    pass


@bot.on(events.NewMessage())
async def telegram_event_handler(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id
    message = event.raw_text
    print(f'{chat}:{chat_id} - Автор {sender}:{sender_id} "{message}"')


async def main():
    me = await bot.get_me()

    print(me.stringify())

    await bot.send_message('AleksandrKochetkov', 'Hello, myself!')

bot.start()
bot.run_until_disconnected()
