from abc import ABC, abstractmethod

class HealthcheckService(ABC):
    @abstractmethod
    def check(self):
        """Check the health of the service"""
        pass