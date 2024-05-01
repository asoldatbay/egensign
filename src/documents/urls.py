from django.urls import path, include
from rest_framework.routers import DefaultRouter

from documents.views.generate import GenerateViewSet

router = DefaultRouter()
router.register(r"generate", GenerateViewSet, "generate")

urlpatterns = [
    path("", include(router.urls)),
]
