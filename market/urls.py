from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

route = routers.DefaultRouter() # A router object to handle the API endpoints


route.register('regions', views.RegionsViewSets, basename='Regions') # Endpoint for Regions
route.register('fruits', views.FruitsViewSets, basename='Fruits') # Endpoint for Fruits

urlpatterns = [
    path('admin/', admin.site.urls), # Default Admin endpoint
    path('api/', include(route.urls)), # Uses the endpoints
]
