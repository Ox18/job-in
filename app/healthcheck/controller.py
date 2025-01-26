from .services.healthcheckService import HealthcheckService
from main.utils.response import Response

class HealthcheckController:
    def __init__(self, healthcheckService: HealthcheckService):
        self.healtcheckService = healthcheckService

    def check(self, request):
        response = self.healtcheckService.check()
    
        return Response.ok(response, 'Healthcheck is OK')