from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    about = models.TextField()

    def __str__(self):
        return "El usuario activo es "+ self.username