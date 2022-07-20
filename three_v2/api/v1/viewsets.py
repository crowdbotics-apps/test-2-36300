from rest_framework import authentication
from three_v2.models import Three_v2
from .serializers import Three_v2Serializer
from rest_framework import viewsets


class Three_v2ViewSet(viewsets.ModelViewSet):
    serializer_class = Three_v2Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Three_v2.objects.all()
