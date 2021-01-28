import json

from bots import Teleboto
from config import config


def get_webhook_info_lambda_handler(event, context):
    bot = Teleboto(config)
    try:
        wh = bot.get_webhook()
        return {
            "statusCode": 200,
            "body": json.dumps(wh),
        }
    except Exception as ex:
        print(ex)
        return {
            "statusCode": 200,
            "body": 1,
        }


def set_webhook_info_lambda_handler(event, context):
    bot = Teleboto(config)
    try:
        res = bot.set_webhook()
        return {
            "statusCode": 200,
            "body": json.dumps({"res": res}),
        }
    except Exception as ex:
        print(ex)
        return {
            "statusCode": 200,
            "body": 1,
        }


if __name__ == "__main__":
    a = set_webhook_info_lambda_handler(None, None)
    a = get_webhook_info_lambda_handler(None, None)
    print(a)
    pass
