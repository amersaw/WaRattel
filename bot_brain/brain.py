from quran import QuranPageProvider
from telegram_bot import TelegramBot

# from model import User
# from data import users


class BotBrain(object):
    def __init__(self, bot: TelegramBot):
        self.quranPages = QuranPageProvider()
        self.bot = bot
        pass

    def isInt(self, x):
        return all([xi in "1234567890" for xi in x])

    def process(self, msg_text, channel, user_id, msg, msg_id):
        # if channel == 'telegram':
        #     user = users.get_user_by_telegram_id(user_id)
        # if user is None:
        #     users.add_user(User.from_telegram_user(msg.from_user))
        try:
            if self.isInt(msg.text):
                file = self.quranPages.get_quran_page(msg.text)
                msg = self.bot.send_photo(
                    chat_id=user_id,
                    photo=file,
                    caption="Page : 377",
                    reply_to_message_id=msg_id,
                )
                print(msg)
            else:
                self.bot.send_message(chat_id=user_id, text="وعليكم السلام")
        except Exception as ex:
            self.bot.send_message(chat_id=user_id, text=str(ex))
        return 1

