from django.db import models
from users.models import GeneralUser


class Driver(GeneralUser):
    phone_number = models.IntegerField()

    def __str__(self):
        return self.username
