

from django.db import transaction
from user.models import UserProfile
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError, ObjectDoesNotExist



class UserRegisterProfileService:
    @staticmethod
    @transaction.atomic
    def create_userprofile(
         password,
            username=None,
            email=None,
            first_name=None,
            phone_no=None,
           
            
    ):
        
        try:
            userprofile = UserProfile.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                phone_no=phone_no,
            ) 
            userprofile.set_password(password)
            userprofile.save()
            return userprofile

        except Exception as e:
            raise e
        
    @staticmethod
    def login_userprofile(

            username,
            password,
            device_token=None,

    ):
        try:
            get_user = UserProfile.objects.filter(username=username).last()
            if get_user:

                user = authenticate(username=get_user.username, password=password)

                if not user:
                    raise ValidationError('Email and Password is Incorrect')

                return user

            raise ValidationError("Invalid Credentials")

        except Exception as e:
            raise e




