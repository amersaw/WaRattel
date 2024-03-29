from absbot.model import MsgType, Request, Response
from absbot.interfaces import BotBrain
from warattel_bot_brain.quran import QuranPageProvider


# from model import User
# from data import users


class WarattelBotBrain(BotBrain):
    def __init__(self):
        self.quranPages = QuranPageProvider()
        self.id = "warattel"

    def isInt(self, x):
        return all([xi in "1234567890" for xi in x])

    def process(self, update: Update):
        # if channel == 'telegram':
        #     user = users.get_user_by_telegram_id(user_id)
        # if user is None:
        #     users.add_user(User.from_telegram_user(msg.from_user))
        try:
            if self.isInt(update.text):
                file = self.quranPages.get_quran_page(update.text)
                response = Response(
                    update=update,
                    text=f"Page : {update.text}",
                    channel=update.channel,
                    type=MsgType.ATTACHMENT_URL,
                    attachement_url=file,
                )
                return response
            else:
                return Response(update, "❤️وعليكم السلام")
        except Exception as ex:
            return Response(update, str(ex))
