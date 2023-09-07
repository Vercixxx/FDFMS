from django.db import models
from users.models import GeneralUser

class AssetUser(GeneralUser):
    test_field = models.IntegerField()

    class Meta:
        db_table = 'AssetsUsers'
        
    def __str__(self):
        return self.username