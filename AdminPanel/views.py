from django.shortcuts import render, HttpResponse, redirect
from user.models import UserProfile
from technician.models import Categories, SubCategories
# Create your views here.

def home(request):
    return render(request, "home.html")

def all_technician(request):
    data=UserProfile.objects.filter(is_techinician=True).order_by('-date_joined')
    return render(request, "dashbord/technician/all_technician.html",{'data':data})

def all_uers(request):
    data=UserProfile.objects.filter(is_user=True).order_by('-date_joined')
    return render(request, "dashbord/users/all_uers.html", {'data':data})

def catagiory(request):
    data=Categories.objects.all().order_by('-id')
    SubCategorie = SubCategories.objects.all().order_by('-id')
    context = {"SubCategorie" : SubCategorie, 'data':data}
    return render(request, "dashbord/catagiories/catagiory.html", context)

def AddNewCatagiory(request):
    if request.method == "POST":
        CategoryName = request.POST.get("CategoryName")
        CategoryImage = request.FILES.get("CategoryImage")
        saveCategory = Categories(image = CategoryImage, categories = CategoryName)
        saveCategory.save()
        return redirect("catagiory")
    return render(request, "dashbord/catagiories/catagiory.html")

def AddNewSubCatagiory(request, id):
    if request.method == "POST":
        category = Categories.objects.get(id=id)
        Name = request.POST.get("SubCategoryName")
        Image = request.FILES.get("SubCategoryImage")
        saveData = SubCategories(category = category,image = Image, sub_categories = Name)
        saveData.save()
        return redirect("catagiory")
    return render(request, "dashbord/catagiories/catagiory.html")