

from django.urls import path

from user.views import UserRegisterRestApi,UserExistsRestApi
urlpatterns = [

    path('user-register/',UserRegisterRestApi.as_view()),
    path('user-login/',UserExistsRestApi.as_view())
]
