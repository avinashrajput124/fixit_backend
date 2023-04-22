from django.urls import path

from user.views import UserRegisterRestApi,UserExistsRestApi
urlpatterns = [

    path('technician-register/',UserRegisterRestApi.as_view()),
    path('technician-login/',UserExistsRestApi.as_view())
]
