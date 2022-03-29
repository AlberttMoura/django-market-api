from rest_framework import viewsets
from api import serializers
from api import models

class RegionsViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.RegionsSerializer
    queryset = models.Regions.objects.all()

class FruitsViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.FruitsSerializer
    queryset = models.Fruits.objects.all()