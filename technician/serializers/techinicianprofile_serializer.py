from rest_framework.authtoken.models import Token
from rest_framework import serializers

from user.models import UserProfile
from technician.models import Categories,SubCategories


class TechnicianProfileInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    fullname = serializers.CharField(required=False)
    phone_no = serializers.IntegerField(required=False)
    categories = serializers.CharField(required=True)
    visiting_charges= serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    is_techinician = serializers.BooleanField(default=True)


class TechnicianProfileLoginInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password=serializers.CharField(required=True)


class TechnicianProfileSerializer(serializers.ModelSerializer):
    user_token = serializers.SerializerMethodField('get_token')
    role = serializers.SerializerMethodField('user_role')

    class Meta:
        model = UserProfile
        fields = (
            "user_id","username","fullname","phone_no","categories","visiting_charges","is_user","is_techinician","user_token","role")
    @staticmethod
    def get_token(user_id):
        token, _ = Token.objects.get_or_create(user_id=user_id)
        return str(token)
    
    @staticmethod
    def user_role(obj):
        role=UserProfile.objects.get(id=obj.id)
        if role:
            if role.is_techinician==True:
                return 'techinician'
            else:
                return 'customer'
        else:
            return ' '
        


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'image', 'categories')

class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = ('id', "category",'image','sub_categories')

