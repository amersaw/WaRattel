import json
from bot_brain import BotBrain
from bots import Teleboto
from update_handlers import TelegramHandler
from config import config


def lambda_handler(event, context):
    update = None
    bot = Teleboto(config)
    try:
        bot_brain = BotBrain()
        telegram_handler = TelegramHandler(bot, bot_brain)

        update = None
        try:
            update = bot.to_update(json.loads(event["body"]))
            telegram_handler.handle_update(update)
        except Exception as ex:
            if update.sender_id:
                bot.send_message(chat_id=update.sender_id, text=str(ex))

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "hello world",}),
        }
    except Exception as ex:
        if update and update.sender_id:
            bot.send_message(chat_id=update.sender_id, text=str(ex))
        return {
            "statusCode": 200,
            "body": json.dumps({"Exception": str(ex)}),
        }


if __name__ == "__main__":
    msg = {
        "update_id": 3694319,
        "message": {
            "message_id": 191,
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
            "date": 1611804400,
            "text": "g99",
        },
    }
    msg_json: str = json.dumps(msg)
    event = {
        "queryStringParameters": {"mode": "basic"},
        "pathParameters": {},
        "body": msg_json,  # json.dumps(msg_json),
    }
    a = lambda_handler(event, None)
    pass
