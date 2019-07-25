from rest_framework import serializers
from .models import Xue

class XueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'responses',
            'properties',
        )
        model = Xue