from model.channel import Channel
from update_handlers import TelegramHandler
import update_handlers
from .flask_app_wrapper import FlaskAppWrapper

from bots import Teleboto
from flask import request
from model import Update, Channel

from config import config


class LocalHandler(object):
    def __init__(self, teleboto: Teleboto, telegram_handler: TelegramHandler):
        self.teleboto = teleboto
        self.telegram_handler = telegram_handler
        self.app = FlaskAppWrapper("telegram_handler")
        self.app.add_endpoint(
            endpoint=f"/telegram/TAFADAL",
            endpoint_name="ad",
            handler=self.respond,
            methods=["POST"],
        )
        self.app.add_endpoint(
            endpoint=f"/telegram/set_webhook",
            endpoint_name="set_webhook",
            handler=self.teleboto.set_webhook,
            methods=["GET"],
        )
        self.app.add_endpoint(
            endpoint=f"/telegram",
            endpoint_name="index",
            handler=self.index,
            methods=["GET"],
        )

    def run(self, port=4743):
        self.app.run(port)

    def set_webhook(self):
        if self.teleboto.set_webhook():
            return "webhook setup ok"
        else:
            return "webhook setup failed"

    def index(self):
        info = self.teleboto.get_webhook_info()
        return f"<pre>{info}</pre>"

    def respond(self):
        update = None
        try:
            update = self.teleboto.to_update(request.get_json(force=True))
            self.telegram_handler.handle_update(update)
        except Exception as ex:
            if update and update.sender_id:
                self.telegram_handler.bot.send_message(
                    chat_id=update.sender_id, text=str(ex)
                )
        return 1
