from django.contrib import admin

from .models import Car, CarDailyReports

admin.site.register(Car)
admin.site.register(CarDailyReports)

