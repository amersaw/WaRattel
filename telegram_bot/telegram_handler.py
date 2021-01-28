# waitress-serve --listen=*:4743 app:app
import re
from config import config
from telegram import Update


class TelegramHandler(object):
    def __init__(self, telegram_bot, bot_brain):
        self.bot = telegram_bot
        self.bot_brain = bot_brain

    def run(self, port=4743):
        self.app.run(port)

    def handle_update(self, update: Update):
        chat_id = update.message.chat.id
        msg_id = update.message.message_id
        text = update.message.text.encode("utf-8").decode()
        if update.message.chat.type != "private":
            self.bot.send(
                chat_id=chat_id,
                reply_to_message_id=msg_id,
                text="Only work on private chats",
            )
            return "ok"
        self.bot_brain.process(text, "telegram", chat_id, update.message)
        return "ok"

    def set_webhook(self):
        s = self.bot.setWebhook(config["bot_webhook_url"])
        if s:
            return "webhook setup ok"
        else:
            return "webhook setup failed"

    def index(self):
        info = self.bot.WebhookInfo()
        return f"<pre>{info}</pre>"
