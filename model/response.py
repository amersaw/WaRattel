from .predef_option import PredefOption
from .update import Update
from .Enums.msg_type import MsgType
from .Enums.channel import Channel
from typing import List


class Response:
    def __init__(
        self,
        update: Update = None,
        text: str = None,
        reciever_service_id: int = None,
        channel: Channel = None,
        type: MsgType = MsgType.TEXT,
        attachement_url: str = None,
        predefined_responces: List[PredefOption] = None,
    ) -> None:

        self.update: Update = update
        # Either Telegram User Id or other service Id
        self.reciever_service_id: int = reciever_service_id or (
            update.sender_id if update else None
        )
        self.channel: Channel = channel or (update.channel if update else None)
        self.type: MsgType = type
        self.text: str = text
        self.attachement_url: str = attachement_url
        self.predefined_responces = predefined_responces
