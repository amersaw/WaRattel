# waitress-serve --listen=*:4743 app:app
from model.Enums.channel import Channel
from model import Response, MsgType, Update
from bots.teleboto import Teleboto
from config import config
from bot_brain import BotBrain
from bots import Teleboto


class TelegramHandler(object):
    def __init__(self, teleboto: Teleboto, bot_brain: BotBrain):
        self.teleboto = teleboto
        self.bot_brain = bot_brain

    def handle_update(self, update: Update):
        if update.type != MsgType.TEXT:
            self.teleboto.send_response(
                Response(
                    update, "Can handle only text messages", channel=Channel.TELEGRAM
                )
            )
        else:
            response = self.bot_brain.process(update)
            self.teleboto.send_response(response)
        return "ok"
