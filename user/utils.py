from rest_framework import status
from rest_framework.response import Response
import random
# from .models import UserProfile
def error_http_response(
        message,
        status_code=status.HTTP_400_BAD_REQUEST,
):
    json_dict = {
        "message": message,
        "code": status_code
    }

    return Response(json_dict, content_type='application/problem+json', status=status_code)


def success_http_response(
        message,
        status_code=status.HTTP_200_OK,
):
    message["code"] = status_code if message else ""

    return Response(message, content_type='application/json', status=status_code)


from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # Allow client to override, using `?page_size=xxx`.
    max_page_size = 1000  # Maximum limit allowed when using `?page_size=xxx`.





def create_new_ref_number():
    return str(random.randint(1000000000, 9999999999))



# def create_new_ref_number():
#     not_unique = True
#     while not_unique:
#         unique_ref = random.randint(1000000000, 9999999999)
#         if not UserProfile.objects.filter(user_id=unique_ref):
#             not_unique = False
#     return str(unique_ref)