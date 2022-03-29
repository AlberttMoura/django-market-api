from rest_framework import serializers
from api import models

# Parse the models' data

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Regions
        fields = '__all__'

class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fruits
        fields = '__all__'