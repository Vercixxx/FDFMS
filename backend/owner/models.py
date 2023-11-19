from django.db import models
from users.models import GeneralUser

class Owner(GeneralUser):
    test_field = models.IntegerField()

    class Meta:
        db_table = 'Owner'
        
    def __str__(self):
        return self.username