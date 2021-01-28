# waitress-serve --listen=*:4743 app:app
from bots.teleboto import Teleboto
from model.msg_type import MsgType
import re
from config import config
from model import Update
from bot_brain import BotBrain
from bots import Teleboto


class TelegramHandler(object):
    def __init__(self, bot: Teleboto, bot_brain: BotBrain):
        self.bot = bot
        self.bot_brain = bot_brain

    def handle_update(self, update: Update):
        if update.type != MsgType.TEXT:
            self.bot.send_message(
                chat_id=update.sender_id,
                reply_to_message_id=update.id,
                text="Can handle only text messages",
            )
        else:
            self.bot_brain.process(update)
        return "ok"
