

from django.db.models import Q
from django.db import transaction
from user.models import UserProfile
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from technician.models import Categories,SubCategories,TechnicianWork
from user.models import TechnicianHire,TechnicianWorkDetails


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
        

    @staticmethod
    def get_userprofile(
            user_id,
    ):
               
        try:
            user = UserProfile.objects.get(id=user_id)
            if user:
                return user
            raise ValidationError("user does not exists") 
        except Exception as e:
            raise e
    
    @staticmethod
    def update_user_profile(
            user_id,
            fullname=None,
            address=None,
    ):  
        try:
            user = UserProfile.objects.get(id=user_id)
            if user:
                if fullname==None:
                    user.fullname = user.fullname
                else:
                    user.fullname=fullname
                if address == None:
                    user.address = user.address
                else:
                    user.address=address
                user.save()
                return user
            raise ValidationError("user does not exists") 
        except Exception as e:
            raise e
    @staticmethod
    def update_user_profile_pic(
            user_id,
            profile_image,
    ):  
        try:
            user = UserProfile.objects.get(id=user_id)
            user.profile_image=profile_image
            user.save()
            return user
        except Exception as e:
            raise e
        


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
            search_categerious = Categories.objects.filter(categories__icontains=category)
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
        
class TechnicianSearchService:
    @staticmethod
    def get_technician_search(categories,sub_category):
        try:
            if categories or sub_category:
                allQs = Q()
                if categories is not None: 
                    allQs |= Q(sub_category__category__categories__icontains=categories ,activate=True)
                if sub_category is not None:                     
                    allQs |= Q(sub_category__sub_categories__icontains=sub_category,activate=True)
            result = TechnicianWork.objects.filter(allQs)
            return result
        except Exception as e:
            raise e
    @staticmethod
    def post_hire_technician(
        user_id,
        technician,
        address=None,
        distance=None,
        date=None):
        try:
            print(technician)
            hire=TechnicianHire.objects.create(user_id=user_id,technician_id=technician,
                                               address=address,distance=distance,
                                            date=date
                                            )
            print(hire)
            if hire:
                 technicianworkDetails=TechnicianWorkDetails.objects.create(technicianhire_id=hire.id)
            return hire
            
        except Exception as e:
            raise e
