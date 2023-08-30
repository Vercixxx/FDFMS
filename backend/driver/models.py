from django.db import models
from users.models import GeneralUser


class Driver(GeneralUser):
    phone_number123 = models.IntegerField()

    class Meta:
        db_table = 'Drivers'

    def __str__(self):
        return self.username
