from update_handlers import TelegramHandler
from bots import Teleboto
from bot_brain import BotBrain
from app_local import LocalHandler
from config import config

if __name__ == "__main__":
    bot = Teleboto(config)
    bot_brain = BotBrain()
    t_handler = TelegramHandler(bot, bot_brain)
    local_handler = LocalHandler(bot, t_handler)
    local_handler.run()
