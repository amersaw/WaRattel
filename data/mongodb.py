import pymongo
from config import config

client = pymongo.MongoClient(config["connection_string"])
db = client[config["db_name"]]
