import python_socks

postgres_database_settings = {
    'POSTGRES_SERVER': 'db',
    'POSTGRES_USER': "postgres",
    'POSTGRES_PASSWORD': "postgres",
    'POSTGRES_DB': "ksb-messworks-dev",
    'POSTGRES_PORT': 5433,
}

telegram_settings = {
    'TELEGRAM_BOT_HTTP_TOKEN': "",
    'TELEGRAM_API_ID': "",
    'TELEGRAM_API_HASH': "",
}

# Типы прокси. Для Python > 3.5
# python_socks.ProxyType.SOCKS5
# python_socks.ProxyType.SOCKS4
# python_socks.ProxyType.HTTP
proxy_settings = {
    'PROXY_TYPE': python_socks.ProxyType.HTTP.name,
    'PROXY_HOST': '10.38.46.202',
    'PROXY_PORT': '3128',
    'PROXY_USERNAME': '',
    'PROXY_PASSWORD': '',
    'PROXY_RDNS':  False,
}
