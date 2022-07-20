from rest_framework import serializers
from five_v2.models import Five_v2


class Five_v2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Five_v2
        fields = "__all__"
