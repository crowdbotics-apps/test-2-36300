from rest_framework import serializers
from three_v2.models import Three_v2


class Three_v2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Three_v2
        fields = "__all__"
