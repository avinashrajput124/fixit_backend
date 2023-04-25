

from django.urls import path

from user.views import UserRegisterRestApi,UserExistsRestApi,UserAlreadyExistsRestApi
urlpatterns = [

    path('user-register/',UserRegisterRestApi.as_view()),
    path('user-exist-check/',UserAlreadyExistsRestApi.as_view()),
    path('user-login/',UserExistsRestApi.as_view())
]
