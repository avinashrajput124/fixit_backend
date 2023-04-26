from django.contrib import admin

# Register your models here.

from technician.models import Categories,SubCategories

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "id","image","categories")
    list_per_page = 10
    search_fields = ('id',)


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "id","category","image","sub_categories")
    list_per_page = 10
    search_fields = ('id',)
