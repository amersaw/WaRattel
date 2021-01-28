from telegram_bot.telegram_handler import TelegramHandler
from .flask_app_wrapper import FlaskAppWrapper

from flask import request


class LocalHandler(object):
    def __init__(self, telegram_handler: TelegramHandler):
        self.telegram_handler = telegram_handler
        self.app = FlaskAppWrapper("telegram_handler")
        self.app.add_endpoint(
            endpoint=f"/telegram/{self.telegram_handler.bot.TOKEN}",
            endpoint_name="ad",
            handler=self.respond,
            methods=["POST"],
        )
        self.app.add_endpoint(
            endpoint=f"/telegram/set_webhook",
            endpoint_name="set_webhook",
            handler=self.telegram_handler.set_webhook,
            methods=["GET"],
        )
        self.app.add_endpoint(
            endpoint=f"/telegram",
            endpoint_name="index",
            handler=self.telegram_handler.index,
            methods=["GET"],
        )

    def run(self, port=4743):
        self.app.run(port)

    def respond(self):
        update = self.telegram_handler.bot.get_update(request.get_json(force=True))
        self.telegram_handler.handle_update(update)
