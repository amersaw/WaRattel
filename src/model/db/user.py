from __future__ import annotations
from typing import NoReturn
from typing import Type, TypeVar
from telegram import User as TGUser


class User(object):
    def __init__(
        self: "User", telegram_id: str, username: str, firstname: str, lastname: str
    ) -> None:
        self.telegram_id = telegram_id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def from_telegram_user(cls, tg_user: TGUser) -> User:
        return cls(
            tg_user.id,
            tg_user.username,
            firstname=tg_user.first_name,
            lastname=tg_user.last_name,
        )

