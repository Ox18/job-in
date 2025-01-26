from django.urls import path
from .controller import HomeController
from .services.implements.homeServiceImpl import HomeServiceImpl

homeService = HomeServiceImpl()

homeController = HomeController(homeService)

urlpatterns = [
    path('', homeController.index, name='home'),
]