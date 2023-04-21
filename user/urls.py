

from django.urls import path

from user.views import UserRegisterRestApi
urlpatterns = [

    path('user-register/',UserRegisterRestApi.as_view())
]
