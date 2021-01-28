import json
from os import path

if path.exists("config.json"):
    config = json.load(open("config.json"))
else:
    config = {
        "connection_string": "",
        "db_name": "warattel",
        "bot_token": "",
        "bot_webhook_url": "",
    }

