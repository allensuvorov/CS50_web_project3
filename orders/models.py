from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.

# region Models: Pizza

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
        return f"Pizza: {self.name} size {self.size} with {self.combo} - {self.price}$" 

# endregion Pizza models

# region Models: Sub

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
    price = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return f"{self.add_on} - {self.price}$"

class Sub(models.Model):
    name = models.ForeignKey(Sub_name, on_delete=models.CASCADE)
    size = models.ForeignKey(Sub_size, on_delete=models.CASCADE)
    add_ons = models.ManyToManyField(Sub_add_on, blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return f"Sub: {self.name} {self.size} - {self.price}$"

# endregion Sub models

# region Models: Dinner Platter
class Dinner_platter_name(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Dinner_platter_size(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.size}"

class Dinner_platter(models.Model):

    name = models.ForeignKey(Dinner_platter_name, on_delete=models.CASCADE)
    size = models.ForeignKey(Dinner_platter_size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"Dinner Platter: {self.name} {self.size} {self.price}"
# endregion Pasta, Salad, Dinner Platter

# region Models: Pasta, Salad 
class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"Pasta: {self.name} {self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"Salad: {self.name} {self.price}"
# endregion Pasta, Salad

# region Models: Order

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
    price = models.DecimalField(max_digits=7,decimal_places=2, blank=True, null=True)
    
    # cart = models.BooleanField(default=True, blank=True)
      
    def __str__(self):
        return f"#{self.id}, NAME: {self.user}, STATUS: {self.status}, ADDRESS: {self.address}, {self.date}, {self.price}$"
        # , {self.pizzas.all()}, {self.subs.all()}"

class Pizza_order_item(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True)
    toppings = models.ManyToManyField(Pizza_topping, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="pizzas")

    def __str__(self):
        return f"{self.pizza} - {self.count} pizzas, including toppings: " + ", ".join([a.topping for a in self.toppings.all()]) #that iterates the list of values, adding commas between those values

class Sub_order_item(models.Model):
    sub = models.ForeignKey(Sub, on_delete=models.CASCADE, blank=True)
    add_ons = models.ManyToManyField(Sub_add_on, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="subs")

    def __str__(self):
        return f"{self.sub} - {self.count} subs, plus add-ons: " + ", ".join([a.add_on + "-" + str(a.price) + "$" for a in self.add_ons.all()]) 

class Pasta_order_item(models.Model):
    pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="pastas")

    def __str__(self):
        return f"{self.pasta} - {self.count} pastas"

class Salad_order_item(models.Model):
    salad = models.ForeignKey(Salad, on_delete=models.CASCADE, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="salads")

    def __str__(self):
        return f"{self.salad} - {self.count} salads"

class Dinner_platter_order_item(models.Model):
    dinner_platter = models.ForeignKey(Dinner_platter, on_delete=models.CASCADE, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="dinner_platters")

    def __str__(self):
        return f"{self.dinner_platter} - {self.count} dinner platters"

# endregion Order