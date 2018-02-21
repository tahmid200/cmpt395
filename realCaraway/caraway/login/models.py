from django.contrib.auth.models import AbstractUser, UserManager

# creates a custom user model
class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()