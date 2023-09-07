from django.db import models
from users.models import GeneralUser

class ClientsUser(GeneralUser):
    test_field = models.IntegerField()

    class Meta:
        db_table = 'ClientsUsers'
        
    def __str__(self):
        return self.username