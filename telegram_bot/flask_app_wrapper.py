from flask import Flask
from .endpoint_action import EndpointAction


class FlaskAppWrapper(object):
    app = None

    def __init__(self, name):
        self.app = Flask(name)

    def run(self, port):
        self.app.run(threaded=True, port=port)

    def add_endpoint(self, endpoint=None, methods=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name,
                              EndpointAction(handler), methods=methods)
