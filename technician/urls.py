from django.urls import path

from technician.views import TechnicianExistsRestApi,TechnicianHomeScreenRestApi,TechnicianRegisterRestApi,TechnicianAlreadyExistsRestApi,TechnicianCategeriosRestApi,TechnicianWorkRestApi
from user.views import UserRegisterRestApi,UserExistsRestApi,UserAlreadyExistsRestApi

urlpatterns = [

    path('technician-register/',TechnicianRegisterRestApi.as_view()),
    path('technician-exist-check/',TechnicianAlreadyExistsRestApi.as_view()),
    path('user-login/',UserExistsRestApi.as_view()),
    path('technician-subcategory/',TechnicianCategeriosRestApi.as_view()),
    path('technician-post-work/',TechnicianWorkRestApi.as_view()),
    path('technician-all-work/',TechnicianHomeScreenRestApi.as_view()),

]

