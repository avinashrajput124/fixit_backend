from django.urls import path

from technician.views import TechnicianExistsRestApi,TechnicianRegisterRestApi
urlpatterns = [

    path('technician-register/',TechnicianRegisterRestApi.as_view()),
    path('technician-login/',TechnicianExistsRestApi.as_view())
]
