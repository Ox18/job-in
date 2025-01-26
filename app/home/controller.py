from main.utils.response import Response
from .services.homeService import HomeService

class HomeController:
    def __init__(self, homeService: HomeService):
        self.homeService = homeService

    def index(self, request):
        routes = self.homeService.getRoutes()

        return Response.ok(routes, 'Home is OK')
