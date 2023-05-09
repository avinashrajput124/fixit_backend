from rest_framework.authtoken.models import Token
from rest_framework import serializers

from user.models import UserProfile
from technician.models import Categories,SubCategories,TechnicianWork


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
            "user_id","username","fullname","profile_image","phone_no","address","categories","visiting_charges","is_user","is_techinician","user_token","role")
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


class TechnicianCategoriesSerializer(serializers.ModelSerializer):
    sub_categeroies = serializers.SerializerMethodField('sub_category')
    class Meta:
        model = Categories
        fields = ('id', 'image', 'categories',"sub_categeroies")

    @staticmethod
    def sub_category(obj):
        sub_catehory=SubCategories.objects.filter(category_id=obj.id)
        print('avi')
        print(sub_catehory,'sub_categeroies')
        if sub_catehory:
            return SubCategoriesSerializer(sub_catehory,many=True).data
        else:
            return []


class TechnicianWorkInputSerializer(serializers.Serializer):
    user = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    time = serializers.CharField(required=False)
    category_id = serializers.IntegerField(required=False)
    longnitude= serializers.DecimalField(max_digits=8, decimal_places=3,required=False)
    latitude= serializers.DecimalField(max_digits=8, decimal_places=3,required=False)
    activate= serializers.BooleanField(required=False)

class TechnicianWorkoutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicianWork
        fields = ('id',"user","sub_category",'price',"time","longnitude","latitude","activate")

class TechnicianseacrinputSerializer(serializers.Serializer):
    sub_category=serializers.CharField(required=False)


