from django.urls import path, include
from rest_framework.routers import DefaultRouter

from templates.views.templates import TemplatesViewSet

router = DefaultRouter()
router.register(r"", TemplatesViewSet, "templates")

urlpatterns = [
    path("", include(router.urls)),
]
