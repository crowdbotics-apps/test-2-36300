from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import OneViewSet

router = DefaultRouter()
router.register("one", OneViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
