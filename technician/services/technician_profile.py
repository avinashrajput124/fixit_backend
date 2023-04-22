

from django.db import transaction
from user.models import UserProfile
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError, ObjectDoesNotExist



class TechnicianRegisterProfileService:
    @staticmethod
    @transaction.atomic
    def create_technician_profile(
            password,
            username=None,
            email=None,
            fullname=None,
            phone_no=None,
            visiting_charges=None,
            categories=None,
            is_techinician=True,
           
            
    ):
        
        try:
            userprofile = UserProfile.objects.create(
                username=username,
                email=email,
                fullname=fullname,
                phone_no=phone_no,
                visiting_charges=visiting_charges,
                categories=categories,
                is_techinician=is_techinician,
            ) 
            userprofile.set_password(password)
            userprofile.save()
            return userprofile

        except Exception as e:
            raise e
        
    @staticmethod
    def login_technician_profile(

            username,
            password,

    ):
        try:
            get_user = UserProfile.objects.filter(username=username,is_techinician=True).last()
            if get_user:

                user = authenticate(username=get_user.username, password=password)

                if not user:
                    raise ValidationError('Email and Password is Incorrect')

                return user

            raise ValidationError("Invalid Credentials")

        except Exception as e:
            raise e




