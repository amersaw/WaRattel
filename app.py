from telegram_bot import TelegramHandler, TelegramBot
from bot_brain import BotBrain

if __name__ == "__main__":
    bot = TelegramBot()
    bot_brain = BotBrain(bot)
    handler = TelegramHandler(bot, bot_brain)
    handler.run()
