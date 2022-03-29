from statistics import mode
from tabnanny import verbose
from django.db import models

class Regions(models.Model):
    name = models.CharField(primary_key=True, max_length=128) # Defines Regions' name as PK

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Regions"


class Fruits(models.Model):
    name = models.CharField(primary_key=True, max_length=128) # Defines Fruits' name as PK
    region = models.ForeignKey(Regions, on_delete=models.CASCADE) # Defines a FK from Regions and cascade effect in case of the Region being deleted

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Fruits"
