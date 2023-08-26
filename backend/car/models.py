from django.db import models
from django.utils import timezone

class Car(models.Model):
    vin = models.TextField(primary_key=True, max_length=17)
    
    brand = models.TextField()
    model = models.TextField()
    
    # Year of production
    YEAR_CHOICES = [(r, r) for r in range(1990, timezone.now().year+1)]
    year_of_prod = models.PositiveIntegerField(choices=YEAR_CHOICES, default=timezone.now().year)
    # Year of production
    
    color = models.TextField()
    mileage = models.IntegerField(default=0)
    engine_cap = models.FloatField()
    engine_pow = models.IntegerField()
    
    # Transmission 
    transmission_choices = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic')
        )
    
    transmission = models.CharField(
        max_length=20,
        choices=transmission_choices,
        default='Manual'
    )
    # Transmission 
    
    policy_number = models.TextField()
    is_oc = models.BooleanField()
    is_ac = models.BooleanField()
    phone_policy_contact = models.IntegerField()
    
    
    
    def __str__(self):
        return self.vin
    class Meta:
        db_table = 'Cars'
    