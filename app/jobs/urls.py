from django.urls import path
from .controller import JobsController
from main.apis.implements.linkedinApiImpl import LinkedinApiImpl
from .services.implements.jobServiceImpl import JobServiceImpl
from .repositories.implements.jobRepositoryImpl import JobRepositoryImpl

# controller = JobsController(JobServiceImpl(JobRepositoryImpl(), LinkedinApiImpl()))

linkedinApi = LinkedinApiImpl()
jobRepository = JobRepositoryImpl(linkedinApi)
jobService = JobServiceImpl(jobRepository)
controller = JobsController(jobService)

urlpatterns = [
    path('jobs', controller.search, name='home'),
    path('jobs/save', controller.save, name='save'),
    path('jobs/reject', controller.reject, name='reject'),
    path('jobs/test', controller.test, name='test'),
    path('jobs/feedback', controller.feedback, name='feedback')
]