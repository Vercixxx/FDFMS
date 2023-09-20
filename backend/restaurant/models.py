from django.db import models
from rest_manager.models import RestManager
from driver.models import Driver
from car.models import Car

from datetime import datetime


class Restaurant(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    managers = models.ManyToManyField(RestManager, blank=True)
    
    phone = models.CharField(max_length=25, blank=True, null=True)

    #address 
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    home_number = models.CharField(max_length=10, blank=True, null=True)
    apartament_number = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)

class WorkChange(models.Model):
    time_start = models.CharField(max_length=5)
    time_end = models.CharField(max_length=5)
    
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, default=None)
    
    
class DailyCarSchedule(models.Model):
    date = models.DateTimeField()
    
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    work_changes = models.ManyToManyField(WorkChange, blank=True)
    


class Schedule(models.Model):
    date = models.DateTimeField()
    daily_cars_schedules = models.ManyToManyField(DailyCarSchedule, blank=True)

    
    
    