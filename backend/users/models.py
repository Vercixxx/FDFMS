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
        default='Administrator'
    )
    
    phone = models.CharField(max_length=25, blank=True, null=True)
    
    # Country Choices
    COUNTRY_CHOICES = (
        ('Poland', 'Poland'),
        )
    
    POLAND_STATE_CHOICES = (
        ('Mazowieckie', 'Mazowieckie'),
        ('Małopolskie', 'Małopolskie'),
        ('Wielkopolskie', 'Wielkopolskie'),
        ('Dolnośląskie', 'Dolnośląskie'),
        ('Kujawsko-Pomorskie', 'Kujawsko-Pomorskie'),
        ('Lubelskie', 'Lubelskie'),
        ('Lubuskie', 'Lubuskie'),
        ('Łódzkie', 'Łódzkie'),
        ('Opolskie', 'Opolskie'),
        ('Podkarpackie', 'Podkarpackie'),
        ('Podlaskie', 'Podlaskie'),
        ('Pomorskie', 'Pomorskie'),
        ('Śląskie', 'Śląskie'),
        ('Świętokrzyskie', 'Warmińsko-Mazurskie'),
        ('Warmińsko-Mazurskie', 'Śląskie'),
        ('Zachodniopomorskie', 'Zachodniopomorskie'),
    )
    
    
    #address of residence
    residence_country = models.CharField(max_length=100, blank=True, null=True)
    residence_city = models.CharField(max_length=100, blank=True, null=True)
    residence_state = models.CharField(max_length=100, blank=True, null=True)
    residence_street = models.CharField(max_length=200, blank=True, null=True)
    residence_home_number = models.CharField(max_length=10, blank=True, null=True)
    residence_apartament_number = models.CharField(max_length=10, blank=True, null=True)
    residence_zip_code = models.CharField(max_length=10, blank=True, null=True)
    
    
    # Adress of registered
    registered_country = models.CharField(max_length=100, blank=True, null=True)
    registered_city = models.CharField(max_length=100, blank=True, null=True)
    registered_state = models.CharField(max_length=100, blank=True, null=True)
    registered_street = models.CharField(max_length=200, blank=True, null=True)
    registered_home_number = models.CharField(max_length=10, blank=True, null=True)
    registered_apartament_number = models.CharField(max_length=10, blank=True, null=True)
    registered_zip_code = models.CharField(max_length=10, blank=True, null=True)
    
    # Adress of correspondence
    correspondence_country = models.CharField(max_length=100, blank=True, null=True)
    correspondence_city = models.CharField(max_length=100, blank=True, null=True)
    correspondence_state = models.CharField(max_length=100, blank=True, null=True)
    correspondence_street = models.CharField(max_length=200, blank=True, null=True)
    correspondence_home_number = models.CharField(max_length=10, blank=True, null=True)
    correspondence_apartament_number = models.CharField(max_length=10, blank=True, null=True)
    correspondence_zip_code = models.CharField(max_length=10, blank=True, null=True)
    
    bank_account_number = models.CharField(max_length=30, blank=True, null=True)
    pesel_nip = models.CharField(max_length=12, blank=True, null=True)
    tax_office_name = models.CharField(max_length=80, blank=True, null=True)
    tax_office_address = models.CharField(max_length=220, blank=True, null=True)

    nfz = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.username