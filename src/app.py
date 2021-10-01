from flask import Flask, request,jsonify
from teleboto.teleboto import Teleboto
from config import config
from warattel_bot_brain.brain import WarattelBotBrain
import json
app = Flask(__name__)




@app.route(f"/handle", methods=["GET","POST"])
def generic_handler():
    action = request.args.get("action")
    if not action:
        return get_webhook_info()
    elif action == "telegram_update":
        return telegram_update()
    elif action == "set_webhook":
        return set_webhook()
    return "Invalid action"


def set_webhook():
    return bot.set_webhook()
def get_webhook_info():
    return bot.get_webhook()
def telegram_update():
    if request.args.get("token") != config["bot_token"]:
        return 0
    body = json.loads(request.data)
    return bot.update(body)



if __name__ == "__main__":
    bot_brain = WarattelBotBrain()
    bot = Teleboto(config, bot_brain)
    app.run("127.0.0.1", 4743)
