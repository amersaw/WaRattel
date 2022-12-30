from __future__ import annotations


class User(object):
    def __init__(
        self: User, telegram_id: str, username: str, firstname: str, lastname: str
    ) -> None:
        self.telegram_id = telegram_id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
