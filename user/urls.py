

from django.urls import path

from user.views import UserRegisterRestApi,UserExistsRestApi,UserAlreadyExistsRestApi
from user.views import SubCategeriousRestApi,UserSearchCategeriousRestApi,CategeriousRestApi
urlpatterns = [

    path('user-register/',UserRegisterRestApi.as_view()),
    path('user-exist-check/',UserAlreadyExistsRestApi.as_view()),
    path('user-login/',UserExistsRestApi.as_view()),
    path('technician-categerious/',CategeriousRestApi.as_view()),
    path('technician-subcategerious/',SubCategeriousRestApi.as_view()),
    path('user-search-technician/',UserSearchCategeriousRestApi.as_view())
]
