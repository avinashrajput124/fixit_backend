from django.urls import path

from technician.views import TechnicianExistsRestApi,TechnicianRegisterRestApi,TechnicianAlreadyExistsRestApi,TechnicianCategeriosRestApi,TechnicianWorkRestApi
from user.views import UserRegisterRestApi,UserExistsRestApi,UserAlreadyExistsRestApi

urlpatterns = [

    path('technician-register/',TechnicianRegisterRestApi.as_view()),
    path('technician-exist-check/',TechnicianAlreadyExistsRestApi.as_view()),
    path('user-login/',UserExistsRestApi.as_view()),
    path('technician-subcategory/',TechnicianCategeriosRestApi.as_view()),
    path('technician-work/',TechnicianWorkRestApi.as_view()),

]

