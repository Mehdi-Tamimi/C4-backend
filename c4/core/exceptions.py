from rest_framework.exceptions import APIException
from rest_framework import status


class ParticipationExistsException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "قبلا در این پروژه شرکت کرده اید"

class ParticipationOwnerException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "شما مالک این عضویت نیستید"