from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

route = routers.DefaultRouter()


route.register('regions', views.RegionsViewSets, basename='Regions')
route.register('fruits', views.FruitsViewSets, basename='Fruits')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('api/', include(route.urls)),
]
