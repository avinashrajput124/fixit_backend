from django.contrib import admin

# Register your models here.
from user.models import UserProfile,TechnicianHire,TechnicianWorkDetails



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user_id", "phone_no", "fullname","username", "is_user", "is_techinician","categories")
    list_per_page = 10
    search_fields = ('user_id',)

@admin.register(TechnicianHire)
class TechnicianHireAdmin(admin.ModelAdmin):
    list_display = (
        "technician", "user", "address","distance", "date",)
    list_per_page = 10
    search_fields = ('technician',)

@admin.register(TechnicianWorkDetails)
class TechnicianWorkDetailsAdmin(admin.ModelAdmin):
    list_display = (
        "technicianhire", "is_accepted", "is_rejected")
    list_per_page = 10
    search_fields = ('technicianhire',)