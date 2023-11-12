from django.contrib import admin
from .models import Restaurant, WorkChange, DailyCarSchedule, Schedule, Brands

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Restaurant._meta.fields]
    filter_horizontal = ['managers']
    
@admin.register(WorkChange)
class WorkChangeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WorkChange._meta.fields]

@admin.register(DailyCarSchedule)
class DailyCarScheduleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DailyCarSchedule._meta.fields]
    filter_horizontal = ['work_changes']
    
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Schedule._meta.fields]
    filter_horizontal = ['daily_cars_schedules']
@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brands._meta.fields]