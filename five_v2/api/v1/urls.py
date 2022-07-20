from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Five_v2ViewSet

router = DefaultRouter()
router.register("five_v2", Five_v2ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
