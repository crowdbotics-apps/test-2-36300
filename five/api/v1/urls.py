from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FiveViewSet

router = DefaultRouter()
router.register("five", FiveViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
