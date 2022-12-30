from absbot.interfaces import Store
import pymongo
from config import config
from model import Channel, User

channel_keys = {Channel.TELEGRAM: "telegram_id"}
USERS_TABLE = "Users"


class MongoDBStore(Store):
    def __init__(self, brain_id) -> None:
        self.client = pymongo.MongoClient(config["connection_string"])
        self.db = self.client[config["db_name"]]
        self.users_table = self.db[USERS_TABLE]

    pass

    def add_user(self, channel:Channel, user: User):
        return self.users_table.insert_one(
            {
                "telegram_id": user.telegram_id,
                "username": user.username,
                "first_name": user.firstname,
                "last_name": user.lastname,
            }
        )

    def get_user_by_id(self, channel: Channel, user_id):
        res = self.users_table.find_one({channel_keys[channel]: user_id})
        return res
