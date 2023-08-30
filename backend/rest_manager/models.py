from django.db import models
from users.models import GeneralUser

class RestManager(GeneralUser):
    generaluser_ptr = models.OneToOneField(
        GeneralUser,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
        default=1  # To jest wartość domyślna
    )

    
    def __str__(self):
        return self.username