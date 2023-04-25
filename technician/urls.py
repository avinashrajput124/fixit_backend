from django.urls import path

from technician.views import TechnicianExistsRestApi,TechnicianRegisterRestApi,TechnicianAlreadyExistsRestApi
urlpatterns = [

    path('technician-register/',TechnicianRegisterRestApi.as_view()),
    path('technician-exist-check/',TechnicianAlreadyExistsRestApi.as_view()),
    path('technician-login/',TechnicianExistsRestApi.as_view())
]
