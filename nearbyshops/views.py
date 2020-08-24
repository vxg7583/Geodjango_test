from django.shortcuts import render
from .models import Shop
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
# Create your views here.

latitude = 47.611080
longitude = -122.329790

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    queryset = Shop.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:10]
    template_name = "shops/index.html"
    
