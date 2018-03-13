from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db import models

# creates a custom user model
class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()

class ClassCreation(models.Model):
    classroom = models.CharField(max_length=255)

