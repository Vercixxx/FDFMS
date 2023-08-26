from django.contrib import admin

from .models import GeneralUser
from .forms import GeneralUserAdminConf


class GeneralUserAdmin(admin.ModelAdmin):
    form = GeneralUserAdminConf
    list_display = ['username', 'user_role', 'is_active']
    
admin.site.register(GeneralUser, GeneralUserAdmin)