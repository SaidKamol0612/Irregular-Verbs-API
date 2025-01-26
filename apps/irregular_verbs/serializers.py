from rest_framework import serializers
from .models import IrregularVerb

class IrregularVerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrregularVerb
        fields = '__all__'