from model.user import User
from data.mongodb import db
from .constants import USERS_TABLE



def add_user(user: User):
    return db[USERS_TABLE].insert_one({
        'telegram_id': user.telegram_id,
        'username': user.username,
        'first_name': user.firstname,
        'last_name': user.lastname
    })


def get_user_by_telegram_id(telegram_id):
    res = db[USERS_TABLE].find_one({'telegram_id': telegram_id})
    return res
