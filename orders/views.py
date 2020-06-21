from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from orders.forms import RegistrationForm
from django.urls import reverse

from .models import Pizza, Pizza_name, Pizza_size, Pizza_topping, Pizza_topping_combo, Order, Order_status, Pizza_order_item

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
        pizza_count = int(request.POST["count"])
        
    
    # find pizza in BD
        pizza = Pizza.objects.get(name=pizza_name_id, size=pizza_size_id, combo=pizza_topping_combo_id)
    
    # find cart in order table
        # cart = Order.objects.get(user=request.user, status=1)
    # todo: this exception needs tuning 
    except Pizza.DoesNotExist:
        return render(request, "orders/error.html", {"message": "That Pizza Does not Exist."})
    

    # obj.pizzas.add(pizza)
    pizza_order = Pizza_order_item(pizza=pizza, count=pizza_count, order=obj)
    pizza_order.save()

    # get all toppings
    pizza_toppings = request.POST.getlist("pizza_toppings")
    print ("\n", pizza_toppings, "\n")
    
    if pizza_toppings is not None:
        for topping in pizza_toppings:
            pizza_order.toppings.add(topping)

    return HttpResponseRedirect(reverse("index"))

def price_view(request):
    print ("\n","trying to get price", "\n")
    if request.is_ajax and request.method == "GET":
        # get data name from the client side.
        print ("\n", "AJAX GET", "\n")

        pizza_name_id = int(request.GET["pizza_name"])
        pizza_size_id = int(request.GET["pizza_size"])
        pizza_topping_combo_id = int(request.GET["pizza_topping_combo"])
        # pizza_count = int(request.GET["count"])
        
        print ("\n", pizza_name_id, "\n")


    try:
    #     pizza_name_id = request.GET.get("pizza_name", None)
        
    #     # pizza_name_id = request.GET['pizza_name']
    #     print ("\n", pizza_name_id, "\n")
    #     # pizza_name_id = int(request.GET.get("pizza_name"))
    #     # pizza_size_id = int(request.GET["pizza_size"])
    #     # pizza_topping_combo_id = int(request.GET["pizza_topping_combo"])
    #     # pizza_count = int(request.GET["count"])

        pizza = Pizza.objects.get(name=pizza_name_id, size=pizza_size_id, combo=pizza_topping_combo_id)
        price = pizza.price

    except Pizza.DoesNotExist:
        return JsonResponse ({'message': 'product not in menu'})
    
    print ("\n", price, "\n")

    return JsonResponse ({'price': price})
