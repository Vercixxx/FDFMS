from django.db import models
from django.utils import timezone

from driver.models import Driver

class Car(models.Model):

    vin = models.TextField(max_length=17, primary_key = True)
    
    # license_plate = models.TextField(max_length=10, unique=True)
    
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
        
class DriverCar(models.Model):
    date =  models.DateTimeField(null=True)
    
    driver = models.ForeignKey(Driver, db_column='driver', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, db_column='car', on_delete=models.CASCADE)
    
    car_mileage = models.IntegerField(null=True)
    
    car_condition_options = (
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Bad', 'Bad'),
        )
    
    car_condition = models.CharField(
        max_length=20,
        choices=car_condition_options,
        default='Good'
    )
    
    how_clean_is_car_options = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),

        )
    
    car_cleanliness = models.CharField(
        max_length=5,
        choices=how_clean_is_car_options,
        default='5'
    )
    
    additional_remarks = models.TextField(null=True)
    
    def formatted_date(self):
        return self.date.strftime('%d:%m:%Y:%H:%M') if self.date else ""

    def save(self, *args, **kwargs):
        if self.formatted_date():
            self.date = timezone.datetime.strptime(self.formatted_date(), '%d:%m:%Y:%H:%M')
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.date, self.car, self.car_mileage
    class Meta:
        db_table = 'DD_report'