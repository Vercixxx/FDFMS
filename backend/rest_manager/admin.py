from django.contrib import admin
from .models import RestManager

@admin.register(RestManager)
class RestManagerAdmin(admin.ModelAdmin):
    list_display = ['username', 'generaluser_ptr']
