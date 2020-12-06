# waitress-serve --listen=*:4743 app:app
import re
from flask import Flask, request
from config import config
from .flask_app_wrapper import FlaskAppWrapper


class TelegramHandler(object):
    def __init__(self, telegram_bot, bot_brain):
        self.bot = telegram_bot
        self.bot_brain = bot_brain
        # @app.route('/{}'.format(Bot.TOKEN), methods=['POST'])
        # @app.route('/set_webhook', methods=['GET', 'POST'])
        # @app.route('/')
        #self.app = Flask(__name__)
        self.app = FlaskAppWrapper('telegram_handler')
        self.app.add_endpoint(
            endpoint=f'/{self.bot.TOKEN}', endpoint_name='ad', handler=self.respond, methods=['POST'])
        self.app.add_endpoint(
            endpoint=f'/set_webhook', endpoint_name='set_webhook', handler=self.set_webhook, methods=['GET'])
        self.app.add_endpoint(
            endpoint=f'/', endpoint_name='index', handler=self.index, methods=['GET'])

    def run(self, port=4743):
        self.app.run(port)

    def respond(self):
        update = self.bot.get_update(request.get_json(force=True))
        chat_id = update.message.chat.id
        msg_id = update.message.message_id
        text = update.message.text.encode('utf-8').decode()
        if update.message.chat.type != 'private':
            self.bot.send(chat_id=chat_id, reply_to_message_id=msg_id,text="Only work on private chats")
            return 'ok'
        self.bot_brain.process(text, "telegram", chat_id, update.message)
        return 'ok'

    def set_webhook(self):
        s = self.bot.setWebhook(config['bot_webhook_url'])
        if s:
            return "webhook setup ok"
        else:
            return "webhook setup failed"

    def index(self):
        info = self.bot.WebhookInfo()
        return f'<pre>{info}</pre>'
