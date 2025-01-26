from django.urls import path
from .controller import HealthcheckController
from .services.implements.healthcheckServiceImpl import HealthcheckServiceImpl


healtcheckService = HealthcheckServiceImpl()
healthcheck_controller = HealthcheckController(healtcheckService)

urlpatterns = [
    path('healthcheck/', healthcheck_controller.check, name='healthcheck'),
]