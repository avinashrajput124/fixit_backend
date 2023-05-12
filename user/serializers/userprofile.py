from rest_framework.authtoken.models import Token
from rest_framework import serializers

from user.models import UserProfile,TechnicianHire

class UserProfileLoginInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password=serializers.CharField(required=True)


class UserProfileInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    fullname = serializers.CharField(required=False)
    phone_no = serializers.IntegerField(required=False)
    password=serializers.CharField(required=True)
    is_user = serializers.BooleanField(default=True)


class UserProfileSerializer(serializers.ModelSerializer):
    user_token = serializers.SerializerMethodField('get_token')
    role = serializers.SerializerMethodField('user_role')

    class Meta:
        model = UserProfile
        fields = (
            "user_id", "username","phone_no","profile_image","fullname","address","is_user","is_techinician","user_token","role")
        
    @staticmethod
    def get_token(user_id):
        token, _ = Token.objects.get_or_create(user_id=user_id)
        return str(token)
    
    @staticmethod
    def user_role(obj):
        role=UserProfile.objects.get(id=obj.id)
        if role:
            if role.is_user==True:
                return 'customer'
            else:
                return 'techinician'
        else:
            return ' '


class UserAddressInputSerializer(serializers.Serializer):
    fullname=serializers.CharField(required=False)
    address=serializers.CharField(required=False)

class UserProfilepicInputSerializer(serializers.Serializer):
    profile_image = serializers.FileField(required=False)


class HireTechnicianInputSerializer(serializers.Serializer):
    address = serializers.CharField(required=False)
    distance = serializers.CharField(required=False)
    date = serializers.CharField(required=False)

class TechnicianWorkDetailsInputSerializer(serializers.Serializer):
    is_accepted = serializers.BooleanField(required=False)
    is_rejected = serializers.BooleanField(required=False)


class HireTechnicianOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicianHire
        fields = "__all__"

