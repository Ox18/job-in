from ..healthcheckService import HealthcheckService
import socket

class HealthcheckServiceImpl(HealthcheckService):
    def __init__(self):
        pass

    def check(self):
        return {
            "status": "up",
            "hostname": socket.gethostname(),
        }