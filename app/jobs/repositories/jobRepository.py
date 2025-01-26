from typing import Protocol

class JobRepository(Protocol):

    def getPaginated(self, start: int, limit: int) -> dict:
        pass

    def getRecluter(self, job_id: int) -> dict:
        pass

    def save(self, job: dict, action: str) -> dict:
        pass