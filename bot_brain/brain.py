from quran import QuranPageProvider
from telegram_bot import TelegramBot
from model import User
from data import users

class BotBrain (object):
    def __init__(self, bot: TelegramBot):
        self.quranPages = QuranPageProvider()
        self.bot = bot
        pass

    def process(self, msg_text, channel, user_id, msg):
        if channel == 'telegram':
            user = users.get_user_by_telegram_id(user_id)
        if user is None:
            users.add_user(User.from_telegram_user(msg.from_user))
        if msg_text == "/start" or True:
            file = "AgACAgQAAxkDAAMFX81Q-x-_zlHCqrVuLChByBVzMC8AApqrMRs_uHRSFMPgutkz8zS9myQqXQADAQADAgADeAADa0wAAh4E"
            # file = self.quranPages.get_quran_page(377)
            # msg = self.bot.send_photo(chat_id = user_id, photo=fileThumb ,caption="Page : 377")
            print(msg)