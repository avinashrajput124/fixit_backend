from rest_framework.authtoken.models import Token
from rest_framework import serializers

from user.models import UserProfile

class TechnicianProfileInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    fullname = serializers.CharField(required=False)
    phone_no = serializers.IntegerField(required=False)
    categories = serializers.CharField(required=False)
    visiting_charges= serializers.CharField(required=False)
    password=serializers.CharField(required=True)
    is_techinician = serializers.BooleanField(default=True)

class TechnicianProfileLoginInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password=serializers.CharField(required=True)


class TechnicianProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "user_id", "email","phone_no", "username","date_joined")


class TechnicianSerializer(serializers.ModelSerializer):
    user_token = serializers.SerializerMethodField('get_token')

    class Meta:
        model = UserProfile
        fields = (
            "user_id", "email","phone_no", "username","date_joined","user_token")
        
    @staticmethod
    def get_token(user):
        token, _ = Token.objects.get_or_create(user=user)
        return str(token)
