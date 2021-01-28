from telegram_bot import TelegramHandler, TelegramBot
from bot_brain import BotBrain
from app_local import LocalHandler
from config import config

if __name__ == "__main__":
    bot = TelegramBot(config)
    bot_brain = BotBrain(bot)
    t_handler = TelegramHandler(bot, bot_brain)
    local_handler = LocalHandler(t_handler)
    local_handler.run()
