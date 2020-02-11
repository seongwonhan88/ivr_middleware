from rest_framework import status
from rest_framework.exceptions import APIException


class RequestWithoutData(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = {'error': 'POST request received without data. Please include data into request body'}


class MissingCreditCardNumber(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = {'error': 'cc_num value is missing'}


class MissingCVV(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = {'error': 'cvv value is missing'}


class InvalidCVV(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = {'error': 'cvv can only be either 3 or 4 digit value'}
