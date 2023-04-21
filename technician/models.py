from django.db import models

# Create your models here.
from user.models import UserProfile
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# from user.models import UserDetails


# class Technician(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     user = models.OneToOneField(UserDetails,on_delete=models.CASCADE)  
#     phone_no = models.CharField(max_length=15,unique=True, null=True, blank=True)
   


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)