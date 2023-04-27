

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
            fullname=None,
            phone_no=None,
            is_user=True,
           
            
    ):
        
        try:
            userprofile = UserProfile.objects.create(
                username=username,
                email=email,
                fullname=fullname,
                phone_no=phone_no,
                is_user=is_user
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

    ):
        try:
            get_user = UserProfile.objects.filter(username=username).last()
            if get_user:
                user = authenticate(username=get_user.username, password=password)
                if not user:
                    raise ValidationError('Username and Password is Incorrect')

                return user

            raise ValidationError("Username and Password is Incorrect")

        except Exception as e:
            raise e

    @staticmethod
    def check_username(
            username
    ):
        try:
            user_profile = UserProfile.objects.filter(username=username).last()

            if user_profile:
                return {'status': True,'user':'exist'}
            else:
                return {'status': False,'user':'notexist'}
        except Exception as ex:
            raise ex





