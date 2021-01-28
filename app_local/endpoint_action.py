from flask import Response


class EndpointAction(object):
    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        res = self.action()
        self.response.data = str(res)
        return self.response
