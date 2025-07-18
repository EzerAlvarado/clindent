from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    
    clave = models.CharField(max_length=20, unique=True, null=True, blank=True)

    puede_editar = models.BooleanField(default=False)

    def __str__(self):
        return self.username