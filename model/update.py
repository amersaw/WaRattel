from .Enums.channel import Channel
from .Enums.msg_type import MsgType


class Update:
    def __init__(self):
        self.msg_id: int
        self.sender_id: int
        self.channel: Channel
        self.text: str
        self.type: MsgType

