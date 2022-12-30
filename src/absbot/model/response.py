from typing import Optional
from . import User, MsgType, Channel, Request


class Response:
    def __init__(
        self,
        destination_user: User = None,
        request: Request = None,
        text: str = None,
        channel: Channel = None,
        type: MsgType = MsgType.TEXT,
        attachement_url: str = None,
    ) -> None:

        self.request: Optional[Request] = request
        self.destination_user: User = destination_user
        self.channel: Channel = channel or (request.channel if request else None)
        self.type: MsgType = type
        self.text: Optional[str] = text
        self.attachement_url: Optional[str] = attachement_url
