from absbot.interfaces import BotBrain, Store


class ABSBot:
    def __init__(self, brain: BotBrain, store: Store) -> None:
        self.brain = brain
        self.store = store

    def configure_telegram(self, token, public_wehbook_url):
        from teleboto
        self.teleboto = Teleboto
