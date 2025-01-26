from typing import Protocol

class LinkedinApi(Protocol):
    def get(self, url: str) -> dict:
        pass
