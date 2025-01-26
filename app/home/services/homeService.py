from abc import ABC, abstractmethod

class HomeService(ABC):
    @abstractmethod
    def getRoutes(self):
        """Get all routes in the application"""
        pass