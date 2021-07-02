from telethon.sync import TelegramClient, events
from config.main import settings
from apps.telegrammer.logic.core import ChatMessages

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
                     proxy=telegram_proxy_settings)\
    .start(bot_token=settings.TELEGRAM_BOT_HTTP_TOKEN)


async def do_something(me):
    pass


@bot.on(events.NewMessage())
async def telegram_event_handler(event):
    """
    Бот слушает все сообщения групп в которых он состоит.
    При получении любого сообщения в любой группе мы получаем данные этого
    сообщения. После чего, данные записываются в базу данных.
    Получаемый ответ из чата:
    Chat(id=592513999, title='ksb_test_chat_bot', photo=ChatPhotoEmpty(),
    participants_count=3, date=datetime.datetime(2021, 7, 2, 4, 23, 32,
    tzinfo=datetime.timezone.utc), version=2, creator=False, kicked=False,
    left=False, deactivated=False, call_active=False, call_not_empty=False,
    migrated_to=None, admin_rights=None, default_banned_rights=
    ChatBannedRights(until_date=datetime.datetime(2038, 1, 19, 3, 14, 7,
    tzinfo=datetime.timezone.utc), view_messages=False, send_messages=False,
    send_media=False, send_stickers=False, send_gifs=False, send_games=False,
    send_inline=False, embed_links=False, send_polls=False, change_info=False,
    invite_users=False, pin_messages=False)):-592513999 -
    Автор User(id=168677602, is_self=False, contact=False, mutual_contact=False,
    deleted=False, bot=False, bot_chat_history=False, bot_nochats=False,
    verified=False, restricted=False, min=False, bot_inline_geo=False,
    support=False, scam=False, apply_min_photo=True, fake=False,
    access_hash=5909172583760012408, first_name='Aleksandr',
    last_name='Kochetkov', username='AleksandrKochetkov', phone=None,
    photo=UserProfilePhoto(photo_id=724464784613943255, dc_id=2,
    has_video=False, stripped_thumb=None), status=UserStatusRecently(),
    bot_info_version=None, restriction_reason=[], bot_inline_placeholder=None,
    lang_code='ru'):168677602 "Тест прокси"

    # Данные при получении личного сообщения боту.
    User(id=168677602, is_self=False, contact=False, mutual_contact=False,
    deleted=False, bot=False, bot_chat_history=False, bot_nochats=False,
    verified=False, restricted=False, min=False, bot_inline_geo=False,
    support=False, scam=False, apply_min_photo=True, fake=False,
    access_hash=5909172583760012408, first_name='Aleksandr',
    last_name='Kochetkov', username='AleksandrKochetkov',
    phone=None, photo=UserProfilePhoto(photo_id=724464784613943255, dc_id=2,
    has_video=False, stripped_thumb=None), status=UserStatusRecently(),
    bot_info_version=None, restriction_reason=[], bot_inline_placeholder=None,
    lang_code='ru'):168677602 - Автор User(id=168677602, is_self=False,
    contact=False, mutual_contact=False, deleted=False, bot=False,
    bot_chat_history=False, bot_nochats=False, verified=False, restricted=False,
    min=False, bot_inline_geo=False, support=False, scam=False,
    apply_min_photo=True, fake=False, access_hash=5909172583760012408,
    first_name='Aleksandr', last_name='Kochetkov', username='AleksandrKochetkov',
    phone=None, photo=UserProfilePhoto(photo_id=724464784613943255, dc_id=2,
    has_video=False, stripped_thumb=None), status=UserStatusRecently(),
    bot_info_version=None, restriction_reason=[], bot_inline_placeholder=None,
    lang_code='ru'):168677602 "Снова привет"
    """
    chat = await event.get_chat()
    sender = await event.get_sender()

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


async def main():
    me = await bot.get_me()

    print(me.stringify())

bot.start()
bot.run_until_disconnected()
