from django.contrib import admin
from api.models import Regions
from api.models import Fruits

admin.site.register(Regions) # Add Regions model to admin page
admin.site.register(Fruits) # Add fruits model to admin page
