from django.urls import path
from AdminPanel import views 
urlpatterns = [
    path("", views.home, name='home'),
]
