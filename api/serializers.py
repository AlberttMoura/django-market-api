from dataclasses import field
from rest_framework import serializers
from api import models

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Regions
        fields = '__all__'

class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fruits
        fields = '__all__'