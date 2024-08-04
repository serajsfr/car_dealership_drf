from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    