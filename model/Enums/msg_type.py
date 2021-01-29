from enum import Enum


class MsgType(Enum):
    OTHER = 0
    TEXT = 1
    VOICE = 2
    ATTACHMENT = 3
    ATTACHMENT_URL = 4
