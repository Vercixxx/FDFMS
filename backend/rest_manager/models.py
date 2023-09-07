from django.db import models
from users.models import GeneralUser

class RestManager(GeneralUser):
    test_field = models.IntegerField()

    class Meta:
        db_table = 'Managers'
        
    def __str__(self):
        return self.username