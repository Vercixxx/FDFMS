from django.db import models
from users.models import GeneralUser

class Administrator(GeneralUser):
    test_field = models.IntegerField()

    class Meta:
        db_table = 'Administrators'
        
    def __str__(self):
        return self.username