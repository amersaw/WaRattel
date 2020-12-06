from telegram import User as TGUser


class User(object):
    def __init__(self, telegram_id, username, firstname, lastname):
        self.telegram_id = telegram_id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def from_telegram_user(cls, tg_user: TGUser):
        return User(tg_user.id, tg_user.username, firstname=tg_user.first_name  , lastname=tg_user.last_name)
