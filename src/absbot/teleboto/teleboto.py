import telegram
from telegram.user import User as TGUser
from model import Update, Channel, MsgType, Response, User
from absbot.interfaces import Store
from absbot.interfaces import BotBrain


class Teleboto(telegram.Bot):
    def __init__(
        self,
        bot_token: str,
        public_webhook_url: str,
        bot_brain: BotBrain,
        store: Store,
    ):
        self.TOKEN = bot_token
        self.public_webhook_url = public_webhook_url
        self.bot_brain = bot_brain
        self.store = store

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
        return self.setWebhook(
            f"{self.public_webhook_url}?action=telegram_update&token={self.TOKEN}"
        )

    def get_webhook(self):
        wh = self.getWebhookInfo()
        return {
            "url": wh.url,
            "pending_update_count": wh.pending_update_count,
            "last_error_message": wh.last_error_message,
            "last_error_date": wh.last_error_date,
        }

    @staticmethod
    def to_user(tg_user: TGUser) -> User:
        return User(
            tg_user.id,
            tg_user.username,
            firstname=tg_user.first_name,
            lastname=tg_user.last_name,
        )

    def to_update(self, update) -> Update:
        res = Update()
        res.user = self.to_user(update)

        res.channel = Channel.TELEGRAM
        res.msg_id = update.message.message_id
        res.text = (
            update.message.text.encode("utf-8").decode()
            if update.message and update.message.text
            else None
        )
        res.type = (
            MsgType.TEXT if update.message and update.message.text else MsgType.OTHER
        )
        # u.message.chat.type
        return res

    def process_update(self, update_request):
        update = None
        try:
            update = telegram.Update.de_json(update_request, self)
            update = self.to_update(update)
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
                self.send_message(chat_id=update.sender_id, text=str(ex))
        return 1
