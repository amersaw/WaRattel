from abc import ABC, abstractmethod

from absbot.model import User
from absbot.model.Enums.channel import Channel


class Store(ABC):
    @abstractmethod
    def add_user(self, channel: Channel, user: User):
        pass
