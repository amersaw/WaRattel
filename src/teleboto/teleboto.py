import telegram
from model import Update, Channel, MsgType, Response


class Teleboto(telegram.Bot):
    def __init__(self, config, bot_brain):
        self.TOKEN = config["bot_token"]
        self.webhook_url = config["bot_webhook_url"]
        self.bot_brain = bot_brain

        super().__init__(token=self.TOKEN)
        # self.bot = telegram.Bot(token=self.TOKEN)

    def send_response(self, response: Response) -> bool:
        if response.channel != Channel.TELEGRAM:
            return False
        if response.type == MsgType.TEXT:
            self.send_message(
                chat_id=response.reciever_service_id,
                text=response.text,
                reply_to_message_id=response.update.msg_id if response.update else None,
            )
        elif response.type == MsgType.ATTACHMENT_URL:
            self.send_photo(
                chat_id=response.reciever_service_id,
                photo=response.attachement_url,
                caption=response.text,
                reply_to_message_id=response.update.msg_id if response.update else None,
            )
        return True

    def send(self, chat_id, text, reply_to_message_id):
        self.send_message(
            chat_id=chat_id, text=text, reply_to_message_id=reply_to_message_id
        )

    def set_webhook(self):
        return self.setWebhook(f"{self.webhook_url}?action=telegram_update&token={self.TOKEN}")

    def get_webhook(self):
        wh = self.getWebhookInfo()
        return {
            "url": wh.url,
            "pending_update_count": wh.pending_update_count,
            "last_error_message": wh.last_error_message,
            "last_error_date": wh.last_error_date,
        }

    def to_update(self, json) -> Update:
        u = telegram.Update.de_json(json, self)
        res = Update()
        res.channel = Channel.TELEGRAM
        res.sender_id = u.message.chat.id
        res.msg_id = u.message.message_id
        res.text = (
            u.message.text.encode("utf-8").decode()
            if u.message and u.message.text
            else None
        )
        res.type = MsgType.TEXT if u.message and u.message.text else MsgType.OTHER
        # u.message.chat.type
        return res

    def update(self, update_request):
        update = None
        try:
            update = self.to_update(update_request)
            if update.type != MsgType.TEXT:
                self.send_response(
                    Response(
                        update,
                        "Can handle only text messages",
                        channel=Channel.TELEGRAM,
                    )
                )
            else:
                response = self.bot_brain.process(update)
                self.send_response(response)
            return "ok"

        except Exception as ex:
            if update and update.sender_id:
                self.send_message(
                    chat_id=update.sender_id, text=str(ex)
                )
        return 1
