from django.db import models
from rest_manager.models import RestManager

class Restaurant(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    managers = models.ManyToManyField(RestManager, blank=True)
