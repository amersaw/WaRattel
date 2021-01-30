import json
from bot_brain import BotBrain
from bots import Teleboto
from update_handlers import TelegramHandler
from config import config
from lambdarest import lambda_handler

from flask import Flask, request

app = Flask(__name__)


@lambda_handler.handle("get", path="/")
def get_webhook_info_lambda_handler(event):
    return get_webhook_info(event)


@app.route("/", methods=["GET"])
def get_webhook_info_flask_handler():
    return get_webhook_info(None)


@lambda_handler.handle("get", path="/set_webhook")
def set_webhook_info_lambda_handler(event):
    return set_webhook_info(event)


@app.route("/set_webhook", methods=["GET"])
def set_webhook_info_flask_handler():
    return set_webhook_info(None)


@lambda_handler.handle("post", path=f"/handle/{config['bot_token']}")
def handle_update_lambda(event):
    body = json.loads(event["body"])
    return handle_update(body)


@app.route(f"/handle/{config['bot_token']}", methods=["POST"])
def handle_update_flask():
    body = json.loads(request.data)
    return handle_update(body)


def get_webhook_info(_):
    bot = Teleboto(config)
    try:
        wh = bot.get_webhook()
        return wh
    except Exception as ex:
        print(str(ex), ex.__traceback__)
        return {"Exception": str(ex), "TraceBack": ex.__traceback__}


def set_webhook_info(_):
    bot = Teleboto(config)
    try:
        res = bot.set_webhook()
        wh = bot.get_webhook()
        return {"res": res, "webhook": wh}
    except Exception as ex:
        print(str(ex), ex.__traceback__)
        return {"Exception": str(ex), "TraceBack": ex.__traceback__}


@lambda_handler.handle("post", path=f"/handle/{config['bot_token']}")
def handle_update(body):
    update = None
    bot = Teleboto(config)
    try:
        bot_brain = BotBrain()
        telegram_handler = TelegramHandler(bot, bot_brain)

        update = bot.to_update(body)
        telegram_handler.handle_update(update)
    except Exception as ex:
        if update.sender_id:
            bot.send_message(chat_id=update.sender_id, text=str(ex))
        print(str(ex), ex.__traceback__)
        return {"Exception": str(ex), "TraceBack": ex.__traceback__, "success": False}

    return {"success": True}


the_handler = lambda_handler
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
        "httpMethod": "POST",
        "body": msg_json,  # json.dumps(msg_json),
        "resource": f"/handle/{config['bot_token']}",
    }
    a = lambda_handler(event=event)
    pass


app.run("127.0.0.1", 4743)
