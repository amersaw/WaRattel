from abc import ABC, abstractmethod


class BotBrain(ABC):
    @property
    @abstractmethod
    def id(self):
        pass

    @abstractmethod
    def process(self):
        pass
