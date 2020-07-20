from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.

# region Models: Pizza

class PizzaName(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class PizzaSize(models.Model):
    size = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.size}"

class PizzaToppingCombo(models.Model):
    combo = models.CharField(max_length=64)
    count = models.IntegerField()
    def __str__(self):
        return f"{self.combo}"

class PizzaTopping(models.Model):
    topping = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.topping}"

class Pizza(models.Model):
    name = models.ForeignKey(PizzaName, on_delete=models.CASCADE)
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    combo = models.ForeignKey(PizzaToppingCombo, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"Pizza: {self.name} size {self.size} with {self.combo} - {self.price}$" 

# endregion Pizza models

# region Models: Sub

class SubName(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class SubSize(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.size}"

class SubAddOn(models.Model):
    add_on = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return f"{self.add_on} - {self.price}$"

class Sub(models.Model):
    name = models.ForeignKey(SubName, on_delete=models.CASCADE)
    size = models.ForeignKey(SubSize, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return f"Sub: {self.name} {self.size} - {self.price}$"

# endregion Sub models

# region Models: Dinner Platter
class DinnerPlatterName(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class DinnerPlatterSize(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.size}"

class DinnerPlatter(models.Model):

    name = models.ForeignKey(DinnerPlatterName, on_delete=models.CASCADE)
    size = models.ForeignKey(DinnerPlatterSize, on_delete=models.CASCADE)
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

class OrderStatus(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        blank=True
        )
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, blank=True)

    address = models.CharField(max_length=64, blank=True)
    date = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=7,decimal_places=2, blank=True, null=True)
      
    def __str__(self):
        return f"#{self.id}, NAME: {self.user}, STATUS: {self.status}, ADDRESS: {self.address}, {self.date}, {self.price}$"
        # , {self.pizzas.all()}, {self.subs.all()}"

class PizzaOrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True)
    toppings = models.ManyToManyField(PizzaTopping, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="pizzas")

    def __str__(self):
        return f"{self.pizza} - {self.count} pizzas, including toppings: " + ", ".join([a.topping for a in self.toppings.all()]) #that iterates the list of values, adding commas between those values

class SubOrderItem(models.Model):
    sub = models.ForeignKey(Sub, on_delete=models.CASCADE, blank=True)
    add_ons = models.ManyToManyField(SubAddOn, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="subs")

    def __str__(self):
        return f"{self.sub} - {self.count} subs, plus add-ons: " + ", ".join([a.add_on + "-" + str(a.price) + "$" for a in self.add_ons.all()]) 

class PastaOrderItem(models.Model):
    pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="pastas")

    def __str__(self):
        return f"{self.pasta} - {self.count} pastas"

class SaladOrderItem(models.Model):
    salad = models.ForeignKey(Salad, on_delete=models.CASCADE, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="salads")

    def __str__(self):
        return f"{self.salad} - {self.count} salads"

class DinnerPlatterOrderItem(models.Model):
    dinner_platter = models.ForeignKey(DinnerPlatter, on_delete=models.CASCADE, blank=True)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="dinner_platters")

    def __str__(self):
        return f"{self.dinner_platter} - {self.count} dinner platters"

# endregion Order