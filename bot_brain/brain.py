from quran import QuranPageProvider
from model import Update
from bots import Teleboto

# from telegram_bot import TelegramBot

# from model import User
# from data import users


class BotBrain:
    def __init__(self, bot: Teleboto):
        self.quranPages = QuranPageProvider()
        self.bot = bot
        pass

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
                msg = self.bot.send_photo(
                    chat_id=update.sender_id,
                    photo=file,
                    caption=f"Page : {update.text}",
                    reply_to_message_id=update.msg_id,
                )

            else:
                self.bot.send_message(chat_id=update.sender_id, text="وعليكم السلام")
        except Exception as ex:
            self.bot.send_message(chat_id=update.sender_id, text=str(ex))
        return 1

