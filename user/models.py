from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.

from django.contrib.auth.models import AbstractUser

import uuid

TYPE_CHOICES = (
    ('Electrician', 'Electrician'),
    ('Plumber', 'Plumber'),
    ('Ac_Repair', 'Ac_Repair'),
    ('Carpainter', 'Carpainter')
)
class UserProfile(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    phone_no = models.CharField(max_length=15,unique=True, null=True, blank=True)
    email=models.CharField(max_length=255,unique=True, null=True, blank=True)
    fullname=models.CharField(max_length=255,null=True, blank=True)
    visiting_charges = models.CharField(max_length=255, null=True, blank=True)
    categories = models.CharField(choices=TYPE_CHOICES,max_length=255, null=True, blank=True)
    is_user = models.BooleanField(default=False)
    is_techinician = models.BooleanField(default=False)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)