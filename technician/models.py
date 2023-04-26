from django.db import models

def get_categerious_image_path(instance, filename):
    return 'profile/{0}'.format(filename)


# Create your models here.
class Categories(models.Model):
    image=models.FileField(upload_to=get_categerious_image_path, null=True, blank=True)
    categories=models.CharField(max_length=255,null=True, blank=True)
    
    def __str__(self):
        return self.categories

    class Meta:
        db_table = 'Categories'

class SubCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image=models.FileField(upload_to=get_categerious_image_path, null=True, blank=True)
    sub_categories=models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.sub_categories
    
    class Meta:
        db_table = 'SubCategories'