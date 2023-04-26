from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from technician.serializers.techinicianprofile_serializer import TechnicianProfileInputSerializer,TechnicianProfileLoginInputSerializer,\
    TechnicianProfileSerializer,CategoriesSerializer,SubCategoriesSerializer
from technician.services.technician_profile import TechnicianRegisterProfileService,UserCategoriesService
from user.utils import success_http_response, error_http_response


class TechnicianAlreadyExistsRestApi(GenericAPIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        try:
            filter_fields = {
                'username': request.query_params.get('username', None),

            }
            technician = TechnicianRegisterProfileService.check_username(**filter_fields)
            return success_http_response(
                message=technician
            )

        except ValidationError as e:
            return error_http_response(message=str(e.message), status_code=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return error_http_response(message=str(e), status_code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_http_response(message=str(e))



class TechnicianExistsRestApi(GenericAPIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        try:

            serializer = TechnicianProfileLoginInputSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                validated_data = serializer.validated_data
                technician_profile = TechnicianRegisterProfileService.login_technician_profile(**validated_data)
                return success_http_response(
                    message=TechnicianProfileSerializer(technician_profile).data,
                )

        except ValidationError as e:
            return error_http_response(message=str(e.message), status_code=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return error_http_response(message=str(e), status_code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_http_response(message=str(e))
class TechnicianRegisterRestApi(GenericAPIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        try:

            serializer = TechnicianProfileInputSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                validated_data = serializer.validated_data
                technician_profile = TechnicianRegisterProfileService.create_technician_profile(**validated_data)
                return success_http_response(
                    message=TechnicianProfileSerializer(technician_profile).data,

                )

        except ValidationError as e:
            return error_http_response(message=str(e.message), status_code=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return error_http_response(message=str(e), status_code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return error_http_response(message=str(e))


class CategeriousRestApi(GenericAPIView):

    def get(self, request):
        try:
            categerious = UserCategoriesService.get_categories()
            return Response(
                data=CategoriesSerializer(categerious, many=True).data,
                status=status.HTTP_200_OK
            )

        except ValidationError as e:
            return error_http_response(message=str(e.message))
        except Exception as e:
            return error_http_response(message=str(e))
class UserSearchCategeriousRestApi(GenericAPIView):

    def get(self, request):
        try:
            filter_fields = {
                'category': request.query_params.get('category', None),
            }

            sub_categerious = UserCategoriesService.get_user_search_categories(**filter_fields)
            serializer = CategoriesSerializer(sub_categerious, many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return error_http_response(message=str(e.message))
        except Exception as e:
            return error_http_response(message=str(e))
        
class SubCategeriousRestApi(GenericAPIView):

    def get(self, request):
        try:
            filter_fields = {
                'category_id': request.query_params.get('category_id', None),
            }

            sub_categerious = UserCategoriesService.get_sub_categories(**filter_fields)
            serializer = SubCategoriesSerializer(sub_categerious, many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        except ValidationError as e:
            return error_http_response(message=str(e.message))
        except Exception as e:
            return error_http_response(message=str(e))
