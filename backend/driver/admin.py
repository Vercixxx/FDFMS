from django.contrib import admin
from .models import Driver, DailyWork

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass

@admin.register(DailyWork)
class DailyWorkAdmin(admin.ModelAdmin):
    pass
    