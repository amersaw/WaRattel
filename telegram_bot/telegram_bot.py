import telegram


class TelegramBot(telegram.Bot):
    def __init__(self, config):
        self.TOKEN = config["bot_token"]
        super().__init__(token=self.TOKEN)
        # self.bot = telegram.Bot(token=self.TOKEN)

    def send(self, chat_id, text, reply_to_message_id):
        self.send_message(
            chat_id=chat_id, text=text, reply_to_message_id=reply_to_message_id
        )

    def setWebhook(self, url):
        x = super().setWebhook(f"{url}{self.TOKEN}")
        print(x)

    def WebhookInfo(self):
        return self.getWebhookInfo()

    def get_update(self, json):
        return telegram.Update.de_json(json, self)
