import json
from bot_brain import BotBrain
from telegram_bot import TelegramHandler, TelegramBot
from config import config


def lambda_handler(event, context):
    update = None
    bot = TelegramBot(config)
    try:
        bot_brain = BotBrain(bot)
        handler = TelegramHandler(bot, bot_brain)
        update = handler.bot.get_update(json.loads(event["body"]))
        handler.handle_update(update)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "hello world",}),
        }
    except Exception as ex:
        if update and update.message and update.message.chat and update.message.chat.id:
            bot.send_message(chat_id=update.message.chat.id, text=str(ex))
        return {
            "statusCode": 200,
            "body": 1,
        }


if __name__ == "__main__":
    msg = {
        "update_id": 3694258,
        "message": {
            "message_id": 60,
            "from": {
                "id": 176412950,
                "is_bot": False,
                "first_name": "A",
                "last_name": "Saw",
                "username": "amersaw",
                "language_code": "en",
            },
            "chat": {
                "id": 176412950,
                "first_name": "A",
                "last_name": "Saw",
                "username": "amersaw",
                "type": "private",
            },
            "date": 1611784576,
            "text": "11",
        },
    }
    msg_json: str = json.dumps(msg)
    event = {
        "queryStringParameters": {"mode": "basic"},
        "pathParameters": {},
        "body": msg_json,
    }
    a = lambda_handler(event, None)
    pass
