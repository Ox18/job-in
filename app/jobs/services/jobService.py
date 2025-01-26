
from typing import Protocol

class JobService(Protocol):
    def get_jobs(self, page: int, limit: int) -> dict:
        pass

    def save(self, job: dict, action: str) -> dict:
        pass