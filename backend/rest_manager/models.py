from django.db import models
from users.models import GeneralUser

class RestManager(GeneralUser):
    test_field = models.IntegerField()
    # generaluser_ptr = models.OneToOneField(
    #     GeneralUser,
    #     on_delete=models.CASCADE,
    #     parent_link=True,
    #     primary_key=True,
    #     default=1 
    # )

    class Meta:
        db_table = 'Managers'
        
    def __str__(self):
        return self.username