from rest_framework import serializers
from one.models import One


class OneSerializer(serializers.ModelSerializer):
    class Meta:
        model = One
        fields = "__all__"
