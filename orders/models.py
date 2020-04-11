from django.db import models

# Create your models here.

# region Pizza models

class Pizza_name(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Pizza_size(models.Model):
    size = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.size}"

class Pizza_topping_combo(models.Model):
    combo = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.combo}"

class Pizza_topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"

class Pizza(models.Model):
    name = models.ForeignKey(Pizza_name, on_delete=models.CASCADE)
    size = models.ForeignKey(Pizza_size, on_delete=models.CASCADE)
    combo = models.ForeignKey(Pizza_topping_combo, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Pizza_topping, blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.id} - pizza {self.name} size {self.size} with {self.combo} - {self.price} dollars" 

# endregion Pizza models

# region Sub models

class Sub_name(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Sub_size(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.size}"

class Sub_add_on(models.Model):
    add_on = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.add_on}"

class Sub(models.Model):
    name = models.ForeignKey(Sub_name, on_delete=models.CASCADE)
    size = models.ForeignKey(Sub_size, on_delete=models.CASCADE)
    add_ons = models.ManyToManyField(Sub_add_on, blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return f"{self.name} {self.size} - {self.price} dollars"

# endregion Sub models
