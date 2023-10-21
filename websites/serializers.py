from rest_framework import serializers
from .models import DinnerOption

class DinnerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DinnerOption
        fields = ['id', 'name', 'votes']
