from django.contrib import admin
from .models import Owner

@admin.register(Owner)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_role', 'is_active']
