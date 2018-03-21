from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# creates a custom user model
class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()

#--------------------------------------------------------------------------
class ParentCreation(models.Model):
    username = models.CharField(max_length=254)
    email = models.EmailField(max_length = 254)
    password2 = models.CharField(max_length=254)
    children1 = models.CharField(max_length=255)
    children2 = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    curent_hours = models.IntegerField(default=0)
    monthly_hours = models.IntegerField(default=0)
    total_hours = models.IntegerField(default=0)
#-----------------------------------------------------------------------------