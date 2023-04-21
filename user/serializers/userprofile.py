from rest_framework.authtoken.models import Token
from rest_framework import serializers

from user.models import UserProfile

class UserProfileInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    phone_no = serializers.IntegerField(required=False)
    categories = serializers.CharField(required=False)
    password=serializers.CharField(required=True)



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "user_id", "email","phone_no", "username","date_joined")
