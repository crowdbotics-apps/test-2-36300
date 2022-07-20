from rest_framework import authentication
from five.models import Five
from .serializers import FiveSerializer
from rest_framework import viewsets


class FiveViewSet(viewsets.ModelViewSet):
    serializer_class = FiveSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Five.objects.all()
