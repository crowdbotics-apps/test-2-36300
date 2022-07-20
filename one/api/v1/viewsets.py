from rest_framework import authentication
from one.models import One
from .serializers import OneSerializer
from rest_framework import viewsets


class OneViewSet(viewsets.ModelViewSet):
    serializer_class = OneSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = One.objects.all()
