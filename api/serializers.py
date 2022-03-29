from dataclasses import field
from rest_framework import serializers
from api import models

class RegionsSerializer(serializers.models.ModelSerializer):
    class Meta:
        model = models.Regions
        fields = '__all__'

class FruitsSerializer(serializers.models.ModelSerializer):
    class Meta:
        model = models.Fruits
        fields = '__all__'