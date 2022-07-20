from rest_framework import authentication
from five_v2.models import Five_v2
from .serializers import Five_v2Serializer
from rest_framework import viewsets


class Five_v2ViewSet(viewsets.ModelViewSet):
    serializer_class = Five_v2Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Five_v2.objects.all()
