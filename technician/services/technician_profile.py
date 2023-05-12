

from django.db import transaction
from user.models import UserProfile,TechnicianHire
from technician.models import Categories,SubCategories,TechnicianWork

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
        

class TechnicianCategoriesService:
    @staticmethod
    @transaction.atomic
    def get_technician_categories(
        user_id
    ):
        try:
            user_categerory=UserProfile.objects.get(id=user_id)
            if user_categerory:
                sub_category=Categories.objects.filter(categories=user_categerory.categories)
                return sub_category
        except Exception as e:
            raise e

class TechnicianWorkService:
    @staticmethod
    @transaction.atomic
    def post_technician_work(
        user_id,
        category_id=None,
        price=None,
        time=None,
        longnitude=None,
        latitude=None,
        activate=False,

             ):
        try:
            if category_id:
                category_id=str(category_id)
                sub_category_ids = category_id.split(",")
                sub_category_ids = [int(x) for x in sub_category_ids]
                sub_category_list = []
                for sub_category in sub_category_ids:
                    user_profile = UserProfile.objects.filter(id=user_id).last()
                    sub_categorys=SubCategories.objects.get(id=sub_category)
                    sub_category_list.append(TechnicianWork(
                        user_id=user_profile.id,
                        sub_category=sub_categorys,
                        price=price,
                        time=time,
                        longnitude=longnitude,latitude=latitude,activate=activate

                    ))
                user_technician_work = TechnicianWork.objects.bulk_create(sub_category_list)
                return user_technician_work

        except Exception as e:
            raise e



class TechnicianScreenWorkServices:
    @staticmethod
    @transaction.atomic
    def get_technician_screen_online_work(
        user_id
    ):
        try:
            user_categerory=TechnicianHire.objects.filter(technician_id=user_id)
            print(user_categerory)
            return user_categerory
        except Exception as e:
            raise e

