from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


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
    count = models.IntegerField()
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
    # toppings = models.ManyToManyField(Pizza_topping, blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"pizza {self.name} size {self.size} with {self.combo} - {self.price} dollars" 

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

# region Pasta, Salad, Dinner Platter
class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.price}"

class Dinner_platter(models.Model):

    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.price}"
# endregion Pasta, Salad, Dinner Platter

# region Order

class Order_status(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        blank=True
        )
    status = models.ForeignKey(Order_status, on_delete=models.CASCADE, blank=True)

    address = models.CharField(max_length=64, blank=True)
    date = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=7,decimal_places=2, blank=True)
    
    # cart = models.BooleanField(default=True, blank=True)
      
    def __str__(self):
        return f"#{self.id}, NAME: {self.user}, STATUS: {self.status}, ADDRESS: {self.address}"
        # , {self.pizzas.all()}, {self.subs.all()}"

class Pizza_order_item(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True, )
    toppings = models.ManyToManyField(Pizza_topping, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="pizzas")

    def __str__(self):
        return f"{self.pizza} - {self.count} pizzas, with toppings: " + ", ".join([a.topping for a in self.toppings.all()]) #


# endregion Order