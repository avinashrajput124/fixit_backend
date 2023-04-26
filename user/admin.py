from django.contrib import admin

# Register your models here.
from user.models import UserProfile



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user_id", "phone_no", "fullname", "is_user", "is_techinician")
    list_per_page = 10
    search_fields = ('user_id',)