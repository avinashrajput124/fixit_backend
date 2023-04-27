

from django.urls import path

from user.views import UserRegisterRestApi,UserExistsRestApi,UserAlreadyExistsRestApi
from user.views import SubCategeriousRestApi,UserSearchCategeriousRestApi,CategeriousRestApi,UserProfileDataRestApi,UpdateUserAddressDataRestApi,UpdateUserProfilepicDataRestApi
urlpatterns = [

    path('user-register/',UserRegisterRestApi.as_view()),
    path('user-exist-check/',UserAlreadyExistsRestApi.as_view()),
    path('user-login/',UserExistsRestApi.as_view()),
    path('technician-categerious/',CategeriousRestApi.as_view()),
    path('technician-subcategerious/',SubCategeriousRestApi.as_view()),
    path('user-search-technician/',UserSearchCategeriousRestApi.as_view()),
    path('user-profile-details/',UserProfileDataRestApi.as_view()),
    path('user-update-profile-details/',UpdateUserAddressDataRestApi.as_view()),
    path('user-update-profile-photo/',UpdateUserProfilepicDataRestApi.as_view())
]
