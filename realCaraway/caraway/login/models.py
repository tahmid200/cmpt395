from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# creates a custom user model
class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    #children1 = models.CharField(max_length=255)
    #children2 = models.CharField(max_length=255)

#class ClassCreation(models.Model):
 #   classroom = models.CharField(max_length=255)

class ParentCreation(models.Model):
    username = models.CharField(max_length=254, blank=True)
    email = models.EmailField(blank=True, unique=True)
    password2 = models.CharField(max_length=254, blank=True)
    children1 = models.CharField(max_length=255, blank=True)
    children2 = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

