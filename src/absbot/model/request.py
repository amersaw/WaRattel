from model.user import User
from .Enums.channel import Channel
from .Enums.msg_type import MsgType


class Request:
    def __init__(self):
        self.msg_id: int
        self.user: User
        self.channel: Channel
        self.text: str
        self.type: MsgType
