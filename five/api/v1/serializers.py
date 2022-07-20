from rest_framework import serializers
from five.models import Five


class FiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Five
        fields = "__all__"
