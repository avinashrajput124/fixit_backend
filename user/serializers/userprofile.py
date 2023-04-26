from rest_framework.authtoken.models import Token
from rest_framework import serializers

from user.models import UserProfile

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

    class Meta:
        model = UserProfile
        fields = (
            "user_id", "username","phone_no","fullname","is_user","is_techinician","user_token",)
        
    @staticmethod
    def get_token(user_id):
        token, _ = Token.objects.get_or_create(user_id=user_id)
        return str(token)
