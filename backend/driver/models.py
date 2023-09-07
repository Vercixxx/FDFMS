from django.db import models
from users.models import GeneralUser


from datetime import datetime

class Driver(GeneralUser):
    phone_number123 = models.IntegerField()

    class Meta:
        db_table = 'Drivers'

    def __str__(self):
        return self.username


class DailyWork(models.Model):
    user = models.ForeignKey(Driver, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_work = models.TimeField()
    end_work = models.TimeField()
    orders = models.IntegerField(default=0)
    working_time = models.CharField(max_length=5, blank=True)
    
    def save(self, *args, **kwargs):
        if self.start_work and self.end_work:
            start_datetime = datetime.combine(datetime.today(), self.start_work)
            end_datetime = datetime.combine(datetime.today(), self.end_work)
            time_difference = end_datetime - start_datetime
            hours = time_difference.seconds // 3600
            minutes = (time_difference.seconds // 60) % 60
            self.working_time = f"{hours:02}:{minutes:02}"
        super(DailyWork, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"Start Work: {self.start_work}, End Work: {self.end_work}, Orders: {self.orders}, Working Time: {self.working_time()}"