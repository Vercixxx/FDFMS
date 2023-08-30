from django.db import models
from restaurant.models import Restaurant
from car.models import Car


class Fleet(models.Model):
    id = models.IntegerField(primary_key=True)
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
    cars = models.ManyToManyField(Car, blank=True)
