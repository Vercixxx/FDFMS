from django.db import models
from users.models import GeneralUser


class Driver(GeneralUser):
    license_number = models.CharField(max_length=50, blank=True, null=True)
    ln_release_date = models.DateField(max_length=50, blank=True, null=True)
    ln_expire_date = models.DateField(max_length=50, blank=True, null=True)
    ln_published_by = models.CharField(max_length=70, blank=True, null=True)
    ln_code = models.CharField(max_length=15, blank=True, null=True)
    

    class Meta:
        db_table = 'Drivers'

    def __str__(self):
        return self.username


class DailyWork(models.Model):
    driver = models.ForeignKey(Driver, db_column='driver', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    orders = models.IntegerField(default=0)
    start_work = models.TimeField()
    end_work = models.TimeField()
    working_time = models.TimeField()
        
    class Meta:
        db_table = 'DailyWorkReports'