from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    topping = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=3,decimal_places=2)
