from rest_framework import serializers
from .models import Xue, Yao, Cases

class XueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'responses',
            'properties',
        )
        model = Xue


class YaoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'responses',
            'properties',
        )
        model = Yao

class CasesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'facts',
            'marks',
            'symptom',
            'solution',
            'reference',
        )
        model = Cases


