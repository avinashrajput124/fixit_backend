from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.
import random
from django.contrib.auth.models import AbstractUser
from user.utils import create_new_ref_number
import uuid

def get_profile_image_path(instance, filename):
    return 'profile/{0}'.format(filename)


class UserProfile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.CharField(max_length = 10,blank=True,editable=False,unique=True, default=create_new_ref_number)
    profile_image = models.FileField(upload_to=get_profile_image_path, null=True, blank=True)
    phone_no = models.CharField(max_length=15,null=True, blank=True)
    email=models.CharField(max_length=255,unique=True, null=True, blank=True)
    address=models.CharField(max_length=500, null=True, blank=True)
    fullname=models.CharField(max_length=255,null=True, blank=True)
    visiting_charges = models.CharField(max_length=255, null=True, blank=True)
    categories = models.CharField(max_length=255, null=True, blank=True)
    is_user = models.BooleanField(default=False)
    is_techinician = models.BooleanField(default=False)
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)










