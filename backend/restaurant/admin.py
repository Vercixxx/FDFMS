from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Restaurant._meta.fields]
    list_filter = ['city', 'country']
    search_fields = ['name', 'city', 'country']
    filter_horizontal = ['managers']