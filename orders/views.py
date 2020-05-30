from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from orders.forms import RegistrationForm
from django.urls import reverse

from .models import Pizza, Pizza_name, Pizza_size, Pizza_topping, Pizza_topping_combo, Order, Order_status

# Create your views here.
def index(request):
    # if user is not authenticated than show index page with login and register links
    if not request.user.is_authenticated:
        return render(request, "orders/index.html", {"message": None})
    
    # else show user page
    
    context = {
        "pizzas": Pizza.objects.all(),
        "pizza_names": Pizza_name.objects.all(),
        "pizza_sizes": Pizza_size.objects.all(),
        "pizza_topping_combos": Pizza_topping_combo.objects.all(),
        "pizza_toppings": Pizza_topping.objects.all(),
        "cart": Order.objects.filter(user=request.user, status=1),
        "user": request.user
    }
    return render(request, "orders/user.html", context)

def register_view(request):
    
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        print (form.errors)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "orders/register.html")
    else:
        form = RegistrationForm()
        context = {
            "form": form
        }
        return render(request, "orders/register.html", context)

def login_view(request):
    if request.method =='POST':

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "orders/login.html", {"message": "Enter credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/index.html", {"message": "Logged out."})

def cart_view(request):
    
    # add check if cart is already in created, then use it or create a it
    obj, created = Order.objects.get_or_create(
        user=request.user,
        status=Order_status.objects.get(pk=1)
        )
    print ("\n", obj, "\n")

    try:
        pizza_name_id = int(request.POST["pizza_name"])
        pizza_size_id = int(request.POST["pizza_size"])
        pizza_topping_combo_id = int(request.POST["pizza_topping_combo"])

    # find pizza in BD
        pizza = Pizza.objects.get(name=pizza_name_id, size=pizza_size_id, combo=pizza_topping_combo_id)
    
    # find cart in order table
        # cart = Order.objects.get(user=request.user, status=1)
    # todo: this exception needs tuning 
    except Pizza.DoesNotExist:
        return render(request, "orders/error.html", {"message": "That Pizza Does not Exist."})
    
    obj.pizzas.add(pizza)
    return HttpResponseRedirect(reverse("index"))