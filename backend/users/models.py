from django.db import models
from django.contrib.auth.models import AbstractUser

class GeneralUser(AbstractUser):

    # User rank
    ROLE_CHOICES = (
        ('Owner', 'Owner'),
        ('HR', 'HR'),
        ('Payroll', 'Payroll'),
        ('Asset', 'Asset'),
        ('Clients', 'Clients'),
        ('Manager', 'Manager'),
        ('Driver', 'Driver'),
        ('Administrator', 'Administrator'),
        )
    
    user_role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Driver'
    )
    
    
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    home_number = models.CharField(max_length=10, blank=True, null=True)
    apartament_number = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.username