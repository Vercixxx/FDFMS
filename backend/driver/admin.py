from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_role', 'is_active']
