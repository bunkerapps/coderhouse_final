from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to='user_images/', null=True, blank=True)
    about = models.TextField(null=False, blank=False)

    def __str__(self):
        return "El usuario activo es "+ self.username