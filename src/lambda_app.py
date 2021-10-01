import json
from warattel_bot_brain import WarattelBotBrain
from teleboto import Teleboto
from config import config
import logging
from lambda_utils import get_query_param, error_response, success_response

logger = logging.getLogger(__name__)
bot_brain = WarattelBotBrain()
bot = Teleboto(config, bot_brain)


def warattel_lambda_handler(event, context):
    action = get_query_param(event, "action")
    if not action:
        return get_webhook_info()
    elif action == "telegram_update":
        return telegram_update(event)
    elif action == "set_webhook":
        return set_webhook()
    return "Invalid action"


def get_webhook_info():
    try:
        wh = bot.get_webhook()
        return success_response(wh)
    except Exception as ex:
        return error_response(str(ex), 400)


def set_webhook():
    try:
        res = bot.set_webhook()
        return get_webhook_info()
    except Exception as ex:
        logger.exception("Error while setting bot webhook")
        return error_response("error while setting webhook")


def telegram_update(event):
    update = None
    try:
        body = json.loads(event["body"])
        # update = bot.to_update(body)
        bot.update(body)
    except Exception as ex:
        if update and getattr(update, "sender_id"):
            bot.send_message(chat_id=update.sender_id, text=str(ex))
        logger.exception("Error while handling telegram update")
        # return error_response(str({"success": False}),400)
    return success_response({"success": True})


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
            "text": "99",
        },
    }
    msg_json: str = json.dumps(msg)
    event = {
        "queryStringParameters": {"mode": "basic", "action": "telegram_update"},
        "pathParameters": {},
        "httpMethod": "POST",
        "body": msg_json,  # json.dumps(msg_json),
        "resource": f"/handle/{config['bot_token']}",
    }
    a = warattel_lambda_handler(event, None)
    pass
