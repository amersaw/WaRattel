from absbot import ABSBot
from absbot.model import Request, Response
from absbot.interfaces import BotBrain

from absbot.mongodb_store import MongoDBStore


class EchoBotBrain(BotBrain):
    def __init__(self) -> None:
        self.id = "EchoBotBrain"

    def process(self, request: Request, user) -> Response:
        return Response(user, request, request.text, request.channel)


store = MongoDBStore()
abs_bot = ABSBot(EchoBotBrain(), store)
abs_bot.configure_telegram("Token", "Public Webhook URL")

abs_bot.process_request(Request)
