from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")

config = {
    "connection_string": getenv("DB_CONNECTION_STRING"),
    "db_name": getenv("DB_NAME"),
    "bot_token": getenv("TELEGRAM_BOT_TOKEN"),
    "bot_webhook_url": getenv("TELEGRAM_WEBHOOK_URL"),
}