

from django.db import transaction
from user.models import UserProfile
from technician.models import Categories,SubCategories

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

                user = authenticate(username=get_user.username, password=password,is_techinician=True)

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
                return {'status': True,'technician':'exist'}
            else:
                return {'status': False,'technician':'notexist'}
        except Exception as ex:
            raise ex
        

class UserCategoriesService:
    @staticmethod
    @transaction.atomic
    def get_categories():
        try:
            return Categories.objects.all()

        except Exception as e:
            raise e
        
    @staticmethod
    def get_user_search_categories(category):
        try:
            search_categerious = Categories.objects.filter(categories=category)
            return search_categerious

        except Exception as e:
            raise e
        

    @staticmethod
    def get_sub_categories(category_id):
        try:
            sub_categerious = SubCategories.objects.filter(category_id=category_id)
            return sub_categerious

        except Exception as e:
            raise e





