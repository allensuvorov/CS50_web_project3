from django.db import models

# Create your models here.
class Pizza_name(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    name = models.ForeignKey(Pizza_name, on_delete=models.CASCADE)
    size = models.CharField(max_length=64)
    topping = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.id} - pizza {self.name} size {self.size} with {self.topping} is {self.price} dollars" 
