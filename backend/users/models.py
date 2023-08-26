from django.db import models
from django.contrib.auth.models import AbstractUser

class GeneralUser(AbstractUser):

    # User rank
    ROLE_CHOICES = (
        ('Error', 'Error'),
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
        default='Error'
    )
    
    def __str__(self):
        return self.username