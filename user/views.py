from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from user.serializers.userprofile import UserProfileInputSerializer,UserProfileSerializer,UserProfileLoginInputSerializer
from user.services.userprofile_service import UserRegisterProfileService
from user.utils import success_http_response, error_http_response




class UserExistsRestApi(GenericAPIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        try:

            serializer = UserProfileLoginInputSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                validated_data = serializer.validated_data
                userprofile = UserRegisterProfileService.login_userprofile(**validated_data)
                return success_http_response(
                    message=UserProfileSerializer(userprofile).data,
                )

        except ValidationError as e:
            return error_http_response(message=str(e.message), status_code=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return error_http_response(message=str(e), status_code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_http_response(message=str(e))
class UserRegisterRestApi(GenericAPIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        try:

            serializer = UserProfileInputSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                validated_data = serializer.validated_data
                userprofile = UserRegisterProfileService.create_userprofile(**validated_data)
                return success_http_response(
                    message=UserProfileSerializer(userprofile).data,

                )

        except ValidationError as e:
            return error_http_response(message=str(e.message), status_code=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return error_http_response(message=str(e), status_code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_http_response(message=str(e))



