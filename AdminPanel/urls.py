from django.urls import path
from AdminPanel import views 
urlpatterns = [
    path("", views.home, name='home'),
    path("all-technicians-profiles", views.all_technician, name='all_technician'),
    path("all-users-profiles", views.all_uers, name='all_uers'),
    path("technician-all-catagrios", views.catagiory, name='catagiory'),
    path("add-new-catagiory", views.AddNewCatagiory, name='AddNewCatagiory'),
    path("add-new-sub-catagiory/<int:id>", views.AddNewSubCatagiory, name='AddNewSubCatagiory'),

]
