from django.db import models

# Create your models here.
class Parents(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length = 250)
    email = models.CharField(max_length = 250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

class Children(models.Model):
    children = models.ForeignKey(Parents,on_delete=models.CASCADE)
    names = models.CharField(max_length=250)
