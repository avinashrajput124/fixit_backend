from django.shortcuts import render
from user.models import UserProfile
# Create your views here.

def home(request):
    return render(request, "home.html")

def all_technician(request):
    data=UserProfile.objects.filter(is_techinician=True).order_by('-date_joined')
    return render(request, "dashbord/technician/all_technician.html",{'data':data})

def all_uers(request):
    data=UserProfile.objects.filter(is_user=True).order_by('-date_joined')
    return render(request, "dashbord/users/all_uers.html", {'data':data})