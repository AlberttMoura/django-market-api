from rest_framework import viewsets
from api import serializers
from api import models

# Render the models' data

class RegionsViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.RegionsSerializer # Uses the Regions Serializer
    queryset = models.Regions.objects.all() # Shows all Regions from Regions Table

class FruitsViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.FruitsSerializer # Uses the Fruits Serializer
    queryset = models.Fruits.objects.all() # Shows all Fruits from Fruits Table