from django.urls import path

from technician.views import TechnicianExistsRestApi,TechnicianRegisterRestApi,TechnicianAlreadyExistsRestApi,CategeriousRestApi,UserSearchCategeriousRestApi
urlpatterns = [

    path('technician-register/',TechnicianRegisterRestApi.as_view()),
    path('technician-exist-check/',TechnicianAlreadyExistsRestApi.as_view()),
    path('technician-login/',TechnicianExistsRestApi.as_view()),
    # path('technician-categerious/',CategeriousRestApi.as_view()),

]

