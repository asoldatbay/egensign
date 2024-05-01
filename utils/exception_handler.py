import logging

from django.http import Http404
from rest_framework import exceptions, status
from rest_framework.exceptions import APIException, PermissionDenied, NotFound
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    logger.exception(msg="e", exc_info=exc)

    response = exception_handler(exc, context)

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response_json = {
        "data": None,
        "message": exc.detail,
        "status_code": response.status_code,
    }

    return Response(data=response_json, status=response.status_code)


def raise_for_status(r):
    if r.status_code == status.HTTP_404_NOT_FOUND:
        raise NotFound("Данный ресурс не найден")

    if r.status_code == status.HTTP_403_FORBIDDEN:
        raise PermissionDenied(detail=r.json())

    if 400 <= r.status_code < 500:
        raise APIException(detail=r.json(), code=status.HTTP_400_BAD_REQUEST)
    if 500 <= r.status_code < 600:
        raise APIException(detail=r.json(), code=status.HTTP_500_INTERNAL_SERVER_ERROR)
