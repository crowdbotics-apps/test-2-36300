from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Three_v2ViewSet

router = DefaultRouter()
router.register("three_v2", Three_v2ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
